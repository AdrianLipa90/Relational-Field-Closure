from __future__ import annotations

import math
from typing import Sequence

SOURCE_REPOSITORY = "AdrianLipa90/Relational-Field-Closure"
SOURCE_COMMIT = "85bbb1d0754605be2720b6bd258b486b0a072345"
SOURCE_PATH = "tests/reference/test_rfe10_gauss_codazzi_projections.py"
STATUS = "CANDIDATE_EXTRACTED_FROM_REFERENCE_TEST_NOT_CANONICAL_PROVIDER"


def inv_matrix(a: Sequence[Sequence[float]]):
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

    Provenance-exact algorithm extracted from RFC reference test at SOURCE_COMMIT.
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
    for i in range(3): h[i][i] = 1.0
    dh = [[[0.0] * n for _ in range(n)] for __ in range(n)]
    ddh = [[[[0.0] * n for _ in range(n)] for __ in range(n)] for ___ in range(n)]
    for i in range(3):
        coeff = [q[i], 0.0, 0.0]
        for a in range(n):
            dh[a][i][i] = 2.0 * coeff[a]
            for b in range(n): ddh[a][b][i][i] = 4.0 * coeff[a] * coeff[b]
    return h, dh, ddh
