import math
from functools import lru_cache

import numpy as np

ETA = np.diag([1.0, -1.0, -1.0, -1.0])


def dot(a, b):
    return a @ ETA @ b


def generate_2to3(rng, energy=1.0):
    for _ in range(100):
        v3 = rng.normal(size=3)
        v4 = rng.normal(size=3)
        if np.linalg.norm(v3) < 1e-5 or np.linalg.norm(v4) < 1e-5:
            continue
        v5 = -(v3 + v4)
        if np.linalg.norm(v5) < 1e-5:
            continue
        scale = 2 * energy / (np.linalg.norm(v3) + np.linalg.norm(v4) + np.linalg.norm(v5))
        vs = [scale * v3, scale * v4, scale * v5]
        ps = [np.array([-energy, 0.0, 0.0, -energy]), np.array([-energy, 0.0, 0.0, energy])]
        ps += [np.r_[np.linalg.norm(v), v] for v in vs]
        if min(abs(dot(ps[i] + ps[j], ps[i] + ps[j])) for i in range(5) for j in range(i + 1, 5)) > 1e-5:
            return ps
    raise RuntimeError


def transverse_basis(p):
    n = p[1:] / np.linalg.norm(p[1:])
    ref = np.array([1.0, 0.0, 0.0])
    if abs(np.dot(n, ref)) > 0.9:
        ref = np.array([0.0, 1.0, 0.0])
    e1 = np.cross(n, ref)
    e1 /= np.linalg.norm(e1)
    e2 = np.cross(n, e1)
    e2 /= np.linalg.norm(e2)
    return np.r_[0.0, e1], np.r_[0.0, e2]


def polarizations(ps, rng):
    out = []
    for p in ps:
        e1, e2 = transverse_basis(p)
        a, b = rng.normal(size=2)
        out.append((a * e1 + b * e2) / math.sqrt(a * a + b * b))
    return out


def bg_amplitude(ps, es, quartic_scale=2.0, binary_scale=2.0):
    @lru_cache(None)
    def mom(seq):
        return sum((ps[i] for i in seq), np.zeros(4))

    @lru_cache(None)
    def cur(seq):
        if len(seq) == 1:
            return es[seq[0]].astype(float)
        return num(seq) / dot(mom(seq), mom(seq))

    @lru_cache(None)
    def num(seq):
        L = len(seq)
        out = np.zeros(4)
        for k in range(1, L):
            X, Y = seq[:k], seq[k:]
            JX, JY = cur(X), cur(Y)
            kX, kY = mom(X), mom(Y)
            jj = dot(JX, JY)
            out += binary_scale * (dot(kY, JX) * JY + 0.5 * kX * jj - dot(kX, JY) * JX - 0.5 * kY * jj)
        for i in range(1, L - 1):
            for j in range(i + 1, L):
                X, Y, Z = seq[:i], seq[i:j], seq[j:]
                JX, JY, JZ = cur(X), cur(Y), cur(Z)
                out += quartic_scale * (dot(JX, JZ) * JY - 0.5 * dot(JX, JY) * JZ - 0.5 * dot(JY, JZ) * JX)
        return out

    return dot(num(tuple(range(len(ps) - 1))), es[-1])


def A(ps, es, order, quartic_scale=2.0):
    return bg_amplitude([ps[i] for i in order], [es[i] for i in order], quartic_scale=quartic_scale, binary_scale=2.0)


def sij(ps, i, j):
    return 2 * dot(ps[i], ps[j])


def kernel(ps):
    s12, s13, s23 = sij(ps, 0, 1), sij(ps, 0, 2), sij(ps, 1, 2)
    return np.array([[s12 * (s13 + s23), s12 * s13], [s12 * s13, s13 * (s12 + s23)]], float)


def klt(ps, eL, eR, qL=2.0, qR=2.0):
    L = np.array([A(ps, eL, [0, 1, 2, 3, 4], qL), A(ps, eL, [0, 2, 1, 3, 4], qL)])
    R = np.array([A(ps, eR, [0, 1, 2, 4, 3], qR), A(ps, eR, [0, 2, 1, 4, 3], qR)])
    return L @ kernel(ps) @ R


def klt_two_term(ps, eL, eR):
    return -(sij(ps, 0, 1) * sij(ps, 2, 3) * A(ps, eL, [0, 1, 2, 3, 4]) * A(ps, eR, [1, 0, 3, 2, 4]) + sij(ps, 0, 2) * sij(ps, 1, 3) * A(ps, eL, [0, 2, 1, 3, 4]) * A(ps, eR, [2, 0, 3, 1, 4]))


def test_project_five_point_klt_matrix_matches_two_term_form():
    rng = np.random.default_rng(20260908)
    for _ in range(150):
        ps = generate_2to3(rng)
        eL = polarizations(ps, rng)
        eR = polarizations(ps, rng)
        x, y = klt(ps, eL, eR), klt_two_term(ps, eL, eR)
        assert abs(x - y) < 1.6e-10 * max(1.0, abs(x), abs(y))


def test_project_five_point_gravity_ward_identity_in_left_copy():
    rng = np.random.default_rng(20260909)
    for _ in range(100):
        ps = generate_2to3(rng)
        eL = polarizations(ps, rng)
        eR = polarizations(ps, rng)
        scale = max(1.0, abs(klt(ps, eL, eR)))
        for leg in range(5):
            x = [e.copy() for e in eL]
            x[leg] = ps[leg].copy()
            assert abs(klt(ps, x, eR)) < 4e-10 * scale


def test_project_five_point_gravity_ward_identity_in_right_copy():
    rng = np.random.default_rng(20260910)
    for _ in range(100):
        ps = generate_2to3(rng)
        eL = polarizations(ps, rng)
        eR = polarizations(ps, rng)
        scale = max(1.0, abs(klt(ps, eL, eR)))
        for leg in range(5):
            x = [e.copy() for e in eR]
            x[leg] = ps[leg].copy()
            assert abs(klt(ps, eL, x)) < 4e-10 * scale


def test_project_klt_is_copy_exchange_symmetric():
    rng = np.random.default_rng(20260911)
    for _ in range(120):
        ps = generate_2to3(rng)
        eL = polarizations(ps, rng)
        eR = polarizations(ps, rng)
        a, b = klt(ps, eL, eR), klt(ps, eR, eL)
        assert abs(a - b) < 6e-10 * max(1.0, abs(a), abs(b))


def test_quartic_contact_is_required_for_gravitational_ward_closure():
    rng = np.random.default_rng(20260912)
    witnessed = False
    for _ in range(20):
        ps = generate_2to3(rng)
        eL = polarizations(ps, rng)
        eR = polarizations(ps, rng)
        good, bad = [], []
        for leg in range(5):
            x = [e.copy() for e in eL]
            x[leg] = ps[leg].copy()
            good.append(abs(klt(ps, x, eR, 2.0, 2.0)))
            bad.append(abs(klt(ps, x, eR, 0.0, 2.0)))
        assert max(good) < 6e-9
        if max(bad) > 1e-3:
            witnessed = True
    assert witnessed


def test_project_five_point_gravity_prefactor_uses_kappa_over_four_cubed():
    for mbar in [0.8, 1.0, 2.0, 4.5]:
        kappa_g = 2 / mbar
        kappa_E = 1 / (mbar * mbar)
        pref = (kappa_g / 4) ** 3
        assert math.isclose(pref, 1 / (8 * mbar**3), rel_tol=1e-15)
        assert math.isclose(pref, kappa_E / (8 * mbar), rel_tol=1e-15)
