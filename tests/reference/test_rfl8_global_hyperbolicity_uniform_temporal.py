import math

import pytest

from src.rfc.global_hyperbolicity_uniform_temporal import (
    GlobalHyperbolicityWitnessError,
    certify_causal_vector_steepness,
    certify_global_hyperbolicity,
    uniform_temporal_scale,
)


def test_uniform_temporal_scale_is_exact_formula():
    assert uniform_temporal_scale(2.0) == pytest.approx(1.0 / math.sqrt(5.0))


def test_null_boundary_saturates_steepness_at_global_lapse_bound():
    # N=Nmax=2, a=3, q=N^2 a^2=36 gives
    # W=45 and epsilon*sqrt(W)=3=a exactly.
    cert = certify_causal_vector_steepness(
        lapse=2.0,
        lapse_upper_bound=2.0,
        dt_component=3.0,
        shifted_spatial_norm_sq=36.0,
    )
    assert cert.causal_margin == pytest.approx(0.0)
    assert cert.scaled_wick_norm == pytest.approx(3.0)
    assert cert.steepness_margin == pytest.approx(0.0, abs=1e-12)
    assert cert.steepness_pass


def test_timelike_vector_has_positive_steepness_margin():
    cert = certify_causal_vector_steepness(
        lapse=1.0,
        lapse_upper_bound=2.0,
        dt_component=2.0,
        shifted_spatial_norm_sq=1.0,
    )
    assert cert.causal_margin > 0.0
    assert cert.steepness_margin > 0.0


def test_shift_is_already_absorbed_into_shifted_spatial_norm():
    # RF-L8 only needs h(Y,Y), Y=X+b*a, so no separate bound on b is used
    # in the causal-to-Wick estimate.
    cert = certify_causal_vector_steepness(
        lapse=1.5,
        lapse_upper_bound=1.5,
        dt_component=4.0,
        shifted_spatial_norm_sq=9.0,
    )
    assert cert.wick_norm_sq == pytest.approx(25.0)
    assert cert.causal


def test_local_lapse_above_declared_global_bound_fails_closed():
    with pytest.raises(GlobalHyperbolicityWitnessError, match="exceeds declared global upper bound"):
        certify_causal_vector_steepness(
            lapse=2.1,
            lapse_upper_bound=2.0,
            dt_component=1.0,
            shifted_spatial_norm_sq=0.0,
        )


def test_spacelike_vector_declared_causal_fails_closed():
    with pytest.raises(GlobalHyperbolicityWitnessError, match="violates ADM causal inequality"):
        certify_causal_vector_steepness(
            lapse=1.0,
            lapse_upper_bound=2.0,
            dt_component=1.0,
            shifted_spatial_norm_sq=1.5,
        )


@pytest.mark.parametrize("bad_dt", [0.0, -1.0, float("inf"), float("nan")])
def test_future_causal_orientation_requires_positive_finite_dt(bad_dt):
    with pytest.raises(GlobalHyperbolicityWitnessError):
        certify_causal_vector_steepness(
            lapse=1.0,
            lapse_upper_bound=2.0,
            dt_component=bad_dt,
            shifted_spatial_norm_sq=0.0,
        )


@pytest.mark.parametrize("bad_bound", [0.0, -1.0, float("inf"), float("nan")])
def test_invalid_lapse_upper_bound_fails_closed(bad_bound):
    with pytest.raises(GlobalHyperbolicityWitnessError):
        uniform_temporal_scale(bad_bound)


def test_global_hyperbolicity_promotes_only_when_all_geometry_witnesses_are_supplied():
    cert = certify_global_hyperbolicity(
        3.0,
        global_lorentzian_carrier_supplied=True,
        global_regular_clock_supplied=True,
        global_lapse_upper_bound_certified=True,
        wick_metric_complete_supplied=True,
    )
    assert cert.completely_uniform_temporal
    assert cert.global_hyperbolicity
    assert cert.cauchy_foliation
    assert not cert.global_gr_cauchy_carrier


@pytest.mark.parametrize(
    "missing",
    [
        "carrier",
        "clock",
        "bound",
        "complete",
    ],
)
def test_each_global_geometry_witness_is_fail_closed(missing):
    kwargs = {
        "global_lorentzian_carrier_supplied": True,
        "global_regular_clock_supplied": True,
        "global_lapse_upper_bound_certified": True,
        "wick_metric_complete_supplied": True,
    }
    key = {
        "carrier": "global_lorentzian_carrier_supplied",
        "clock": "global_regular_clock_supplied",
        "bound": "global_lapse_upper_bound_certified",
        "complete": "wick_metric_complete_supplied",
    }[missing]
    kwargs[key] = False
    cert = certify_global_hyperbolicity(2.0, **kwargs)
    assert not cert.completely_uniform_temporal
    assert not cert.global_hyperbolicity
    assert not cert.cauchy_foliation


def test_full_gr_cauchy_carrier_additionally_requires_global_einstein_carrier():
    cert = certify_global_hyperbolicity(
        2.0,
        global_lorentzian_carrier_supplied=True,
        global_regular_clock_supplied=True,
        global_lapse_upper_bound_certified=True,
        wick_metric_complete_supplied=True,
        global_einstein_carrier_supplied=True,
    )
    assert cert.global_hyperbolicity
    assert cert.global_gr_cauchy_carrier


def test_global_einstein_carrier_alone_cannot_promote_global_hyperbolicity():
    cert = certify_global_hyperbolicity(
        2.0,
        global_einstein_carrier_supplied=True,
    )
    assert not cert.global_hyperbolicity
    assert not cert.global_gr_cauchy_carrier


def test_nonlinear_global_stability_remains_separate():
    cert = certify_global_hyperbolicity(
        1.0,
        global_lorentzian_carrier_supplied=True,
        global_regular_clock_supplied=True,
        global_lapse_upper_bound_certified=True,
        wick_metric_complete_supplied=True,
        global_einstein_carrier_supplied=True,
    )
    assert cert.nonlinear_global_stability == "OPEN_SEPARATE_GATE"
