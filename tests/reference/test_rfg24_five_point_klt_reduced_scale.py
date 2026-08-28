import math
import numpy as np


def angle(a, b):
    return a[0] * b[1] - a[1] * b[0]


def square(a, b):
    return a[0] * b[1] - a[1] * b[0]


def sij(lam, til, i, j):
    return angle(lam[i], lam[j]) * square(til[j], til[i])


def generate_five(rng):
    for _ in range(100):
        lam = [rng.normal(size=2) + 1j * rng.normal(size=2) for _ in range(5)]
        if abs(angle(lam[3], lam[4])) < 0.2:
            continue
        til = [rng.normal(size=2) + 1j * rng.normal(size=2) for _ in range(3)]
        M = sum(np.outer(lam[i], til[i]) for i in range(3))
        X = np.linalg.solve(np.column_stack([lam[3], lam[4]]), -M)
        til += [X[0], X[1]]
        return lam, til
    raise RuntimeError("failed to generate stable five-point kinematics")


def A5(order, lam, neg=(0, 1)):
    num = angle(lam[neg[0]], lam[neg[1]]) ** 4
    den = 1.0 + 0j
    for i in range(5):
        den *= angle(lam[order[i]], lam[order[(i + 1) % 5]])
    return num / den


def kernel(lam, til):
    s12 = sij(lam, til, 0, 1)
    s13 = sij(lam, til, 0, 2)
    s23 = sij(lam, til, 1, 2)
    return np.array(
        [
            [s12 * (s13 + s23), s12 * s13],
            [s12 * s13, s13 * (s12 + s23)],
        ],
        complex,
    )


def core(lam, til, negL=(0, 1), negR=(0, 1)):
    left = np.array(
        [A5([0, 1, 2, 3, 4], lam, negL), A5([0, 2, 1, 3, 4], lam, negL)]
    )
    right = np.array(
        [A5([0, 1, 2, 4, 3], lam, negR), A5([0, 2, 1, 4, 3], lam, negR)]
    )
    return left @ kernel(lam, til) @ right


def test_klt_kernel_is_symmetric_and_has_factorization_determinant():
    rng = np.random.default_rng(20260830)
    for _ in range(300):
        lam, til = generate_five(rng)
        S = kernel(lam, til)
        assert np.linalg.norm(S - S.T) < 1e-13
        s12 = sij(lam, til, 0, 1)
        s13 = sij(lam, til, 0, 2)
        s23 = sij(lam, til, 1, 2)
        rhs = s12 * s13 * s23 * (s12 + s13 + s23)
        assert abs(np.linalg.det(S) - rhs) < 2e-11 * max(1.0, abs(rhs))


def test_matrix_klt_matches_two_term_five_point_relation():
    rng = np.random.default_rng(20260831)
    for negR in [(0, 1), (0, 2), (1, 3)]:
        for _ in range(150):
            lam, til = generate_five(rng)
            matrix_form = core(lam, til, (0, 1), negR)
            s12 = sij(lam, til, 0, 1)
            s13 = sij(lam, til, 0, 2)
            two_term = -(
                s12
                * sij(lam, til, 2, 3)
                * A5([0, 1, 2, 3, 4], lam, (0, 1))
                * A5([1, 0, 3, 2, 4], lam, negR)
                + s13
                * sij(lam, til, 1, 3)
                * A5([0, 2, 1, 3, 4], lam, (0, 1))
                * A5([2, 0, 3, 1, 4], lam, negR)
            )
            assert abs(matrix_form - two_term) < 3e-11 * max(
                1.0, abs(matrix_form), abs(two_term)
            )


def test_klt_bilinear_is_symmetric_under_copy_exchange():
    rng = np.random.default_rng(20260901)
    for _ in range(200):
        lam, til = generate_five(rng)
        S = kernel(lam, til)
        left = np.array(
            [A5([0, 1, 2, 3, 4], lam, (0, 1)), A5([0, 2, 1, 3, 4], lam, (0, 1))]
        )
        right = np.array(
            [A5([0, 1, 2, 4, 3], lam, (0, 2)), A5([0, 2, 1, 4, 3], lam, (0, 2))]
        )
        assert abs(left @ S @ right - right @ S @ left) < 2e-11 * max(
            1.0, abs(left @ S @ right)
        )


def test_pure_spin2_little_group_weight_is_doubled():
    lam, til = generate_five(np.random.default_rng(7))
    base = core(lam, til)
    z = 1.37
    for leg, h in [(0, -2), (2, 2)]:
        l2 = [x.copy() for x in lam]
        t2 = [x.copy() for x in til]
        l2[leg] *= z
        t2[leg] /= z
        ratio = core(l2, t2) / base
        expected = z ** (-2 * h)
        assert abs(ratio - expected) < 2e-11 * max(1.0, abs(expected))


def test_five_point_gravity_prefactor_extends_reduced_scale_holonomy():
    for mbar in [0.7, 1.0, 2.3, 10.0]:
        kappa_g = 2.0 / mbar
        kappa_E = 1.0 / (mbar * mbar)
        prefactor = (kappa_g / 2.0) ** 3
        assert math.isclose(prefactor, 1.0 / mbar**3, rel_tol=1e-15)
        assert math.isclose(prefactor, kappa_E / mbar, rel_tol=1e-15)


def test_horizon_and_local_carrier_forms_of_five_point_prefactor():
    alpha = 0.47483961905223004
    for gamma, omega in [(0.9, 1.4), (1.2, 0.8), (2.0, 3.1)]:
        mbar = alpha * omega / (2.0 * gamma)
        mhth = mbar * mbar
        p1 = 1.0 / mbar**3
        p2 = 1.0 / (mhth**1.5)
        p3 = (2.0 * gamma / (alpha * omega)) ** 3
        assert math.isclose(p1, p2, rel_tol=1e-14)
        assert math.isclose(p1, p3, rel_tol=1e-14)
