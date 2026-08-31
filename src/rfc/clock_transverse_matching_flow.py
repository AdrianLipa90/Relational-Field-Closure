"""Clock-transverse matching-flow soldering checks for RFC GSC-3A.

The algebraic layer verifies that local ADM matching fields represent one global
clock-transverse vector field under shared-clock spatial relabelings.  The global
product-trivialization theorem is conditional on interval-complete flow coverage;
that analytic coverage and physical event placement retain separate production
statuses.
"""
from __future__ import annotations

from dataclasses import dataclass
from math import isfinite
from typing import Iterable, Sequence


class ClockTransverseMatchingFlowError(ValueError):
    """Raised when a supplied GSC-3A witness fails closed."""


Vector3 = tuple[float, float, float]
Matrix3 = tuple[tuple[float, float, float], ...]


def _finite(value: float, label: str) -> float:
    out = float(value)
    if not isfinite(out):
        raise ClockTransverseMatchingFlowError(f"{label} must be finite")
    return out


def _vector3(values: Sequence[float], label: str) -> Vector3:
    if len(values) != 3:
        raise ClockTransverseMatchingFlowError(f"{label} must have length 3")
    return tuple(_finite(x, label) for x in values)  # type: ignore[return-value]


def _matrix3(values: Sequence[Sequence[float]], label: str) -> Matrix3:
    if len(values) != 3 or any(len(row) != 3 for row in values):
        raise ClockTransverseMatchingFlowError(f"{label} must be 3x3")
    return tuple(
        tuple(_finite(x, f"{label}[{i}]") for x in row)
        for i, row in enumerate(values)
    )  # type: ignore[return-value]


def matvec3(a: Matrix3, v: Vector3) -> Vector3:
    return tuple(sum(a[i][k] * v[k] for k in range(3)) for i in range(3))  # type: ignore[return-value]


def matmul3(a: Matrix3, b: Matrix3) -> Matrix3:
    return tuple(
        tuple(sum(a[i][k] * b[k][j] for k in range(3)) for j in range(3))
        for i in range(3)
    )  # type: ignore[return-value]


def add3(a: Vector3, b: Vector3) -> Vector3:
    return tuple(a[i] + b[i] for i in range(3))  # type: ignore[return-value]


def sub3(a: Vector3, b: Vector3) -> Vector3:
    return tuple(a[i] - b[i] for i in range(3))  # type: ignore[return-value]


def max_abs_vector(a: Vector3, b: Vector3) -> float:
    return max(abs(a[i] - b[i]) for i in range(3))


def max_abs_matrix(a: Matrix3, b: Matrix3) -> float:
    return max(abs(a[i][j] - b[i][j]) for i in range(3) for j in range(3))


@dataclass(frozen=True)
class MatchingPatch:
    name: str
    shift: Vector3

    def __post_init__(self) -> None:
        if not isinstance(self.name, str) or not self.name:
            raise ClockTransverseMatchingFlowError("patch name must be non-empty")
        object.__setattr__(self, "shift", _vector3(self.shift, "shift"))


@dataclass(frozen=True)
class MatchingTransition:
    """First-order data for x_target=f(t,x_source)."""

    source: str
    target: str
    spatial_jacobian: Matrix3
    time_drift: Vector3

    def __post_init__(self) -> None:
        if not isinstance(self.source, str) or not self.source:
            raise ClockTransverseMatchingFlowError("transition source must be non-empty")
        if not isinstance(self.target, str) or not self.target:
            raise ClockTransverseMatchingFlowError("transition target must be non-empty")
        if self.source == self.target:
            raise ClockTransverseMatchingFlowError("transition must connect distinct patches")
        object.__setattr__(self, "spatial_jacobian", _matrix3(self.spatial_jacobian, "spatial_jacobian"))
        object.__setattr__(self, "time_drift", _vector3(self.time_drift, "time_drift"))


