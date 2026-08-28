import cmath
import math


def test_primitive_euclidean_horizon_period_closes_at_two_pi():
    kappa_h = 0.37
    beta_h = 2.0 * math.pi / kappa_h
    assert math.isclose(kappa_h * beta_h, 2.0 * math.pi, rel_tol=1e-12, abs_tol=1e-12)


def test_primitive_horizon_holonomy_is_unity():
    kappa_h = 0.91
    beta_h = 2.0 * math.pi / kappa_h
    assert abs(cmath.exp(1j * kappa_h * beta_h) - 1.0) < 1e-12


def test_hawking_temperature_matches_inverse_period():
    kappa_h = 1.23
    beta_h = 2.0 * math.pi / kappa_h
    assert math.isclose(1.0 / beta_h, kappa_h / (2.0 * math.pi), rel_tol=1e-12, abs_tol=1e-12)


def test_detuned_period_fails_regular_horizon_gate():
    kappa_h = 0.8
    beta_h = 2.0 * math.pi / kappa_h
    beta_bad = 1.07 * beta_h
    delta_cone = 2.0 * math.pi - kappa_h * beta_bad
    W_bad = cmath.exp(1j * kappa_h * beta_bad)
    assert abs(delta_cone) > 1e-3
    assert abs(W_bad - 1.0) > 1e-3


def test_integer_multicovers_retain_u1_closure():
    kappa_h = 0.44
    for n in range(1, 6):
        beta_n = 2.0 * math.pi * n / kappa_h
        assert abs(cmath.exp(1j * kappa_h * beta_n) - 1.0) < 1e-12


def test_ab_horizon_isomorphism_preserves_u1_loop_map_shape():
    phi_ab = 0.731
    phi_h = 0.731
    assert cmath.exp(1j * phi_ab) == cmath.exp(1j * phi_h)
