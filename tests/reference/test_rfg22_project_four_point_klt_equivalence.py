import math
import numpy as np

ETA = np.diag([1.0, -1.0, -1.0, -1.0])


def dot(a, b):
    return a @ ETA @ b


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


def partials(n, d):
    a1234 = n["s"] / d["s"] - n["u"] / d["u"]
    a1324 = n["t"] / d["t"] + n["u"] / d["u"]
    return a1234, a1324


def gravity_core(na, nb, d):
    return sum(na[k] * nb[k] / d[k] for k in ("s", "t", "u"))


def kinematics(theta, energy=1.0):
    s, c = math.sin(theta), math.cos(theta)
    ps = [
        np.array([energy, 0, 0, energy]),
        np.array([energy, 0, 0, -energy]),
        np.array([-energy, -energy * s, 0, -energy * c]),
        np.array([-energy, energy * s, 0, energy * c]),
    ]
    ey = np.array([0.0, 0.0, 1.0, 0.0])
    e12 = np.array([0.0, 1.0, 0.0, 0.0])
    e34 = np.array([0.0, c, 0.0, -s])
    return ps, ey, e12, e34


def polarizations(theta, weights):
    ps, ey, e12, e34 = kinematics(theta)
    es = []
    for w, b in zip(weights, [e12, e12, e34, e34]):
        es.append((ey + w * b) / math.sqrt(1.0 + w * w))
    return ps, es


def test_mandelstam_closure_on_project_kinematics():
    for theta in np.linspace(0.25, 2.75, 51):
        ps, es = polarizations(float(theta), [0.1, -0.2, 0.3, -0.4])
        _, d = project_numerators(ps, es)
        assert abs(d["s"] + d["t"] + d["u"]) < 2e-14


def test_project_partial_amplitudes_obey_four_point_bcj_relation():
    rng = np.random.default_rng(20260903)
    for _ in range(500):
        theta = float(rng.uniform(0.23, 2.78))
        ps, es = polarizations(theta, rng.uniform(-0.9, 0.9, 4))
        n, d = project_numerators(ps, es)
        a1, a2 = partials(n, d)
        lhs = d["s"] * a1
        rhs = d["t"] * a2
        assert abs(lhs - rhs) < 3e-13 * max(1.0, abs(lhs), abs(rhs))


def test_project_klt_equals_direct_double_copy_core_for_independent_copies():
    rng = np.random.default_rng(20260904)
    for _ in range(500):
        theta = float(rng.uniform(0.24, 2.77))
        ps, ea = polarizations(theta, rng.uniform(-0.9, 0.9, 4))
        _, eb = polarizations(theta, rng.uniform(-0.9, 0.9, 4))
        na, d = project_numerators(ps, ea)
        nb, _ = project_numerators(ps, eb)
        a1234, _ = partials(na, d)
        _, b1324 = partials(nb, d)
        direct = gravity_core(na, nb, d)
        klt = -d["u"] * a1234 * b1324
        assert abs(direct - klt) < 5e-13 * max(1.0, abs(direct), abs(klt))


def test_klt_relation_is_symmetric_under_copy_exchange_using_bcj():
    rng = np.random.default_rng(20260905)
    for _ in range(250):
        theta = float(rng.uniform(0.28, 2.70))
        ps, ea = polarizations(theta, rng.uniform(-0.8, 0.8, 4))
        _, eb = polarizations(theta, rng.uniform(-0.8, 0.8, 4))
        na, d = project_numerators(ps, ea)
        nb, _ = project_numerators(ps, eb)
        a1, a2 = partials(na, d)
        b1, b2 = partials(nb, d)
        left = -d["u"] * a1 * b2
        right = -d["u"] * b1 * a2
        assert abs(left - right) < 5e-13 * max(1.0, abs(left), abs(right))


def test_color_ordered_project_partial_is_gauge_invariant():
    rng = np.random.default_rng(20260906)
    for _ in range(120):
        theta = float(rng.uniform(0.3, 2.65))
        ps, es = polarizations(theta, rng.uniform(-0.75, 0.75, 4))
        n, d = project_numerators(ps, es)
        base, _ = partials(n, d)
        scale = max(1.0, abs(base))
        for leg in range(4):
            repl = [x.copy() for x in es]
            repl[leg] = ps[leg].copy()
            nr, _ = project_numerators(ps, repl)
            ar, _ = partials(nr, d)
            assert abs(ar) < 3e-13 * scale


def test_corrected_full_amplitude_prefactor_is_kappa_e_over_four():
    ps, ea = polarizations(1.1, [0.2, -0.3, 0.4, -0.1])
    _, eb = polarizations(1.1, [-0.4, 0.1, 0.3, -0.2])
    na, d = project_numerators(ps, ea)
    nb, _ = project_numerators(ps, eb)
    a1, _ = partials(na, d)
    _, b2 = partials(nb, d)
    core = gravity_core(na, nb, d)
    kg = 0.7
    kappa_e = kg * kg / 4.0
    direct = -1j * (kappa_e / 4.0) * core
    klt = 1j * (kappa_e / 4.0) * d["u"] * a1 * b2
    assert abs(direct - klt) < 2e-14 * max(1.0, abs(direct), abs(klt))
