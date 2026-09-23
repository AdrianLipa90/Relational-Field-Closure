from __future__ import annotations

import math
from dataclasses import dataclass

from src.rfc.foundational_phase_source_formalism import (
    FoundationalPhaseSourceError,
    path_holonomy_difference,
)


@dataclass(frozen=True)
class LoopPhaseDisplacement:
    reference_loop_phase: float
    perturbed_loop_phase: float
    lifted_delta: float
    projective_delta: float


def _finite(name: str, value: float) -> float:
    value = float(value)
    if not math.isfinite(value):
        raise FoundationalPhaseSourceError(f"{name} must be finite")
    return value


def loop_phase_from_two_paths(
    line_integral_c1: float,
    line_integral_c2: float,
) -> float:
    """RFC F1 lifted loop phase for two paths with common endpoints."""
    return path_holonomy_difference(line_integral_c1, line_integral_c2)


def loop_phase_displacement(
    reference_c1: float,
    reference_c2: float,
    perturbed_c1: float,
    perturbed_c2: float,
) -> LoopPhaseDisplacement:
    """Gauge-invariant change of a declared lifted loop coordinate."""
    gamma0 = loop_phase_from_two_paths(reference_c1, reference_c2)
    gamma1 = loop_phase_from_two_paths(perturbed_c1, perturbed_c2)
    delta = gamma1 - gamma0
    projective = math.atan2(math.sin(delta), math.cos(delta))
    return LoopPhaseDisplacement(
        reference_loop_phase=gamma0,
        perturbed_loop_phase=gamma1,
        lifted_delta=delta,
        projective_delta=projective,
    )


def fixed_carrier_phase_energy_response(
    B_action_joule_second: float,
    omega_rad_s: float,
    lifted_phase_displacement: float,
) -> float:
    """RF-F5 energy change at fixed B and omega: delta epsilon = B*omega*delta Phi."""
    B = _finite("B_action_joule_second", B_action_joule_second)
    omega = _finite("omega_rad_s", omega_rad_s)
    delta = _finite("lifted_phase_displacement", lifted_phase_displacement)
    return B * omega * delta
