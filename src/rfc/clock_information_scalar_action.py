from __future__ import annotations

import math


class ClockInformationScalarActionError(ValueError):
    pass


def _finite(name: str, value: float) -> float:
    value = float(value)
    if not math.isfinite(value):
        raise ClockInformationScalarActionError(f"{name} must be finite")
    return value


def _positive(name: str, value: float) -> float:
    value = _finite(name, value)
    if value <= 0.0:
        raise ClockInformationScalarActionError(f"{name} must be positive")
    return value


def phi(x: float) -> float:
    x = _positive("x", x)
    return x - 1.0 - math.log(x)


def directional_x(beta: float, orientation: int) -> float:
    beta = _finite("beta", beta)
    if not abs(beta) < 1.0:
        raise ClockInformationScalarActionError("|beta|<1 required")
    if orientation not in (-1, 1):
        raise ClockInformationScalarActionError("orientation must be +1 or -1")
    return 1.0 / (1.0 - orientation * beta)


def clock_information_scalar(beta: float, orientation: int, area_rel: float) -> float:
    area_rel = _positive("area_rel", area_rel)
    return phi(directional_x(beta, orientation)) / area_rel


def scalar_potential_density(
    beta: float,
    orientation: int,
    area_rel: float,
    alpha_clk: float,
    kappa_e: float,
) -> float:
    alpha_clk = _finite("alpha_clk", alpha_clk)
    kappa_e = _finite("kappa_e", kappa_e)
    if kappa_e == 0.0:
        raise ClockInformationScalarActionError("kappa_e must be nonzero")
    xi = clock_information_scalar(beta, orientation, area_rel)
    return alpha_clk * xi / kappa_e


def homogeneous_cell_energy(
    beta: float,
    orientation: int,
    area_rel: float,
    volume_cell: float,
    alpha_clk: float,
    kappa_e: float,
) -> dict[str, float]:
    volume_cell = _positive("volume_cell", volume_cell)
    area_rel = _positive("area_rel", area_rel)
    alpha_clk = _finite("alpha_clk", alpha_clk)
    kappa_e = _finite("kappa_e", kappa_e)
    if kappa_e == 0.0:
        raise ClockInformationScalarActionError("kappa_e must be nonzero")
    x = directional_x(beta, orientation)
    info = phi(x)
    e_star = alpha_clk * volume_cell / (kappa_e * area_rel)
    return {
        "x": x,
        "information": info,
        "E_star": e_star,
        "U_clk": alpha_clk * info / (kappa_e * area_rel),
        "H_clk": e_star * info,
    }


def mass_scale_defect(
    mass: float,
    c: float,
    area_rel: float,
    volume_cell: float,
    alpha_clk: float,
    kappa_e: float,
) -> float:
    mass = _positive("mass", mass)
    c = _positive("c", c)
    state = homogeneous_cell_energy(0.0, +1, area_rel, volume_cell, alpha_clk, kappa_e)
    return state["E_star"] - mass * c * c
