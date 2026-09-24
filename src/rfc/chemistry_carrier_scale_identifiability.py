from __future__ import annotations

import math
from dataclasses import dataclass


class CarrierScaleIdentifiabilityError(ValueError):
    pass


@dataclass(frozen=True)
class CarrierScaleState:
    B_action: float
    occupation: float
    volume: float
    omega: float
    phase_factor: float

    @property
    def occupation_density(self) -> float:
        return self.occupation / self.volume

    @property
    def carrier_energy(self) -> float:
        return self.B_action * self.omega * self.phase_factor

    @property
    def source_density(self) -> float:
        return self.occupation_density * self.carrier_energy


def _positive(name: str, value: float) -> float:
    value = float(value)
    if not math.isfinite(value) or value <= 0.0:
        raise CarrierScaleIdentifiabilityError(f"{name} must be finite and positive")
    return value


def carrier_scale_state(
    B_action: float,
    occupation: float,
    volume: float,
    omega: float,
    phase_factor: float,
) -> CarrierScaleState:
    B = _positive("B_action", B_action)
    N = _positive("occupation", occupation)
    V = _positive("volume", volume)
    w = float(omega)
    p = float(phase_factor)
    if not math.isfinite(w) or not math.isfinite(p):
        raise CarrierScaleIdentifiabilityError("omega and phase_factor must be finite")
    return CarrierScaleState(B, N, V, w, p)


def rescale_source_equivalent(
    state: CarrierScaleState,
    *,
    action_scale: float,
    occupation_scale: float,
) -> CarrierScaleState:
    a = _positive("action_scale", action_scale)
    b = _positive("occupation_scale", occupation_scale)
    return CarrierScaleState(
        B_action=a * state.B_action,
        occupation=b * state.occupation,
        volume=a * b * state.volume,
        omega=state.omega,
        phase_factor=state.phase_factor,
    )


def log_source_jacobian() -> tuple[float, float, float]:
    """d ln|rho| / d(ln B, ln N, ln V) at fixed omega and phase."""
    return (1.0, 1.0, -1.0)


def log_source_null_directions() -> tuple[tuple[float, float, float], ...]:
    return ((1.0, 0.0, 1.0), (0.0, 1.0, 1.0))


def dot(a, b) -> float:
    return sum(float(x) * float(y) for x, y in zip(a, b))


OBSERVABLE_SENSITIVITIES = {
    "rho": (1.0, 1.0, -1.0),
    "epsilon": (1.0, 0.0, 0.0),
    "n": (0.0, 1.0, -1.0),
    "N": (0.0, 1.0, 0.0),
    "V": (0.0, 0.0, 1.0),
}


def matrix_rank(rows, *, atol: float = 1e-12) -> int:
    matrix = [list(map(float, row)) for row in rows]
    if not matrix:
        return 0
    width = len(matrix[0])
    if any(len(row) != width for row in matrix):
        raise CarrierScaleIdentifiabilityError("all sensitivity rows must have equal width")
    rank = 0
    column = 0
    while rank < len(matrix) and column < width:
        pivot = max(range(rank, len(matrix)), key=lambda i: abs(matrix[i][column]))
        if abs(matrix[pivot][column]) <= atol:
            column += 1
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        scale = matrix[rank][column]
        matrix[rank] = [x / scale for x in matrix[rank]]
        for i in range(len(matrix)):
            if i == rank:
                continue
            factor = matrix[i][column]
            if abs(factor) > atol:
                matrix[i] = [
                    x - factor * y for x, y in zip(matrix[i], matrix[rank])
                ]
        rank += 1
        column += 1
    return rank


def observable_rank(observables) -> int:
    names = tuple(observables)
    try:
        rows = [OBSERVABLE_SENSITIVITIES[name] for name in names]
    except KeyError as exc:
        raise CarrierScaleIdentifiabilityError(
            f"unknown observable {exc.args[0]}"
        ) from exc
    return matrix_rank(rows)


def parameter_identifiable(observables, parameter: str) -> bool:
    axes = {
        "B": (1.0, 0.0, 0.0),
        "N": (0.0, 1.0, 0.0),
        "V": (0.0, 0.0, 1.0),
    }
    if parameter not in axes:
        raise CarrierScaleIdentifiabilityError(f"unknown parameter {parameter}")
    names = tuple(observables)
    rows = [OBSERVABLE_SENSITIVITIES[name] for name in names]
    return matrix_rank(rows + [axes[parameter]]) == matrix_rank(rows)
