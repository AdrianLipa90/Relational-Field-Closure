from __future__ import annotations

import math
from collections.abc import Sequence


class PhaseClockProjectorError(ValueError):
    pass


def _finite(name: str, value: float) -> float:
    value = float(value)
    if not math.isfinite(value):
        raise PhaseClockProjectorError(f"{name} must be finite")
    return value


def _positive(name: str, value: float) -> float:
    value = _finite(name, value)
    if value <= 0.0:
        raise PhaseClockProjectorError(f"{name} must be positive")
    return value


def _vec4(name: str, values: Sequence[float]) -> tuple[float, float, float, float]:
    if len(values) != 4:
        raise PhaseClockProjectorError(f"{name} must have length 4")
    return tuple(_finite(f"{name}[{i}]", value) for i, value in enumerate(values))  # type: ignore[return-value]


def _mat4(name: str, values: Sequence[Sequence[float]]) -> tuple[tuple[float, ...], ...]:
    if len(values) != 4 or any(len(row) != 4 for row in values):
        raise PhaseClockProjectorError(f"{name} must be 4x4")
    return tuple(
        tuple(_finite(f"{name}[{i}][{j}]", value) for j, value in enumerate(row))
        for i, row in enumerate(values)
    )


def gauge_covariant_phase_covector(
    phase_gradient: Sequence[float],
    abe_connection: Sequence[float],
) -> tuple[float, float, float, float]:
    """IDT 01AC one-form q_mu = d_mu vartheta + A_mu^ABE."""
    dtheta = _vec4("phase_gradient", phase_gradient)
    connection = _vec4("abe_connection", abe_connection)
    return tuple(dtheta[i] + connection[i] for i in range(4))  # type: ignore[return-value]


def gauge_transform_pair(
    phase_gradient: Sequence[float],
    abe_connection: Sequence[float],
    lambda_gradient: Sequence[float],
) -> tuple[tuple[float, float, float, float], tuple[float, float, float, float]]:
    """Apply IDT 01AC: dtheta -> dtheta+dlambda, A^ABE -> A^ABE-dlambda."""
    dtheta = _vec4("phase_gradient", phase_gradient)
    connection = _vec4("abe_connection", abe_connection)
    dlam = _vec4("lambda_gradient", lambda_gradient)
    return (
        tuple(dtheta[i] + dlam[i] for i in range(4)),  # type: ignore[return-value]
        tuple(connection[i] - dlam[i] for i in range(4)),  # type: ignore[return-value]
    )


def inverse_metric_contraction(
    inverse_metric: Sequence[Sequence[float]],
    covector_a: Sequence[float],
    covector_b: Sequence[float],
) -> float:
    ginv = _mat4("inverse_metric", inverse_metric)
    a = _vec4("covector_a", covector_a)
    b = _vec4("covector_b", covector_b)
    return sum(ginv[i][j] * a[i] * b[j] for i in range(4) for j in range(4))


def phase_clock_projector(
    inverse_metric: Sequence[Sequence[float]],
    phase_covector: Sequence[float],
    mu_phase: float,
) -> float:
    """C_vartheta=-g^{mn} q_m q_n / mu_vartheta^2.

    mu_phase is an independent calibration input with the same norm units as q_mu.
    """
    mu = _positive("mu_phase", mu_phase)
    q2 = inverse_metric_contraction(inverse_metric, phase_covector, phase_covector)
    return -q2 / (mu * mu)


def unit_surface_defect(
    inverse_metric: Sequence[Sequence[float]],
    phase_covector: Sequence[float],
    mu_phase: float,
) -> float:
    return abs(phase_clock_projector(inverse_metric, phase_covector, mu_phase) - 1.0)


def normalized_phase_covector(
    phase_covector: Sequence[float],
    mu_phase: float,
) -> tuple[float, float, float, float]:
    q = _vec4("phase_covector", phase_covector)
    mu = _positive("mu_phase", mu_phase)
    return tuple(value / mu for value in q)  # type: ignore[return-value]


