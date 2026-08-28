import math


def kappa_e_double_copy(beta_w, gamma_dc, omega_q):
    return 144.0 * gamma_dc**2 / (beta_w**2 * omega_q**2)


def einstein_hilbert_coefficient(beta_w, gamma_dc, omega_q):
    return beta_w**2 * omega_q**2 / (288.0 * gamma_dc**2)


def test_einstein_hilbert_coefficient_is_inverse_two_kappa_e():
    beta_w, gamma_dc, omega_q = 5.9, 0.93, 3.1
    kappa_e = kappa_e_double_copy(beta_w, gamma_dc, omega_q)
    assert math.isclose(
        einstein_hilbert_coefficient(beta_w, gamma_dc, omega_q),
        1.0 / (2.0 * kappa_e),
        rel_tol=1e-14,
    )


def test_graviton_and_einstein_action_normalizations_match():
    beta_w, gamma_dc, omega_q = 6.2, 1.07, 2.7
    g_squared = 6.0 / beta_w
    m_star = 0.5 * omega_q
    kappa_g = 2.0 * gamma_dc * g_squared / m_star
    kappa_e = kappa_e_double_copy(beta_w, gamma_dc, omega_q)

    assert math.isclose(kappa_e, kappa_g**2 / 4.0, rel_tol=1e-14)
    assert math.isclose(
        einstein_hilbert_coefficient(beta_w, gamma_dc, omega_q),
        2.0 / kappa_g**2,
        rel_tol=1e-14,
    )


def test_same_action_normalization_recovers_rfn1c_source_law():
    beta_w, gamma_dc, omega_q, j_q = 6.0, 0.89, 3.5, 2.2
    kappa_e = kappa_e_double_copy(beta_w, gamma_dc, omega_q)
    rho_m = 0.5 * omega_q * j_q
    source_from_einstein = 0.5 * kappa_e * rho_m
    source_from_rfn1c = 36.0 * gamma_dc**2 * j_q / (beta_w**2 * omega_q)

    assert math.isclose(source_from_einstein, source_from_rfn1c, rel_tol=1e-14)


def test_normalization_triangle_matches_newton_coordinate():
    beta_w, gamma_dc, omega_q = 5.7, 0.96, 4.0
    kappa_e = kappa_e_double_copy(beta_w, gamma_dc, omega_q)
    g_newton = kappa_e / (8.0 * math.pi)

    assert math.isclose(
        1.0 / (2.0 * kappa_e),
        1.0 / (16.0 * math.pi * g_newton),
        rel_tol=1e-14,
    )
