import math


def beta_from_cp(c_p):
    return 3.0 * c_p


def g2_from_cp(c_p):
    if c_p <= 0:
        raise ValueError("positive plaquette action coefficient required")
    return 2.0 / c_p


def alpha_from_cp(c_p):
    return c_p / 2.0


def test_project_coefficient_to_wilson_beta():
    c_p = 0.94
    assert math.isclose(beta_from_cp(c_p), 2.82, rel_tol=1e-15)


def test_project_coefficient_to_bare_g2():
    c_p = 1.2
    g2 = g2_from_cp(c_p)
    assert math.isclose(g2, 2.0 / 1.2, rel_tol=1e-15)
    assert math.isclose(6.0 / g2, beta_from_cp(c_p), rel_tol=1e-15)


def test_alpha_binding_iff_cp_equals_two_alpha():
    alpha = 0.47483961905223004
    c_p = 2.0 * alpha
    assert math.isclose(alpha_from_cp(c_p), alpha, rel_tol=1e-15)
    assert math.isclose(beta_from_cp(c_p), 6.0 * alpha, rel_tol=1e-15)


def test_wrong_cp_breaks_alpha_binding():
    alpha = 0.47483961905223004
    c_p = 1.9 * alpha
    assert not math.isclose(alpha_from_cp(c_p), alpha, rel_tol=1e-12)


def test_archive_and_canonical_beta_sensitivity():
    alpha_legacy = 0.47481202619417856
    alpha_canonical = 0.47483961905223004
    assert math.isclose(
        (6.0 * alpha_canonical) / (6.0 * alpha_legacy),
        alpha_canonical / alpha_legacy,
        rel_tol=1e-15,
    )
