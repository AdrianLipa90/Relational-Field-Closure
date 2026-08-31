import math
import pytest

from src.rfc.compact_fiber_open_interval_proper_clock import (
    OpenInterval,
    certify_compact_fiber_product_route,
    interval_to_real,
    interval_to_real_derivative,
)


@pytest.mark.parametrize(
    "interval,x",
    [
        (OpenInterval(), 0.25),
        (OpenInterval(lower=1.0), 2.5),
        (OpenInterval(upper=3.0), 1.5),
        (OpenInterval(lower=-2.0, upper=5.0), 1.0),
    ],
)
def test_all_open_interval_types_map_smoothly_to_real_line(interval, x):
    y = interval_to_real(x, interval)
    dy = interval_to_real_derivative(x, interval)
    assert math.isfinite(y)
    assert math.isfinite(dy)
    assert dy > 0.0


def test_finite_interval_map_diverges_with_correct_orientation():
    interval = OpenInterval(lower=0.0, upper=1.0)
    assert interval_to_real(1e-9, interval) < -10.0
    assert interval_to_real(1.0 - 1e-9, interval) > 10.0
    assert interval_to_real_derivative(0.25, interval) > 0.0
    assert interval_to_real_derivative(0.75, interval) > 0.0


def test_half_line_maps_cover_both_real_directions():
    right = OpenInterval(lower=0.0)
    left = OpenInterval(upper=0.0)
    assert interval_to_real(1e-9, right) < -10.0
    assert interval_to_real(math.exp(12.0), right) > 10.0
    assert interval_to_real(-math.exp(12.0), left) < -10.0
    assert interval_to_real(-1e-9, left) > 10.0


def test_interval_validation_and_domain_checks_fail_closed():
    with pytest.raises(ValueError):
        OpenInterval(lower=1.0, upper=1.0)
    with pytest.raises(ValueError):
        OpenInterval(lower=2.0, upper=1.0)
    interval = OpenInterval(lower=0.0, upper=1.0)
    with pytest.raises(ValueError):
        interval_to_real(0.0, interval)
    with pytest.raises(ValueError):
        interval_to_real(1.0, interval)
    with pytest.raises(ValueError):
        interval_to_real_derivative(float("nan"), interval)


def test_compact_fiber_product_derives_gsc6b_proper_clock_input():
    route = certify_compact_fiber_product_route(
        global_product_trivialization=True,
        global_regular_clock=True,
        spatial_fiber_compact=True,
        rf_e25_global_lorentzian_adm_carrier=True,
        smooth_finite_positive_lapse=True,
    )
    assert route.open_interval_clock_derived
    assert route.compact_spatial_fiber_admitted
    assert route.proper_real_clock_derived
    assert route.temporal_orientation_preserved
    assert route.gsc6b_proper_clock_input_derived
    assert route.global_hyperbolicity_eligible
    assert not route.global_gr_cauchy_carrier_eligible


def test_global_gr_cauchy_bit_requires_global_einstein_carrier():
    route = certify_compact_fiber_product_route(
        global_product_trivialization=True,
        global_regular_clock=True,
        spatial_fiber_compact=True,
        rf_e25_global_lorentzian_adm_carrier=True,
        smooth_finite_positive_lapse=True,
        global_einstein_carrier=True,
    )
    assert route.global_gr_cauchy_carrier_eligible


@pytest.mark.parametrize(
    "overrides",
    [
        {"global_product_trivialization": False},
        {"global_regular_clock": False},
        {"spatial_fiber_compact": False},
        {"rf_e25_global_lorentzian_adm_carrier": False},
        {"smooth_finite_positive_lapse": False},
    ],
)
def test_route_preserves_parent_gates(overrides):
    kwargs = dict(
        global_product_trivialization=True,
        global_regular_clock=True,
        spatial_fiber_compact=True,
        rf_e25_global_lorentzian_adm_carrier=True,
        smooth_finite_positive_lapse=True,
    )
    kwargs.update(overrides)
    route = certify_compact_fiber_product_route(**kwargs)
    assert route.global_hyperbolicity_eligible is False
