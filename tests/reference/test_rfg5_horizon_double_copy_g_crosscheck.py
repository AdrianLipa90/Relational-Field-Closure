import math


def g_dc(gamma_dc, g_ym, m_star):
    return gamma_dc**2 * g_ym**4 / (8.0 * math.pi * m_star**2)


def g_horizon_natural(m_h, kappa_h):
    return 1.0 / (4.0 * m_h * kappa_h)


def test_g_equality_is_equivalent_to_g_free_cross_invariant():
    gamma = 0.83
    g = 0.71
    m_star = 1.9
    m_h = 4.3
    # Choose kappa_h from equality of the two G routes.
    G = g_dc(gamma, g, m_star)
    kappa_h = 1.0 / (4.0 * m_h * G)
    lhs = gamma**2 * g**4 * m_h * kappa_h
    rhs = 2.0 * math.pi * m_star**2
    assert math.isclose(lhs, rhs, rel_tol=1e-13, abs_tol=1e-13)
    assert math.isclose(G, g_horizon_natural(m_h, kappa_h), rel_tol=1e-13, abs_tol=1e-13)


def test_source_carrier_substitution_gives_phase_rate_form():
    gamma = 0.92
    g = 0.64
    m_h = 3.7
    d_tau_chi = 2.6
    m_star = 0.5 * d_tau_chi
    G = g_dc(gamma, g, m_star)
    kappa_h = 1.0 / (4.0 * m_h * G)
    lhs = gamma**2 * g**4 * m_h * kappa_h
    rhs = 0.5 * math.pi * d_tau_chi**2
    assert math.isclose(lhs, rhs, rel_tol=1e-13, abs_tol=1e-13)


def test_wilson_substitution_yields_72_factor():
    gamma = 1.07
    beta_w = 5.8
    d_tau_chi = 3.1
    m_h = 5.2
    g2 = 6.0 / beta_w
    g = math.sqrt(g2)
    m_star = 0.5 * d_tau_chi
    G = g_dc(gamma, g, m_star)
    kappa_h = 1.0 / (4.0 * m_h * G)
    lhs = 72.0 * gamma**2 * m_h * kappa_h
    rhs = math.pi * beta_w**2 * d_tau_chi**2
    assert math.isclose(lhs, rhs, rel_tol=1e-13, abs_tol=1e-13)


def test_hawking_temperature_form_is_equivalent_in_natural_units():
    gamma = 0.77
    beta_w = 6.1
    d_tau_chi = 4.4
    m_h = 2.9
    g = math.sqrt(6.0 / beta_w)
    m_star = 0.5 * d_tau_chi
    G = g_dc(gamma, g, m_star)
    kappa_h = 1.0 / (4.0 * m_h * G)
    T_h = kappa_h / (2.0 * math.pi)
    lhs = 144.0 * gamma**2 * m_h * T_h
    rhs = beta_w**2 * d_tau_chi**2
    assert math.isclose(lhs, rhs, rel_tol=1e-13, abs_tol=1e-13)


def test_detuned_horizon_data_fails_cross_route_gate():
    gamma = 1.0
    beta_w = 6.0
    d_tau_chi = 3.0
    m_h = 4.0
    g = math.sqrt(6.0 / beta_w)
    m_star = 0.5 * d_tau_chi
    G = g_dc(gamma, g, m_star)
    kappa_exact = 1.0 / (4.0 * m_h * G)
    kappa_bad = 1.08 * kappa_exact
    lhs = 72.0 * gamma**2 * m_h * kappa_bad
    rhs = math.pi * beta_w**2 * d_tau_chi**2
    defect = abs(lhs - rhs) / rhs
    assert defect > 0.05


def test_G_cancels_from_cross_route_identity():
    # Same invariant can be evaluated entirely from upstream coordinates.
    gamma = 0.9
    beta_w = 5.5
    d_tau_chi = 2.8
    m_h = 6.2
    rhs = math.pi * beta_w**2 * d_tau_chi**2
    kappa_required = rhs / (72.0 * gamma**2 * m_h)
    assert kappa_required > 0.0
    # No numerical G is used in constructing kappa_required here.
    reconstructed_ratio = 72.0 * gamma**2 * m_h * kappa_required / rhs
    assert math.isclose(reconstructed_ratio, 1.0, rel_tol=1e-14, abs_tol=1e-14)
