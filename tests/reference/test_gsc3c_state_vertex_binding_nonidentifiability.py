import pytest

from src.rfc.state_vertex_binding_nonidentifiability import (
    StateVertexBindingObstructionError,
    certify_state_vertex_binding_obstruction,
)


def test_nontrivial_vertex_sector_produces_relabeling_witness():
    cert = certify_state_vertex_binding_obstruction(
        ["s0", "s1"],
        ["v0", "v1", "v2"],
        {"s0": "v0", "s1": "v2"},
    )
    assert cert.nontrivial_target_sector is True
    assert cert.obstruction_witnessed is True
    assert cert.witness_state == "s0"
    assert cert.original_vertex == "v0"
    assert cert.transposed_vertex in {"v1", "v2"}
    assert cert.transposed_vertex != cert.original_vertex
    assert cert.source_information_status == "SHARED_NAMESPACE_OR_EXPLICIT_SOURCE_BINDING_REQUIRED"


def test_witness_is_independent_of_injectivity_of_proposed_map():
    cert = certify_state_vertex_binding_obstruction(
        ["s0", "s1"],
        ["v0", "v1"],
        {"s0": "v0", "s1": "v0"},
    )
    assert cert.obstruction_witnessed is True
    assert cert.transposed_vertex == "v1"


def test_single_vertex_sector_is_typed_as_fixed_point_exception():
    cert = certify_state_vertex_binding_obstruction(
        ["s0", "s1"],
        ["v0"],
        {"s0": "v0", "s1": "v0"},
    )
    assert cert.nontrivial_target_sector is False
    assert cert.obstruction_witnessed is False
    assert cert.source_information_status == "UNIQUE_TARGET_FIXED_POINT_SECTOR"


def test_mapping_must_cover_exact_state_carrier():
    with pytest.raises(StateVertexBindingObstructionError, match="cover every state"):
        certify_state_vertex_binding_obstruction(
            ["s0", "s1"],
            ["v0", "v1"],
            {"s0": "v0"},
        )


def test_mapping_rejects_unknown_vertex():
    with pytest.raises(StateVertexBindingObstructionError, match="unknown vertex"):
        certify_state_vertex_binding_obstruction(
            ["s0"],
            ["v0", "v1"],
            {"s0": "v2"},
        )


def test_identifiers_are_unique_and_nonempty():
    with pytest.raises(StateVertexBindingObstructionError, match="unique"):
        certify_state_vertex_binding_obstruction(
            ["s0", "s0"],
            ["v0", "v1"],
            {"s0": "v0"},
        )
    with pytest.raises(StateVertexBindingObstructionError, match="non-empty"):
        certify_state_vertex_binding_obstruction(
            ["s0"],
            ["v0", ""],
            {"s0": "v0"},
        )
