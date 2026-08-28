import math


def g_newton(source_r, omega_q, j_q):
    return source_r / (2.0 * math.pi * omega_q * j_q)


def g_double_copy(beta_w, gamma_dc, omega_q):
    return 18.0 * gamma_dc**2 / (math.pi * beta_w**2 * omega_q**2)


def kappa_e_from_g(g_value):
    return 8.0 * math.pi * g_value


def kappa_e_double_copy(beta_w, gamma_dc, omega_q):
    return 144.0 * gamma_dc**2 / (beta_w**2 * omega_q**2)


def source_double_copy(beta_w, gamma_dc, omega_q, j_q):
    return 36.0 * gamma_dc**2 * j_q / (beta_w**2 * omega_q)


def g_horizon(m_h, kappa_h):
    return 1.0 / (4.0 * m_h * kappa_h)


def residuals(beta_w, gamma_dc, omega_q, j_q, source_r, m_h, kappa_h):
    c_sd = beta_w**2 * source_r * omega_q - 36.0 * gamma_dc**2 * j_q
    c_sh = 2.0 * m_h * kappa_h * source_r - math.pi * omega_q * j_q
    c_dh = 72.0 * gamma_dc**2 * m_h * kappa_h - math.pi * beta_w**2 * omega_q**2
    return c_sd, c_sh, c_dh


def test_double_copy_source_matches_newton_and_einstein_normalization():
    beta_w, gamma_dc, omega_q, j_q = 5.9, 0.91, 3.7, 2.4
    source_r = source_double_copy(beta_w, gamma_dc, omega_q, j_q)
    rho_m = 0.5 * omega_q * j_q
    g_dc = g_double_copy(beta_w, gamma_dc, omega_q)
    kappa_e = kappa_e_double_copy(beta_w, gamma_dc, omega_q)

    assert math.isclose(source_r, 4.0 * math.pi * g_dc * rho_m, rel_tol=1e-14)
    assert math.isclose(source_r, 0.5 * kappa_e * rho_m, rel_tol=1e-14)
    assert math.isclose(kappa_e, kappa_e_from_g(g_dc), rel_tol=1e-14)


def test_newton_estimator_equals_double_copy_on_source_double_copy_surface():
    beta_w, gamma_dc, omega_q, j_q = 6.1, 1.03, 2.8, 1.7
    source_r = source_double_copy(beta_w, gamma_dc, omega_q, j_q)
    assert math.isclose(
        g_newton(source_r, omega_q, j_q),
        g_double_copy(beta_w, gamma_dc, omega_q),
        rel_tol=1e-14,
    )


def test_graviton_coupling_maps_to_einstein_field_coupling_by_one_quarter():
    beta_w, gamma_dc, omega_q = 5.8, 0.97, 4.1
    g_squared = 6.0 / beta_w
    m_star = 0.5 * omega_q
    kappa_g = 2.0 * gamma_dc * g_squared / m_star

    assert math.isclose(
        kappa_g**2 / 4.0,
        kappa_e_double_copy(beta_w, gamma_dc, omega_q),
        rel_tol=1e-14,
    )


def test_three_routes_close_when_inputs_share_one_coupling():
    beta_w, gamma_dc, omega_q, j_q = 6.0, 0.88, 3.2, 2.1
    source_r = source_double_copy(beta_w, gamma_dc, omega_q, j_q)
    g_dc = g_double_copy(beta_w, gamma_dc, omega_q)
    m_h = 2.3
    kappa_h = 1.0 / (4.0 * m_h * g_dc)

    c_sd, c_sh, c_dh = residuals(
        beta_w, gamma_dc, omega_q, j_q, source_r, m_h, kappa_h
    )

    assert abs(c_sd) < 1e-12
    assert abs(c_sh) < 1e-12
    assert abs(c_dh) < 1e-12
    assert math.isclose(g_horizon(m_h, kappa_h), g_dc, rel_tol=1e-14)


def test_coupling_holonomy_syzygy_is_exact_off_shell():
    beta_w, gamma_dc, omega_q, j_q = 5.7, 1.11, 2.9, 1.6
    source_r, m_h, kappa_h = 0.27, 3.4, 0.19
    c_sd, c_sh, c_dh = residuals(
        beta_w, gamma_dc, omega_q, j_q, source_r, m_h, kappa_h
    )

    lhs = source_r * c_dh
    rhs = 36.0 * gamma_dc**2 * c_sh - math.pi * omega_q * c_sd
    assert math.isclose(lhs, rhs, rel_tol=1e-13, abs_tol=1e-13)


def test_source_perturbation_breaks_source_routes_while_syzygy_remains_exact():
    beta_w, gamma_dc, omega_q, j_q = 6.0, 0.88, 3.2, 2.1
    source_r = 1.07 * source_double_copy(beta_w, gamma_dc, omega_q, j_q)
    g_dc = g_double_copy(beta_w, gamma_dc, omega_q)
    m_h = 2.3
    kappa_h = 1.0 / (4.0 * m_h * g_dc)

    c_sd, c_sh, c_dh = residuals(
        beta_w, gamma_dc, omega_q, j_q, source_r, m_h, kappa_h
    )

    assert abs(c_sd) > 1e-3
    assert abs(c_sh) > 1e-3
    assert abs(c_dh) < 1e-12
    assert math.isclose(
        source_r * c_dh,
        36.0 * gamma_dc**2 * c_sh - math.pi * omega_q * c_sd,
        rel_tol=1e-12,
        abs_tol=1e-12,
    )
