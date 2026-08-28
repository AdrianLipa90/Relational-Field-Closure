import math


def homogeneous_scalar(A, omega, m):
    K = A * A * omega * omega
    V = A * A * m * m
    eps = K + V
    p = K - V
    j = 2 * A * A * omega
    return K, V, eps, p, j


def test_harmonic_on_shell_condition_sets_omega_squared_equal_m_squared():
    for m in [0.2, 0.7, 1.0, 3.4]:
        omega = m
        assert math.isclose(omega * omega, m * m, rel_tol=0, abs_tol=1e-15)


def test_on_shell_quadratic_potential_equals_phase_kinetic_density():
    A, m = 1.3, 0.81
    K, V, _, _, _ = homogeneous_scalar(A, m, m)
    assert math.isclose(V, K, rel_tol=1e-15)


def test_on_shell_homogeneous_scalar_is_pressureless():
    A, m = 0.9, 1.2
    _, _, _, p, _ = homogeneous_scalar(A, m, m)
    assert abs(p) < 1e-14


def test_total_energy_density_is_twice_phase_kinetic_density():
    A, m = 1.1, 0.63
    K, _, eps, _, _ = homogeneous_scalar(A, m, m)
    assert math.isclose(eps, 2 * K, rel_tol=1e-15)


def test_phase_kinetic_and_total_energy_per_noether_charge_differ_by_two():
    A, m = 1.4, 0.73
    K, _, eps, _, j = homogeneous_scalar(A, m, m)
    assert math.isclose(K / j, m / 2, rel_tol=1e-15)
    assert math.isclose(eps / j, m, rel_tol=1e-15)
    assert math.isclose((eps / j) / (K / j), 2.0, rel_tol=1e-15)


def test_dust_active_source_equals_total_energy_not_phase_K():
    A, m = 0.77, 1.09
    K, _, eps, p, _ = homogeneous_scalar(A, m, m)
    active = eps + 3 * p
    assert math.isclose(active, eps, rel_tol=1e-15)
    assert math.isclose(active, 2 * K, rel_tol=1e-15)
