import math

import pytest

from src.rfc.dynamical_phase_transport import (
    DynamicalPhaseTransportError,
    boundary_flux_source_identity,
    constant_B_dust_phase_factor_squared,
    constant_dust_phase_energy_invariant,
    constant_lambda_constant_B_omega_dot,
    constant_w_energy_per_occupation,
    constant_w_prefactor,
    flrw_density_scaling,
    flrw_phase_cell_scaling,
    flrw_phase_rate,
    phase_energy_curvature_2form,
    phase_energy_transport_state,
)
from src.rfc.foundational_phase_source_formalism import KAPPA_INFO


def test_phase_energy_curvature_vanishes_on_constant_B_flat_connection_patch():
    out = phase_energy_curvature_2form(
        2.0,
        0.7,
        (0.0, 0.0),
        (1.0, 3.0),
        ((0.0, 0.0), (0.0, 0.0)),
    )
    assert out == ((0.0, 0.0), (0.0, 0.0))


def test_phase_energy_curvature_contains_dB_wedge_phase_and_connection_curvature():
    B = 2.0
    X = 3.0
    dB = (1.0, 4.0)
    Omega = (5.0, 7.0)
    F = ((0.0, 11.0), (-11.0, 0.0))
    out = phase_energy_curvature_2form(B, X, dB, Omega, F)
    expected01 = X * (dB[0] * Omega[1] - dB[1] * Omega[0]) + B * X * F[0][1]
    assert math.isclose(out[0][1], expected01, rel_tol=0.0, abs_tol=1e-15)
    assert math.isclose(out[1][0], -expected01, rel_tol=0.0, abs_tol=1e-15)
    assert out[0][0] == 0.0
    assert out[1][1] == 0.0


def test_boundary_flux_identity_reduces_source_to_divergence_for_constant_B_conserved_current():
    out = boundary_flux_source_identity(
        B_action=2.0,
        phase_factor=3.0,
        current_phase_derivative=5.0,
        current_B_derivative=0.0,
        current_divergence=0.0,
    )
    assert out.source_density == 30.0
    assert out.flux_divergence == 30.0
    assert out.reconstructed_source_density == 30.0


def test_boundary_flux_identity_tracks_variable_B_and_current_divergence_corrections():
    out = boundary_flux_source_identity(
        B_action=2.0,
        phase_factor=3.0,
        current_phase_derivative=5.0,
        current_B_derivative=7.0,
        current_divergence=11.0,
    )
    assert math.isclose(
        out.reconstructed_source_density,
        out.source_density,
        rel_tol=0.0,
        abs_tol=1e-15,
    )
    assert out.B_gradient_correction != 0.0
    assert out.current_divergence_correction != 0.0


def test_phase_energy_derivative_matches_direct_finite_algebra():
    B = 2.0
    Bdot = 3.0
    omega = 5.0
    omega_dot = 7.0
    phase = 0.4
    X = phase + KAPPA_INFO
    out = phase_energy_transport_state(B, Bdot, omega, omega_dot, phase)
    expected = Bdot * omega * X + B * omega_dot * X + B * omega**2
    assert math.isclose(out.comoving_energy_rate, expected, rel_tol=1e-15)


def test_dynamic_lambda_exchange_zero_residual_when_transport_matches_target():
    B = 1.5
    omega = 2.0
    phase = 0.3
    X = phase + KAPPA_INFO
    Bdot = 0.2
    omega_dot = -0.6
    epsilon_dot = Bdot * omega * X + B * omega_dot * X + B * omega**2
    kappa_E = 4.0
    n = 5.0
    lambda_dot = -epsilon_dot * kappa_E * n
    out = phase_energy_transport_state(
        B,
        Bdot,
        omega,
        omega_dot,
        phase,
        lambda_dot=lambda_dot,
        kappa_E=kappa_E,
        proper_density=n,
    )
    assert abs(out.transport_residual) < 1e-15


def test_constant_lambda_constant_B_dust_transport_makes_energy_invariant():
    B = 2.5
    omega = 4.0
    phase = 0.7
    omega_dot = constant_lambda_constant_B_omega_dot(omega, phase)
    out = phase_energy_transport_state(B, 0.0, omega, omega_dot, phase)
    assert abs(out.comoving_energy_rate) < 1e-14


