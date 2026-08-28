import math


def g_from_kappa(kappa_g):
    return kappa_g * kappa_g / (32.0 * math.pi)


def g_factorized(g1, g2, m_star, gamma_dc=1.0):
    return gamma_dc * gamma_dc * g1 * g1 * g2 * g2 / (8.0 * math.pi * m_star * m_star)


def test_double_copy_factorization_reconstructs_kappa_definition():
    g1, g2, m_star, gamma = 0.61, 0.47, 3.2, 0.83
    kappa_g = 2.0 * gamma * g1 * g2 / m_star
    assert math.isclose(
        g_from_kappa(kappa_g),
        g_factorized(g1, g2, m_star, gamma),
        rel_tol=1e-14,
        abs_tol=1e-14,
    )


def test_self_copy_reduction_uses_fourth_power_of_gauge_coupling():
    g_yang_mills, m_star, gamma = 0.72, 4.1, 1.0
    expected = g_yang_mills ** 4 / (8.0 * math.pi * m_star ** 2)
    assert math.isclose(
        g_factorized(g_yang_mills, g_yang_mills, m_star, gamma),
        expected,
        rel_tol=1e-14,
        abs_tol=1e-14,
    )


def test_epsilon_carrier_candidate_gives_dtau_chi_form():
    g_yang_mills, gamma, d_tau_chi = 0.66, 0.91, 5.7
    epsilon_n = 0.5 * d_tau_chi
    via_epsilon = gamma ** 2 * g_yang_mills ** 4 / (8.0 * math.pi * epsilon_n ** 2)
    via_rate = gamma ** 2 * g_yang_mills ** 4 / (2.0 * math.pi * d_tau_chi ** 2)
    assert math.isclose(via_epsilon, via_rate, rel_tol=1e-14, abs_tol=1e-14)


def test_mass_scale_doubling_quarters_candidate_G():
    g1, g2, m_star = 0.6, 0.5, 3.0
    G0 = g_factorized(g1, g2, m_star)
    G1 = g_factorized(g1, g2, 2.0 * m_star)
    assert math.isclose(G1 / G0, 0.25, rel_tol=1e-14, abs_tol=1e-14)


def test_self_copy_coupling_doubling_multiplies_candidate_G_by_sixteen():
    g, m_star = 0.4, 2.8
    G0 = g_factorized(g, g, m_star)
    G1 = g_factorized(2.0 * g, 2.0 * g, m_star)
    assert math.isclose(G1 / G0, 16.0, rel_tol=1e-14, abs_tol=1e-14)


def test_matched_jacobi_triplet_has_zero_defect():
    n_i, n_j = 0.73, -0.21
    n_k = -(n_i + n_j)
    defect = abs(n_i + n_j + n_k)
    assert defect < 1e-15


def test_adversarial_kinematic_triplet_fails_jacobi_gate():
    n_i, n_j, n_k = 0.73, -0.21, 0.19
    defect = abs(n_i + n_j + n_k)
    assert defect > 0.1


def test_independent_double_copy_normalization_changes_G_quadratically():
    g1, g2, m_star = 0.52, 0.63, 3.7
    G1 = g_factorized(g1, g2, m_star, gamma_dc=1.0)
    G2 = g_factorized(g1, g2, m_star, gamma_dc=1.5)
    assert math.isclose(G2 / G1, 2.25, rel_tol=1e-14, abs_tol=1e-14)