@dataclass(frozen=True)
class EventClockAnchor:
    event_id: str
    discrete_clock: float
    spacetime_clock: float

    def __post_init__(self) -> None:
        if not isinstance(self.event_id, str) or not self.event_id:
            raise ClockTransverseMatchingFlowError("event_id must be non-empty")
        object.__setattr__(self, "discrete_clock", _finite(self.discrete_clock, "discrete_clock"))
        object.__setattr__(self, "spacetime_clock", _finite(self.spacetime_clock, "spacetime_clock"))


@dataclass(frozen=True)
class ClockTransverseMatchingFlowCertificate:
    compatible: bool
    patch_count: int
    transition_count: int
    triangle_count: int
    event_anchor_count: int
    connected: bool
    clock_pairing_dt: float
    max_spatial_coframe_pairing_residual: float
    max_shift_overlap_residual: float
    max_transition_cocycle_residual: float
    max_time_drift_cocycle_residual: float
    additive_clock_offset: float | None
    max_event_anchor_residual: float
    local_soldering_status: str = "EXACT_CLOCK_TRANSVERSE_MATCHING_FIELD"
    product_trivialization_theorem_status: str = "EXACT_ON_INTERVAL_COMPLETE_FLOW"
    global_flow_coverage_status: str = "OPEN_ANALYTIC_INPUT"
    physical_event_placement_status: str = "OPEN_PRODUCTION_INPUT"


def clock_transverse_pairing(shift: Sequence[float]) -> tuple[float, Vector3]:
    """Evaluate dt and (dx^i+b^i dt) on X=partial_t-b^i partial_i."""
    b = _vector3(shift, "shift")
    dt_on_x = 1.0
    dx_on_x = tuple(-value for value in b)
    spatial = tuple(dx_on_x[i] + b[i] * dt_on_x for i in range(3))
    return dt_on_x, spatial  # type: ignore[return-value]


def expected_target_shift(transition: MatchingTransition, source_shift: Sequence[float]) -> Vector3:
    """Return b_target=A b_source-v for one shared-clock overlap."""
    b = _vector3(source_shift, "source_shift")
    return sub3(matvec3(transition.spatial_jacobian, b), transition.time_drift)


def _connected(names: set[str], transitions: Sequence[MatchingTransition]) -> bool:
    if len(names) <= 1:
        return True
    adjacency = {name: set() for name in names}
    for transition in transitions:
        adjacency[transition.source].add(transition.target)
        adjacency[transition.target].add(transition.source)
    root = next(iter(names))
    seen = {root}
    stack = [root]
    while stack:
        current = stack.pop()
        for nxt in adjacency[current] - seen:
            seen.add(nxt)
            stack.append(nxt)
    return seen == names


