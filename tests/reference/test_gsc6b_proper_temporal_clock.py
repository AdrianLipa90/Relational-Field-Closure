import pytest

from src.rfc.proper_temporal_clock_global_hyperbolicity import (
    certify_product_projection_properness,
    certify_proper_clock_route,
    wick_dominates_clock,
    wick_norm_sq,
)


def test_wick_metric_dominates_clock_component():
    assert wick_norm_sq(2.0, 3.0) == pytest.approx(7.0)
    assert wick_dominates_clock(2.0, 3.0) is True


def test_proper_clock_derives_wick_completeness_and_steep_reparametrization():
    result = certify_proper_clock_route(
        global_lorentzian_carrier=True,
        global_regular_temporal_clock=True,
        proper_temporal_clock_to_real_line=True,
        smooth_finite_positive_lapse=True,
    )
    assert result.proper_temporal_clock is True
    assert result.wick_complete_derived is True
    assert result.smooth_slice_lapse_majorant_derived is True
    assert result.steep_reparametrization_derived is True
    assert result.global_hyperbolicity_eligible is True


def test_properness_is_fail_closed_global_input():
    result = certify_proper_clock_route(
        global_lorentzian_carrier=True,
        global_regular_temporal_clock=True,
        proper_temporal_clock_to_real_line=False,
        smooth_finite_positive_lapse=True,
    )
    assert result.wick_complete_derived is False
    assert result.global_hyperbolicity_eligible is False


def test_smooth_finite_lapse_is_needed_for_majorant_route():
    result = certify_proper_clock_route(
        global_lorentzian_carrier=True,
        global_regular_temporal_clock=True,
        proper_temporal_clock_to_real_line=True,
        smooth_finite_positive_lapse=False,
    )
    assert result.wick_complete_derived is True
    assert result.smooth_slice_lapse_majorant_derived is False
    assert result.global_hyperbolicity_eligible is False


def test_gr_cauchy_bit_stays_separate():
    result = certify_proper_clock_route(
        global_lorentzian_carrier=True,
        global_regular_temporal_clock=True,
        proper_temporal_clock_to_real_line=True,
        smooth_finite_positive_lapse=True,
        global_einstein_carrier=True,
    )
    assert result.global_hyperbolicity_eligible is True
    assert result.global_gr_cauchy_carrier_eligible is True


def test_compact_spatial_product_makes_projection_proper():
    receipt = certify_product_projection_properness(
        global_product_trivialization=True,
        time_axis_is_real_line=True,
        spatial_fiber_compact=True,
    )
    assert receipt["product_clock_proper"] is True
    assert receipt["global_hyperbolicity_promoted"] is False


def test_noncompact_spatial_product_does_not_get_properness_for_free():
    receipt = certify_product_projection_properness(
        global_product_trivialization=True,
        time_axis_is_real_line=True,
        spatial_fiber_compact=False,
    )
    assert receipt["product_clock_proper"] is False


def test_missing_global_product_trivialization_keeps_corollary_open():
    receipt = certify_product_projection_properness(
        global_product_trivialization=False,
        time_axis_is_real_line=True,
        spatial_fiber_compact=True,
    )
    assert receipt["product_clock_proper"] is False


def test_negative_spatial_norm_fails_closed():
    with pytest.raises(ValueError):
        wick_norm_sq(1.0, -1.0)
