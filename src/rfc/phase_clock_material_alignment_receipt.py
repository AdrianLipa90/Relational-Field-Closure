from __future__ import annotations

import math
from dataclasses import dataclass
from collections.abc import Sequence


class PhaseClockMaterialAlignmentError(ValueError):
    pass


def _finite(name: str, value: float) -> float:
    value = float(value)
    if not math.isfinite(value):
        raise PhaseClockMaterialAlignmentError(f"{name} must be finite")
    return value


def _positive(name: str, value: float) -> float:
    value = _finite(name, value)
    if value <= 0.0:
        raise PhaseClockMaterialAlignmentError(f"{name} must be positive")
    return value


def _vec4(name: str, values: Sequence[float]) -> tuple[float, ...]:
    if len(values) != 4:
        raise PhaseClockMaterialAlignmentError(f"{name} must have length 4")
    return tuple(_finite(f"{name}[{i}]", value) for i, value in enumerate(values))


def _metric(name: str, values: Sequence[Sequence[float]]) -> tuple[tuple[float, ...], ...]:
    if len(values) != 4 or any(len(row) != 4 for row in values):
        raise PhaseClockMaterialAlignmentError(f"{name} must be 4x4")
    matrix = tuple(
        tuple(_finite(f"{name}[{i}][{j}]", value) for j, value in enumerate(row))
        for i, row in enumerate(values)
    )
    for i in range(4):
        for j in range(4):
            if matrix[i][j] != matrix[j][i]:
                raise PhaseClockMaterialAlignmentError(f"{name} must be symmetric")
    return matrix


def _mat_vec(matrix: Sequence[Sequence[float]], vector: Sequence[float]) -> tuple[float, ...]:
    return tuple(sum(matrix[i][j] * vector[j] for j in range(4)) for i in range(4))


def _dot_cov_contra(covector: Sequence[float], vector: Sequence[float]) -> float:
    return sum(covector[i] * vector[i] for i in range(4))


def _vector_norm(metric: Sequence[Sequence[float]], vector: Sequence[float]) -> float:
    covector = _mat_vec(metric, vector)
    return _dot_cov_contra(covector, vector)


def _covector_norm(inverse_metric: Sequence[Sequence[float]], covector: Sequence[float]) -> float:
    vector = _mat_vec(inverse_metric, covector)
    return _dot_cov_contra(covector, vector)


@dataclass(frozen=True)
class AlignmentLineage:
    u1_bundle: str
    phase_patch: str
    connection: str
    slice_id: str
    coframe: str
    measure: str
    support: str

    def __post_init__(self) -> None:
        for name, value in (
            ("u1_bundle", self.u1_bundle),
            ("phase_patch", self.phase_patch),
            ("connection", self.connection),
            ("slice_id", self.slice_id),
            ("coframe", self.coframe),
            ("measure", self.measure),
            ("support", self.support),
        ):
            if not isinstance(value, str) or not value:
                raise PhaseClockMaterialAlignmentError(f"{name} must be a nonempty string")


def lineage_defects(phase: AlignmentLineage, current: AlignmentLineage) -> dict[str, float]:
    return {
        "u1_bundle": 0.0 if phase.u1_bundle == current.u1_bundle else 1.0,
        "phase_patch": 0.0 if phase.phase_patch == current.phase_patch else 1.0,
        "connection": 0.0 if phase.connection == current.connection else 1.0,
        "slice": 0.0 if phase.slice_id == current.slice_id else 1.0,
        "coframe": 0.0 if phase.coframe == current.coframe else 1.0,
        "measure": 0.0 if phase.measure == current.measure else 1.0,
        "support": 0.0 if phase.support == current.support else 1.0,
    }


def metric_inverse_defect(
    metric: Sequence[Sequence[float]],
    inverse_metric: Sequence[Sequence[float]],
) -> float:
    g = _metric("metric", metric)
    g_inv = _metric("inverse_metric", inverse_metric)
    return max(
        abs(sum(g[i][a] * g_inv[a][j] for a in range(4)) - (1.0 if i == j else 0.0))
        for i in range(4)
        for j in range(4)
    )


