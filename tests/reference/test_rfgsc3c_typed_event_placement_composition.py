import pytest

from src.rfc.typed_event_placement_composition import (
    TypedEventPlacementCompositionError,
    certify_typed_event_placement_composition,
)


def fixture():
    return {
        "spatial_vertex_ids": ["v0", "v1", "v2"],
        "occurrence_to_terminal_state": {
            "o0": "sA",
            "o1": "sB",
            "o2a": "sC",
            "o2b": "sC",
        },
        "occurrence_state_table_sha256": "table-00g",
        "occurrence_state_event_complex_incidence_sha256": "event-05j",
        "event_complex_incidence_sha256": "event-05j",
        "state_to_vertex": {"sA": "v0", "sB": "v1", "sC": "v2"},
        "state_vertex_binding_sha256": "binding-fpdg",
        "state_vertex_binding_occurrence_state_table_sha256": "table-00g",
        "state_vertex_binding_spatial_complex_incidence_sha256": "spatial-tir",
        "spatial_complex_incidence_sha256": "spatial-tir",
        "event_classes": [
            {"event_id": "e0", "members": ["o0"]},
            {"event_id": "e1", "members": ["o1"]},
            {"event_id": "e2", "members": ["o2a", "o2b"]},
        ],
        "event_clock": {"e0": 0.0, "e1": 1.0, "e2": 2.0},
        "clock_offset": 0.25,
    }


def test_typed_composition_reaches_existing_gsc3b_placement_gate():
    cert = certify_typed_event_placement_composition(**fixture())
    assert cert.compatible
    assert cert.occurrence_state_table_bound_to_event_complex
    assert cert.state_vertex_binding_bound_to_occurrence_state_table
    assert cert.state_vertex_binding_bound_to_spatial_complex
    assert cert.terminal_state_domain_exact
    assert cert.placement.spatial_anchor_by_event == {
        "e0": "v0",
        "e1": "v1",
        "e2": "v2",
    }
    assert cert.placement.placement_by_event["e2"] == (2.25, "v2")


def test_00g_to_05j_digest_drift_fails_closed():
    data = fixture()
    data["event_complex_incidence_sha256"] = "other"
    with pytest.raises(TypedEventPlacementCompositionError, match="different 05J"):
        certify_typed_event_placement_composition(**data)


def test_fpdg_to_00g_digest_drift_fails_closed():
    data = fixture()
    data["state_vertex_binding_occurrence_state_table_sha256"] = "other"
    with pytest.raises(TypedEventPlacementCompositionError, match="different 00G"):
        certify_typed_event_placement_composition(**data)


def test_fpdg_to_tir_digest_drift_fails_closed():
    data = fixture()
    data["state_vertex_binding_spatial_complex_incidence_sha256"] = "other"
    with pytest.raises(TypedEventPlacementCompositionError, match="different TIR"):
        certify_typed_event_placement_composition(**data)


def test_binding_domain_must_equal_used_terminal_state_domain():
    data = fixture()
    data["state_to_vertex"] = {"sA": "v0", "sB": "v1"}
    with pytest.raises(TypedEventPlacementCompositionError, match="domain differs"):
        certify_typed_event_placement_composition(**data)


def test_downstream_quotient_fibre_conflict_remains_a_real_failure():
    data = fixture()
    data["occurrence_to_terminal_state"]["o2b"] = "sB"
    with pytest.raises(TypedEventPlacementCompositionError, match="downstream GSC3B"):
        certify_typed_event_placement_composition(**data)


def test_noninjective_state_vertex_binding_is_allowed_at_composition_layer():
    data = fixture()
    data["state_to_vertex"] = {"sA": "v0", "sB": "v0", "sC": "v2"}
    cert = certify_typed_event_placement_composition(**data)
    assert cert.compatible
    assert cert.placement.spatial_anchor_by_event["e0"] == "v0"
    assert cert.placement.spatial_anchor_by_event["e1"] == "v0"
