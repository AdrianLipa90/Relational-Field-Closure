from __future__ import annotations
import math
from typing import Callable, Sequence

STATUS='CANDIDATE_LOCAL_TETRAD_PROVIDER_NOT_CANONICAL'
SCOPE='RF-N0 lapse N_R + RF-02H isotropic hexahedral coframe -> local zero-shift 4D metric'
SOURCE_RFN0='AdrianLipa90/Relational-Field-Closure formalism/RFN0_RELATIONAL_LAPSE_CLOCK_DYNAMICS.md'
SOURCE_RF02H='AdrianLipa90/Relational-Field-Closure formalism/RF02H_HEXAHEDRAL_RANK3_SPATIAL_METRIC.md'

def relational_lapse(phi_x: float, phi_ref: float) -> float:
    px=float(phi_x); pr=float(phi_ref)
    if not math.isfinite(px) or not math.isfinite(pr) or px<=0.0 or pr<=0.0:
        raise ValueError('elapsed clock densities must be finite positive')
    return px/pr

def isotropic_hexahedral_scale(omega: float, c_scale: float=1.0) -> float:
    w=float(omega); c=float(c_scale)
    if not math.isfinite(w) or w==0.0: raise ValueError('omega must be finite nonzero')
    if not math.isfinite(c) or c<=0.0: raise ValueError('c_scale must be finite positive')
    return c/(math.sqrt(6.0)*abs(w))

def local_metric_from_fields(point: Sequence[float], lapse_fn: Callable[[Sequence[float]],float], omega_fn: Callable[[Sequence[float]],float], c_scale: float=1.0):
    x=tuple(float(v) for v in point)
    if len(x)!=4 or not all(math.isfinite(v) for v in x): raise ValueError('point must be finite 4-vector')
    N=float(lapse_fn(x)); w=float(omega_fn(x)); c=float(c_scale)
    if not math.isfinite(N) or N<=0.0: raise ValueError('N_R must be finite positive')
    a=isotropic_hexahedral_scale(w,c)
    return [
        [-(N*c)**2,0.0,0.0,0.0],
        [0.0,a*a,0.0,0.0],
        [0.0,0.0,a*a,0.0],
        [0.0,0.0,0.0,a*a],
    ]
