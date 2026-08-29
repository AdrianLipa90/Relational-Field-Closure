import math

import pytest

from src.rfc.qubit_ic_full_tetra_scope_selection import (
    QubitICScopeSelectionError,
    ic_fs_shape_area,
    ic_information_curvature,
    ic_relational_area,
    minimal_qubit_ic_outcomes,
    normalized_probability_capacity,
    qubit_bloch_real_dimension,
    reconstruct_bloch,
    reconstruction_defect,
    scope_meets_minimal_qubit_ic_dimension,
    scope_outcome_count,
    scope_probability_capacity,
    selected_minimal_ic_scope,
    tetrahedral_bloch_vectors,
    tetrahedral_probabilities,
)
from src.rfc.tetra_fs_projective_refinement import FACE, FULL_TETRA_CP1


def test_qubit_dimension_lower_bound_selects_four_outcomes():
    assert qubit_bloch_real_dimension() == 3
    assert minimal_qubit_ic_outcomes() == 4
    assert normalized_probability_capacity(3) == 2
    assert normalized_probability_capacity(4) == 3


def test_rfs10_scope_capacity_selects_full_tetra_on_minimal_ic_branch():
    assert scope_outcome_count(FACE, 1) == 3
    assert scope_outcome_count(FULL_TETRA_CP1) == 4
    assert scope_probability_capacity(FACE, 1) == 2
    assert scope_probability_capacity(FULL_TETRA_CP1) == 3
    assert not scope_meets_minimal_qubit_ic_dimension(FACE, 1)
    assert scope_meets_minimal_qubit_ic_dimension(FULL_TETRA_CP1)
    assert selected_minimal_ic_scope() == FULL_TETRA_CP1


def test_tetrahedral_frame_has_exact_regular_pairwise_geometry():
    vectors = tetrahedral_bloch_vectors()
    assert len(vectors) == 4
    for vector in vectors:
        assert sum(x * x for x in vector) == pytest.approx(1.0)
    for i in range(4):
        for j in range(i + 1, 4):
            dot = sum(a * b for a, b in zip(vectors[i], vectors[j]))
            assert dot == pytest.approx(-1.0 / 3.0)
    for axis in range(3):
        assert sum(vector[axis] for vector in vectors) == pytest.approx(0.0)


@pytest.mark.parametrize(
    "r",
    [
        (0.0, 0.0, 0.0),
        (0.2, -0.3, 0.4),
        (0.7, 0.0, 0.0),
        (1.0 / math.sqrt(3.0),) * 3,
        (-0.4, 0.5, -0.2),
    ],
)
def test_tetrahedral_probabilities_reconstruct_generic_qubit_bloch_vector(r):
    probabilities = tetrahedral_probabilities(r)
    assert len(probabilities) == 4
    assert all(value >= 0.0 for value in probabilities)
    assert sum(probabilities) == pytest.approx(1.0)
    reconstructed = reconstruct_bloch(probabilities)
    assert reconstructed == pytest.approx(r, abs=1.0e-12)
    assert reconstruction_defect(r, probabilities) == pytest.approx(0.0, abs=1.0e-12)


def test_maximally_mixed_state_is_uniform_tetrahedral_probability_vector():
    probabilities = tetrahedral_probabilities((0.0, 0.0, 0.0))
    assert probabilities == pytest.approx((0.25, 0.25, 0.25, 0.25))
    assert reconstruct_bloch(probabilities) == pytest.approx((0.0, 0.0, 0.0))


def test_ic_scope_inherits_full_tetra_fs_area():
    assert ic_fs_shape_area() == pytest.approx(math.pi)
    omega = 2.5
    c = 3.0
    assert ic_relational_area(omega, c) == pytest.approx(
        math.pi * c * c / (omega * omega)
    )


def test_ic_information_curvature_matches_idt_01k_full_scope_formula():
    j_nats = 0.41
    omega = 1.7
    c = 2.3
    assert ic_information_curvature(j_nats, omega, c) == pytest.approx(
        (j_nats / math.pi) * (omega / c) ** 2
    )


def test_invalid_probability_capacity_input_fails_closed():
    for value in (0, -1):
        with pytest.raises(QubitICScopeSelectionError):
            normalized_probability_capacity(value)
    with pytest.raises(QubitICScopeSelectionError):
        normalized_probability_capacity(2.5)  # type: ignore[arg-type]


def test_invalid_bloch_vectors_fail_closed():
    with pytest.raises(QubitICScopeSelectionError):
        tetrahedral_probabilities((0.0, 0.0))
    with pytest.raises(QubitICScopeSelectionError):
        tetrahedral_probabilities((1.0, 1.0, 1.0))
    with pytest.raises(QubitICScopeSelectionError):
        tetrahedral_probabilities((math.nan, 0.0, 0.0))


def test_invalid_reconstruction_probabilities_fail_closed():
    with pytest.raises(QubitICScopeSelectionError):
        reconstruct_bloch((0.5, 0.5, 0.0))
    with pytest.raises(QubitICScopeSelectionError):
        reconstruct_bloch((0.5, 0.5, 0.1, -0.1))
    with pytest.raises(QubitICScopeSelectionError):
        reconstruct_bloch((0.4, 0.2, 0.2, 0.1))
    with pytest.raises(QubitICScopeSelectionError):
        reconstruct_bloch((0.25, 0.25, 0.25, math.inf))


def test_negative_information_numerator_fails_closed():
    with pytest.raises(QubitICScopeSelectionError):
        ic_information_curvature(-1.0, 1.0)
