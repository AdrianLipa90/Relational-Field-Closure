from __future__ import annotations
import copy, json
from production_ingest_entrypoint_v0_8 import SCHEMA, ingest_dict

H='a'*64; R='b'*64

def idt(): return {
 'schema':'IDT_GLOBAL_LAPSE_PRECISION_CAPTURE_V0_8','source_schema':'IDT_GLOBAL_LAPSE_PRODUCTION_CAPTURE_V0_1',
 'input_valid':True,'integrity_valid':True,'cocycle_valid':True,'patch_coverage_valid':True,
 'production_input':False,'promotion_review_eligible':False,'canon_allowed':False,
 'dataset_id':'zenodo-8184043-fig3-precision-benchmark','realization_id':'R1','clock_id':'C1','reference_patch_id':'h0','dataset_sha256':H,
 'encoding':'DECIMAL_LOG_N','precision_digits':80,'tolerance_log':'1e-40','max_log_residual':'0','patch_count':5,'edge_count':4,
 'source_evidence_class':'EXTERNAL_PROCESS_DATA_REFERENCE','source_reference':'doi:10.5281/zenodo.8184043#Fig3.csv','source_digest':R}
def tir(): return {'schema':'TIR_GSC1_PRODUCTION_SPATIAL_RECEIPT_BRIDGE_V0_6','capture_schema':'TIR_GLOBAL_RELATIONAL_COMPLEX_CAPTURE_V0_1','production_source_admitted':False,'capture_sha256':H,'capture_receipt_sha256':None,'incidence_sha256':H,'manifold_certified':True,'input_valid':True,'integrity_valid':True,'edge_refinement_certificate_sha256':H,'edge_refinement_ready':True,'overlap_cocycle_witness_supplied':True,'domain_coverage_witness_supplied':True,'realization_id':'R1'}
def rfc(): return {'status':'PASS_GSC3C_BETA_MATCH_RFC_SHIFT_SOURCE_BINDING_ON_SUPPLIED_REALIZATION','realization_id':'R1','clock_id':'C1','overlap_covariance_pass':True,'source_binding_exact':True,'max_beta_overlap_defect':0.0,'max_shift_overlap_defect':0.0,'max_homogeneous_w_defect':0.0,'max_source_binding_defect':0.0,'production_status':'SOURCE_BINDING_CERTIFIED_ON_SUPPLIED_REALIZATION','global_flow_coverage_witness_supplied':True,'global_clock_properness_witness_supplied':True,'physical_event_placement_witness_supplied':True,'receipt_sha256':H}
def bundle(): return {'schema':SCHEMA,'bundle_id':'v08-control','idt_lapse_precision':idt(),'tir_spatial':tir(),'rfc_shift':rfc()}

def run():
    out=[]
    def check(name,cond,detail): out.append({'name':name,'status':'PASS' if cond else 'FAIL','detail':detail})
    rec,code=ingest_dict(bundle())
    check('external_realdata_precision_receipt_admitted_but_not_promoted', code==2 and rec['status']=='BLOCKED_PRODUCTION_EVIDENCE' and 'IDT_05K_PRECISION_PRODUCTION_CAPTURE_DATASET' in rec['blockers'],rec)
    b=bundle(); b['idt_lapse_precision']['encoding']='FLOAT64_N'; rec,code=ingest_dict(b)
    check('float64_encoding_rejected',code==1 and rec['status']=='FAIL_CONTRACT',rec.get('reason'))
    b=bundle(); b['idt_lapse_precision']['production_input']=True; b['idt_lapse_precision']['promotion_review_eligible']=True; rec,code=ingest_dict(b)
    check('production_flag_without_production_source_rejected',code==1 and 'PRODUCTION_SOURCE' in rec.get('reason',''),rec.get('reason'))
    b=bundle(); b['idt_lapse_precision']['max_log_residual']='1e-20'; rec,code=ingest_dict(b)
    check('log_residual_above_tolerance_rejected',code==1 and 'exceeds tolerance' in rec.get('reason',''),rec.get('reason'))
    b=bundle(); b['tir_spatial']['realization_id']='R2'; rec,code=ingest_dict(b)
    check('same_realization_firewall_preserved',code==2 and 'SAME_PHYSICAL_REALIZATION_BINDING' in rec['blockers'],rec['blockers'])
    b=bundle(); b['rfc_shift']['clock_id']='C2'; rec,code=ingest_dict(b)
    check('same_clock_firewall_preserved',code==2 and 'SAME_CLOCK_ID_BINDING' in rec['blockers'],rec['blockers'])
    passed=sum(x['status']=='PASS' for x in out)
    return {'schema':'QHTRI_TOE_PRODUCTION_INGEST_VALIDATION_V0_8','status':'PASS' if passed==len(out) else 'FAIL','authority':'CANDIDATE_ONLY','canon_allowed':False,'passed':passed,'failed':len(out)-passed,'checks':out,'production_ready_path_status':'OPEN_UNTIL_TRUE_PRODUCTION_SOURCE_RECEIPTS_EXIST'}
if __name__=='__main__':
    r=run(); print(json.dumps(r,indent=2,sort_keys=True)); raise SystemExit(0 if r['status']=='PASS' else 1)
