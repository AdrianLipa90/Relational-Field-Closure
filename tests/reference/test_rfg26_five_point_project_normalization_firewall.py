import math
from functools import lru_cache

import numpy as np

ETA = np.diag([1.0, -1.0, -1.0, -1.0]).astype(complex)


def dot(a, b):
    return a @ ETA @ b


def br(a, b):
    return a[0] * b[1] - a[1] * b[0]


def vec(M):
    return np.array([
        (M[0, 0] + M[1, 1]) / 2,
        (M[0, 1] + M[1, 0]) / 2,
        (M[1, 0] - M[0, 1]) / (2j),
        (M[0, 0] - M[1, 1]) / 2,
    ], complex)


def point(rng, n):
    for _ in range(1000):
        lam = [rng.normal(size=2) + 1j * rng.normal(size=2) for _ in range(n)]
        m = n - 2
        if abs(np.linalg.det(np.column_stack([lam[m], lam[m + 1]]))) < 0.2:
            continue
        til = [rng.normal(size=2) + 1j * rng.normal(size=2) for _ in range(m)]
        rhs = sum(np.outer(lam[i], til[i]) for i in range(m))
        x = np.linalg.solve(np.column_stack([lam[m], lam[m + 1]]), -rhs)
        til += [x[0], x[1]]
        ps = [vec(np.outer(lam[i], til[i])) for i in range(n)]
        if np.linalg.norm(sum(ps)) < 2e-10:
            return lam, til, ps
    raise RuntimeError


def ep(lam, til, i, r):
    return vec(np.sqrt(2) * np.outer(lam[r], til[i]) / br(lam[r], lam[i]))


def em(lam, til, i, r):
    return -vec(np.sqrt(2) * np.outer(lam[i], til[r]) / br(til[i], til[r]))


def hel(lam, til):
    if len(lam) == 4:
        return [em(lam, til, 0, 2), em(lam, til, 1, 3),
                ep(lam, til, 2, 0), ep(lam, til, 3, 1)]
    return [em(lam, til, 0, 2), em(lam, til, 1, 3),
            ep(lam, til, 2, 0), ep(lam, til, 3, 1), ep(lam, til, 4, 0)]


def cubic(p, q, r, a, b):
    return dot(a, b) * (p - q) + b * dot(a, q - r) + a * dot(b, r - p)


def rfg15(ps, es):
    p1, p2, p3, p4 = ps
    e1, e2, e3, e4 = es

    def ex(ch):
        if ch == "s":
            q = p1 + p2
            jl, jr = cubic(p1, p2, -q, e1, e2), cubic(p3, p4, q, e3, e4)
        elif ch == "u":
            q = p1 + p4
            jl, jr = cubic(p1, p4, -q, e1, e4), cubic(p2, p3, q, e2, e3)
        return dot(jl, jr), dot(q, q)

    def ct(ch):
        if ch == "s":
            return dot(e1, e3) * dot(e2, e4) - dot(e1, e4) * dot(e2, e3)
        return dot(e1, e2) * dot(e3, e4) - dot(e1, e3) * dot(e2, e4)

    xs, s = ex("s")
    xu, u = ex("u")
    return (xs + s * ct("s")) / s - (xu + u * ct("u")) / u


def bg(ps, es, bscale, qscale):
    n = len(ps)

    @lru_cache(None)
    def mom(seq):
        return sum((ps[i] for i in seq), np.zeros(4, complex))

    @lru_cache(None)
    def cur(seq):
        if len(seq) == 1:
            return es[seq[0]].astype(complex)
        return num(seq) / dot(mom(seq), mom(seq))

    @lru_cache(None)
    def num(seq):
        out = np.zeros(4, complex)
        for k in range(1, len(seq)):
            X, Y = seq[:k], seq[k:]
            a, b = cur(X), cur(Y)
            kx, ky = mom(X), mom(Y)
            ab = dot(a, b)
            out += bscale * (dot(ky, a) * b + 0.5 * kx * ab
                             - dot(kx, b) * a - 0.5 * ky * ab)
        for i in range(1, len(seq) - 1):
            for j in range(i + 1, len(seq)):
                a, b, c = cur(seq[:i]), cur(seq[i:j]), cur(seq[j:])
                out += qscale * (dot(a, c) * b - 0.5 * dot(a, b) * c
                                 - 0.5 * dot(b, c) * a)
        return out

    return dot(num(tuple(range(n - 1))), es[-1])


