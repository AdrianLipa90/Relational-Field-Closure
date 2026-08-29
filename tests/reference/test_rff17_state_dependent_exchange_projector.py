import math

import pytest

from src.rfc.state_dependent_exchange_projector import (
    ExchangeProjectorError,
    clock_projector_metric_derivative,
    dust_normalization_slope,
    eta_one_clock_stress,
    exchange_derivative_on_surface,
    metric_derivative_is_nontrivial,
    net_potential_stress_on_surface,
    scalar_potential_force_coefficient_on_surface,
)


MINKOWSKI = (
    (-1.0, 0.0, 0.0, 0.0),
    (0.0, 1.0, 0.0, 0.0),
    (0.0, 0.0, 1.0, 0.0),
    (0.0, 0.0, 0.0, 1.0),
)


def test_projector_surface_preserves_rf_f13_exchange_derivative():
    assert exchange_derivative_on_surface(0.4, 7.0, 1.0) == pytest.approx(2.8)


def test_eta_zero_recovers_rf_l2_force_coefficient():
    assert scalar_potential_force_coefficient_on_surface(0.0) == 1.0


def test_eta_one_with_f1_one_removes_metric_potential_force():
    assert scalar_potential_force_coefficient_on_surface(1.0, 1.0) == 0.0


def test_metric_independent_projector_reduces_to_rff16_minimal_counterterm():
    zero = tuple(tuple(0.0 for _ in range(4)) for _ in range(4))
    T = net_potential_stress_on_surface(5.0, 1.0, 1.0, 3.0, MINKOWSKI, zero)
    assert all(abs(v) < 1e-15 for row in T for v in row)


def test_clock_projector_has_rank_one_metric_derivative():
    u_cov = (-1.0, 0.0, 0.0, 0.0)
    dc = clock_projector_metric_derivative(u_cov)
    assert dc[0][0] == -1.0
    assert sum(abs(v) for row in dc for v in row) == 1.0


def test_eta_one_clock_projector_produces_pressureless_rank_one_stress():
    u_cov = (-1.0, 0.0, 0.0, 0.0)
    T = eta_one_clock_stress(6.0, 0.5, u_cov)
    assert T[0][0] == pytest.approx(6.0)
    assert T[1][1] == 0.0
    assert T[2][2] == 0.0
    assert T[3][3] == 0.0


def test_clock_projector_general_slope_sets_dust_density():
    u_cov = (-1.0, 0.0, 0.0, 0.0)
    slope = 0.75
    U = 4.0
    T = eta_one_clock_stress(U, slope, u_cov)
    assert T[0][0] == pytest.approx(2.0 * slope * U)


def test_dust_normalization_slope_half_gives_rho_equal_u():
    assert dust_normalization_slope(1.0) == 0.5
    assert dust_normalization_slope(2.0) == 1.0


def test_general_stress_formula_matches_clock_specialization():
    U = 3.0
    slope = 0.5
    u_cov = (-1.0, 0.0, 0.0, 0.0)
    dc = clock_projector_metric_derivative(u_cov)
    generic = net_potential_stress_on_surface(U, 1.0, 1.0, slope, MINKOWSKI, dc)
    clock = eta_one_clock_stress(U, slope, u_cov)
    assert generic == clock


def test_nontrivial_gate_detects_metric_sensitivity():
    zero = tuple(tuple(0.0 for _ in range(4)) for _ in range(4))
    assert not metric_derivative_is_nontrivial(zero)
    assert metric_derivative_is_nontrivial(clock_projector_metric_derivative((-1.0, 0.0, 0.0, 0.0)))


def test_fail_closed_inputs():
    with pytest.raises(ExchangeProjectorError):
        exchange_derivative_on_surface(1.1, 1.0)
    with pytest.raises(ExchangeProjectorError):
        clock_projector_metric_derivative((1.0, 2.0))
    with pytest.raises(ExchangeProjectorError):
        dust_normalization_slope(float("nan"))
    with pytest.raises(ExchangeProjectorError):
        metric_derivative_is_nontrivial(((0.0,),), atol=0.0)
