from __future__ import annotations
from dataclasses import dataclass, asdict
import hashlib, json, re
from typing import Any, Mapping, Sequence

HEX64=re.compile(r'^[0-9a-f]{64}$')
PNCS_REALIZATION_RE=re.compile(r'^pncs:realization36:sha256:[0-9a-f]{64}$')
PNCS_BINDING_RE=re.compile(r'^pncs:binding36:sha256:[0-9a-f]{64}$')
CAPTURE_SCHEMA='TIR_GLOBAL_RELATIONAL_COMPLEX_CAPTURE_V0_1'
PNCS_RECEIPT_SCHEMA='PNCS_REALIZATION_REGISTRY_RECEIPT_V0_18'

class TIRSourceRealizationBridgeError(ValueError): pass

def compact(obj): return json.dumps(obj,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False)
def sha256(obj): return hashlib.sha256(compact(obj).encode()).hexdigest()
def reqstr(v,label):
    if not isinstance(v,str) or not v.strip(): raise TIRSourceRealizationBridgeError(f'{label} must be non-empty string')
    return v.strip()
def reqsha(v,label):
    x=reqstr(v,label)
    if HEX64.fullmatch(x) is None: raise TIRSourceRealizationBridgeError(f'{label} must be 64 lowercase hex')
    return x

def canonical_capture_sha(capture: Mapping[str,Any]) -> str:
    if capture.get('schema')!=CAPTURE_SCHEMA: raise TIRSourceRealizationBridgeError('capture schema mismatch')
    cid=reqstr(capture.get('capture_id'),'capture_id')
    src=capture.get('source')
    if not isinstance(src,Mapping): raise TIRSourceRealizationBridgeError('source must be object')
    cells=capture.get('tetrahedral_cells')
    if not isinstance(cells,list) or not cells: raise TIRSourceRealizationBridgeError('tetrahedral_cells must be non-empty list')
    seen_ids=set(); seen_tets=set(); canon=[]
    for i,c in enumerate(cells):
        if not isinstance(c,Mapping): raise TIRSourceRealizationBridgeError(f'cell {i} must be object')
        cell_id=reqstr(c.get('cell_id'),f'cell {i} id')
        if cell_id in seen_ids: raise TIRSourceRealizationBridgeError('duplicate cell_id')
        seen_ids.add(cell_id)
        verts=c.get('vertices')
        if not isinstance(verts,list) or len(verts)!=4: raise TIRSourceRealizationBridgeError('each cell requires four vertices')
        vv=tuple(sorted(reqstr(v,'vertex') for v in verts))
        if len(set(vv))!=4: raise TIRSourceRealizationBridgeError('tetrahedron repeats vertex')
        if vv in seen_tets: raise TIRSourceRealizationBridgeError('duplicate tetrahedral facet')
        seen_tets.add(vv); canon.append({'cell_id':cell_id,'vertices':list(vv)})
    payload={'schema':CAPTURE_SCHEMA,'capture_id':cid,'source':dict(src),'tetrahedral_cells':sorted(canon,key=lambda x:x['cell_id'])}
    return sha256(payload)

