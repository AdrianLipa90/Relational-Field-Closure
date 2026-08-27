import math

# Dimension vectors are (M, L, T, Q), where Q is the abstract carrier charge.
ENERGY = (1, 2, -2, 0)
C2 = (0, 2, -2, 0)
CHARGE = (0, 0, 0, 1)
CHARGE_DENSITY = (0, -3, 0, 1)


def add_dim(a, b):
    return tuple(x + y for x, y in zip(a, b))


def sub_dim(a, b):
    return tuple(x - y for x, y in zip(a, b))


def scale(values, factor):
    return [factor * x for x in values]


def normalize_carrier(cell_charges):
    total = sum(cell_charges)
    assert total > 0.0
    return total, [q / total for q in cell_charges]


def test_internal_continuity_flux_conserves_total_carrier():
    # Three cells, two internal oriented fluxes 0->1 and 1->2.
    f01 = 0.7
    f12 = -0.2
    qdot = [-f01, f01 - f12, f12]
    assert math.isclose(sum(qdot), 0.0, rel_tol=0.0, abs_tol=1e-15)


def test_normalized_carrier_profile_sums_to_one():
    total, p = normalize_carrier([2.0, 3.0, 5.0])
    assert total == 10.0
    assert math.isclose(sum(p), 1.0, rel_tol=0.0, abs_tol=1e-15)


def test_normalized_profile_is_blind_to_extensive_scale():
    q = [2.0, 3.0, 5.0]
    _, p1 = normalize_carrier(q)
    _, p2 = normalize_carrier(scale(q, 17.0))
    assert all(math.isclose(a, b, rel_tol=0.0, abs_tol=1e-15) for a, b in zip(p1, p2))


def test_idt_shape_does_not_fix_total_source_amount():
    p = [0.2, 0.3, 0.5]
    q1 = scale(p, 4.0)
    q2 = scale(p, 11.0)
    assert q1 != q2
    _, p1 = normalize_carrier(q1)
    _, p2 = normalize_carrier(q2)
    assert p1 == p2 == p


def test_charge_quantum_converts_carrier_to_occupation():
    q0 = 0.25
    cell_charges = [0.5, 1.0, 1.5]
    occupations = [q / q0 for q in cell_charges]
    assert occupations == [2.0, 4.0, 6.0]
    assert math.isclose(sum(occupations), sum(cell_charges) / q0, rel_tol=0.0, abs_tol=1e-15)


def test_charge_quantum_is_not_identified_by_continuity():
    cell_charges = [0.5, 1.0, 1.5]
    n1 = [q / 0.25 for q in cell_charges]
    n2 = [q / 0.50 for q in cell_charges]
    assert n1 != n2
    assert math.isclose(sum(cell_charges), 3.0, rel_tol=0.0, abs_tol=1e-15)


def test_energy_per_charge_times_charge_density_over_c2_has_mass_density_type():
    energy_per_charge = sub_dim(ENERGY, CHARGE)
    energy_density = add_dim(energy_per_charge, CHARGE_DENSITY)
    mass_density = sub_dim(energy_density, C2)
    assert mass_density == (1, -3, 0, 0)


def test_per_quantum_energy_binding_reduces_to_previous_cell_formula():
    hbar = 1.054571817e-34
    c = 299792458.0
    omega = 19.0
    q0 = 0.2
    q_cell = 0.74
    a_h = c / (math.sqrt(6.0) * omega)
    E = hbar * omega

    n_e = q_cell / q0
    rho_from_occupation = n_e * E / (c * c * a_h**3)

    charge_density = q_cell / a_h**3
    energy_per_charge = E / q0
    rho_from_current = energy_per_charge * charge_density / (c * c)

    assert math.isclose(rho_from_occupation, rho_from_current, rel_tol=2e-15, abs_tol=0.0)


def test_energy_per_charge_nonidentifiability_is_constructive():
    c = 299792458.0
    carrier_density = 3.0
    rho1 = 2.0 * carrier_density / (c * c)
    rho2 = 5.0 * carrier_density / (c * c)
    assert rho1 != rho2
    assert math.isclose(rho2 / rho1, 2.5, rel_tol=1e-15)


if __name__ == "__main__":
    tests = [name for name, obj in globals().items() if name.startswith("test_") and callable(obj)]
    for name in tests:
        globals()[name]()
    print(f"PASS {len(tests)}/{len(tests)}")
