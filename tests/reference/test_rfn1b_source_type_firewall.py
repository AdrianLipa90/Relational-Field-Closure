import math

# Dimension vectors are (M, L, T).
MASS = (1, 0, 0)
LENGTH = (0, 1, 0)
TIME = (0, 0, 1)
DIMLESS = (0, 0, 0)


def add_dim(a, b):
    return tuple(x + y for x, y in zip(a, b))


def scale_dim(a, p):
    return tuple(p * x for x in a)


def sub_dim(a, b):
    return tuple(x - y for x, y in zip(a, b))


def test_information_curvature_has_source_type():
    xi_dim = scale_dim(LENGTH, -2)
    source_dim = scale_dim(LENGTH, -2)
    assert xi_dim == source_dim


def test_phase_energy_is_not_mass_density_type():
    energy_dim = add_dim(MASS, add_dim(scale_dim(LENGTH, 2), scale_dim(TIME, -2)))
    rho_m_dim = add_dim(MASS, scale_dim(LENGTH, -3))
    assert energy_dim != rho_m_dim


def test_energy_over_volume_over_c2_has_mass_density_type():
    energy_dim = (1, 2, -2)
    volume_dim = (0, 3, 0)
    c2_dim = (0, 2, -2)
    got = sub_dim(sub_dim(energy_dim, volume_dim), c2_dim)
    assert got == (1, -3, 0)


def test_conditional_phase_cell_density_formula():
    hbar = 1.054571817e-34
    c = 299792458.0
    omega = 2.0 * math.pi * 7.83
    n_e = 0.37
    a_h = c / (math.sqrt(6.0) * omega)
    E = hbar * omega
    direct = n_e * E / (c * c * a_h**3)
    reduced = 6.0 * math.sqrt(6.0) * n_e * hbar * omega**4 / c**5
    assert math.isclose(direct, reduced, rel_tol=2e-15, abs_tol=0.0)


def test_candidate_G_has_gravitational_constant_dimension():
    # c^5/(hbar omega^2)
    c5 = (0, 5, -5)
    hbar = (1, 2, -1)
    omega2 = (0, 0, -2)
    got = sub_dim(sub_dim(c5, hbar), omega2)
    assert got == (-1, 3, -2)


def test_occupation_nonidentifiability_is_constructive():
    hbar = 1.054571817e-34
    c = 299792458.0
    omega = 13.0
    a_h = c / (math.sqrt(6.0) * omega)
    E = hbar * omega
    rho1 = 0.25 * E / (c * c * a_h**3)
    rho2 = 0.75 * E / (c * c * a_h**3)
    assert rho1 != rho2
    # Geometry/phase variables are identical; only the unconstrained occupation differs.
    assert math.isclose(rho2 / rho1, 3.0, rel_tol=1e-15)


def test_newton_consistency_relation_is_algebraically_exact():
    hbar = 1.054571817e-34
    c = 299792458.0
    omega = 23.0
    beta = 0.4
    J = 0.21
    a_fs = 0.73
    n_e = 0.62

    xi = (J / a_fs) * (omega / c) ** 2
    rho = 6.0 * math.sqrt(6.0) * n_e * hbar * omega**4 / c**5
    G_candidate = beta * J * c**5 / (24.0 * math.pi * math.sqrt(6.0) * n_e * a_fs * hbar * omega**2)

    lhs = c * c * beta * xi
    rhs = 4.0 * math.pi * G_candidate * rho
    assert math.isclose(lhs, rhs, rel_tol=2e-15, abs_tol=0.0)


if __name__ == "__main__":
    tests = [name for name, obj in globals().items() if name.startswith("test_") and callable(obj)]
    for name in tests:
        globals()[name]()
    print(f"PASS {len(tests)}/{len(tests)}")
