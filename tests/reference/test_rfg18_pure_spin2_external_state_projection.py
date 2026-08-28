import itertools
import math
import numpy as np

ETA = np.diag([1.0, -1.0, -1.0, -1.0])


def dot(a, b):
    return a @ ETA @ b


def decompose_transverse(M):
    S = 0.5 * (M + M.T)
    B = 0.5 * (M - M.T)
    phi = 0.5 * np.trace(S) * np.eye(2)
    h = S - phi
    return h, B, phi


def inner(A, B):
    return float(np.sum(A * B))


def basis_tensors():
    x = np.array([1.0, 0.0])
    y = np.array([0.0, 1.0])
    rt = math.sqrt(2.0)
    plus = (np.outer(x, x) - np.outer(y, y)) / rt
    cross = (np.outer(x, y) + np.outer(y, x)) / rt
    b = (np.outer(x, y) - np.outer(y, x)) / rt
    dil = (np.outer(x, x) + np.outer(y, y)) / rt
    return plus, cross, b, dil


def cubic_current(p, q, r, e1, e2):
    return dot(e1, e2) * (p - q) + e2 * dot(e1, q - r) + e1 * dot(e2, r - p)


def channel_exchange_numerator(ps, es, kind):
    p1, p2, p3, p4 = ps
    e1, e2, e3, e4 = es
    if kind == "s":
        k = p1 + p2
        jl = cubic_current(p1, p2, -k, e1, e2)
        jr = cubic_current(p3, p4, k, e3, e4)
    elif kind == "t":
        k = p1 + p3
        jl = cubic_current(p1, p3, -k, e1, e3)
        jr = cubic_current(p2, p4, k, e2, e4)
    else:
        k = p1 + p4
        jl = cubic_current(p1, p4, -k, e1, e4)
        jr = cubic_current(p2, p3, k, e2, e3)
    return dot(jl, jr), dot(k, k)


def contact_kinematic(es, kind):
    e1, e2, e3, e4 = es
    if kind == "s":
        return dot(e1, e3) * dot(e2, e4) - dot(e1, e4) * dot(e2, e3)
    if kind == "t":
        return dot(e1, e2) * dot(e3, e4) - dot(e1, e4) * dot(e2, e3)
    return dot(e1, e2) * dot(e3, e4) - dot(e1, e3) * dot(e2, e4)


def project_numerators(ps, es):
    n, d = {}, {}
    for kind in ("s", "t", "u"):
        x, den = channel_exchange_numerator(ps, es, kind)
        n[kind] = x + den * contact_kinematic(es, kind)
        d[kind] = den
    return n, d


def gravity_core(ps, ea, eb):
    na, d = project_numerators(ps, ea)
    nb, _ = project_numerators(ps, eb)
    return sum(na[k] * nb[k] / d[k] for k in ("s", "t", "u"))


def kinematics(theta, energy=1.0):
    s, c = math.sin(theta), math.cos(theta)
    ps = [
        np.array([energy, 0, 0, energy]),
        np.array([energy, 0, 0, -energy]),
        np.array([-energy, -energy * s, 0, -energy * c]),
        np.array([-energy, energy * s, 0, energy * c]),
    ]
    e_y = np.array([0.0, 0.0, 1.0, 0.0])
    e12 = np.array([0.0, 1.0, 0.0, 0.0])
    e34 = np.array([0.0, c, 0.0, -s])
    return ps, [(e12, e_y), (e12, e_y), (e34, e_y), (e34, e_y)]


def state_terms(kind, basis):
    x, y = basis
    rt = math.sqrt(2.0)
    if kind == "plus":
        return [(1 / rt, x, x), (-1 / rt, y, y)]
    if kind == "cross":
        return [(1 / rt, x, y), (1 / rt, y, x)]
    if kind == "dilaton":
        return [(1 / rt, x, x), (1 / rt, y, y)]
    if kind == "B":
        return [(1 / rt, x, y), (-1 / rt, y, x)]
    raise ValueError(kind)


def tensor_amplitude(ps, termlists):
    total = 0.0
    for combo in itertools.product(*termlists):
        coeff = np.prod([t[0] for t in combo])
        ea = [t[1] for t in combo]
        eb = [t[2] for t in combo]
        total += coeff * gravity_core(ps, ea, eb)
    return total


def test_random_transverse_tensor_decomposition_is_exact_and_orthogonal():
    rng = np.random.default_rng(20260902)
    for _ in range(1000):
        M = rng.normal(size=(2, 2))
        h, b, phi = decompose_transverse(M)
        assert np.linalg.norm(M - (h + b + phi)) < 1e-14
        assert abs(np.trace(h)) < 1e-14
        assert np.linalg.norm(h - h.T) < 1e-14
        assert np.linalg.norm(b + b.T) < 1e-14
        assert abs(inner(h, b)) < 1e-14
        assert abs(inner(h, phi)) < 1e-14
        assert abs(inner(b, phi)) < 1e-14


def test_plus_cross_B_dilaton_form_orthonormal_transverse_basis():
    ts = basis_tensors()
    gram = np.array([[inner(a, b) for b in ts] for a in ts])
    assert np.linalg.norm(gram - np.eye(4)) < 1e-14


def test_spin2_projector_is_idempotent_and_removes_complementary_sectors():
    plus, cross, b, dil = basis_tensors()
    for h0 in (plus, cross):
        h, bb, phi = decompose_transverse(h0)
        assert np.linalg.norm(h - h0) < 1e-14
        assert np.linalg.norm(bb) < 1e-14
        assert np.linalg.norm(phi) < 1e-14
    for m in (b, dil):
        h, _, _ = decompose_transverse(m)
        assert np.linalg.norm(h) < 1e-14


def test_factorized_self_copy_state_contains_spin2_and_trace_components():
    x = np.array([1.0, 0.0])
    M = np.outer(x, x)
    h, b, phi = decompose_transverse(M)
    assert np.linalg.norm(b) < 1e-14
    assert math.isclose(np.linalg.norm(h), 1 / math.sqrt(2), rel_tol=1e-15)
    assert math.isclose(np.linalg.norm(phi), 1 / math.sqrt(2), rel_tol=1e-15)


def test_lifted_spin2_polarizations_are_transverse_symmetric_and_traceless():
    for theta in np.linspace(0.3, 2.6, 21):
        ps, bases = kinematics(float(theta))
        for p, (x, y) in zip(ps, bases):
            for terms in (state_terms("plus", (x, y)), state_terms("cross", (x, y))):
                H = sum(c * np.outer(a, b) for c, a, b in terms)
                assert np.linalg.norm(H - H.T) < 1e-14
                assert abs(np.sum(ETA * H)) < 1e-14
                assert np.linalg.norm(p @ ETA @ H) < 2e-14
                assert np.linalg.norm(H @ ETA @ p) < 2e-14


def test_projected_spin2_four_point_amplitude_obeys_linearized_diffeomorphism_ward_gate():
    for theta in (0.4, 0.9, 1.5, 2.2):
        ps, bases = kinematics(theta)
        states = [state_terms("plus", b) for b in bases]
        base = tensor_amplitude(ps, states)
        assert abs(base) > 1e-3
        for leg in range(4):
            xi = bases[leg][0]
            gauge = [(1.0, ps[leg], xi), (1.0, xi, ps[leg])]
            trial = list(states)
            trial[leg] = gauge
            assert abs(tensor_amplitude(ps, trial)) < 3e-13 * max(1.0, abs(base))
