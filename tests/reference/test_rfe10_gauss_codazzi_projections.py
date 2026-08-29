import math
import pytest


def inv_matrix(a):
    n = len(a)
    aug = [
        [float(x) for x in row] + [1.0 if i == j else 0.0 for j in range(n)]
        for i, row in enumerate(a)
    ]
    for i in range(n):
        pivot = max(range(i, n), key=lambda r: abs(aug[r][i]))
        if abs(aug[pivot][i]) < 1e-14:
            raise ValueError("singular matrix")
        aug[i], aug[pivot] = aug[pivot], aug[i]
        p = aug[i][i]
        aug[i] = [x / p for x in aug[i]]
        for r in range(n):
            if r == i:
                continue
            f = aug[r][i]
            aug[r] = [aug[r][c] - f * aug[i][c] for c in range(2 * n)]
    return [row[n:] for row in aug]


def curvature_at_point(g, dg, ddg):
    """Direct coordinate Ricci/Einstein tensor from g, first and second derivatives.

    dg[a][m][n] = partial_a g_mn
    ddg[a][b][m][n] = partial_a partial_b g_mn
    """
    n = len(g)
    gi = inv_matrix(g)

    dgi = [[[0.0] * n for _ in range(n)] for __ in range(n)]
    for a in range(n):
        for r in range(n):
            for s in range(n):
                dgi[a][r][s] = -sum(
                    gi[r][u] * dg[a][u][v] * gi[v][s]
                    for u in range(n)
                    for v in range(n)
                )

    gamma = [[[0.0] * n for _ in range(n)] for __ in range(n)]
    for r in range(n):
        for m in range(n):
            for q in range(n):
                gamma[r][m][q] = 0.5 * sum(
                    gi[r][s]
                    * (dg[m][s][q] + dg[q][s][m] - dg[s][m][q])
                    for s in range(n)
                )

    dgamma = [[[[0.0] * n for _ in range(n)] for __ in range(n)] for ___ in range(n)]
    for a in range(n):
        for r in range(n):
            for m in range(n):
                for q in range(n):
                    total = 0.0
                    for s in range(n):
                        first = dg[m][s][q] + dg[q][s][m] - dg[s][m][q]
                        second = (
                            ddg[a][m][s][q]
                            + ddg[a][q][s][m]
                            - ddg[a][s][m][q]
                        )
                        total += dgi[a][r][s] * first + gi[r][s] * second
                    dgamma[a][r][m][q] = 0.5 * total

    ricci = [[0.0] * n for _ in range(n)]
    for m in range(n):
        for q in range(n):
            ricci[m][q] = sum(
                dgamma[r][r][m][q] - dgamma[q][r][m][r]
                for r in range(n)
            ) + sum(
                gamma[r][r][s] * gamma[s][m][q]
                - gamma[r][q][s] * gamma[s][m][r]
                for r in range(n)
                for s in range(n)
            )

    scalar = sum(gi[m][q] * ricci[m][q] for m in range(n) for q in range(n))
    einstein = [
        [ricci[m][q] - 0.5 * g[m][q] * scalar for q in range(n)]
        for m in range(n)
    ]
    return scalar, ricci, einstein


def exponential_diagonal_4d(p, q):
    """Metric diag(-1,e^(2f1),e^(2f2),e^(2f3)) at t=x=0.

    f_i = p_i*x0 + q_i*x1. The returned arrays contain exact derivatives at origin.
    """
    n = 4
    g = [[0.0] * n for _ in range(n)]
    g[0][0] = -1.0
    for i in range(3):
        g[i + 1][i + 1] = 1.0

    dg = [[[0.0] * n for _ in range(n)] for __ in range(n)]
    ddg = [[[[0.0] * n for _ in range(n)] for __ in range(n)] for ___ in range(n)]
    for i in range(3):
        idx = i + 1
        coeff = [p[i], q[i], 0.0, 0.0]
        for a in range(n):
            dg[a][idx][idx] = 2.0 * coeff[a]
            for b in range(n):
                ddg[a][b][idx][idx] = 4.0 * coeff[a] * coeff[b]
    return g, dg, ddg


def exponential_diagonal_3d(q):
    n = 3
    h = [[0.0] * n for _ in range(n)]
    for i in range(3):
        h[i][i] = 1.0

    dh = [[[0.0] * n for _ in range(n)] for __ in range(n)]
    ddh = [[[[0.0] * n for _ in range(n)] for __ in range(n)] for ___ in range(n)]
    for i in range(3):
        coeff = [q[i], 0.0, 0.0]
        for a in range(n):
            dh[a][i][i] = 2.0 * coeff[a]
            for b in range(n):
                ddh[a][b][i][i] = 4.0 * coeff[a] * coeff[b]
    return h, dh, ddh


def test_static_flat_null_control():
    p = [0.0, 0.0, 0.0]
    q = [0.0, 0.0, 0.0]
    g, dg, ddg = exponential_diagonal_4d(p, q)
    _, _, G = curvature_at_point(g, dg, ddg)
    assert max(abs(x) for row in G for x in row) < 1e-13


def test_flat_isotropic_normal_normal_certificate():
    H = 0.27
    p = [H, H, H]
    q = [0.0, 0.0, 0.0]
    g, dg, ddg = exponential_diagonal_4d(p, q)
    _, _, G = curvature_at_point(g, dg, ddg)

    k_trace = -3.0 * H
    k2 = 3.0 * H * H
    geom_h = k_trace * k_trace - k2

    assert geom_h == pytest.approx(6.0 * H * H)
    assert 2.0 * G[0][0] == pytest.approx(geom_h, abs=1e-12)


def test_nonhomogeneous_direct_component_audit_fixes_both_projection_signs():
    # Nontrivial time and x dependence; N=1, shift=0 at the audit point.
    p = [0.2, -0.3, 0.5]
    q = [0.1, 0.4, -0.2]

    g, dg, ddg = exponential_diagonal_4d(p, q)
    _, _, G4 = curvature_at_point(g, dg, ddg)

    h, dh, ddh = exponential_diagonal_3d(q)
    R3, _, _ = curvature_at_point(h, dh, ddh)

    # RF-E9 convention: K^i_j = -p_i delta^i_j at the origin.
    K = -sum(p)
    KijKij = sum(x * x for x in p)
    geom_h = R3 + K * K - KijKij

    assert 2.0 * G4[0][0] == pytest.approx(geom_h, abs=1e-12)

    # For h_ii=e^(2 q_i x), direct spatial covariant differentiation gives
    # M_x = D_j K^j_x - D_x K = sum_j (p_j-p_x) q_j.
    geom_m_x = (p[1] - p[0]) * q[1] + (p[2] - p[0]) * q[2]

    # n^mu=(1,0,0,0), h_x^mu picks x; RF-E10 convention is M_i=-G_{n i}.
    assert -G4[0][1] == pytest.approx(geom_m_x, abs=1e-12)
    assert G4[0][1] == pytest.approx(-geom_m_x, abs=1e-12)


def test_projection_dimensions_are_inverse_length_squared_contract():
    # Scaling a length coordinate by L sends K -> K/L and R3 -> R3/L^2.
    L = 3.5
    K = 0.8
    R3 = -0.2
    K2 = 0.31
    original = R3 + K * K - K2
    scaled = R3 / (L * L) + (K / L) ** 2 - K2 / (L * L)
    assert scaled == pytest.approx(original / (L * L))
