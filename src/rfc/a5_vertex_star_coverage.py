"""RF-GSC4C canonical overlap-incidence generator from an admitted TIR A5 complex.

The source carrier is a finite tetrahedral simplicial complex already admitted by
TIR A5.  GSC4C uses the open stars of vertices as a canonical patch cover.
For a simplicial complex, intersections of vertex open stars are non-empty
exactly when the corresponding vertex set spans a simplex.  Pair and triple
coverage indices are therefore determined by the tetrahedral facet list.

This module generates coverage/incidence only.  It does not synthesize spatial
coframes, Jacobian values, SO(3) rotations, lapse values, or matching fields.
"""
from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations
from typing import Hashable, Iterable, Sequence


class A5VertexStarCoverageError(ValueError):
    """Raised when a declared GSC4C coverage witness fails closed."""


Vertex = Hashable
Tetrahedron = tuple[Vertex, Vertex, Vertex, Vertex]


def _stable_key(value: Vertex) -> tuple[str, str]:
    return (type(value).__name__, repr(value))


def _sorted_tuple(values: Iterable[Vertex]) -> tuple[Vertex, ...]:
    return tuple(sorted(values, key=_stable_key))


@dataclass(frozen=True)
class VertexStarCoverageCertificate:
    status: str
    a5_parent_certificate_id: str
    patch_ids: tuple[str, ...]
    vertices: tuple[Vertex, ...]
    pair_overlap_vertices: tuple[tuple[Vertex, Vertex], ...]
    triple_overlap_vertices: tuple[tuple[Vertex, Vertex, Vertex], ...]
    pair_overlaps: tuple[tuple[str, str], ...]
    triple_overlaps: tuple[tuple[str, str, str], ...]
    tetrahedron_count: int
    coverage_exact: bool = True
    production_geometry_values_status: str = "OPEN_SOURCE_GEOMETRY_PACKET"
    theorem_status: str = "EXACT_VERTEX_OPEN_STAR_COVERAGE_INCIDENCE"


def _normalize_tetrahedra(tetrahedra: Sequence[Sequence[Vertex]]) -> tuple[Tetrahedron, ...]:
    if not tetrahedra:
        raise A5VertexStarCoverageError("at least one tetrahedron is required")
    normalized: list[Tetrahedron] = []
    seen: set[tuple[Vertex, ...]] = set()
    for index, raw in enumerate(tetrahedra):
        if len(raw) != 4:
            raise A5VertexStarCoverageError(f"tetrahedron {index} must contain four vertices")
        if len(set(raw)) != 4:
            raise A5VertexStarCoverageError(f"tetrahedron {index} has repeated vertices")
        key = _sorted_tuple(raw)
        if key in seen:
            raise A5VertexStarCoverageError("duplicate tetrahedron is not admitted")
        seen.add(key)
        normalized.append(key)  # type: ignore[arg-type]
    return tuple(normalized)


def derive_a5_vertex_star_coverage(
    tetrahedra: Sequence[Sequence[Vertex]],
    *,
    a5_manifold_certified: bool,
    a5_parent_certificate_id: str,
    patch_prefix: str = "star",
) -> VertexStarCoverageCertificate:
    """Derive pair/triple overlap incidence for the canonical vertex-star cover.

    The A5 certification is an explicit parent gate.  The generator does not
    attempt to replace or infer the manifold certificate from the local facet
    list supplied here.
    """
    if a5_manifold_certified is not True:
        raise A5VertexStarCoverageError("an admitted TIR A5 manifold certificate is required")
    parent = str(a5_parent_certificate_id).strip()
    if not parent:
        raise A5VertexStarCoverageError("a5_parent_certificate_id must be nonempty")
    prefix = str(patch_prefix).strip()
    if not prefix:
        raise A5VertexStarCoverageError("patch_prefix must be nonempty")

    tets = _normalize_tetrahedra(tetrahedra)
    vertices = _sorted_tuple({v for tet in tets for v in tet})

    edge_set: set[tuple[Vertex, ...]] = set()
    triangle_set: set[tuple[Vertex, ...]] = set()
    for tet in tets:
        edge_set.update(_sorted_tuple(c) for c in combinations(tet, 2))
        triangle_set.update(_sorted_tuple(c) for c in combinations(tet, 3))

    edges = tuple(sorted(edge_set, key=lambda item: tuple(_stable_key(x) for x in item)))
    triangles = tuple(sorted(triangle_set, key=lambda item: tuple(_stable_key(x) for x in item)))

    patch_by_vertex = {v: f"{prefix}:{repr(v)}" for v in vertices}
    pair_overlaps = tuple((patch_by_vertex[a], patch_by_vertex[b]) for a, b in edges)
    triple_overlaps = tuple(
        (patch_by_vertex[a], patch_by_vertex[b], patch_by_vertex[c])
        for a, b, c in triangles
    )

    return VertexStarCoverageCertificate(
        status="PASS_GSC4C_A5_VERTEX_STAR_COVERAGE_INCIDENCE",
        a5_parent_certificate_id=parent,
        patch_ids=tuple(patch_by_vertex[v] for v in vertices),
        vertices=vertices,
        pair_overlap_vertices=edges,  # type: ignore[arg-type]
        triple_overlap_vertices=triangles,  # type: ignore[arg-type]
        pair_overlaps=pair_overlaps,
        triple_overlaps=triple_overlaps,
        tetrahedron_count=len(tets),
    )
