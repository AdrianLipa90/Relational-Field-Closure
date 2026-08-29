from __future__ import annotations

import math
from collections.abc import Sequence

from src.rfc.abe_euler_metric_response import projector_metric_derivative


class EinsteinSourceAssemblyError(ValueError):
    pass


def _finite(name: str, value: float) -> float:
    value = float(value)
    if not math.isfinite(value):
        raise EinsteinSourceAssemblyError(f"{name} must be finite")
    return value


def _positive(name: str, value: float) -> float:
    value = _finite(name, value)
    if value <= 0.0:
        raise EinsteinSourceAssemblyError(f"{name} must be positive")
    return value


def _eta(value: float) -> float:
    value = _finite("eta", value)
    if not 0.0 <= value <= 1.0:
        raise EinsteinSourceAssemblyError("eta must lie in [0,1]")
    return value


def _vec4(name: str, values: Sequence[float]) -> tuple[float, ...]:
    if len(values) != 4:
        raise EinsteinSourceAssemblyError(f"{name} must have length 4")
    return tuple(_finite(f"{name}[{i}]", value) for i, value in enumerate(values))


def _mat4(name: str, values: Sequence[Sequence[float]]) -> tuple[tuple[float, ...], ...]:
    if len(values) != 4 or any(len(row) != 4 for row in values):
        raise EinsteinSourceAssemblyError(f"{name} must be 4x4")
    return tuple(
        tuple(_finite(f"{name}[{i}][{j}]", value) for j, value in enumerate(row))
        for i, row in enumerate(values)
    )


def _add(*matrices: Sequence[Sequence[float]]) -> tuple[tuple[float, ...], ...]:
    parsed = [_mat4(f"matrix[{i}]", matrix) for i, matrix in enumerate(matrices)]
    if not parsed:
        return tuple(tuple(0.0 for _ in range(4)) for _ in range(4))
    return tuple(tuple(sum(matrix[i][j] for matrix in parsed) for j in range(4)) for i in range(4))


def _scale(value: float, matrix: Sequence[Sequence[float]]) -> tuple[tuple[float, ...], ...]:
    coefficient = _finite("coefficient", value)
    parsed = _mat4("matrix", matrix)
    return tuple(tuple(coefficient * parsed[i][j] for j in range(4)) for i in range(4))


def lambda0_from_reference(lambda_star: float, kappa_e: float, u_hat: float) -> float:
    return _finite("lambda_star", lambda_star) + _positive("kappa_e", kappa_e) * _finite("u_hat", u_hat)


def projector_interaction_stress_from_derivative(
    eta: float,
    u_hat: float,
    f_prime_at_one: float,
    projector_derivative: Sequence[Sequence[float]],
) -> tuple[tuple[float, ...], ...]:
    """D_mn=-2 eta Uhat f'(1) partial C/partial g^{mn}."""
    eta_value = _eta(eta)
    U = _finite("u_hat", u_hat)
    fp = _finite("f_prime_at_one", f_prime_at_one)
    dC = _mat4("projector_derivative", projector_derivative)
    return _scale(-2.0 * eta_value * U * fp, dC)


def projector_interaction_stress_from_f20(
    *,
    eta: float,
    u_hat: float,
    f_prime_at_one: float,
    phase_covector: Sequence[float],
    phase_scale: float,
    contracted_abe_response: Sequence[Sequence[float]],
    scale_log_metric_response: Sequence[Sequence[float]] | None = None,
    projector_value: float = 1.0,
) -> tuple[tuple[float, ...], ...]:
    dC = projector_metric_derivative(
        phase_covector,
        phase_scale,
        contracted_abe_response,
        projector_value=projector_value,
        scale_log_metric_response=scale_log_metric_response,
    )
    return projector_interaction_stress_from_derivative(eta, u_hat, f_prime_at_one, dC)


def fixed_reference_u_sector(
    metric: Sequence[Sequence[float]],
    *,
    eta: float,
    u_hat: float,
    projector_stress: Sequence[Sequence[float]],
) -> tuple[tuple[float, ...], ...]:
    """U-sector with constant Lambda_star kept on geometry side."""
    g = _mat4("metric", metric)
    eta_value = _eta(eta)
    U = _finite("u_hat", u_hat)
    D = _mat4("projector_stress", projector_stress)
    return _add(_scale(-(1.0 - eta_value) * U, g), D)


