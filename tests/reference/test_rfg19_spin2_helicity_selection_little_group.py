import math
import numpy as np

ETA = np.diag([1.0, -1.0, -1.0, -1.0]).astype(complex)


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


def gravity_core(ps, es):
    n, d = project_numerators(ps, es)
    return sum(n[k] * n[k] / d[k] for k in ("s", "t", "u"))


def kinematics(theta, energy=1.0):
    s, c = math.sin(theta), math.cos(theta)
    return [
        np.array([energy, 0, 0, energy], complex),
        np.array([energy, 0, 0, -energy], complex),
        np.array([-energy, -energy * s, 0, -energy * c], complex),
        np.array([-energy, energy * s, 0, energy * c], complex),
    ]


def helicity_frame(p, psi=0.0):
    spatial = np.real(p[1:]).astype(float)
    n = spatial / np.linalg.norm(spatial)
    ref = np.array([0.0, 1.0, 0.0])
    if abs(np.dot(ref, n)) > 0.9:
        ref = np.array([1.0, 0.0, 0.0])
    u = ref - n * np.dot(ref, n)
    u /= np.linalg.norm(u)
    v = np.cross(n, u)
    v /= np.linalg.norm(v)
    ur = math.cos(psi) * u + math.sin(psi) * v
    vr = -math.sin(psi) * u + math.cos(psi) * v
    ep = np.concatenate([[0.0], (ur + 1j * vr) / math.sqrt(2.0)]).astype(complex)
    em = np.concatenate([[0.0], (ur - 1j * vr) / math.sqrt(2.0)]).astype(complex)
    return {+1: ep, -1: em}


def physical_helicity_vectors(ps, physical_helicities, psis=None):
    if psis is None:
        psis = [0.0] * 4
    out = []
    for i, (p, h, psi) in enumerate(zip(ps, physical_helicities, psis)):
        h_in = h if i < 2 else -h
        out.append(helicity_frame(p, psi)[h_in])
    return out


def amplitude(theta, physical_helicities, psis=None):
    ps = kinematics(theta)
    es = physical_helicity_vectors(ps, physical_helicities, psis)
    return gravity_core(ps, es)


def test_helicity_vectors_are_transverse_null_and_dual_normalized():
    for theta in np.linspace(0.3, 2.6, 17):
        for p in kinematics(float(theta)):
            frame = helicity_frame(p)
            ep, em = frame[+1], frame[-1]
            assert abs(dot(p, ep)) < 2e-14
            assert abs(dot(p, em)) < 2e-14
            assert abs(dot(ep, ep)) < 2e-14
            assert abs(dot(em, em)) < 2e-14
            assert abs(dot(ep, em) + 1.0) < 2e-14


def test_physical_all_plus_spin2_amplitude_vanishes():
    for theta in np.linspace(0.28, 2.72, 31):
        assert abs(amplitude(float(theta), (+1, +1, +1, +1))) < 2e-27


def test_all_physical_single_minus_spin2_amplitudes_vanish():
    for theta in np.linspace(0.32, 2.65, 23):
        for leg in range(4):
            hs = [+1, +1, +1, +1]
            hs[leg] = -1
            assert abs(amplitude(float(theta), tuple(hs))) < 3e-27


def test_mhv_spin2_sector_is_nonzero_and_parity_mirror_matches():
    for theta in np.linspace(0.35, 2.55, 19):
        a = amplitude(float(theta), (-1, -1, +1, +1))
        b = amplitude(float(theta), (+1, +1, -1, -1))
        assert abs(a) > 1e-3
        assert abs(a - b) < 2e-12 * max(1.0, abs(a), abs(b))


def test_external_frame_rotation_has_spin2_double_phase():
    theta = 1.1
    hs = (-1, -1, +1, +1)
    base = amplitude(theta, hs)
    for leg in range(4):
        h_in = hs[leg] if leg < 2 else -hs[leg]
        for psi in (0.2, -0.37, 0.71):
            psis = [0.0] * 4
            psis[leg] = psi
            ratio = amplitude(theta, hs, psis) / base
            expected = np.exp(-2j * h_in * psi)
            assert abs(ratio - expected) < 2e-14


def test_helicity_spin2_states_are_symmetric_transverse_and_traceless():
    for theta in np.linspace(0.3, 2.6, 13):
        ps = kinematics(float(theta))
        for p in ps:
            for e in helicity_frame(p).values():
                H = np.outer(e, e)
                assert np.linalg.norm(H - H.T) < 1e-14
                assert abs(np.sum(ETA * H)) < 2e-14
                assert np.linalg.norm(p @ ETA @ H) < 3e-14
                assert np.linalg.norm(H @ ETA @ p) < 3e-14
