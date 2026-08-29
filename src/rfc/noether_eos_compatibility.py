from __future__ import annotations

import math
from dataclasses import dataclass


class NoetherEOSCompatibilityError(ValueError):
    pass


@dataclass(frozen=True)
class MicroscopicPhaseEOS:
    amplitude_squared: float
    phase_rate: float
    spatial_phase_norm: float
    potential_density: float
    temporal_kinetic_density: float
    spatial_ratio: float
    potential_ratio: float
    energy_density: float
    isotropic_pressure: float
    equation_of_state: float
    action_charge_density: float
    energy_per_action_charge_rate: float
    generator_prefactor_ratio: float
    vacuum_gap: float


@dataclass(frozen=True)
class PhaseCellEOSCompatibility:
    microscopic_w: float
    required_prefactor_log_slope: float
    supplied_prefactor_log_slope: float
    phase_cell_w: float
    eos_residual: float


@dataclass(frozen=True)
class RadiationCompatibility:
    spatial_ratio: float
    potential_ratio: float
    radiation_surface_residual: float
    generator_prefactor_ratio: float


@dataclass(frozen=True)
class BranchSignature:
    name: str
    equation_of_state: float
    generator_prefactor_ratio: float
    phase_cell_required_slope: float
    vacuum_gap: float


def _finite(name: str, value: float) -> float:
    out = float(value)
    if not math.isfinite(out):
        raise NoetherEOSCompatibilityError(f"{name} must be finite")
    return out


def microscopic_phase_eos(
    amplitude_squared: float,
    phase_rate: float,
    spatial_phase_norm: float = 0.0,
    potential_density: float = 0.0,
) -> MicroscopicPhaseEOS:
    """Isotropic-average stress ledger for the RF-E6/RF-E7 phase sector.

    In a local orthonormal (-,+,+,+) frame let

        q_a=(omega, k-vector),  |k-vector|=k,
        psi=A exp(i theta),      A2=A^2.

    The canonical scalar action gives

        rho = A2*(omega^2+k^2)+V,
        p_iso = A2*(omega^2-k^2/3)-V,
        j_theta = 2*A2*omega

    on the positive-orientation carrier branch.  Therefore the total scalar
    energy/action-charge rate is rho/j_theta and the F13 generator binding
    coordinate is

        P/q0 = (rho/j_theta)/omega.
    """

    A2 = _finite("amplitude_squared", amplitude_squared)
    omega = _finite("phase_rate", phase_rate)
    k = _finite("spatial_phase_norm", spatial_phase_norm)
    V = _finite("potential_density", potential_density)
    if A2 <= 0.0:
        raise NoetherEOSCompatibilityError("amplitude_squared must be positive")
    if omega <= 0.0:
        raise NoetherEOSCompatibilityError("phase_rate must be positive on this oriented carrier branch")
    if k < 0.0:
        raise NoetherEOSCompatibilityError("spatial_phase_norm must be nonnegative")
    if V < 0.0:
        raise NoetherEOSCompatibilityError("potential_density must be nonnegative")

    K = A2 * omega * omega
    x = (k / omega) ** 2
    v = V / K
    rho = A2 * (omega * omega + k * k) + V
    pressure = A2 * (omega * omega - k * k / 3.0) - V
    if rho <= 0.0:
        raise NoetherEOSCompatibilityError("energy density must be positive")
    w = pressure / rho
    j = 2.0 * A2 * omega
    eps_rate = rho / j
    prefactor_ratio = eps_rate / omega
    vacuum_gap = rho + pressure
    return MicroscopicPhaseEOS(
        amplitude_squared=A2,
        phase_rate=omega,
        spatial_phase_norm=k,
        potential_density=V,
        temporal_kinetic_density=K,
        spatial_ratio=x,
        potential_ratio=v,
        energy_density=rho,
        isotropic_pressure=pressure,
        equation_of_state=w,
        action_charge_density=j,
        energy_per_action_charge_rate=eps_rate,
        generator_prefactor_ratio=prefactor_ratio,
        vacuum_gap=vacuum_gap,
    )


def required_prefactor_log_slope_for_eos(w: float) -> float:
    """RF-F8 requirement d ln|P| / d ln|omega| = 3w-1 for P=B(Phi+kappa)."""

    value = _finite("w", w)
    return 3.0 * value - 1.0


def phase_cell_eos_from_prefactor_log_slope(prefactor_log_slope: float) -> float:
    slope = _finite("prefactor_log_slope", prefactor_log_slope)
    return (1.0 + slope) / 3.0


def phase_cell_compatibility(
    microscopic_w: float,
    supplied_prefactor_log_slope: float,
) -> PhaseCellEOSCompatibility:
    w = _finite("microscopic_w", microscopic_w)
    supplied = _finite("supplied_prefactor_log_slope", supplied_prefactor_log_slope)
    required = required_prefactor_log_slope_for_eos(w)
    phase_cell_w = phase_cell_eos_from_prefactor_log_slope(supplied)
    return PhaseCellEOSCompatibility(
        microscopic_w=w,
        required_prefactor_log_slope=required,
        supplied_prefactor_log_slope=supplied,
        phase_cell_w=phase_cell_w,
        eos_residual=phase_cell_w - w,
    )


