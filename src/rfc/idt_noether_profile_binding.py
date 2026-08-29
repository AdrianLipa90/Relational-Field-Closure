from __future__ import annotations

import math
from dataclasses import dataclass
from collections.abc import Sequence

from src.rfc.noether_profile_source_reconstruction import normalized_noether_profile
from src.rfc.relational_generator_source_density import KAPPA_INFO


class IDTNoetherProfileBindingError(ValueError):
    pass


@dataclass(frozen=True)
class IDTNoetherProfileBinding:
    idt_profile: tuple[float, ...]
    noether_profile: tuple[float, ...]
    hellinger_squared: float
    l1_distance: float
    max_abs_distance: float
    zero_defect: bool


@dataclass(frozen=True)
class IDTSourceReconstruction:
    total_occupation: float
    occupations: tuple[float, ...]
    occupation_densities: tuple[float, ...]
    carrier_energies: tuple[float, ...]
    source_energy_densities: tuple[float, ...]
    integrated_source_energy: float


def _finite(name: str, value: float) -> float:
    value = float(value)
    if not math.isfinite(value):
        raise IDTNoetherProfileBindingError(f"{name} must be finite")
    return value


def _probability_profile(name: str, values: Sequence[float], *, tolerance: float = 1e-12) -> tuple[float, ...]:
    if len(values) < 1:
        raise IDTNoetherProfileBindingError(f"{name} must be nonempty")
    out = tuple(_finite(f"{name}[{i}]", x) for i, x in enumerate(values))
    if any(x < 0.0 for x in out):
        raise IDTNoetherProfileBindingError(f"{name} entries must be nonnegative")
    total = math.fsum(out)
    if total <= 0.0:
        raise IDTNoetherProfileBindingError(f"{name} must have positive total")
    if not math.isclose(total, 1.0, rel_tol=0.0, abs_tol=tolerance):
        raise IDTNoetherProfileBindingError(f"{name} must be normalized")
    return tuple(x / total for x in out)


def compare_idt_noether_profiles(
    idt_profile: Sequence[float],
    noether_current_densities: Sequence[float],
    cell_volumes: Sequence[float],
    *,
    tolerance: float = 1e-12,
) -> IDTNoetherProfileBinding:
    tol = _finite("tolerance", tolerance)
    if tol < 0.0:
        raise IDTNoetherProfileBindingError("tolerance must be nonnegative")
    p = _probability_profile("idt_profile", idt_profile, tolerance=tol)
    try:
        q = normalized_noether_profile(noether_current_densities, cell_volumes)
    except ValueError as exc:
        raise IDTNoetherProfileBindingError(str(exc)) from exc
    if len(p) != len(q):
        raise IDTNoetherProfileBindingError("IDT and Noether profiles must have equal length")

    overlap = math.fsum(math.sqrt(a * b) for a, b in zip(p, q))
    h2 = max(0.0, 1.0 - overlap)
    l1 = math.fsum(abs(a - b) for a, b in zip(p, q))
    max_abs = max(abs(a - b) for a, b in zip(p, q))
    return IDTNoetherProfileBinding(
        idt_profile=p,
        noether_profile=q,
        hellinger_squared=h2,
        l1_distance=l1,
        max_abs_distance=max_abs,
        zero_defect=max_abs <= tol,
    )


def reconstruct_source_from_idt_profile(
    idt_profile: Sequence[float],
    cell_volumes: Sequence[float],
    total_occupation: float,
    B_action_joule_second: Sequence[float],
    omega_rad_s: Sequence[float],
    phase: Sequence[float],
    *,
    kappa: float = KAPPA_INFO,
    tolerance: float = 1e-12,
) -> IDTSourceReconstruction:
    p = _probability_profile("idt_profile", idt_profile, tolerance=tolerance)
    count = len(p)
    if len(cell_volumes) != count or len(B_action_joule_second) != count or len(omega_rad_s) != count or len(phase) != count:
        raise IDTNoetherProfileBindingError("all cell arrays must have equal length")

    volumes = tuple(_finite(f"cell_volumes[{i}]", x) for i, x in enumerate(cell_volumes))
    if any(v <= 0.0 for v in volumes):
        raise IDTNoetherProfileBindingError("cell volumes must be positive")
    B = tuple(_finite(f"B_action_joule_second[{i}]", x) for i, x in enumerate(B_action_joule_second))
    omega = tuple(_finite(f"omega_rad_s[{i}]", x) for i, x in enumerate(omega_rad_s))
    phi = tuple(_finite(f"phase[{i}]", x) for i, x in enumerate(phase))
    kap = _finite("kappa", kappa)
    N_total = _finite("total_occupation", total_occupation)
    if N_total < 0.0:
        raise IDTNoetherProfileBindingError("total_occupation must be nonnegative")

    occupations = tuple(N_total * x for x in p)
    densities = tuple(occupations[i] / volumes[i] for i in range(count))
    energies = tuple(B[i] * omega[i] * (phi[i] + kap) for i in range(count))
    sources = tuple(densities[i] * energies[i] for i in range(count))
    integrated = math.fsum(sources[i] * volumes[i] for i in range(count))
    return IDTSourceReconstruction(
        total_occupation=N_total,
        occupations=occupations,
        occupation_densities=densities,
        carrier_energies=energies,
        source_energy_densities=sources,
        integrated_source_energy=integrated,
    )


def source_profile_mismatch_bound(
    idt_profile: Sequence[float],
    noether_current_densities: Sequence[float],
    cell_volumes: Sequence[float],
    total_occupation: float,
    carrier_energy_scale: float,
    *,
    tolerance: float = 1e-12,
) -> float:
    """L1 upper bound on integrated source-energy mismatch for uniform |epsilon| bound.

    If |epsilon_a| <= Emax, then

        |sum_a N_tot epsilon_a (p_a-q_a)| <= N_tot Emax ||p-q||_1.
    """
    binding = compare_idt_noether_profiles(
        idt_profile,
        noether_current_densities,
        cell_volumes,
        tolerance=tolerance,
    )
    N_total = _finite("total_occupation", total_occupation)
    Emax = _finite("carrier_energy_scale", carrier_energy_scale)
    if N_total < 0.0:
        raise IDTNoetherProfileBindingError("total_occupation must be nonnegative")
    if Emax < 0.0:
        raise IDTNoetherProfileBindingError("carrier_energy_scale must be nonnegative")
    return N_total * Emax * binding.l1_distance
