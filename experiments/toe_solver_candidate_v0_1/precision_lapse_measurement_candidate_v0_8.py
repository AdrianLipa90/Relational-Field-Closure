from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal, localcontext
from typing import Hashable, Iterable, Sequence
import json, hashlib

class PrecisionClockError(ValueError):
    pass

D = Decimal


def dec(value, label='value') -> Decimal:
    try:
        out = D(str(value))
    except Exception as exc:
        raise PrecisionClockError(f'{label} must parse as Decimal') from exc
    if not out.is_finite():
        raise PrecisionClockError(f'{label} must be finite')
    return out


def log_ratio_from_fractional_offset(delta, *, precision: int = 80) -> Decimal:
    d = dec(delta, 'fractional offset')
    if d <= -1:
        raise PrecisionClockError('fractional offset must satisfy delta > -1')
    with localcontext() as ctx:
        ctx.prec = precision
        return +(D(1) + d).ln()


def fractional_offset_from_log_ratio(log_n, *, precision: int = 80) -> Decimal:
    x = dec(log_n, 'log ratio')
    with localcontext() as ctx:
        ctx.prec = precision
        return +(x.exp() - D(1))

@dataclass(frozen=True)
class LogClockCertificate:
    reference: str
    log_rates: dict[str, str]
    fractional_offsets: dict[str, str]
    max_log_residual: str
    edge_count: int
    precision_digits: int


def reconstruct_log_clock_potential(
    edges: Iterable[tuple[Hashable, Hashable, str]],
    *,
    reference: Hashable | None = None,
    tolerance_log: str = '1e-30',
    precision: int = 80,
) -> LogClockCertificate:
    edge_list = list(edges)
    if not edge_list:
        raise PrecisionClockError('at least one log-ratio edge is required')
    tol = dec(tolerance_log, 'tolerance_log')
    if tol <= 0:
        raise PrecisionClockError('tolerance_log must be positive')

    nodes=set(); adj={}; clean=[]
    for x,y,raw in edge_list:
        l=dec(raw,'log_N_x_given_y')
        nodes.update((x,y)); adj.setdefault(x,[]); adj.setdefault(y,[])
        clean.append((x,y,l))
        if x==y:
            if abs(l)>tol: raise PrecisionClockError('self log-ratio must be zero')
            continue
        adj[y].append((x,l)); adj[x].append((y,l.copy_negate()))

    if reference is None:
        reference=sorted(nodes,key=str)[0]
    if reference not in nodes:
        raise PrecisionClockError('reference clock must occur in graph')

    with localcontext() as ctx:
        ctx.prec=precision
        rates={reference:D(0)}; queue=[reference]; maxr=D(0)
        while queue:
            s=queue.pop(0)
            for t,inc in adj[s]:
                cand=rates[s]+inc
                if t not in rates:
                    rates[t]=cand; queue.append(t)
                else:
                    r=abs(rates[t]-cand); maxr=max(maxr,r)
                    if r>tol: raise PrecisionClockError(f'additive log cocycle failed: residual={r}')
        if len(rates)!=len(nodes): raise PrecisionClockError('clock graph disconnected')
        for x,y,l in clean:
            r=abs((rates[x]-rates[y])-l); maxr=max(maxr,r)
            if r>tol: raise PrecisionClockError(f'log edge incompatible with global potential: residual={r}')
        offsets={str(k):str(+(rates[k].exp()-D(1))) for k in sorted(rates,key=str)}
        out_rates={str(k):str(+rates[k]) for k in sorted(rates,key=str)}
        return LogClockCertificate(str(reference),out_rates,offsets,str(+maxr),len(clean),precision)

@dataclass(frozen=True)
class WeightedSlopeCertificate:
    slope: str
    sigma_slope: str
    chi2: str
    dof: int
    point_count: int
    scale: str


def weighted_slope_through_origin(
    x: Sequence[str], y: Sequence[str], sigma: Sequence[str], *, scale: str='1', precision: int=80
) -> WeightedSlopeCertificate:
    if not (len(x)==len(y)==len(sigma)) or len(x)<2:
        raise PrecisionClockError('x,y,sigma must have equal length >=2')
    sc=dec(scale,'scale')
    if sc<=0: raise PrecisionClockError('scale must be positive')
    with localcontext() as ctx:
        ctx.prec=precision
        xx=[dec(v,'x') for v in x]
        yy=[dec(v,'y')/sc for v in y]
        ss=[dec(v,'sigma')/sc for v in sigma]
        if any(s<=0 for s in ss): raise PrecisionClockError('sigma must be positive')
        w=[D(1)/(s*s) for s in ss]
        denom=sum(wi*xi*xi for wi,xi in zip(w,xx))
        if denom<=0: raise PrecisionClockError('singular weighted fit')
        slope=sum(wi*xi*yi for wi,xi,yi in zip(w,xx,yy))/denom
        sig=(D(1)/denom).sqrt()
        chi=sum(wi*(yi-slope*xi)**2 for wi,xi,yi in zip(w,xx,yy))
        return WeightedSlopeCertificate(str(+slope),str(+sig),str(+chi),len(xx)-1,len(xx),str(sc))


def stable_receipt_sha(obj) -> str:
    raw=json.dumps(obj,sort_keys=True,separators=(',',':')).encode()
    return hashlib.sha256(raw).hexdigest()
