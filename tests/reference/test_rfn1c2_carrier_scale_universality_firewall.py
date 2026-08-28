import math


def g_from_dc(gamma, g2, mstar):
    return gamma**2 * g2**2 / (8.0 * math.pi * mstar**2)


def reduced_gravity_scale(gamma, g2, mstar):
    return mstar / (gamma * g2)


def reduced_gravity_scale_wilson(beta, gamma, mstar):
    return beta * mstar / (6.0 * gamma)


def reduced_gravity_scale_local(beta, gamma, omega):
    return beta * omega / (12.0 * gamma)


def test_dc_G_is_inverse_eight_pi_reduced_scale_squared():
    gamma, g2, m = 0.84, 1.23, 2.7
    mbar = reduced_gravity_scale(gamma, g2, m)
    assert math.isclose(g_from_dc(gamma, g2, m), 1.0 / (8.0 * math.pi * mbar * mbar), rel_tol=1e-14)


def test_wilson_reduced_scale_identity():
    beta, gamma, m = 3.2, 0.91, 4.4
    g2 = 6.0 / beta
    assert math.isclose(reduced_gravity_scale(gamma, g2, m), reduced_gravity_scale_wilson(beta, gamma, m), rel_tol=1e-14)


def test_local_carrier_binding_gives_beta_omega_over_twelve_gamma():
    beta, gamma, omega = 2.8, 1.07, 3.6
    m = omega / 2.0
    assert math.isclose(reduced_gravity_scale_wilson(beta, gamma, m), reduced_gravity_scale_local(beta, gamma, omega), rel_tol=1e-14)


def test_equal_reduced_scale_implies_equal_G_across_systems():
    beta1, gamma1, omega1 = 2.4, 0.8, 3.0
    target = reduced_gravity_scale_local(beta1, gamma1, omega1)
    beta2, omega2 = 3.6, 1.7
    gamma2 = beta2 * omega2 / (12.0 * target)
    mbar2 = reduced_gravity_scale_local(beta2, gamma2, omega2)
    assert math.isclose(mbar2, target, rel_tol=1e-14)
    G1 = 1.0 / (8.0 * math.pi * target**2)
    G2 = 1.0 / (8.0 * math.pi * mbar2**2)
    assert math.isclose(G1, G2, rel_tol=1e-14)


def test_fixed_beta_gamma_with_different_omega_fails_universal_G():
    beta, gamma = 3.0, 1.0
    m1 = reduced_gravity_scale_local(beta, gamma, 1.0)
    m2 = reduced_gravity_scale_local(beta, gamma, 2.0)
    G1 = 1.0 / (8.0 * math.pi * m1 * m1)
    G2 = 1.0 / (8.0 * math.pi * m2 * m2)
    assert math.isclose(G2 / G1, 0.25, rel_tol=1e-14)
    assert not math.isclose(G1, G2, rel_tol=1e-12)


def test_pairwise_universality_defect_zero_on_common_scale():
    mbar_a = 2.3
    mbar_b = 2.3
    defect = abs(math.log((mbar_b / mbar_a) ** 2))
    assert defect == 0.0
