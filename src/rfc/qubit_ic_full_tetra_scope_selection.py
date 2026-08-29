from __future__ import annotations

import math
from collections.abc import Sequence

from src.rfc.tetra_fs_projective_refinement import (
    FACE,
    FULL_TETRA_CP1,
    constant_phase_relational_area,
    fs_shape_area,
    validate_scope,
)


class QubitICScopeSelectionError(ValueError):
    pass


def _finite(name: str, value: float) -> float:
    value = float(value)
    if not math.isfinite(value):
        raise QubitICScopeSelectionError(f"{name} must be finite")
    return value


def qubit_bloch_real_dimension() -> int:
    return 3


def normalized_probability_capacity(outcome_count: int) -> int:
    if not isinstance(outcome_count, int) or outcome_count < 1:
        raise QubitICScopeSelectionError("outcome_count must be a positive integer")
    return outcome_count - 1


def minimal_qubit_ic_outcomes() -> int:
    return qubit_bloch_real_dimension() + 1


def scope_outcome_count(scope: str, face_id: int | None = None) -> int:
    validate_scope(scope, face_id)
    if scope == FACE:
        return 3
    return 4


def scope_probability_capacity(scope: str, face_id: int | None = None) -> int:
    return normalized_probability_capacity(scope_outcome_count(scope, face_id))


def scope_meets_minimal_qubit_ic_dimension(
    scope: str,
    face_id: int | None = None,
) -> bool:
    return scope_probability_capacity(scope, face_id) >= qubit_bloch_real_dimension()


def selected_minimal_ic_scope() -> str:
    full_capacity = scope_probability_capacity(FULL_TETRA_CP1)
    if full_capacity != qubit_bloch_real_dimension():
        raise QubitICScopeSelectionError("FULL_TETRA_CP1 capacity mismatch")
    return FULL_TETRA_CP1


def tetrahedral_bloch_vectors() -> tuple[tuple[float, float, float], ...]:
    inv = 1.0 / math.sqrt(3.0)
    return (
        (inv, inv, inv),
        (inv, -inv, -inv),
        (-inv, inv, -inv),
        (-inv, -inv, inv),
    )


def _bloch_vector(r: Sequence[float]) -> tuple[float, float, float]:
    if len(r) != 3:
        raise QubitICScopeSelectionError("Bloch vector must have three coordinates")
    out = tuple(_finite(f"r[{i}]", value) for i, value in enumerate(r))
    norm_sq = math.fsum(value * value for value in out)
    if norm_sq > 1.0 + 1.0e-12:
        raise QubitICScopeSelectionError("Bloch vector must lie in the unit ball")
    return out  # type: ignore[return-value]


def tetrahedral_probabilities(r: Sequence[float]) -> tuple[float, float, float, float]:
    rv = _bloch_vector(r)
    probs = []
    for n in tetrahedral_bloch_vectors():
        dot = math.fsum(a * b for a, b in zip(rv, n))
        probs.append(0.25 * (1.0 + dot))
    if any(value < -1.0e-12 for value in probs):
        raise QubitICScopeSelectionError("tetrahedral probability became negative")
    probs = [max(0.0, value) for value in probs]
    total = math.fsum(probs)
    if not math.isclose(total, 1.0, rel_tol=0.0, abs_tol=1.0e-12):
        raise QubitICScopeSelectionError("tetrahedral probabilities must sum to one")
    return tuple(probs)  # type: ignore[return-value]


def _probabilities(p: Sequence[float]) -> tuple[float, float, float, float]:
    if len(p) != 4:
        raise QubitICScopeSelectionError("tetrahedral reconstruction requires four probabilities")
    out = tuple(_finite(f"p[{i}]", value) for i, value in enumerate(p))
    if any(value < 0.0 for value in out):
        raise QubitICScopeSelectionError("probabilities must be nonnegative")
    if not math.isclose(math.fsum(out), 1.0, rel_tol=0.0, abs_tol=1.0e-12):
        raise QubitICScopeSelectionError("probabilities must sum to one")
    return out  # type: ignore[return-value]


def reconstruct_bloch(p: Sequence[float]) -> tuple[float, float, float]:
    probs = _probabilities(p)
    vectors = tetrahedral_bloch_vectors()
    return tuple(
        3.0 * math.fsum(probs[a] * vectors[a][i] for a in range(4))
        for i in range(3)
    )  # type: ignore[return-value]


def reconstruction_defect(r: Sequence[float], p: Sequence[float]) -> float:
    rv = _bloch_vector(r)
    recon = reconstruct_bloch(p)
    return math.sqrt(math.fsum((a - b) ** 2 for a, b in zip(rv, recon)))


def ic_fs_shape_area() -> float:
    return fs_shape_area(selected_minimal_ic_scope())


def ic_relational_area(omega: float, c: float = 1.0) -> float:
    return constant_phase_relational_area(selected_minimal_ic_scope(), omega, c)


def ic_information_curvature(j_nats: float, omega: float, c: float = 1.0) -> float:
    j_nats = _finite("j_nats", j_nats)
    if j_nats < 0.0:
        raise QubitICScopeSelectionError("j_nats must be nonnegative")
    return j_nats / ic_relational_area(omega, c)
