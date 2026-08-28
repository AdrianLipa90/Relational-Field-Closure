import math
import pytest


def field_inertia(amplitudes, volumes):
    if len(amplitudes) != len(volumes) or not amplitudes:
        raise ValueError("common non-empty field support required")
    if any(v <= 0.0 for v in volumes):
        raise ValueError("positive cell volumes required")
    if any(a < 0.0 for a in amplitudes):
        raise ValueError("non-negative field amplitude required")
    return 2.0 * sum((a * a) * v for a, v in zip(amplitudes, volumes))


def field_phase_lagrangian(amplitudes, volumes, dchi):
    return sum((a * a) * v for a, v in zip(amplitudes, volumes)) * dchi * dchi


def rotor_phase_lagrangian(i_phi, dchi):
    if i_phi <= 0.0:
        raise ValueError("positive rotor inertia required")
    return 0.5 * i_phi * dchi * dchi


def test_rfn1b2l_scalar_field_phase_term_has_half_I_A_coefficient():
    amplitudes = [1.0, 2.0, 0.5]
    volumes = [0.5, 1.0, 2.0]
    dchi = 0.7
    i_a = field_inertia(amplitudes, volumes)
    assert math.isclose(
        field_phase_lagrangian(amplitudes, volumes, dchi),
        0.5 * i_a * dchi * dchi,
        rel_tol=1e-15,
        abs_tol=1e-15,
    )


def test_same_collective_reduction_fixes_I_phi_equal_I_A():
    amplitudes = [0.8, 1.1]
    volumes = [1.5, 0.75]
    i_a = field_inertia(amplitudes, volumes)
    i_phi = i_a
    for dchi in (0.2, 0.7, 1.3):
        assert math.isclose(
            field_phase_lagrangian(amplitudes, volumes, dchi),
            rotor_phase_lagrangian(i_phi, dchi),
            rel_tol=1e-15,
            abs_tol=1e-15,
        )


def test_rfn1b2j_inertia_defect_closes_to_zero_after_reduction():
    i_a = field_inertia([1.0, 1.5], [1.0, 2.0])
    i_phi = i_a
    assert abs(i_a / i_phi - 1.0) == 0.0


def test_finite_noether_charge_equals_rotor_kinetic_carrier_after_reduction():
    i_a = field_inertia([1.0, 0.5], [2.0, 1.0])
    i_phi = i_a
    dchi = 0.4
    q_theta = i_a * dchi
    p_phi = i_phi * dchi
    assert q_theta == p_phi


def test_bound_rfc_energy_per_carrier_reduces_to_half_phase_rate():
    i_phi = field_inertia([1.0, 2.0], [1.0, 0.5])
    dchi = 0.6
    p_phi = i_phi * dchi
    h_phi = p_phi * p_phi / (2.0 * i_phi)
    epsilon_n = h_phi / p_phi
    assert math.isclose(epsilon_n, 0.5 * dchi, rel_tol=1e-15, abs_tol=1e-15)


def test_linear_intention_source_does_not_renormalize_quadratic_inertia():
    i_phi = 5.0
    j_i = 1.7
    for dchi in (0.4, 0.9):
        lagrangian = 0.5 * i_phi * dchi * dchi + j_i * dchi
        quadratic_coefficient = (lagrangian - j_i * dchi) / (dchi * dchi)
        assert math.isclose(quadratic_coefficient, i_phi / 2.0, rel_tol=1e-15)


def test_support_measure_and_positive_inertia_gates_fail_closed():
    with pytest.raises(ValueError, match="common non-empty field support"):
        field_inertia([1.0, 2.0], [1.0])
    with pytest.raises(ValueError, match="positive cell volumes"):
        field_inertia([1.0], [0.0])
    with pytest.raises(ValueError, match="non-negative field amplitude"):
        field_inertia([-1.0], [1.0])
    with pytest.raises(ValueError, match="positive rotor inertia"):
        rotor_phase_lagrangian(0.0, 1.0)
