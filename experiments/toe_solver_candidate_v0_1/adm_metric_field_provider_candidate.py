from __future__ import annotations
import math
from typing import Callable, Sequence
import numpy as np

SOURCE_REPOSITORY='AdrianLipa90/Relational-Field-Closure'
SOURCE_COMMIT='85bbb1d0754605be2720b6bd258b486b0a072345'
SOURCE_PATH='closure/einstein/RF_E8_ADM_KINEMATIC_ASSEMBLY_FIREWALL.md'
STATUS='CANDIDATE_EXACT_RF_E8_INTERFACE_NOT_PRODUCTION_FIELD_SOURCE'


def _spd3(h: Sequence[Sequence[float]]) -> np.ndarray:
    a=np.asarray(h,dtype=float)
    if a.shape!=(3,3) or not np.isfinite(a).all(): raise ValueError('h must be finite 3x3')
    if not np.allclose(a,a.T,rtol=0.0,atol=1e-12): raise ValueError('h must be symmetric')
    if np.min(np.linalg.eigvalsh(a))<=0.0: raise ValueError('h must be positive definite')
    return a


def adm_metric(lapse: float, h, shift) -> np.ndarray:
    n=float(lapse)
    if not math.isfinite(n) or n<=0.0: raise ValueError('N_R must be finite positive')
    H=_spd3(h)
    b=np.asarray(shift,dtype=float)
    if b.shape!=(3,) or not np.isfinite(b).all(): raise ValueError('shift must be finite length-3')
    bi=H@b
    b2=float(b@bi)
    g=np.empty((4,4),dtype=float)
    g[0,0]=-n*n+b2
    g[0,1:]=bi; g[1:,0]=bi; g[1:,1:]=H
    return g


def adm_inverse(lapse: float, h, shift) -> np.ndarray:
    n=float(lapse); H=_spd3(h); b=np.asarray(shift,dtype=float)
    if not math.isfinite(n) or n<=0.0: raise ValueError('N_R must be finite positive')
    if b.shape!=(3,) or not np.isfinite(b).all(): raise ValueError('shift must be finite length-3')
    Hi=np.linalg.inv(H); gi=np.empty((4,4),dtype=float)
    gi[0,0]=-1.0/(n*n)
    gi[0,1:]=b/(n*n); gi[1:,0]=b/(n*n)
    gi[1:,1:]=Hi-np.outer(b,b)/(n*n)
    return gi


def coframe_metric(lapse: float, triad, shift) -> np.ndarray:
    n=float(lapse); e=np.asarray(triad,dtype=float); b=np.asarray(shift,dtype=float)
    if not math.isfinite(n) or n<=0.0: raise ValueError('N_R must be finite positive')
    if e.shape!=(3,3) or not np.isfinite(e).all() or abs(np.linalg.det(e))<=1e-14: raise ValueError('triad must be finite invertible 3x3')
    if b.shape!=(3,) or not np.isfinite(b).all(): raise ValueError('shift must be finite length-3')
    E=np.zeros((4,4),dtype=float); E[0,0]=n; E[1:,0]=e@b; E[1:,1:]=e
    eta=np.diag([-1.0,1.0,1.0,1.0])
    return E.T@eta@E


def make_metric_fn(lapse_fn: Callable, h_fn: Callable, shift_fn: Callable):
    def metric_fn(x): return adm_metric(lapse_fn(x),h_fn(x),shift_fn(x)).tolist()
    return metric_fn
