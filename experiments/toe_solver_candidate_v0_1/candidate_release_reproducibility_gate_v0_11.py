from __future__ import annotations
import importlib.util, json, hashlib
from pathlib import Path

HERE=Path(__file__).resolve().parent
EXPECTED_VALIDATION_SHA='5c6378513af679fe0a6472652f85ff6690bb9dab7dd3f3b5c86d4333071ae768'
EXPECTED_ADVERSARIAL_SHA='ebe2fc40928a160453f0b4a847028d6399567695efb1eae53f4a0f95bf04bb69'
EXPECTED_SOURCE_SHA='e6c18e85a6f2b62c6820258b7ecfc514f8a177f1c2eaff54d6a5ff0b8fab2399'

def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod); return mod

def canon(o): return json.dumps(o,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()
def sha(o): return hashlib.sha256(canon(o)).hexdigest()

def run():
    val=load('v011_val',HERE/'igs_sp3_observational_validation_v0_11.py').run()
    adv=load('v011_adv',HERE/'igs_sp3_observational_adversarial_v0_11.py').run()
    ledger=json.loads((HERE/'CONCEPTNAV_CLOSURE_LEDGER_V0_11.json').read_text())
    retained=json.loads((HERE/'IGS_SP3_OBSERVATIONAL_SERIALIZATION_FAIL_V0_11.json').read_text())
    checks={
      'validation_7_of_7_pass': val['status']=='PASS' and len(val['checks'])==7 and all(val['checks'].values()),
      'validation_receipt_reproducible': val['receipt_sha256']==EXPECTED_VALIDATION_SHA,
      'adversarial_5_of_5_pass': adv['status']=='PASS' and adv['passed']==5 and adv['failed']==0,
      'adversarial_receipt_reproducible': adv['receipt_sha256']==EXPECTED_ADVERSARIAL_SHA,
      'single_archived_source_digest': val['source_extract_sha256']==EXPECTED_SOURCE_SHA==ledger['source']['source_extract_sha256'],
      'candidate_ledger_complete': ledger['status']=='PASS_CANDIDATE_REPO_COMPLETE_OBSERVATIONAL_E2E' and ledger['candidate_release_ready'] is True,
      'zero_missing_software_operators': ledger['remaining_missing_software_operators']==0 and ledger['remaining_missing_source_wiring_operators']==0,
      'retained_fail_preserved': retained['status']=='FAIL_RETAINED_FIXED' and retained['data_changed_by_fix'] is False and retained['physics_thresholds_changed_by_fix'] is False,
      'epistemic_firewall': ledger['authority']=='CANDIDATE_ONLY' and ledger['canon_allowed'] is False and ledger['physical_production_claim'] is False,
      'main_merge_requires_explicit_order': ledger['merge_to_main_requires_explicit_user_order'] is True,
    }
    status='PASS' if all(checks.values()) else 'FAIL'
    out={
      'schema':'QHTRI_TOE_CANDIDATE_RELEASE_REPRODUCIBILITY_GATE_V0_11',
      'status':status,
      'authority':'CANDIDATE_ONLY',
      'canon_allowed':False,
      'physical_production_claim':False,
      'checks':checks,
      'validation_receipt_sha256':val['receipt_sha256'],
      'adversarial_receipt_sha256':adv['receipt_sha256'],
      'source_extract_sha256':EXPECTED_SOURCE_SHA,
      'candidate_release_ready': status=='PASS',
      'merge_to_main_requires_explicit_user_order':True,
    }
    out['receipt_sha256']=sha(out)
    return out
if __name__=='__main__':
    r=run(); print(json.dumps(r,indent=2,sort_keys=True)); raise SystemExit(0 if r['status']=='PASS' else 1)
