import cmath
import math


def test_spin_connection_integrates_to_two_pi():
    kappa_h = 0.77
    beta_h = 2.0 * math.pi / kappa_h
    assert math.isclose(kappa_h * beta_h, 2.0 * math.pi, rel_tol=1e-12, abs_tol=1e-12)


def test_integer_spin_sector_is_periodic():
    for m in range(-3, 4):
        assert abs(cmath.exp(1j * 2.0 * math.pi * m) - 1.0) < 1e-12


def test_spin_half_sector_is_antiperiodic():
    assert abs(cmath.exp(1j * math.pi) + 1.0) < 1e-12


def test_bosonic_matsubara_spacing():
    kappa_h = 0.63
    beta_h = 2.0 * math.pi / kappa_h
    for n in range(-4, 5):
        omega = 2.0 * math.pi * n / beta_h
        assert math.isclose(omega, n * kappa_h, rel_tol=1e-12, abs_tol=1e-12)


def test_fermionic_matsubara_spacing():
    kappa_h = 0.63
    beta_h = 2.0 * math.pi / kappa_h
    for n in range(-4, 5):
        omega = (2 * n + 1) * math.pi / beta_h
        assert math.isclose(omega, (n + 0.5) * kappa_h, rel_tol=1e-12, abs_tol=1e-12)


def test_two_spin_half_turns_restore_identity():
    W_half = cmath.exp(1j * math.pi)
    assert abs(W_half ** 2 - 1.0) < 1e-12
