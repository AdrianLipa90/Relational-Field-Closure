from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
V5 = ROOT / 'v0_5'
V6 = ROOT / 'v0_6'
V7 = ROOT / 'v0_7'

class ReleaseGateError(ValueError):
    pass


def load(path: Path):
    try:
        return json.loads(path.read_text())
    except Exception as exc:
        raise ReleaseGateError(f'cannot load {path.name}: {exc}') from exc


def sha(path: Path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(cond: bool, msg: str):
    if not cond:
        raise ReleaseGateError(msg)


def main():
    sources = {
        'v0_5': V5 / 'production_source_bundle_receipt_v0_5.json',
        'v0_6': V6 / 'production_contract_bridge_receipt_v0_6.json',
        'v0_6_discovery': V6 / 'source_branch_discovery_receipt_v0_6.json',
        'v0_7': V7 / 'production_ingest_receipt_v0_7.json',
        'ledger_v0_7': V7 / 'conceptnav_closure_ledger_v0_7.json',
    }
    docs = {k: load(v) for k,v in sources.items()}

    checks = []
    def check(name, cond, detail=None):
        checks.append({'name': name, 'pass': bool(cond), **({} if detail is None else {'detail': detail})})
        require(bool(cond), name)

    check('v0_5_generic_source_bundle_pass', docs['v0_5'].get('status') == 'PASS' and docs['v0_5'].get('summary') == {'fail':0,'pass':6})
    check('v0_6_typed_contract_bridge_pass', docs['v0_6'].get('status') == 'PASS' and docs['v0_6'].get('summary') == {'fail':0,'pass':7})
    check('v0_7_production_ingest_pass', docs['v0_7'].get('status') == 'PASS' and docs['v0_7'].get('summary') == {'fail':0,'pass':6})
    check('provider_discovery_no_missing_operator', docs['v0_6_discovery'].get('conclusion',{}).get('missing_executable_provider_operators') == 0)
    check('provider_discovery_keeps_three_physical_witnesses', docs['v0_6_discovery'].get('conclusion',{}).get('production_source_witness_objects_required') == 3)

    ledger = docs['ledger_v0_7']
    check('ledger_software_closure_ready', ledger.get('status') == 'SOFTWARE_CLOSURE_READY_FOR_PRODUCTION_INGEST_PHYSICAL_EVIDENCE_OPEN')
    check('ledger_zero_live_fail', ledger.get('summary',{}).get('live_fail') == 0)
    check('ledger_thirteen_live_pass', ledger.get('summary',{}).get('live_pass') == 13)
    check('ledger_zero_missing_provider_operators', ledger.get('summary',{}).get('missing_executable_provider_operators') == 0)
    check('ledger_retains_historical_fail', ledger.get('summary',{}).get('retained_historical_candidate_fail') == 1)
    check('production_frontier_exactly_three', len(ledger.get('production_evidence_frontier',[])) == 3)
    check('candidate_authority_only', all(d.get('authority') == 'CANDIDATE_ONLY' for d in (docs['v0_5'],docs['v0_6'],docs['v0_7'],ledger)))
    check('no_canon_self_promotion', all(d.get('canon_allowed') is False for d in (docs['v0_5'],docs['v0_6'],docs['v0_7'],ledger)))
    check('no_physical_claim_from_fixture_gates', all(d.get('physical_production_claim') is False for d in (docs['v0_5'],docs['v0_6'],docs['v0_7'])))
    check('ready_not_equal_physical_closure_firewall', ledger.get('firewalls',{}).get('ready_for_field_ingest_equals_physical_closure') is False)
    check('same_realization_required', ledger.get('firewalls',{}).get('same_realization_required') is True)
    check('same_clock_required', ledger.get('firewalls',{}).get('same_clock_identity_required') is True)
    check('qhtri_scope_model_state_only', ledger.get('qhtri_v0_7',{}).get('epistemic_status') == 'MODEL_STATE_VALIDATION' and ledger.get('qhtri_v0_7',{}).get('hardware_witness_scope') == 'UNASSESSED')

    receipt = {
        'schema':'QHTRI_TOE_CANDIDATE_SOFTWARE_RELEASE_GATE_V0_7',
        'status':'PASS_SOFTWARE_ARCHIVE_RELEASE_GATE',
        'authority':'CANDIDATE_ONLY',
        'canon_allowed':False,
        'physical_production_claim':False,
        'tested_candidate_head_before_gate_archive':'154ef2c4a162fa3f9f7416ff7c6276d30722f7ca',
        'checks':checks,
        'summary':{
            'pass':sum(c['pass'] for c in checks),
            'fail':sum(not c['pass'] for c in checks),
            'software_provider_operator_closure':'PASS',
            'production_evidence_closure':'OPEN_3_SOURCE_WITNESSES',
        },
        'source_receipt_sha256':{k:sha(v) for k,v in sources.items()},
        'known_global_reference_v0_4_receipt_sha256':'d3560eef20de26bb69aed4688ae7afc988b527e64a64025f0c2818189a8e3809',
        'retained_historical_fail_policy':'PRESERVED_IN_CANDIDATE_HISTORY',
        'release_semantics':'PASS means candidate software/provider/ingest archive is internally consistent; it does not certify physical production evidence, canon, or a physical ToE closure.',
    }
    text=json.dumps(receipt,sort_keys=True,indent=2)
    (V7/'candidate_software_release_gate_receipt_v0_7.json').write_text(text+'\n')
    print(text)

if __name__ == '__main__':
    main()
