import pytest

from src.rfc.open_interval_product_proper_clock import (
    OpenInterval,
    certify_open_interval_product_route,
)


@pytest.mark.parametrize(
    ("interval", "x"),
    [
        (OpenInterval(), 0.25),
        (OpenInterval(left=2.0), 3.5),
        (OpenInterval(right=-1.0), -2.5),
        (OpenInterval(left=0.0, right=1.0), 0.3),
    ],
)
def test_canonical_open_interval_maps_are_orientation_preserving_diffeomorphisms(interval, x):
    y = interval.to_real(x)
    assert interval.derivative(x) > 0.0
    assert interval.from_real(y) == pytest.approx(x)


def test_bounded_interval_logit_reaches_both_real_directions():
    interval = OpenInterval(left=0.0, right=1.0)
    assert interval.to_real(1.0e-6) < -10.0
    assert interval.to_real(1.0 - 1.0e-6) > 10.0


def test_half_line_maps_cover_real_line():
    right_half = OpenInterval(left=0.0)
    left_half = OpenInterval(right=0.0)
    assert right_half.from_real(-8.0) > 0.0
    assert right_half.from_real(8.0) > right_half.from_real(-8.0)
    assert left_half.from_real(-8.0) < left_half.from_real(8.0) < 0.0


def test_invalid_or_closed_interval_data_fail_closed():
    with pytest.raises(ValueError):
        OpenInterval(left=1.0, right=1.0)
    with pytest.raises(ValueError):
        OpenInterval(left=2.0, right=1.0)
    interval = OpenInterval(left=0.0, right=1.0)
    with pytest.raises(ValueError):
        interval.to_real(0.0)
    with pytest.raises(ValueError):
        interval.to_real(1.0)


def test_finite_a5_flow_derived_product_derives_proper_real_clock_and_gsc6b_route():
    route = certify_open_interval_product_route(
        interval=OpenInterval(left=0.0, right=1.0),
        finite_a5_spatial_carrier=True,
        a5_closed_3manifold_certified=True,
        global_product_trivialization=True,
        product_trivialization_provenance="FLOW_COVERAGE",
        global_regular_product_clock=True,
        global_lorentzian_carrier=True,
        smooth_finite_positive_lapse=True,
    )
    assert route.compact_spatial_fiber_derived is True
    assert route.product_provenance_independent_of_proper_clock is True
    assert route.orientation_preserving_interval_diffeomorphism_derived is True
    assert route.proper_real_temporal_clock_derived is True
    assert route.proper_clock_route.wick_complete_derived is True
    assert route.global_hyperbolicity_eligible is True


def test_clock_properness_derived_product_is_rejected_by_circularity_firewall():
    route = certify_open_interval_product_route(
        interval=OpenInterval(),
        finite_a5_spatial_carrier=True,
        a5_closed_3manifold_certified=True,
        global_product_trivialization=True,
        product_trivialization_provenance="CLOCK_PROPERNESS",
        global_regular_product_clock=True,
        global_lorentzian_carrier=True,
        smooth_finite_positive_lapse=True,
    )
    assert route.product_provenance_independent_of_proper_clock is False
    assert route.proper_real_temporal_clock_derived is False
    assert route.global_hyperbolicity_eligible is False


def test_independent_source_receipt_requires_explicit_no_proper_clock_ancestry():
    blocked = certify_open_interval_product_route(
        interval=OpenInterval(),
        finite_a5_spatial_carrier=True,
        a5_closed_3manifold_certified=True,
        global_product_trivialization=True,
        product_trivialization_provenance="INDEPENDENT_SOURCE_RECEIPT",
        independent_product_no_proper_clock_ancestry=False,
        global_regular_product_clock=True,
        global_lorentzian_carrier=True,
        smooth_finite_positive_lapse=True,
    )
    admitted = certify_open_interval_product_route(
        interval=OpenInterval(),
        finite_a5_spatial_carrier=True,
        a5_closed_3manifold_certified=True,
        global_product_trivialization=True,
        product_trivialization_provenance="INDEPENDENT_SOURCE_RECEIPT",
        independent_product_no_proper_clock_ancestry=True,
        global_regular_product_clock=True,
        global_lorentzian_carrier=True,
        smooth_finite_positive_lapse=True,
    )
    assert blocked.proper_real_temporal_clock_derived is False
    assert admitted.proper_real_temporal_clock_derived is True


