from __future__ import annotations

import math

import numpy as np
import sympy as sp


def test_conformal_scalar_curvature_linear_log_scale() -> None:
    # h_ij = exp(2 k x) delta_ij. Exact 3D conformal formula predicts
    # R = -2 k^2 exp(-2 k x).
    x, y, z, k = sp.symbols("x y z k", real=True)
    coords = (x, y, z)
    sigma = k * x
    a2 = sp.exp(2 * sigma)
    g = sp.diag(a2, a2, a2)
    g_inv = sp.simplify(g.inv())
    n = 3
    Gamma = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(n)]
    for r in range(n):
        for m in range(n):
            for q in range(n):
                Gamma[r][m][q] = sp.simplify(
                    sp.Rational(1, 2)
                    * sum(
                        g_inv[r, s]
                        * (
                            sp.diff(g[s, q], coords[m])
                            + sp.diff(g[s, m], coords[q])
                            - sp.diff(g[m, q], coords[s])
                        )
                        for s in range(n)
                    )
                )
    Ric = sp.MutableDenseMatrix.zeros(n, n)
    for m in range(n):
        for q in range(n):
            Ric[m, q] = sp.simplify(
                sum(
                    sp.diff(Gamma[r][m][q], coords[r])
                    - sp.diff(Gamma[r][m][r], coords[q])
                    + sum(
                        Gamma[r][r][s] * Gamma[s][m][q]
                        - Gamma[r][q][s] * Gamma[s][m][r]
                        for s in range(n)
                    )
                    for r in range(n)
                )
            )
    R = sp.simplify(sum(g_inv[m, q] * Ric[m, q] for m in range(n) for q in range(n)))
    expected = -2 * k**2 * sp.exp(-2 * k * x)
    assert sp.simplify(R - expected) == 0


def test_phase_rate_curvature_formula_matches_conformal_form() -> None:
    # Dimensionless coordinates. Choose omega=exp(-k x), c=sqrt(6),
    # so a=c/(sqrt(6) omega)=exp(k x).
    x, k = sp.symbols("x k", real=True, positive=True)
    omega = sp.exp(-k * x)
    c2 = sp.Integer(6)
    R_omega = sp.simplify((24 * omega * sp.diff(omega, x, 2) - 36 * sp.diff(omega, x) ** 2) / c2)
    expected = -2 * k**2 * sp.exp(-2 * k * x)
    assert sp.simplify(R_omega - expected) == 0


def test_uniform_phase_rate_adds_no_scale_connection() -> None:
    # q_i = E_i ln|omega| vanishes for constant omega.
    omega = 7.83
    grad_log_omega = np.zeros(3)
    assert np.allclose(grad_log_omega, 0.0)
    # scale-induced antisymmetric connection coefficients vanish.
    for i in range(3):
        for j in range(3):
            coeff = -grad_log_omega[j] if i != j else 0.0
            assert coeff == 0.0


def test_constant_lapse_static_metric_has_zero_Gamma_i_tt() -> None:
    # Gamma^i_tt = -1/2 h^{ij} partial_j g_tt; constant g_tt -> zero.
    h_inv = np.diag([2.0, 3.0, 5.0])
    grad_gtt = np.zeros(3)
    gamma = -0.5 * h_inv @ grad_gtt
    assert np.allclose(gamma, 0.0)


def test_nontrivial_lapse_gives_exact_static_acceleration() -> None:
    c = 299_792_458.0
    N = 1.0000001
    h_inv = np.eye(3)
    grad_N = np.array([1.0e-15, -2.0e-15, 0.5e-15])
    gamma_tt = c**2 * N * (h_inv @ grad_N)
    acceleration = -gamma_tt
    expected = -c**2 * N * grad_N
    assert np.allclose(acceleration, expected)


def test_weak_lapse_recovers_force_potential_gradient() -> None:
    # N = 1 + Phi/c^2 and h=I. At first weak-field order,
    # -c^2 N grad N = -grad Phi + O(Phi grad Phi/c^2).
    c = 299_792_458.0
    Phi = 1.0e6
    grad_Phi = np.array([3.0, -4.0, 1.5])
    N = 1.0 + Phi / c**2
    grad_N = grad_Phi / c**2
    a_exact = -c**2 * N * grad_N
    a_newton_kinematic = -grad_Phi
    relative = np.linalg.norm(a_exact - a_newton_kinematic) / np.linalg.norm(a_newton_kinematic)
    assert relative < 1.0e-9


def test_so3_gluing_preserves_metric() -> None:
    theta = 0.37
    R = np.array(
        [
            [math.cos(theta), -math.sin(theta), 0.0],
            [math.sin(theta), math.cos(theta), 0.0],
            [0.0, 0.0, 1.0],
        ]
    )
    h = np.diag([2.0, 2.0, 2.0])
    assert np.allclose(R.T @ h @ R, h, atol=1e-12, rtol=1e-12)
    assert np.allclose(R.T @ R, np.eye(3), atol=1e-12, rtol=1e-12)
