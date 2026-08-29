import math

import pytest

from src.rfc.foundational_phase_source_formalism import (
    C_LIGHT,
    FULL_TETRA_FS_AREA,
    KAPPA_INFO,
    FoundationalPhaseSourceError,
    berry_connection_sign_bridge,
    covariant_source_state,
    density_scaling_exponent_from_eos,
    direct_generator_density,
    dust_divergence_from_current_conservation,
    dust_tensor_from_current,
    energy_from_phase_action_rate,
    eos_from_energy_scaling_exponent,
    euler_projective_closure_residual,
    euler_root_triad_closure_residual,
    expansion_from_phase_rate_log_derivative,
    generator_prefactor_scaling_for_eos,
    occupation_density_from_cell,
    path_holonomy_difference,
    phase_action_rate,
    phase_cell,
    phase_energy_state,
    proper_density_from_fourcurrent,
    projective_holonomy,
    relational_lifted_phase,
    transformed_connection_line_integral_minus,
)


def test_kappa_is_canonical_information_offset():
    assert math.isclose(KAPPA_INFO, math.log(2.0) / (24.0 * math.pi), rel_tol=0.0, abs_tol=1e-18)


def test_rf01_and_rfn1b2m_connection_signs_are_exact_opposites():
    bridge = berry_connection_sign_bridge(0.375)
    assert bridge.berry_plus == 0.375
    assert bridge.phase_minus == -0.375


def test_wilson_line_dressed_relational_phase_is_gauge_invariant():
    theta_x = 1.7
    theta_0 = -0.4
    line = 0.63
    base = relational_lifted_phase(theta_x, theta_0, line)

    lambda_x = 4.2
    lambda_0 = -1.1
    transformed_line = transformed_connection_line_integral_minus(line, lambda_x, lambda_0)
    transformed = relational_lifted_phase(
        theta_x + lambda_x,
        theta_0 + lambda_0,
        transformed_line,
    )

    assert math.isclose(
        base.lifted_relational_phase,
        transformed.lifted_relational_phase,
        rel_tol=0.0,
        abs_tol=1e-15,
    )


def test_two_path_relational_phase_difference_is_loop_holonomy_lift():
    assert math.isclose(path_holonomy_difference(1.25, -0.75), 2.0, rel_tol=0.0, abs_tol=1e-15)


def test_projective_euler_closure_and_lifted_winding():
    for winding in range(-8, 9):
        gamma = 2.0 * math.pi * winding
        assert euler_projective_closure_residual(gamma) < 1e-14
        assert abs(projective_holonomy(gamma) - 1.0) < 1e-14


def test_euler_root_triad_closes_for_arbitrary_relational_phase():
    for phase in (-17.0, -0.3, 0.0, 0.71, 21.5):
        assert euler_root_triad_closure_residual(phase) < 5e-15


def test_phase_cell_matches_rfs15_geometry():
    omega = 8.0e6
    cell = phase_cell(omega)
    assert math.isclose(cell.area_fs_dimensionless, math.pi, rel_tol=0.0, abs_tol=1e-15)
    assert math.isclose(cell.phase_clock_length_m, C_LIGHT / omega, rel_tol=1e-15)
    assert math.isclose(cell.projective_area_m2, math.pi * C_LIGHT**2 / omega**2, rel_tol=1e-15)
    assert math.isclose(cell.relational_volume_m3, math.pi * C_LIGHT**3 / omega**3, rel_tol=1e-15)


def test_phase_energy_is_comoving_phase_action_rate_for_constant_B():
    B = 2.5e-34
    omega = 7.0e9
    phase = 0.42
    state = phase_energy_state(B, omega, phase)
    action_rate = phase_action_rate(B, 0.0, omega, phase)
    assert math.isclose(action_rate, state.energy_per_occupation_joule, rel_tol=1e-15)


def test_variable_B_phase_action_identity_recovers_generator_energy_exactly():
    B = 1.7e-34
    Bdot = 3.2e-20
    omega = 4.0e8
    phase = -0.1
    state = phase_energy_state(B, omega, phase)
    action_rate = phase_action_rate(B, Bdot, omega, phase)
    recovered = energy_from_phase_action_rate(action_rate, Bdot, phase)
    assert math.isclose(recovered, state.energy_per_occupation_joule, rel_tol=1e-15, abs_tol=1e-40)