def verify_pncs_registry_receipt(receipt: Mapping[str,Any]) -> tuple[str,list[Mapping[str,Any]]]:
    if not isinstance(receipt,Mapping) or receipt.get('schema')!=PNCS_RECEIPT_SCHEMA: raise TIRSourceRealizationBridgeError('PNCS receipt schema mismatch')
    if receipt.get('semantic_equivalence_from_vectors') is not False: raise TIRSourceRealizationBridgeError('PNCS receipt must deny semantic equivalence from vectors')
    ids=receipt.get('binding_ids'); bindings=receipt.get('bindings')
    if not isinstance(ids,list) or not isinstance(bindings,list) or not bindings: raise TIRSourceRealizationBridgeError('PNCS receipt requires non-empty bindings')
    supplied=reqsha(receipt.get('receipt_sha256'),'PNCS receipt_sha256')
    payload={'schema':PNCS_RECEIPT_SCHEMA,'binding_ids':ids,'bindings':bindings,'semantic_equivalence_from_vectors':False}
    if sha256(payload)!=supplied: raise TIRSourceRealizationBridgeError('PNCS receipt_sha256 mismatch')
    recomputed_ids=[]
    for b in bindings:
        if not isinstance(b,Mapping): raise TIRSourceRealizationBridgeError('PNCS binding must be object')
        if b.get('schema')!='PNCS_EXACT_36D_BINDING_V0_18': raise TIRSourceRealizationBridgeError('PNCS binding schema mismatch')
        rid=reqstr(b.get('realization_id'),'PNCS realization_id')
        if PNCS_REALIZATION_RE.fullmatch(rid) is None: raise TIRSourceRealizationBridgeError('PNCS realization_id format mismatch')
        reqsha(b.get('source_digest_sha256'),'PNCS source_digest_sha256'); reqstr(b.get('source_locator'),'PNCS source_locator')
        recomputed_ids.append('pncs:binding36:sha256:'+sha256(dict(b)))
        if b.get('epistemic_operator')!='CHYBA' or b.get('canon_allowed') is not False: raise TIRSourceRealizationBridgeError('PNCS epistemic firewall violated')
    if any(not isinstance(x,str) or PNCS_BINDING_RE.fullmatch(x) is None for x in ids): raise TIRSourceRealizationBridgeError('PNCS binding_ids format mismatch')
    if sorted(ids)!=sorted(recomputed_ids): raise TIRSourceRealizationBridgeError('PNCS binding_ids do not match binding payloads')
    return supplied,bindings

@dataclass(frozen=True)
class TIRSourceRealizationBridgeCertificateV09:
    capture_schema_valid: bool
    capture_integrity_valid: bool
    pncs_provenance_receipt_valid: bool
    immutable_source_digest_bound: bool
    immutable_source_locator_bound: bool
    physical_realization_declared: bool
    phase_realization_kept_separate: bool
    production_source_class: bool
    provenance_ready: bool
    production_spatial_ready: bool
    canon_allowed: bool
    capture_id: str
    capture_sha256: str
    source_digest_sha256: str
    physical_realization_id: str
    matched_pncs_realization_ids: tuple[str,...]
    pncs_receipt_sha256: str
    blocker: str

def certify_source_realization_bridge(capture: Mapping[str,Any], pncs_receipt: Mapping[str,Any]) -> TIRSourceRealizationBridgeCertificateV09:
    capture_sha=canonical_capture_sha(capture)
    src=capture['source']
    source_class=reqstr(src.get('source_class'),'source.source_class')
    if source_class not in {'PRODUCTION_SOURCE','REFERENCE_CONTROL','CANDIDATE_SOURCE'}: raise TIRSourceRealizationBridgeError('unsupported source_class')
    immutable_ref=reqstr(src.get('immutable_ref'),'source.immutable_ref')
    source_digest=reqsha(src.get('source_digest_sha256'),'source.source_digest_sha256')
    physical_rid=reqstr(src.get('physical_realization_id'),'source.physical_realization_id')
    receipt_sha,bindings=verify_pncs_registry_receipt(pncs_receipt)
    if source_class=='PRODUCTION_SOURCE':
        if reqsha(src.get('capture_receipt_sha256'),'source.capture_receipt_sha256') != receipt_sha:
            raise TIRSourceRealizationBridgeError('capture receipt does not match PNCS provenance receipt')
    matches=[b for b in bindings if b['source_digest_sha256']==source_digest and b['source_locator']==immutable_ref]
    if not matches: raise TIRSourceRealizationBridgeError('no PNCS binding matches immutable source digest and locator')
    phase_ids=tuple(sorted({str(b['realization_id']) for b in matches}))
    if physical_rid in phase_ids: raise TIRSourceRealizationBridgeError('physical_realization_id must remain distinct from PNCS phase realization_id namespace')
    prod=source_class=='PRODUCTION_SOURCE'
    return TIRSourceRealizationBridgeCertificateV09(True,True,True,True,True,True,True,prod,prod,False,False,reqstr(capture.get('capture_id'),'capture_id'),capture_sha,source_digest,physical_rid,phase_ids,receipt_sha,'TIR_GSC1_A5_EDGE_REFINEMENT_AND_DOMAIN_WITNESSES_STILL_REQUIRED')

def certificate_receipt(cert):
    d={'schema':'QHTRI_TOE_TIR_GSC1_SOURCE_REALIZATION_BRIDGE_RECEIPT_V0_9','authority':'CANDIDATE_ONLY','physical_production_claim':False,**asdict(cert)}
    d['receipt_sha256']=sha256(d); return d