def test_unknown_product_provenance_keeps_reduction_closed():
    route = certify_open_interval_product_route(
        interval=OpenInterval(),
        finite_a5_spatial_carrier=True,
        a5_closed_3manifold_certified=True,
        global_product_trivialization=True,
        product_trivialization_provenance="UNKNOWN",
        global_regular_product_clock=True,
        global_lorentzian_carrier=True,
        smooth_finite_positive_lapse=True,
    )
    assert route.product_provenance_independent_of_proper_clock is False
    assert route.proper_real_temporal_clock_derived is False


def test_unsupported_product_provenance_fails_closed():
    with pytest.raises(ValueError):
        certify_open_interval_product_route(
            interval=OpenInterval(),
            finite_a5_spatial_carrier=True,
            a5_closed_3manifold_certified=True,
            global_product_trivialization=True,
            product_trivialization_provenance="UNDECLARED_ROUTE",
            global_regular_product_clock=True,
            global_lorentzian_carrier=True,
            smooth_finite_positive_lapse=True,
        )


def test_locally_finite_or_unfrozen_spatial_carrier_does_not_get_compactness_for_free():
    route = certify_open_interval_product_route(
        interval=OpenInterval(),
        finite_a5_spatial_carrier=False,
        a5_closed_3manifold_certified=True,
        global_product_trivialization=True,
        product_trivialization_provenance="FLOW_COVERAGE",
        global_regular_product_clock=True,
        global_lorentzian_carrier=True,
        smooth_finite_positive_lapse=True,
    )
    assert route.compact_spatial_fiber_derived is False
    assert route.proper_real_temporal_clock_derived is False
    assert route.global_hyperbolicity_eligible is False


def test_a5_certificate_is_required_for_compact_spatial_parent():
    route = certify_open_interval_product_route(
        interval=OpenInterval(left=0.0),
        finite_a5_spatial_carrier=True,
        a5_closed_3manifold_certified=False,
        global_product_trivialization=True,
        product_trivialization_provenance="FLOW_COVERAGE",
        global_regular_product_clock=True,
        global_lorentzian_carrier=True,
        smooth_finite_positive_lapse=True,
    )
    assert route.compact_spatial_fiber_derived is False
    assert route.proper_real_temporal_clock_derived is False


def test_local_product_charts_do_not_promote_global_properness():
    route = certify_open_interval_product_route(
        interval=OpenInterval(right=0.0),
        finite_a5_spatial_carrier=True,
        a5_closed_3manifold_certified=True,
        global_product_trivialization=False,
        product_trivialization_provenance="FLOW_COVERAGE",
        global_regular_product_clock=True,
        global_lorentzian_carrier=True,
        smooth_finite_positive_lapse=True,
    )
    assert route.proper_real_temporal_clock_derived is False
    assert route.global_hyperbolicity_eligible is False


def test_gr_cauchy_composition_stays_separate():
    route = certify_open_interval_product_route(
        interval=OpenInterval(),
        finite_a5_spatial_carrier=True,
        a5_closed_3manifold_certified=True,
        global_product_trivialization=True,
        product_trivialization_provenance="FLOW_COVERAGE",
        global_regular_product_clock=True,
        global_lorentzian_carrier=True,
        smooth_finite_positive_lapse=True,
        global_einstein_carrier=True,
    )
    assert route.global_hyperbolicity_eligible is True
    assert route.global_gr_cauchy_carrier_eligible is True