def certify_clock_transverse_matching_flow(
    patches: Iterable[MatchingPatch],
    transitions: Sequence[MatchingTransition],
    *,
    triangles: Iterable[tuple[str, str, str]] = (),
    event_anchors: Sequence[EventClockAnchor] = (),
    require_connected: bool = True,
    atol: float = 1.0e-12,
) -> ClockTransverseMatchingFlowCertificate:
    """Certify the finite algebraic part of the GSC-3A soldering gate.

    On each overlap x_q=f_qp(t,x_p), write A=D_x f and v=partial_t f.  Local
    fields X_p=partial_t-b_p^i partial_i represent one vector field precisely when

        b_q = A b_p - v.

    Declared triples additionally verify the first-order coordinate cocycle. Event
    anchors verify one additive calibration between the 05H event clock and the
    smooth spacetime clock.
    """
    atol = _finite(atol, "atol")
    if atol < 0.0:
        raise ClockTransverseMatchingFlowError("atol must be non-negative")

    patch_list = tuple(patches)
    if not patch_list:
        raise ClockTransverseMatchingFlowError("at least one matching patch is required")
    if any(not isinstance(patch, MatchingPatch) for patch in patch_list):
        raise ClockTransverseMatchingFlowError("all patches must be MatchingPatch instances")
    if len({patch.name for patch in patch_list}) != len(patch_list):
        raise ClockTransverseMatchingFlowError("duplicate patch name")
    patch_map = {patch.name: patch for patch in patch_list}
    names = set(patch_map)

    transition_list = tuple(transitions)
    transition_map: dict[tuple[str, str], MatchingTransition] = {}
    max_shift = 0.0
    for transition in transition_list:
        if not isinstance(transition, MatchingTransition):
            raise ClockTransverseMatchingFlowError("all transitions must be MatchingTransition instances")
        if transition.source not in names or transition.target not in names:
            raise ClockTransverseMatchingFlowError("transition references an unknown patch")
        key = (transition.source, transition.target)
        if key in transition_map:
            raise ClockTransverseMatchingFlowError(f"duplicate directed transition {key}")
        transition_map[key] = transition
        expected = expected_target_shift(transition, patch_map[transition.source].shift)
        residual = max_abs_vector(expected, patch_map[transition.target].shift)
        max_shift = max(max_shift, residual)
        if residual > atol:
            raise ClockTransverseMatchingFlowError(
                f"matching-field overlap law failed on {key}; residual={residual:.17g}"
            )

    connected = _connected(names, transition_list)
    if require_connected and not connected:
        raise ClockTransverseMatchingFlowError("connected matching-flow claim requested for disconnected patches")

    max_a = 0.0
    max_v = 0.0
    triangle_list = tuple(triangles)
    for p, q, r in triangle_list:
        try:
            qp = transition_map[(p, q)]
            rq = transition_map[(q, r)]
            rp = transition_map[(p, r)]
        except KeyError as exc:
            raise ClockTransverseMatchingFlowError(
                f"declared triangle {(p, q, r)} requires p->q, q->r and p->r"
            ) from exc
        composed_a = matmul3(rq.spatial_jacobian, qp.spatial_jacobian)
        a_res = max_abs_matrix(composed_a, rp.spatial_jacobian)
        max_a = max(max_a, a_res)
        if a_res > atol:
            raise ClockTransverseMatchingFlowError(
                f"spatial Jacobian cocycle failed on {(p, q, r)}; residual={a_res:.17g}"
            )
        composed_v = add3(rq.time_drift, matvec3(rq.spatial_jacobian, qp.time_drift))
        v_res = max_abs_vector(composed_v, rp.time_drift)
        max_v = max(max_v, v_res)
        if v_res > atol:
            raise ClockTransverseMatchingFlowError(
                f"time-drift cocycle failed on {(p, q, r)}; residual={v_res:.17g}"
            )

    max_spatial_pair = 0.0
    for patch in patch_list:
        dt_value, spatial = clock_transverse_pairing(patch.shift)
        if dt_value != 1.0:
            raise ClockTransverseMatchingFlowError("clock pairing must equal one")
        max_spatial_pair = max(max_spatial_pair, max(abs(x) for x in spatial))
        if max(abs(x) for x in spatial) > atol:
            raise ClockTransverseMatchingFlowError("spatial coframe pairing residual exceeded tolerance")

    anchor_list = tuple(event_anchors)
    if len({anchor.event_id for anchor in anchor_list}) != len(anchor_list):
        raise ClockTransverseMatchingFlowError("duplicate event anchor")
    offset: float | None = None
    max_anchor = 0.0
    for anchor in anchor_list:
        if not isinstance(anchor, EventClockAnchor):
            raise ClockTransverseMatchingFlowError("all event anchors must be EventClockAnchor instances")
        current = anchor.spacetime_clock - anchor.discrete_clock
        if offset is None:
            offset = current
        residual = abs(current - offset)
        max_anchor = max(max_anchor, residual)
        if residual > atol:
            raise ClockTransverseMatchingFlowError(
                f"event clock anchors require more than one additive calibration; residual={residual:.17g}"
            )

    return ClockTransverseMatchingFlowCertificate(
        compatible=True,
        patch_count=len(patch_list),
        transition_count=len(transition_list),
        triangle_count=len(triangle_list),
        event_anchor_count=len(anchor_list),
        connected=connected,
        clock_pairing_dt=1.0,
        max_spatial_coframe_pairing_residual=max_spatial_pair,
        max_shift_overlap_residual=max_shift,
        max_transition_cocycle_residual=max_a,
        max_time_drift_cocycle_residual=max_v,
        additive_clock_offset=offset,
        max_event_anchor_residual=max_anchor,
    )
