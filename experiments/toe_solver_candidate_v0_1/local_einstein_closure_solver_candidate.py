from __future__ import annotations
import math
from dataclasses import dataclass
from typing import Sequence
import numpy as np
from scipy.optimize import lsq_linear

STATUS='CANDIDATE_LOCAL_CONSTRAINED_CLOSURE_NOT_CANONICAL'
SCOPE='zero-shift Lorentzian metric + Einstein tensor -> Lambda plus nonnegative orthonormal massless-stream pair couplings'


def _mat4(x, name='matrix'):
    a=np.asarray(x,dtype=float)
    if a.shape!=(4,4) or not np.all(np.isfinite(a)): raise ValueError(f'{name} must be finite 4x4')
    return a


def zero_shift_null_pair_bases(metric: Sequence[Sequence[float]]):
    g=_mat4(metric,'metric')
    if np.max(np.abs(g[0,1:]))>1e-12 or np.max(np.abs(g[1:,0]))>1e-12:
        raise ValueError('candidate solver requires zero-shift metric')
    if g[0,0]>=0: raise ValueError('timelike g00 required')
    h=g[1:,1:]
    ev=np.linalg.eigvalsh(h)
    if np.min(ev)<=0: raise ValueError('spatial metric must be SPD')
    N=math.sqrt(-float(g[0,0]))
    L=np.linalg.cholesky(h)
    e=L.T
    bases=[]
    for a in range(3):
        v=e[a,:]
        B=np.zeros((4,4),dtype=float)
        B[0,0]=N*N
        B[1:,1:]=np.outer(v,v)
        bases.append(B)
    return bases

@dataclass(frozen=True)
class ClosureSolution:
    cosmological_coordinate: float
    stream_pair_couplings: tuple[float,float,float]
    max_abs_residual: float
    rms_residual: float
    success: bool
    active_constraints: tuple[str,...]


def solve_positive_massless_pair_closure(einstein_tensor, metric, *, tolerance=1e-10):
    G=_mat4(einstein_tensor,'einstein_tensor'); g=_mat4(metric,'metric')
    B=zero_shift_null_pair_bases(g)
    A=np.stack([g.reshape(-1), *[-b.reshape(-1) for b in B]],axis=1)
    y=-G.reshape(-1)
    sol=lsq_linear(A,y,bounds=([-np.inf,0.,0.,0.],[np.inf,np.inf,np.inf,np.inf]),tol=1e-14,lsmr_tol=1e-14,max_iter=2000)
    x=sol.x
    R=G+x[0]*g-sum(x[j+1]*B[j] for j in range(3))
    mx=float(np.max(np.abs(R))); rms=float(np.sqrt(np.mean(R*R)))
    active=tuple(f'stream_pair_{j}_nonnegative_boundary' for j in range(3) if x[j+1] <= 1e-12)
    return ClosureSolution(float(x[0]),tuple(float(v) for v in x[1:]),mx,rms,bool(sol.success and mx<=float(tolerance)),active)


def solve_unconstrained_diagnostic(einstein_tensor, metric):
    G=_mat4(einstein_tensor,'einstein_tensor'); g=_mat4(metric,'metric'); B=zero_shift_null_pair_bases(g)
    A=np.stack([g.reshape(-1), *[-b.reshape(-1) for b in B]],axis=1); y=-G.reshape(-1)
    x=np.linalg.lstsq(A,y,rcond=None)[0]
    R=G+x[0]*g-sum(x[j+1]*B[j] for j in range(3))
    return {'coefficients':tuple(float(v) for v in x),'max_abs_residual':float(np.max(np.abs(R))),'requires_negative_stream_coupling':bool(np.any(x[1:]<0.0))}
