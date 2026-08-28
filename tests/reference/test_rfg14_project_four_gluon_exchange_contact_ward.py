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
    return (
        dot(e1, e2) * (p - q)
        + e2 * dot(e1, q - r)
        + e1 * dot(e2, r - p)
    )


def color_factor(cols, kind):
    a, b, c, d = cols
    if kind == "s":
        return sum(FABC[a, b, e] * FABC[c, d, e] for e in range(8))
    if kind == "t":
        return sum(FABC[a, c, e] * FABC[b, d, e] for e in range(8))
    return sum(FABC[a, d, e] * FABC[b, c, e] for e in range(8))


def exchange(ps, es, cols, kind):
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
    return color_factor(cols, kind) * dot(jl, jr) / dot(k, k)


def contact(es, cols):
    e1, e2, e3, e4 = es
    c1 = color_factor(cols, "s")
    c2 = color_factor(cols, "t")
    c3 = color_factor(cols, "u")
    return (
        c1 * (dot(e1, e3) * dot(e2, e4) - dot(e1, e4) * dot(e2, e3))
        + c2 * (dot(e1, e2) * dot(e3, e4) - dot(e1, e4) * dot(e2, e3))
        + c3 * (dot(e1, e2) * dot(e3, e4) - dot(e1, e3) * dot(e2, e4))
    )


def amplitude(ps, es, cols, g=G_YM, contact_sign=1.0, sigma_link=1):
    # Every exchange graph contains two oriented cubic factors (-sigma_link*g),
    # so the common exchange factor is g^2. The quartic contact is orientation-even.
    return g * g * (
        sum(exchange(ps, es, cols, kind) for kind in ("s", "t", "u"))
        + contact_sign * contact(es, cols)
    )


def kinematics(theta, energy=1.0):
    s = math.sin(theta)
    c = math.cos(theta)
    ps = [
        np.array([energy, 0, 0, energy]),
        np.array([energy, 0, 0, -energy]),
        np.array([-energy, -energy * s, 0, -energy * c]),
        np.array([-energy, energy * s, 0, energy * c]),
    ]
    e_y = np.array([0.0, 0.0, 1.0, 0.0])
    e_plane_12 = np.array([0.0, 1.0, 0.0, 0.0])
    e_plane_34 = np.array([0.0, c, 0.0, -s])
    return ps, e_y, e_plane_12, e_plane_34


def polarizations(theta, weights):
    ps, e_y, e12, e34 = kinematics(theta)
    es = []
    for w, basis in zip(weights, [e12, e12, e34, e34]):
        es.append((e_y + w * basis) / math.sqrt(1.0 + w * w))
    return ps, es


COLORS = [(0, 1, 0, 1), (0, 1, 1, 0), (0, 3, 0, 3)]


def test_external_states_are_on_shell_transverse_and_conserved():
    for theta in np.linspace(0.35, 2.5, 12):
        ps, es = polarizations(float(theta), [0.3, -0.4, 0.5, -0.2])
        assert np.linalg.norm(sum(ps)) < 1e-14
        for p, e in zip(ps, es):
            assert abs(dot(p, p)) < 2e-14
            assert abs(dot(p, e)) < 2e-14


def test_full_exchange_plus_contact_satisfies_four_leg_ward_identity():
    rng = np.random.default_rng(20260828)
    for _ in range(80):
        theta = float(rng.uniform(0.25, 2.75))
        weights = rng.uniform(-0.9, 0.9, size=4)
        ps, es = polarizations(theta, weights)
        for cols in COLORS:
            scale = max(1.0, abs(amplitude(ps, es, cols)))
            for leg in range(4):
                replaced = [x.copy() for x in es]
                replaced[leg] = ps[leg].copy()
                assert abs(amplitude(ps, replaced, cols)) < 2e-11 * scale


def test_contact_term_is_required_for_ward_cancellation():
    ps, es = polarizations(0.7, [0.3, -0.4, 0.5, -0.2])
    cols = (0, 1, 0, 1)
    residuals_full = []
    residuals_wrong = []
    for leg in range(4):
        replaced = [x.copy() for x in es]
        replaced[leg] = ps[leg].copy()
        residuals_full.append(abs(amplitude(ps, replaced, cols, contact_sign=1.0)))
        residuals_wrong.append(abs(amplitude(ps, replaced, cols, contact_sign=-1.0)))
    assert max(residuals_full) < 1e-12
    assert max(residuals_wrong) > 0.5


def test_physical_amplitude_is_nonzero_for_witness():
    ps, es = polarizations(0.7, [0.3, -0.4, 0.5, -0.2])
    assert abs(amplitude(ps, es, (0, 1, 0, 1))) > 1e-3


def test_amplitude_scales_as_g_squared_and_alpha_inverse():
    ps, es = polarizations(1.1, [0.1, 0.2, -0.3, 0.4])
    cols = (0, 1, 1, 0)
    base = amplitude(ps, es, cols, g=1.0)
    scaled = amplitude(ps, es, cols, g=G_YM)
    assert abs(scaled - G_YM * G_YM * base) < 1e-12 * max(1.0, abs(scaled))
    assert math.isclose(G_YM * G_YM, 1.0 / ALPHA_C, rel_tol=1e-15)


def test_link_orientation_sign_squares_out_of_four_point_amplitude():
    ps, es = polarizations(1.3, [0.2, -0.1, 0.4, -0.5])
    cols = (0, 3, 0, 3)
    assert math.isclose(
        amplitude(ps, es, cols, sigma_link=1),
        amplitude(ps, es, cols, sigma_link=-1),
        rel_tol=1e-15,
        abs_tol=1e-15,
    )
