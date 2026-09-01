from __future__ import annotations

from dataclasses import dataclass
from collections import deque
import math
import numpy as np


class ProductionLapsePacketError(ValueError):
    pass


@dataclass(frozen=True)
class ClockRatioEdge:
    x: str
    y: str
    ratio_x_over_y: float


@dataclass(frozen=True)
class LapseEventEmbedding:
    event: str
    coordinates: tuple[float, float, float, float]


@dataclass(frozen=True)
class AffineLogLapseModel:
    reference: str
    coefficients: np.ndarray  # [b,a0,a1,a2,a3], log N = b + a_mu x^mu
    relative_rates: dict[str, float]
    graph_residual: float
    fit_residual: float
    design_rank: int
    domain_coverage_witness_supplied: bool
    provenance_id: str

    def log_lapse(self, x) -> float:
        x = np.asarray(x, dtype=float)
        if x.shape != (4,) or not np.all(np.isfinite(x)):
            raise ProductionLapsePacketError('x must be finite shape (4,)')
        return float(self.coefficients[0] + np.dot(self.coefficients[1:], x))

    def lapse(self, x) -> float:
        value = math.exp(self.log_lapse(x))
        if not math.isfinite(value) or value <= 0.0:
            raise ProductionLapsePacketError('lapse left positive finite domain')
        return value

    @property
    def production_ready(self) -> bool:
        return bool(self.domain_coverage_witness_supplied)


def reconstruct_relative_rates(edges, reference: str, tolerance: float = 1e-10):
    edges = tuple(edges)
    if not edges:
        raise ProductionLapsePacketError('at least one clock-ratio edge required')
    adj: dict[str, list[tuple[str,float]]] = {}
    clean = []
    nodes = set()
    for edge in edges:
        if not isinstance(edge, ClockRatioEdge):
            raise ProductionLapsePacketError('all edges must be ClockRatioEdge')
        r = float(edge.ratio_x_over_y)
        if not math.isfinite(r) or r <= 0:
            raise ProductionLapsePacketError('clock ratios must be finite positive')
        nodes.update((edge.x, edge.y))
        adj.setdefault(edge.x, []).append((edge.y, 1.0/r))
        adj.setdefault(edge.y, []).append((edge.x, r))
        clean.append((edge.x, edge.y, r))
    if reference not in nodes:
        raise ProductionLapsePacketError('reference must occur in ratio graph')
    rates = {reference: 1.0}
    q = deque([reference])
    max_res = 0.0
    while q:
        s = q.popleft()
        for t,factor in adj.get(s,[]):
            cand = rates[s]*factor
            if t not in rates:
                rates[t] = cand
                q.append(t)
            else:
                scale=max(1.0,abs(cand),abs(rates[t]))
                res=abs(cand-rates[t])/scale
                max_res=max(max_res,res)
                if res > tolerance:
                    raise ProductionLapsePacketError('multiplicative clock cycle closure failed')
    if len(rates)!=len(nodes):
        raise ProductionLapsePacketError('clock-ratio graph disconnected')
    for x,y,r in clean:
        pred=rates[x]/rates[y]
        scale=max(1.0,abs(pred),abs(r))
        res=abs(pred-r)/scale
        max_res=max(max_res,res)
        if res>tolerance:
            raise ProductionLapsePacketError('clock edge inconsistent with reconstructed rates')
    return dict(sorted(rates.items())), max_res


def fit_affine_log_lapse(*, edges, embeddings, reference: str, provenance_id: str,
                         domain_coverage_witness_supplied: bool=False,
                         graph_tolerance: float=1e-10, fit_tolerance: float=1e-9):
    if not provenance_id:
        raise ProductionLapsePacketError('provenance_id required')
    rates, graph_res = reconstruct_relative_rates(edges, reference, graph_tolerance)
    embeddings = tuple(embeddings)
    by_event = {}
    for emb in embeddings:
        if not isinstance(emb, LapseEventEmbedding):
            raise ProductionLapsePacketError('all embeddings must be LapseEventEmbedding')
        x=np.asarray(emb.coordinates,dtype=float)
        if x.shape!=(4,) or not np.all(np.isfinite(x)):
            raise ProductionLapsePacketError('embedding coordinates must be finite shape (4,)')
        if emb.event in by_event:
            raise ProductionLapsePacketError('duplicate event embedding')
        if emb.event not in rates:
            raise ProductionLapsePacketError('embedding event absent from ratio graph')
        by_event[emb.event]=x
    if set(by_event)!=set(rates):
        raise ProductionLapsePacketError('every clock node requires exactly one embedding')
    A=[]; y=[]
    for event,x in sorted(by_event.items()):
        A.append(np.r_[1.0,x])
        y.append(math.log(rates[event]/rates[reference]))
    A=np.asarray(A,float); y=np.asarray(y,float)
    rank=int(np.linalg.matrix_rank(A))
    if rank<5:
        raise ProductionLapsePacketError(f'affine log-lapse witness underdetermined: rank={rank}<5')
    coeff,*_=np.linalg.lstsq(A,y,rcond=None)
    pred=A@coeff
    fit_res=float(np.max(np.abs(pred-y)))
    if fit_res>fit_tolerance:
        raise ProductionLapsePacketError(f'affine log-lapse residual {fit_res} exceeds tolerance')
    return AffineLogLapseModel(reference, coeff, rates, graph_res, fit_res, rank,
                               bool(domain_coverage_witness_supplied), provenance_id)
