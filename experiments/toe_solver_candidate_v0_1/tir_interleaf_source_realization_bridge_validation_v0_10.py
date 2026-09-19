from __future__ import annotations
import json
from tir_interleaf_source_realization_bridge_v0_10 import *
from tir_gsc1_source_realization_bridge_validation_v0_9 import registry,SOURCE_DIGEST,LOCATOR,PHYSICAL_RID,PHASE_RID

def dataset(production=True,physical=PHYSICAL_RID,digest=SOURCE_DIGEST,locator=LOCATOR):
    patches=[{'patch_id':'A','beta_match':[3.0,-2.0,5.0]},{'patch_id':'B','beta_match':[2.5,-1.0,3.0]}]
    overlaps=[{'source':'A','target':'B','spatial_jacobian':[[1.,0.,0.],[0.,1.,0.],[0.,0.,1.]],'time_drift':[0.5,-1.0,2.0]}]
    d={'schema':SCHEMA,'dataset_id':'tir-interleaf-R1','production':production,
       'provenance':{'source':'TIR_INTERLEAF_R1','source_commit_or_digest':locator,'source_digest_sha256':digest,'physical_realization_id':physical},
       'temporal_coordinate':{'kind':'t','x0_binding':'x0=c*t','c_scale':10.0},
       'patches':patches,'overlaps':overlaps}
    normp=[{'patch_id':p['patch_id'],'beta_match':tuple(p['beta_match'])} for p in patches]
    normo=[{'source':o['source'],'target':o['target'],'spatial_jacobian':tuple(tuple(r) for r in o['spatial_jacobian']),'time_drift':tuple(o['time_drift'])} for o in overlaps]
    d['payload_sha256']=payload_sha('t',10.0,normp,normo)
    if production: d['provenance']['capture_receipt_sha256']=registry()['receipt_sha256']
    return d

def run():
    checks=[]
    def ck(name,fn,pred=None,err=None):
        try:
            x=fn(); ok=err is None and (pred(x) if pred else True); detail=receipt(x) if hasattr(x,'rfe8_shift_packet') else x
        except Exception as e:
            ok=err is not None and err in str(e); detail=str(e)
        checks.append({'name':name,'status':'PASS' if ok else 'FAIL','detail':detail})
    reg=registry()
    ck('production_matching_source_derives_rfc_shift',lambda:certify_interleaf_source_bridge(dataset(),reg),lambda c:c.tir_promotion_eligible and c.rfc_shift_derived_downstream and not c.rfc_source_witness_required and c.rfe8_shift_packet['patches'][0]['b_x0']==[0.3,-0.2,0.5])
    bad=dataset(); bad['patches'][1]['beta_match'][0]=2.75; bad['payload_sha256']=payload_sha('t',10.0,[{'patch_id':p['patch_id'],'beta_match':tuple(p['beta_match'])} for p in bad['patches']],[{'source':'A','target':'B','spatial_jacobian':((1.,0.,0.),(0.,1.,0.),(0.,0.,1.)),'time_drift':(0.5,-1.,2.)}])
    ck('matching_relation_defect_fails',lambda:certify_interleaf_source_bridge(bad,reg),err='matching handoff residual')
    bad=dataset(); bad['payload_sha256']='0'*64
    ck('payload_digest_tamper_fails',lambda:certify_interleaf_source_bridge(bad,reg),err='payload_sha256 mismatch')
    ck('source_digest_mismatch_fails',lambda:certify_interleaf_source_bridge(dataset(digest='9'*64),reg),err='no PNCS binding matches')
    ck('source_locator_mismatch_fails',lambda:certify_interleaf_source_bridge(dataset(locator='snapshot://other'),reg),err='no PNCS binding matches')
    ck('phase_realization_cannot_be_physical_realization',lambda:certify_interleaf_source_bridge(dataset(physical=PHASE_RID),reg),err='must remain distinct')
    ck('reference_packet_derives_shift_but_cannot_promote',lambda:certify_interleaf_source_bridge(dataset(production=False),reg),lambda c:not c.tir_promotion_eligible and c.rfc_shift_derived_downstream and not c.rfc_source_witness_required)
    bad=dataset(); bad['provenance']['capture_receipt_sha256']='a'*64
    ck('production_receipt_mismatch_fails',lambda:certify_interleaf_source_bridge(bad,reg),err='capture receipt does not match')
    passed=sum(c['status']=='PASS' for c in checks)
    out={'schema':'QHTRI_TOE_TIR_INTERLEAF_SOURCE_REALIZATION_BRIDGE_VALIDATION_V0_10','status':'PASS' if passed==len(checks) else 'FAIL','authority':'CANDIDATE_ONLY','canon_allowed':False,'physical_production_claim':False,'passed':passed,'failed':len(checks)-passed,'checks':checks,'result':'RFC_SHIFT_IS_DERIVED_DOWNSTREAM_NOT_AN_INDEPENDENT_SOURCE_WITNESS','production_frontier':'ACTUAL_SOURCE_OWNED_TIR_INTERLEAF_MATCHING_DATASET_STILL_OPEN'}
    out['receipt_sha256']=sha256(out);return out
if __name__=='__main__':
    r=run();print(json.dumps(r,indent=2,sort_keys=True));raise SystemExit(0 if r['status']=='PASS' else 1)
