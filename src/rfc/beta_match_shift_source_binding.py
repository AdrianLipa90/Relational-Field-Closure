"""RF-GSC3C beta_match <-> RFC shift source-binding certifier.

The TIR inter-leaf matching field in coordinate time, beta_t, and the RFC RF-E8
shift b_0 written with x^0=ct have the same inhomogeneous overlap law after the
exact scale conversion beta_t = c b_0.

If both carriers obey their overlap laws, the difference

    W = beta_t - c b_0

obeys the homogeneous spatial-vector law W_q = A_qp W_p.  The overlap geometry
therefore admits a covariant family labelled by W.  The source-owned identity is
the distinguished W=0 section on one declared physical realization.

This module checks both layers separately:
- overlap covariance of each carrier;
- exact source binding on the supplied realization.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import isfinite
from typing import Mapping, Sequence


class BetaMatchShiftBindingError(ValueError):
    """Raised when a supplied GSC3C witness fails its declared contract."""


Vector3 = tuple[float, float, float]
Matrix3 = tuple[tuple[float, float, float], ...]


def _finite(x: float, label: str) -> float:
    y = float(x)
    if not isfinite(y):
        raise BetaMatchShiftBindingError(f"{label} must be finite")
    return y


def _vector3(values: Sequence[float], label: str) -> Vector3:
    if len(values) != 3:
        raise BetaMatchShiftBindingError(f"{label} must have length 3")
    return tuple(_finite(x, f"{label}[{i}]") for i, x in enumerate(values))  # type: ignore[return-value]


def _matrix3(values: Sequence[Sequence[float]], label: str) -> Matrix3:
    if len(values) != 3 or any(len(row) != 3 for row in values):
        raise BetaMatchShiftBindingError(f"{label} must be 3x3")
    return tuple(
        tuple(_finite(x, f"{label}[{i}][{j}]") for j, x in enumerate(row))
        for i, row in enumerate(values)
    )  # type: ignore[return-value]


def _matvec(a: Matrix3, x: Vector3) -> Vector3:
    return tuple(sum(a[i][j] * x[j] for j in range(3)) for i in range(3))  # type: ignore[return-value]


def _sub(a: Vector3, b: Vector3) -> Vector3:
    return tuple(a[i] - b[i] for i in range(3))  # type: ignore[return-value]


def _scale(c: float, a: Vector3) -> Vector3:
    return tuple(c * a[i] for i in range(3))  # type: ignore[return-value]


def _max_abs(a: Vector3) -> float:
    return max(abs(x) for x in a)


@dataclass(frozen=True)
class MatchingPatch:
    patch_id: str
    beta_t: Vector3
    b_x0: Vector3


@dataclass(frozen=True)
class MatchingOverlap:
    source_patch: str
    target_patch: str
    spatial_jacobian: Matrix3
    spatial_time_velocity_t: Vector3


@dataclass(frozen=True)
class BetaMatchShiftBindingCertificate:
    status: str
    realization_id: str
    clock_id: str
    c: float
    overlap_covariance_pass: bool
    source_binding_exact: bool
    max_beta_overlap_defect: float
    max_shift_overlap_defect: float
    max_homogeneous_w_defect: float
    max_source_binding_defect: float
    w_by_patch: Mapping[str, Vector3]
    production_status: str


def matching_patch(patch_id: str, beta_t: Sequence[float], b_x0: Sequence[float]) -> MatchingPatch:
    pid = str(patch_id).strip()
    if not pid:
        raise BetaMatchShiftBindingError("patch_id must be nonempty")
    return MatchingPatch(pid, _vector3(beta_t, "beta_t"), _vector3(b_x0, "b_x0"))


def matching_overlap(
    source_patch: str,
    target_patch: str,
    spatial_jacobian: Sequence[Sequence[float]],
    spatial_time_velocity_t: Sequence[float],
) -> MatchingOverlap:
    p = str(source_patch).strip()
    q = str(target_patch).strip()
    if not p or not q or p == q:
        raise BetaMatchShiftBindingError("overlap patch ids must be distinct and nonempty")
    return MatchingOverlap(
        p,
        q,
        _matrix3(spatial_jacobian, "spatial_jacobian"),
        _vector3(spatial_time_velocity_t, "spatial_time_velocity_t"),
    )


def audit_beta_match_shift_source_binding(
    patches: Sequence[MatchingPatch],
    overlaps: Sequence[MatchingOverlap],
    *,
    tir_realization_id: str,
    rfc_realization_id: str,
    tir_clock_id: str,
    rfc_clock_id: str,
    c: float = 299792458.0,
    tol: float = 1e-10,
) -> BetaMatchShiftBindingCertificate:
    """Audit covariance and the W=0 source-binding section.

    Coordinate conventions:
      - TIR beta_t is expressed against coordinate time t;
      - RFC b_x0 is dimensionless against x^0=ct;
      - v_t = partial_t f on each shared-clock spatial overlap.

    Hence the two overlap laws are

      beta_q = A beta_p - v_t,
      b_q    = A b_p    - v_t/c.

    Their difference W=beta-c*b obeys W_q=A W_p.
    """

    speed = _finite(c, "c")
    tolerance = _finite(tol, "tol")
    if speed <= 0.0:
        raise BetaMatchShiftBindingError("c must be positive")
    if tolerance <= 0.0:
        raise BetaMatchShiftBindingError("tol must be positive")

    tir_rid = str(tir_realization_id).strip()
    rfc_rid = str(rfc_realization_id).strip()
    tir_cid = str(tir_clock_id).strip()
    rfc_cid = str(rfc_clock_id).strip()
    if not tir_rid or not rfc_rid or tir_rid != rfc_rid:
        raise BetaMatchShiftBindingError("TIR and RFC realization_id must match exactly")
    if not tir_cid or not rfc_cid or tir_cid != rfc_cid:
        raise BetaMatchShiftBindingError("TIR and RFC clock_id must match exactly")
    if not patches:
        raise BetaMatchShiftBindingError("at least one patch is required")

    by_id: dict[str, MatchingPatch] = {}
    for patch in patches:
        if patch.patch_id in by_id:
            raise BetaMatchShiftBindingError(f"duplicate patch_id: {patch.patch_id}")
        by_id[patch.patch_id] = patch

    w_by_patch: dict[str, Vector3] = {
        pid: _sub(p.beta_t, _scale(speed, p.b_x0)) for pid, p in by_id.items()
    }
    max_source = max(_max_abs(w) for w in w_by_patch.values())

    max_beta = 0.0
    max_shift = 0.0
    max_w = 0.0
    for ov in overlaps:
        if ov.source_patch not in by_id or ov.target_patch not in by_id:
            raise BetaMatchShiftBindingError("overlap references an unknown patch")
        p = by_id[ov.source_patch]
        q = by_id[ov.target_patch]
        a = ov.spatial_jacobian
        v_t = ov.spatial_time_velocity_t

        expected_beta_q = _sub(_matvec(a, p.beta_t), v_t)
        expected_b_q = _sub(_matvec(a, p.b_x0), _scale(1.0 / speed, v_t))
        expected_w_q = _matvec(a, w_by_patch[p.patch_id])

        max_beta = max(max_beta, _max_abs(_sub(q.beta_t, expected_beta_q)))
        max_shift = max(max_shift, _max_abs(_sub(q.b_x0, expected_b_q)))
        max_w = max(max_w, _max_abs(_sub(w_by_patch[q.patch_id], expected_w_q)))

    if max(max_beta, max_shift, max_w) > tolerance:
        raise BetaMatchShiftBindingError("shared-overlap covariance defect exceeds tolerance")

    exact = max_source <= tolerance
    status = (
        "PASS_GSC3C_BETA_MATCH_RFC_SHIFT_SOURCE_BINDING_ON_SUPPLIED_REALIZATION"
        if exact
        else "PASS_GSC3C_COVARIANT_FAMILY_WITH_SOURCE_BINDING_OPEN"
    )
    return BetaMatchShiftBindingCertificate(
        status=status,
        realization_id=tir_rid,
        clock_id=tir_cid,
        c=speed,
        overlap_covariance_pass=True,
        source_binding_exact=exact,
        max_beta_overlap_defect=max_beta,
        max_shift_overlap_defect=max_shift,
        max_homogeneous_w_defect=max_w,
        max_source_binding_defect=max_source,
        w_by_patch=w_by_patch,
        production_status=(
            "SOURCE_BINDING_CERTIFIED_ON_SUPPLIED_REALIZATION"
            if exact
            else "PRODUCTION_SOURCE_BINDING_OPEN"
        ),
    )


def require_exact_source_binding(cert: BetaMatchShiftBindingCertificate) -> None:
    """Fail closed when a downstream gate requires the W=0 source binding."""

    if not cert.source_binding_exact:
        raise BetaMatchShiftBindingError(
            "downstream source binding requires beta_match = c*b_x0 on every supplied patch"
        )
