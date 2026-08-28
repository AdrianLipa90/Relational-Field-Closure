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


def exp_i_hermitian(h):
    vals, vecs = np.linalg.eigh(h)
    return (vecs * np.exp(1j * vals)) @ vecs.conj().T


def principal_hermitian_log(u):
    vals, vecs = np.linalg.eig(u)
    h = vecs @ np.diag(np.angle(vals)) @ np.linalg.inv(vecs)
    return (h + h.conj().T) / 2.0


def link_component(amplitude, a, color):
    return exp_i_hermitian(a * G_YM * amplitude * T[color])


def recover_component(u, a, color):
    return (np.trace(LAM[color] @ (principal_hermitian_log(u) / a)) / G_YM).real


def plaquette(u, v):
    return u @ v @ u.conj().T @ v.conj().T


def recover_f_components(p, a):
    f = principal_hermitian_log(p) / (G_YM * a * a)
    f -= np.trace(f) / 3.0 * np.eye(3)
    f = (f + f.conj().T) / 2.0
    return np.array([np.trace(lam @ f).real for lam in LAM])


def fields(n=128, m1=5, m2=7, a1=0.15, a2=0.12):
    idx = np.arange(n)
    return (
        a1 * np.cos(2.0 * np.pi * m1 * idx / n),
        a2 * np.cos(2.0 * np.pi * m2 * idx / n),
    )


def make(n=128, a=0.04):
    a1, a2 = fields(n)
    u = [link_component(x, a, 0) for x in a1]
    v = [link_component(x, a, 1) for x in a2]
    return a1, a2, u, v


def test_two_noncommuting_input_fields_recover_from_links():
    a1, a2, u, v = make()
    r1 = np.array([recover_component(link, 0.04, 0) for link in u])
    r2 = np.array([recover_component(link, 0.04, 1) for link in v])
    assert np.max(np.abs(r1 - a1)) < 3e-13
    assert np.max(np.abs(r2 - a2)) < 3e-13
    assert np.linalg.norm(T[0] @ T[1] - T[1] @ T[0]) > 0.0


def test_interaction_curvature_color3_converges_to_oriented_commutator():
    a1, a2, _, _ = make()
    target = -G_YM * a1 * a2
    errors = []
    for a in [0.08, 0.04, 0.02, 0.01]:
        _, _, u, v = make(a=a)
        f3 = np.array([recover_f_components(plaquette(x, y), a)[2] for x, y in zip(u, v)])
        errors.append(np.linalg.norm(f3 - target) / np.linalg.norm(target))
    assert all(y < x for x, y in zip(errors, errors[1:]))
    assert errors[-1] < 2e-4


def test_output_momentum_is_sum_and_difference_convolution():
    _, _, u, v = make(a=0.02)
    f3 = np.array([recover_f_components(plaquette(x, y), 0.02)[2] for x, y in zip(u, v)])
    magnitude = np.abs(np.fft.rfft(f3))
    magnitude[0] = 0.0
    assert set(np.argsort(magnitude)[-2:]) == {2, 12}


def test_analytic_product_has_same_output_modes():
    a1, a2, _, _ = make()
    target = -G_YM * a1 * a2
    magnitude = np.abs(np.fft.rfft(target))
    magnitude[0] = 0.0
    assert set(np.argsort(magnitude)[-2:]) == {2, 12}


def test_wrong_commutator_sign_is_falsified():
    a1, a2, u, v = make(a=0.01)
    f3 = np.array([recover_f_components(plaquette(x, y), 0.01)[2] for x, y in zip(u, v)])
    right = -G_YM * a1 * a2
    wrong = G_YM * a1 * a2
    assert np.linalg.norm(f3 - right) < np.linalg.norm(f3 - wrong) * 1e-3


def test_subleading_colors_vanish_in_continuum():
    ratios = []
    for a in [0.08, 0.04, 0.02, 0.01]:
        _, _, u, v = make(a=a)
        fc = np.array([recover_f_components(plaquette(x, y), a) for x, y in zip(u, v)])
        main = np.linalg.norm(fc[:, 2])
        side = np.linalg.norm(np.delete(fc, 2, axis=1))
        ratios.append(side / main)
    assert all(y < x for x, y in zip(ratios, ratios[1:]))
    assert ratios[-1] < 3e-3
