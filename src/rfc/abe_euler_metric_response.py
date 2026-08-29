from __future__ import annotations

import math
from collections.abc import Sequence


class ABEMetricResponseError(ValueError):
    pass


def _finite(name: str, value: float) -> float:
    value = float(value)
    if not math.isfinite(value):
        raise ABEMetricResponseError(f"{name} must be finite")
    return value


def _positive(name: str, value: float) -> float:
    value = _finite(name, value)
    if value <= 0.0:
        raise ABEMetricResponseError(f"{name} must be positive")
    return value


def _vec4(name: str, values: Sequence[float]) -> tuple[float, ...]:
    if len(values) != 4:
        raise ABEMetricResponseError(f"{name} must have length 4")
    return tuple(_finite(f"{name}[{i}]", value) for i, value in enumerate(values))


def _mat4(name: str, values: Sequence[Sequence[float]]) -> tuple[tuple[float, ...], ...]:
    if len(values) != 4 or any(len(row) != 4 for row in values):
        raise ABEMetricResponseError(f"{name} must be 4x4")
    return tuple(
        tuple(_finite(f"{name}[{i}][{j}]", value) for j, value in enumerate(row))
        for i, row in enumerate(values)
    )


def _rank3_metric_response(
    name: str,
    values: Sequence[Sequence[Sequence[float]]],
) -> tuple[tuple[tuple[float, ...], ...], ...]:
    """dA_beta/dg^{mn}, indexed [beta][m][n]."""
    if len(values) != 4:
        raise ABEMetricResponseError(f"{name} must have 4 beta components")
    out: list[tuple[tuple[float, ...], ...]] = []
    for beta, matrix in enumerate(values):
        parsed = _mat4(f"{name}[{beta}]", matrix)
        for m in range(4):
            for n in range(4):
                if parsed[m][n] != parsed[n][m]:
                    raise ABEMetricResponseError(
                        f"{name}[{beta}] must be symmetric in metric indices"
                    )
        out.append(parsed)
    return tuple(out)


def zero_connection_metric_response() -> tuple[tuple[tuple[float, ...], ...], ...]:
    return tuple(tuple(tuple(0.0 for _ in range(4)) for _ in range(4)) for _ in range(4))


def sum_connection_metric_responses(
    ab_response: Sequence[Sequence[Sequence[float]]],
    berry_response: Sequence[Sequence[Sequence[float]]],
    euler_response: Sequence[Sequence[Sequence[float]]],
) -> tuple[tuple[tuple[float, ...], ...], ...]:
    """Linearity of A^ABE=A_AB+A_B+A_E under off-shell metric variation."""
    ab = _rank3_metric_response("ab_response", ab_response)
    berry = _rank3_metric_response("berry_response", berry_response)
    euler = _rank3_metric_response("euler_response", euler_response)
    return tuple(
        tuple(
            tuple(ab[b][m][n] + berry[b][m][n] + euler[b][m][n] for n in range(4))
            for m in range(4)
        )
        for b in range(4)
    )


def contracted_phase_connection_response(
    inverse_metric: Sequence[Sequence[float]],
    phase_covector: Sequence[float],
    connection_metric_response: Sequence[Sequence[Sequence[float]]],
) -> tuple[tuple[float, ...], ...]:
    """R_mn=g^{ab} q_a partial A_b/partial g^{mn}."""
    g_inv = _mat4("inverse_metric", inverse_metric)
    q = _vec4("phase_covector", phase_covector)
    response = _rank3_metric_response("connection_metric_response", connection_metric_response)
    return tuple(
        tuple(
            sum(g_inv[a][b] * q[a] * response[b][m][n] for a in range(4) for b in range(4))
            for n in range(4)
        )
        for m in range(4)
    )


def abe_contracted_response(
    inverse_metric: Sequence[Sequence[float]],
    phase_covector: Sequence[float],
    ab_response: Sequence[Sequence[Sequence[float]]],
    berry_response: Sequence[Sequence[Sequence[float]]],
    euler_response: Sequence[Sequence[Sequence[float]]],
) -> tuple[tuple[float, ...], ...]:
    total = sum_connection_metric_responses(ab_response, berry_response, euler_response)
    return contracted_phase_connection_response(inverse_metric, phase_covector, total)


def projector_metric_derivative(
    phase_covector: Sequence[float],
    phase_scale: float,
    contracted_response: Sequence[Sequence[float]],
    *,
    projector_value: float = 1.0,
    scale_log_metric_response: Sequence[Sequence[float]] | None = None,
) -> tuple[tuple[float, ...], ...]:
    """dC/dg^{mn}=-(q_m q_n+2R_mn)/mu^2-2 C S_mn."""
    q = _vec4("phase_covector", phase_covector)
    mu = _positive("phase_scale", phase_scale)
    R = _mat4("contracted_response", contracted_response)
    C = _finite("projector_value", projector_value)
    S = (
        tuple(tuple(0.0 for _ in range(4)) for _ in range(4))
        if scale_log_metric_response is None
        else _mat4("scale_log_metric_response", scale_log_metric_response)
    )
    return tuple(
        tuple(-(q[m] * q[n] + 2.0 * R[m][n]) / (mu * mu) - 2.0 * C * S[m][n] for n in range(4))
        for m in range(4)
    )


def phase_stress_metric_response_correction(
    amplitude_squared: float,
    contracted_response: Sequence[Sequence[float]],
) -> tuple[tuple[float, ...], ...]:
    """Correction to RF-E4 phase stress: Delta T_mn=4 A^2 R_mn."""
    A2 = _finite("amplitude_squared", amplitude_squared)
    if A2 < 0.0:
        raise ABEMetricResponseError("amplitude_squared must be nonnegative")
    R = _mat4("contracted_response", contracted_response)
    return tuple(tuple(4.0 * A2 * R[m][n] for n in range(4)) for m in range(4))


def eta_one_projector_stress(
    u_hat_value: float,
    f_prime_at_one: float,
    phase_covector: Sequence[float],
    phase_scale: float,
    contracted_response: Sequence[Sequence[float]],
    *,
    scale_log_metric_response: Sequence[Sequence[float]] | None = None,
) -> tuple[tuple[float, ...], ...]:
    """RF-F18/F19 eta=1 stress including ABE response and independent-scale response."""
    U = _finite("u_hat_value", u_hat_value)
    fp = _finite("f_prime_at_one", f_prime_at_one)
    q = _vec4("phase_covector", phase_covector)
    mu = _positive("phase_scale", phase_scale)
    R = _mat4("contracted_response", contracted_response)
    S = (
        tuple(tuple(0.0 for _ in range(4)) for _ in range(4))
        if scale_log_metric_response is None
        else _mat4("scale_log_metric_response", scale_log_metric_response)
    )
    return tuple(
        tuple(
            2.0 * U * fp * q[m] * q[n] / (mu * mu)
            + 4.0 * U * fp * R[m][n] / (mu * mu)
            + 4.0 * U * fp * S[m][n]
            for n in range(4)
        )
        for m in range(4)
    )


def max_abs_matrix(values: Sequence[Sequence[float]]) -> float:
    matrix = _mat4("values", values)
    return max(abs(value) for row in matrix for value in row)


def frozen_connection_branch(contracted_response: Sequence[Sequence[float]], *, atol: float = 0.0) -> bool:
    tol = _finite("atol", atol)
    if tol < 0.0:
        raise ABEMetricResponseError("atol must be nonnegative")
    return max_abs_matrix(contracted_response) <= tol
