import math
import pytest


def connection_after_gauge(connection, d_lambda):
    return connection - d_lambda


def phase_gradient_after_gauge(d_theta, d_lambda):
    return d_theta + d_lambda


def covariant_phase_gradient(d_theta, connection):
    return d_theta + connection


def collective_inertia(amplitudes, volumes):
    if len(amplitudes) != len(volumes) or not amplitudes:
        raise ValueError("common non-empty support required")
    if any(a < 0.0 for a in amplitudes):
        raise ValueError("non-negative amplitudes required")
    if any(v <= 0.0 for v in volumes):
        raise ValueError("positive volumes required")
    return 2.0 * sum(a * a * v for a, v in zip(amplitudes, volumes))


def test_common_u1_connection_sign_is_gauge_invariant():
    d_theta = 0.35
    connection = 0.4
    d_lambda = -0.8
    before = covariant_phase_gradient(d_theta, connection)
    after = covariant_phase_gradient(
        phase_gradient_after_gauge(d_theta, d_lambda),
        connection_after_gauge(connection, d_lambda),
    )
    assert math.isclose(before, after, rel_tol=1e-15, abs_tol=1e-15)


def test_opposite_phase_connection_combination_is_rejected_by_same_witness():
    d_theta = 0.35
    connection = 0.4
    d_lambda = -0.8
    before = d_theta - connection
    after = phase_gradient_after_gauge(d_theta, d_lambda) - connection_after_gauge(connection, d_lambda)
    assert not math.isclose(before, after, rel_tol=1e-15, abs_tol=1e-15)


def test_common_fiber_pullback_reconstructs_rotor_covariant_rate():
    grad_theta = [0.2, -0.4]
    connection = [0.3, 0.1]
    qdot = [0.8, -0.5]
    theta_dot = sum(g * v for g, v in zip(grad_theta, qdot))
    field_rate = sum((g + a) * v for g, a, v in zip(grad_theta, connection, qdot))
    rotor_rate = theta_dot + sum(a * v for a, v in zip(connection, qdot))
    assert math.isclose(field_rate, rotor_rate, rel_tol=1e-15, abs_tol=1e-15)


def test_collective_field_action_matches_rotor_coefficient_at_I_phi_equals_I_A():
    amplitudes = [0.9, 1.4]
    volumes = [1.2, 0.7]
    rate = 0.65
    i_a = collective_inertia(amplitudes, volumes)
    field_action = sum(a * a * v * rate * rate for a, v in zip(amplitudes, volumes))
    rotor_action = 0.5 * i_a * rate * rate
    assert math.isclose(field_action, rotor_action, rel_tol=1e-15, abs_tol=1e-15)


def test_field_noether_charge_equals_rotor_generator_on_common_reduction():
    amplitudes = [0.5, 1.25, 0.75]
    volumes = [1.0, 0.8, 1.4]
    rate = 0.3
    i_a = collective_inertia(amplitudes, volumes)
    i_phi = i_a
    q_theta = sum(2.0 * a * a * rate * v for a, v in zip(amplitudes, volumes))
    p_phi = i_phi * rate
    assert math.isclose(q_theta, p_phi, rel_tol=1e-15, abs_tol=1e-15)


def test_rfc_energy_per_promoted_carrier_candidate_is_half_rate():
    i_phi = collective_inertia([1.0, 0.8], [1.0, 1.5])
    rate = 0.42
    p_phi = i_phi * rate
    q_theta = p_phi
    h_phi = p_phi * p_phi / (2.0 * i_phi)
    epsilon_q_candidate = h_phi / q_theta
    assert math.isclose(epsilon_q_candidate, rate / 2.0, rel_tol=1e-15, abs_tol=1e-15)


def test_rate_and_generator_defects_are_independently_visible():
    field_rate = 0.44
    rotor_rate = 0.40
    i_a = 5.0
    i_phi = 5.0
    q_theta = i_a * field_rate
    p_phi = i_phi * rotor_rate
    delta_rate = abs(field_rate - rotor_rate) / abs(rotor_rate)
    delta_q = abs(q_theta - p_phi) / abs(p_phi)
    assert delta_rate > 0.0
    assert delta_q > 0.0


def test_support_and_reference_rate_gates_fail_closed():
    with pytest.raises(ValueError, match="common non-empty support"):
        collective_inertia([], [])
    with pytest.raises(ValueError, match="non-negative amplitudes"):
        collective_inertia([-1.0], [1.0])
    with pytest.raises(ValueError, match="positive volumes"):
        collective_inertia([1.0], [-1.0])
    with pytest.raises(ZeroDivisionError):
        _ = abs(0.1 - 0.0) / abs(0.0)
