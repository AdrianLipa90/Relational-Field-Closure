"""Finite witness for the RF-GSC3C state-to-vertex relabeling obstruction."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping, Sequence


class StateVertexBindingObstructionError(ValueError):
    """Raised when the supplied finite witness is malformed."""


@dataclass(frozen=True)
class StateVertexBindingObstructionCertificate:
    state_count: int
    vertex_count: int
    nontrivial_target_sector: bool
    obstruction_witnessed: bool
    witness_state: str | None
    original_vertex: str | None
    transposed_vertex: str | None
    source_information_status: str
    theorem_status: str = "EXACT_RELABELING_OBSTRUCTION_THEOREM"


def _ids(values: Sequence[str], label: str) -> tuple[str, ...]:
    out = tuple(values)
    if any(not isinstance(value, str) or not value for value in out):
        raise StateVertexBindingObstructionError(f"{label} must contain non-empty strings")
    if len(set(out)) != len(out):
        raise StateVertexBindingObstructionError(f"{label} must be unique")
    return out


def certify_state_vertex_binding_obstruction(
    state_ids: Sequence[str],
    vertex_ids: Sequence[str],
    proposed_mapping: Mapping[str, str],
) -> StateVertexBindingObstructionCertificate:
    """Construct a target-label transposition witness when the target sector is nontrivial.

    The parent IDT state carrier is held fixed.  A transposition of two TIR vertex
    labels preserves the abstract identifier cardinality while changing the image
    of a proposed state-to-vertex assignment.  This supplies the finite symmetry
    witness for the relabeling-obstruction theorem.
    """
    states = _ids(state_ids, "state_ids")
    vertices = _ids(vertex_ids, "vertex_ids")
    if not states:
        raise StateVertexBindingObstructionError("at least one state identifier is required")
    if not vertices:
        raise StateVertexBindingObstructionError("at least one vertex identifier is required")
    if set(proposed_mapping) != set(states):
        raise StateVertexBindingObstructionError("proposed_mapping must cover every state exactly once")
    if any(value not in set(vertices) for value in proposed_mapping.values()):
        raise StateVertexBindingObstructionError("proposed_mapping references an unknown vertex")

    witness_state = states[0]
    original = proposed_mapping[witness_state]
    if len(vertices) == 1:
        return StateVertexBindingObstructionCertificate(
            state_count=len(states),
            vertex_count=1,
            nontrivial_target_sector=False,
            obstruction_witnessed=False,
            witness_state=witness_state,
            original_vertex=original,
            transposed_vertex=original,
            source_information_status="UNIQUE_TARGET_FIXED_POINT_SECTOR",
        )

    transposed = next(vertex for vertex in vertices if vertex != original)
    return StateVertexBindingObstructionCertificate(
        state_count=len(states),
        vertex_count=len(vertices),
        nontrivial_target_sector=True,
        obstruction_witnessed=True,
        witness_state=witness_state,
        original_vertex=original,
        transposed_vertex=transposed,
        source_information_status="SHARED_NAMESPACE_OR_EXPLICIT_SOURCE_BINDING_REQUIRED",
    )