def test_constant_B_dust_integrated_solution_preserves_omega_times_phase_factor():
    X0 = 2.0
    C = 3.0
    dt = 5.0
    X2 = constant_B_dust_phase_factor_squared(X0, C, dt)
    assert math.isclose(X2, X0**2 + 2.0 * C * dt, rel_tol=0.0, abs_tol=1e-15)


def test_constant_w_integrated_prefactor_family():
    C = 7.0
    omega = 5.0
    dust = constant_w_prefactor(C, omega, 0.0)
    radiation = constant_w_prefactor(C, omega, 1.0 / 3.0)
    vacuum = constant_w_prefactor(C, omega, -1.0)
    assert math.isclose(dust, C / omega, rel_tol=1e-15)
    assert math.isclose(radiation, C, rel_tol=1e-15)
    assert math.isclose(vacuum, C / omega**4, rel_tol=1e-15)


def test_constant_w_energy_scaling_family():
    C = 2.0
    omega = 5.0
    assert math.isclose(constant_w_energy_per_occupation(C, omega, 0.0), C, rel_tol=1e-15)
    assert math.isclose(constant_w_energy_per_occupation(C, omega, 1.0 / 3.0), C * omega, rel_tol=1e-15)
    assert math.isclose(constant_w_energy_per_occupation(C, omega, -1.0), C / omega**3, rel_tol=1e-15)


def test_flrw_phase_cell_scaling_is_exactly_geometric():
    out = flrw_phase_cell_scaling(3.0)
    assert out.omega_ratio == pytest.approx(1.0 / 3.0)
    assert out.phase_clock_length_ratio == pytest.approx(3.0)
    assert out.projective_area_ratio == pytest.approx(9.0)
    assert out.relational_volume_ratio == pytest.approx(27.0)


def test_flrw_phase_rate_has_a_omega_invariant():
    omega0 = 8.0
    a0 = 2.0
    a1 = 5.0
    omega1 = flrw_phase_rate(omega0, a0, a1)
    assert math.isclose(a0 * omega0, a1 * omega1, rel_tol=1e-15)


def test_flrw_density_scaling_recovers_standard_dust_radiation_vacuum_exponents():
    rho0 = 10.0
    a0 = 1.0
    a1 = 2.0
    dust = flrw_density_scaling(rho0, a0, a1, 0.0)
    radiation = flrw_density_scaling(rho0, a0, a1, 1.0 / 3.0)
    vacuum = flrw_density_scaling(rho0, a0, a1, -1.0)
    assert math.isclose(dust, rho0 / 8.0, rel_tol=1e-15)
    assert math.isclose(radiation, rho0 / 16.0, rel_tol=1e-15)
    assert math.isclose(vacuum, rho0, rel_tol=1e-15)


def test_fail_closed_inputs():
    bad_calls = (
        lambda: phase_energy_curvature_2form(1.0, 1.0, (1.0,), (1.0, 2.0), ((0.0,),)),
        lambda: phase_energy_curvature_2form(1.0, 1.0, (1.0, 2.0), (3.0, 4.0), ((0.0, 1.0), (1.0, 0.0))),
        lambda: phase_energy_transport_state(1.0, 0.0, 1.0, 0.0, 0.0, kappa_E=0.0),
        lambda: phase_energy_transport_state(1.0, 0.0, 1.0, 0.0, 0.0, proper_density=0.0),
        lambda: constant_lambda_constant_B_omega_dot(1.0, -KAPPA_INFO),
        lambda: constant_w_prefactor(1.0, 0.0, 0.0),
        lambda: constant_w_energy_per_occupation(1.0, 0.0, 0.0),
        lambda: flrw_phase_cell_scaling(0.0),
        lambda: flrw_phase_rate(1.0, 1.0, 0.0),
        lambda: flrw_density_scaling(1.0, 1.0, 0.0, 0.0),
    )
    for call in bad_calls:
        with pytest.raises(DynamicalPhaseTransportError):
            call()