def test_covariant_cell_source_equals_original_generator_exactly():
    B = 3.25e-34
    omega = 7.5e9
    occupation = 42.0
    phase = 0.61
    cell = phase_cell(omega)
    state = covariant_source_state(occupation, B, omega, phase)
    direct = direct_generator_density(
        B,
        omega,
        occupation,
        cell.projective_area_m2,
        cell.phase_clock_length_m,
        phase,
    )
    assert math.isclose(state.energy_density_j_m3, direct, rel_tol=1e-15)
    assert math.isclose(
        state.proper_occupation_density_m3,
        occupation_density_from_cell(occupation, omega),
        rel_tol=1e-15,
    )


def test_full_tetra_positive_frequency_source_has_omega4_state_family_scaling():
    B = 2.0e-34
    occupation = 9.0
    phase = 0.31
    rho1 = covariant_source_state(occupation, B, 2.0e6, phase).energy_density_j_m3
    rho2 = covariant_source_state(occupation, B, 4.0e6, phase).energy_density_j_m3
    assert math.isclose(rho2 / rho1, 16.0, rel_tol=1e-15)


def test_timelike_current_reconstructs_proper_density_and_dust_tensor():
    J = (5.0, 3.0, 0.0, 0.0)
    n = proper_density_from_fourcurrent(J)
    assert math.isclose(n, 4.0, rel_tol=0.0, abs_tol=1e-15)

    epsilon = 7.0
    tensor = dust_tensor_from_current(epsilon, J)
    assert math.isclose(tensor[0][0], epsilon * 25.0 / 4.0, rel_tol=1e-15)
    assert math.isclose(tensor[0][1], epsilon * 15.0 / 4.0, rel_tol=1e-15)
    assert math.isclose(tensor[1][1], epsilon * 9.0 / 4.0, rel_tol=1e-15)


def test_dust_divergence_identity_separates_energy_rate_and_acceleration():
    n = 2.0
    epsilon = 3.0
    edot = 5.0
    u_cov = (-1.0, 0.0, 0.0, 0.0)
    a_cov = (0.0, 0.25, -0.5, 1.0)
    out = dust_divergence_from_current_conservation(n, epsilon, edot, u_cov, a_cov)
    assert out == (-10.0, 1.5, -3.0, 6.0)


def test_phase_cell_continuity_maps_energy_scaling_to_equation_of_state():
    assert eos_from_energy_scaling_exponent(0.0) == 0.0
    assert math.isclose(eos_from_energy_scaling_exponent(1.0), 1.0 / 3.0, rel_tol=0.0, abs_tol=1e-15)
    assert eos_from_energy_scaling_exponent(-3.0) == -1.0


def test_generator_prefactor_scalings_for_dust_radiation_and_vacuum():
    assert generator_prefactor_scaling_for_eos(0.0) == -1.0
    assert math.isclose(generator_prefactor_scaling_for_eos(1.0 / 3.0), 0.0, rel_tol=0.0, abs_tol=1e-15)
    assert generator_prefactor_scaling_for_eos(-1.0) == -4.0


def test_density_scaling_exponent_matches_perfect_fluid_continuity():
    assert density_scaling_exponent_from_eos(0.0) == 3.0
    assert density_scaling_exponent_from_eos(1.0 / 3.0) == 4.0
    assert density_scaling_exponent_from_eos(-1.0) == 0.0


def test_number_current_continuity_links_expansion_to_phase_rate():
    assert expansion_from_phase_rate_log_derivative(-0.2) == pytest.approx(0.6)


def test_fail_closed_inputs():
    bad_calls = (
        lambda: phase_cell(0.0),
        lambda: phase_cell(1.0, area_fs_dimensionless=0.0),
        lambda: covariant_source_state(-1.0, 1.0, 1.0, 0.0),
        lambda: direct_generator_density(1.0, 1.0, 1.0, 0.0, 1.0, 0.0),
        lambda: proper_density_from_fourcurrent((1.0, 1.0, 0.0, 0.0)),
        lambda: proper_density_from_fourcurrent((-2.0, 0.0, 0.0, 0.0)),
        lambda: dust_tensor_from_current(-1.0, (2.0, 0.0, 0.0, 0.0)),
        lambda: relational_lifted_phase(float("nan"), 0.0, 0.0),
    )
    for call in bad_calls:
        with pytest.raises(FoundationalPhaseSourceError):
            call()
