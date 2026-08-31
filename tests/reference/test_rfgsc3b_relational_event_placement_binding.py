import math

import pytest

from src.rfc.relational_event_placement_binding import (
    RelationalEventPlacementError,
    certify_relational_event_placement,
)


def fixture():
    return {
        "spatial_vertex_ids": ["A", "B", "C"],
        "occurrences": [
            {"occurrence_id": "o0", "terminal_state_id": "A"},
            {"occurrence_id": "o1", "terminal_state_id": "B"},
            {"occurrence_id": "o2a", "terminal_state_id": "C"},
            {"occurrence_id": "o2b", "terminal_state_id": "C"},
        ],
        "event_classes": [
            {"event_id": "e0", "members": ["o0"]},
            {"event_id": "e1", "members": ["o1"]},
            {"event_id": "e2", "members": ["o2a", "o2b"]},
        ],
        "event_clock": {"e0": 0.0, "e1": 1.0, "e2": 2.0},
        "clock_offset": 0.5,
    }


def test_identity_namespace_descends_and_preserves_common_clock_offset():
    cert = certify_relational_event_placement(**fixture())
    assert cert.quotient_descends
    assert cert.spatial_anchor_by_event == {"e0": "A", "e1": "B", "e2": "C"}
    assert cert.placement_by_event["e0"] == (0.5, "A")
    assert cert.placement_by_event["e2"] == (2.5, "C")
    assert cert.clock_offset == 0.5
    assert cert.verdict == "PASS_QUOTIENT_DESCENDED_EVENT_PLACEMENT"


def test_explicit_state_to_vertex_binding_descends():
    data = fixture()
    data["occurrences"] = [
        {"occurrence_id": "o0", "terminal_state_id": "sA"},
        {"occurrence_id": "o1", "terminal_state_id": "sB"},
        {"occurrence_id": "o2a", "terminal_state_id": "sC"},
        {"occurrence_id": "o2b", "terminal_state_id": "sC"},
    ]
    data["state_to_vertex"] = {"sA": "A", "sB": "B", "sC": "C"}
    cert = certify_relational_event_placement(**data)
    assert cert.spatial_anchor_by_event["e2"] == "C"


def test_terminal_state_binding_must_be_constant_on_each_quotient_fibre():
    data = fixture()
    data["occurrences"][-1]["terminal_state_id"] = "B"
    with pytest.raises(RelationalEventPlacementError, match="does not descend"):
        certify_relational_event_placement(**data)


def test_unbound_terminal_state_fails_closed():
    data = fixture()
    data["occurrences"][-1]["terminal_state_id"] = "Z"
    with pytest.raises(RelationalEventPlacementError, match="no source-bound spatial vertex"):
        certify_relational_event_placement(**data)


def test_event_classes_must_cover_every_occurrence_exactly_once():
    data = fixture()
    data["event_classes"][-1]["members"] = ["o2a"]
    with pytest.raises(RelationalEventPlacementError, match="uncovered"):
        certify_relational_event_placement(**data)

    data = fixture()
    data["event_classes"][-1]["members"] = ["o1", "o2a", "o2b"]
    with pytest.raises(RelationalEventPlacementError, match="multiple event classes"):
        certify_relational_event_placement(**data)


def test_unknown_occurrence_in_event_class_fails_closed():
    data = fixture()
    data["event_classes"][-1]["members"].append("ghost")
    with pytest.raises(RelationalEventPlacementError, match="unknown occurrences"):
        certify_relational_event_placement(**data)


def test_event_clock_must_cover_exact_event_quotient_and_be_finite():
    data = fixture()
    del data["event_clock"]["e2"]
    with pytest.raises(RelationalEventPlacementError, match="cover exactly"):
        certify_relational_event_placement(**data)

    data = fixture()
    data["event_clock"]["e2"] = math.inf
    with pytest.raises(RelationalEventPlacementError, match="must be finite"):
        certify_relational_event_placement(**data)


def test_spatial_vertex_namespace_is_unique_and_binding_targets_it():
    data = fixture()
    data["spatial_vertex_ids"] = ["A", "A", "C"]
    with pytest.raises(RelationalEventPlacementError, match="must be unique"):
        certify_relational_event_placement(**data)

    data = fixture()
    data["state_to_vertex"] = {"A": "outside"}
    with pytest.raises(RelationalEventPlacementError, match="not a supplied spatial vertex"):
        certify_relational_event_placement(**data)


def test_spacetime_injectivity_is_optional_and_explicitly_gated():
    data = fixture()
    data["occurrences"][1]["terminal_state_id"] = "A"
    data["event_clock"]["e1"] = 0.0
    cert = certify_relational_event_placement(**data)
    assert not cert.injective_spacetime_placement
    assert not cert.injectivity_required

    data["require_injective"] = True
    with pytest.raises(RelationalEventPlacementError, match="injective placement"):
        certify_relational_event_placement(**data)


def test_nonfinite_clock_offset_fails_closed():
    data = fixture()
    data["clock_offset"] = float("nan")
    with pytest.raises(RelationalEventPlacementError, match="clock_offset must be finite"):
        certify_relational_event_placement(**data)
