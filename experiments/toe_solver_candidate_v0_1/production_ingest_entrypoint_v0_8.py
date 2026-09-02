from __future__ import annotations
import argparse, hashlib, json
from dataclasses import fields
from pathlib import Path
from idt05k_precision_receipt_v0_8 import IDT05KPrecisionLapseReceiptV08, IDT05KPrecisionReceiptError
from production_contract_bridge_v0_6 import TIRGSC1SpatialReceipt, RFCGSC3CShiftReceipt, ProductionContractBridgeError

SCHEMA='QHTRI_TOE_PRODUCTION_INGEST_BUNDLE_V0_8'
RECEIPT_SCHEMA='QHTRI_TOE_PRODUCTION_INGEST_RECEIPT_V0_8'
class ProductionIngestV08Error(ValueError): pass

def _strict(cls,payload,label):
    if not isinstance(payload,dict): raise ProductionIngestV08Error(f'{label} must be object')
    expected={f.name for f in fields(cls)}; supplied=set(payload)
    missing=sorted(expected-supplied); extra=sorted(supplied-expected)
    if missing or extra: raise ProductionIngestV08Error(f'{label} field mismatch: missing={missing}, extra={extra}')
    return cls(**payload)

def sha(obj): return hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(',',':')).encode()).hexdigest()

def ingest_dict(data):
    if not isinstance(data,dict) or data.get('schema')!=SCHEMA: raise ProductionIngestV08Error(f'bundle schema must equal {SCHEMA}')
    expected={'schema','bundle_id','idt_lapse_precision','tir_spatial','rfc_shift'}
    if set(data)!=expected: raise ProductionIngestV08Error(f'bundle field mismatch: missing={sorted(expected-set(data))}, extra={sorted(set(data)-expected)}')
    bid=data['bundle_id']
    if not isinstance(bid,str) or not bid.strip(): raise ProductionIngestV08Error('bundle_id must be non-empty')
    inp=sha(data)
    try:
        idt=_strict(IDT05KPrecisionLapseReceiptV08,data['idt_lapse_precision'],'idt_lapse_precision'); idt.validate()
        tir=_strict(TIRGSC1SpatialReceipt,data['tir_spatial'],'tir_spatial'); tir.validate()
        rfc=_strict(RFCGSC3CShiftReceipt,data['rfc_shift'],'rfc_shift'); rfc.validate()
    except (IDT05KPrecisionReceiptError,ProductionContractBridgeError,ValueError,TypeError) as exc:
        return {'schema':RECEIPT_SCHEMA,'status':'FAIL_CONTRACT','authority':'CANDIDATE_ONLY','canon_allowed':False,'physical_production_claim':False,'bundle_id':bid,'input_sha256':inp,'reason':str(exc),'promotion_review_eligible':False,'ready_for_field_ingest':False,'blockers':['INVALID_SOURCE_CONTRACT']},1
    blockers=[]
    if not idt.production_input: blockers.append('IDT_05K_PRECISION_PRODUCTION_CAPTURE_DATASET')
    if not tir.production_source_admitted: blockers.append('TIR_GSC1_PRODUCTION_SOURCE_CAPTURE')
    if not (idt.realization_id==tir.realization_id==rfc.realization_id): blockers.append('SAME_PHYSICAL_REALIZATION_BINDING')
    if idt.clock_id!=rfc.clock_id: blockers.append('SAME_CLOCK_ID_BINDING')
    ready=not blockers
    receipt={'schema':RECEIPT_SCHEMA,'status':'READY_FOR_FIELD_INGEST_AND_E2E_PHYSICAL_CLOSURE' if ready else 'BLOCKED_PRODUCTION_EVIDENCE','authority':'CANDIDATE_ONLY','canon_allowed':False,'physical_production_claim':False,'bundle_id':bid,'input_sha256':inp,'promotion_review_eligible':ready,'ready_for_field_ingest':ready,'blockers':blockers,'precision_encoding':idt.encoding,'precision_digits':idt.precision_digits,'max_log_residual':idt.max_log_residual,'source_evidence_class':idt.source_evidence_class,'firewall':'READY requires precision-safe IDT, TIR and RFC source receipts from one realization; it is only eligibility for downstream physical closure and never a canon or physical-result claim.'}
    receipt['receipt_sha256']=sha(receipt)
    return receipt,0 if ready else 2

def main(argv=None):
    p=argparse.ArgumentParser(); p.add_argument('--bundle',required=True,type=Path); p.add_argument('--output',type=Path); ns=p.parse_args(argv)
    try: receipt,code=ingest_dict(json.loads(ns.bundle.read_text()))
    except (OSError,json.JSONDecodeError,ProductionIngestV08Error) as exc:
        receipt={'schema':RECEIPT_SCHEMA,'status':'FAIL_INPUT','authority':'CANDIDATE_ONLY','canon_allowed':False,'physical_production_claim':False,'reason':str(exc),'promotion_review_eligible':False,'ready_for_field_ingest':False,'blockers':['INVALID_INGEST_INPUT']}; code=1
    text=json.dumps(receipt,indent=2,sort_keys=True); print(text)
    if ns.output: ns.output.write_text(text+'\n')
    return code
if __name__=='__main__': raise SystemExit(main())
