import math


def rho_phase(a, omega):
    return a * a * omega * omega


def g_dc(beta, gamma, omega):
    return 18.0 * gamma * gamma / (math.pi * beta * beta * omega * omega)


def source_dc_from_current(beta, gamma, omega, a):
    j = 2.0 * a * a * omega
    return 36.0 * gamma * gamma * j / (beta * beta * omega)


def source_dc_reduced(beta, gamma, a):
    return 72.0 * gamma * gamma * a * a / (beta * beta)


def test_phase_rate_cancels_from_source_law():
    beta, gamma, a = 2.9, 0.83, 1.4
    for omega in (0.7, 1.1, 3.8, 9.2):
        assert math.isclose(source_dc_from_current(beta, gamma, omega, a), source_dc_reduced(beta, gamma, a), rel_tol=1e-14)


def test_newton_product_closes_same_source():
    beta, gamma, a, omega = 3.1, 0.91, 0.77, 2.4
    s = source_dc_reduced(beta, gamma, a)
    assert math.isclose(4.0 * math.pi * g_dc(beta, gamma, omega) * rho_phase(a, omega), s, rel_tol=1e-14)


def test_rate_rescaling_moves_G_and_rho_inversely():
    beta, gamma, a, omega, lam = 2.7, 1.03, 1.2, 1.8, 3.0
    g0 = g_dc(beta, gamma, omega)
    g1 = g_dc(beta, gamma, lam * omega)
    r0 = rho_phase(a, omega)
    r1 = rho_phase(a, lam * omega)
    assert math.isclose(g1 / g0, lam**-2, rel_tol=1e-14)
    assert math.isclose(r1 / r0, lam**2, rel_tol=1e-14)
    assert math.isclose(g0 * r0, g1 * r1, rel_tol=1e-14)


def test_einstein_kappa_source_matches_newton_source():
    beta, gamma, a, omega = 3.4, 0.72, 0.9, 1.6
    g = g_dc(beta, gamma, omega)
    kappa_e = 8.0 * math.pi * g
    rho = rho_phase(a, omega)
    s_e = 0.5 * kappa_e * rho
    assert math.isclose(s_e, source_dc_reduced(beta, gamma, a), rel_tol=1e-14)
