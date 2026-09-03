from __future__ import annotations

from dataclasses import dataclass, asdict
import hashlib
import json
import math
import re
from typing import Iterable, Sequence

HEX64 = re.compile(r'^[0-9a-f]{64}$')
EVIDENCE_CLASSES = {'PRODUCTION_SOURCE','REFERENCE_CONTROL','CANDIDATE_SOURCE'}

class ProductionSourceBundleError(ValueError):
    pass


def _finite(x, label):
    y=float(x)
    if not math.isfinite(y):
        raise ProductionSourceBundleError(f'{label} must be finite')
    return y


def _vec3(v,label):
    if len(v)!=3: raise ProductionSourceBundleError(f'{label} must have length 3')
    return tuple(_finite(x,label) for x in v)


def _mat3(a,label):
    if len(a)!=3 or any(len(r)!=3 for r in a):
        raise ProductionSourceBundleError(f'{label} must be 3x3')
    return tuple(tuple(_finite(x,label) for x in r) for r in a)


def _mv(a,v): return tuple(sum(a[i][j]*v[j] for j in range(3)) for i in range(3))
def _mm(a,b): return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(3)) for j in range(3)) for i in range(3))
def _add(a,b): return tuple(a[i]+b[i] for i in range(3))
def _sub(a,b): return tuple(a[i]-b[i] for i in range(3))
def _vmax(a,b): return max(abs(a[i]-b[i]) for i in range(3))
def _mmax(a,b): return max(abs(a[i][j]-b[i][j]) for i in range(3) for j in range(3))

@dataclass(frozen=True)
class SourceProvenance:
    source_id: str
    evidence_class: str
    immutable_ref: str
    receipt_sha256: str | None
    physical_realization_id: str | None

    def validate(self) -> None:
        if not self.source_id or not self.immutable_ref:
            raise ProductionSourceBundleError('source_id and immutable_ref are required')
        if self.evidence_class not in EVIDENCE_CLASSES:
            raise ProductionSourceBundleError('unsupported evidence_class')
        if self.evidence_class == 'PRODUCTION_SOURCE':
            if not self.receipt_sha256 or not HEX64.fullmatch(self.receipt_sha256):
                raise ProductionSourceBundleError('PRODUCTION_SOURCE requires 64-hex receipt_sha256')
            if not self.physical_realization_id:
                raise ProductionSourceBundleError('PRODUCTION_SOURCE requires physical_realization_id')
        elif self.receipt_sha256 is not None and not HEX64.fullmatch(self.receipt_sha256):
            raise ProductionSourceBundleError('receipt_sha256 must be 64-hex when supplied')

    @property
    def is_production(self):
        return self.evidence_class == 'PRODUCTION_SOURCE'

@dataclass(frozen=True)
class ClockActivityEdge:
    x: str
    y: str
    activity_x: float
    activity_y: float

    @property
    def ratio(self):
        ax=_finite(self.activity_x,'activity_x'); ay=_finite(self.activity_y,'activity_y')
        if ax<=0 or ay<=0: raise ProductionSourceBundleError('clock activities must be strictly positive')
        return ax/ay

@dataclass(frozen=True)
class ClockCapture:
    provenance: SourceProvenance
    edges: tuple[ClockActivityEdge,...]
    reference: str
    event_complex_certificate_sha256: str | None
    smooth_domain_certificate_sha256: str | None
    domain_coverage_witness_supplied: bool

@dataclass(frozen=True)
class ClockCertificate:
    relative_rates: dict[str,float]
    max_cycle_residual: float
    graph_connected: bool
    production_ready: bool


def certify_clock_capture(c: ClockCapture, tol=1e-10) -> ClockCertificate:
    c.provenance.validate()
    if not c.edges: raise ProductionSourceBundleError('clock capture requires edges')
    nodes=set(); adj={}; clean=[]
    for e in c.edges:
        if not e.x or not e.y: raise ProductionSourceBundleError('clock node ids required')
        r=e.ratio
        nodes.update((e.x,e.y)); adj.setdefault(e.x,[]); adj.setdefault(e.y,[])
        if e.x==e.y:
            if abs(r-1)>tol: raise ProductionSourceBundleError('clock self-ratio must equal one')
        else:
            adj[e.y].append((e.x,r)); adj[e.x].append((e.y,1/r))
        clean.append((e.x,e.y,r))
    if c.reference not in nodes: raise ProductionSourceBundleError('clock reference absent')
    rates={c.reference:1.0}; q=[c.reference]; maxr=0.0
    while q:
        s=q.pop(0)
        for t,f in adj[s]:
            cand=rates[s]*f
            if t not in rates:
                rates[t]=cand; q.append(t)
            else:
                rr=abs(rates[t]-cand)/max(1.0,abs(rates[t]),abs(cand)); maxr=max(maxr,rr)
                if rr>tol: raise ProductionSourceBundleError('multiplicative clock cycle closure failed')
    if len(rates)!=len(nodes): raise ProductionSourceBundleError('clock graph disconnected')
    for x,y,r in clean:
        pred=rates[x]/rates[y]
        rr=abs(pred-r)/max(1.0,abs(pred),abs(r)); maxr=max(maxr,rr)
        if rr>tol: raise ProductionSourceBundleError('clock edge incompatible with global potential')
    hashes_ok=all(h is not None and HEX64.fullmatch(h) for h in (
        c.event_complex_certificate_sha256,c.smooth_domain_certificate_sha256))
    ready=bool(c.provenance.is_production and hashes_ok and c.domain_coverage_witness_supplied)
    return ClockCertificate(dict(sorted(rates.items())),maxr,True,ready)

