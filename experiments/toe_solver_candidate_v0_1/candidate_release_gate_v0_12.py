from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
EXPECTED_SOURCE_SHA="e6c18e85a6f2b62c6820258b7ecfc514f8a177f1c2eaff54d6a5ff0b8fab2399"

def sha(o): return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
def read(p): return json.loads(Path(p).read_text())

def run(audit_path,sp3_validation_path,sp3_adversarial_path,rindler_path,retained_fail_path,loader_fail_path=None):
    audit=read(audit_path); val=read(sp3_validation_path); adv=read(sp3_adversarial_path); rin=read(rindler_path); fail=read(retained_fail_path)
    loader=None if loader_fail_path is None else read(loader_fail_path)
    checks={
      'evidence_boundary_audit_pass': audit.get('status')=='PASS' and all(audit.get('checks',{}).values()),
      'sp3_observational_model_validation_pass': val.get('status')=='PASS' and len(val.get('checks',{}))==7 and all(val.get('checks',{}).values()),
      'sp3_source_digest_stable': val.get('source_extract_sha256')==EXPECTED_SOURCE_SHA==audit.get('sp3_source_extract_sha256'),
      'sp3_adversarial_5_of_5_pass': adv.get('status')=='PASS' and adv.get('passed')==5 and adv.get('failed')==0,
      'independent_rindler_10_of_10_pass': rin.get('status')=='PASS' and rin.get('passed')==10 and rin.get('failed')==0,
      'historical_sp3_serialization_fail_retained': fail.get('status')=='FAIL_RETAINED_FIXED' and fail.get('data_changed_by_fix') is False and fail.get('physics_thresholds_changed_by_fix') is False,
      'sp3_topology_not_promoted_to_production_measurement': audit.get('evidence_reclassification',{}).get('sp3_topology')=='MODEL_DERIVED_TOPOLOGY_CONTROL_NOT_PRODUCTION_SOURCE',
      'sp3_matching_not_promoted_to_independent_measurement': audit.get('evidence_reclassification',{}).get('sp3_matching')=='MODEL_DERIVED_KINEMATIC_CONSISTENCY_CONTROL',
      'same_id_is_only_provenance_consistency': audit.get('evidence_reclassification',{}).get('sp3_same_id')=='SOURCE_PROVENANCE_CONSISTENCY_NOT_INDEPENDENT_PHYSICAL_REALIZATION_PROOF',
      'physical_and_canon_firewall': audit.get('physical_production_claim') is False and audit.get('canon_allowed') is False and audit.get('empirical_theory_confirmation') is False,
    }
    if loader is not None:
        checks['v012_loader_fail_retained']=loader.get('status')=='FAIL_RETAINED_FIXED' and loader.get('data_changed_by_fix') is False and loader.get('physics_thresholds_changed_by_fix') is False
    status='PASS' if all(checks.values()) else 'FAIL'
    out={
      'schema':'QHTRI_TOE_CANDIDATE_RELEASE_GATE_V0_12','status':status,
      'verdict':'PASS_CANDIDATE_IMPLEMENTATION_COMPLETE_EVIDENCE_BOUNDARY_AUDITED' if status=='PASS' else 'FAIL_CANDIDATE_IMPLEMENTATION_EVIDENCE_BOUNDARY',
      'authority':'CANDIDATE_ONLY','canon_allowed':False,'physical_production_claim':False,'empirical_theory_confirmation':False,
      'checks':checks,'passed':sum(checks.values()),'failed':sum(not v for v in checks.values()),
      'candidate_release_ready':status=='PASS','repository_implementation_complete':status=='PASS',
      'remaining_missing_software_operators':0 if status=='PASS' else None,
      'remaining_missing_source_wiring_operators':0 if status=='PASS' else None,
      'validated_evidence_layers':['EXTERNAL_OBSERVATIONAL_ARCHIVE_DERIVED_MODEL_LEVEL_SP3','EXTERNAL_EMPIRICAL_RINDLER_CALIBRATED_REFERENCE'],
      'open_non_repository_evidence':['FULL_PHYSICAL_3PLUS1_PRODUCTION_CAPTURE_ONLY_IF_A_PHYSICAL_PRODUCTION_OR_THEORY_CONFIRMATION_CLAIM_IS_REQUESTED'],
      'merge_to_main_requires_explicit_user_order':True,
      'historical_v011_preserved':True,
      'firewall':'Candidate repository completion is an implementation/reference-validation verdict. Model-derived SP3 topology/matching are not independent production-source measurements; no physical-production or empirical-theory-confirmation claim is made.'
    }
    out['receipt_sha256']=sha(out); return out

if __name__=='__main__':
    ap=argparse.ArgumentParser();
    for x in ['audit','sp3_validation','sp3_adversarial','rindler','retained_fail']: ap.add_argument('--'+x.replace('_','-'),dest=x,required=True,type=Path)
    ap.add_argument('--loader-fail',dest='loader_fail',type=Path)
    a=ap.parse_args(); r=run(a.audit,a.sp3_validation,a.sp3_adversarial,a.rindler,a.retained_fail,a.loader_fail); print(json.dumps(r,indent=2,sort_keys=True)); raise SystemExit(0 if r['status']=='PASS' else 1)
