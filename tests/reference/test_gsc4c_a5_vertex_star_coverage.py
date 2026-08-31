import pytest

from src.rfc.a5_vertex_star_coverage import (
    A5VertexStarCoverageError,
    derive_a5_vertex_star_coverage,
)


BOUNDARY_4_SIMPLEX = [
    (1, 2, 3, 4),
    (0, 2, 3, 4),
    (0, 1, 3, 4),
    (0, 1, 2, 4),
    (0, 1, 2, 3),
]


def test_boundary_of_4_simplex_generates_complete_vertex_star_cover_incidence():
    cert = derive_a5_vertex_star_coverage(
        BOUNDARY_4_SIMPLEX,
        a5_manifold_certified=True,
        a5_parent_certificate_id="A5:S3:boundary4simplex",
    )
    assert cert.coverage_exact is True
    assert len(cert.vertices) == 5
    assert len(cert.patch_ids) == 5
    assert len(cert.pair_overlaps) == 10
    assert len(cert.triple_overlaps) == 10
    assert cert.tetrahedron_count == 5


def test_pair_overlap_incidence_is_exactly_edge_incidence():
    cert = derive_a5_vertex_star_coverage(
        [(0, 1, 2, 3), (0, 1, 2, 4)],
        a5_manifold_certified=True,
        a5_parent_certificate_id="A5:test",
    )
    assert (3, 4) not in cert.pair_overlap_vertices
    assert (0, 4) in cert.pair_overlap_vertices
    assert (1, 3) in cert.pair_overlap_vertices


def test_triple_overlap_incidence_is_exactly_triangle_incidence():
    cert = derive_a5_vertex_star_coverage(
        [(0, 1, 2, 3), (0, 1, 2, 4)],
        a5_manifold_certified=True,
        a5_parent_certificate_id="A5:test",
    )
    assert (0, 3, 4) not in cert.triple_overlap_vertices
    assert (0, 1, 2) in cert.triple_overlap_vertices
    assert (0, 1, 4) in cert.triple_overlap_vertices


def test_coverage_generator_keeps_geometry_values_open():
    cert = derive_a5_vertex_star_coverage(
        BOUNDARY_4_SIMPLEX,
        a5_manifold_certified=True,
        a5_parent_certificate_id="A5:S3",
    )
    assert cert.production_geometry_values_status == "OPEN_SOURCE_GEOMETRY_PACKET"


def test_missing_a5_parent_fails_closed():
    with pytest.raises(A5VertexStarCoverageError, match="A5 manifold certificate"):
        derive_a5_vertex_star_coverage(
            [(0, 1, 2, 3)],
            a5_manifold_certified=False,
            a5_parent_certificate_id="A5:none",
        )


def test_repeated_vertex_tetrahedron_fails_closed():
    with pytest.raises(A5VertexStarCoverageError, match="repeated vertices"):
        derive_a5_vertex_star_coverage(
            [(0, 0, 1, 2)],
            a5_manifold_certified=True,
            a5_parent_certificate_id="A5:test",
        )


def test_duplicate_tetrahedron_fails_closed_independent_of_ordering():
    with pytest.raises(A5VertexStarCoverageError, match="duplicate tetrahedron"):
        derive_a5_vertex_star_coverage(
            [(0, 1, 2, 3), (3, 2, 1, 0)],
            a5_manifold_certified=True,
            a5_parent_certificate_id="A5:test",
        )