def normalized_material_current(
    metric: Sequence[Sequence[float]],
    current: Sequence[float],
) -> tuple[float, ...]:
    g = _metric("metric", metric)
    J = _vec4("current", current)
    norm2 = _vector_norm(g, J)
    if norm2 >= 0.0:
        raise PhaseClockMaterialAlignmentError("material current must be timelike and nonzero")
    scale = math.sqrt(-norm2)
    return tuple(value / scale for value in J)


def phase_clock_material_alignment_receipt(
    *,
    metric: Sequence[Sequence[float]],
    inverse_metric: Sequence[Sequence[float]],
    phase_covector: Sequence[float],
    phase_scale: float,
    material_current: Sequence[float],
    slice_normal: Sequence[float],
    phase_lineage: AlignmentLineage,
    current_lineage: AlignmentLineage,
) -> dict[str, object]:
    """Independent RF-F18 phase-clock <-> RF-E19 material-current alignment audit."""
    g = _metric("metric", metric)
    g_inv = _metric("inverse_metric", inverse_metric)
    q = _vec4("phase_covector", phase_covector)
    mu = _positive("phase_scale", phase_scale)
    J = _vec4("material_current", material_current)
    n = _vec4("slice_normal", slice_normal)

    inverse_defect = metric_inverse_defect(g, g_inv)
    slice_norm2 = _vector_norm(g, n)
    current_norm2 = _vector_norm(g, J)
    if current_norm2 >= 0.0:
        raise PhaseClockMaterialAlignmentError("material current must be timelike and nonzero")

    nu = normalized_material_current(g, J)
    v_cov = tuple(value / mu for value in q)
    v_contra = _mat_vec(g_inv, v_cov)
    phase_projector = -_covector_norm(g_inv, q) / (mu * mu)

    n_cov = _mat_vec(g, n)
    current_future_measure = -_dot_cov_contra(n_cov, J)
    phase_future_measure = -_dot_cov_contra(v_cov, n)

    gamma_vartheta_j = -_dot_cov_contra(v_cov, nu)

    defects: dict[str, float] = {
        "metric_inverse": inverse_defect,
        "slice_unit": abs(slice_norm2 + 1.0),
        "phase_projector": abs(phase_projector - 1.0),
        "current_unit_after_normalization": abs(_vector_norm(g, nu) + 1.0),
        "phase_future_orientation": 0.0 if phase_future_measure > 0.0 else 1.0,
        "current_future_orientation": 0.0 if current_future_measure > 0.0 else 1.0,
        "alignment": abs(gamma_vartheta_j - 1.0),
    }
    defects.update(
        {f"lineage_{name}": value for name, value in lineage_defects(phase_lineage, current_lineage).items()}
    )

    return {
        "phase_projector": phase_projector,
        "phase_covector_normalized": v_cov,
        "phase_vector_normalized": v_contra,
        "material_current_norm2": current_norm2,
        "material_velocity": nu,
        "phase_future_measure": phase_future_measure,
        "current_future_measure": current_future_measure,
        "gamma_vartheta_j": gamma_vartheta_j,
        "delta_vartheta_j": abs(gamma_vartheta_j - 1.0),
        "defects": defects,
        "max_defect": max(defects.values()),
    }


def receipt_passes(receipt: dict[str, object], *, atol: float = 0.0) -> bool:
    tol = _finite("atol", atol)
    if tol < 0.0:
        raise PhaseClockMaterialAlignmentError("atol must be nonnegative")
    defects = receipt.get("defects")
    if not isinstance(defects, dict):
        raise PhaseClockMaterialAlignmentError("receipt must contain a defects mapping")
    return all(abs(_finite(f"defect[{name}]", value)) <= tol for name, value in defects.items())
