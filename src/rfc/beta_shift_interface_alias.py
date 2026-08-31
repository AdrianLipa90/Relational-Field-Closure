"""RF-GSC3D beta-match / RFC shift interface alias checks."""
from __future__ import annotations

from dataclasses import dataclass
from math import isfinite
from typing import Sequence


class BetaShiftInterfaceAliasError(ValueError):
    """Raised when an interface alias witness fails closed."""


Vector3 = tuple[float, float, float]
Matrix3 = tuple[tuple[float, float, float], ...]


def _finite(value: float, label: str) -> float:
    out = float(value)
    if not isfinite(out):
        raise BetaShiftInterfaceAliasError(f"{label} must be finite")
    return out


def _vector3(values: Sequence[float], label: str) -> Vector3:
    if len(values) != 3:
        raise BetaShiftInterfaceAliasError(f"{label} must have length 3")
    return tuple(_finite(value, label) for value in values)  # type: ignore[return-value]


def _matrix3(values: Sequence[Sequence[float]], label: str) -> Matrix3:
    if len(values) != 3 or any(len(row) != 3 for row in values):
        raise BetaShiftInterfaceAliasError(f"{label} must be 3x3")
    return tuple(tuple(_finite(value, label) for value in row) for row in values)  # type: ignore[return-value]


def _matvec(a: Matrix3, v: Vector3) -> Vector3:
    return tuple(sum(a[i][k] * v[k] for k in range(3)) for i in range(3))  # type: ignore[return-value]


def _sub(a: Vector3, b: Vector3) -> Vector3:
    return tuple(a[i] - b[i] for i in range(3))  # type: ignore[return-value]


def _scale(alpha: float, v: Vector3) -> Vector3:
    return tuple(alpha * value for value in v)  # type: ignore[return-value]


def _max_abs(v: Vector3) -> float:
    return max(abs(value) for value in v)


@dataclass(frozen=True)
class BetaShiftAliasCertificate:
    compatible: bool
    temporal_scale: float
    coefficient_residual: float
    drift_scale_residual: float
    target_alias_residual: float
    patch_identity_status: str
    clock_identity_status: str
    theorem_status: str = "EXACT_MATCHING_ONE_FORM_COEFFICIENT_ALIAS"
    production_status: str = "SAME_PATCH_CLOCK_IDENTITY_SOURCE_BOUND"


def certify_beta_shift_interface_alias(
    *,
    tir_patch_id: str,
    rfc_patch_id: str,
    tir_clock_id: str,
    rfc_clock_id: str,
    temporal_scale: float,
    beta_theta: Sequence[float],
    b_zero: Sequence[float],
    spatial_jacobian: Sequence[Sequence[float]] | None = None,
    drift_theta: Sequence[float] | None = None,
    drift_zero: Sequence[float] | None = None,
    beta_theta_target: Sequence[float] | None = None,
    b_zero_target: Sequence[float] | None = None,
    atol: float = 1.0e-12,
) -> BetaShiftAliasCertificate:
    """Certify beta_Theta = alpha*b_0 and optional overlap equivariance."""
    if not tir_patch_id or not rfc_patch_id or tir_patch_id != rfc_patch_id:
        raise BetaShiftInterfaceAliasError("same patch identity is required")
    if not tir_clock_id or not rfc_clock_id or tir_clock_id != rfc_clock_id:
        raise BetaShiftInterfaceAliasError("same clock identity is required")

    alpha = _finite(temporal_scale, "temporal_scale")
    tol = _finite(atol, "atol")
    if alpha <= 0.0:
        raise BetaShiftInterfaceAliasError("temporal_scale must be positive")
    if tol < 0.0:
        raise BetaShiftInterfaceAliasError("atol must be non-negative")

    beta = _vector3(beta_theta, "beta_theta")
    shift = _vector3(b_zero, "b_zero")
    coefficient_residual = _max_abs(_sub(beta, _scale(alpha, shift)))
    if coefficient_residual > tol:
        raise BetaShiftInterfaceAliasError(
            f"matching coefficient alias failed; residual={coefficient_residual:.17g}"
        )

    optional = (
        spatial_jacobian,
        drift_theta,
        drift_zero,
        beta_theta_target,
        b_zero_target,
    )
    if all(value is None for value in optional):
        return BetaShiftAliasCertificate(
            compatible=True,
            temporal_scale=alpha,
            coefficient_residual=coefficient_residual,
            drift_scale_residual=0.0,
            target_alias_residual=0.0,
            patch_identity_status="SAME_PATCH_ID",
            clock_identity_status="SAME_CLOCK_ID",
        )
    if any(value is None for value in optional):
        raise BetaShiftInterfaceAliasError("complete overlap data are required together")

    a = _matrix3(spatial_jacobian, "spatial_jacobian")  # type: ignore[arg-type]
    v_theta = _vector3(drift_theta, "drift_theta")  # type: ignore[arg-type]
    v_zero = _vector3(drift_zero, "drift_zero")  # type: ignore[arg-type]
    beta_target = _vector3(beta_theta_target, "beta_theta_target")  # type: ignore[arg-type]
    shift_target = _vector3(b_zero_target, "b_zero_target")  # type: ignore[arg-type]

    drift_scale_residual = _max_abs(_sub(v_theta, _scale(alpha, v_zero)))
    if drift_scale_residual > tol:
        raise BetaShiftInterfaceAliasError(
            f"temporal drift scale failed; residual={drift_scale_residual:.17g}"
        )

    expected_beta_target = _sub(_matvec(a, beta), v_theta)
    expected_shift_target = _sub(_matvec(a, shift), v_zero)
    beta_residual = _max_abs(_sub(beta_target, expected_beta_target))
    shift_residual = _max_abs(_sub(shift_target, expected_shift_target))
    target_alias_residual = _max_abs(_sub(beta_target, _scale(alpha, shift_target)))
    worst = max(beta_residual, shift_residual, target_alias_residual)
    if worst > tol:
        raise BetaShiftInterfaceAliasError(
            f"overlap equivariance failed; residual={worst:.17g}"
        )

    return BetaShiftAliasCertificate(
        compatible=True,
        temporal_scale=alpha,
        coefficient_residual=coefficient_residual,
        drift_scale_residual=drift_scale_residual,
        target_alias_residual=target_alias_residual,
        patch_identity_status="SAME_PATCH_ID",
        clock_identity_status="SAME_CLOCK_ID",
    )
