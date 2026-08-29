from __future__ import annotations

import math
from dataclasses import dataclass
from collections.abc import Sequence


class FourCurrentDustClosureError(ValueError):
    pass


Vector3 = tuple[float, float, float]
Vector4 = tuple[float, float, float, float]
Matrix3 = tuple[Vector3, Vector3, Vector3]
Matrix4 = tuple[
    tuple[float, float, float, float],
    tuple[float, float, float, float],
    tuple[float, float, float, float],
    tuple[float, float, float, float],
]


@dataclass(frozen=True)
class FourCurrentDustState:
    current_contravariant: Vector4
    proper_charge_density: float
    four_velocity_contravariant: Vector4
    beta: Vector3
    gamma: float
    energy_per_charge: float
    rest_energy_density: float
    T_cov: Matrix4
    rho_n: float
    j_i: Vector3
    S_ij: Matrix3
    S_trace: float


def _finite(name: str, value: float) -> float:
    value = float(value)
    if not math.isfinite(value):
        raise FourCurrentDustClosureError(f"{name} must be finite")
    return value


def _four(values: Sequence[float]) -> Vector4:
    if len(values) != 4:
        raise FourCurrentDustClosureError("current must contain exactly four components")
    return tuple(_finite(f"current[{i}]", x) for i, x in enumerate(values))  # type: ignore[return-value]


def minkowski_norm_squared(current_contravariant: Sequence[float]) -> float:
    j = _four(current_contravariant)
    return -j[0] * j[0] + math.fsum(x * x for x in j[1:])


def fourcurrent_dust_state(
    current_contravariant: Sequence[float],
    energy_per_charge: float,
) -> FourCurrentDustState:
    """Build a pressureless stress tensor from a future timelike current.

    Conventions are local orthonormal (-,+,+,+), with J^mu components sharing
    one current-density unit.  For future timelike J^mu define

        q = sqrt(-J_mu J^mu) > 0,
        u^mu = J^mu/q,
        rho_0 = epsilon_Q q,
        T_mn = epsilon_Q J_m J_n/q.

    The RF-E11 projections then follow without separately supplying velocity.
    """

    J = _four(current_contravariant)
    epsilon = _finite("energy_per_charge", energy_per_charge)
    if J[0] <= 0.0:
        raise FourCurrentDustClosureError("current must be future-directed with J^0 > 0")
    if epsilon < 0.0:
        raise FourCurrentDustClosureError("energy_per_charge must be nonnegative")

    proper2 = J[0] * J[0] - math.fsum(x * x for x in J[1:])
    if proper2 <= 0.0:
        raise FourCurrentDustClosureError("current must be strictly timelike")
    q = math.sqrt(proper2)
    u = tuple(x / q for x in J)
    beta = tuple(J[i] / J[0] for i in range(1, 4))
    gamma = J[0] / q
    rho0 = epsilon * q

    J_cov = (-J[0], J[1], J[2], J[3])
    T_cov = tuple(
        tuple(epsilon * J_cov[mu] * J_cov[nu] / q for nu in range(4))
        for mu in range(4)
    )

    rho_n = T_cov[0][0]
    j_i = tuple(-T_cov[0][i] for i in range(1, 4))
    S_ij = tuple(tuple(T_cov[i][j] for j in range(1, 4)) for i in range(1, 4))
    S_trace = math.fsum(S_ij[i][i] for i in range(3))

    return FourCurrentDustState(
        current_contravariant=J,
        proper_charge_density=q,
        four_velocity_contravariant=u,  # type: ignore[arg-type]
        beta=beta,  # type: ignore[arg-type]
        gamma=gamma,
        energy_per_charge=epsilon,
        rest_energy_density=rho0,
        T_cov=T_cov,  # type: ignore[arg-type]
        rho_n=rho_n,
        j_i=j_i,  # type: ignore[arg-type]
        S_ij=S_ij,  # type: ignore[arg-type]
        S_trace=S_trace,
    )


def current_normalization_rescale(
    current_contravariant: Sequence[float],
    energy_per_charge: float,
    factor: float,
) -> tuple[Vector4, float]:
    J = _four(current_contravariant)
    epsilon = _finite("energy_per_charge", energy_per_charge)
    lam = _finite("factor", factor)
    if lam <= 0.0:
        raise FourCurrentDustClosureError("factor must be positive")
    return tuple(lam * x for x in J), epsilon / lam  # type: ignore[return-value]


def tensor_frobenius_defect(left: Matrix4, right: Matrix4) -> float:
    numerator = math.fsum(
        abs(left[i][j] - right[i][j]) for i in range(4) for j in range(4)
    )
    denominator = math.fsum(
        abs(left[i][j]) + abs(right[i][j]) for i in range(4) for j in range(4)
    )
    return 0.0 if denominator == 0.0 else 2.0 * numerator / denominator


def dust_trace_residual(state: FourCurrentDustState) -> float:
    return -state.rho_n + state.S_trace + state.rest_energy_density


def dust_rank_one_residual(state: FourCurrentDustState) -> float:
    j2 = math.fsum(x * x for x in state.j_i)
    return j2 - state.rho_n * state.S_trace
