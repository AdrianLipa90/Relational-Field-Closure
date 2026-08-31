from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping, Sequence

from .relational_event_placement_binding import (
    RelationalEventPlacementCertificate,
    RelationalEventPlacementError,
    certify_relational_event_placement,
)


class TypedEventPlacementCompositionError(ValueError):
    """Raised when typed upstream placement artifacts cannot be composed."""


@dataclass(frozen=True)
class TypedEventPlacementCompositionCertificate:
    compatible: bool
    occurrence_state_table_bound_to_event_complex: bool
    state_vertex_binding_bound_to_occurrence_state_table: bool
    state_vertex_binding_bound_to_spatial_complex: bool
    terminal_state_domain_exact: bool
    placement: RelationalEventPlacementCertificate
    occurrence_state_table_sha256: str
    event_complex_incidence_sha256: str
    state_vertex_binding_sha256: str
    spatial_complex_incidence_sha256: str
    verdict: str = "PASS_TYPED_EVENT_PLACEMENT_COMPOSITION"
    production_data_status: str = "OPEN_INPUT"


def _digest(value: str, name: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise TypedEventPlacementCompositionError(f"{name} must be a non-empty digest")
    return value.strip()


def certify_typed_event_placement_composition(
    *,
    spatial_vertex_ids: Sequence[str],
    occurrence_to_terminal_state: Mapping[str, str],
    occurrence_state_table_sha256: str,
    occurrence_state_event_complex_incidence_sha256: str,
    event_complex_incidence_sha256: str,
    state_to_vertex: Mapping[str, str],
    state_vertex_binding_sha256: str,
    state_vertex_binding_occurrence_state_table_sha256: str,
    state_vertex_binding_spatial_complex_incidence_sha256: str,
    spatial_complex_incidence_sha256: str,
    event_classes: Sequence[Mapping[str, object]],
    event_clock: Mapping[str, float],
    clock_offset: float = 0.0,
    require_injective: bool = False,
) -> TypedEventPlacementCompositionCertificate:
    """Compose typed IDT 00G + FPDG state/vertex + RFC GSC3B artifacts.

    The function verifies the immutable digest handoffs before constructing the
    occurrence rows consumed by ``certify_relational_event_placement``.
    Production data remain a separate input status; this function owns only the
    deterministic composition and compatibility gate.
    """

    table_digest = _digest(occurrence_state_table_sha256, "occurrence_state_table_sha256")
    table_event_digest = _digest(
        occurrence_state_event_complex_incidence_sha256,
        "occurrence_state_event_complex_incidence_sha256",
    )
    event_digest = _digest(event_complex_incidence_sha256, "event_complex_incidence_sha256")
    binding_digest = _digest(state_vertex_binding_sha256, "state_vertex_binding_sha256")
    binding_table_digest = _digest(
        state_vertex_binding_occurrence_state_table_sha256,
        "state_vertex_binding_occurrence_state_table_sha256",
    )
    binding_spatial_digest = _digest(
        state_vertex_binding_spatial_complex_incidence_sha256,
        "state_vertex_binding_spatial_complex_incidence_sha256",
    )
    spatial_digest = _digest(spatial_complex_incidence_sha256, "spatial_complex_incidence_sha256")

    if table_event_digest != event_digest:
        raise TypedEventPlacementCompositionError(
            "00G occurrence-state table is bound to a different 05J event-complex incidence digest"
        )
    if binding_table_digest != table_digest:
        raise TypedEventPlacementCompositionError(
            "FPDG state-vertex binding is bound to a different 00G table digest"
        )
    if binding_spatial_digest != spatial_digest:
        raise TypedEventPlacementCompositionError(
            "FPDG state-vertex binding is bound to a different TIR spatial-complex incidence digest"
        )

    if not isinstance(occurrence_to_terminal_state, Mapping) or not occurrence_to_terminal_state:
        raise TypedEventPlacementCompositionError("occurrence_to_terminal_state must be non-empty")
    occurrence_rows = []
    used_states = set()
    for raw_occurrence, raw_state in occurrence_to_terminal_state.items():
        occurrence_id = str(raw_occurrence).strip()
        terminal_state_id = str(raw_state).strip()
        if not occurrence_id or not terminal_state_id:
            raise TypedEventPlacementCompositionError(
                "occurrence and terminal-state identifiers must be non-empty"
            )
        occurrence_rows.append(
            {"occurrence_id": occurrence_id, "terminal_state_id": terminal_state_id}
        )
        used_states.add(terminal_state_id)

    if not isinstance(state_to_vertex, Mapping) or not state_to_vertex:
        raise TypedEventPlacementCompositionError("state_to_vertex must be non-empty")
    bound_states = {str(state).strip() for state in state_to_vertex}
    if "" in bound_states or bound_states != used_states:
        missing = sorted(used_states - bound_states)
        extra = sorted(bound_states - used_states)
        raise TypedEventPlacementCompositionError(
            f"state-vertex binding domain differs from used 00G terminal-state domain; missing={missing}, extra={extra}"
        )

    try:
        placement = certify_relational_event_placement(
            spatial_vertex_ids=spatial_vertex_ids,
            occurrences=occurrence_rows,
            event_classes=event_classes,
            event_clock=event_clock,
            state_to_vertex=state_to_vertex,
            clock_offset=clock_offset,
            require_injective=require_injective,
        )
    except RelationalEventPlacementError as exc:
        raise TypedEventPlacementCompositionError(
            f"downstream GSC3B placement gate failed: {exc}"
        ) from exc

    return TypedEventPlacementCompositionCertificate(
        compatible=True,
        occurrence_state_table_bound_to_event_complex=True,
        state_vertex_binding_bound_to_occurrence_state_table=True,
        state_vertex_binding_bound_to_spatial_complex=True,
        terminal_state_domain_exact=True,
        placement=placement,
        occurrence_state_table_sha256=table_digest,
        event_complex_incidence_sha256=event_digest,
        state_vertex_binding_sha256=binding_digest,
        spatial_complex_incidence_sha256=spatial_digest,
    )
