import math


C = 299_792_458.0


def field_inertia(amplitudes, volumes):
    if len(amplitudes) != len(volumes) or not amplitudes:
        raise ValueError("support mismatch")
    return 2.0 * sum((a * a) * v for a, v in zip(amplitudes, volumes))


def noether_charge(i_a, phase_rate):
    return i_a * phase_rate


def rotor_carrier(j_total, j_i):
    return j_total - j_i


def rotor_energy(p_phi, i_phi):
    if i_phi <= 0.0:
        raise ValueError("I_phi must be positive")
    return p_phi * p_phi / (2.0 * i_phi)


def epsilon_noether(h_phi, q_theta):
    if q_theta <= 0.0:
        raise ValueError("positive finite Noether carrier required")
    return h_phi / q_theta


def test_noether_finite_charge_from_collective_phase_rate():
    i_a = field_inertia([1.0, 2.0], [0.5, 0.25])
    assert math.isclose(i_a, 3.0, rel_tol=0.0, abs_tol=1e-15)
    assert math.isclose(noether_charge(i_a, 2.0), 6.0, rel_tol=0.0, abs_tol=1e-15)


def test_inertia_binding_maps_noether_charge_to_rotor_kinetic_charge():
    i_phi = 3.0
    rate = 2.0
    q_theta = noether_charge(i_phi, rate)
    p_phi = rotor_carrier(10.0, 4.0)
    assert math.isclose(q_theta, p_phi, rel_tol=0.0, abs_tol=1e-15)


def test_inertia_binding_defect_is_exact_ratio_defect():
    i_phi = 4.0
    i_a = 5.0
    rate = 1.5
    q_theta = noether_charge(i_a, rate)
    p_phi = i_phi * rate
    defect = abs(q_theta - p_phi) / abs(p_phi)
    assert math.isclose(defect, abs(i_a / i_phi - 1.0), rel_tol=0.0, abs_tol=1e-15)


def test_general_rfc_energy_per_carrier_is_typed_by_q_theta():
    i_phi = 4.0
    i_a = 5.0
    rate = 1.5
    p_phi = i_phi * rate
    q_theta = noether_charge(i_a, rate)
    h_phi = rotor_energy(p_phi, i_phi)
    epsilon_n = epsilon_noether(h_phi, q_theta)
    assert math.isclose(epsilon_n, h_phi / q_theta, rel_tol=0.0, abs_tol=1e-15)
    assert not math.isclose(epsilon_n, h_phi / p_phi, rel_tol=0.0, abs_tol=1e-15)


def test_euler_closed_ratio_reduces_to_p_over_2I_under_inertia_binding():
    hbar = 1.0
    theta_i_eb = math.pi
    j_i = hbar * theta_i_eb
    p_phi = rotor_carrier(2.0 * math.pi, j_i)
    i_phi = 2.0
    q_theta = noether_charge(i_phi, p_phi / i_phi)
    h_phi = rotor_energy(p_phi, i_phi)
    epsilon_n = epsilon_noether(h_phi, q_theta)
    assert math.isclose(q_theta, p_phi, rel_tol=0.0, abs_tol=1e-15)
    assert math.isclose(epsilon_n, p_phi / (2.0 * i_phi), rel_tol=0.0, abs_tol=1e-15)


def test_noether_energy_per_charge_equals_half_phase_rate_after_inertia_binding():
    i_phi = 2.0
    rate = 3.0
    p_phi = i_phi * rate
    q_theta = noether_charge(i_phi, rate)
    h_phi = rotor_energy(p_phi, i_phi)
    assert math.isclose(epsilon_noether(h_phi, q_theta), rate / 2.0, rel_tol=0.0, abs_tol=1e-15)


def test_rfc_mass_coordinate_equals_rotor_energy_over_c2_for_finite_noether_charge():
    i_phi = 2.0
    i_a = 2.5
    rate = 1.5
    p_phi = i_phi * rate
    q_theta = noether_charge(i_a, rate)
    h_phi = rotor_energy(p_phi, i_phi)
    epsilon_n = epsilon_noether(h_phi, q_theta)
    m_n = epsilon_n * q_theta / (C * C)
    assert math.isclose(m_n, h_phi / (C * C), rel_tol=1e-15, abs_tol=0.0)


def test_zero_noether_carrier_remains_outside_positive_source_ratio_sector():
    try:
        epsilon_noether(1.0, 0.0)
    except ValueError:
        pass
    else:
        raise AssertionError("zero carrier must fail closed")
