import numpy as np

ETA = np.diag([-1.0, 1.0, 1.0, 1.0])


def stress_phase(A, q_cov, V=0.0):
    q_cov = np.asarray(q_cov, float)
    q_con = ETA @ q_cov
    q2 = float(q_cov @ q_con)
    L = -A * A * q2 - V
    return 2 * A * A * np.outer(q_cov, q_cov) + ETA * L


def active_density_from_orthonormal(T):
    return float(T[0, 0] + T[1, 1] + T[2, 2] + T[3, 3])


def test_pure_normal_phase_matches_rfn1b2o_energy_density():
    A, r = 1.7, 0.83
    T = stress_phase(A, [r, 0, 0, 0])
    K = A * A * r * r
    assert abs(T[0, 0] - K) < 1e-14


def test_pure_normal_phase_is_stiff_pressure_sector():
    A, r = 0.9, 1.2
    T = stress_phase(A, [r, 0, 0, 0])
    K = A * A * r * r
    assert np.allclose(np.diag(T), [K, K, K, K], rtol=0, atol=1e-14)


def test_phase_only_active_einstein_source_is_four_times_energy_density():
    A, r = 1.1, 0.73
    T = stress_phase(A, [r, 0, 0, 0])
    K = A * A * r * r
    assert abs(active_density_from_orthonormal(T) - 4 * K) < 1e-14


def test_potential_changes_energy_pressure_and_active_source():
    A, r, V = 1.3, 0.61, 0.27
    K = A * A * r * r
    T = stress_phase(A, [r, 0, 0, 0], V=V)
    eps = K + V
    p = K - V
    assert abs(T[0, 0] - eps) < 1e-14
    assert np.allclose([T[1, 1], T[2, 2], T[3, 3]], [p, p, p], atol=1e-14)
    assert abs(active_density_from_orthonormal(T) - (4 * K - 2 * V)) < 1e-14


def test_dust_condition_requires_V_equal_K_for_homogeneous_scalar():
    A, r = 0.8, 0.91
    K = A * A * r * r
    T = stress_phase(A, [r, 0, 0, 0], V=K)
    assert np.allclose([T[1, 1], T[2, 2], T[3, 3]], [0, 0, 0], atol=1e-14)
    assert abs(T[0, 0] - 2 * K) < 1e-14


def test_if_newton_target_is_phase_K_active_source_condition_is_V_3K_over_2():
    A, r = 1.2, 0.77
    K = A * A * r * r
    V = 1.5 * K
    T = stress_phase(A, [r, 0, 0, 0], V=V)
    assert abs(active_density_from_orthonormal(T) - K) < 1e-14