@dataclass(frozen=True)
class SpatialCapture:
    provenance: SourceProvenance
    tir_global_complex_certificate_sha256: str | None
    tir_edge_refinement_certificate_sha256: str | None
    global_complex_promotion_eligible: bool
    edge_refinement_ready: bool
    overlap_cocycle_witness_supplied: bool
    domain_coverage_witness_supplied: bool

@dataclass(frozen=True)
class SpatialCertificate:
    production_ready: bool


def certify_spatial_capture(s: SpatialCapture) -> SpatialCertificate:
    s.provenance.validate()
    hashes_ok=all(h is not None and HEX64.fullmatch(h) for h in (
        s.tir_global_complex_certificate_sha256,s.tir_edge_refinement_certificate_sha256))
    ready=bool(s.provenance.is_production and hashes_ok and s.global_complex_promotion_eligible
               and s.edge_refinement_ready and s.overlap_cocycle_witness_supplied
               and s.domain_coverage_witness_supplied)
    return SpatialCertificate(ready)

@dataclass(frozen=True)
class ShiftPatch:
    name: str
    shift: tuple[float,float,float]

@dataclass(frozen=True)
class ShiftTransition:
    source: str
    target: str
    spatial_jacobian: tuple[tuple[float,float,float],...]
    time_drift: tuple[float,float,float]

@dataclass(frozen=True)
class ShiftCapture:
    provenance: SourceProvenance
    patches: tuple[ShiftPatch,...]
    transitions: tuple[ShiftTransition,...]
    triangles: tuple[tuple[str,str,str],...]
    global_flow_coverage_witness_supplied: bool
    global_clock_properness_witness_supplied: bool
    physical_event_placement_witness_supplied: bool

@dataclass(frozen=True)
class ShiftCertificate:
    max_shift_overlap_residual: float
    max_transition_cocycle_residual: float
    max_time_drift_cocycle_residual: float
    production_ready: bool


def certify_shift_capture(c: ShiftCapture, tol=1e-12) -> ShiftCertificate:
    c.provenance.validate()
    if not c.patches: raise ProductionSourceBundleError('shift capture requires patches')
    pm={}
    for p in c.patches:
        if not p.name or p.name in pm: raise ProductionSourceBundleError('invalid/duplicate shift patch')
        pm[p.name]=_vec3(p.shift,'shift')
    tm={}; max_shift=0.0
    for t in c.transitions:
        if t.source not in pm or t.target not in pm or t.source==t.target:
            raise ProductionSourceBundleError('shift transition references invalid patch')
        key=(t.source,t.target)
        if key in tm: raise ProductionSourceBundleError('duplicate shift transition')
        A=_mat3(t.spatial_jacobian,'spatial_jacobian'); v=_vec3(t.time_drift,'time_drift')
        tm[key]=(A,v)
        exp=_sub(_mv(A,pm[t.source]),v)
        r=_vmax(exp,pm[t.target]); max_shift=max(max_shift,r)
        if r>tol: raise ProductionSourceBundleError('GSC3A shift overlap law failed')
    adj={n:set() for n in pm}
    for a,b in tm: adj[a].add(b); adj[b].add(a)
    seen={next(iter(pm))}; st=list(seen)
    while st:
        a=st.pop()
        for b in adj[a]-seen: seen.add(b); st.append(b)
    if seen!=set(pm): raise ProductionSourceBundleError('shift atlas disconnected')
    ma=mv=0.0
    for p,q,r in c.triangles:
        try: (Aqp,vqp),(Arq,vrq),(Arp,vrp)=tm[(p,q)],tm[(q,r)],tm[(p,r)]
        except KeyError as e: raise ProductionSourceBundleError('shift triangle missing direct transitions') from e
        ar=_mmax(_mm(Arq,Aqp),Arp); vr=_vmax(_add(vrq,_mv(Arq,vqp)),vrp)
        ma=max(ma,ar); mv=max(mv,vr)
        if ar>tol or vr>tol: raise ProductionSourceBundleError('shift transition cocycle failed')
    ready=bool(c.provenance.is_production and c.global_flow_coverage_witness_supplied
               and c.global_clock_properness_witness_supplied
               and c.physical_event_placement_witness_supplied)
    return ShiftCertificate(max_shift,ma,mv,ready)

@dataclass(frozen=True)
class ProductionSourceBundle:
    clock: ClockCapture
    spatial: SpatialCapture
    shift: ShiftCapture

@dataclass(frozen=True)
class ProductionBundleCertificate:
    clock: ClockCertificate
    spatial: SpatialCertificate
    shift: ShiftCertificate
    same_physical_realization: bool
    production_admitted: bool
    blockers: tuple[str,...]


def certify_production_bundle(b: ProductionSourceBundle) -> ProductionBundleCertificate:
    cc=certify_clock_capture(b.clock); sc=certify_spatial_capture(b.spatial); xc=certify_shift_capture(b.shift)
    ids=[b.clock.provenance.physical_realization_id,b.spatial.provenance.physical_realization_id,b.shift.provenance.physical_realization_id]
    same=bool(all(x is not None for x in ids) and len(set(ids))==1)
    blockers=[]
    if not cc.production_ready: blockers.append('CLOCK_SOURCE_WITNESS')
    if not sc.production_ready: blockers.append('SPATIAL_SOURCE_WITNESS')
    if not xc.production_ready: blockers.append('SHIFT_FLOW_SOURCE_WITNESS')
    if not same: blockers.append('SAME_PHYSICAL_REALIZATION_BINDING')
    admitted=not blockers
    return ProductionBundleCertificate(cc,sc,xc,same,admitted,tuple(blockers))


def certificate_json(cert: ProductionBundleCertificate):
    return json.dumps(asdict(cert),sort_keys=True,separators=(',',':'))

def certificate_sha256(cert: ProductionBundleCertificate):
    return hashlib.sha256(certificate_json(cert).encode()).hexdigest()
