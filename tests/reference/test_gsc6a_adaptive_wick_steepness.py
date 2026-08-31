import pytest

from src.rfc.adaptive_wick_steepness import (
    adaptive_scale,
    adaptive_wick_norm_sq,
    certify_adaptive_global_promotion,
    certify_adaptive_steepness,
)


def test_adaptive_scale_is_positive_for_positive_lapse():
    assert adaptive_scale(2.0) == pytest.approx(0.2)


def test_null_boundary_saturates_adaptive_steepness():
    # h(Y,Y)=N^2 a^2 -> H_N(v,v)=a^2 exactly.
    result = certify_adaptive_steepness(lapse=3.0, dt_value=2.0, spatial_norm_sq=36.0)
    assert result.passed is True
    assert result.adaptive_norm_sq == pytest.approx(4.0)
    assert result.steepness_defect == pytest.approx(0.0)


def test_timelike_vector_is_strictly_steep():
    result = certify_adaptive_steepness(lapse=2.0, dt_value=1.0, spatial_norm_sq=1.0)
    assert result.passed is True
    assert result.adaptive_norm_sq < 1.0


def test_large_finite_lapse_needs_no_global_nmax_for_pointwise_bound():
    result = certify_adaptive_steepness(lapse=1.0e6, dt_value=1.0, spatial_norm_sq=1.0e12)
    assert result.passed is True
    assert result.adaptive_norm_sq == pytest.approx(1.0)


def test_causal_violation_is_reported():
    result = certify_adaptive_steepness(lapse=1.0, dt_value=1.0, spatial_norm_sq=1.1)
    assert result.passed is False
    assert result.causal_defect > 0.0


def test_future_orientation_fails_closed():
    with pytest.raises(ValueError, match="dt\(v\)>0"):
        certify_adaptive_steepness(lapse=1.0, dt_value=0.0, spatial_norm_sq=0.0)


def test_nonpositive_lapse_fails_closed():
    with pytest.raises(ValueError):
        adaptive_wick_norm_sq(0.0, 1.0, 0.0)


def test_global_route_requires_complete_adaptive_metric():
    blocked = certify_adaptive_global_promotion(
        global_lorentzian_carrier=True,
        global_regular_clock=True,
        adaptive_metric_complete=False,
    )
    assert blocked["global_hyperbolicity_eligible"] is False
    assert blocked["global_lapse_upper_bound_required_on_this_route"] is False
    assert blocked["adaptive_metric_completeness_required"] is True


def test_complete_adaptive_metric_closes_pure_causal_geometry_route():
    passed = certify_adaptive_global_promotion(
        global_lorentzian_carrier=True,
        global_regular_clock=True,
        adaptive_metric_complete=True,
    )
    assert passed["global_hyperbolicity_eligible"] is True
    assert passed["global_gr_cauchy_carrier_eligible"] is False


def test_full_gr_cauchy_bit_remains_separate():
    passed = certify_adaptive_global_promotion(
        global_lorentzian_carrier=True,
        global_regular_clock=True,
        adaptive_metric_complete=True,
        global_einstein_carrier=True,
    )
    assert passed["global_gr_cauchy_carrier_eligible"] is True
    assert passed["nonlinear_global_stability_promoted"] is False
