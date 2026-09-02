from __future__ import annotations

import argparse
from dataclasses import asdict, fields
import hashlib
import json
from pathlib import Path
import sys

HERE=Path(__file__).resolve().parent
V06=HERE.parent/'v0_6'
if V06.exists():
    sys.path.insert(0,str(V06))
from production_contract_bridge_v0_6 import (
    IDT05KLapseReceipt,
    TIRGSC1SpatialReceipt,
    RFCGSC3CShiftReceipt,
    ProductionContractBundleV06,
    ProductionContractBridgeError,
    certify_production_contract_bundle,
)

SCHEMA='QHTRI_TOE_PRODUCTION_INGEST_BUNDLE_V0_7'
RECEIPT_SCHEMA='QHTRI_TOE_PRODUCTION_INGEST_RECEIPT_V0_7'

class ProductionIngestError(ValueError):
    pass


def _strict_dataclass(cls,payload,label):
    if not isinstance(payload,dict):
        raise ProductionIngestError(f'{label} must be a JSON object')
    expected={f.name for f in fields(cls)}
    supplied=set(payload)
    missing=sorted(expected-supplied)
    extra=sorted(supplied-expected)
    if missing or extra:
        raise ProductionIngestError(f'{label} field mismatch: missing={missing}, extra={extra}')
    try:
        return cls(**payload)
    except TypeError as exc:
        raise ProductionIngestError(f'{label} could not be constructed: {exc}') from exc


def load_bundle_dict(data):
    if not isinstance(data,dict):
        raise ProductionIngestError('bundle must be a JSON object')
    if data.get('schema') != SCHEMA:
        raise ProductionIngestError(f'bundle schema must equal {SCHEMA}')
    expected={'schema','idt_lapse','tir_spatial','rfc_shift','bundle_id'}
    missing=sorted(expected-set(data)); extra=sorted(set(data)-expected)
    if missing or extra:
        raise ProductionIngestError(f'bundle top-level field mismatch: missing={missing}, extra={extra}')
    bundle_id=data.get('bundle_id')
    if not isinstance(bundle_id,str) or not bundle_id.strip():
        raise ProductionIngestError('bundle_id must be a non-empty string')
    return bundle_id, ProductionContractBundleV06(
        _strict_dataclass(IDT05KLapseReceipt,data['idt_lapse'],'idt_lapse'),
        _strict_dataclass(TIRGSC1SpatialReceipt,data['tir_spatial'],'tir_spatial'),
        _strict_dataclass(RFCGSC3CShiftReceipt,data['rfc_shift'],'rfc_shift'),
    )


def canonical_sha256(obj):
    raw=json.dumps(obj,sort_keys=True,separators=(',',':')).encode()
    return hashlib.sha256(raw).hexdigest()


def ingest_dict(data):
    bundle_id,bundle=load_bundle_dict(data)
    input_sha=canonical_sha256(data)
    try:
        cert=certify_production_contract_bundle(bundle)
    except (ProductionContractBridgeError,ValueError,TypeError) as exc:
        return {
            'schema':RECEIPT_SCHEMA,'status':'FAIL_CONTRACT','authority':'CANDIDATE_ONLY',
            'canon_allowed':False,'physical_production_claim':False,'bundle_id':bundle_id,
            'input_sha256':input_sha,'reason':str(exc),'promotion_review_eligible':False,
            'ready_for_field_ingest':False,'blockers':['INVALID_SOURCE_CONTRACT']
        },1
    status='READY_FOR_FIELD_INGEST_AND_E2E_PHYSICAL_CLOSURE' if cert.promotion_review_eligible else 'BLOCKED_PRODUCTION_EVIDENCE'
    receipt={
        'schema':RECEIPT_SCHEMA,'status':status,'authority':'CANDIDATE_ONLY','canon_allowed':False,
        'physical_production_claim':False,'bundle_id':bundle_id,'input_sha256':input_sha,
        'promotion_review_eligible':bool(cert.promotion_review_eligible),
        'ready_for_field_ingest':bool(cert.promotion_review_eligible),
        'blockers':list(cert.blockers),'certificate':asdict(cert),
        'firewall':'READY means source contracts passed and data are eligible for downstream physical review; it does not self-promote canon or assert a physical result.'
    }
    receipt['receipt_sha256']=canonical_sha256(receipt)
    return receipt,0 if cert.promotion_review_eligible else 2


def main(argv=None):
    parser=argparse.ArgumentParser()
    parser.add_argument('--bundle',required=True,type=Path)
    parser.add_argument('--output',type=Path)
    ns=parser.parse_args(argv)
    try:
        data=json.loads(ns.bundle.read_text())
        receipt,code=ingest_dict(data)
    except (OSError,json.JSONDecodeError,ProductionIngestError) as exc:
        receipt={'schema':RECEIPT_SCHEMA,'status':'FAIL_INPUT','authority':'CANDIDATE_ONLY','canon_allowed':False,'physical_production_claim':False,'reason':str(exc),'promotion_review_eligible':False,'ready_for_field_ingest':False,'blockers':['INVALID_INGEST_INPUT']}
        code=1
    text=json.dumps(receipt,sort_keys=True,indent=2)
    print(text)
    if ns.output:
        ns.output.write_text(text+'\n')
    return code

if __name__=='__main__': raise SystemExit(main())
