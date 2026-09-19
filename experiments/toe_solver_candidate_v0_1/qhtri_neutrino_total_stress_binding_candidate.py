from __future__ import annotations
import math
from typing import Sequence
STATUS='CANDIDATE_BINDING_NOT_CANONICAL'
SCOPE='IDT massless neutrino integrated stress -> RFC total Einstein source assembly interface'
IDT_SOURCE='AdrianLipa90/Informational-Dynamics-of-Time src/idt/neutrino_physical_stress.py'
RFC_SOURCE='AdrianLipa90/Relational-Field-Closure src/rfc/total_einstein_source_assembly.py'

def _mat4(m):
    if len(m)!=4 or any(len(r)!=4 for r in m): raise ValueError('matrix must be 4x4')
    out=tuple(tuple(float(x) for x in r) for r in m)
    if not all(math.isfinite(x) for r in out for x in r): raise ValueError('matrix must be finite')
    return out

def _add(*ms):
    ps=[_mat4(m) for m in ms]
    return tuple(tuple(sum(m[i][j] for m in ps) for j in range(4)) for i in range(4))
def _scale(s,m):
    s=float(s); a=_mat4(m)
    if not math.isfinite(s): raise ValueError('scale finite')
    return tuple(tuple(s*a[i][j] for j in range(4)) for i in range(4))

def integrated_massless_stress(directions: Sequence[Sequence[float]], energies: Sequence[float]):
    if len(directions)==0 or len(directions)!=len(energies): raise ValueError('equal nonzero streams required')
    T=[[0.0]*4 for _ in range(4)]
    for d,E0 in zip(directions,energies):
        if len(d)!=3: raise ValueError('direction must be 3D')
        E=float(E0); v=[float(x) for x in d]
        n=math.sqrt(sum(x*x for x in v))
        if not math.isfinite(E) or E<0 or not math.isfinite(n) or n<=0: raise ValueError('invalid stream')
        v=[x/n for x in v]; k=[1.0,*v]
        for mu in range(4):
            for nu in range(4): T[mu][nu]+=E*k[mu]*k[nu]
    return tuple(tuple(r) for r in T)

def assemble_fixed_reference_source(rest_source, metric, *, eta, u_hat, projector_stress):
    return _add(rest_source,_scale(-(1.0-float(eta))*float(u_hat),metric),projector_stress)
def assemble_dynamic_lambda_source(rest_source, metric, *, eta, u_hat, projector_stress):
    return _add(rest_source,_scale(float(eta)*float(u_hat),metric),projector_stress)
def lambda0_from_reference(lambda_star,kappa_e,u_hat): return float(lambda_star)+float(kappa_e)*float(u_hat)
def einstein_residual(G,g,Lambda,kappa,T): return _add(G,_scale(Lambda,g),_scale(-kappa,T))
def dynamic_bianchi_residual_from_fixed(kappa_e,fixed_source_divergence,grad_u_hat):
    k=float(kappa_e); d=tuple(float(x) for x in fixed_source_divergence); u=tuple(float(x) for x in grad_u_hat)
    if len(d)!=4 or len(u)!=4 or k<=0: raise ValueError('bad bianchi inputs')
    return tuple(k*(d[i]+u[i])-k*u[i] for i in range(4))
