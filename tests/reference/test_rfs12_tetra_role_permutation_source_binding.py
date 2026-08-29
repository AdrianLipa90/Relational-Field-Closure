import math

import pytest

from src.rfc.tetra_role_permutation_source_binding import (
    TetraRolePermutationBindingError,
    all_role_permutations,
    candidate_congruence,
    congruence_defect,
    determinant_for_permutation,
    orthogonality_defect,
    permutation_parity,
    role_assignment_defect,
    select_unique_role_binding,
    validate_permutation,
)


def test_tetrahedral_residual_role_set_is_s4_and_oriented_a4():
    all_perms = all_role_permutations(oriented_only=False)
    oriented = all_role_permutations(oriented_only=True)
    assert len(all_perms) == 24
    assert len(set(all_perms)) == 24
    assert len(oriented) == 12
    assert all(permutation_parity(perm) == 1 for perm in oriented)


def test_every_role_permutation_has_exact_orthogonal_tetrahedral_congruence():
    for perm in all_role_permutations():
        assert congruence_defect(perm) == pytest.approx(0.0, abs=1.0e-12)
        assert orthogonality_defect(perm) == pytest.approx(0.0, abs=1.0e-12)
        assert abs(determinant_for_permutation(perm)) == pytest.approx(1.0, abs=1.0e-12)


def test_compatible_orientation_makes_determinant_equal_permutation_parity():
    for perm in all_role_permutations():
        assert determinant_for_permutation(perm) == pytest.approx(
            float(permutation_parity(perm)), abs=1.0e-12
        )


def test_identity_role_order_has_identity_congruence():
    q = candidate_congruence((0, 1, 2, 3))
    expected = (
        (1.0, 0.0, 0.0),
        (0.0, 1.0, 0.0),
        (0.0, 0.0, 1.0),
    )
    for row, target in zip(q, expected):
        assert row == pytest.approx(target, abs=1.0e-12)


def test_unique_even_zero_defect_signature_binding_is_selected_in_a4():
    spatial = ((10.0,), (20.0,), (30.0,), (40.0,))
    true_perm = (1, 0, 3, 2)
    assert permutation_parity(true_perm) == 1
    sic = ((20.0,), (10.0,), (40.0,), (30.0,))

    assert role_assignment_defect(spatial, sic, true_perm) == pytest.approx(0.0)
    result = select_unique_role_binding(
        spatial,
        sic,
        oriented_only=True,
        tolerance=1.0e-12,
    )
    assert result.selected == true_perm
    assert result.accepted_count == 1
    assert result.best_multiplicity == 1
    assert result.candidate_count == 12
    assert result.best_defect == pytest.approx(0.0)


def test_odd_exact_binding_is_visible_unoriented_and_excluded_by_oriented_ledger():
    spatial = ((1.0,), (2.0,), (3.0,), (4.0,))
    odd_perm = (1, 0, 2, 3)
    assert permutation_parity(odd_perm) == -1
    sic = ((2.0,), (1.0,), (3.0,), (4.0,))

    unoriented = select_unique_role_binding(spatial, sic, oriented_only=False)
    assert unoriented.selected == odd_perm
    assert unoriented.accepted_count == 1
    assert unoriented.candidate_count == 24

    oriented = select_unique_role_binding(spatial, sic, oriented_only=True)
    assert oriented.selected is None
    assert oriented.accepted_count == 0
    assert oriented.candidate_count == 12
    assert oriented.best_defect > 0.0


def test_symmetric_role_signatures_preserve_full_residual_permutation_symmetry():
    spatial = ((1.0, 2.0),) * 4
    sic = ((1.0, 2.0),) * 4

    unoriented = select_unique_role_binding(spatial, sic, oriented_only=False)
    assert unoriented.selected is None
    assert unoriented.accepted_count == 24
    assert unoriented.best_multiplicity == 24

    oriented = select_unique_role_binding(spatial, sic, oriented_only=True)
    assert oriented.selected is None
    assert oriented.accepted_count == 12
    assert oriented.best_multiplicity == 12


def test_mismatched_source_ledgers_have_no_zero_defect_binding():
    spatial = ((0.0,), (1.0,), (2.0,), (3.0,))
    sic = ((10.0,), (11.0,), (12.0,), (13.0,))
    result = select_unique_role_binding(spatial, sic, tolerance=1.0e-12)
    assert result.selected is None
    assert result.accepted_count == 0
    assert result.best_defect > 0.0


def test_multidimensional_signature_binding_works_componentwise():
    spatial = ((1.0, 5.0), (2.0, 6.0), (3.0, 7.0), (4.0, 8.0))
    true_perm = (2, 3, 0, 1)
    assert permutation_parity(true_perm) == 1
    sic = ((3.0, 7.0), (4.0, 8.0), (1.0, 5.0), (2.0, 6.0))
    result = select_unique_role_binding(spatial, sic, oriented_only=True)
    assert result.selected == true_perm
    assert result.best_defect == pytest.approx(0.0)


@pytest.mark.parametrize(
    "perm",
    [
        (0, 1, 2),
        (0, 1, 2, 2),
        (0, 1, 2, 4),
        (0, 1, -1, 3),
    ],
)
def test_invalid_permutations_fail_closed(perm):
    with pytest.raises(TetraRolePermutationBindingError):
        validate_permutation(perm)


def test_invalid_source_signature_shapes_and_values_fail_closed():
    with pytest.raises(TetraRolePermutationBindingError):
        select_unique_role_binding(((1.0,),) * 3, ((1.0,),) * 4)
    with pytest.raises(TetraRolePermutationBindingError):
        select_unique_role_binding(
            ((1.0,), (2.0, 3.0), (4.0,), (5.0,)),
            ((1.0,),) * 4,
        )
    with pytest.raises(TetraRolePermutationBindingError):
        select_unique_role_binding(
            ((1.0,),) * 4,
            ((1.0, 2.0),) * 4,
        )
    with pytest.raises(TetraRolePermutationBindingError):
        select_unique_role_binding(
            ((1.0,), (2.0,), (3.0,), (math.nan,)),
            ((1.0,),) * 4,
        )


def test_negative_or_nonfinite_tolerance_fails_closed():
    signatures = ((1.0,), (2.0,), (3.0,), (4.0,))
    with pytest.raises(TetraRolePermutationBindingError):
        select_unique_role_binding(signatures, signatures, tolerance=-1.0)
    with pytest.raises(TetraRolePermutationBindingError):
        select_unique_role_binding(signatures, signatures, tolerance=math.inf)
