from __future__ import annotations

import math
from dataclasses import dataclass
from collections.abc import Sequence

from src.rfc.noether_profile_source_reconstruction import normalized_noether_profile
from src.rfc.relational_generator_source_density import KAPPA_INFO


class NoetherHamiltonianSourceClosureError(ValueError):
    pass


@dataclass(frozen=True)
class NoetherHamiltonianSourceClosure:
    total_hamiltonian_energy: float
    total_noether_charge: float
    noether_profile: tuple[float, ...]
    carrier_energies: tuple[float, ...]
    mean_carrier_energy: float
    inferred_total_occupation: float
    occupations: tuple[float, ...]
    source_energy_densities: tuple[float, ...]
    integrated_source_energy: float


def _finite(name: str, value: float) -> float:
    value = float(value)
    if not math.isfinite(value):
        raise NoetherHamiltonianSourceClosureError(f"{name} must be finite")
    return value


def _vector(name: str, values: Sequence[float]) -> tuple[float, ...]:
    if len(values) < 1:
        raise NoetherHamiltonianSourceClosureError(f"{name} must be nonempty")
    return tuple(_finite(f"{name}[{i}]", x) for i, x in enumerate(values))


def close_source_from_noether_hamiltonian(
    total_hamiltonian_energy: float,
    noether_current_densities: Sequence[float],
    cell_volumes: Sequence[float],
    B_action_joule_second: Sequence[float],
    omega_rad_s: Sequence[float],
    phase: Sequence[float],
    *,
    kappa: float = KAPPA_INFO,
) -> NoetherHamiltonianSourceClosure:
    """Close total occupation by matching the generator to an extensive Hamiltonian.

    RF-N1B2K supplies the finite Noether charge/current profile and downstream
    epsilon=H/Q. RF-S20/RF-S21 supply the occupation-profile source form. For
    local per-occupation energies epsilon_a=B_a*omega_a*(phi_a+kappa), define

        epsilon_bar = sum_a p_a epsilon_a.

    On the positive-source branch epsilon_bar>0 and H>=0, exact extensive
    matching E_G=H fixes

        N_tot = H / epsilon_bar.

    The local source is then

        rho_a = (N_tot p_a / V_a) epsilon_a,

    whose cell integral sums exactly to H.
    """

    H = _finite("total_hamiltonian_energy", total_hamiltonian_energy)
    if H < 0.0:
        raise NoetherHamiltonianSourceClosureError("total_hamiltonian_energy must be nonnegative")

    j = _vector("noether_current_densities", noether_current_densities)
    volumes = _vector("cell_volumes", cell_volumes)
    B = _vector("B_action_joule_second", B_action_joule_second)
    omega = _vector("omega_rad_s", omega_rad_s)
    phi = _vector("phase", phase)
    n = len(j)
    if any(len(v) != n for v in (volumes, B, omega, phi)):
        raise NoetherHamiltonianSourceClosureError("all cell arrays must have equal length")
    if any(x < 0.0 for x in j):
        raise NoetherHamiltonianSourceClosureError("Noether current densities must be nonnegative")
    if any(v <= 0.0 for v in volumes):
        raise NoetherHamiltonianSourceClosureError("cell volumes must be positive")

    try:
        profile = normalized_noether_profile(j, volumes)
    except ValueError as exc:
        raise NoetherHamiltonianSourceClosureError(str(exc)) from exc

    Q = math.fsum(j[i] * volumes[i] for i in range(n))
    kap = _finite("kappa", kappa)
    energies = tuple(B[i] * omega[i] * (phi[i] + kap) for i in range(n))
    mean_energy = math.fsum(profile[i] * energies[i] for i in range(n))

    if mean_energy <= 0.0:
        if H == 0.0:
            N_total = 0.0
        else:
            raise NoetherHamiltonianSourceClosureError("positive Hamiltonian requires positive mean carrier energy")
    else:
        N_total = H / mean_energy

    occupations = tuple(N_total * profile[i] for i in range(n))
    densities = tuple((occupations[i] / volumes[i]) * energies[i] for i in range(n))
    integrated = math.fsum(densities[i] * volumes[i] for i in range(n))

    return NoetherHamiltonianSourceClosure(
        total_hamiltonian_energy=H,
        total_noether_charge=Q,
        noether_profile=profile,
        carrier_energies=energies,
        mean_carrier_energy=mean_energy,
        inferred_total_occupation=N_total,
        occupations=occupations,
        source_energy_densities=densities,
        integrated_source_energy=integrated,
    )


def uniform_generator_occupation(
    total_hamiltonian_energy: float,
    B_action_joule_second: float,
    omega_rad_s: float,
    phase: float,
    *,
    kappa: float = KAPPA_INFO,
) -> float:
    H = _finite("total_hamiltonian_energy", total_hamiltonian_energy)
    B = _finite("B_action_joule_second", B_action_joule_second)
    omega = _finite("omega_rad_s", omega_rad_s)
    phi = _finite("phase", phase)
    kap = _finite("kappa", kappa)
    if H < 0.0:
        raise NoetherHamiltonianSourceClosureError("total_hamiltonian_energy must be nonnegative")
    epsilon = B * omega * (phi + kap)
    if epsilon <= 0.0:
        if H == 0.0:
            return 0.0
        raise NoetherHamiltonianSourceClosureError("positive Hamiltonian requires positive carrier energy")
    return H / epsilon


def h_over_q_energy_per_charge(
    total_hamiltonian_energy: float,
    total_noether_charge: float,
) -> float:
    H = _finite("total_hamiltonian_energy", total_hamiltonian_energy)
    Q = _finite("total_noether_charge", total_noether_charge)
    if H < 0.0:
        raise NoetherHamiltonianSourceClosureError("total_hamiltonian_energy must be nonnegative")
    if Q <= 0.0:
        raise NoetherHamiltonianSourceClosureError("total_noether_charge must be positive")
    return H / Q


def hamiltonian_profile_density(
    total_hamiltonian_energy: float,
    noether_current_densities: Sequence[float],
    cell_volumes: Sequence[float],
) -> tuple[float, ...]:
    """Uniform energy-per-Noether-charge source: rho_a=(H/Q)j_a."""
    H = _finite("total_hamiltonian_energy", total_hamiltonian_energy)
    if H < 0.0:
        raise NoetherHamiltonianSourceClosureError("total_hamiltonian_energy must be nonnegative")
    j = _vector("noether_current_densities", noether_current_densities)
    volumes = _vector("cell_volumes", cell_volumes)
    if len(j) != len(volumes):
        raise NoetherHamiltonianSourceClosureError("current and volume arrays must have equal length")
    if any(x < 0.0 for x in j):
        raise NoetherHamiltonianSourceClosureError("Noether current densities must be nonnegative")
    if any(v <= 0.0 for v in volumes):
        raise NoetherHamiltonianSourceClosureError("cell volumes must be positive")
    Q = math.fsum(j[i] * volumes[i] for i in range(len(j)))
    if Q <= 0.0:
        raise NoetherHamiltonianSourceClosureError("total Noether charge must be positive")
    epsilon_Q = H / Q
    return tuple(epsilon_Q * x for x in j)