def ordered(ps, es, order, bscale, qscale):
    return bg([ps[i] for i in order], [es[i] for i in order], bscale, qscale)


def s(ps, i, j):
    return 2 * dot(ps[i], ps[j])


def klt(ps, left, right, bscale, qscale):
    L = np.array([ordered(ps, left, [0, 1, 2, 3, 4], bscale, qscale),
                  ordered(ps, left, [0, 2, 1, 3, 4], bscale, qscale)])
    R = np.array([ordered(ps, right, [0, 1, 2, 4, 3], bscale, qscale),
                  ordered(ps, right, [0, 2, 1, 4, 3], bscale, qscale)])
    s12, s13, s23 = s(ps, 0, 1), s(ps, 0, 2), s(ps, 1, 2)
    S = np.array([[s12 * (s13 + s23), s12 * s13],
                  [s12 * s13, s13 * (s12 + s23)]], complex)
    return L @ S @ R


def test_base_bg_is_half_rfg15_at_four_points():
    rng = np.random.default_rng(20260913)
    for _ in range(60):
        la, ti, ps = point(rng, 4)
        es = hel(la, ti)
        assert abs(bg(ps, es, math.sqrt(2), 1) - 0.5 * rfg15(ps, es)) < 3e-10


def test_project_bg_matches_rfg15_at_four_points():
    rng = np.random.default_rng(20260914)
    for _ in range(60):
        la, ti, ps = point(rng, 4)
        es = hel(la, ti)
        assert abs(bg(ps, es, 2, 2) - rfg15(ps, es)) < 3e-10


def test_tree_rescaling_is_two_and_two_sqrt_two():
    rng = np.random.default_rng(20260915)
    for _ in range(40):
        la, ti, ps = point(rng, 4)
        es = hel(la, ti)
        assert abs(bg(ps, es, 2, 2) - 2 * bg(ps, es, math.sqrt(2), 1)) < 3e-10
        la, ti, ps = point(rng, 5)
        es = hel(la, ti)
        assert abs(bg(ps, es, 2, 2) - 2 * math.sqrt(2) * bg(ps, es, math.sqrt(2), 1)) < 1e-8


def test_five_point_klt_core_rescales_by_eight():
    rng = np.random.default_rng(20260916)
    for _ in range(30):
        la, ti, ps = point(rng, 5)
        L = hel(la, ti)
        R = [em(la, ti, 0, 3), em(la, ti, 1, 4),
             ep(la, ti, 2, 1), ep(la, ti, 3, 0), ep(la, ti, 4, 1)]
        assert abs(klt(ps, L, R, 2, 2) - 8 * klt(ps, L, R, math.sqrt(2), 1)) < 2e-8


def test_kappa_over_four_cubed_compensates_factor_eight():
    for kg in [0.17, 0.4, 0.93, 1.7]:
        assert math.isclose((kg / 2) ** 3 / (kg / 4) ** 3, 8.0, rel_tol=1e-15)


def test_reduced_scale_form():
    for mbar in [0.8, 1.0, 2.0, 4.5]:
        kg = 2 / mbar
        kE = 1 / mbar**2
        pref = (kg / 4) ** 3
        assert math.isclose(pref, 1 / (8 * mbar**3), rel_tol=1e-15)
        assert math.isclose(pref, kE / (8 * mbar), rel_tol=1e-15)
