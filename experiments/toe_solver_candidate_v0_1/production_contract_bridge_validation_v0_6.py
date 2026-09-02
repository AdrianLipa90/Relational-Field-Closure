from __future__ import annotations
import json
from pathlib import Path
from production_contract_bridge_v0_6 import *

HERE=Path(__file__).resolve().parent
H='a'*64

def idt(*,production=False,rid='R1',clock='C1',canon=False):
    return IDT05KLapseReceipt(
        'IDT_GLOBAL_LAPSE_PRODUCTION_CAPTURE_V0_1',True,True,True,True,
        production,production,canon,'d','%s'%rid,'%s'%clock,'p0',H,0.0,3,3)

def tir(*,production=False,rid='R1'):
    return TIRGSC1SpatialReceipt(
        'TIR_GSC1_PRODUCTION_SPATIAL_RECEIPT_BRIDGE_V0_6',
        'TIR_GLOBAL_RELATIONAL_COMPLEX_CAPTURE_V0_1',production,H,H if production else None,H,
        True,True,True,H,True,True,True,rid)

def rfc(*,rid='R1',clock='C1',exact=True):
    return RFCGSC3CShiftReceipt(
        'PASS_GSC3C_BETA_MATCH_RFC_SHIFT_SOURCE_BINDING_ON_SUPPLIED_REALIZATION' if exact else 'PASS_GSC3C_COVARIANT_FAMILY_WITH_SOURCE_BINDING_OPEN',
        rid,clock,True,exact,0.0,0.0,0.0,0.0,
        'SOURCE_BINDING_CERTIFIED_ON_SUPPLIED_REALIZATION' if exact else 'PRODUCTION_SOURCE_BINDING_OPEN',
        True,True,True,H)

def expect_error(name,fn,needle):
    try: fn()
    except Exception as e:
        return {'name':name,'pass':needle in str(e),'error':str(e)}
    return {'name':name,'pass':False,'error':'NO_ERROR'}

def main():
    checks=[]
    c=certify_production_contract_bundle(ProductionContractBundleV06(idt(production=False),tir(production=False),rfc()))
    checks.append({'name':'provider_contracts_valid_but_source_data_not_production','pass':not c.promotion_review_eligible and set(c.blockers)=={'IDT_05K_PRODUCTION_CAPTURE_DATASET','TIR_GSC1_PRODUCTION_SOURCE_CAPTURE'},'blockers':list(c.blockers)})

    c2=certify_production_contract_bundle(ProductionContractBundleV06(idt(production=True),tir(production=True),rfc()))
    checks.append({'name':'same_realization_same_clock_production_shaped_fixture_reaches_review_gate','pass':c2.promotion_review_eligible and not c2.canon_allowed and not c2.blockers,'certificate_sha256':certificate_sha256(c2)})

    c3=certify_production_contract_bundle(ProductionContractBundleV06(idt(production=True,rid='RA'),tir(production=True,rid='RA'),rfc(rid='RB')))
    checks.append({'name':'same_physical_realization_firewall','pass':not c3.promotion_review_eligible and c3.blockers==('SAME_PHYSICAL_REALIZATION_BINDING',),'blockers':list(c3.blockers)})

    c4=certify_production_contract_bundle(ProductionContractBundleV06(idt(production=True,clock='clock-A'),tir(production=True),rfc(clock='clock-B')))
    checks.append({'name':'same_clock_identity_firewall','pass':not c4.promotion_review_eligible and c4.blockers==('SAME_CLOCK_ID_BINDING',),'blockers':list(c4.blockers)})

    checks.append(expect_error('idt_canon_self_authorization_rejected',lambda: certify_production_contract_bundle(ProductionContractBundleV06(idt(production=True,canon=True),tir(production=True),rfc())),'must not self-authorize canon'))
    checks.append(expect_error('rfc_covariance_without_exact_source_binding_rejected',lambda: certify_production_contract_bundle(ProductionContractBundleV06(idt(production=True),tir(production=True),rfc(exact=False))),'requires source_binding_exact'))

    bad=TIRGSC1SpatialReceipt('TIR_GSC1_PRODUCTION_SPATIAL_RECEIPT_BRIDGE_V0_6','TIR_GLOBAL_RELATIONAL_COMPLEX_CAPTURE_V0_1',True,H,'not-a-hash',H,True,True,True,H,True,True,True,'R1')
    checks.append(expect_error('tir_malformed_production_capture_receipt_rejected',lambda: certify_production_contract_bundle(ProductionContractBundleV06(idt(production=True),bad,rfc())),'64 lowercase hex'))

    status='PASS' if all(x['pass'] for x in checks) else 'FAIL'
    out={
      'schema':'QHTRI_TOE_TYPED_PRODUCTION_CONTRACT_BRIDGE_VALIDATION_V0_6',
      'status':status,
      'authority':'CANDIDATE_ONLY','canon_allowed':False,'physical_production_claim':False,
      'checks':checks,
      'summary':{'pass':sum(x['pass'] for x in checks),'fail':sum(not x['pass'] for x in checks)},
      'source_contracts':{
        'idt_05k':'IDT_GLOBAL_LAPSE_PRODUCTION_CAPTURE_V0_1 @ branch feat/05k-global-lapse-production-capture-v0.1 commit 979c470c719c199ac56f86963e2effc7f3bc3e98',
        'tir_gsc1':'TIR_GLOBAL_RELATIONAL_COMPLEX_CAPTURE_V0_1 + deterministic source freeze on TIR main 9a004eebe3d1d9bece971180a240136f896d0799',
        'rfc_gsc3c':'beta_match_shift_source_binding on RFC main 85bbb1d0754605be2720b6bd258b486b0a072345'
      },
      'interpretation_firewall':'Production-shaped fixtures validate typed contract logic only. No fixture is a physical production capture.'
    }
    text=json.dumps(out,sort_keys=True,indent=2)
    (HERE/'production_contract_bridge_receipt_v0_6.json').write_text(text+'\n')
    print(text)
    return 0 if status=='PASS' else 1

if __name__=='__main__': raise SystemExit(main())
