import math

# Dimension vectors are (M, L, T).
MASS = (1, 0, 0)
LENGTH = (0, 1, 0)
TIME = (0, 0, 1)


def add_dim(a, b):
    return tuple(x + y for x, y in zip(a, b))


def scale_dim(a, p):
    return tuple(p * x for x in a)


def test_lambda_to_energy_density_dimensions_close():
    lambda_dim = scale_dim(LENGTH, -2)
    c4_dim = (0, 4, -4)
    g_dim = (-1, 3, -2)
    u_dim = tuple(lambda_dim[i] + c4_dim[i] - g_dim[i] for i in range(3))
    assert u_dim == (1, -1, -2)


def test_support_volume_closes_to_energy():
    u_dim = (1, -1, -2)
    volume_dim = (0, 3, 0)
    energy_dim = add_dim(u_dim, volume_dim)
    assert energy_dim == (1, 2, -2)


def partition(E, tau):
    c_h = math.cos(tau / 2.0) ** 2
    d_h = math.sin(tau / 2.0) ** 2
    return c_h, d_h, E * c_h, E * d_h


def test_half_angle_partition_closes_energy():
    for tau in (0.0, 0.2, math.pi / 2.0, 2.4, math.pi, -0.8):
        E = 3.7
        c_h, d_h, j_c, j_d = partition(E, tau)
        assert math.isclose(c_h + d_h, 1.0, rel_tol=2e-15, abs_tol=2e-15)
        assert math.isclose(j_c + j_d, E, rel_tol=2e-15, abs_tol=2e-15)


def test_channel_imbalance_is_cosine_projection():
    for tau in (0.0, 0.3, math.pi / 2.0, 2.0, math.pi, -1.2):
        E = 2.9
        c_h, d_h, j_c, j_d = partition(E, tau)
        assert math.isclose(c_h - d_h, math.cos(tau), rel_tol=2e-15, abs_tol=2e-15)
        assert math.isclose(j_c - j_d, E * math.cos(tau), rel_tol=2e-15, abs_tol=2e-15)


def test_oriented_complex_magnitude_closes_to_source_energy():
    for tau in (0.0, 0.7, math.pi / 2.0, math.pi, -0.7):
        E = 4.1
        real = E * math.cos(tau)
        imag = E * math.sin(tau)
        assert math.isclose(math.hypot(real, imag), abs(E), rel_tol=2e-15, abs_tol=2e-15)


def test_orientation_reversal_preserves_real_and_flips_quadrature():
    E = 5.2
    tau = 0.83
    real_pos = E * math.cos(tau)
    imag_pos = E * math.sin(tau)
    real_neg = E * math.cos(-tau)
    imag_neg = E * math.sin(-tau)
    assert math.isclose(real_pos, real_neg, rel_tol=2e-15, abs_tol=2e-15)
    assert math.isclose(imag_pos, -imag_neg, rel_tol=2e-15, abs_tol=2e-15)


def test_quarter_turn_keeps_orientation_when_partition_is_degenerate():
    E = 1.0
    tau = math.pi / 2.0
    c_h, d_h, j_c, j_d = partition(E, tau)
    assert math.isclose(j_c, j_d, rel_tol=2e-15, abs_tol=2e-15)
    assert E * math.sin(tau) > 0.0


if __name__ == "__main__":
    tests = [name for name, obj in globals().items() if name.startswith("test_") and callable(obj)]
    for name in tests:
        globals()[name]()
    print(f"PASS {len(tests)}/{len(tests)}")
