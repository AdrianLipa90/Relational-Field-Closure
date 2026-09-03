from __future__ import annotations
import math
from dataclasses import dataclass
from typing import Sequence
import numpy as np
from scipy.optimize import lsq_linear
from local_einstein_closure_solver_candidate import _mat4, zero_shift_null_pair_bases

STATUS='CANDIDATE_MULTI_SECTOR_SOURCE_CONE_NOT_CANONICAL'
SOURCE_RF_E7='AdrianLipa90/Relational-Field-Closure closure/einstein/RF_E7_TOTAL_SCALAR_STRESS_ENERGY_COMPOSITION.md'


def orthonormal_coframe(metric):
    g=_mat4(metric,'metric')
    if np.max(np.abs(g[0,1:]))>1e-12: raise ValueError('zero shift required')
    N=math.sqrt(-float(g[0,0])); h=g[1:,1:]; L=np.linalg.cholesky(h); e=L.T
    E=np.zeros((4,4)); E[0,0]=N; E[1:,1:]=e
    return E


def scalar_amplitude_gradient_bases(metric):
    E=orthonormal_coframe(metric); out=[]
    for axis in range(3):
        signs=np.full(3,-1.0); signs[axis]=1.0
        T_hat=np.diag([1.0,*signs])
        out.append(E.T @ T_hat @ E)
    return out


def maxwell_axis_bases(metric):
    E=orthonormal_coframe(metric); out=[]
    for axis in range(3):
        signs=np.ones(3); signs[axis]=-1.0
        T_hat=np.diag([1.0,*signs])
        out.append(E.T @ T_hat @ E)
    return out


def dust_basis(metric):
    E=orthonormal_coframe(metric)
    return E.T @ np.diag([1.0,0.0,0.0,0.0]) @ E

@dataclass(frozen=True)
class MultiSectorSolution:
    Lambda: float
    massless: tuple[float,float,float]
    scalar_amp: tuple[float,float,float]
    maxwell: tuple[float,float,float]
    dust: float
    max_abs_residual: float
    rms_residual: float
    success: bool


def solve_source_cone(einstein_tensor,metric,*,include_scalar=True,include_maxwell=False,include_dust=False,tolerance=1e-10):
    G=_mat4(einstein_tensor,'G'); g=_mat4(metric,'g')
    groups=[]; labels=[]
    B=zero_shift_null_pair_bases(g); groups.extend(B); labels.extend([('massless',i) for i in range(3)])
    if include_scalar:
        S=scalar_amplitude_gradient_bases(g); groups.extend(S); labels.extend([('scalar',i) for i in range(3)])
    if include_maxwell:
        M=maxwell_axis_bases(g); groups.extend(M); labels.extend([('maxwell',i) for i in range(3)])
    if include_dust:
        D=dust_basis(g); groups.append(D); labels.append(('dust',0))
    A=np.stack([g.reshape(-1),*[-b.reshape(-1) for b in groups]],axis=1); y=-G.reshape(-1)
    lo=np.r_[-np.inf,np.zeros(len(groups))]; hi=np.r_[np.inf,np.full(len(groups),np.inf)]
    q=lsq_linear(A,y,bounds=(lo,hi),method='bvls',tol=1e-14,max_iter=5000)
    x=q.x; R=G+x[0]*g-sum(x[i+1]*groups[i] for i in range(len(groups)))
    vals={'massless':[0.,0.,0.],'scalar':[0.,0.,0.],'maxwell':[0.,0.,0.],'dust':[0.]}
    for coeff,(kind,idx) in zip(x[1:],labels): vals[kind][idx]=float(coeff)
    mx=float(np.max(np.abs(R))); rms=float(np.sqrt(np.mean(R*R)))
    return MultiSectorSolution(float(x[0]),tuple(vals['massless']),tuple(vals['scalar']),tuple(vals['maxwell']),float(vals['dust'][0]),mx,rms,bool(q.success and mx<=tolerance))
