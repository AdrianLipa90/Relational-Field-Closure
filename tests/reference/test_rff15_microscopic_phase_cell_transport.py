import math

import pytest

from src.rfc.microscopic_phase_cell_transport import (
    MicroscopicPhaseCellTransportError,
    current_phase_cell_binding,
    dust_transport_solution,
    fixed_spatial_ratio_solution,
    radiation_fixed_point,
    transport_compatibility,
)


def test_current_binding_fixes_amplitude_squared_proportional_to_omega_squared():
    q0 = 7.0
    N = 5.0
    a_fs = 2.0
    c = 3.0
    out1 = current_phase_cell_binding(N, q0, 4.0, area_fs_dimensionless=a_fs, c_light=c)
    out2 = current_phase_cell_binding(N, q0, 8.0, area_fs_dimensionless=a_fs, c_light=c)
    assert math.isclose(out2.amplitude_squared / out1.amplitude_squared, 4.0, rel_tol=1e-15)
    assert math.isclose(out1.action_charge_density, 2.0 * out1.amplitude_squared * out1.phase_rate, rel_tol=1e-15)


def test_current_binding_roundtrips_phase_cell_density():
    out = current_phase_cell_binding(3.0, 11.0, 5.0, area_fs_dimensionless=math.pi, c_light=2.0)
    assert math.isclose(out.occupation_density, 3.0 / out.phase_cell_volume, rel_tol=1e-15)
    assert math.isclose(out.action_charge_density, 11.0 * out.occupation_density, rel_tol=1e-15)


def test_transport_equation_exact_on_radiation_fixed_point():
    for x in (0.0, 0.25, 1.0):
        rad = radiation_fixed_point(x)
        out = transport_compatibility(x, rad.potential_ratio, 0.0, 0.0)
        assert abs(out.differential_residual) < 1e-15
        assert math.isclose(out.microscopic_w, 1.0 / 3.0, rel_tol=1e-15)
        assert math.isclose(rad.generator_prefactor_ratio, (3.0 + x) / 4.0, rel_tol=1e-15)


def test_null_and_normal_radiation_endpoints_match_rf_f14():
    normal = radiation_fixed_point(0.0)
    null = radiation_fixed_point(1.0)
    assert math.isclose(normal.potential_ratio, 0.5, rel_tol=1e-15)
    assert math.isclose(normal.generator_prefactor_ratio, 0.75, rel_tol=1e-15)
    assert math.isclose(null.potential_ratio, 0.0, abs_tol=1e-15)
    assert math.isclose(null.generator_prefactor_ratio, 1.0, rel_tol=1e-15)


def test_fixed_x_solution_is_exact_radiation_plus_constant_vacuum():
    x = 0.4
    omega = 3.0
    C = 7.0
    K0 = 2.5
    out = fixed_spatial_ratio_solution(x, omega, C, K0)
    assert abs(out.differential_residual) < 1e-14
    assert math.isclose(out.total_density, out.radiation_density + out.vacuum_density, rel_tol=1e-15)
    assert math.isclose(out.total_pressure, out.radiation_density / 3.0 - out.vacuum_density, rel_tol=1e-15)
    assert math.isclose(out.vacuum_density, K0 * C, rel_tol=1e-15)


def test_fixed_x_zero_integration_constant_is_pure_radiation():
    out = fixed_spatial_ratio_solution(0.6, 5.0, 0.0, 1.7)
    assert abs(out.differential_residual) < 1e-15
    assert out.vacuum_density == 0.0
    assert math.isclose(out.eos, 1.0 / 3.0, rel_tol=1e-15)


def test_fixed_x_vacuum_piece_is_independent_of_phase_rate():
    a = fixed_spatial_ratio_solution(0.2, 2.0, 9.0, 4.0)
    b = fixed_spatial_ratio_solution(0.2, 5.0, 9.0, 4.0)
    assert math.isclose(a.vacuum_density, b.vacuum_density, rel_tol=1e-15)
    expected_ratio = (5.0 / 2.0) ** 4
    assert math.isclose(b.radiation_density / a.radiation_density, expected_ratio, rel_tol=1e-15)


def test_dust_transport_has_zero_pressure_constant_energy_per_charge_and_omega_cubed_density():
    Cd = 12.0
    K0 = 2.0
    a = dust_transport_solution(3.0, Cd, K0)
    b = dust_transport_solution(2.5, Cd, K0)
    assert abs(a.differential_residual) < 1e-14
    assert abs(b.differential_residual) < 1e-14
    assert abs(a.pressure) < 1e-12
    assert abs(b.pressure) < 1e-12
    assert math.isclose(a.energy_per_action_charge_rate, Cd / 3.0, rel_tol=1e-15)
    assert math.isclose(b.energy_per_action_charge_rate, Cd / 3.0, rel_tol=1e-15)
    assert math.isclose(a.density / b.density, (3.0 / 2.5) ** 3, rel_tol=1e-14)


def test_dust_prefactor_is_inverse_phase_rate():
    Cd = 12.0
    a = dust_transport_solution(3.0, Cd, 1.0)
    b = dust_transport_solution(2.5, Cd, 1.0)
    assert math.isclose(a.generator_prefactor_ratio / b.generator_prefactor_ratio, 2.5 / 3.0, rel_tol=1e-15)
    assert math.isclose(a.generator_prefactor_ratio * a.phase_rate, Cd / 3.0, rel_tol=1e-15)


def test_dust_x_and_v_stay_on_microscopic_pressureless_surface():
    out = dust_transport_solution(3.0, 12.0, 1.0)
    assert math.isclose(out.potential_ratio, 1.0 - out.spatial_ratio / 3.0, rel_tol=1e-15)
    assert math.isclose(out.energy_factor, 2.0 * 12.0 / (3.0 * 3.0), rel_tol=1e-15)


def test_general_transport_residual_detects_wrong_composition_flow():
    out = transport_compatibility(0.0, 1.0, 0.0, 0.0)
    assert out.differential_residual != 0.0
    assert math.isclose(out.microscopic_w, 0.0, abs_tol=1e-15)
    assert math.isclose(out.required_energy_factor_derivative, -2.0, rel_tol=1e-15)


def test_fail_closed_inputs():
    bad = (
        lambda: current_phase_cell_binding(-1.0, 1.0, 1.0),
        lambda: current_phase_cell_binding(1.0, 0.0, 1.0),
        lambda: current_phase_cell_binding(1.0, 1.0, 0.0),
        lambda: radiation_fixed_point(-0.1),
        lambda: radiation_fixed_point(1.1),
        lambda: transport_compatibility(-1.0, 0.0, 0.0, 0.0),
        lambda: fixed_spatial_ratio_solution(0.0, 0.0, 1.0, 1.0),
        lambda: fixed_spatial_ratio_solution(3.0, 1.0, 0.0, 1.0),
        lambda: dust_transport_solution(3.0, 8.0, 1.0),
        lambda: dust_transport_solution(float("nan"), 12.0, 1.0),
    )
    for call in bad:
        with pytest.raises(MicroscopicPhaseCellTransportError):
            call()
