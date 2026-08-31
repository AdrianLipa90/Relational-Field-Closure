"""Premetric product-clock atlas lift for the global spacetime closure candidate.

Given an oriented spatial 3-manifold atlas on Sigma and a global interval clock I,
this module certifies the coordinate part of the product construction M = I x Sigma.
The shared clock coordinate is preserved exactly while spatial coordinates may be
time-dependent.  The resulting spacetime overlap Jacobian has the form

    J = [[1, 0],
         [v, A]],

with det(J) = det(A).  This is the coordinate structure expected by RF-E25.

The module certifies only the product/coordinate theorem.  Physical identification
of the TIR x IDT carrier with this product and the RF-E25 ADM/coframe data remain
separate promotion inputs.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import isfinite
from typing import Iterable, Sequence


class ProductClockAtlasLiftError(ValueError):
    """Raised when a supplied product-clock atlas witness fails closed."""


Matrix3 = tuple[tuple[float, float, float], ...]
Matrix4 = tuple[tuple[float, float, float, float], ...]
Vector3 = tuple[float, float, float]


def _finite(value: float, label: str) -> float:
    out = float(value)
    if not isfinite(out):
        raise ProductClockAtlasLiftError(f"{label} must be finite")
    return out


def _vector3(values: Sequence[float], label: str) -> Vector3:
    if len(values) != 3:
        raise ProductClockAtlasLiftError(f"{label} must have length 3")
    return tuple(_finite(x, label) for x in values)  # type: ignore[return-value]


def _matrix3(values: Sequence[Sequence[float]], label: str) -> Matrix3:
    if len(values) != 3 or any(len(row) != 3 for row in values):
        raise ProductClockAtlasLiftError(f"{label} must be 3x3")
    return tuple(
        tuple(_finite(x, f"{label}[{i}]") for x in row)
        for i, row in enumerate(values)
    )  # type: ignore[return-value]


def det3(a: Matrix3) -> float:
    return (
        a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
        - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
        + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0])
    )


def matmul3(a: Matrix3, b: Matrix3) -> Matrix3:
    return tuple(
        tuple(sum(a[i][k] * b[k][j] for k in range(3)) for j in range(3))
        for i in range(3)
    )  # type: ignore[return-value]


def matvec3(a: Matrix3, v: Vector3) -> Vector3:
    return tuple(sum(a[i][k] * v[k] for k in range(3)) for i in range(3))  # type: ignore[return-value]


def add3(a: Vector3, b: Vector3) -> Vector3:
    return tuple(a[i] + b[i] for i in range(3))  # type: ignore[return-value]


def max_abs3_matrix(a: Matrix3, b: Matrix3) -> float:
    return max(abs(a[i][j] - b[i][j]) for i in range(3) for j in range(3))


def max_abs3_vector(a: Vector3, b: Vector3) -> float:
    return max(abs(a[i] - b[i]) for i in range(3))


@dataclass(frozen=True)
class SpatialAtlasTransition:
    """First-order data for x_target=f(t,x_source) on one spatial overlap."""

    source: str
    target: str
    spatial_jacobian: Matrix3
    time_drift: Vector3 = (0.0, 0.0, 0.0)

    def __post_init__(self) -> None:
        if not isinstance(self.source, str) or not self.source:
            raise ProductClockAtlasLiftError("transition source must be non-empty")
        if not isinstance(self.target, str) or not self.target:
            raise ProductClockAtlasLiftError("transition target must be non-empty")
        if self.source == self.target:
            raise ProductClockAtlasLiftError("self-transition is not an atlas overlap")
        object.__setattr__(self, "spatial_jacobian", _matrix3(self.spatial_jacobian, "spatial_jacobian"))
        object.__setattr__(self, "time_drift", _vector3(self.time_drift, "time_drift"))

    @property
    def spacetime_jacobian(self) -> Matrix4:
        a = self.spatial_jacobian
        v = self.time_drift
        return (
            (1.0, 0.0, 0.0, 0.0),
            (v[0], a[0][0], a[0][1], a[0][2]),
            (v[1], a[1][0], a[1][1], a[1][2]),
            (v[2], a[2][0], a[2][1], a[2][2]),
        )


@dataclass(frozen=True)
class ProductClockAtlasCertificate:
    compatible: bool
    spacetime_dimension: int
    patch_count: int
    transition_count: int
    triangle_count: int
    connected: bool
    shared_clock_first_row: bool
    dt_nowhere_zero: bool
    min_spatial_orientation_det: float
    max_spatial_cocycle_residual: float
    max_time_drift_cocycle_residual: float
    theorem_status: str = "EXACT_PRODUCT_CLOCK_ATLAS_LIFT"
    physical_product_realization_status: str = "OPEN_INPUT"


def _connected(names: set[str], transitions: Sequence[SpatialAtlasTransition]) -> bool:
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


def certify_product_clock_atlas_lift(
    patches: Iterable[str],
    transitions: Sequence[SpatialAtlasTransition],
    *,
    triangles: Iterable[tuple[str, str, str]] = (),
    require_connected: bool = True,
    orientation_floor: float = 1.0e-12,
    atol: float = 1.0e-12,
) -> ProductClockAtlasCertificate:
    """Certify the shared-clock product atlas coordinate structure.

    For each transition p->q the input is the spatial derivative A_{q<-p} and
    temporal drift v_{q<-p}=partial_t f_{q<-p}.  The lifted Jacobian is

        [[1, 0], [v, A]].

    Therefore det(J)=det(A) and dt is globally preserved.  Declared triples
    additionally check the first-order cocycle inherited from spatial chart maps:

        A_{r<-p}=A_{r<-q} A_{q<-p},
        v_{r<-p}=v_{r<-q}+A_{r<-q} v_{q<-p}.
    """

    orientation_floor = _finite(orientation_floor, "orientation_floor")
    atol = _finite(atol, "atol")
    if orientation_floor <= 0.0 or atol < 0.0:
        raise ProductClockAtlasLiftError("orientation_floor must be positive and atol non-negative")

    patch_names = tuple(patches)
    if not patch_names:
        raise ProductClockAtlasLiftError("at least one spatial patch is required")
    if any(not isinstance(name, str) or not name for name in patch_names):
        raise ProductClockAtlasLiftError("patch names must be non-empty strings")
    if len(set(patch_names)) != len(patch_names):
        raise ProductClockAtlasLiftError("duplicate patch name")
    names = set(patch_names)

    transition_list = tuple(transitions)
    transition_map: dict[tuple[str, str], SpatialAtlasTransition] = {}
    dets: list[float] = []
    for transition in transition_list:
        if not isinstance(transition, SpatialAtlasTransition):
            raise ProductClockAtlasLiftError("all transitions must be SpatialAtlasTransition instances")
        if transition.source not in names or transition.target not in names:
            raise ProductClockAtlasLiftError("transition references an unknown patch")
        key = (transition.source, transition.target)
        if key in transition_map:
            raise ProductClockAtlasLiftError(f"duplicate directed transition {key}")
        transition_map[key] = transition
        determinant = det3(transition.spatial_jacobian)
        dets.append(determinant)
        if determinant <= orientation_floor:
            raise ProductClockAtlasLiftError(
                f"spatial overlap must be invertible and orientation preserving; det={determinant:.17g}"
            )
        if transition.spacetime_jacobian[0] != (1.0, 0.0, 0.0, 0.0):
            raise ProductClockAtlasLiftError("shared clock differential was not preserved")

    connected = _connected(names, transition_list)
    if require_connected and not connected:
        raise ProductClockAtlasLiftError("connected product-atlas claim requested for disconnected patches")

    max_a_residual = 0.0
    max_v_residual = 0.0
    triangle_list = tuple(triangles)
    for p, q, r in triangle_list:
        try:
            qp = transition_map[(p, q)]
            rq = transition_map[(q, r)]
            rp = transition_map[(p, r)]
        except KeyError as exc:
            raise ProductClockAtlasLiftError(
                f"declared triangle {(p, q, r)} requires transitions p->q, q->r and p->r"
            ) from exc

        composed_a = matmul3(rq.spatial_jacobian, qp.spatial_jacobian)
        a_residual = max_abs3_matrix(composed_a, rp.spatial_jacobian)
        max_a_residual = max(max_a_residual, a_residual)
        if a_residual > atol:
            raise ProductClockAtlasLiftError(
                f"spatial transition cocycle failed on {(p, q, r)}; residual={a_residual:.17g}"
            )

        composed_v = add3(rq.time_drift, matvec3(rq.spatial_jacobian, qp.time_drift))
        v_residual = max_abs3_vector(composed_v, rp.time_drift)
        max_v_residual = max(max_v_residual, v_residual)
        if v_residual > atol:
            raise ProductClockAtlasLiftError(
                f"time-drift cocycle failed on {(p, q, r)}; residual={v_residual:.17g}"
            )

    return ProductClockAtlasCertificate(
        compatible=True,
        spacetime_dimension=4,
        patch_count=len(patch_names),
        transition_count=len(transition_list),
        triangle_count=len(triangle_list),
        connected=connected,
        shared_clock_first_row=True,
        dt_nowhere_zero=True,
        min_spatial_orientation_det=min(dets) if dets else float("inf"),
        max_spatial_cocycle_residual=max_a_residual,
        max_time_drift_cocycle_residual=max_v_residual,
    )