def projector_metric_derivative(
    phase_covector: Sequence[float],
    mu_phase: float,
    *,
    connection_metric_response_contraction: Sequence[Sequence[float]] | None = None,
) -> tuple[tuple[float, ...], ...]:
    """Metric derivative of C_vartheta.

    Let R_mn := g^{ab} q_a * partial(q_b)/partial(g^{mn}). Then

      partial C / partial g^{mn}
        = -q_m q_n/mu^2 - 2 R_mn/mu^2.

    The frozen-one-form branch is R_mn=0. This keeps possible metric dependence of
    the Euler/ABE connection explicit instead of silently dropping it.
    """
    q = _vec4("phase_covector", phase_covector)
    mu = _positive("mu_phase", mu_phase)
    if connection_metric_response_contraction is None:
        response = tuple(tuple(0.0 for _ in range(4)) for _ in range(4))
    else:
        response = _mat4(
            "connection_metric_response_contraction",
            connection_metric_response_contraction,
        )
    mu2 = mu * mu
    return tuple(
        tuple(-(q[i] * q[j] + 2.0 * response[i][j]) / mu2 for j in range(4))
        for i in range(4)
    )


def eta_one_projector_stress(
    u_hat_value: float,
    f_prime_at_one: float,
    phase_covector: Sequence[float],
    mu_phase: float,
    *,
    connection_metric_response_contraction: Sequence[Sequence[float]] | None = None,
) -> tuple[tuple[float, ...], ...]:
    """RF-F17 eta=1 stress -2 Uhat f'(1) dC/dg for the phase-clock projector."""
    U = _finite("u_hat_value", u_hat_value)
    fp = _finite("f_prime_at_one", f_prime_at_one)
    derivative = projector_metric_derivative(
        phase_covector,
        mu_phase,
        connection_metric_response_contraction=connection_metric_response_contraction,
    )
    return tuple(
        tuple(-2.0 * U * fp * derivative[i][j] for j in range(4))
        for i in range(4)
    )


def frozen_one_form_dust_stress(
    u_hat_value: float,
    phase_covector: Sequence[float],
    mu_phase: float,
) -> tuple[tuple[float, ...], ...]:
    """f'(1)=1/2, R_mn=0 gives T_mn=Uhat u_m u_n on C=1."""
    return eta_one_projector_stress(
        u_hat_value,
        0.5,
        phase_covector,
        mu_phase,
        connection_metric_response_contraction=None,
    )


def connection_response_stress_correction(
    u_hat_value: float,
    f_prime_at_one: float,
    mu_phase: float,
    connection_metric_response_contraction: Sequence[Sequence[float]],
) -> tuple[tuple[float, ...], ...]:
    """Additional eta=1 tensor 4 Uhat f'(1) R_mn/mu^2."""
    U = _finite("u_hat_value", u_hat_value)
    fp = _finite("f_prime_at_one", f_prime_at_one)
    mu = _positive("mu_phase", mu_phase)
    response = _mat4(
        "connection_metric_response_contraction",
        connection_metric_response_contraction,
    )
    factor = 4.0 * U * fp / (mu * mu)
    return tuple(tuple(factor * response[i][j] for j in range(4)) for i in range(4))


def material_alignment_gamma(
    normalized_phase_covector_value: Sequence[float],
    material_four_velocity_contravariant: Sequence[float],
) -> float:
    """For future unit timelike sectors, gamma_rel=-u_phase_mu * nu_J^mu >= 1."""
    u_cov = _vec4("normalized_phase_covector", normalized_phase_covector_value)
    nu = _vec4("material_four_velocity_contravariant", material_four_velocity_contravariant)
    return -sum(u_cov[i] * nu[i] for i in range(4))


def material_alignment_defect(
    normalized_phase_covector_value: Sequence[float],
    material_four_velocity_contravariant: Sequence[float],
) -> float:
    return abs(material_alignment_gamma(normalized_phase_covector_value, material_four_velocity_contravariant) - 1.0)


def response_is_zero(
    connection_metric_response_contraction: Sequence[Sequence[float]],
    *,
    atol: float = 0.0,
) -> bool:
    response = _mat4(
        "connection_metric_response_contraction",
        connection_metric_response_contraction,
    )
    tol = _finite("atol", atol)
    if tol < 0.0:
        raise PhaseClockProjectorError("atol must be nonnegative")
    return all(abs(value) <= tol for row in response for value in row)
