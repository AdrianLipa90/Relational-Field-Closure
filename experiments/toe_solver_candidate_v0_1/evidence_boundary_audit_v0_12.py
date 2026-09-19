from __future__ import annotations
import importlib.util, json, hashlib, math, sys
from pathlib import Path
import numpy as np

HERE=Path(__file__).resolve().parent
EXPECTED_SP3_SOURCE_SHA="e6c18e85a6f2b62c6820258b7ecfc514f8a177f1c2eaff54d6a5ff0b8fab2399"
EXPECTED_SPATIAL_DERIVATION="DETERMINISTIC_RELATIONAL_BOUNDARY_CLOSURE_FROM_OBSERVED_NODE_SET"

def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path); mod=importlib.util.module_from_spec(spec); sys.modules[name]=mod; spec.loader.exec_module(mod); return mod

def canon(o): return json.dumps(o,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()
def sha(o): return hashlib.sha256(canon(o)).hexdigest()

def run(sp3_path=None,rindler_path=None):
    if sp3_path is None: sp3_path=HERE/'igs_sp3_observational_e2e_v0_11.py'
    if rindler_path is None: rindler_path=HERE/'empirical_rindler_bounded_e2e_v0_11.py'
    sp3=load('sp3_v011',Path(sp3_path)); rin=load('rin_v011',Path(rindler_path))
    o=sp3.run(); rr=rin.run_e2e()
    source_sha=o['source_extract_sha256']; spatial=o['spatial']['capture']; matching=o['matching']
    sats=tuple(o['source']['satellites'])
    expected_tets=sorted(tuple(sorted(s for s in sats if s!=om)) for om in sats)
    actual_tets=sorted(tuple(sorted(c['vertices'])) for c in spatial['tetrahedral_cells'])
    topology_constructed=(actual_tets==expected_tets and spatial['source'].get('derivation_class')==EXPECTED_SPATIAL_DERIVATION)
    bet={p['patch_id']:np.asarray(p['beta_match'],float) for p in matching['patches']}
    matching_constructed=True
    for edge in matching['overlaps']:
        A=np.asarray(edge['spatial_jacobian'],float); v=np.asarray(edge['time_drift'],float)
        if not np.array_equal(A,np.eye(3)) or not np.allclose(v,bet[edge['source']]-bet[edge['target']],rtol=0,atol=1e-15):
            matching_constructed=False
    hist_prod=(spatial['source'].get('source_class')=='PRODUCTION_SOURCE')
    same_id=(o['clock']['physical_realization_id']==spatial['physical_realization_id']==matching['physical_realization_id'])
    checks={
      'sp3_archive_digest_reproducible': source_sha==EXPECTED_SP3_SOURCE_SHA,
      'sp3_model_level_claim_firewall': o['evidence_class']=='EXTERNAL_OBSERVATIONAL_ARCHIVE_DERIVED_MODEL_LEVEL' and o['physical_production_claim'] is False and o['canon_allowed'] is False,
      'historical_spatial_production_overclassification_detected': hist_prod and topology_constructed,
      'spatial_topology_is_model_derived_control': topology_constructed and o['spatial']['manifold_certified'] is True,
      'matching_A_v_are_constructed_consistency_control': matching_constructed and matching['max_matching_residual']<1e-15,
      'same_id_reclassified_as_provenance_consistency': same_id,
      'rindler_independent_empirical_null_control_pass': rr['evidence_class']=='EXTERNAL_EMPIRICAL_RINDLER_CALIBRATED_REFERENCE' and rr['rindler']['max_abs_einstein']==0.0 and rr['rf_e26_reference']['global_einstein_carrier'] is True,
      'independent_archive_sources_present': o['source']['source_url']!=rr['source']['doi'],
      'no_physical_or_canon_promotion': rr['physical_production_claim'] is False and rr['canon_allowed'] is False and o['physical_production_claim'] is False and o['canon_allowed'] is False,
    }
    status='PASS' if all(checks.values()) else 'FAIL'
    out={
      'schema':'QHTRI_TOE_EVIDENCE_BOUNDARY_AUDIT_V0_12','status':status,'authority':'CANDIDATE_ONLY','canon_allowed':False,'physical_production_claim':False,
      'checks':checks,'sp3_source_extract_sha256':source_sha,
      'historical_v011_preserved':True,
      'evidence_reclassification':{
        'sp3_clock':'EXTERNAL_OBSERVATIONAL_ARCHIVE_DERIVED_CLOCK_CONTROL',
        'sp3_topology':'MODEL_DERIVED_TOPOLOGY_CONTROL_NOT_PRODUCTION_SOURCE',
        'sp3_matching':'MODEL_DERIVED_KINEMATIC_CONSISTENCY_CONTROL',
        'sp3_metric':'MODEL_FIT_FROM_ARCHIVE_DERIVED_FIELDS',
        'sp3_bianchi':'NUMERICAL_COVARIANT_IDENTITY_VALIDATION_ON_MODEL_FIT',
        'sp3_same_id':'SOURCE_PROVENANCE_CONSISTENCY_NOT_INDEPENDENT_PHYSICAL_REALIZATION_PROOF',
        'rindler':'INDEPENDENT_EXTERNAL_EMPIRICAL_CALIBRATED_FLAT_NULL_CONTROL'
      },
      'repo_completion_scope':'IMPLEMENTATION_AND_REFERENCE_VALIDATION_COMPLETE',
      'empirical_theory_confirmation':False,
      'note':'v0.12 repairs evidence typing only. It preserves v0.11 calculations and receipts while preventing a model-derived tetrahedral closure or constructed matching identity from being treated as an independent production-source measurement.'
    }
    out['receipt_sha256']=sha(out); return out

if __name__=='__main__':
    import argparse
    ap=argparse.ArgumentParser(); ap.add_argument('--sp3'); ap.add_argument('--rindler'); a=ap.parse_args(); r=run(a.sp3,a.rindler); print(json.dumps(r,indent=2,sort_keys=True)); raise SystemExit(0 if r['status']=='PASS' else 1)
