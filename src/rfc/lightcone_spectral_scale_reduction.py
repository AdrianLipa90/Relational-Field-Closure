from __future__ import annotations

import math


class LightconeSpectralScaleReductionError(ValueError):
    pass


def _positive(name: str, value: float) -> float:
    value = float(value)
    if not math.isfinite(value) or value <= 0.0:
        raise LightconeSpectralScaleReductionError(f"{name} must be positive finite")
    return value


def tetra_fs_shape_coefficient() -> float:
    return 8.0 / (9.0 * math.sqrt(3.0) * math.pi)


def spectral_ratio(omega_lambda_phase: float, mu_lambda: float) -> float:
    omega_lambda_phase = float(omega_lambda_phase)
    if not math.isfinite(omega_lambda_phase) or omega_lambda_phase == 0.0:
        raise LightconeSpectralScaleReductionError(
            "omega_lambda_phase must be nonzero finite"
        )
    mu_lambda = _positive("mu_lambda", mu_lambda)
    return abs(omega_lambda_phase) / mu_lambda


def kg_frequency_physical(c: float, m_i: float) -> float:
    c = _positive("c", c)
    m_i = _positive("m_i", m_i)
    return c * m_i


def phase_frequency_physical(
    omega_lambda_phase: float,
    gamma_t: float,
) -> float:
    omega_lambda_phase = float(omega_lambda_phase)
    if not math.isfinite(omega_lambda_phase) or omega_lambda_phase == 0.0:
        raise LightconeSpectralScaleReductionError(
            "omega_lambda_phase must be nonzero finite"
        )
    gamma_t = _positive("gamma_t", gamma_t)
    return omega_lambda_phase / gamma_t


def phase_length_from_rho_mass(rho_omega: float, m_i: float) -> float:
    rho_omega = _positive("rho_omega", rho_omega)
    m_i = _positive("m_i", m_i)
    return 1.0 / (rho_omega * m_i)


def phase_energy_ratio(rho_omega: float) -> float:
    return _positive("rho_omega", rho_omega)


def spatial_mass_coordinate(m_i: float, ell_s: float) -> float:
    m_i = _positive("m_i", m_i)
    ell_s = _positive("ell_s", ell_s)
    return m_i * ell_s


def q_s_reduced(rho_omega: float, zeta_s: float) -> float:
    rho_omega = _positive("rho_omega", rho_omega)
    zeta_s = _positive("zeta_s", zeta_s)
    return rho_omega * zeta_s


def zeta_from_premetric(
    sigma_x: float,
    mu_lambda: float,
    m_eff: float,
) -> float:
    sigma_x = _positive("sigma_x", sigma_x)
    mu_lambda = _positive("mu_lambda", mu_lambda)
    m_eff = _positive("m_eff", m_eff)
    return sigma_x * mu_lambda / math.sqrt(m_eff)


def q_s_from_premetric(
    rho_omega: float,
    sigma_x: float,
    mu_lambda: float,
    m_eff: float,
) -> float:
    return q_s_reduced(
        rho_omega,
        zeta_from_premetric(sigma_x, mu_lambda, m_eff),
    )


def reduced_energy_scale_natural(
    r_alpha: float,
    rho_omega: float,
    zeta_s: float,
    m_i: float,
) -> float:
    r_alpha = _positive("r_alpha", r_alpha)
    rho_omega = _positive("rho_omega", rho_omega)
    zeta_s = _positive("zeta_s", zeta_s)
    m_i = _positive("m_i", m_i)
    return (
        r_alpha
        * tetra_fs_shape_coefficient()
        * rho_omega**2
        * zeta_s**3
        * m_i
    )


def reduced_closure_defect(
    r_alpha: float,
    rho_omega: float,
    zeta_s: float,
    r_m: float,
) -> float:
    r_alpha = _positive("r_alpha", r_alpha)
    rho_omega = _positive("rho_omega", rho_omega)
    zeta_s = _positive("zeta_s", zeta_s)
    r_m = _positive("r_m", r_m)
    return (
        r_alpha * rho_omega**2 * zeta_s**3
        - r_m / tetra_fs_shape_coefficient()
    )


def required_zeta_s(
    r_alpha: float,
    rho_omega: float,
    r_m: float,
) -> float:
    r_alpha = _positive("r_alpha", r_alpha)
    rho_omega = _positive("rho_omega", rho_omega)
    r_m = _positive("r_m", r_m)
    return (
        r_m
        / (tetra_fs_shape_coefficient() * r_alpha * rho_omega**2)
    ) ** (1.0 / 3.0)
