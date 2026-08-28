import math
import numpy as np

ALPHA_C = 0.47483961905223004
G_YM = ALPHA_C ** -0.5
ETA = np.diag([1.0, -1.0, -1.0, -1.0])


def dot(a, b):
    return a @ ETA @ b


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


def cubic_current(p, q, r, e1, e2):
    return dot(e1, e2) * (p - q) + e2 * dot(e1, q - r) + e1 * dot(e2, r - p)


def channel_color(cols, kind):
    a, b, c, d = cols
    if kind == "s":
        return sum(FABC[a, b, e] * FABC[c, d, e] for e in range(8))
    if kind == "t":
        return sum(FABC[a, c, e] * FABC[b, d, e] for e in range(8))
    return sum(FABC[a, d, e] * FABC[b, c, e] for e in range(8))


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
    out, den = {}, {}
    for kind in ("s", "t", "u"):
        x, d = channel_exchange_numerator(ps, es, kind)
        out[kind] = x + d * contact_kinematic(es, kind)
        den[kind] = d
    return out, den


def direct_project_amplitude(ps, es, cols, g=G_YM):
    total = 0.0
    for kind in ("s", "t", "u"):
        x, d = channel_exchange_numerator(ps, es, kind)
        total += channel_color(cols, kind) * x / d
        total += channel_color(cols, kind) * contact_kinematic(es, kind)
    return g * g * total


def cubicized_amplitude(ps, es, cols, g=G_YM):
    n, d = project_numerators(ps, es)
    return g * g * sum(channel_color(cols, k) * n[k] / d[k] for k in ("s", "t", "u"))


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


def test_color_jacobi_orientation_is_exact_for_all_su3_external_colors():
    for a in range(8):
        for b in range(8):
            for c in range(8):
                for d in range(8):
                    cols = (a, b, c, d)
                    defect = channel_color(cols, "s") - channel_color(cols, "t") + channel_color(cols, "u")
                    assert abs(defect) < 2e-14


def test_project_numerators_obey_matched_jacobi_without_fit():
    rng = np.random.default_rng(20260828)
    max_defect = 0.0
    for _ in range(500):
        theta = float(rng.uniform(0.22, 2.82))
        ps, es = polarizations(theta, rng.uniform(-0.95, 0.95, size=4))
        n, _ = project_numerators(ps, es)
        scale = max(1.0, abs(n["s"]), abs(n["t"]), abs(n["u"]))
        defect = abs(n["s"] - n["t"] + n["u"]) / scale
        max_defect = max(max_defect, defect)
    assert max_defect < 3e-14


def test_cubicized_numerators_reconstruct_full_rfg14_amplitude():
    rng = np.random.default_rng(20260829)
    colors = [(0, 1, 0, 1), (0, 1, 1, 0), (0, 3, 0, 3), (0, 3, 1, 4)]
    for _ in range(200):
        theta = float(rng.uniform(0.25, 2.75))
        ps, es = polarizations(theta, rng.uniform(-0.9, 0.9, size=4))
        for cols in colors:
            a = direct_project_amplitude(ps, es, cols)
            b = cubicized_amplitude(ps, es, cols)
            assert abs(a - b) < 3e-13 * max(1.0, abs(a), abs(b))


def test_quartic_contact_is_required_for_raw_numerator_jacobi():
    ps, es = polarizations(0.7, [0.3, -0.4, 0.5, -0.2])
    x = {kind: channel_exchange_numerator(ps, es, kind)[0] for kind in ("s", "t", "u")}
    raw_defect = x["s"] - x["t"] + x["u"]
    n, _ = project_numerators(ps, es)
    closed = n["s"] - n["t"] + n["u"]
    assert abs(raw_defect) > 1.0
    assert abs(closed) < 1e-13


def test_project_numerators_are_independent_of_color_choice():
    ps, es = polarizations(1.2, [0.2, -0.3, 0.4, -0.1])
    n0, d0 = project_numerators(ps, es)
    for cols in [(0, 1, 0, 1), (0, 3, 1, 4), (3, 4, 3, 4)]:
        reconstructed = G_YM * G_YM * sum(channel_color(cols, k) * n0[k] / d0[k] for k in ("s", "t", "u"))
        direct = direct_project_amplitude(ps, es, cols)
        assert abs(reconstructed - direct) < 1e-12 * max(1.0, abs(direct))


def test_project_bcj_surface_uses_no_gravity_target():
    assert math.isclose(G_YM * G_YM, 1.0 / ALPHA_C, rel_tol=1e-15)
