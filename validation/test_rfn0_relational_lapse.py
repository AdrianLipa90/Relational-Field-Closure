from __future__ import annotations

import math

import numpy as np


def test_lapse_ratio_positive() -> None:
    phi_x, phi_ref = 2.4, 1.2
    N = phi_x / phi_ref
    assert N > 0.0
    assert math.isclose(N, 2.0)


def test_lapse_metric_has_lorentzian_inertia() -> None:
    N = 1.3
    c = 2.0
    h = np.diag([2.0, 3.0, 5.0])
    g = np.zeros((4, 4))
    g[0, 0] = -(N * c) ** 2
    g[1:, 1:] = h
    eig = np.linalg.eigvalsh(g)
    assert np.count_nonzero(eig < 0.0) == 1
    assert np.count_nonzero(eig > 0.0) == 3


def test_static_acceleration_matches_lapse_gradient_formula() -> None:
    c = 299_792_458.0
    N = 1.000001
    h_inv = np.diag([1.0, 0.8, 1.2])
    grad_N = np.array([2.0e-16, -1.0e-16, 0.5e-16])
    gamma_tt = c**2 * N * (h_inv @ grad_N)
    acceleration = -gamma_tt
    expected = -c**2 * N * (h_inv @ grad_N)
    assert np.allclose(acceleration, expected)


def test_phi_R_exact_gradient_relation() -> None:
    c = 299_792_458.0
    N = 1.02
    grad_N = np.array([1.0e-9, -2.0e-9, 0.5e-9])
    grad_ln_N = grad_N / N
    grad_phi = c**2 * grad_ln_N
    a1 = -c**2 * N**2 * grad_ln_N
    a2 = -N**2 * grad_phi
    assert np.allclose(a1, a2)


def test_weak_lapse_force_form() -> None:
    c = 299_792_458.0
    eps = 1.0e-10
    N = 1.0 + eps
    grad_phi = np.array([0.4, -0.2, 0.1])
    a = -N**2 * grad_phi
    target = -grad_phi
    rel = np.linalg.norm(a - target) / np.linalg.norm(target)
    assert rel < 3.0e-10


def test_kinetic_gradient_acceleration_decomposition() -> None:
    c = 10.0
    N = 1.1
    h_inv = np.eye(3)
    M = 2.0
    A = 0.6
    grad_M = np.array([0.2, -0.1, 0.05])
    grad_A = np.array([0.04, 0.03, -0.02])
    grad_ln_N = grad_M / M + 0.5 * math.tanh(A / 2.0) * grad_A
    a = -c**2 * N**2 * (h_inv @ grad_ln_N)
    expected = -c**2 * N**2 * (grad_M / M + 0.5 * math.tanh(A / 2.0) * grad_A)
    assert np.allclose(a, expected)


def test_density_viscosity_drive_decomposition() -> None:
    rho_a, rho_b = 2.0, 5.0
    eta_a, eta_b = 3.0, 7.0
    A = 0.4
    grad_ln_rho_a = np.array([0.1, -0.2, 0.05])
    grad_ln_rho_b = np.array([-0.02, 0.03, 0.04])
    grad_eta_a = np.array([0.03, 0.02, -0.01])
    grad_eta_b = np.array([-0.01, 0.04, 0.02])
    grad_A = np.array([0.06, -0.02, 0.01])
    eta_mean = 0.5 * (eta_a + eta_b)
    grad_eta_mean = 0.5 * (grad_eta_a + grad_eta_b)
    grad_ln_M = 0.5 * grad_ln_rho_a + 0.5 * grad_ln_rho_b - grad_eta_mean / eta_mean
    full = grad_ln_M + 0.5 * math.tanh(A / 2.0) * grad_A
    expanded = (
        0.5 * grad_ln_rho_a
        + 0.5 * grad_ln_rho_b
        - grad_eta_mean / eta_mean
        + 0.5 * math.tanh(A / 2.0) * grad_A
    )
    assert np.allclose(full, expanded)
