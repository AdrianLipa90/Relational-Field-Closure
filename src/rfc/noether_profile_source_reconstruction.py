from __future__ import annotations

import math
from dataclasses import dataclass
from collections.abc import Sequence

from src.rfc.relational_generator_source_density import KAPPA_INFO


class NoetherProfileSourceError(ValueError):
    pass


@dataclass(frozen=True)
class NoetherProfileSourceResult:
    total_noether_charge: float
    total_occupation: float
    profile: tuple[float, ...]
    occupations: tuple[float, ...]
    occupation_densities: tuple[float, ...]
    carrier_energies: tuple[float, ...]
    source_energy_densities: tuple[float, ...]
    integrated_source_energy: float


def _finite(name: str, value: float) -> float:
    value = float(value)
    if not math.isfinite(value):
        raise NoetherProfileSourceError(f"{name} must be finite")
    return value


def _vector(name: str, values: Sequence[float], *, nonnegative: bool = False, positive: bool = False) -> tuple[float, ...]:
    if len(values) < 1:
        raise NoetherProfileSourceError(f"{name} must be nonempty")
    out = tuple(_finite(f"{name}[{i}]", x) for i, x in enumerate(values))
    if positive and any(x <= 0.0 for x in out):
        raise NoetherProfileSourceError(f"{name} entries must be positive")
    if nonnegative and any(x < 0.0 for x in out):
        raise NoetherProfileSourceError(f"{name} entries must be nonnegative")
    return out


def normalized_noether_profile(
    noether_current_densities: Sequence[float],
    cell_volumes: Sequence[float],
) -> tuple[float, ...]:
    """Return p_a = V_a j_a / Q for a positive finite-cell Noether current."""

    j = _vector("noether_current_densities", noether_current_densities, nonnegative=True)
    volumes = _vector("cell_volumes", cell_volumes, positive=True)
    if len(j) != len(volumes):
        raise NoetherProfileSourceError("current and volume arrays must have equal length")
    charges = tuple(volumes[i] * j[i] for i in range(len(j)))
    total = math.fsum(charges)
    if total <= 0.0:
        raise NoetherProfileSourceError("total Noether charge must be positive")
    return tuple(q / total for q in charges)


def reconstruct_occupation_from_noether_profile(
    noether_current_densities: Sequence[float],
    cell_volumes: Sequence[float],
    total_occupation: float,
) -> tuple[tuple[float, ...], tuple[float, ...], float]:
    """Reconstruct local occupation without choosing an absolute carrier unit q0.

    RF-N1B2K provides the normalized conserved-current profile and RF-S16 gives
    p_Q=p_N.  Therefore, once total occupation N_tot is independently supplied,

        N_a = N_tot p_a,
        n_a = N_a / V_a = N_tot j_a / Q_theta.
    """

    j = _vector("noether_current_densities", noether_current_densities, nonnegative=True)
    volumes = _vector("cell_volumes", cell_volumes, positive=True)
    if len(j) != len(volumes):
        raise NoetherProfileSourceError("current and volume arrays must have equal length")
    N_total = _finite("total_occupation", total_occupation)
    if N_total < 0.0:
        raise NoetherProfileSourceError("total_occupation must be nonnegative")

    Q = math.fsum(volumes[i] * j[i] for i in range(len(j)))
    if Q <= 0.0:
        raise NoetherProfileSourceError("total Noether charge must be positive")
    profile = tuple(volumes[i] * j[i] / Q for i in range(len(j)))
    occupations = tuple(N_total * p for p in profile)
    densities = tuple(occupations[i] / volumes[i] for i in range(len(j)))
    return occupations, densities, Q


def reconstruct_generator_source_from_noether_profile(
    noether_current_densities: Sequence[float],
    cell_volumes: Sequence[float],
    total_occupation: float,
    B_action_joule_second: Sequence[float],
    omega_rad_s: Sequence[float],
    phase: Sequence[float],
    *,
    kappa: float = KAPPA_INFO,
) -> NoetherProfileSourceResult:
    """Map a zero-defect Noether current profile into RF-S13 source density.

    Only the current *profile* is used.  A global positive rescaling of every
    Noether current leaves the reconstructed occupation and source unchanged.
    """

    j = _vector("noether_current_densities", noether_current_densities, nonnegative=True)
    volumes = _vector("cell_volumes", cell_volumes, positive=True)
    B = _vector("B_action_joule_second", B_action_joule_second)
    omega = _vector("omega_rad_s", omega_rad_s)
    phi = _vector("phase", phase)
    count = len(j)
    if any(len(values) != count for values in (volumes, B, omega, phi)):
        raise NoetherProfileSourceError("all cell arrays must have equal length")
    kap = _finite("kappa", kappa)

    occupations, densities, Q = reconstruct_occupation_from_noether_profile(j, volumes, total_occupation)
    profile = tuple(occupations[i] / total_occupation for i in range(count)) if total_occupation > 0.0 else tuple(0.0 for _ in range(count))
    carrier_energies = tuple(B[i] * omega[i] * (phi[i] + kap) for i in range(count))
    source_densities = tuple(densities[i] * carrier_energies[i] for i in range(count))
    integrated = math.fsum(source_densities[i] * volumes[i] for i in range(count))

    return NoetherProfileSourceResult(
        total_noether_charge=Q,
        total_occupation=float(total_occupation),
        profile=profile,
        occupations=occupations,
        occupation_densities=densities,
        carrier_energies=carrier_energies,
        source_energy_densities=source_densities,
        integrated_source_energy=integrated,
    )


def current_rescaling_source_defect(
    noether_current_densities: Sequence[float],
    cell_volumes: Sequence[float],
    total_occupation: float,
    B_action_joule_second: Sequence[float],
    omega_rad_s: Sequence[float],
    phase: Sequence[float],
    scale: float,
    *,
    kappa: float = KAPPA_INFO,
) -> float:
    scale = _finite("scale", scale)
    if scale <= 0.0:
        raise NoetherProfileSourceError("scale must be positive")
    base = reconstruct_generator_source_from_noether_profile(
        noether_current_densities,
        cell_volumes,
        total_occupation,
        B_action_joule_second,
        omega_rad_s,
        phase,
        kappa=kappa,
    )
    scaled = reconstruct_generator_source_from_noether_profile(
        tuple(scale * float(x) for x in noether_current_densities),
        cell_volumes,
        total_occupation,
        B_action_joule_second,
        omega_rad_s,
        phase,
        kappa=kappa,
    )
    numerator = math.sqrt(math.fsum((a - b) ** 2 for a, b in zip(base.source_energy_densities, scaled.source_energy_densities)))
    denominator = math.sqrt(math.fsum(a * a for a in base.source_energy_densities))
    return 0.0 if denominator == 0.0 else numerator / denominator
