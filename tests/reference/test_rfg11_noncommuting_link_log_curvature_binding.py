import math
import numpy as np


ALPHA_C = 0.47483961905223004
G_YM = ALPHA_C ** -0.5


def gell_mann():
    return [
        np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]], complex),
        np.array([[0, -1j, 0], [1j, 0, 0], [0, 0, 0]], complex),
        np.array([[1, 0, 0], [0, -1, 0], [0, 0, 0]], complex),
        np.array([[0, 0, 1], [0, 0, 0], [1, 0, 0]], complex),
        np.array([[0, 0, -1j], [0, 0, 0], [1j, 0, 0]], complex),
        np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0]], complex),
        np.array([[0, 0, 0], [0, 0, -1j], [0, 1j, 0]], complex),
        np.array([[1, 0, 0], [0, 1, 0], [0, 0, -2]], complex) / math.sqrt(3),
    ]


LAM = gell_mann()
T = [x / 2.0 for x in LAM]


def field_matrix(coeff):
    return sum((float(c) * t for c, t in zip(coeff, T)), np.zeros((3, 3), complex))


def exp_i_hermitian(h):
    vals, vecs = np.linalg.eigh(h)
    return (vecs * np.exp(1j * vals)) @ vecs.conj().T


def principal_hermitian_log(u):
    vals, vecs = np.linalg.eig(u)
    phases = np.angle(vals)
    h = vecs @ np.diag(phases) @ np.linalg.inv(vecs)
    return (h + h.conj().T) / 2.0


def make_link(coeff, a):
    return exp_i_hermitian(a * G_YM * field_matrix(coeff))


def recover_coeff(u, a):
    q = principal_hermitian_log(u) / a
    q -= np.trace(q) / 3.0 * np.eye(3)
    return np.array([(np.trace(lam @ q) / G_YM).real for lam in LAM])


def principal_admissible(coeff, a, margin=1e-10):
    phases = np.linalg.eigvalsh(a * G_YM * field_matrix(coeff))
    return np.max(np.abs(phases)) < math.pi - margin


def plaquette(cx, cy, a):
    ux = make_link(cx, a)
    uy = make_link(cy, a)
    return ux @ uy @ ux.conj().T @ uy.conj().T


def recover_f(u_plaq, a):
    h = principal_hermitian_log(u_plaq)
    f = h / (G_YM * a * a)
    f -= np.trace(f) / 3.0 * np.eye(3)
    return (f + f.conj().T) / 2.0


def commutator_f_plus_link(cx, cy):
    ax = field_matrix(cx)
    ay = field_matrix(cy)
    return 1j * G_YM * (ax @ ay - ay @ ax)


def test_generator_orthogonality():
    gram = np.array([[np.trace(a @ b).real for b in LAM] for a in LAM])
    assert np.allclose(gram, 2.0 * np.eye(8), atol=1e-14, rtol=0.0)


def test_full_eight_component_principal_log_recovery():
    rng = np.random.default_rng(20260828)
    for _ in range(100):
        coeff = rng.normal(scale=0.12, size=8)
        a = 0.07
        assert principal_admissible(coeff, a)
        recovered = recover_coeff(make_link(coeff, a), a)
        assert np.max(np.abs(recovered - coeff)) < 3e-13


def test_noncommuting_lambda1_lambda2_recovery():
    coeff = np.array([0.21, -0.17, 0, 0, 0, 0, 0, 0], float)
    a = 0.09
    recovered = recover_coeff(make_link(coeff, a), a)
    assert np.max(np.abs(recovered - coeff)) < 3e-13
    assert np.linalg.norm(T[0] @ T[1] - T[1] @ T[0]) > 0.0


def test_constant_noncommuting_plaquette_recovers_oriented_commutator_curvature():
    cx = np.array([0.23, 0, 0, 0, 0, 0, 0, 0], float)
    cy = np.array([0, 0.19, 0, 0, 0, 0, 0, 0], float)
    exact = commutator_f_plus_link(cx, cy)
    errors = []
    for a in [0.08, 0.04, 0.02, 0.01]:
        errors.append(np.linalg.norm(recover_f(plaquette(cx, cy, a), a) - exact))
    assert all(y < x for x, y in zip(errors, errors[1:]))
    assert errors[-1] < 2e-4


def test_matrix_log_field_is_gauge_covariant():
    coeff = np.array([0.17, -0.11, 0.05, 0.08, 0, 0.03, -0.07, 0.02])
    a = 0.05
    u = make_link(coeff, a)
    h = field_matrix(np.array([0.07, 0.03, -0.04, 0, 0.02, 0, 0.01, -0.05]))
    v = exp_i_hermitian(h)
    ug = v @ u @ v.conj().T
    q = principal_hermitian_log(u) / a
    qg = principal_hermitian_log(ug) / a
    assert np.linalg.norm(qg - v @ q @ v.conj().T) < 3e-12


def test_principal_branch_firewall_detects_alias_risk():
    coeff = np.zeros(8)
    coeff[2] = 5.0
    assert not principal_admissible(coeff, 1.0)
