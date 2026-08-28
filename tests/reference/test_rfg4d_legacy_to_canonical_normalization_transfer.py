import math


def coordinates():
    kappa = math.log(2.0) / (24.0 * math.pi)
    I0 = 0.009
    L3 = 7.0
    phi = (1.0 + math.sqrt(5.0)) / 2.0
    alpha_canonical = math.log(phi) - kappa * math.log(2.0)
    alpha_legacy = alpha_canonical - (kappa - I0) / L3
    return kappa, I0, L3, alpha_legacy, alpha_canonical


def test_alpha_shift_equals_information_rounding_offset_over_L3():
    kappa, I0, L3, alpha_l, alpha_c = coordinates()
    assert math.isclose(alpha_c - alpha_l, (kappa - I0) / L3, rel_tol=2e-15, abs_tol=2e-15)


def test_legacy_and_canonical_coordinates_match_frozen_values():
    _, _, _, alpha_l, alpha_c = coordinates()
    assert math.isclose(alpha_l, 0.47481202619417856, rel_tol=2e-15, abs_tol=2e-15)
    assert math.isclose(alpha_c, 0.47483961905223004, rel_tol=2e-15, abs_tol=2e-15)


def test_canonical_alpha_shift_is_about_58_ppm():
    _, _, _, alpha_l, alpha_c = coordinates()
    ppm = (alpha_c / alpha_l - 1.0) * 1e6
    assert 58.0 < ppm < 58.2


def test_candidate_yang_mills_coupling_decreases_under_canonicalization():
    _, _, _, alpha_l, alpha_c = coordinates()
    g_l = alpha_l ** -0.5
    g_c = alpha_c ** -0.5
    assert g_c < g_l
    assert math.isclose(g_c / g_l, math.sqrt(alpha_l / alpha_c), rel_tol=2e-15, abs_tol=2e-15)


def test_su3_wilson_beta_shift_matches_alpha_shift_exactly():
    _, _, _, alpha_l, alpha_c = coordinates()
    beta_l = 6.0 * alpha_l
    beta_c = 6.0 * alpha_c
    assert math.isclose(beta_c / beta_l, alpha_c / alpha_l, rel_tol=2e-15, abs_tol=2e-15)


def test_double_copy_G_candidate_transfer_is_inverse_square_of_alpha_transfer():
    _, _, _, alpha_l, alpha_c = coordinates()
    ratio = (alpha_l / alpha_c) ** 2
    assert math.isclose(ratio, 0.9998837836809062, rel_tol=2e-15, abs_tol=2e-15)
    ppm = (ratio - 1.0) * 1e6
    assert -116.3 < ppm < -116.1


def test_exact_transfer_agrees_with_first_order_sign_and_scale():
    _, _, _, alpha_l, alpha_c = coordinates()
    eps = alpha_c / alpha_l - 1.0
    exact_g = math.sqrt(alpha_l / alpha_c) - 1.0
    exact_G = (alpha_l / alpha_c) ** 2 - 1.0
    assert exact_g < 0.0
    assert exact_G < 0.0
    assert abs(exact_g + 0.5 * eps) < 2e-9
    assert abs(exact_G + 2.0 * eps) < 2e-8
