from __future__ import annotations
import hashlib,json
from pathlib import Path

HERE=Path(__file__).resolve().parent
FILES={
 'precision':'PRECISION_LAPSE_REALDATA_VALIDATION_V0_8_RECEIPT.json',
 'ingest':'PRODUCTION_INGEST_VALIDATION_V0_8_RECEIPT.json',
 'retained_fail':'PRECISION_LAPSE_DECIMAL_CONTEXT_FAIL_V0_8.json',
 'ledger':'CONCEPTNAV_CLOSURE_LEDGER_V0_8.json',
}

def canonical_sha(obj): return hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(',',':')).encode()).hexdigest()

def run(root=HERE):
    d={k:json.loads((root/v).read_text()) for k,v in FILES.items()}
    checks=[]
    def ck(name,cond,detail): checks.append({'name':name,'status':'PASS' if cond else 'FAIL','detail':detail})
    p=d['precision']; i=d['ingest']; f=d['retained_fail']; l=d['ledger']
    ck('precision_realdata_6_of_6',p.get('status')=='PASS' and p.get('passed')==6 and p.get('failed')==0,{'passed':p.get('passed'),'failed':p.get('failed')})
    ck('precision_ingest_6_of_6',i.get('status')=='PASS' and i.get('passed')==6 and i.get('failed')==0,{'passed':i.get('passed'),'failed':i.get('failed')})
    ck('decimal_failure_retained',f.get('status')=='FAIL_RETAINED' and f.get('observed_residual')=='2.429021469594861761852559533E-47',f.get('observed_residual'))
    ck('ledger_precision_aware_status',l.get('status')=='PASS_SOFTWARE_PRECISION_PATCH_PRODUCTION_EVIDENCE_OPEN',l.get('status'))
    ck('v07_historical_not_current',l.get('historical_v07_release_gate_status')=='PASS_RETAINED_AS_PRE_PRECISION_DISCOVERY',l.get('historical_v07_release_gate_status'))
    frontier=l.get('production_frontier',[])
    ck('production_frontier_exact_three',frontier==['IDT_05K_PRECISION_PRODUCTION_CAPTURE_DATASET','TIR_GSC1_PRODUCTION_SOURCE_CAPTURE','RFC_GSC3C_SOURCE_OWNED_BINDING_ON_SAME_REALIZATION'],frontier)
    ck('float64_sub_epsilon_firewall', 'NO_FLOAT64_N_FOR_SUB_EPSILON_CLOCK_OFFSETS' in l.get('firewalls',[]),l.get('firewalls',[]))
    ck('no_self_canon', all(x.get('canon_allowed') is False for x in d.values()),{k:v.get('canon_allowed') for k,v in d.items()})
    passed=sum(x['status']=='PASS' for x in checks)
    out={'schema':'QHTRI_TOE_CANDIDATE_SOFTWARE_RELEASE_GATE_V0_8','status':'PASS' if passed==len(checks) else 'FAIL','authority':'CANDIDATE_ONLY','canon_allowed':False,'physical_production_claim':False,'checks':checks,'passed':passed,'failed':len(checks)-passed,'production_evidence_status':'OPEN','firewall':'Software precision closure PASS does not promote any production witness or physical ToE closure.'}
    out['receipt_sha256']=canonical_sha(out)
    return out
if __name__=='__main__':
    r=run(); print(json.dumps(r,indent=2,sort_keys=True)); raise SystemExit(0 if r['status']=='PASS' else 1)
