import math


def gamma_dc(kappa_g, m_star, g2):
    return kappa_g * m_star / (2.0 * g2)


def mbar_g(m_star, gamma, g2):
    return m_star / (gamma * g2)


def g_from_kappa(kappa_g):
    return kappa_g * kappa_g / (32.0 * math.pi)


def g_from_mbar(mbar):
    return 1.0 / (8.0 * math.pi * mbar * mbar)


def gamma_from_horizon(alpha_c, m_star, m_h, t_h):
    return alpha_c * m_star / math.sqrt(m_h * t_h)


def test_factorization_identity():
    kappa_g, m_star, g2 = 0.071, 3.7, 1.8
    gamma = gamma_dc(kappa_g, m_star, g2)
    assert math.isclose(mbar_g(m_star, gamma, g2), 2.0 / kappa_g, rel_tol=1e-14)


def test_g_identity():
    kappa_g, m_star, g2 = 0.071, 3.7, 1.8
    gamma = gamma_dc(kappa_g, m_star, g2)
    mbar = mbar_g(m_star, gamma, g2)
    assert math.isclose(g_from_mbar(mbar), g_from_kappa(kappa_g), rel_tol=1e-14)


def test_mass_scale_rescaling_invariance():
    kappa_g, m_star, g2, lam = 0.071, 3.7, 1.8, 5.3
    gamma = gamma_dc(kappa_g, m_star, g2)
    gamma_scaled = gamma_dc(kappa_g, lam * m_star, g2)
    assert math.isclose(gamma_scaled, lam * gamma, rel_tol=1e-14)
    assert math.isclose(
        mbar_g(m_star, gamma, g2),
        mbar_g(lam * m_star, gamma_scaled, g2),
        rel_tol=1e-14,
    )


def test_alpha_c_surface():
    alpha_c, kappa_g, m_star = 0.47483961905223004, 0.071, 3.7
    g2 = 1.0 / alpha_c
    gamma = gamma_dc(kappa_g, m_star, g2)
    assert math.isclose(gamma, kappa_g * alpha_c * m_star / 2.0, rel_tol=1e-14)
    assert math.isclose(alpha_c * m_star / gamma, 2.0 / kappa_g, rel_tol=1e-14)


def test_horizon_route_fixes_gamma_given_mstar():
    alpha_c, m_star, m_h, t_h = 0.47483961905223004, 3.7, 11.0, 0.013
    gamma = gamma_from_horizon(alpha_c, m_star, m_h, t_h)
    assert math.isclose(alpha_c * m_star / gamma, math.sqrt(m_h * t_h), rel_tol=1e-14)


def test_local_carrier_horizon_formula():
    alpha_c, omega_q, m_h, t_h = 0.47483961905223004, 2.4, 11.0, 0.013
    gamma = gamma_from_horizon(alpha_c, omega_q / 2.0, m_h, t_h)
    assert math.isclose(
        gamma,
        alpha_c * omega_q / (2.0 * math.sqrt(m_h * t_h)),
        rel_tol=1e-14,
    )


def test_gamma_one_selects_specific_mstar():
    alpha_c, kappa_g = 0.47483961905223004, 0.071
    g2 = 1.0 / alpha_c
    m_required = 2.0 * g2 / kappa_g
    assert math.isclose(gamma_dc(kappa_g, m_required, g2), 1.0, rel_tol=1e-14)