def radiation_compatibility(
    amplitude_squared: float,
    phase_rate: float,
    spatial_phase_norm: float = 0.0,
    potential_density: float = 0.0,
) -> RadiationCompatibility:
    """Exact RF-E7 radiation surface.

    Write x=k^2/omega^2 and v=V/(A^2 omega^2).  From the microscopic tensor,

        w=1/3  <=>  x + 2v = 1.

    The corresponding total-energy/action-charge generator ratio is

        P/q0 = 1/2 * (1+x+v).
    """

    state = microscopic_phase_eos(
        amplitude_squared,
        phase_rate,
        spatial_phase_norm,
        potential_density,
    )
    residual = state.spatial_ratio + 2.0 * state.potential_ratio - 1.0
    return RadiationCompatibility(
        spatial_ratio=state.spatial_ratio,
        potential_ratio=state.potential_ratio,
        radiation_surface_residual=residual,
        generator_prefactor_ratio=state.generator_prefactor_ratio,
    )


def normal_phase_kinetic_branch(amplitude_squared: float, phase_rate: float) -> BranchSignature:
    """RF-N1B2O / RF-E4 pure normal kinetic branch."""

    state = microscopic_phase_eos(amplitude_squared, phase_rate)
    return BranchSignature(
        name="NORMAL_PHASE_KINETIC",
        equation_of_state=state.equation_of_state,
        generator_prefactor_ratio=state.generator_prefactor_ratio,
        phase_cell_required_slope=required_prefactor_log_slope_for_eos(state.equation_of_state),
        vacuum_gap=state.vacuum_gap,
    )


def isotropic_null_phase_branch(amplitude_squared: float, phase_rate: float) -> BranchSignature:
    """Massless null phase modes after isotropic directional averaging."""

    state = microscopic_phase_eos(
        amplitude_squared,
        phase_rate,
        spatial_phase_norm=phase_rate,
        potential_density=0.0,
    )
    return BranchSignature(
        name="ISOTROPIC_NULL_PHASE",
        equation_of_state=state.equation_of_state,
        generator_prefactor_ratio=state.generator_prefactor_ratio,
        phase_cell_required_slope=required_prefactor_log_slope_for_eos(state.equation_of_state),
        vacuum_gap=state.vacuum_gap,
    )


def homogeneous_radiation_completion_branch(amplitude_squared: float, phase_rate: float) -> BranchSignature:
    """Pure-normal homogeneous scalar tuned to the exact w=1/3 surface V=K/2."""

    K = _finite("amplitude_squared", amplitude_squared) * _finite("phase_rate", phase_rate) ** 2
    state = microscopic_phase_eos(amplitude_squared, phase_rate, 0.0, 0.5 * K)
    return BranchSignature(
        name="HOMOGENEOUS_RADIATION_COMPLETION",
        equation_of_state=state.equation_of_state,
        generator_prefactor_ratio=state.generator_prefactor_ratio,
        phase_cell_required_slope=required_prefactor_log_slope_for_eos(state.equation_of_state),
        vacuum_gap=state.vacuum_gap,
    )


def homogeneous_dust_branch(amplitude_squared: float, phase_rate: float) -> BranchSignature:
    """RF-E5 homogeneous on-shell dust surface V=K."""

    K = _finite("amplitude_squared", amplitude_squared) * _finite("phase_rate", phase_rate) ** 2
    state = microscopic_phase_eos(amplitude_squared, phase_rate, 0.0, K)
    return BranchSignature(
        name="HOMOGENEOUS_DUST",
        equation_of_state=state.equation_of_state,
        generator_prefactor_ratio=state.generator_prefactor_ratio,
        phase_cell_required_slope=required_prefactor_log_slope_for_eos(state.equation_of_state),
        vacuum_gap=state.vacuum_gap,
    )


def phase_noether_prefactor_binding_residual(generator_prefactor_ratio: float) -> float:
    """Zero on the RF-N1B2O normal collective phase-energy binding P/q0=1/2."""

    ratio = _finite("generator_prefactor_ratio", generator_prefactor_ratio)
    return ratio - 0.5


def total_scalar_prefactor_binding_residual(
    generator_prefactor_ratio: float,
    microscopic_state: MicroscopicPhaseEOS,
) -> float:
    """Zero when F13 P/q0 carries the complete scalar energy/current ratio."""

    ratio = _finite("generator_prefactor_ratio", generator_prefactor_ratio)
    return ratio - microscopic_state.generator_prefactor_ratio


def vacuum_current_gap(amplitude_squared: float, phase_rate: float, spatial_phase_norm: float = 0.0) -> float:
    """rho+p for the phase kinetic sector; positive for every nonzero oriented phase current.

    The potential cancels from rho+p, giving

        rho+p = 2 A^2 omega^2 + (2/3) A^2 k^2 > 0.

    The exact metric-proportional vacuum surface is consequently reached at
    the zero-phase-current boundary of this scalar carrier ledger.
    """

    A2 = _finite("amplitude_squared", amplitude_squared)
    omega = _finite("phase_rate", phase_rate)
    k = _finite("spatial_phase_norm", spatial_phase_norm)
    if A2 <= 0.0:
        raise NoetherEOSCompatibilityError("amplitude_squared must be positive")
    if omega < 0.0 or k < 0.0:
        raise NoetherEOSCompatibilityError("phase-rate magnitudes must be nonnegative")
    return 2.0 * A2 * omega * omega + (2.0 / 3.0) * A2 * k * k
