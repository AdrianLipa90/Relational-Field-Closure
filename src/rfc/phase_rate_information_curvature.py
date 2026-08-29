from __future__ import annotations

import math


class PhaseRateInformationCurvatureError(ValueError):
    pass


def _positive(name: str, value: float) -> float:
    value = float(value)
    if not math.isfinite(value) or value <= 0.0:
        raise PhaseRateInformationCurvatureError(f"{name} must be positive finite")
    return value


def phi(x: float) -> float:
    x = _positive("x", x)
    return x - 1.0 - math.log(x)


def directional_rate_ratio(rate_directional: float, rate_reference: float) -> tuple[float, float]:
    rs = _positive("rate_directional", rate_directional)
    r0 = _positive("rate_reference", rate_reference)
    ratio = rs / r0
    return ratio, 1.0 / ratio


def phase_rate_information_nats(rate_directional: float, rate_reference: float) -> float:
    """D_KL(Exp(rate_directional)||Exp(rate_reference)) in the IDT 05F embedding."""
    rs = _positive("rate_directional", rate_directional)
    r0 = _positive("rate_reference", rate_reference)
    return math.log(rs / r0) + r0 / rs - 1.0


def information_curvature(rate_directional: float, rate_reference: float, relational_area: float) -> float:
    area = _positive("relational_area", relational_area)
    return phase_rate_information_nats(rate_directional, rate_reference) / area


def constant_phase_clock_area(rate_reference: float, a_fs: float, c: float = 1.0) -> float:
    r0 = _positive("rate_reference", rate_reference)
    a = _positive("a_fs", a_fs)
    c = _positive("c", c)
    return (c * c / (r0 * r0)) * a


def constant_cell_information_curvature(
    rate_directional: float,
    rate_reference: float,
    a_fs: float,
    c: float = 1.0,
) -> float:
    area = constant_phase_clock_area(rate_reference, a_fs, c)
    return information_curvature(rate_directional, rate_reference, area)


def clock_scalar_potential_density(
    rate_directional: float,
    rate_reference: float,
    relational_area: float,
    alpha_clock: float,
    kappa_e: float,
) -> float:
    alpha = _positive("alpha_clock", alpha_clock)
    kappa = _positive("kappa_e", kappa_e)
    xi = information_curvature(rate_directional, rate_reference, relational_area)
    return (alpha / kappa) * xi


def homogeneous_clock_action_energy(
    rate_directional: float,
    rate_reference: float,
    relational_area: float,
    cell_volume: float,
    alpha_clock: float,
    kappa_e: float,
) -> tuple[float, float, float]:
    volume = _positive("cell_volume", cell_volume)
    alpha = _positive("alpha_clock", alpha_clock)
    kappa = _positive("kappa_e", kappa_e)
    j = phase_rate_information_nats(rate_directional, rate_reference)
    e_star = (alpha / kappa) * volume / _positive("relational_area", relational_area)
    return e_star * j, e_star, j
