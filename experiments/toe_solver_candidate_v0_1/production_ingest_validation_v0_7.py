from __future__ import annotations
import json
from pathlib import Path
from production_ingest_entrypoint_v0_7 import ingest_dict,SCHEMA

HERE=Path(__file__).resolve().parent
H='a'*64

def fixture(*,production=False,rid='R1',clock='C1',shift_rid=None,shift_clock=None,exact=True):
    shift_rid=rid if shift_rid is None else shift_rid
    shift_clock=clock if shift_clock is None else shift_clock
    return {
      'schema':SCHEMA,'bundle_id':'fixture-bundle',
      'idt_lapse':{
        'schema':'IDT_GLOBAL_LAPSE_PRODUCTION_CAPTURE_V0_1','input_valid':True,'integrity_valid':True,'cocycle_valid':True,'patch_coverage_valid':True,
        'production_input':production,'promotion_review_eligible':production,'canon_allowed':False,'dataset_id':'d','realization_id':rid,'clock_id':clock,'reference_patch_id':'p0','dataset_sha256':H,'max_relative_residual':0.0,'patch_count':3,'edge_count':3
      },
      'tir_spatial':{
        'schema':'TIR_GSC1_PRODUCTION_SPATIAL_RECEIPT_BRIDGE_V0_6','capture_schema':'TIR_GLOBAL_RELATIONAL_COMPLEX_CAPTURE_V0_1','production_source_admitted':production,
        'capture_sha256':H,'capture_receipt_sha256':H if production else None,'incidence_sha256':H,'manifold_certified':True,'input_valid':True,'integrity_valid':True,
        'edge_refinement_certificate_sha256':H,'edge_refinement_ready':True,'overlap_cocycle_witness_supplied':True,'domain_coverage_witness_supplied':True,'realization_id':rid
      },
      'rfc_shift':{
        'status':'PASS_GSC3C_BETA_MATCH_RFC_SHIFT_SOURCE_BINDING_ON_SUPPLIED_REALIZATION' if exact else 'PASS_GSC3C_COVARIANT_FAMILY_WITH_SOURCE_BINDING_OPEN',
        'realization_id':shift_rid,'clock_id':shift_clock,'overlap_covariance_pass':True,'source_binding_exact':exact,
        'max_beta_overlap_defect':0.0,'max_shift_overlap_defect':0.0,'max_homogeneous_w_defect':0.0,'max_source_binding_defect':0.0,
        'production_status':'SOURCE_BINDING_CERTIFIED_ON_SUPPLIED_REALIZATION' if exact else 'PRODUCTION_SOURCE_BINDING_OPEN',
        'global_flow_coverage_witness_supplied':True,'global_clock_properness_witness_supplied':True,'physical_event_placement_witness_supplied':True,'receipt_sha256':H
      }
    }

def main():
    checks=[]
    r,code=ingest_dict(fixture(production=False))
    checks.append({'name':'reference_source_bundle_blocks_without_failure','pass':code==2 and r['status']=='BLOCKED_PRODUCTION_EVIDENCE' and set(r['blockers'])=={'IDT_05K_PRODUCTION_CAPTURE_DATASET','TIR_GSC1_PRODUCTION_SOURCE_CAPTURE'},'status':r['status'],'blockers':r['blockers']})

    r,code=ingest_dict(fixture(production=True))
    checks.append({'name':'production_shaped_same_realization_reaches_field_ingest_gate','pass':code==0 and r['status']=='READY_FOR_FIELD_INGEST_AND_E2E_PHYSICAL_CLOSURE' and r['promotion_review_eligible'] and not r['canon_allowed'] and not r['physical_production_claim'],'status':r['status'],'receipt_sha256':r.get('receipt_sha256')})

    r,code=ingest_dict(fixture(production=True,shift_rid='R2'))
    checks.append({'name':'realization_mismatch_blocks','pass':code==2 and r['blockers']==['SAME_PHYSICAL_REALIZATION_BINDING'],'blockers':r['blockers']})

    r,code=ingest_dict(fixture(production=True,shift_clock='C2'))
    checks.append({'name':'clock_identity_mismatch_blocks','pass':code==2 and r['blockers']==['SAME_CLOCK_ID_BINDING'],'blockers':r['blockers']})

    r,code=ingest_dict(fixture(production=True,exact=False))
    checks.append({'name':'rfc_source_binding_open_is_contract_fail','pass':code==1 and r['status']=='FAIL_CONTRACT' and r['blockers']==['INVALID_SOURCE_CONTRACT'],'status':r['status'],'reason':r.get('reason')})

    bad=fixture(production=True); bad['idt_lapse']['unexpected']=1
    try:
        ingest_dict(bad)
    except Exception as e:
        checks.append({'name':'unexpected_input_field_fail_closed','pass':'field mismatch' in str(e),'error':str(e)})
    else:
        checks.append({'name':'unexpected_input_field_fail_closed','pass':False,'error':'NO_ERROR'})

    status='PASS' if all(x['pass'] for x in checks) else 'FAIL'
    out={'schema':'QHTRI_TOE_PRODUCTION_INGEST_VALIDATION_V0_7','status':status,'authority':'CANDIDATE_ONLY','canon_allowed':False,'physical_production_claim':False,'checks':checks,'summary':{'pass':sum(x['pass'] for x in checks),'fail':sum(not x['pass'] for x in checks)},'interpretation_firewall':'READY fixture tests ingest mechanics only. It is not a physical production capture or physical closure result.'}
    text=json.dumps(out,sort_keys=True,indent=2)
    (HERE/'production_ingest_receipt_v0_7.json').write_text(text+'\n')
    print(text)
    return 0 if status=='PASS' else 1

if __name__=='__main__': raise SystemExit(main())
