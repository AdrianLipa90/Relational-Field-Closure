from __future__ import annotations

import math


class TIRPremetricCellChartBindingError(ValueError):
    pass


def _positive(name: str, value: float) -> float:
    value = float(value)
    if not math.isfinite(value) or value <= 0.0:
        raise TIRPremetricCellChartBindingError(
            f"{name} must be positive finite"
        )
    return value


def tetra_edge_hat() -> float:
    return math.sqrt(8.0 / 3.0)


def tetra_fs_shape_coefficient() -> float:
    return 8.0 / (9.0 * math.sqrt(3.0) * math.pi)


def physical_tir_edge(ell_s: float) -> float:
    ell_s = _positive("ell_s", ell_s)
    return ell_s * tetra_edge_hat()


def gamma_x_from_cell(l_h: float, h: float) -> float:
    l_h = _positive("l_h", l_h)
    h = _positive("h", h)
    return l_h / h


def chart_h_defect(h: float) -> float:
    h = _positive("h", h)
    return abs(h / tetra_edge_hat() - 1.0)


def chart_length_defect(l_h: float, ell_s: float) -> float:
    l_h = _positive("l_h", l_h)
    ell_s = _positive("ell_s", ell_s)
    return abs(l_h / physical_tir_edge(ell_s) - 1.0)


def sigma_x(ell_s: float, gamma_x: float) -> float:
    ell_s = _positive("ell_s", ell_s)
    gamma_x = _positive("gamma_x", gamma_x)
    return ell_s / gamma_x


def premetric_eta(mu_lambda: float, m_eff: float) -> float:
    mu_lambda = _positive("mu_lambda", mu_lambda)
    m_eff = _positive("m_eff", m_eff)
    return mu_lambda / math.sqrt(m_eff)


def zeta_from_rfs2(
    sigma_x_value: float,
    mu_lambda: float,
    m_eff: float,
) -> float:
    sigma_x_value = _positive("sigma_x", sigma_x_value)
    return sigma_x_value * premetric_eta(mu_lambda, m_eff)


def physical_zeta(m_i: float, ell_s: float) -> float:
    m_i = _positive("m_i", m_i)
    ell_s = _positive("ell_s", ell_s)
    return m_i * ell_s


def rfl5a_mu_lambda(gamma_t: float, c: float, m_i: float) -> float:
    gamma_t = _positive("gamma_t", gamma_t)
    c = _positive("c", c)
    m_i = _positive("m_i", m_i)
    return gamma_t * c * m_i


def rfl5a_gamma_x(gamma_t: float, c: float, m_eff: float) -> float:
    gamma_t = _positive("gamma_t", gamma_t)
    c = _positive("c", c)
    m_eff = _positive("m_eff", m_eff)
    return gamma_t * c / math.sqrt(m_eff)


def reduced_scale_coupling_defect(
    r_alpha: float,
    mu_lambda: float,
    m_eff: float,
) -> float:
    r_alpha = _positive("r_alpha", r_alpha)
    eta = premetric_eta(mu_lambda, m_eff)
    return r_alpha * eta**3 - 1.0 / tetra_fs_shape_coefficient()


def required_r_alpha(mu_lambda: float, m_eff: float) -> float:
    eta = premetric_eta(mu_lambda, m_eff)
    return 1.0 / (tetra_fs_shape_coefficient() * eta**3)


def required_eta(r_alpha: float) -> float:
    r_alpha = _positive("r_alpha", r_alpha)
    return (1.0 / (tetra_fs_shape_coefficient() * r_alpha)) ** (1.0 / 3.0)
