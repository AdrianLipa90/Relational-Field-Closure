from __future__ import annotations
from dataclasses import dataclass, asdict
import hashlib,json,math
from typing import Any,Mapping
from tir_gsc1_source_realization_bridge_v0_9 import verify_pncs_registry_receipt,reqstr,reqsha,sha256,TIRSourceRealizationBridgeError

SCHEMA='TIR_INTERLEAF_MATCHING_FIELD_INPUT_V0_1'
class TIRInterleafSourceBridgeError(ValueError): pass

def finite(x,label):
    if isinstance(x,bool): raise TIRInterleafSourceBridgeError(f'{label} must be finite number')
    y=float(x)
    if not math.isfinite(y): raise TIRInterleafSourceBridgeError(f'{label} must be finite number')
    return y
def vec3(v,label):
    if not isinstance(v,(list,tuple)) or len(v)!=3: raise TIRInterleafSourceBridgeError(f'{label} must be vec3')
    return tuple(finite(x,label) for x in v)
def mat3(a,label):
    if not isinstance(a,(list,tuple)) or len(a)!=3: raise TIRInterleafSourceBridgeError(f'{label} must be 3x3')
    return tuple(vec3(r,label) for r in a)
def matvec(a,v): return tuple(sum(a[i][k]*v[k] for k in range(3)) for i in range(3))
def sub(a,b): return tuple(a[i]-b[i] for i in range(3))
def maxres(a,b): return max(abs(a[i]-b[i]) for i in range(3))

def canonical_payload(kind,c_scale,patches,overlaps):
    return {'temporal_coordinate_kind':kind,'c_scale':c_scale,
      'patches':sorted([{'patch_id':p['patch_id'],'beta_match':list(p['beta_match'])} for p in patches],key=lambda x:x['patch_id']),
      'overlaps':sorted([{'source':o['source'],'target':o['target'],'spatial_jacobian':[list(r) for r in o['spatial_jacobian']],'time_drift':list(o['time_drift'])} for o in overlaps],key=lambda x:(x['source'],x['target']))}
def payload_sha(kind,c_scale,patches,overlaps): return sha256(canonical_payload(kind,c_scale,patches,overlaps))

@dataclass(frozen=True)
class TIRInterleafSourceBridgeCertificateV10:
    input_valid: bool
    integrity_valid: bool
    handoff_compatible: bool
    pncs_provenance_receipt_valid: bool
    immutable_source_bound: bool
    physical_realization_declared: bool
    phase_realization_kept_separate: bool
    production_input: bool
    tir_promotion_eligible: bool
    rfc_shift_derived_downstream: bool
    rfc_source_witness_required: bool
    canon_allowed: bool
    dataset_id: str
    payload_sha256: str
    physical_realization_id: str
    source_digest_sha256: str
    pncs_receipt_sha256: str
    matched_pncs_realization_ids: tuple[str,...]
    max_matching_residual: float
    rfe8_shift_packet: dict[str,Any]

