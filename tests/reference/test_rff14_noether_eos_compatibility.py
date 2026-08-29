import math

import pytest

from src.rfc.noether_eos_compatibility import (
    NoetherEOSCompatibilityError,
    homogeneous_dust_branch,
    homogeneous_radiation_completion_branch,
    isotropic_null_phase_branch,
    microscopic_phase_eos,
    normal_phase_kinetic_branch,
    phase_cell_compatibility,
    phase_noether_prefactor_binding_residual,
    radiation_compatibility,
    required_prefactor_log_slope_for_eos,
    total_scalar_prefactor_binding_residual,
    vacuum_current_gap,
)


def test_pure_normal_phase_is_stiff_and_has_half_rate_per_action_charge():
    out = microscopic_phase_eos(amplitude_squared=3.0, phase_rate=5.0)
    assert math.isclose(out.equation_of_state, 1.0, rel_tol=1e-15)
    assert math.isclose(out.energy_per_action_charge_rate, 2.5, rel_tol=1e-15)
    assert math.isclose(out.generator_prefactor_ratio, 0.5, rel_tol=1e-15)
    assert abs(phase_noether_prefactor_binding_residual(out.generator_prefactor_ratio)) < 1e-15


def test_isotropic_null_phase_is_radiation_and_has_unit_prefactor_ratio():
    out = microscopic_phase_eos(
        amplitude_squared=2.0,
        phase_rate=7.0,
        spatial_phase_norm=7.0,
    )
    assert math.isclose(out.equation_of_state, 1.0 / 3.0, rel_tol=1e-15)
    assert math.isclose(out.generator_prefactor_ratio, 1.0, rel_tol=1e-15)
    rad = radiation_compatibility(2.0, 7.0, 7.0, 0.0)
    assert abs(rad.radiation_surface_residual) < 1e-15


def test_homogeneous_normal_radiation_completion_requires_V_equals_K_over_two():
    A2 = 4.0
    omega = 3.0
    K = A2 * omega**2
    out = microscopic_phase_eos(A2, omega, 0.0, 0.5 * K)
    assert math.isclose(out.equation_of_state, 1.0 / 3.0, rel_tol=1e-15)
    assert math.isclose(out.potential_ratio, 0.5, rel_tol=1e-15)
    assert math.isclose(out.generator_prefactor_ratio, 0.75, rel_tol=1e-15)
    rad = radiation_compatibility(A2, omega, 0.0, 0.5 * K)
    assert abs(rad.radiation_surface_residual) < 1e-15


def test_exact_radiation_surface_is_x_plus_two_v_equals_one():
    A2 = 5.0
    omega = 4.0
    x = 0.36
    k = omega * math.sqrt(x)
    K = A2 * omega**2
    v = (1.0 - x) / 2.0
    out = radiation_compatibility(A2, omega, k, v * K)
    assert abs(out.radiation_surface_residual) < 1e-15
    state = microscopic_phase_eos(A2, omega, k, v * K)
    assert math.isclose(state.equation_of_state, 1.0 / 3.0, rel_tol=1e-14)


def test_rf_e5_normal_dust_surface_has_total_energy_per_current_equal_omega():
    A2 = 2.0
    omega = 6.0
    K = A2 * omega**2
    out = microscopic_phase_eos(A2, omega, 0.0, K)
    assert abs(out.equation_of_state) < 1e-15
    assert math.isclose(out.energy_per_action_charge_rate, omega, rel_tol=1e-15)
    assert math.isclose(out.generator_prefactor_ratio, 1.0, rel_tol=1e-15)


