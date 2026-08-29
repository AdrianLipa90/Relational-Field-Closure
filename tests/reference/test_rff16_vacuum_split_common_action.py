import math

import pytest

from src.rfc.vacuum_split_common_action import (
    VacuumSplitError,
    dynamic_lambda,
    effective_scalar_mass_sq,
    exchange_partition,
    fixed_x_generator_potential,
    fixed_x_generator_rho_p,
    interaction_lagrangian_derivative,
    kinetic_divergence_coefficient,
    minimal_common_potential_coefficient,
    source_modified_transport_rhs,
    total_nonvacuum_divergence_coefficient,
    vacuum_reference_state,
    vacuum_split_invariant,
)


def test_constant_vacuum_absorbs_into_lambda_star():
    state = vacuum_reference_state(2.0, 3.0, 5.0, 7.0)
    assert state.lambda_star == 38.0
    assert dynamic_lambda(state.lambda_star, 3.0, 0.0) == 38.0


def test_vacuum_split_constant_shift_is_geometry_invariant():
    base = vacuum_split_invariant(2.0, 3.0, 5.0, 7.0)
    shifted = vacuum_split_invariant(2.0, 3.0, 9.5, 2.5)
    assert shifted == base


def test_eta_partition_sums_to_one():
    part = exchange_partition(0.37)
    assert math.isclose(part.generator_fraction + part.kinetic_fraction, 1.0)


def test_eta_zero_recovers_unsourced_rff15_transport():
    rhs = source_modified_transport_rhs(0.2, 0.4, 0.0, 11.0, 100.0)
    assert math.isclose(rhs, 2.0 * (1.0 - 0.2 - 0.8))


def test_fixed_x_solution_reconstructs_plus_eta_u_lagrangian_interaction():
    K, x, rho_c, eta, uhat = 12.0, 0.25, 4.0, 0.6, 5.0
    V1 = fixed_x_generator_potential(K, x, rho_c, eta, uhat)
    V2 = fixed_x_generator_potential(K, x, rho_c, eta, uhat + 1e-6)
    dVdU = (V2 - V1) / 1e-6
    assert math.isclose(dVdU, -eta, rel_tol=1e-7, abs_tol=1e-7)
    assert math.isclose(interaction_lagrangian_derivative(eta, 2.5), eta * 2.5)


def test_fixed_x_rho_p_vacuum_shift_is_metric_proportional():
    K, x, rho_c, eta = 8.0, 0.5, 3.0, 0.75
    rho0, p0 = fixed_x_generator_rho_p(K, x, rho_c, eta, 0.0)
    rho1, p1 = fixed_x_generator_rho_p(K, x, rho_c, eta, 2.0)
    assert math.isclose(rho1 - rho0, -eta * 2.0)
    assert math.isclose(p1 - p0, +eta * 2.0)
    assert math.isclose((rho1 + p1), (rho0 + p0))


def test_exchange_partition_matches_bianchi_sum():
    eta, up = 0.42, 9.0
    assert math.isclose(interaction_lagrangian_derivative(eta, up), eta * up)
    assert math.isclose(kinetic_divergence_coefficient(eta, up), (1.0 - eta) * up)
    assert math.isclose(total_nonvacuum_divergence_coefficient(eta, up), up)


def test_eta_zero_is_rf_l2_scalar_eom_and_mass():
    assert minimal_common_potential_coefficient(0.0) == 1.0
    assert effective_scalar_mass_sq(0.0, 7.0) == 7.0
    assert kinetic_divergence_coefficient(0.0, 5.0) == 5.0


def test_eta_one_is_rf_f7_all_generator_allocation_minimal_degeneracy():
    assert minimal_common_potential_coefficient(1.0) == 0.0
    assert effective_scalar_mass_sq(1.0, 7.0) == 0.0
    assert kinetic_divergence_coefficient(1.0, 5.0) == 0.0
    assert interaction_lagrangian_derivative(1.0, 5.0) == 5.0


def test_dynamic_lambda_uses_only_uhat_after_reference_absorption():
    state = vacuum_reference_state(1.5, 2.0, 4.0, 6.0)
    assert state.lambda_star == 21.5
    assert dynamic_lambda(state.lambda_star, 2.0, 3.0) == 27.5


def test_sourced_fixed_x_solution_satisfies_transport_ode_numerically():
    K0 = 2.3
    x = 0.4
    eta = 0.35
    rho_c = 1.7

    def U(y):
        return 0.8 * math.exp(0.7 * y)

    def K(y):
        return K0 * math.exp(4.0 * y)

    def v(y):
        return (1.0 - x) / 2.0 + rho_c / K(y) - eta * U(y) / K(y)

    y = 0.3
    h = 1e-6
    dv = (v(y + h) - v(y - h)) / (2.0 * h)
    du = 0.7 * U(y)
    rhs = source_modified_transport_rhs(x, v(y), eta, K(y), du)
    assert math.isclose(dv, rhs, rel_tol=2e-6, abs_tol=2e-6)


def test_fail_closed_nonfinite_and_eta_range():
    with pytest.raises(VacuumSplitError):
        exchange_partition(-0.1)
    with pytest.raises(VacuumSplitError):
        exchange_partition(1.1)
    with pytest.raises(VacuumSplitError):
        source_modified_transport_rhs(0.0, 0.0, 0.5, 0.0, 0.0)
    with pytest.raises(VacuumSplitError):
        vacuum_split_invariant(0.0, float("nan"), 0.0, 0.0)