def dynamic_lambda_u_sector(
    metric: Sequence[Sequence[float]],
    *,
    eta: float,
    u_hat: float,
    projector_stress: Sequence[Sequence[float]],
) -> tuple[tuple[float, ...], ...]:
    """U-sector after moving -Uhat*g to Lambda0=Lambda_star+kappa_E Uhat."""
    g = _mat4("metric", metric)
    eta_value = _eta(eta)
    U = _finite("u_hat", u_hat)
    D = _mat4("projector_stress", projector_stress)
    return _add(_scale(eta_value * U, g), D)


def assemble_fixed_reference_source(
    rest_source: Sequence[Sequence[float]],
    metric: Sequence[Sequence[float]],
    *,
    eta: float,
    u_hat: float,
    projector_stress: Sequence[Sequence[float]],
) -> tuple[tuple[float, ...], ...]:
    return _add(
        rest_source,
        fixed_reference_u_sector(metric, eta=eta, u_hat=u_hat, projector_stress=projector_stress),
    )


def assemble_dynamic_lambda_source(
    rest_source: Sequence[Sequence[float]],
    metric: Sequence[Sequence[float]],
    *,
    eta: float,
    u_hat: float,
    projector_stress: Sequence[Sequence[float]],
) -> tuple[tuple[float, ...], ...]:
    return _add(
        rest_source,
        dynamic_lambda_u_sector(metric, eta=eta, u_hat=u_hat, projector_stress=projector_stress),
    )


def source_repartition_difference(
    dynamic_source: Sequence[Sequence[float]],
    fixed_source: Sequence[Sequence[float]],
) -> tuple[tuple[float, ...], ...]:
    dynamic = _mat4("dynamic_source", dynamic_source)
    fixed = _mat4("fixed_source", fixed_source)
    return tuple(tuple(dynamic[i][j] - fixed[i][j] for j in range(4)) for i in range(4))


def einstein_residual(
    einstein_tensor: Sequence[Sequence[float]],
    metric: Sequence[Sequence[float]],
    cosmological_coordinate: float,
    kappa_e: float,
    source: Sequence[Sequence[float]],
) -> tuple[tuple[float, ...], ...]:
    G = _mat4("einstein_tensor", einstein_tensor)
    g = _mat4("metric", metric)
    Lambda = _finite("cosmological_coordinate", cosmological_coordinate)
    kappa = _positive("kappa_e", kappa_e)
    T = _mat4("source", source)
    return _add(G, _scale(Lambda, g), _scale(-kappa, T))


def fixed_dynamic_residual_pair(
    *,
    einstein_tensor: Sequence[Sequence[float]],
    metric: Sequence[Sequence[float]],
    lambda_star: float,
    kappa_e: float,
    rest_source: Sequence[Sequence[float]],
    eta: float,
    u_hat: float,
    projector_stress: Sequence[Sequence[float]],
) -> tuple[tuple[tuple[float, ...], ...], tuple[tuple[float, ...], ...]]:
    fixed = assemble_fixed_reference_source(
        rest_source,
        metric,
        eta=eta,
        u_hat=u_hat,
        projector_stress=projector_stress,
    )
    dynamic = assemble_dynamic_lambda_source(
        rest_source,
        metric,
        eta=eta,
        u_hat=u_hat,
        projector_stress=projector_stress,
    )
    Lambda0 = lambda0_from_reference(lambda_star, kappa_e, u_hat)
    return (
        einstein_residual(einstein_tensor, metric, lambda_star, kappa_e, fixed),
        einstein_residual(einstein_tensor, metric, Lambda0, kappa_e, dynamic),
    )


def dynamic_bianchi_residual_from_fixed(
    kappa_e: float,
    fixed_source_divergence: Sequence[float],
    grad_u_hat: Sequence[float],
) -> tuple[float, ...]:
    """kappa div(T_dyn)-grad Lambda0 after T_dyn=T_fixed+Uhat*g and metric compatibility."""
    kappa = _positive("kappa_e", kappa_e)
    div_fixed = _vec4("fixed_source_divergence", fixed_source_divergence)
    grad_u = _vec4("grad_u_hat", grad_u_hat)
    div_dynamic = tuple(div_fixed[i] + grad_u[i] for i in range(4))
    grad_lambda0 = tuple(kappa * grad_u[i] for i in range(4))
    return tuple(kappa * div_dynamic[i] - grad_lambda0[i] for i in range(4))


def max_abs_matrix_difference(
    left: Sequence[Sequence[float]],
    right: Sequence[Sequence[float]],
) -> float:
    a = _mat4("left", left)
    b = _mat4("right", right)
    return max(abs(a[i][j] - b[i][j]) for i in range(4) for j in range(4))
