from __future__ import annotations

import math
from dataclasses import dataclass
from itertools import permutations
from collections.abc import Sequence

from src.rfc.qubit_ic_full_tetra_scope_selection import tetrahedral_bloch_vectors


class TetraRolePermutationBindingError(ValueError):
    pass


Permutation4 = tuple[int, int, int, int]
Vector3 = tuple[float, float, float]
Matrix3 = tuple[Vector3, Vector3, Vector3]


@dataclass(frozen=True)
class RoleBindingResult:
    selected: Permutation4 | None
    best_defect: float
    accepted_count: int
    best_multiplicity: int
    candidate_count: int


def _finite(name: str, value: float) -> float:
    value = float(value)
    if not math.isfinite(value):
        raise TetraRolePermutationBindingError(f"{name} must be finite")
    return value


def validate_permutation(perm: Sequence[int]) -> Permutation4:
    if len(perm) != 4:
        raise TetraRolePermutationBindingError("tetrahedral permutation must have four entries")
    out = tuple(int(x) for x in perm)
    if any(not isinstance(x, int) for x in perm):
        raise TetraRolePermutationBindingError("permutation entries must be integers")
    if sorted(out) != [0, 1, 2, 3]:
        raise TetraRolePermutationBindingError("permutation must contain each role index 0..3 exactly once")
    return out  # type: ignore[return-value]


def permutation_parity(perm: Sequence[int]) -> int:
    p = validate_permutation(perm)
    inversions = sum(1 for i in range(4) for j in range(i + 1, 4) if p[i] > p[j])
    return 1 if inversions % 2 == 0 else -1


def all_role_permutations(oriented_only: bool = False) -> tuple[Permutation4, ...]:
    out = tuple(tuple(p) for p in permutations(range(4)))
    if oriented_only:
        out = tuple(p for p in out if permutation_parity(p) == 1)
    return out  # type: ignore[return-value]


def canonical_frame() -> tuple[Vector3, Vector3, Vector3, Vector3]:
    return tetrahedral_bloch_vectors()


def permuted_sic_frame(perm: Sequence[int]) -> tuple[Vector3, Vector3, Vector3, Vector3]:
    p = validate_permutation(perm)
    frame = canonical_frame()
    return tuple(frame[p[a]] for a in range(4))  # type: ignore[return-value]


def candidate_congruence(perm: Sequence[int]) -> Matrix3:
    pframe = permuted_sic_frame(perm)
    spatial = canonical_frame()
    rows = []
    for i in range(3):
        rows.append(
            tuple(
                0.75 * math.fsum(pframe[a][i] * spatial[a][j] for a in range(4))
                for j in range(3)
            )
        )
    return tuple(rows)  # type: ignore[return-value]


def _apply(matrix: Matrix3, vector: Vector3) -> Vector3:
    return tuple(math.fsum(matrix[i][j] * vector[j] for j in range(3)) for i in range(3))  # type: ignore[return-value]


def congruence_defect(perm: Sequence[int]) -> float:
    q = candidate_congruence(perm)
    spatial = canonical_frame()
    target = permuted_sic_frame(perm)
    return math.sqrt(
        math.fsum(
            (_apply(q, spatial[a])[i] - target[a][i]) ** 2
            for a in range(4)
            for i in range(3)
        )
    )


def orthogonality_defect(perm: Sequence[int]) -> float:
    q = candidate_congruence(perm)
    return math.sqrt(
        math.fsum(
            (
                math.fsum(q[i][k] * q[j][k] for k in range(3))
                - (1.0 if i == j else 0.0)
            )
            ** 2
            for i in range(3)
            for j in range(3)
        )
    )


def determinant_for_permutation(perm: Sequence[int]) -> float:
    q = candidate_congruence(perm)
    return (
        q[0][0] * (q[1][1] * q[2][2] - q[1][2] * q[2][1])
        - q[0][1] * (q[1][0] * q[2][2] - q[1][2] * q[2][0])
        + q[0][2] * (q[1][0] * q[2][1] - q[1][1] * q[2][0])
    )


def _signatures(name: str, values: Sequence[Sequence[float]]) -> tuple[tuple[float, ...], ...]:
    if len(values) != 4:
        raise TetraRolePermutationBindingError(f"{name} must contain four role signatures")
    if not values or len(values[0]) < 1:
        raise TetraRolePermutationBindingError(f"{name} signatures must have positive dimension")
    dimension = len(values[0])
    out = []
    for a, vector in enumerate(values):
        if len(vector) != dimension:
            raise TetraRolePermutationBindingError(f"{name} signatures must share one dimension")
        out.append(tuple(_finite(f"{name}[{a}][{i}]", value) for i, value in enumerate(vector)))
    return tuple(out)


def role_assignment_defect(
    spatial_signatures: Sequence[Sequence[float]],
    sic_signatures: Sequence[Sequence[float]],
    perm: Sequence[int],
) -> float:
    spatial = _signatures("spatial_signatures", spatial_signatures)
    sic = _signatures("sic_signatures", sic_signatures)
    if len(spatial[0]) != len(sic[0]):
        raise TetraRolePermutationBindingError("spatial and SIC signature dimensions must match")
    p = validate_permutation(perm)
    return math.sqrt(
        math.fsum(
            (spatial[a][i] - sic[p[a]][i]) ** 2
            for a in range(4)
            for i in range(len(spatial[0]))
        )
    )


def select_unique_role_binding(
    spatial_signatures: Sequence[Sequence[float]],
    sic_signatures: Sequence[Sequence[float]],
    *,
    oriented_only: bool = False,
    tolerance: float = 1.0e-12,
) -> RoleBindingResult:
    tolerance = _finite("tolerance", tolerance)
    if tolerance < 0.0:
        raise TetraRolePermutationBindingError("tolerance must be nonnegative")

    candidates = all_role_permutations(oriented_only=oriented_only)
    scored = tuple(
        (perm, role_assignment_defect(spatial_signatures, sic_signatures, perm))
        for perm in candidates
    )
    best_defect = min(score for _, score in scored)
    accepted = tuple(perm for perm, score in scored if score <= tolerance)
    best_multiplicity = sum(
        1
        for _, score in scored
        if math.isclose(score, best_defect, rel_tol=0.0, abs_tol=max(tolerance, 1.0e-15))
    )
    selected = accepted[0] if len(accepted) == 1 else None
    return RoleBindingResult(
        selected=selected,
        best_defect=best_defect,
        accepted_count=len(accepted),
        best_multiplicity=best_multiplicity,
        candidate_count=len(candidates),
    )
