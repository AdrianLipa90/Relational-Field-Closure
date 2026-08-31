from __future__ import annotations

import pytest

from src.rfc.clock_transverse_matching_flow import (
    ClockTransverseMatchingFlowError,
    EventClockAnchor,
    MatchingPatch,
    MatchingTransition,
    certify_clock_transverse_matching_flow,
    clock_transverse_pairing,
    expected_target_shift,
    matmul3,
    matvec3,
    add3,
)

I = ((1.0, 0.0, 0.0), (0.0, 1.0, 0.0), (0.0, 0.0, 1.0))


def test_clock_transverse_pairing_is_exact():
    dt_value, spatial = clock_transverse_pairing((2.0, -3.0, 5.0))
    assert dt_value == 1.0
    assert spatial == (0.0, 0.0, 0.0)


def test_time_dependent_overlap_uses_minus_drift_sign():
    transition = MatchingTransition("p", "q", I, (0.5, -1.0, 2.0))
    source = (3.0, 4.0, 5.0)
    assert expected_target_shift(transition, source) == (2.5, 5.0, 3.0)
    cert = certify_clock_transverse_matching_flow(
        [MatchingPatch("p", source), MatchingPatch("q", (2.5, 5.0, 3.0))],
        [transition],
    )
    assert cert.compatible
    assert cert.max_shift_overlap_residual == 0.0


def test_plus_drift_sign_is_rejected():
    transition = MatchingTransition("p", "q", I, (0.5, -1.0, 2.0))
    with pytest.raises(ClockTransverseMatchingFlowError, match="overlap law failed"):
        certify_clock_transverse_matching_flow(
            [MatchingPatch("p", (3.0, 4.0, 5.0)), MatchingPatch("q", (3.5, 3.0, 7.0))],
            [transition],
        )


def test_triple_overlap_closes_matching_field_and_coordinate_cocycle():
    a_qp = ((2.0, 0.0, 0.0), (0.0, 1.0, 0.0), (0.0, 0.0, 1.0))
    a_rq = ((1.0, 0.0, 0.0), (0.0, 3.0, 0.0), (0.0, 0.0, 1.0))
    v_qp = (1.0, 0.5, -0.5)
    v_rq = (-2.0, 1.0, 0.25)
    a_rp = matmul3(a_rq, a_qp)
    v_rp = add3(v_rq, matvec3(a_rq, v_qp))
    b_p = (2.0, -1.0, 4.0)
    b_q = expected_target_shift(MatchingTransition("p", "q", a_qp, v_qp), b_p)
    b_r = expected_target_shift(MatchingTransition("q", "r", a_rq, v_rq), b_q)
    transitions = [
        MatchingTransition("p", "q", a_qp, v_qp),
        MatchingTransition("q", "r", a_rq, v_rq),
        MatchingTransition("p", "r", a_rp, v_rp),
    ]
    cert = certify_clock_transverse_matching_flow(
        [MatchingPatch("p", b_p), MatchingPatch("q", b_q), MatchingPatch("r", b_r)],
        transitions,
        triangles=[("p", "q", "r")],
    )
    assert cert.max_transition_cocycle_residual == 0.0
    assert cert.max_time_drift_cocycle_residual == 0.0
    assert cert.max_shift_overlap_residual == 0.0


def test_event_anchors_share_one_additive_calibration():
    cert = certify_clock_transverse_matching_flow(
        [MatchingPatch("p", (0.0, 0.0, 0.0))],
        [],
        event_anchors=[
            EventClockAnchor("e0", 0.0, 7.5),
            EventClockAnchor("e1", 2.0, 9.5),
            EventClockAnchor("e2", 5.0, 12.5),
        ],
    )
    assert cert.additive_clock_offset == 7.5
    assert cert.max_event_anchor_residual == 0.0


def test_inconsistent_event_clock_calibration_is_rejected():
    with pytest.raises(ClockTransverseMatchingFlowError, match="more than one additive calibration"):
        certify_clock_transverse_matching_flow(
            [MatchingPatch("p", (0.0, 0.0, 0.0))],
            [],
            event_anchors=[EventClockAnchor("e0", 0.0, 1.0), EventClockAnchor("e1", 2.0, 3.25)],
        )


def test_unknown_patch_transition_is_rejected():
    with pytest.raises(ClockTransverseMatchingFlowError, match="unknown patch"):
        certify_clock_transverse_matching_flow(
            [MatchingPatch("p", (0.0, 0.0, 0.0))],
            [MatchingTransition("p", "q", I, (0.0, 0.0, 0.0))],
        )


def test_disconnected_matching_atlas_is_rejected_for_connected_claim():
    with pytest.raises(ClockTransverseMatchingFlowError, match="disconnected patches"):
        certify_clock_transverse_matching_flow(
            [MatchingPatch("p", (0.0, 0.0, 0.0)), MatchingPatch("q", (0.0, 0.0, 0.0))],
            [],
        )


def test_certificate_keeps_global_coverage_and_event_placement_typed_open():
    cert = certify_clock_transverse_matching_flow([MatchingPatch("p", (0.0, 0.0, 0.0))], [])
    assert cert.product_trivialization_theorem_status == "EXACT_ON_INTERVAL_COMPLETE_FLOW"
    assert cert.global_flow_coverage_status == "OPEN_ANALYTIC_INPUT"
    assert cert.proper_clock_sufficient_route_status == "EXACT_PROPER_CLOCK_IMPLIES_INTERVAL_COMPLETE_FLOW"
    assert cert.global_clock_properness_status == "OPEN_ANALYTIC_INPUT"
    assert cert.physical_event_placement_status == "OPEN_PRODUCTION_INPUT"
