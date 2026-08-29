from __future__ import annotations

import math


class TetraClockMassScaleClosureError(ValueError):
    pass


def _positive(name: str, value: float) -> float:
    value = float(value)
    if not math.isfinite(value) or value <= 0.0:
        raise TetraClockMassScaleClosureError(f"{name} must be positive finite")
    return value


def tetra_fs_shape_coefficient() -> float:
    return 8.0 / (9.0 * math.sqrt(3.0) * math.pi)


def inverse_shape_coefficient() -> float:
    return 1.0 / tetra_fs_shape_coefficient()


def kappa_shape_coefficient(kappa: float) -> float:
    kappa = _positive("kappa", kappa)
    return 64.0 * kappa / (3.0 * math.sqrt(3.0) * math.log(2.0))


def volume_area_ratio(ell_s: float, ell_phi: float) -> float:
    ell_s = _positive("ell_s", ell_s)
    ell_phi = _positive("ell_phi", ell_phi)
    q = ell_s / ell_phi
    return tetra_fs_shape_coefficient() * q**3 * ell_phi


def energy_scale_natural(
    r_alpha: float,
    q_s: float,
    m_i: float,
    e_phi: float,
) -> float:
    r_alpha = _positive("r_alpha", r_alpha)
    q_s = _positive("q_s", q_s)
    m_i = _positive("m_i", m_i)
    e_phi = _positive("e_phi", e_phi)
    return r_alpha * tetra_fs_shape_coefficient() * q_s**3 * m_i**2 / e_phi


def closure_defect(
    r_alpha: float,
    q_s: float,
    mu_phi: float,
    r_m: float,
) -> float:
    r_alpha = _positive("r_alpha", r_alpha)
    q_s = _positive("q_s", q_s)
    mu_phi = _positive("mu_phi", mu_phi)
    r_m = _positive("r_m", r_m)
    return r_alpha * q_s**3 - r_m * mu_phi * inverse_shape_coefficient()


def required_q_s(r_alpha: float, mu_phi: float, r_m: float) -> float:
    r_alpha = _positive("r_alpha", r_alpha)
    mu_phi = _positive("mu_phi", mu_phi)
    r_m = _positive("r_m", r_m)
    return (r_m * mu_phi * inverse_shape_coefficient() / r_alpha) ** (1.0 / 3.0)


def required_r_alpha(q_s: float, mu_phi: float, r_m: float) -> float:
    q_s = _positive("q_s", q_s)
    mu_phi = _positive("mu_phi", mu_phi)
    r_m = _positive("r_m", r_m)
    return r_m * mu_phi * inverse_shape_coefficient() / q_s**3


def physical_directional_phi(beta_phys: float, orientation: int) -> float:
    beta_phys = float(beta_phys)
    if not math.isfinite(beta_phys) or not abs(beta_phys) < 1.0:
        raise TetraClockMassScaleClosureError("|beta_phys|<1 required")
    if orientation not in (-1, 1):
        raise TetraClockMassScaleClosureError("orientation must be +1 or -1")
    x = 1.0 / (1.0 - orientation * beta_phys)
    return x - 1.0 - math.log(x)


def physical_directional_energy_natural(
    beta_phys: float,
    orientation: int,
    target_mass: float,
) -> float:
    target_mass = _positive("target_mass", target_mass)
    return target_mass * physical_directional_phi(beta_phys, orientation)