def certify_interleaf_source_bridge(data:Mapping[str,Any],pncs_receipt:Mapping[str,Any],atol=1e-12):
    if not isinstance(data,Mapping) or data.get('schema')!=SCHEMA: raise TIRInterleafSourceBridgeError('dataset schema mismatch')
    did=reqstr(data.get('dataset_id'),'dataset_id')
    if type(data.get('production')) is not bool: raise TIRInterleafSourceBridgeError('production must be bool')
    prov=data.get('provenance')
    if not isinstance(prov,Mapping): raise TIRInterleafSourceBridgeError('provenance must be object')
    locator=reqstr(prov.get('source_commit_or_digest'),'provenance.source_commit_or_digest')
    source_digest=reqsha(prov.get('source_digest_sha256'),'provenance.source_digest_sha256')
    physical=reqstr(prov.get('physical_realization_id'),'provenance.physical_realization_id')
    coord=data.get('temporal_coordinate')
    if not isinstance(coord,Mapping): raise TIRInterleafSourceBridgeError('temporal_coordinate must be object')
    kind=reqstr(coord.get('kind'),'temporal_coordinate.kind')
    if kind not in {'t','x0'} or coord.get('x0_binding')!='x0=c*t': raise TIRInterleafSourceBridgeError('coordinate contract mismatch')
    c=finite(coord.get('c_scale'),'c_scale')
    if c<=0: raise TIRInterleafSourceBridgeError('c_scale must be positive')
    rawp=data.get('patches'); rawo=data.get('overlaps')
    if not isinstance(rawp,list) or not rawp or not isinstance(rawo,list): raise TIRInterleafSourceBridgeError('patches/overlaps malformed')
    patches=[]; ids=set()
    for p in rawp:
        pid=reqstr(p.get('patch_id'),'patch_id')
        if pid in ids: raise TIRInterleafSourceBridgeError('duplicate patch id')
        ids.add(pid); patches.append({'patch_id':pid,'beta_match':vec3(p.get('beta_match'),'beta_match')})
    pm={p['patch_id']:p['beta_match'] for p in patches}; overlaps=[]; keys=set(); mr=0.0
    for o in rawo:
        s=reqstr(o.get('source'),'overlap.source'); t=reqstr(o.get('target'),'overlap.target')
        if s==t or s not in pm or t not in pm or (s,t) in keys: raise TIRInterleafSourceBridgeError('invalid overlap')
        keys.add((s,t)); a=mat3(o.get('spatial_jacobian'),'spatial_jacobian'); v=vec3(o.get('time_drift'),'time_drift')
        r=maxres(sub(matvec(a,pm[s]),v),pm[t]); mr=max(mr,r)
        if r>atol: raise TIRInterleafSourceBridgeError(f'matching handoff residual exceeds tolerance: {r}')
        overlaps.append({'source':s,'target':t,'spatial_jacobian':a,'time_drift':v})
    computed=payload_sha(kind,c,patches,overlaps)
    if reqsha(data.get('payload_sha256'),'payload_sha256')!=computed: raise TIRInterleafSourceBridgeError('payload_sha256 mismatch')
    receipt_sha,bindings=verify_pncs_registry_receipt(pncs_receipt)
    if data['production']:
        if reqsha(prov.get('capture_receipt_sha256'),'provenance.capture_receipt_sha256')!=receipt_sha: raise TIRInterleafSourceBridgeError('capture receipt does not match PNCS receipt')
    matches=[b for b in bindings if b['source_digest_sha256']==source_digest and b['source_locator']==locator]
    if not matches: raise TIRInterleafSourceBridgeError('no PNCS binding matches matching-field source')
    phase_ids=tuple(sorted({str(b['realization_id']) for b in matches}))
    if physical in phase_ids: raise TIRInterleafSourceBridgeError('physical realization must remain distinct from PNCS phase realization')
    divisor=c if kind=='t' else 1.0
    packet={'schema':'TIR_TO_RFC_RFE8_SHIFT_HANDOFF_V0_1','source_dataset_id':did,'coordinate':'x0','x0_binding':'x0=c*t',
      'patches':[{'patch_id':p['patch_id'],'b_x0':[x/divisor for x in p['beta_match']]} for p in patches],
      'overlaps':[{'source':o['source'],'target':o['target'],'spatial_jacobian':[list(r) for r in o['spatial_jacobian']],'time_drift_x0':[x/divisor for x in o['time_drift']]} for o in overlaps]}
    prod=bool(data['production'])
    return TIRInterleafSourceBridgeCertificateV10(True,True,True,True,True,True,True,prod,prod,True,False,False,did,computed,physical,source_digest,receipt_sha,phase_ids,mr,packet)

def receipt(cert):
    d={'schema':'QHTRI_TOE_TIR_INTERLEAF_SOURCE_REALIZATION_BRIDGE_RECEIPT_V0_10','authority':'CANDIDATE_ONLY','physical_production_claim':False,**asdict(cert)}; d['receipt_sha256']=sha256(d); return d
