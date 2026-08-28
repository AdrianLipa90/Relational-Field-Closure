import math
import numpy as np


ALPHA_C = 0.47483961905223004
G_YM = ALPHA_C ** -0.5


LAM = [
    np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]], complex),
    np.array([[0, -1j, 0], [1j, 0, 0], [0, 0, 0]], complex),
    np.array([[1, 0, 0], [0, -1, 0], [0, 0, 0]], complex),
    np.array([[0, 0, 1], [0, 0, 0], [1, 0, 0]], complex),
    np.array([[0, 0, -1j], [0, 0, 0], [1j, 0, 0]], complex),
    np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0]], complex),
    np.array([[0, 0, 0], [0, 0, -1j], [0, 1j, 0]], complex),
    np.array([[1, 0, 0], [0, 1, 0], [0, 0, -2]], complex) / math.sqrt(3),
]
T = [x / 2.0 for x in LAM]
FABC = np.zeros((8, 8, 8))
for a in range(8):
    for b in range(8):
        comm = T[a] @ T[b] - T[b] @ T[a]
        for c in range(8):
            FABC[a, b, c] = (-2j * np.trace(T[c] @ comm)).real


def field_matrix(coeff):
    return sum((float(x) * t for x, t in zip(coeff, T)), np.zeros((3, 3), complex))


def exp_i_hermitian(h):
    vals, vecs = np.linalg.eigh(h)
    return (vecs * np.exp(1j * vals)) @ vecs.conj().T


def f_matrix(cx, cy, sigma=1):
    ax = field_matrix(cx)
    ay = field_matrix(cy)
    return 1j * sigma * G_YM * (ax @ ay - ay @ ax)


def f_components(cx, cy, sigma=1):
    return np.array([
        -sigma * G_YM * sum(
            FABC[a, b, c] * cx[b] * cy[c]
            for b in range(8)
            for c in range(8)
        )
        for a in range(8)
    ])


def density_matrix(cx, cy, sigma=1):
    f = f_matrix(cx, cy, sigma)
    return np.trace(f @ f).real


def density_components(cx, cy, sigma=1):
    f = f_components(cx, cy, sigma)
    return 0.5 * np.dot(f, f)


def defect(cx, cy, a, sigma=1):
    ux = exp_i_hermitian(sigma * a * G_YM * field_matrix(cx))
    uy = exp_i_hermitian(sigma * a * G_YM * field_matrix(cy))
    p = ux @ uy @ ux.conj().T @ uy.conj().T
    return 3.0 - np.trace(p).real


def test_matrix_and_component_quartic_density_match_random():
    rng = np.random.default_rng(20260828)
    for _ in range(200):
        x = rng.normal(scale=0.2, size=8)
        y = rng.normal(scale=0.2, size=8)
        assert math.isclose(
            density_matrix(x, y),
            density_components(x, y),
            rel_tol=2e-13,
            abs_tol=2e-14,
        )


def test_orientation_sign_squares_out():
    x = np.array([0.2, 0.1, 0, 0.04, 0, 0.03, 0, 0.02])
    y = np.array([-0.03, 0.17, 0.08, 0, 0.02, 0, 0.05, -0.01])
    assert math.isclose(density_matrix(x, y, 1), density_matrix(x, y, -1), rel_tol=1e-15)


def test_field_scaling_is_quartic():
    x = np.array([0.2, 0.1, 0, 0.04, 0, 0.03, 0, 0.02])
    y = np.array([-0.03, 0.17, 0.08, 0, 0.02, 0, 0.05, -0.01])
    lam = 2.3
    assert math.isclose(
        density_matrix(lam * x, lam * y),
        lam ** 4 * density_matrix(x, y),
        rel_tol=2e-14,
    )


def test_coupling_scaling_is_g_squared_via_alpha():
    x = np.array([0.2, 0, 0, 0, 0, 0, 0, 0])
    y = np.array([0, 0.17, 0, 0, 0, 0, 0, 0])
    base = density_matrix(x, y)
    comm = 1j * (field_matrix(x) @ field_matrix(y) - field_matrix(y) @ field_matrix(x))
    unit = np.trace(comm @ comm).real
    assert math.isclose(base, G_YM ** 2 * unit, rel_tol=1e-14)


def test_wilson_cp_reconstructs_quartic_density_in_small_loop():
    x = np.array([0.2, 0, 0, 0, 0, 0, 0, 0])
    y = np.array([0, 0.17, 0, 0, 0, 0, 0, 0])
    target = density_matrix(x, y)
    c_p = 2.0 * ALPHA_C
    errors = []
    for a in [0.12, 0.08, 0.04, 0.02]:
        errors.append(abs(c_p * defect(x, y, a) / a ** 4 - target) / target)
    assert all(v < u for u, v in zip(errors, errors[1:]))
    assert errors[-1] < 5e-4


def test_wrong_cp_half_normalization_fails():
    x = np.array([0.2, 0, 0, 0, 0, 0, 0, 0])
    y = np.array([0, 0.17, 0, 0, 0, 0, 0, 0])
    target = density_matrix(x, y)
    a = 0.02
    right = 2.0 * ALPHA_C * defect(x, y, a) / a ** 4
    wrong = ALPHA_C * defect(x, y, a) / a ** 4
    assert abs(right - target) < abs(wrong - target) * 1e-3
