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
