import math

import pytest

from src.rfc.tetra_fs_projective_refinement import (
    FACE,
    FULL_TETRA_CP1,
    TetraFSProjectiveRefinementError,
    constant_phase_relational_area,
    fs_shape_area,
    full_area_from_face_quadratures,
    full_area_from_faces,
    information_curvature,
    refinement_defect,
    refinement_ratio,
    uniform_face_defect,
)


def test_tir_exact_projective_shape_areas():
    assert fs_shape_area(FACE, 1) == pytest.approx(math.pi / 4.0)
    assert fs_shape_area(FACE, 4) == pytest.approx(math.pi / 4.0)
    assert fs_shape_area(FULL_TETRA_CP1) == pytest.approx(math.pi)
    assert refinement_ratio() == pytest.approx(4.0)


def test_idt_01k_constant_rate_full_is_four_faces():
    omega = 2.3
    c = 3.1
    face = constant_phase_relational_area(FACE, omega, c, face_id=2)
    full = constant_phase_relational_area(FULL_TETRA_CP1, omega, c)
    assert full == pytest.approx(4.0 * face)
    assert refinement_defect(full, (face, face, face, face)) == pytest.approx(0.0)


def test_refinement_ratio_is_independent_of_clock_units():
    for omega, c in ((0.7, 1.0), (3.2, 2.0), (11.0, 299792458.0)):
        face = constant_phase_relational_area(FACE, omega, c, face_id=1)
        full = constant_phase_relational_area(FULL_TETRA_CP1, omega, c)
        assert full / face == pytest.approx(4.0)


def test_full_area_is_exact_sum_of_four_supplied_faces():
    faces = (0.3, 0.4, 0.5, 0.6)
    full = full_area_from_faces(faces)
    assert full == pytest.approx(1.8)
    assert refinement_defect(full, faces) == pytest.approx(0.0)
    assert uniform_face_defect(faces) > 0.0


def test_nonuniform_phase_rates_preserve_sum_but_not_uniform_factor_four():
    weights = (
        (math.pi / 8.0, math.pi / 8.0),
        (math.pi / 8.0, math.pi / 8.0),
        (math.pi / 8.0, math.pi / 8.0),
        (math.pi / 8.0, math.pi / 8.0),
    )
    rates = (
        (1.0, 1.0),
        (1.2, 1.2),
        (1.5, 1.5),
        (2.0, 2.0),
    )
    full, faces = full_area_from_face_quadratures(weights, rates, c=1.0)
    assert full == pytest.approx(sum(faces))
    assert refinement_defect(full, faces) == pytest.approx(0.0)
    assert uniform_face_defect(faces) > 0.0
    assert full != pytest.approx(4.0 * faces[0])


def test_uniform_nonuniform_quadrature_recovers_four_equal_faces():
    weights = tuple((math.pi / 8.0, math.pi / 8.0) for _ in range(4))
    rates = tuple((1.75, 1.75) for _ in range(4))
    full, faces = full_area_from_face_quadratures(weights, rates, c=2.0)
    assert uniform_face_defect(faces) == pytest.approx(0.0)
    assert full == pytest.approx(4.0 * faces[0])
    assert full == pytest.approx(
        constant_phase_relational_area(FULL_TETRA_CP1, 1.75, 2.0)
    )


def test_information_curvature_face_full_specialization_for_same_numerator():
    j_nats = 0.37
    omega = 2.4
    c = 1.7
    xi_face = information_curvature(j_nats, FACE, omega, c, face_id=3)
    xi_full = information_curvature(j_nats, FULL_TETRA_CP1, omega, c)
    assert xi_face == pytest.approx(
        (4.0 * j_nats / math.pi) * (omega / c) ** 2
    )
    assert xi_full == pytest.approx(
        (j_nats / math.pi) * (omega / c) ** 2
    )
    assert xi_face == pytest.approx(4.0 * xi_full)


@pytest.mark.parametrize("face_id", [None, 0, 5, -1])
def test_face_scope_requires_canonical_face_id(face_id):
    with pytest.raises(TetraFSProjectiveRefinementError):
        fs_shape_area(FACE, face_id)


def test_full_scope_rejects_face_id():
    with pytest.raises(TetraFSProjectiveRefinementError):
        fs_shape_area(FULL_TETRA_CP1, 1)


def test_invalid_scope_and_nonpositive_rate_fail_closed():
    with pytest.raises(TetraFSProjectiveRefinementError):
        fs_shape_area("UNKNOWN")
    with pytest.raises(TetraFSProjectiveRefinementError):
        constant_phase_relational_area(FACE, 0.0, face_id=1)
    with pytest.raises(TetraFSProjectiveRefinementError):
        constant_phase_relational_area(FULL_TETRA_CP1, -1.0)


def test_refinement_requires_exactly_four_positive_face_areas():
    with pytest.raises(TetraFSProjectiveRefinementError):
        full_area_from_faces((1.0, 1.0, 1.0))
    with pytest.raises(TetraFSProjectiveRefinementError):
        full_area_from_faces((1.0, 1.0, 1.0, 0.0))
