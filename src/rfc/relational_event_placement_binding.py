from __future__ import annotations

from dataclasses import dataclass
from math import isfinite
from typing import Any, Mapping, Sequence


class RelationalEventPlacementError(ValueError):
    """Raised when a GSC3B relational placement witness violates its contract."""


@dataclass(frozen=True)
class RelationalEventPlacementCertificate:
    quotient_descends: bool
    all_terminal_states_bound: bool
    event_clock_complete: bool
    injective_spacetime_placement: bool
    injectivity_required: bool
    event_count: int
    occurrence_count: int
    spatial_anchor_by_event: dict[str, str]
    placement_by_event: dict[str, tuple[float, str]]
    clock_offset: float
    verdict: str


def _nonempty_id(value: Any, name: str) -> str:
    text = str(value).strip()
    if not text:
        raise RelationalEventPlacementError(f"{name} must be a non-empty identifier")
    return text


def _finite_scalar(value: Any, name: str) -> float:
    try:
        scalar = float(value)
    except (TypeError, ValueError) as exc:
        raise RelationalEventPlacementError(f"{name} must be finite") from exc
    if not isfinite(scalar):
        raise RelationalEventPlacementError(f"{name} must be finite")
    return scalar


def certify_relational_event_placement(
    *,
    spatial_vertex_ids: Sequence[str],
    occurrences: Sequence[Mapping[str, Any]],
    event_classes: Sequence[Mapping[str, Any]],
    event_clock: Mapping[str, float],
    state_to_vertex: Mapping[str, str] | None = None,
    clock_offset: float = 0.0,
    require_injective: bool = False,
) -> RelationalEventPlacementCertificate:
    """Certify quotient-descended event placement into an ``I x Sigma`` carrier.

    ``occurrences`` supplies the IDT occurrence-to-terminal-state map
    ``x: O -> S``. ``event_classes`` supplies the quotient ``q: O -> E``.
    ``state_to_vertex`` is an optional source-owned binding ``S -> V(Sigma)``;
    when omitted, terminal-state identifiers are required to already belong to
    the spatial-vertex namespace.

    The spatial anchor descends to an event map exactly when the bound terminal
    state is constant on every quotient fibre. With a supplied 05H event clock
    ``t`` and common additive calibration ``C``, the certified placement is
    ``iota(e) = (t(e) + C, x_bar(e))``.

    Injectivity is a separate optional sector. The factorization theorem itself
    does not require distinct event classes to map to distinct spacetime pairs.
    """

    vertices = tuple(_nonempty_id(v, "spatial_vertex_id") for v in spatial_vertex_ids)
    if not vertices:
        raise RelationalEventPlacementError("spatial_vertex_ids must be non-empty")
    if len(set(vertices)) != len(vertices):
        raise RelationalEventPlacementError("spatial_vertex_ids must be unique")
    vertex_set = set(vertices)

    occurrence_state: dict[str, str] = {}
    for row in occurrences:
        if not isinstance(row, Mapping):
            raise RelationalEventPlacementError("each occurrence must be a mapping")
        occurrence_id = _nonempty_id(row.get("occurrence_id", ""), "occurrence_id")
        terminal_state_id = _nonempty_id(row.get("terminal_state_id", ""), "terminal_state_id")
        if occurrence_id in occurrence_state:
            raise RelationalEventPlacementError(f"duplicate occurrence_id: {occurrence_id}")
        occurrence_state[occurrence_id] = terminal_state_id
    if not occurrence_state:
        raise RelationalEventPlacementError("occurrences must be non-empty")

    binding: dict[str, str] = {}
    if state_to_vertex is not None:
        if not isinstance(state_to_vertex, Mapping):
            raise RelationalEventPlacementError("state_to_vertex must be a mapping")
        for raw_state, raw_vertex in state_to_vertex.items():
            state_id = _nonempty_id(raw_state, "state_to_vertex state")
            vertex_id = _nonempty_id(raw_vertex, "state_to_vertex vertex")
            if state_id in binding and binding[state_id] != vertex_id:
                raise RelationalEventPlacementError(f"conflicting binding for terminal state {state_id}")
            if vertex_id not in vertex_set:
                raise RelationalEventPlacementError(
                    f"state_to_vertex target {vertex_id!r} is not a supplied spatial vertex"
                )
            binding[state_id] = vertex_id

    def spatial_vertex_for(state_id: str) -> str:
        vertex_id = binding.get(state_id, state_id)
        if vertex_id not in vertex_set:
            raise RelationalEventPlacementError(
                f"terminal state {state_id!r} has no source-bound spatial vertex"
            )
        return vertex_id

    covered_occurrences: set[str] = set()
    anchor_by_event: dict[str, str] = {}
    for row in event_classes:
        if not isinstance(row, Mapping):
            raise RelationalEventPlacementError("each event class must be a mapping")
        event_id = _nonempty_id(row.get("event_id", ""), "event_id")
        raw_members = row.get("members", ())
        if not isinstance(raw_members, (list, tuple)):
            raise RelationalEventPlacementError("event-class members must be a sequence")
        members = tuple(_nonempty_id(m, "event member") for m in raw_members)
        if not members:
            raise RelationalEventPlacementError(f"event {event_id!r} must have at least one occurrence")
        if len(set(members)) != len(members):
            raise RelationalEventPlacementError(f"event {event_id!r} repeats an occurrence member")
        if event_id in anchor_by_event:
            raise RelationalEventPlacementError(f"duplicate event_id: {event_id}")
        unknown = [member for member in members if member not in occurrence_state]
        if unknown:
            raise RelationalEventPlacementError(
                f"event {event_id!r} references unknown occurrences: {unknown}"
            )
        repeated = [member for member in members if member in covered_occurrences]
        if repeated:
            raise RelationalEventPlacementError(
                f"occurrences belong to multiple event classes: {repeated}"
            )
        covered_occurrences.update(members)

        fibre_vertices = {
            spatial_vertex_for(occurrence_state[member])
            for member in members
        }
        if len(fibre_vertices) != 1:
            raise RelationalEventPlacementError(
                "terminal-state spatial binding does not descend through quotient "
                f"for event {event_id!r}: {sorted(fibre_vertices)}"
            )
        anchor_by_event[event_id] = next(iter(fibre_vertices))

    missing = sorted(set(occurrence_state) - covered_occurrences)
    if missing:
        raise RelationalEventPlacementError(
            f"event classes must partition all occurrences; uncovered={missing}"
        )
    if not anchor_by_event:
        raise RelationalEventPlacementError("event_classes must be non-empty")

    clock_by_event: dict[str, float] = {}
    for raw_event, raw_value in event_clock.items():
        event_id = _nonempty_id(raw_event, "event_clock event_id")
        if event_id in clock_by_event:
            raise RelationalEventPlacementError(f"duplicate event-clock key: {event_id}")
        clock_by_event[event_id] = _finite_scalar(raw_value, f"event_clock[{event_id}]")
    if set(clock_by_event) != set(anchor_by_event):
        missing_clock = sorted(set(anchor_by_event) - set(clock_by_event))
        extra_clock = sorted(set(clock_by_event) - set(anchor_by_event))
        raise RelationalEventPlacementError(
            f"event clock must cover exactly event ids; missing={missing_clock}, extra={extra_clock}"
        )

    offset = _finite_scalar(clock_offset, "clock_offset")
    placement_by_event = {
        event_id: (clock_by_event[event_id] + offset, anchor_by_event[event_id])
        for event_id in sorted(anchor_by_event)
    }
    injective = len(set(placement_by_event.values())) == len(placement_by_event)
    if bool(require_injective) and not injective:
        raise RelationalEventPlacementError(
            "injective placement was explicitly requested but distinct event classes collide"
        )

    return RelationalEventPlacementCertificate(
        quotient_descends=True,
        all_terminal_states_bound=True,
        event_clock_complete=True,
        injective_spacetime_placement=injective,
        injectivity_required=bool(require_injective),
        event_count=len(anchor_by_event),
        occurrence_count=len(occurrence_state),
        spatial_anchor_by_event=dict(sorted(anchor_by_event.items())),
        placement_by_event=placement_by_event,
        clock_offset=offset,
        verdict="PASS_QUOTIENT_DESCENDED_EVENT_PLACEMENT",
    )
