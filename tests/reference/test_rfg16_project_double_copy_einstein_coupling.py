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


def gravity_core(ps, es_a, es_b):
    na, d = project_numerators(ps, es_a)
    nb, _ = project_numerators(ps, es_b)
    return sum(na[k] * nb[k] / d[k] for k in ("s", "t", "u"))


def gravity_amplitude(ps, es_a, es_b, kappa_g):
    return -1j * (kappa_g / 4.0) ** 2 * gravity_core(ps, es_a, es_b)


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
    return ps, e_y, e12, e34


def polarizations(theta, weights):
    ps, e_y, e12, e34 = kinematics(theta)
    es = []
    for w, basis in zip(weights, [e12, e12, e34, e34]):
        es.append((e_y + w * basis) / math.sqrt(1.0 + w * w))
    return ps, es


def test_both_project_copies_obey_matched_jacobi():
    rng = np.random.default_rng(20260830)
    for _ in range(300):
        theta = float(rng.uniform(0.23, 2.80))
        ps, ea = polarizations(theta, rng.uniform(-0.9, 0.9, 4))
        _, eb = polarizations(theta, rng.uniform(-0.9, 0.9, 4))
        for es in (ea, eb):
            n, _ = project_numerators(ps, es)
            scale = max(1.0, abs(n["s"]), abs(n["t"]), abs(n["u"]))
            assert abs(n["s"] - n["t"] + n["u"]) < 3e-14 * scale


def test_double_copy_is_symmetric_under_exchange_of_kinematic_copies():
    rng = np.random.default_rng(20260831)
    for _ in range(150):
        theta = float(rng.uniform(0.25, 2.75))
        ps, ea = polarizations(theta, rng.uniform(-0.8, 0.8, 4))
        _, eb = polarizations(theta, rng.uniform(-0.8, 0.8, 4))
        a = gravity_core(ps, ea, eb)
        b = gravity_core(ps, eb, ea)
        assert abs(a - b) < 2e-14 * max(1.0, abs(a), abs(b))


def test_gravitational_ward_identity_in_either_copy():
    rng = np.random.default_rng(20260901)
    max_defect = 0.0
    for _ in range(180):
        theta = float(rng.uniform(0.27, 2.70))
        ps, ea = polarizations(theta, rng.uniform(-0.85, 0.85, 4))
        _, eb = polarizations(theta, rng.uniform(-0.85, 0.85, 4))
        base = gravity_core(ps, ea, eb)
        scale = max(1.0, abs(base))
        for left, right in ((ea, eb), (eb, ea)):
            for leg in range(4):
                repl = [x.copy() for x in left]
                repl[leg] = ps[leg].copy()
                val = gravity_core(ps, repl, right)
                max_defect = max(max_defect, abs(val) / scale)
    assert max_defect < 3e-13


def test_project_double_copy_is_nonzero_on_physical_witness():
    ps, ea = polarizations(0.73, [0.3, -0.4, 0.5, -0.2])
    _, eb = polarizations(0.73, [-0.2, 0.1, 0.4, -0.3])
    assert abs(gravity_core(ps, ea, eb)) > 1e-3


def test_physical_einstein_coupling_and_project_core_prefactor_are_distinct():
    for kappa_g in (0.1, 0.37, 1.0, 2.4):
        G = kappa_g * kappa_g / (32.0 * math.pi)
        kappa_e = 8.0 * math.pi * G
        mbar = 2.0 / kappa_g
        assert math.isclose(kappa_g * kappa_g / 4.0, kappa_e, rel_tol=2e-15)
        assert math.isclose((kappa_g / 4.0) ** 2, kappa_e / 4.0, rel_tol=2e-15)
        assert math.isclose(kappa_e, 1.0 / (mbar * mbar), rel_tol=2e-15)
        assert math.isclose(G, 1.0 / (8.0 * math.pi * mbar * mbar), rel_tol=2e-15)


def test_gravity_amplitude_uses_corrected_project_normalized_prefactor():
    ps, ea = polarizations(1.1, [0.1, 0.2, -0.3, 0.4])
    _, eb = polarizations(1.1, [0.2, -0.4, 0.1, 0.3])
    core = gravity_core(ps, ea, eb)
    for kappa_g in (0.3, 0.7, 1.4):
        amp = gravity_amplitude(ps, ea, eb, kappa_g)
        kappa_e = kappa_g * kappa_g / 4.0
        assert abs(amp - (-1j) * (kappa_e / 4.0) * core) < 2e-15 * max(1.0, abs(amp), abs(core))
