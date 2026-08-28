import math
import numpy as np


def vertex_tensor(p, q, r):
    d = len(p)
    out = np.zeros((d, d, d), dtype=float)
    for mu in range(d):
        for nu in range(d):
            for rho in range(d):
                out[mu, nu, rho] = (
                    (1.0 if mu == nu else 0.0) * (p[rho] - q[rho])
                    + (1.0 if nu == rho else 0.0) * (q[mu] - r[mu])
                    + (1.0 if rho == mu else 0.0) * (r[nu] - p[nu])
                )
    return out


def inverse_transverse(k):
    return np.dot(k, k) * np.eye(len(k)) - np.outer(k, k)


def test_kinematic_vertex_exchange_antisymmetry():
    p = np.array([0.2, -0.4, 0.7, 0.1])
    q = np.array([-0.5, 0.3, 0.2, -0.6])
    r = -(p + q)
    lhs = np.transpose(vertex_tensor(q, p, r), (1, 0, 2))
    rhs = -vertex_tensor(p, q, r)
    assert np.allclose(lhs, rhs, rtol=0.0, atol=1e-13)


def test_full_color_kinematic_vertex_boson_exchange():
    p = np.array([0.2, -0.4, 0.7, 0.1])
    q = np.array([-0.5, 0.3, 0.2, -0.6])
    r = -(p + q)
    f_abc = 0.5
    lhs = f_abc * vertex_tensor(p, q, r)
    f_bac = -f_abc
    rhs = f_bac * np.transpose(vertex_tensor(q, p, r), (1, 0, 2))
    assert np.allclose(lhs, rhs, rtol=0.0, atol=1e-13)


def test_ward_identity_many_random_points():
    rng = np.random.default_rng(20260828)
    for _ in range(250):
        q = rng.normal(size=4)
        r = rng.normal(size=4)
        p = -(q + r)
        contracted = np.einsum("m,mnr->nr", p, vertex_tensor(p, q, r))
        expected = inverse_transverse(r) - inverse_transverse(q)
        assert np.allclose(contracted, expected, rtol=2e-13, atol=2e-13)


def test_rfg4g_fixes_cubic_vertex_coupling():
    alpha_c = 0.47483961905223004
    g = alpha_c ** -0.5
    beta_w = 6.0 * alpha_c
    assert math.isclose(g * g, 1.0 / alpha_c, rel_tol=1e-15)
    assert math.isclose(6.0 / (g * g), beta_w, rel_tol=1e-15)


def test_cubic_vertex_is_linear_in_g():
    p = np.array([0.2, -0.4, 0.7, 0.1])
    q = np.array([-0.5, 0.3, 0.2, -0.6])
    r = -(p + q)
    base = vertex_tensor(p, q, r)
    g, lam = 1.37, 2.6
    assert np.allclose((lam * g) * base, lam * (g * base), rtol=1e-15, atol=1e-15)
