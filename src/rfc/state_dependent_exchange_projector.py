from __future__ import annotations

import math
from collections.abc import Sequence


class ExchangeProjectorError(ValueError):
    pass


def _finite(name: str, value: float) -> float:
    value = float(value)
    if not math.isfinite(value):
        raise ExchangeProjectorError(f"{name} must be finite")
    return value


def _eta(value: float) -> float:
    value = _finite("eta", value)
    if value < 0.0 or value > 1.0:
        raise ExchangeProjectorError("eta must lie in [0,1]")
    return value


def _vector4(name: str, values: Sequence[float]) -> tuple[float, float, float, float]:
    if len(values) != 4:
        raise ExchangeProjectorError(f"{name} must have length 4")
    return tuple(_finite(f"{name}[{i}]", v) for i, v in enumerate(values))  # type: ignore[return-value]


def _matrix4(name: str, values: Sequence[Sequence[float]]) -> tuple[tuple[float, ...], ...]:
    if len(values) != 4 or any(len(row) != 4 for row in values):
        raise ExchangeProjectorError(f"{name} must be 4x4")
    return tuple(tuple(_finite(f"{name}[{i}][{j}]", v) for j, v in enumerate(row)) for i, row in enumerate(values))


def exchange_derivative_on_surface(eta: float, u_prime: float, f_at_one: float = 1.0) -> float:
    """d L_int/dphi = eta U' f(C); evaluate on C=1."""
    e = _eta(eta)
    up = _finite("u_prime", u_prime)
    f1 = _finite("f_at_one", f_at_one)
    return e * up * f1


def scalar_potential_force_coefficient_on_surface(eta: float, f_at_one: float = 1.0) -> float:
    """Total L_U=-U+eta U f(C) gives -(1-eta f(1)) U in the scalar EOM."""
    e = _eta(eta)
    f1 = _finite("f_at_one", f_at_one)
    return 1.0 - e * f1


def net_potential_stress_on_surface(
    u_value: float,
    eta: float,
    f_at_one: float,
    f_prime_at_one: float,
    metric_covariant: Sequence[Sequence[float]],
    dc_dg_contravariant: Sequence[Sequence[float]],
) -> tuple[tuple[float, ...], ...]:
    """Stress of -U + eta U f(C) on the C=1 projector surface.

    T_mn = -(1-eta f(1)) U g_mn - 2 eta U f'(1) dC/dg^{mn}.
    """
    U = _finite("u_value", u_value)
    e = _eta(eta)
    f1 = _finite("f_at_one", f_at_one)
    fp = _finite("f_prime_at_one", f_prime_at_one)
    g = _matrix4("metric_covariant", metric_covariant)
    dc = _matrix4("dc_dg_contravariant", dc_dg_contravariant)
    return tuple(
        tuple(-(1.0 - e * f1) * U * g[i][j] - 2.0 * e * U * fp * dc[i][j] for j in range(4))
        for i in range(4)
    )


def clock_projector_metric_derivative(
    unit_clock_covector: Sequence[float],
) -> tuple[tuple[float, ...], ...]:
    """For C_T=-g^{mn} t_m t_n/mu_T^2 with t_m/mu_T=u_m on C_T=1.

    dC_T/dg^{mn} = -u_m u_n.
    """
    u = _vector4("unit_clock_covector", unit_clock_covector)
    return tuple(tuple(-u[i] * u[j] for j in range(4)) for i in range(4))


def eta_one_clock_stress(
    u_value: float,
    f_prime_at_one: float,
    unit_clock_covector: Sequence[float],
) -> tuple[tuple[float, ...], ...]:
    """At eta=1, f(1)=1: T_U = 2 f'(1) U u_m u_n for the clock projector."""
    U = _finite("u_value", u_value)
    fp = _finite("f_prime_at_one", f_prime_at_one)
    u = _vector4("unit_clock_covector", unit_clock_covector)
    return tuple(tuple(2.0 * fp * U * u[i] * u[j] for j in range(4)) for i in range(4))


def dust_normalization_slope(target_density_over_u: float = 1.0) -> float:
    """For T_mn=2 f'(1) U u_m u_n, return f'(1) for target rho/U."""
    ratio = _finite("target_density_over_u", target_density_over_u)
    return 0.5 * ratio


def metric_derivative_is_nontrivial(
    dc_dg_contravariant: Sequence[Sequence[float]],
    *,
    atol: float = 0.0,
) -> bool:
    dc = _matrix4("dc_dg_contravariant", dc_dg_contravariant)
    tol = _finite("atol", atol)
    if tol < 0.0:
        raise ExchangeProjectorError("atol must be nonnegative")
    return any(abs(v) > tol for row in dc for v in row)
