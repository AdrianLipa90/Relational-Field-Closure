import numpy as np


SEED = 20260828


def bracket(a, b):
    return a[0] * b[1] - a[1] * b[0]


def make_point(rng):
    while True:
        lam = [rng.normal(size=2) + 1j * rng.normal(size=2) for _ in range(4)]
        matrix = np.column_stack([lam[2], lam[3]])
        if abs(np.linalg.det(matrix)) < 0.2:
            continue

        tilde = [rng.normal(size=2) + 1j * rng.normal(size=2) for _ in range(2)]
        t3 = np.empty(2, dtype=complex)
        t4 = np.empty(2, dtype=complex)
        for dotted in range(2):
            rhs = -(lam[0] * tilde[0][dotted] + lam[1] * tilde[1][dotted])
            sol = np.linalg.solve(matrix, rhs)
            t3[dotted], t4[dotted] = sol
        tilde.extend([t3, t4])

        def angle(i, j):
            return bracket(lam[i], lam[j])

        denominators = [
            angle(0, 1), angle(1, 2), angle(2, 3), angle(3, 0),
            angle(0, 2), angle(2, 1), angle(1, 3),
        ]
        if min(abs(x) for x in denominators) < 0.05:
            continue
        return lam, tilde


def amplitude(lam, order, g=1.0):
    def angle(i, j):
        return bracket(lam[i], lam[j])

    product = 1.0 + 0.0j
    for i, j in zip(order, order[1:] + order[:1]):
        product *= angle(i, j)
    return 1j * g * g * angle(0, 1) ** 4 / product


def sij(lam, tilde, i, j):
    return bracket(lam[i], lam[j]) * bracket(tilde[j], tilde[i])


def test_momentum_conservation_and_massless_spinors():
    rng = np.random.default_rng(SEED)
    for _ in range(100):
        lam, tilde = make_point(rng)
        total = sum(np.outer(lam[i], tilde[i]) for i in range(4))
        assert np.max(np.abs(total)) < 2e-12
        for i in range(4):
            assert abs(np.linalg.det(np.outer(lam[i], tilde[i]))) < 2e-12


def test_four_point_bcj_relation_mhv_random_complex():
    rng = np.random.default_rng(SEED + 1)
    for _ in range(250):
        lam, tilde = make_point(rng)
        a_1234 = amplitude(lam, [0, 1, 2, 3])
        a_1324 = amplitude(lam, [0, 2, 1, 3])
        lhs = sij(lam, tilde, 0, 1) * a_1234
        rhs = sij(lam, tilde, 0, 2) * a_1324
        rel = abs(lhs - rhs) / max(1.0, abs(lhs), abs(rhs))
        assert rel < 2e-11


def test_mandelstam_closure():
    rng = np.random.default_rng(SEED + 2)
    for _ in range(100):
        lam, tilde = make_point(rng)
        total = (
            sij(lam, tilde, 0, 1)
            + sij(lam, tilde, 0, 2)
            + sij(lam, tilde, 0, 3)
        )
        assert abs(total) < 2e-10


def test_bcj_gauge_numerators_exist_and_reconstruct_second_ordering():
    rng = np.random.default_rng(SEED + 3)
    for _ in range(200):
        lam, tilde = make_point(rng)
        a_1 = amplitude(lam, [0, 1, 2, 3])
        a_2 = amplitude(lam, [0, 2, 1, 3])
        s = sij(lam, tilde, 0, 1)
        u = sij(lam, tilde, 0, 2)
        n_s = s * a_1
        n_t = 0.0j
        n_u = -n_s
        assert abs(n_s + n_t + n_u) < 1e-12
        reconstructed = -n_u / u
        rel = abs(reconstructed - a_2) / max(1.0, abs(a_2))
        assert rel < 2e-11


def test_rfg8_coupling_scales_amplitude_and_numerators_as_g2():
    rng = np.random.default_rng(SEED + 4)
    lam, tilde = make_point(rng)
    alpha_c = 0.47483961905223004
    g = alpha_c ** -0.5
    a_0 = amplitude(lam, [0, 1, 2, 3], g=1.0)
    a_g = amplitude(lam, [0, 1, 2, 3], g=g)
    assert abs(a_g - g * g * a_0) < 1e-11 * max(1.0, abs(a_g))
    s = sij(lam, tilde, 0, 1)
    assert abs(s * a_g - g * g * (s * a_0)) < 1e-11 * max(1.0, abs(s * a_g))
