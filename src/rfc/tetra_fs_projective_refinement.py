from __future__ import annotations

import math
from collections.abc import Sequence


FACE = "FACE"
FULL_TETRA_CP1 = "FULL_TETRA_CP1"
_VALID_SCOPES = {FACE, FULL_TETRA_CP1}


class TetraFSProjectiveRefinementError(ValueError):
    pass


def _finite(name: str, value: float) -> float:
    value = float(value)
    if not math.isfinite(value):
        raise TetraFSProjectiveRefinementError(f"{name} must be finite")
    return value


def _positive(name: str, value: float) -> float:
    value = _finite(name, value)
    if value <= 0.0:
        raise TetraFSProjectiveRefinementError(f"{name} must be positive")
    return value


def _nonnegative(name: str, value: float) -> float:
    value = _finite(name, value)
    if value < 0.0:
        raise TetraFSProjectiveRefinementError(f"{name} must be nonnegative")
    return value


def validate_scope(scope: str, face_id: int | None = None) -> tuple[str, int | None]:
    if scope not in _VALID_SCOPES:
        raise TetraFSProjectiveRefinementError(
            f"scope must be one of {sorted(_VALID_SCOPES)}"
        )
    if scope == FACE:
        if face_id not in (1, 2, 3, 4):
            raise TetraFSProjectiveRefinementError(
                "FACE scope requires face_id in {1,2,3,4}"
            )
    elif face_id is not None:
        raise TetraFSProjectiveRefinementError(
            "FULL_TETRA_CP1 scope carries no face_id"
        )
    return scope, face_id


def fs_shape_area(scope: str, face_id: int | None = None) -> float:
    scope, _ = validate_scope(scope, face_id)
    if scope == FACE:
        return math.pi / 4.0
    return math.pi


def constant_phase_relational_area(
    scope: str,
    omega: float,
    c: float = 1.0,
    face_id: int | None = None,
) -> float:
    omega = _positive("omega", omega)
    c = _positive("c", c)
    return (c * c / (omega * omega)) * fs_shape_area(scope, face_id)


def refinement_ratio() -> float:
    return fs_shape_area(FULL_TETRA_CP1) / fs_shape_area(FACE, 1)


def refinement_defect(full_area: float, face_areas: Sequence[float]) -> float:
    full_area = _positive("full_area", full_area)
    if len(face_areas) != 4:
        raise TetraFSProjectiveRefinementError(
            "tetrahedral refinement requires exactly four face areas"
        )
    faces = tuple(_positive(f"face_areas[{i}]", value) for i, value in enumerate(face_areas))
    summed = math.fsum(faces)
    return abs(full_area - summed) / (full_area + summed)


def full_area_from_faces(face_areas: Sequence[float]) -> float:
    if len(face_areas) != 4:
        raise TetraFSProjectiveRefinementError(
            "tetrahedral refinement requires exactly four face areas"
        )
    return math.fsum(
        _positive(f"face_areas[{i}]", value)
        for i, value in enumerate(face_areas)
    )


def uniform_face_defect(face_areas: Sequence[float]) -> float:
    if len(face_areas) != 4:
        raise TetraFSProjectiveRefinementError(
            "tetrahedral refinement requires exactly four face areas"
        )
    faces = tuple(_positive(f"face_areas[{i}]", value) for i, value in enumerate(face_areas))
    mean = math.fsum(faces) / 4.0
    return max(abs(value - mean) for value in faces) / mean


def full_area_from_face_quadratures(
    face_da_fs_weights: Sequence[Sequence[float]],
    face_omega_values: Sequence[Sequence[float]],
    c: float = 1.0,
) -> tuple[float, tuple[float, float, float, float]]:
    if len(face_da_fs_weights) != 4 or len(face_omega_values) != 4:
        raise TetraFSProjectiveRefinementError(
            "tetrahedral quadrature requires four face partitions"
        )
    c = _positive("c", c)
    face_areas: list[float] = []
    for f, (weights, rates) in enumerate(
        zip(face_da_fs_weights, face_omega_values), start=1
    ):
        if not weights or len(weights) != len(rates):
            raise TetraFSProjectiveRefinementError(
                f"face {f} weights and rates must be nonempty and aligned"
            )
        checked_weights = tuple(
            _nonnegative(f"face{f}.weight[{i}]", value)
            for i, value in enumerate(weights)
        )
        if math.fsum(checked_weights) <= 0.0:
            raise TetraFSProjectiveRefinementError(
                f"face {f} must carry positive projective area"
            )
        checked_rates = tuple(
            _positive(f"face{f}.omega[{i}]", value)
            for i, value in enumerate(rates)
        )
        face_areas.append(
            math.fsum(
                (c * c / (omega * omega)) * weight
                for weight, omega in zip(checked_weights, checked_rates)
            )
        )
    face_tuple = tuple(face_areas)
    return math.fsum(face_tuple), face_tuple  # type: ignore[return-value]


def information_curvature(
    j_nats: float,
    scope: str,
    omega: float,
    c: float = 1.0,
    face_id: int | None = None,
) -> float:
    j_nats = _nonnegative("j_nats", j_nats)
    area = constant_phase_relational_area(scope, omega, c, face_id)
    return j_nats / area
