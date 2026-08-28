import math

import numpy as np
import pytest

ETA = np.diag([-1.0, 1.0, 1.0, 1.0])


def finite4(values, name):
    out = np.asarray(values, dtype=float)
    if out.shape != (4,) or not np.all(np.isfinite(out)):
        raise ValueError(f"{name} must be one finite four-vector")
    return out


def phase_one_form(dtheta, potential, charge, hbar):
    dtheta = finite4(dtheta, "dtheta")
    potential = finite4(potential, "potential")
    if not math.isfinite(hbar) or hbar == 0.0:
        raise ValueError("hbar must be finite and nonzero")
    if not math.isfinite(charge):
        raise ValueError("charge must be finite")
    return dtheta + (charge / hbar) * potential


def direct_polar_kinetic(A, theta, grad_A, q_cov):
    grad_A = finite4(grad_A, "grad_A")
    q_cov = finite4(q_cov, "q_cov")
    if not math.isfinite(A) or not math.isfinite(theta):
        raise ValueError("A and theta must be finite")
    phase = complex(math.cos(theta), math.sin(theta))
    dpsi = phase * (grad_A.astype(complex) + 1j * A * q_cov)
    return float(np.vdot(dpsi, ETA @ dpsi).real)


def decomposed_kinetic(A, grad_A, q_cov):
    grad_A = finite4(grad_A, "grad_A")
    q_cov = finite4(q_cov, "q_cov")
    return float(grad_A @ ETA @ grad_A + A * A * (q_cov @ ETA @ q_cov))


def scalar_stress(A, grad_A, q_cov, V):
    grad_A = finite4(grad_A, "grad_A")
    q_cov = finite4(q_cov, "q_cov")
    if not all(math.isfinite(x) for x in (A, V)):
        raise ValueError("A and V must be finite")
    grad2 = float(grad_A @ ETA @ grad_A)
    q2 = float(q_cov @ ETA @ q_cov)
    L = -grad2 - A * A * q2 - V
    return 2.0 * np.outer(grad_A, grad_A) + 2.0 * A * A * np.outer(q_cov, q_cov) + ETA * L


def stress_parts(A, grad_A, q_cov, V):
    grad_A = finite4(grad_A, "grad_A")
    q_cov = finite4(q_cov, "q_cov")
    grad2 = float(grad_A @ ETA @ grad_A)
    q2 = float(q_cov @ ETA @ q_cov)
    T_amp = 2.0 * np.outer(grad_A, grad_A) - ETA * grad2
    T_phase = 2.0 * A * A * np.outer(q_cov, q_cov) - ETA * (A * A * q2)
    T_pot = -ETA * V
    return T_amp, T_phase, T_pot


def em_current_from_scalar_carrier(j_theta, charge, hbar):
    if not math.isfinite(hbar) or hbar == 0.0:
        raise ValueError("hbar must be finite and nonzero")
    return (charge / hbar) * finite4(j_theta, "j_theta")


def test_polar_kinetic_mixed_terms_cancel_exactly():
    A = 1.3
    theta = 0.71
    grad_A = [0.2, -0.5, 0.4, 0.1]
    q_cov = [1.1, 0.3, -0.2, 0.7]
    assert direct_polar_kinetic(A, theta, grad_A, q_cov) == pytest.approx(
        decomposed_kinetic(A, grad_A, q_cov), rel=0.0, abs=1e-14
    )


def test_full_scalar_tensor_recomposes_from_three_exact_parts():
    A = 0.93
    grad_A = [0.15, 0.2, -0.31, 0.27]
    q_cov = [1.4, -0.1, 0.45, 0.2]
    V = 0.37
    full = scalar_stress(A, grad_A, q_cov, V)
    parts = stress_parts(A, grad_A, q_cov, V)
    assert full == pytest.approx(sum(parts), rel=0.0, abs=1e-14)


