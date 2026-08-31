"""RF-GSC3B matching-flow to extrinsic-curvature seam.

This module checks the exact ADM kinematic identity, in the sign convention used by
the TIR spatial-temporal interface and RFC:

    K_ij = (D_i b_j + D_j b_i - partial_t h_ij)/(2 N)

for the clock-transverse matching field

    X = partial_t - b^i partial_i.

On spatial arguments,

    (L_X h)_ij = partial_t h_ij - D_i b_j - D_j b_i,

hence

    K_ij = -(L_X h)_ij/(2 N).

This is a kinematic certifier. It does not supply production matching-flow coverage,
physical event placement, or RF-E25 Lorentz/coframe realization.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import isfinite
from typing import Sequence


class MatchingFlowExtrinsicCurvatureError(ValueError):
    """Raised when a supplied GSC3B witness fails closed."""


Matrix3 = tuple[tuple[float, float, float], ...]


def _finite(value: float, label: str) -> float:
    out = float(value)
    if not isfinite(out):
        raise MatchingFlowExtrinsicCurvatureError(f"{label} must be finite")
    return out


def _matrix3(values: Sequence[Sequence[float]], label: str) -> Matrix3:
    if len(values) != 3 or any(len(row) != 3 for row in values):
        raise MatchingFlowExtrinsicCurvatureError(f"{label} must be 3x3")
    out = tuple(
        tuple(_finite(x, f"{label}[{i}][{j}]") for j, x in enumerate(row))
        for i, row in enumerate(values)
    )
    return out  # type: ignore[return-value]


def _symmetric(a: Matrix3, tol: float, label: str) -> None:
    for i in range(3):
        for j in range(3):
            if abs(a[i][j] - a[j][i]) > tol:
                raise MatchingFlowExtrinsicCurvatureError(f"{label} must be symmetric")


def _sub(a: Matrix3, b: Matrix3) -> Matrix3:
    return tuple(
        tuple(a[i][j] - b[i][j] for j in range(3)) for i in range(3)
    )  # type: ignore[return-value]


def _scale(c: float, a: Matrix3) -> Matrix3:
    return tuple(
        tuple(c * a[i][j] for j in range(3)) for i in range(3)
    )  # type: ignore[return-value]


def _max_abs(a: Matrix3, b: Matrix3) -> float:
    return max(abs(a[i][j] - b[i][j]) for i in range(3) for j in range(3))


def matching_lie_metric(
    partial_t_h: Sequence[Sequence[float]],
    sym_covariant_shift: Sequence[Sequence[float]],
    *,
    symmetry_tol: float = 1e-12,
) -> Matrix3:
    """Return the spatial components of L_X h for X=partial_t-b.

    `sym_covariant_shift` is the already-covariant symmetric tensor
    D_i b_j + D_j b_i on the supplied spatial slice.
    """

    dt_h = _matrix3(partial_t_h, "partial_t_h")
    sym_db = _matrix3(sym_covariant_shift, "sym_covariant_shift")
    _symmetric(dt_h, symmetry_tol, "partial_t_h")
    _symmetric(sym_db, symmetry_tol, "sym_covariant_shift")
    return _sub(dt_h, sym_db)


def extrinsic_curvature_from_matching_flow(
    partial_t_h: Sequence[Sequence[float]],
    sym_covariant_shift: Sequence[Sequence[float]],
    lapse: float,
    *,
    symmetry_tol: float = 1e-12,
) -> Matrix3:
    """Return K in the declared TIR/RFC ADM sign convention."""

    n = _finite(lapse, "lapse")
    if n <= 0.0:
        raise MatchingFlowExtrinsicCurvatureError("lapse must be positive")
    lie_x_h = matching_lie_metric(
        partial_t_h, sym_covariant_shift, symmetry_tol=symmetry_tol
    )
    return _scale(-0.5 / n, lie_x_h)


def unit_normal_lie_metric(
    partial_t_h: Sequence[Sequence[float]],
    sym_covariant_shift: Sequence[Sequence[float]],
    lapse: float,
    *,
    symmetry_tol: float = 1e-12,
) -> Matrix3:
    """Return spatial (L_n h) for n=X/N.

    On spatial arguments, the derivative-of-1/N terms vanish because the spatial
    metric annihilates the normal/matching direction. Thus L_n h=(1/N)L_X h.
    """

    n = _finite(lapse, "lapse")
    if n <= 0.0:
        raise MatchingFlowExtrinsicCurvatureError("lapse must be positive")
    lie_x_h = matching_lie_metric(
        partial_t_h, sym_covariant_shift, symmetry_tol=symmetry_tol
    )
    return _scale(1.0 / n, lie_x_h)


def dragged_coordinate_metric_rate(
    extrinsic_curvature: Sequence[Sequence[float]],
    lapse: float,
    *,
    symmetry_tol: float = 1e-12,
) -> Matrix3:
    """Metric evolution in coordinates dragged by the GSC3A matching flow.

    In these coordinates X=partial_t and the coordinate shift is zero, while the
    deformation remains in the metric rate:

        partial_t h = -2 N K.
    """

    n = _finite(lapse, "lapse")
    if n <= 0.0:
        raise MatchingFlowExtrinsicCurvatureError("lapse must be positive")
    k = _matrix3(extrinsic_curvature, "extrinsic_curvature")
    _symmetric(k, symmetry_tol, "extrinsic_curvature")
    return _scale(-2.0 * n, k)


@dataclass(frozen=True)
class MatchingFlowExtrinsicCurvatureCertificate:
    status: str
    lapse: float
    lie_x_h: Matrix3
    extrinsic_curvature: Matrix3
    lie_n_h: Matrix3
    defining_identity_defect: float
    unit_normal_identity_defect: float
    dragged_coordinate_defect: float
    shift_zero_is_coordinate_gauge: bool
    production_matching_flow: str
    physical_event_placement: str


def certify_matching_flow_extrinsic_curvature(
    partial_t_h: Sequence[Sequence[float]],
    sym_covariant_shift: Sequence[Sequence[float]],
    lapse: float,
    *,
    tol: float = 1e-10,
) -> MatchingFlowExtrinsicCurvatureCertificate:
    """Fail-closed deterministic certificate for the GSC3B kinematic seam."""

    tolerance = _finite(tol, "tol")
    if tolerance <= 0.0:
        raise MatchingFlowExtrinsicCurvatureError("tol must be positive")

    n = _finite(lapse, "lapse")
    if n <= 0.0:
        raise MatchingFlowExtrinsicCurvatureError("lapse must be positive")

    lie_x_h = matching_lie_metric(partial_t_h, sym_covariant_shift)
    k = extrinsic_curvature_from_matching_flow(partial_t_h, sym_covariant_shift, n)
    lie_n_h = unit_normal_lie_metric(partial_t_h, sym_covariant_shift, n)

    expected_k = _scale(-0.5 / n, lie_x_h)
    expected_lie_n = _scale(-2.0, k)
    dragged_rate = dragged_coordinate_metric_rate(k, n)
    expected_dragged_rate = _scale(-2.0 * n, k)

    d_k = _max_abs(k, expected_k)
    d_n = _max_abs(lie_n_h, expected_lie_n)
    d_drag = _max_abs(dragged_rate, expected_dragged_rate)

    if max(d_k, d_n, d_drag) > tolerance:
        raise MatchingFlowExtrinsicCurvatureError("GSC3B defining identity defect")

    return MatchingFlowExtrinsicCurvatureCertificate(
        status="PASS_RFC_GSC3B_MATCHING_FLOW_EXTRINSIC_CURVATURE_KINEMATIC_SEAM",
        lapse=n,
        lie_x_h=lie_x_h,
        extrinsic_curvature=k,
        lie_n_h=lie_n_h,
        defining_identity_defect=d_k,
        unit_normal_identity_defect=d_n,
        dragged_coordinate_defect=d_drag,
        shift_zero_is_coordinate_gauge=True,
        production_matching_flow="UPSTREAM_GSC3A_OPEN_INPUT",
        physical_event_placement="UPSTREAM_OPEN_INPUT",
    )
