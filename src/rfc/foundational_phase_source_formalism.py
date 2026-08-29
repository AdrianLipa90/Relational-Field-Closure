from __future__ import annotations

import cmath
import math
from dataclasses import dataclass
from collections.abc import Sequence


KAPPA_INFO = math.log(2.0) / (24.0 * math.pi)
C_LIGHT = 299_792_458.0
FULL_TETRA_FS_AREA = math.pi


class FoundationalPhaseSourceError(ValueError):
    pass


@dataclass(frozen=True)
class ConnectionSignBridge:
    berry_plus: float
    phase_minus: float


@dataclass(frozen=True)
class RelationalPhaseState:
    theta_endpoint: float
    theta_reference: float
    connection_line_integral: float
    lifted_relational_phase: float


@dataclass(frozen=True)
class PhaseCell:
    omega_rad_s: float
    area_fs_dimensionless: float
    phase_clock_length_m: float
    projective_area_m2: float
    relational_volume_m3: float


@dataclass(frozen=True)
class PhaseEnergyState:
    B_action_joule_second: float
    omega_rad_s: float
    relational_phase: float
    kappa: float
    phase_factor: float
    energy_per_occupation_joule: float
    phase_action_joule_second: float


@dataclass(frozen=True)
class CovariantSourceState:
    proper_occupation_density_m3: float
    energy_per_occupation_joule: float
    energy_density_j_m3: float


def _finite(name: str, value: float) -> float:
    value = float(value)
    if not math.isfinite(value):
        raise FoundationalPhaseSourceError(f"{name} must be finite")
    return value


def _finite_vector(name: str, values: Sequence[float], expected: int | None = None) -> tuple[float, ...]:
    if expected is not None and len(values) != expected:
        raise FoundationalPhaseSourceError(f"{name} must have length {expected}")
    if len(values) == 0:
        raise FoundationalPhaseSourceError(f"{name} must be nonempty")
    return tuple(_finite(f"{name}[{i}]", x) for i, x in enumerate(values))


def berry_connection_sign_bridge(berry_plus: float) -> ConnectionSignBridge:
    """Map the RF-01/RF-M0 Berry sign convention to the RF-N1B2M phase convention.

    RF-01/RF-M0 use A_plus=-i<u|du>, transforming as A_plus -> A_plus+d lambda.
    RF-N1B2M uses A_minus=+i<u|du>=-A_plus, transforming as
    A_minus -> A_minus-d lambda.
    """

    plus = _finite("berry_plus", berry_plus)
    return ConnectionSignBridge(berry_plus=plus, phase_minus=-plus)


def relational_lifted_phase(
    theta_endpoint: float,
    theta_reference: float,
    connection_line_integral_minus: float,
) -> RelationalPhaseState:
    """Wilson-line-dressed lifted relative phase.

    With the RF-N1B2M sign convention A_minus -> A_minus-d lambda and
    theta -> theta+lambda,

        Phi_C = theta(x)-theta(x_ref)+int_C A_minus

    is invariant under the simultaneous endpoint/connection transformation.
    The value is real-valued and therefore retains the chosen lift/winding.
    """

    theta_x = _finite("theta_endpoint", theta_endpoint)
    theta_0 = _finite("theta_reference", theta_reference)
    line = _finite("connection_line_integral_minus", connection_line_integral_minus)
    return RelationalPhaseState(
        theta_endpoint=theta_x,
        theta_reference=theta_0,
        connection_line_integral=line,
        lifted_relational_phase=theta_x - theta_0 + line,
    )


def transformed_connection_line_integral_minus(
    connection_line_integral_minus: float,
    lambda_endpoint: float,
    lambda_reference: float,
) -> float:
    line = _finite("connection_line_integral_minus", connection_line_integral_minus)
    lam_x = _finite("lambda_endpoint", lambda_endpoint)
    lam_0 = _finite("lambda_reference", lambda_reference)
    return line - (lam_x - lam_0)


def path_holonomy_difference(line_integral_c1: float, line_integral_c2: float) -> float:
    """Lifted phase difference between two paths with common endpoints."""

    return _finite("line_integral_c1", line_integral_c1) - _finite("line_integral_c2", line_integral_c2)


def projective_holonomy(lifted_loop_phase: float) -> complex:
    return cmath.exp(1j * _finite("lifted_loop_phase", lifted_loop_phase))


def euler_projective_closure_residual(lifted_loop_phase: float) -> float:
    """Distance from projective Euler closure exp(i Gamma)=1."""

    return abs(projective_holonomy(lifted_loop_phase) - 1.0)


