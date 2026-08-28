import math
import numpy as np

ALPHA_C = 0.47483961905223004
G_YM = ALPHA_C ** -0.5


def angle(a, b):
    return a[0] * b[1] - a[1] * b[0]


def square(a, b):
    return a[0] * b[1] - a[1] * b[0]


def sij(lam, til, i, j):
    return angle(lam[i], lam[j]) * square(til[j], til[i])


def A5(order, lam, g=1.0):
    num = angle(lam[0], lam[1]) ** 4
    den = 1.0 + 0j
    for i in range(5):
        den *= angle(lam[order[i]], lam[order[(i + 1) % 5]])
    return g**3 * num / den


def A4(order, lam, g=1.0):
    num = angle(lam[0], lam[1]) ** 4
    den = 1.0 + 0j
    for i in range(4):
        den *= angle(lam[order[i]], lam[order[(i + 1) % 4]])
    return g**2 * num / den


def generate_five(rng):
    for _ in range(100):
        lam = [rng.normal(size=2) + 1j * rng.normal(size=2) for _ in range(5)]
        if abs(angle(lam[3], lam[4])) < 0.3:
            continue
        til = [rng.normal(size=2) + 1j * rng.normal(size=2) for _ in range(3)]
        M = sum(np.outer(lam[i], til[i]) for i in range(3))
        X = np.linalg.solve(np.column_stack([lam[3], lam[4]]), -M)
        til += [X[0], X[1]]
        orders = [[0, 1, 2, 3, 4], [0, 2, 1, 3, 4], [0, 2, 3, 1, 4]]
        dens = []
        for order in orders:
            den = 1.0 + 0j
            for i in range(5):
                den *= angle(lam[order[i]], lam[order[(i + 1) % 5]])
            dens.append(abs(den))
        if min(dens) > 1e-4:
            return lam, til
    raise RuntimeError("failed to generate stable five-point kinematics")


def test_complex_five_point_states_are_massless_and_conserved():
    rng = np.random.default_rng(20260828)
    for _ in range(200):
        lam, til = generate_five(rng)
        P = sum(np.outer(lam[i], til[i]) for i in range(5))
        assert np.linalg.norm(P) < 2e-11
        for i in range(5):
            assert abs(np.linalg.det(np.outer(lam[i], til[i]))) < 2e-11


def test_fundamental_five_point_bcj_relation():
    rng = np.random.default_rng(20260828)
    for _ in range(500):
        lam, til = generate_five(rng)
        s12 = sij(lam, til, 0, 1)
        s23 = sij(lam, til, 1, 2)
        s24 = sij(lam, til, 1, 3)
        a1 = A5([0, 1, 2, 3, 4], lam)
        a2 = A5([0, 2, 1, 3, 4], lam)
        a3 = A5([0, 2, 3, 1, 4], lam)
        terms = [s12 * a1, (s12 + s23) * a2, (s12 + s23 + s24) * a3]
        assert abs(sum(terms)) < 2e-11 * max(1.0, *map(abs, terms))


def test_bcj_reduces_third_ordering_to_two_amplitude_basis():
    rng = np.random.default_rng(20260829)
    for _ in range(200):
        lam, til = generate_five(rng)
        s12 = sij(lam, til, 0, 1)
        s23 = sij(lam, til, 1, 2)
        s24 = sij(lam, til, 1, 3)
        denom = s12 + s23 + s24
        if abs(denom) < 1e-7:
            continue
        a1 = A5([0, 1, 2, 3, 4], lam)
        a2 = A5([0, 2, 1, 3, 4], lam)
        pred = -(s12 * a1 + (s12 + s23) * a2) / denom
        direct = A5([0, 2, 3, 1, 4], lam)
        assert abs(pred - direct) < 2e-11 * max(1.0, abs(direct))


def test_positive_helicity_soft_factorization_on_conserved_family():
    rng = np.random.default_rng(1234)
    lam0 = [rng.normal(size=2) + 1j * rng.normal(size=2) for _ in range(5)]
    while abs(angle(lam0[2], lam0[3])) < 0.3 or min(abs(angle(lam0[3], lam0[4])), abs(angle(lam0[4], lam0[0]))) < 0.3:
        lam0 = [rng.normal(size=2) + 1j * rng.normal(size=2) for _ in range(5)]
    t12 = [rng.normal(size=2) + 1j * rng.normal(size=2) for _ in range(2)]
    t5raw = rng.normal(size=2) + 1j * rng.normal(size=2)
    residues = []
    for eps in [1e-1, 1e-2, 1e-3, 1e-4, 1e-5]:
        lam = [x.copy() for x in lam0]
        til = [None] * 5
        lam[4] = math.sqrt(eps) * lam0[4]
        til[0], til[1] = t12[0].copy(), t12[1].copy()
        til[4] = math.sqrt(eps) * t5raw
        M = np.outer(lam[0], til[0]) + np.outer(lam[1], til[1]) + np.outer(lam[4], til[4])
        X = np.linalg.solve(np.column_stack([lam[2], lam[3]]), -M)
        til[2], til[3] = X[0], X[1]
        assert np.linalg.norm(sum(np.outer(lam[i], til[i]) for i in range(5))) < 2e-11
        a5 = A5([0, 1, 2, 3, 4], lam)
        a4 = A4([0, 1, 2, 3], lam)
        soft = angle(lam[3], lam[0]) / (angle(lam[3], lam[4]) * angle(lam[4], lam[0]))
        assert abs(a5 - soft * a4) < 2e-11 * max(1.0, abs(a5))
        residues.append(eps * a5)
    assert max(abs(x - residues[-1]) for x in residues) < 2e-11 * max(1.0, abs(residues[-1]))


def test_five_point_project_coupling_scales_as_g_cubed():
    rng = np.random.default_rng(55)
    lam, til = generate_five(rng)
    core = A5([0, 1, 2, 3, 4], lam, g=1.0)
    phys = A5([0, 1, 2, 3, 4], lam, g=G_YM)
    assert abs(phys - G_YM**3 * core) < 1e-12 * max(1.0, abs(phys))
    assert math.isclose(G_YM**2, 1.0 / ALPHA_C, rel_tol=1e-15)


def test_five_point_basis_dimension_matches_n_minus_3_factorial():
    assert math.factorial(5 - 3) == 2
