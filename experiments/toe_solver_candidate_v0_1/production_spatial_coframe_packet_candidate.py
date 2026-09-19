from __future__ import annotations

from dataclasses import dataclass
import numpy as np


class ProductionSpatialPacketError(ValueError):
    pass


@dataclass(frozen=True)
class RelationalEdgeSample:
    basepoint: tuple[float,float,float,float]
    coordinate_displacement: tuple[float,float,float]
    internal_displacement: tuple[float,float,float]


@dataclass(frozen=True)
class AffineCoframeModel:
    coefficients: np.ndarray  # shape (3 internal, 3 spatial, 5 affine spacetime coeffs)
    fit_residual: float
    design_rank: int
    min_abs_det_coframe: float
    min_metric_eigenvalue: float
    overlap_cocycle_witness_supplied: bool
    domain_coverage_witness_supplied: bool
    provenance_id: str

    def coframe(self, x) -> np.ndarray:
        x=np.asarray(x,dtype=float)
        if x.shape!=(4,) or not np.all(np.isfinite(x)):
            raise ProductionSpatialPacketError('x must be finite shape (4,)')
        phi=np.r_[1.0,x]
        e=np.einsum('aik,k->ai',self.coefficients,phi)
        if not np.all(np.isfinite(e)):
            raise ProductionSpatialPacketError('coframe nonfinite')
        return e

    def spatial_metric(self,x)->np.ndarray:
        e=self.coframe(x)
        h=e.T@e
        vals=np.linalg.eigvalsh(h)
        if float(vals[0])<=0:
            raise ProductionSpatialPacketError('spatial metric not positive definite')
        return h

    @property
    def production_ready(self)->bool:
        return bool(self.overlap_cocycle_witness_supplied and self.domain_coverage_witness_supplied)


def _design_row(sample: RelationalEdgeSample):
    x=np.asarray(sample.basepoint,dtype=float)
    dx=np.asarray(sample.coordinate_displacement,dtype=float)
    E=np.asarray(sample.internal_displacement,dtype=float)
    if x.shape!=(4,) or dx.shape!=(3,) or E.shape!=(3,):
        raise ProductionSpatialPacketError('bad sample shape')
    if not (np.all(np.isfinite(x)) and np.all(np.isfinite(dx)) and np.all(np.isfinite(E))):
        raise ProductionSpatialPacketError('sample must be finite')
    if np.linalg.norm(dx)<=0:
        raise ProductionSpatialPacketError('coordinate displacement must be nonzero')
    phi=np.r_[1.0,x]
    # flatten (i,k): E_a = sum_i sum_k c[a,i,k] dx_i phi_k
    return np.concatenate([dx[i]*phi for i in range(3)]), E


def fit_affine_coframe(*, samples, provenance_id: str,
                       overlap_cocycle_witness_supplied: bool=False,
                       domain_coverage_witness_supplied: bool=False,
                       fit_tolerance: float=1e-9,
                       det_tolerance: float=1e-9,
                       metric_eigen_tolerance: float=1e-12):
    if not provenance_id:
        raise ProductionSpatialPacketError('provenance_id required')
    rows=[]; targets=[]; points=[]
    for s in tuple(samples):
        if not isinstance(s,RelationalEdgeSample):
            raise ProductionSpatialPacketError('all samples must be RelationalEdgeSample')
        row,E=_design_row(s); rows.append(row); targets.append(E); points.append(np.asarray(s.basepoint,float))
    if not rows:
        raise ProductionSpatialPacketError('at least one edge sample required')
    A=np.asarray(rows,float); Y=np.asarray(targets,float)
    rank=int(np.linalg.matrix_rank(A))
    if rank<15:
        raise ProductionSpatialPacketError(f'affine coframe witness underdetermined: rank={rank}<15')
    Cflat,*_=np.linalg.lstsq(A,Y,rcond=None)  # shape 15x3
    pred=A@Cflat
    fit_res=float(np.max(np.abs(pred-Y)))
    if fit_res>fit_tolerance:
        raise ProductionSpatialPacketError(f'coframe fit residual {fit_res} exceeds tolerance')
    coeff=Cflat.T.reshape(3,3,5)
    model=AffineCoframeModel(coeff,fit_res,rank,float('inf'),float('inf'),
                             bool(overlap_cocycle_witness_supplied),bool(domain_coverage_witness_supplied),provenance_id)
    min_det=float('inf'); min_eig=float('inf')
    for x in points:
        e=model.coframe(x)
        det=abs(float(np.linalg.det(e)))
        h=e.T@e
        eig=float(np.min(np.linalg.eigvalsh(h)))
        min_det=min(min_det,det); min_eig=min(min_eig,eig)
        if det<=det_tolerance or eig<=metric_eigen_tolerance:
            raise ProductionSpatialPacketError('coframe lost rank or metric SPD on witness points')
    return AffineCoframeModel(coeff,fit_res,rank,min_det,min_eig,
                              bool(overlap_cocycle_witness_supplied),bool(domain_coverage_witness_supplied),provenance_id)