def euler_root_triad(relational_phase: float) -> tuple[float, float, float]:
    phi = _finite("relational_phase", relational_phase)
    return (phi, phi + 2.0 * math.pi / 3.0, phi + 4.0 * math.pi / 3.0)


def euler_root_triad_closure_residual(relational_phase: float) -> float:
    triad = euler_root_triad(relational_phase)
    return abs(sum(cmath.exp(1j * x) for x in triad))


def phase_cell(
    omega_rad_s: float,
    *,
    area_fs_dimensionless: float = FULL_TETRA_FS_AREA,
) -> PhaseCell:
    omega = _finite("omega_rad_s", omega_rad_s)
    a_fs = _finite("area_fs_dimensionless", area_fs_dimensionless)
    if omega == 0.0:
        raise FoundationalPhaseSourceError("omega_rad_s must be nonzero")
    if a_fs <= 0.0:
        raise FoundationalPhaseSourceError("area_fs_dimensionless must be positive")
    rate = abs(omega)
    length = C_LIGHT / rate
    area = a_fs * C_LIGHT**2 / rate**2
    volume = a_fs * C_LIGHT**3 / rate**3
    return PhaseCell(
        omega_rad_s=omega,
        area_fs_dimensionless=a_fs,
        phase_clock_length_m=length,
        projective_area_m2=area,
        relational_volume_m3=volume,
    )


def phase_energy_state(
    B_action_joule_second: float,
    omega_rad_s: float,
    relational_phase: float,
    *,
    kappa: float = KAPPA_INFO,
) -> PhaseEnergyState:
    B = _finite("B_action_joule_second", B_action_joule_second)
    omega = _finite("omega_rad_s", omega_rad_s)
    phi = _finite("relational_phase", relational_phase)
    kap = _finite("kappa", kappa)
    factor = phi + kap
    energy = B * omega * factor
    action = 0.5 * B * factor * factor
    return PhaseEnergyState(
        B_action_joule_second=B,
        omega_rad_s=omega,
        relational_phase=phi,
        kappa=kap,
        phase_factor=factor,
        energy_per_occupation_joule=energy,
        phase_action_joule_second=action,
    )


def phase_action_rate(
    B_action_joule_second: float,
    B_rate_joule: float,
    omega_rad_s: float,
    relational_phase: float,
    *,
    kappa: float = KAPPA_INFO,
) -> float:
    """Comoving derivative of S_phi=(B/2)(Phi+kappa)^2.

    B_rate_joule is dB/dtau, with units J.  Since dPhi/dtau=omega,

        dS_phi/dtau = B*omega*(Phi+kappa) + 1/2*Bdot*(Phi+kappa)^2.
    """

    state = phase_energy_state(B_action_joule_second, omega_rad_s, relational_phase, kappa=kappa)
    Bdot = _finite("B_rate_joule", B_rate_joule)
    return state.energy_per_occupation_joule + 0.5 * Bdot * state.phase_factor**2


def energy_from_phase_action_rate(
    action_rate_joule: float,
    B_rate_joule: float,
    relational_phase: float,
    *,
    kappa: float = KAPPA_INFO,
) -> float:
    rate = _finite("action_rate_joule", action_rate_joule)
    Bdot = _finite("B_rate_joule", B_rate_joule)
    phi = _finite("relational_phase", relational_phase)
    kap = _finite("kappa", kappa)
    return rate - 0.5 * Bdot * (phi + kap) ** 2


def occupation_density_from_cell(
    occupation: float,
    omega_rad_s: float,
    *,
    area_fs_dimensionless: float = FULL_TETRA_FS_AREA,
) -> float:
    N = _finite("occupation", occupation)
    if N < 0.0:
        raise FoundationalPhaseSourceError("occupation must be nonnegative")
    cell = phase_cell(omega_rad_s, area_fs_dimensionless=area_fs_dimensionless)
    return N / cell.relational_volume_m3


def covariant_source_state(
    occupation: float,
    B_action_joule_second: float,
    omega_rad_s: float,
    relational_phase: float,
    *,
    area_fs_dimensionless: float = FULL_TETRA_FS_AREA,
    kappa: float = KAPPA_INFO,
) -> CovariantSourceState:
    n = occupation_density_from_cell(
        occupation,
        omega_rad_s,
        area_fs_dimensionless=area_fs_dimensionless,
    )
    energy = phase_energy_state(
        B_action_joule_second,
        omega_rad_s,
        relational_phase,
        kappa=kappa,
    ).energy_per_occupation_joule
    return CovariantSourceState(
        proper_occupation_density_m3=n,
        energy_per_occupation_joule=energy,
        energy_density_j_m3=n * energy,
    )


