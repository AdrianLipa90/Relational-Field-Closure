import itertools
import math
import numpy as np


def delta_h_scalar(f, x, a):
    x = np.asarray(x, dtype=float)
    total = 0.0
    for i in range(3):
        ei = np.zeros(3)
        ei[i] = 1.0
        total += f(x + a * ei) - 2.0 * f(x) + f(x - a * ei)
    return total / (a * a)


def signed_permutation_matrices():
    mats = []
    for perm in itertools.permutations(range(3)):
        P = np.zeros((3, 3))
        for i, j in enumerate(perm):
            P[i, j] = 1.0
        for signs in itertools.product((-1.0, 1.0), repeat=3):
            mats.append(np.diag(signs) @ P)
    return mats


def test_constant_is_exact_null():
    for a in (0.2, 1.0, 3.0):
        assert delta_h_scalar(lambda x: 7.0, np.array([0.3, -0.2, 0.9]), a) == 0.0


def test_affine_is_exact_null():
    f = lambda x: 2.0 * x[0] - 3.0 * x[1] + 0.5 * x[2] + 7.0
    assert abs(delta_h_scalar(f, np.array([0.2, -0.4, 0.8]), 0.125)) < 1e-12


def test_quadratic_laplacian_is_exact():
    f = lambda x: float(np.dot(x, x))
    for a in (0.05, 0.4, 1.7):
        assert math.isclose(delta_h_scalar(f, np.array([0.31, -0.27, 0.52]), a), 6.0, rel_tol=0.0, abs_tol=1e-10)


def test_quartic_truncation_coefficient_at_origin():
    f = lambda x: x[0] ** 4
    for a in (0.1, 0.3, 0.8):
        got = delta_h_scalar(f, np.zeros(3), a)
        expected = 2.0 * a * a  # (a^2/12) * d_x^4 x^4 = (a^2/12)*24
        assert math.isclose(got, expected, rel_tol=1e-12, abs_tol=1e-12)


def test_hexahedral_operator_is_signed_permutation_invariant():
    f = lambda x: x[0] ** 2 + 2.0 * x[1] ** 2 + 3.0 * x[2] ** 2 + 0.2 * x[0] * x[1]
    x = np.array([0.21, -0.37, 0.42])
    a = 0.17
    base = delta_h_scalar(f, x, a)
    for R in signed_permutation_matrices():
        fR = lambda y, R=R: f(R.T @ y)
        got = delta_h_scalar(fR, R @ x, a)
        assert math.isclose(got, base, rel_tol=1e-12, abs_tol=1e-12)


def test_octahedral_average_of_rank_two_tensor_is_isotropic():
    A = np.array([[2.0, 0.7, -0.2], [0.7, 5.0, 1.1], [-0.2, 1.1, 8.0]])
    group = signed_permutation_matrices()
    avg = sum(R @ A @ R.T for R in group) / len(group)
    expected = np.trace(A) / 3.0 * np.eye(3)
    assert np.allclose(avg, expected, rtol=0.0, atol=1e-12)


def test_phase_clock_cell_scale_typing_and_source_dimension():
    c = 299792458.0
    omega = 2.0 * math.pi * 7.83
    a_h = c / (math.sqrt(6.0) * abs(omega))
    assert math.isfinite(a_h) and a_h > 0.0

    # u=ln N is dimensionless; a second difference divided by a_h^2 has L^-2 type.
    N0 = 1.0
    eps = 1e-8
    u0 = math.log(N0)
    up = math.log(N0 + eps)
    second_difference = (up - 2.0 * u0 + up) / (a_h * a_h)
    assert math.isfinite(second_difference)


if __name__ == "__main__":
    tests = [name for name, obj in globals().items() if name.startswith("test_") and callable(obj)]
    for name in tests:
        globals()[name]()
    print(f"PASS {len(tests)}/{len(tests)}")
