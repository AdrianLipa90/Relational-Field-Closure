from __future__ import annotations

import math


class FixedAmplitudeClockRadialStateError(ValueError):
    pass


def _positive(name: str, value: float) -> float:
    value = float(value)
    if not math.isfinite(value) or value <= 0.0:
        raise FixedAmplitudeClockRadialStateError(
            f"{name} must be positive finite"
        )
    return value


def _orientation(s: int) -> int:
    if s not in (-1, 1):
        raise FixedAmplitudeClockRadialStateError("s must be +1 or -1")
    return int(s)


def phi(x: float) -> float:
    x = _positive("x", x)
    return x - 1.0 - math.log(x)


def directional_rate(r0: float, b: float, s: int) -> float:
    r0 = _positive("r0", r0)
    b = float(b)
    if not math.isfinite(b) or abs(b) >= 1.0:
        raise FixedAmplitudeClockRadialStateError("b must be finite with |b|<1")
    s = _orientation(s)
    return r0 * (1.0 - s * b)


def reciprocal_rate_factor(r0: float, rs: float) -> float:
    r0 = _positive("r0", r0)
    rs = _positive("rs", rs)
    return r0 / rs


def phase_information_curvature(r0: float, rs: float, area_rel: float) -> float:
    area_rel = _positive("area_rel", area_rel)
    x = reciprocal_rate_factor(r0, rs)
    value = phi(x) / area_rel
    if value < -1.0e-14:
        raise FixedAmplitudeClockRadialStateError(
            "phase information curvature became negative"
        )
    return max(0.0, value)


def amplitude_sq_from_noether(j_vartheta: float, rs: float) -> float:
    j_vartheta = _positive("j_vartheta", j_vartheta)
    rs = _positive("rs", rs)
    return j_vartheta / (2.0 * rs)


def clock_radial_ratio(
    r0: float,
    rs: float,
    area_rel: float,
    j_vartheta: float,
) -> float:
    xi_phase = phase_information_curvature(r0, rs, area_rel)
    a2 = amplitude_sq_from_noether(j_vartheta, rs)
    return xi_phase / a2


def clock_radial_ratio_closed_form(
    r0: float,
    rs: float,
    area_rel: float,
    j_vartheta: float,
) -> float:
    r0 = _positive("r0", r0)
    rs = _positive("rs", rs)
    area_rel = _positive("area_rel", area_rel)
    j_vartheta = _positive("j_vartheta", j_vartheta)
    return 2.0 * rs * phi(r0 / rs) / (area_rel * j_vartheta)


def clock_radial_state_defect(
    r0: float,
    rs: float,
    area_rel: float,
    j_vartheta: float,
) -> float:
    xi_phase = phase_information_curvature(r0, rs, area_rel)
    xi_rad = amplitude_sq_from_noether(j_vartheta, rs)
    denom = xi_phase + xi_rad
    if denom <= 0.0:
        raise FixedAmplitudeClockRadialStateError(
            "state defect requires nondegenerate support"
        )
    return abs(xi_rad - xi_phase) / denom


def pointwise_crossing_residual(
    r0: float,
    rs: float,
    area_rel: float,
    j_vartheta: float,
) -> float:
    r0 = _positive("r0", r0)
    rs = _positive("rs", rs)
    area_rel = _positive("area_rel", area_rel)
    j_vartheta = _positive("j_vartheta", j_vartheta)
    return area_rel * j_vartheta - 2.0 * rs * phi(r0 / rs)


def phase_curvature_second_derivative_at_reference(area_rel: float) -> float:
    area_rel = _positive("area_rel", area_rel)
    return 1.0 / area_rel


def radial_curvature_second_derivative_fixed_amplitude() -> float:
    return 0.0