def direct_generator_density(
    B_action_joule_second: float,
    omega_rad_s: float,
    occupation: float,
    area_m2: float,
    radial_length_m: float,
    relational_phase: float,
    *,
    kappa: float = KAPPA_INFO,
) -> float:
    B = _finite("B_action_joule_second", B_action_joule_second)
    omega = _finite("omega_rad_s", omega_rad_s)
    N = _finite("occupation", occupation)
    area = _finite("area_m2", area_m2)
    radius = _finite("radial_length_m", radial_length_m)
    phi = _finite("relational_phase", relational_phase)
    kap = _finite("kappa", kappa)
    if N < 0.0:
        raise FoundationalPhaseSourceError("occupation must be nonnegative")
    if area <= 0.0 or radius <= 0.0:
        raise FoundationalPhaseSourceError("area and radial length must be positive")
    return B * omega * N * (phi + kap) / (area * radius)


def proper_density_from_fourcurrent(J_contravariant: Sequence[float]) -> float:
    J = _finite_vector("J_contravariant", J_contravariant, expected=4)
    norm_sq = -(J[0] ** 2) + sum(x * x for x in J[1:])
    if J[0] <= 0.0 or norm_sq >= 0.0:
        raise FoundationalPhaseSourceError("four-current must be future timelike")
    return math.sqrt(-norm_sq)


def dust_tensor_from_current(
    energy_per_occupation_joule: float,
    J_contravariant: Sequence[float],
) -> tuple[tuple[float, float, float, float], ...]:
    epsilon = _finite("energy_per_occupation_joule", energy_per_occupation_joule)
    J = _finite_vector("J_contravariant", J_contravariant, expected=4)
    if epsilon < 0.0:
        raise FoundationalPhaseSourceError("energy_per_occupation_joule must be nonnegative")
    n = proper_density_from_fourcurrent(J)
    return tuple(tuple(epsilon * J[i] * J[j] / n for j in range(4)) for i in range(4))


def dust_divergence_from_current_conservation(
    proper_density: float,
    energy_per_occupation: float,
    comoving_energy_rate: float,
    four_velocity_covariant: Sequence[float],
    four_acceleration_covariant: Sequence[float],
) -> tuple[float, float, float, float]:
    """Algebraic RF-F7 balance identity for conserved J^mu=n u^mu.

        nabla^mu T_{mu nu} = n [dot(epsilon) u_nu + epsilon a_nu].
    """

    n = _finite("proper_density", proper_density)
    epsilon = _finite("energy_per_occupation", energy_per_occupation)
    edot = _finite("comoving_energy_rate", comoving_energy_rate)
    u = _finite_vector("four_velocity_covariant", four_velocity_covariant, expected=4)
    a = _finite_vector("four_acceleration_covariant", four_acceleration_covariant, expected=4)
    if n < 0.0:
        raise FoundationalPhaseSourceError("proper_density must be nonnegative")
    return tuple(n * (edot * u[i] + epsilon * a[i]) for i in range(4))  # type: ignore[return-value]


def eos_from_energy_scaling_exponent(q_energy: float) -> float:
    """RF-F8 perfect-fluid EOS on the conserved comoving phase-cell branch.

    For V_R proportional to |omega|^-3, conserved comoving occupation and
    epsilon proportional locally to |omega|^q, continuity gives w=q/3.
    """

    q = _finite("q_energy", q_energy)
    return q / 3.0


def generator_prefactor_scaling_for_eos(w: float) -> float:
    """Return d ln[B(Phi+kappa)] / d ln|omega| required by a target w.

    Since epsilon=B*omega*(Phi+kappa), q_energy=1+q_prefactor and w=q_energy/3,

        q_prefactor = 3w-1.
    """

    w_value = _finite("w", w)
    return 3.0 * w_value - 1.0


def density_scaling_exponent_from_eos(w: float) -> float:
    """Return q_rho in rho proportional to |omega|^q_rho on the same branch."""

    w_value = _finite("w", w)
    return 3.0 * (1.0 + w_value)


def expansion_from_phase_rate_log_derivative(dln_abs_omega_dtau: float) -> float:
    """Number-current continuity with V_R proportional to |omega|^-3 gives theta=-3 dln|omega|/dtau."""

    return -3.0 * _finite("dln_abs_omega_dtau", dln_abs_omega_dtau)