def test_synchronized_gauge_shift_preserves_full_scalar_tensor():
    A = 1.1
    grad_A = [0.1, 0.2, 0.05, -0.2]
    dtheta = [0.7, -0.4, 0.2, 0.1]
    potential = [0.3, 0.9, -0.5, 0.4]
    dLambda = [0.6, -0.2, 0.8, 0.3]
    charge = 2.0
    hbar = 5.0
    before_q = phase_one_form(dtheta, potential, charge, hbar)
    shifted_theta = np.asarray(dtheta) + (charge / hbar) * np.asarray(dLambda)
    shifted_potential = np.asarray(potential) - np.asarray(dLambda)
    after_q = phase_one_form(shifted_theta, shifted_potential, charge, hbar)
    assert after_q == pytest.approx(before_q, rel=0.0, abs=1e-15)
    assert scalar_stress(A, grad_A, after_q, 0.2) == pytest.approx(
        scalar_stress(A, grad_A, before_q, 0.2), rel=0.0, abs=1e-14
    )


def test_rfe4_homogeneous_phase_limit_is_recovered():
    A, r, V = 1.2, 0.8, 0.23
    K = A * A * r * r
    T = scalar_stress(A, np.zeros(4), [r, 0.0, 0.0, 0.0], V)
    epsilon = K + V
    pressure = K - V
    assert T[0, 0] == pytest.approx(epsilon, rel=0.0, abs=1e-14)
    assert np.diag(T)[1:] == pytest.approx([pressure] * 3, rel=0.0, abs=1e-14)
    assert float(np.trace(T)) == pytest.approx(4.0 * K - 2.0 * V, rel=0.0, abs=1e-14)


def test_rfe5_onshell_massive_dust_and_factor_two_are_recovered():
    A, omega = 0.87, 1.6
    K = A * A * omega * omega
    T = scalar_stress(A, np.zeros(4), [omega, 0.0, 0.0, 0.0], K)
    j_theta = 2.0 * A * A * omega
    assert T[0, 0] == pytest.approx(2.0 * K, rel=0.0, abs=1e-14)
    assert np.diag(T)[1:] == pytest.approx(np.zeros(3), rel=0.0, abs=1e-14)
    assert K / j_theta == pytest.approx(omega / 2.0, rel=0.0, abs=1e-14)
    assert T[0, 0] / j_theta == pytest.approx(omega, rel=0.0, abs=1e-14)


def test_spatial_amplitude_gradient_has_anisotropic_principal_stress():
    g = 0.73
    T = scalar_stress(1.0, [0.0, g, 0.0, 0.0], np.zeros(4), 0.0)
    expected = [g * g, g * g, -g * g, -g * g]
    assert np.diag(T) == pytest.approx(expected, rel=0.0, abs=1e-14)
    assert T[0, 0] > 0.0


def test_neutral_scalar_can_source_gravity_with_zero_maxwell_current():
    A = 1.0
    grad_A = [0.2, 0.3, 0.0, -0.1]
    q_cov = [0.9, -0.2, 0.4, 0.1]
    T = scalar_stress(A, grad_A, q_cov, 0.5)
    j_theta = [2.0, -1.0, 0.5, 0.25]
    j_em = em_current_from_scalar_carrier(j_theta, 0.0, 1.0)
    assert np.linalg.norm(T) > 0.0
    assert j_em == pytest.approx(np.zeros(4), rel=0.0, abs=1e-15)


def test_einstein_source_ledger_is_exact_tensor_sum():
    scalar = scalar_stress(1.1, [0.1, 0.2, 0.3, -0.1], [0.7, 0.1, -0.2, 0.4], 0.3)
    em = np.asarray(
        [
            [2.0, 0.1, 0.2, -0.3],
            [0.1, 0.7, 0.0, 0.1],
            [0.2, 0.0, 0.8, -0.2],
            [-0.3, 0.1, -0.2, 0.5],
        ]
    )
    total = em + scalar
    assert total - em == pytest.approx(scalar, rel=0.0, abs=1e-14)
    assert total - scalar == pytest.approx(em, rel=0.0, abs=1e-14)


def test_fail_closed_on_bad_four_vectors_and_zero_hbar():
    with pytest.raises(ValueError, match="finite four-vector"):
        scalar_stress(1.0, [0.0, 1.0], np.zeros(4), 0.0)
    with pytest.raises(ValueError, match="finite four-vector"):
        phase_one_form(np.zeros(4), [0.0, float("nan"), 0.0, 0.0], 1.0, 1.0)
    with pytest.raises(ValueError, match="finite and nonzero"):
        phase_one_form(np.zeros(4), np.zeros(4), 1.0, 0.0)
