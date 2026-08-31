"""RF-GSC4D rigid anchored TIR spatial-geometry source route.

This module composes two existing source-side structures:

1. TIR anchored Pauli charts
       x_p = Q_p^T (r - r_p),   Q_p in SO(3),
   which give the exact rigid overlap
       A_qp = R_qp = Q_q^T Q_p,
       t_qp = Q_q^T (r_p-r_q);

2. TIR/RF-02H hexahedral phase-clock physicalization
       E^i = [c/(sqrt(6)|omega_t|)] vartheta^i.

On the pure anchored orientation-chart route vartheta=dx in each local frame,
so the coframe matrix is e_p=s_p I.  At a common overlap point the same scalar
phase scale must be represented by both patches.  Under that source-binding
condition, e_q A_qp = R_qp e_p follows exactly.

This is a sufficient rigid-atlas route only.  General smooth spatial overlaps
remain owned by RF-GSC4A and permit A_qp != R_qp.
"""
from __future__ import annotations

from dataclasses import dataclass
from math import isfinite, sqrt
from typing import Mapping, Sequence


class AnchoredRigidGeometryError(ValueError):
    """Raised when a supplied GSC4D source witness fails closed."""


Vector3 = tuple[float, float, float]
Matrix3 = tuple[tuple[float, float, float], ...]
I3: Matrix3 = ((1.0, 0.0, 0.0), (0.0, 1.0, 0.0), (0.0, 0.0, 1.0))


def _finite(value: float, label: str) -> float:
    out = float(value)
    if not isfinite(out):
        raise AnchoredRigidGeometryError(f"{label} must be finite")
    return out


def _vec3(values: Sequence[float], label: str) -> Vector3:
    if len(values) != 3:
        raise AnchoredRigidGeometryError(f"{label} must have length 3")
    return tuple(_finite(x, f"{label}[{i}]") for i, x in enumerate(values))  # type: ignore[return-value]


def _mat3(values: Sequence[Sequence[float]], label: str) -> Matrix3:
    if len(values) != 3 or any(len(row) != 3 for row in values):
        raise AnchoredRigidGeometryError(f"{label} must be 3x3")
    return tuple(
        tuple(_finite(x, f"{label}[{i}][{j}]") for j, x in enumerate(row))
        for i, row in enumerate(values)
    )  # type: ignore[return-value]


def _transpose(a: Matrix3) -> Matrix3:
    return tuple(tuple(a[j][i] for j in range(3)) for i in range(3))  # type: ignore[return-value]


def _mm(a: Matrix3, b: Matrix3) -> Matrix3:
    return tuple(
        tuple(sum(a[i][k] * b[k][j] for k in range(3)) for j in range(3))
        for i in range(3)
    )  # type: ignore[return-value]


def _mv(a: Matrix3, v: Vector3) -> Vector3:
    return tuple(sum(a[i][k] * v[k] for k in range(3)) for i in range(3))  # type: ignore[return-value]


def _subv(a: Vector3, b: Vector3) -> Vector3:
    return tuple(a[i] - b[i] for i in range(3))  # type: ignore[return-value]


def _scale_mat(s: float, a: Matrix3) -> Matrix3:
    return tuple(tuple(s * a[i][j] for j in range(3)) for i in range(3))  # type: ignore[return-value]


def _det(a: Matrix3) -> float:
    return (
        a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
        - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
        + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0])
    )


def _maxm(a: Matrix3, b: Matrix3) -> float:
    return max(abs(a[i][j] - b[i][j]) for i in range(3) for j in range(3))


def _maxv(a: Vector3, b: Vector3) -> float:
    return max(abs(a[i] - b[i]) for i in range(3))


def _require_so3(q: Matrix3, tol: float, label: str) -> None:
    qtq = _mm(_transpose(q), q)
    if _maxm(qtq, I3) > tol or abs(_det(q) - 1.0) > tol:
        raise AnchoredRigidGeometryError(f"{label} must lie in SO(3)")


@dataclass(frozen=True)
class AnchoredPhasePatch:
    patch_id: str
    anchor: Vector3
    frame: Matrix3
    omega_t: float
    phase_scale: float
    coframe: Matrix3


@dataclass(frozen=True)
class AnchoredRigidOverlap:
    source: str
    target: str
    spatial_jacobian: Matrix3
    spatial_rotation: Matrix3
    translation: Vector3
    scale_residual: float
    coframe_residual: float


