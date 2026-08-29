from __future__ import annotations

import math
from dataclasses import dataclass
from collections.abc import Sequence


class CarrierNormalizationError(ValueError):
    pass


@dataclass(frozen=True)
class CarrierNormalizationState:
    carrier_quantum: float
    current_densities: tuple[float, ...]
    energy_per_charge: float
    total_charge: float
    energy_density_cells: tuple[float, ...]
    normalized_profile: tuple[float, ...]


def _finite(name: str, value: float) -> float:
    value = float(value)
    if not math.isfinite(value):
        raise CarrierNormalizationError(f"{name} must be finite")
    return value


def carrier_normalization_state(
    occupations: Sequence[float],
    volumes: Sequence[float],
    *,
    carrier_quantum: float,
    energy_per_occupied_carrier: float,
) -> CarrierNormalizationState:
    if len(occupations) < 1 or len(occupations) != len(volumes):
        raise CarrierNormalizationError("occupations and volumes must be nonempty and equal length")
    occ = tuple(_finite(f"occupations[{i}]", x) for i, x in enumerate(occupations))
    vol = tuple(_finite(f"volumes[{i}]", x) for i, x in enumerate(volumes))
    q0 = _finite("carrier_quantum", carrier_quantum)
    epsilon_occ = _finite("energy_per_occupied_carrier", energy_per_occupied_carrier)
    if any(x < 0.0 for x in occ):
        raise CarrierNormalizationError("occupations must be nonnegative")
    if any(x <= 0.0 for x in vol):
        raise CarrierNormalizationError("volumes must be positive")
    if q0 <= 0.0:
        raise CarrierNormalizationError("carrier_quantum must be positive")
    total_occ = math.fsum(occ)
    if total_occ <= 0.0:
        raise CarrierNormalizationError("total occupation must be positive")

    currents = tuple(q0 * n / v for n, v in zip(occ, vol, strict=True))
    epsilon_q = epsilon_occ / q0
    total_q = q0 * total_occ
    energy_density = tuple(epsilon_q * j for j in currents)
    profile = tuple(n / total_occ for n in occ)
    return CarrierNormalizationState(
        carrier_quantum=q0,
        current_densities=currents,
        energy_per_charge=epsilon_q,
        total_charge=total_q,
        energy_density_cells=energy_density,
        normalized_profile=profile,
    )


def rescale_carrier_normalization(
    state: CarrierNormalizationState,
    factor: float,
) -> CarrierNormalizationState:
    lam = _finite("factor", factor)
    if lam <= 0.0:
        raise CarrierNormalizationError("factor must be positive")
    return CarrierNormalizationState(
        carrier_quantum=lam * state.carrier_quantum,
        current_densities=tuple(lam * j for j in state.current_densities),
        energy_per_charge=state.energy_per_charge / lam,
        total_charge=lam * state.total_charge,
        energy_density_cells=tuple(state.energy_density_cells),
        normalized_profile=tuple(state.normalized_profile),
    )


def energy_density_invariance_defect(
    left: CarrierNormalizationState,
    right: CarrierNormalizationState,
) -> float:
    if len(left.energy_density_cells) != len(right.energy_density_cells):
        raise CarrierNormalizationError("states must have equal cell count")
    numerator = math.fsum(
        abs(a - b)
        for a, b in zip(left.energy_density_cells, right.energy_density_cells, strict=True)
    )
    denominator = math.fsum(
        abs(a) + abs(b)
        for a, b in zip(left.energy_density_cells, right.energy_density_cells, strict=True)
    )
    return 0.0 if denominator == 0.0 else 2.0 * numerator / denominator
