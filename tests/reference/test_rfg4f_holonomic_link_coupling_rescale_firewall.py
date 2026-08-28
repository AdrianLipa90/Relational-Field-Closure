import math


def q_from_gA(g, A):
    return 0.5 * g * A


def A_from_qg(q, g):
    if g <= 0:
        raise ValueError("positive coupling required")
    return 2.0 * q / g


def test_generator_basis_half_factor():
    g, A = 1.4, 0.7
    q = q_from_gA(g, A)
    assert math.isclose(q, 0.49, rel_tol=1e-15)
    assert math.isclose(g * A, 2.0 * q, rel_tol=1e-15)


def test_link_rescaling_degeneracy():
    g, A = 1.3, 0.8
    lam = 3.7
    assert math.isclose(q_from_gA(g, A), q_from_gA(lam * g, A / lam), rel_tol=1e-15)


def test_alpha_c_continuum_binding_gives_field_map():
    alpha = 0.47483961905223004
    g = alpha**-0.5
    q = 0.21
    A = A_from_qg(q, g)
    assert math.isclose(q, q_from_gA(g, A), rel_tol=1e-15)
    assert math.isclose(A, 2.0 * q * math.sqrt(alpha), rel_tol=1e-15)


def test_naive_q_equals_A_forces_g_equal_two():
    q = 0.37
    A = q
    g = 2.0 * q / A
    assert math.isclose(g, 2.0, rel_tol=1e-15)


def test_link_coordinate_cannot_select_unique_g():
    q = 0.25
    for g in (0.7, 1.1, 2.3, 5.0):
        A = A_from_qg(q, g)
        assert math.isclose(q_from_gA(g, A), q, rel_tol=1e-15)