@dataclass(frozen=True)
class AnchoredRigidGeometryCertificate:
    status: str
    patches: Mapping[str, AnchoredPhasePatch]
    overlaps: tuple[AnchoredRigidOverlap, ...]
    max_scale_residual: float
    max_coframe_residual: float
    rigid_route_exact: bool
    general_spatial_atlas_status: str = "GENERAL_GSC4A_ROUTE_SEPARATE"
    production_status: str = "ANCHOR_FRAME_PHASE_RATE_SOURCE_PACKET_OPEN"


def anchored_phase_patch(
    patch_id: str,
    anchor: Sequence[float],
    frame: Sequence[Sequence[float]],
    omega_t: float,
    *,
    c: float = 299792458.0,
    tol: float = 1.0e-10,
) -> AnchoredPhasePatch:
    pid = str(patch_id).strip()
    if not pid:
        raise AnchoredRigidGeometryError("patch_id must be nonempty")
    q = _mat3(frame, "frame")
    tolerance = _finite(tol, "tol")
    if tolerance <= 0.0:
        raise AnchoredRigidGeometryError("tol must be positive")
    _require_so3(q, tolerance, "frame")
    omega = _finite(omega_t, "omega_t")
    speed = _finite(c, "c")
    if speed <= 0.0:
        raise AnchoredRigidGeometryError("c must be positive")
    if omega == 0.0:
        raise AnchoredRigidGeometryError("omega_t must be nonzero")
    s = speed / (sqrt(6.0) * abs(omega))
    return AnchoredPhasePatch(
        patch_id=pid,
        anchor=_vec3(anchor, "anchor"),
        frame=q,
        omega_t=omega,
        phase_scale=s,
        coframe=_scale_mat(s, I3),
    )


def certify_anchored_phase_scaled_rigid_geometry(
    patches: Sequence[AnchoredPhasePatch],
    overlap_pairs: Sequence[tuple[str, str]],
    *,
    tol: float = 1.0e-10,
) -> AnchoredRigidGeometryCertificate:
    """Certify the rigid anchored/hexahedral spatial-geometry source route."""
    tolerance = _finite(tol, "tol")
    if tolerance <= 0.0:
        raise AnchoredRigidGeometryError("tol must be positive")
    if not patches:
        raise AnchoredRigidGeometryError("at least one patch is required")
    by_id: dict[str, AnchoredPhasePatch] = {}
    for patch in patches:
        if patch.patch_id in by_id:
            raise AnchoredRigidGeometryError(f"duplicate patch_id: {patch.patch_id}")
        _require_so3(patch.frame, tolerance, f"frame[{patch.patch_id}]")
        by_id[patch.patch_id] = patch

    overlaps: list[AnchoredRigidOverlap] = []
    max_scale = 0.0
    max_coframe = 0.0
    for source, target in overlap_pairs:
        if source == target or source not in by_id or target not in by_id:
            raise AnchoredRigidGeometryError("overlap must reference two distinct known patches")
        p = by_id[source]
        q = by_id[target]
        # TIR anchored-frame theorem: x_q = Q_q^T Q_p x_p + Q_q^T(r_p-r_q).
        a = _mm(_transpose(q.frame), p.frame)
        r = a
        t = _mv(_transpose(q.frame), _subv(p.anchor, q.anchor))
        _require_so3(a, tolerance, "derived rigid spatial_jacobian")

        scale_residual = abs(q.phase_scale - p.phase_scale)
        scale_bound = tolerance * (1.0 + max(abs(p.phase_scale), abs(q.phase_scale)))
        if scale_residual > scale_bound:
            raise AnchoredRigidGeometryError(
                "shared phase-clock spatial scale mismatch on rigid overlap"
            )

        eqa = _mm(q.coframe, a)
        rep = _mm(r, p.coframe)
        coframe_residual = _maxm(eqa, rep)
        if coframe_residual > tolerance * (1.0 + max(abs(x) for row in eqa for x in row)):
            raise AnchoredRigidGeometryError("derived rigid coframe overlap relation failed")

        overlaps.append(
            AnchoredRigidOverlap(
                source=source,
                target=target,
                spatial_jacobian=a,
                spatial_rotation=r,
                translation=t,
                scale_residual=scale_residual,
                coframe_residual=coframe_residual,
            )
        )
        max_scale = max(max_scale, scale_residual)
        max_coframe = max(max_coframe, coframe_residual)

    return AnchoredRigidGeometryCertificate(
        status="PASS_GSC4D_ANCHORED_PHASE_SCALED_RIGID_SPATIAL_GEOMETRY",
        patches=by_id,
        overlaps=tuple(overlaps),
        max_scale_residual=max_scale,
        max_coframe_residual=max_coframe,
        rigid_route_exact=True,
    )
