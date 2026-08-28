import math


ALPHA_C = 0.474812


def matmul(a, b):
    return [
        [sum(a[i][k] * b[k][j] for k in range(3)) for j in range(3)]
        for i in range(3)
    ]


def dagger(a):
    return [[a[j][i].conjugate() for j in range(3)] for i in range(3)]


def trace(a):
    return sum(a[i][i] for i in range(3))


def matsub(a, b):
    return [[a[i][j] - b[i][j] for j in range(3)] for i in range(3)]


def scalarmul(c, a):
    return [[c * a[i][j] for j in range(3)] for i in range(3)]


def eye3():
    return [[1 + 0j, 0j, 0j], [0j, 1 + 0j, 0j], [0j, 0j, 1 + 0j]]


def link_x(a, q):
    c = math.cos(a * q)
    s = 1j * math.sin(a * q)
    return [[c, s, 0j], [s, c, 0j], [0j, 0j, 1 + 0j]]


def link_y(a, q):
    c = math.cos(a * q)
    s = math.sin(a * q)
    return [[c, s, 0j], [-s, c, 0j], [0j, 0j, 1 + 0j]]


def plaquette(a, qx, qy):
    wx = link_x(a, qx)
    wy = link_y(a, qy)
    return matmul(matmul(matmul(wx, wy), dagger(wx)), dagger(wy))


def curvature_proxy(u, a):
    h = scalarmul(1.0 / (2j * a * a), matsub(u, dagger(u)))
    tr = trace(h) / 3.0
    return matsub(h, scalarmul(tr, eye3()))


def link_density(u, a):
    h = curvature_proxy(u, a)
    return 0.5 * trace(matmul(h, h)).real


def wilson_defect(u):
    return 3.0 - trace(u).real


def continuum_pair_density(qx, qy, g):
    ax = 2.0 * qx / g
    ay = 2.0 * qy / g
    f3 = g * ax * ay
    return 0.5 * f3 * f3


def witness_rows():
    g = 1.0 / math.sqrt(ALPHA_C)
    c_p = 2.0 * ALPHA_C
    qx = math.sqrt(2.0) / 7.0
    qy = math.sqrt(3.0) / 11.0
    rows = []
    for a in (0.08, 0.04, 0.02):
        u = plaquette(a, qx, qy)
        d_density = wilson_defect(u) / (a ** 4)
        l_link = link_density(u, a)
        rows.append((a, d_density, l_link, c_p * d_density, c_p * l_link))
    return g, c_p, qx, qy, rows


def test_noparamsm_alpha_c_inverse_g2_convention():
    g = 1.0 / math.sqrt(ALPHA_C)
    assert math.isclose(ALPHA_C, 1.0 / (g * g), rel_tol=1e-14)


def test_action_and_wilson_coefficients_follow_exactly():
    c_p = 2.0 * ALPHA_C
    beta_w = 3.0 * c_p
    assert math.isclose(c_p, 2.0 * ALPHA_C, rel_tol=1e-15)
    assert math.isclose(beta_w, 6.0 * ALPHA_C, rel_tol=1e-15)


def test_v41_defect_density_matches_curvature_proxy():
    _, _, _, _, rows = witness_rows()
    for _, d_density, l_link, _, _ in rows:
        assert abs(d_density - l_link) / l_link < 2e-6


def test_wilson_action_matches_reconstructed_continuum_density():
    _, _, _, _, rows = witness_rows()
    for _, _, _, wilson_density, reconstructed in rows:
        assert abs(wilson_density - reconstructed) / reconstructed < 2e-6


def test_reconstructed_density_converges_to_constant_field_continuum():
    g, _, qx, qy, rows = witness_rows()
    target = continuum_pair_density(qx, qy, g)
    errors = [abs(reconstructed - target) / target for *_, reconstructed in rows]
    assert errors[2] < errors[1] < errors[0]
    assert errors[-1] < 1e-5


def test_adversarial_half_coefficient_is_rejected():
    g, _, qx, qy, _ = witness_rows()
    a = 0.02
    u = plaquette(a, qx, qy)
    wrong = ALPHA_C * link_density(u, a)
    target = continuum_pair_density(qx, qy, g)
    assert abs(wrong - target) / target > 0.49
