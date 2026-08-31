import math

import pytest

from src.rfc.matching_flow_extrinsic_curvature import (
    MatchingFlowExtrinsicCurvatureError,
    certify_matching_flow_extrinsic_curvature,
    dragged_coordinate_metric_rate,
    extrinsic_curvature_from_matching_flow,
    matching_lie_metric,
    unit_normal_lie_metric,
)


def test_matching_lie_metric_keeps_nonzero_shift_terms():
    dt_h = ((4.0, 1.0, 0.0), (1.0, 2.0, 0.5), (0.0, 0.5, -2.0))
    sym_db = ((2.0, 0.5, 0.0), (0.5, -2.0, 0.5), (0.0, 0.5, 0.0))
    assert matching_lie_metric(dt_h, sym_db) == (
        (2.0, 0.5, 0.0),
        (0.5, 4.0, 0.0),
        (0.0, 0.0, -2.0),
    )


def test_extrinsic_curvature_matches_declared_sign_convention():
    dt_h = ((2.0, 0.0, 0.0), (0.0, -2.0, 0.0), (0.0, 0.0, 4.0))
    sym_db = ((4.0, 0.0, 0.0), (0.0, 2.0, 0.0), (0.0, 0.0, 0.0))
    k = extrinsic_curvature_from_matching_flow(dt_h, sym_db, 2.0)
    assert k == ((0.5, 0.0, 0.0), (0.0, 1.0, 0.0), (0.0, 0.0, -1.0))


def test_unit_normal_identity_is_minus_two_k():
    dt_h = ((1.0, 0.2, 0.0), (0.2, 2.0, 0.0), (0.0, 0.0, 3.0))
    sym_db = ((0.0, 0.0, 0.0), (0.0, 1.0, 0.0), (0.0, 0.0, 1.0))
    lapse = 1.25
    lie_n = unit_normal_lie_metric(dt_h, sym_db, lapse)
    k = extrinsic_curvature_from_matching_flow(dt_h, sym_db, lapse)
    for i in range(3):
        for j in range(3):
            assert lie_n[i][j] == pytest.approx(-2.0 * k[i][j])


def test_dragged_coordinates_zero_shift_preserve_nonzero_extrinsic_curvature():
    k = ((1.0, 0.2, 0.0), (0.2, -0.5, 0.0), (0.0, 0.0, 0.25))
    rate = dragged_coordinate_metric_rate(k, 3.0)
    expected = ((-6.0, -1.2, 0.0), (-1.2, 3.0, 0.0), (0.0, 0.0, -1.5))
    for i in range(3):
        for j in range(3):
            assert rate[i][j] == pytest.approx(expected[i][j])
    assert any(abs(rate[i][j]) > 0.0 for i in range(3) for j in range(3))


def test_zero_shift_is_a_coordinate_gauge_not_k_zero():
    dt_h = ((-2.0, 0.0, 0.0), (0.0, -4.0, 0.0), (0.0, 0.0, 2.0))
    sym_db = ((0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0))
    cert = certify_matching_flow_extrinsic_curvature(dt_h, sym_db, 1.0)
    assert cert.shift_zero_is_coordinate_gauge is True
    assert cert.extrinsic_curvature == (
        (1.0, 0.0, 0.0),
        (0.0, 2.0, 0.0),
        (0.0, 0.0, -1.0),
    )


def test_certificate_separates_kinematic_pass_from_production_inputs():
    cert = certify_matching_flow_extrinsic_curvature(
        ((0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0)),
        ((2.0, 0.0, 0.0), (0.0, 4.0, 0.0), (0.0, 0.0, 6.0)),
        2.0,
    )
    assert cert.status == "PASS_RFC_GSC3B_MATCHING_FLOW_EXTRINSIC_CURVATURE_KINEMATIC_SEAM"
    assert cert.production_matching_flow == "UPSTREAM_GSC3A_OPEN_INPUT"
    assert cert.physical_event_placement == "UPSTREAM_OPEN_INPUT"
    assert cert.defining_identity_defect == 0.0
    assert cert.unit_normal_identity_defect == 0.0


@pytest.mark.parametrize("bad_lapse", [0.0, -1.0, float("nan"), float("inf")])
def test_nonpositive_or_nonfinite_lapse_fails_closed(bad_lapse):
    z = ((0.0, 0.0, 0.0),) * 3
    with pytest.raises(MatchingFlowExtrinsicCurvatureError):
        extrinsic_curvature_from_matching_flow(z, z, bad_lapse)


def test_asymmetric_metric_rate_fails_closed():
    bad = ((0.0, 1.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0))
    z = ((0.0, 0.0, 0.0),) * 3
    with pytest.raises(MatchingFlowExtrinsicCurvatureError):
        matching_lie_metric(bad, z)


def test_nonfinite_tensor_entry_fails_closed():
    bad = ((math.nan, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0))
    z = ((0.0, 0.0, 0.0),) * 3
    with pytest.raises(MatchingFlowExtrinsicCurvatureError):
        matching_lie_metric(bad, z)