def test_named_branch_signatures_roundtrip_exact_surfaces():
    stiff = normal_phase_kinetic_branch(3.0, 5.0)
    null_rad = isotropic_null_phase_branch(3.0, 5.0)
    normal_rad = homogeneous_radiation_completion_branch(3.0, 5.0)
    dust = homogeneous_dust_branch(3.0, 5.0)
    assert math.isclose(stiff.equation_of_state, 1.0, rel_tol=1e-15)
    assert math.isclose(stiff.generator_prefactor_ratio, 0.5, rel_tol=1e-15)
    assert math.isclose(null_rad.equation_of_state, 1.0 / 3.0, rel_tol=1e-15)
    assert math.isclose(null_rad.generator_prefactor_ratio, 1.0, rel_tol=1e-15)
    assert math.isclose(normal_rad.equation_of_state, 1.0 / 3.0, rel_tol=1e-15)
    assert math.isclose(normal_rad.generator_prefactor_ratio, 0.75, rel_tol=1e-15)
    assert abs(dust.equation_of_state) < 1e-15
    assert math.isclose(dust.generator_prefactor_ratio, 1.0, rel_tol=1e-15)


def test_f8_phase_cell_slope_requirement_separates_stiff_radiation_and_dust():
    assert math.isclose(required_prefactor_log_slope_for_eos(1.0), 2.0, rel_tol=1e-15)
    assert math.isclose(required_prefactor_log_slope_for_eos(1.0 / 3.0), 0.0, abs_tol=1e-15)
    assert math.isclose(required_prefactor_log_slope_for_eos(0.0), -1.0, rel_tol=1e-15)
    assert math.isclose(required_prefactor_log_slope_for_eos(-1.0), -4.0, rel_tol=1e-15)


def test_constant_prefactor_phase_cell_branch_is_radiation_effective_eos():
    out = phase_cell_compatibility(microscopic_w=1.0 / 3.0, supplied_prefactor_log_slope=0.0)
    assert abs(out.eos_residual) < 1e-15
    assert math.isclose(out.phase_cell_w, 1.0 / 3.0, rel_tol=1e-15)


def test_pure_normal_noether_half_prefactor_is_not_same_separately_conserved_phase_cell_stiff_surface():
    out = phase_cell_compatibility(microscopic_w=1.0, supplied_prefactor_log_slope=0.0)
    assert math.isclose(out.phase_cell_w, 1.0 / 3.0, rel_tol=1e-15)
    assert not math.isclose(out.eos_residual, 0.0, abs_tol=1e-15)
    assert math.isclose(out.required_prefactor_log_slope, 2.0, rel_tol=1e-15)


def test_total_scalar_binding_distinguishes_phase_only_and_radiation_completion():
    A2 = 2.0
    omega = 8.0
    pure = microscopic_phase_eos(A2, omega)
    rad = homogeneous_radiation_completion_branch(A2, omega)
    rad_state = microscopic_phase_eos(A2, omega, 0.0, 0.5 * A2 * omega**2)
    assert abs(total_scalar_prefactor_binding_residual(0.5, pure)) < 1e-15
    assert math.isclose(rad.generator_prefactor_ratio, 0.75, rel_tol=1e-15)
    assert abs(total_scalar_prefactor_binding_residual(0.75, rad_state)) < 1e-15
    assert not math.isclose(total_scalar_prefactor_binding_residual(0.5, rad_state), 0.0, abs_tol=1e-15)


def test_nonzero_phase_current_has_strict_positive_vacuum_gap():
    gap = vacuum_current_gap(amplitude_squared=3.0, phase_rate=4.0, spatial_phase_norm=2.0)
    assert gap > 0.0
    state = microscopic_phase_eos(3.0, 4.0, 2.0, potential_density=100.0)
    assert math.isclose(gap, state.vacuum_gap, rel_tol=1e-15)


def test_zero_phase_rate_boundary_has_zero_phase_kinetic_vacuum_gap():
    assert vacuum_current_gap(3.0, 0.0, 0.0) == 0.0


def test_fail_closed_inputs():
    bad = (
        lambda: microscopic_phase_eos(0.0, 1.0),
        lambda: microscopic_phase_eos(1.0, 0.0),
        lambda: microscopic_phase_eos(1.0, 1.0, -1.0),
        lambda: microscopic_phase_eos(1.0, 1.0, 0.0, -1.0),
        lambda: microscopic_phase_eos(float("nan"), 1.0),
        lambda: vacuum_current_gap(0.0, 1.0),
        lambda: vacuum_current_gap(1.0, -1.0),
    )
    for call in bad:
        with pytest.raises(NoetherEOSCompatibilityError):
            call()
