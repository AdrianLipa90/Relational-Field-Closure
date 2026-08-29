from __future__ import annotations

import math
from dataclasses import dataclass

from src.rfc.foundational_phase_source_formalism import KAPPA_INFO


class VariationalCommonActionError(ValueError):
    pass


@dataclass(frozen=True)
class CanonicalPhaseState:
    phase_factor: float
    canonical_momentum: float
    phase_rate: float
    energy_per_occupation: float


@dataclass(frozen=True)
class HamiltonianBinding:
    canonical_momentum: float
    hamiltonian: float
    hamiltonian_phase_rate: float
    source_phase_rate: float
    euler_homogeneity_residual: float
    phase_rate_residual: float
    source_energy_residual: float


@dataclass(frozen=True)
class LambdaAllocationBinding:
    required_dH_dphi: float
    supplied_dH_dphi: float
    derivative_residual: float
    hamiltonian_exchange_rate: float
    lambda_exchange_rate: float
    transport_residual: float


@dataclass(frozen=True)
class LambdaPartitionBinding:
    allocation_fraction: float
    required_dH_dphi: float
    supplied_dH_dphi: float
    derivative_residual: float
    generator_exchange_density_rate: float
    kinetic_exchange_density_rate: float
    total_exchange_density_rate: float
    potential_exchange_density_rate: float
    partition_residual: float


@dataclass(frozen=True)
class DirectBELAudit:
    target_Bdot_coefficient: float
    affine_first_order_EL_Bdot_coefficient: float
    generic_assignment_residual: float


@dataclass(frozen=True)
class HomogeneousHamiltonianTransport:
    phase_factor: float
    canonical_momentum: float
    phase_rate: float
    phase_acceleration: float
    B_rate: float
    f11_left_hand_side: float
    explicit_hamiltonian_rate: float
    identity_residual: float


@dataclass(frozen=True)
class ConstantBLinearBranch:
    phase_factor: float
    canonical_momentum: float
    phase_rate: float
    phase_acceleration: float
    hamiltonian: float
    dH_dX: float
    momentum_rate: float
    reconstructed_B_rate: float
    f11_closed_residual: float


@dataclass(frozen=True)
class NoetherHamiltonianBinding:
    noether_energy_per_charge: float
    generator_energy_per_charge: float
    residual: float


def _finite(name: str, value: float) -> float:
    out = float(value)
    if not math.isfinite(out):
        raise VariationalCommonActionError(f"{name} must be finite")
    return out


def canonical_phase_state(
    B_action: float,
    relational_phase: float,
    omega: float,
    *,
    kappa: float = KAPPA_INFO,
    require_nondegenerate: bool = True,
) -> CanonicalPhaseState:
    """RF-F13 canonical phase-space coordinates.

    X = Phi_C + kappa,
    P = B X,
    epsilon_G = P omega = B X omega.

    The common-action branch uses B=P/X, so X=0 is excluded when
    ``require_nondegenerate`` is true.
    """

    B = _finite("B_action", B_action)
    phi = _finite("relational_phase", relational_phase)
    w = _finite("omega", omega)
    kap = _finite("kappa", kappa)
    X = phi + kap
    if require_nondegenerate and X == 0.0:
        raise VariationalCommonActionError("relational_phase+kappa must be nonzero on the canonical B=P/X branch")
    P = B * X
    return CanonicalPhaseState(
        phase_factor=X,
        canonical_momentum=P,
        phase_rate=w,
        energy_per_occupation=P * w,
    )


def hamiltonian_binding(
    B_action: float,
    relational_phase: float,
    omega: float,
    hamiltonian: float,
    dH_dP: float,
    *,
    kappa: float = KAPPA_INFO,
) -> HamiltonianBinding:
    """Audit the RF-F13 Hamiltonian/source identification.

    Hamilton's first equation supplies omega=dH/dP.  The relational source
    energy is epsilon_G=P*omega.  Equality H_G=epsilon_G is therefore the
    one-dimensional Euler homogeneity condition H_G=P*dH/dP.
    """

    state = canonical_phase_state(B_action, relational_phase, omega, kappa=kappa)
    H = _finite("hamiltonian", hamiltonian)
    Hp = _finite("dH_dP", dH_dP)
    predicted_energy = state.canonical_momentum * Hp
    return HamiltonianBinding(
        canonical_momentum=state.canonical_momentum,
        hamiltonian=H,
        hamiltonian_phase_rate=Hp,
        source_phase_rate=state.phase_rate,
        euler_homogeneity_residual=H - predicted_energy,
        phase_rate_residual=Hp - state.phase_rate,
        source_energy_residual=H - state.energy_per_occupation,
    )


def noether_hamiltonian_binding(
    hamiltonian_total: float,
    noether_charge: float,
    B_action: float,
    relational_phase: float,
    omega: float,
    *,
    carrier_quantum: float = 1.0,
    kappa: float = KAPPA_INFO,
) -> NoetherHamiltonianBinding:
    """RF-S16/RF-S22 compatible energy-per-charge audit.

    epsilon_Q = epsilon_occ/q0 = B*omega*(Phi+kappa)/q0,
    while the Noether/Hamiltonian branch supplies H/Q.
    """

    H = _finite("hamiltonian_total", hamiltonian_total)
    Q = _finite("noether_charge", noether_charge)
    q0 = _finite("carrier_quantum", carrier_quantum)
    if Q == 0.0:
        raise VariationalCommonActionError("noether_charge must be nonzero")
    if q0 <= 0.0:
        raise VariationalCommonActionError("carrier_quantum must be positive")
    state = canonical_phase_state(B_action, relational_phase, omega, kappa=kappa)
    eps_noether = H / Q
    eps_generator = state.energy_per_occupation / q0
    return NoetherHamiltonianBinding(
        noether_energy_per_charge=eps_noether,
        generator_energy_per_charge=eps_generator,
        residual=eps_noether - eps_generator,
    )


def lambda_potential_allocation_binding(
    potential_derivative: float,
    proper_density: float,
    supplied_dH_dphi: float,
    phi_dot: float,
) -> LambdaAllocationBinding:
    """Per-occupation Hamiltonian condition for the full RF-F7 Lambda transfer.

    With Lambda0=Lambda_ref+kappa_E*U(phi_L), RF-F7 requires

        Hdot_G = -Lambda_dot/(kappa_E*n) = -(U'(phi_L)/n)*phi_dot.

    For a canonical subsystem Hamiltonian H_G(X,P,phi_L), Hamilton's equations
    cancel its implicit X/P time dependence, leaving

        Hdot_G = partial_phi H_G * phi_dot.

    Therefore the full generator-allocation surface is

        partial_phi H_G = -U'/n.
    """

    Up = _finite("potential_derivative", potential_derivative)
    n = _finite("proper_density", proper_density)
    Hphi = _finite("supplied_dH_dphi", supplied_dH_dphi)
    phidot = _finite("phi_dot", phi_dot)
    if n <= 0.0:
        raise VariationalCommonActionError("proper_density must be positive")
    target = -Up / n
    hdot = Hphi * phidot
    lambda_rate = target * phidot
    return LambdaAllocationBinding(
        required_dH_dphi=target,
        supplied_dH_dphi=Hphi,
        derivative_residual=Hphi - target,
        hamiltonian_exchange_rate=hdot,
        lambda_exchange_rate=lambda_rate,
        transport_residual=hdot - lambda_rate,
    )


def lambda_partition_binding(
    potential_derivative: float,
    proper_density: float,
    allocation_fraction: float,
    supplied_dH_dphi: float,
    phi_dot: float,
) -> LambdaPartitionBinding:
    """Unified RF-L2 <-> RF-F7 dynamic-Lambda allocation ledger.

    Let eta in [0,1] assign the metric-potential transfer between the
    relational generator and the Lambda carrier kinetic sector:

        n * partial_phi H_G = -eta * U_L',
        generator exchange density = eta * U_L' * phi_dot,
        kinetic exchange density   = (1-eta) * U_L' * phi_dot.

    Their sum is U_L'*phi_dot = Lambda_dot/kappa_E.
    eta=0 reproduces the RF-L2 allocation; eta=1 reproduces RF-F7.
    """

    Up = _finite("potential_derivative", potential_derivative)
    n = _finite("proper_density", proper_density)
    eta = _finite("allocation_fraction", allocation_fraction)
    Hphi = _finite("supplied_dH_dphi", supplied_dH_dphi)
    phidot = _finite("phi_dot", phi_dot)
    if n <= 0.0:
        raise VariationalCommonActionError("proper_density must be positive")
    if eta < 0.0 or eta > 1.0:
        raise VariationalCommonActionError("allocation_fraction must lie in [0,1]")
    target = -eta * Up / n
    generator = eta * Up * phidot
    kinetic = (1.0 - eta) * Up * phidot
    potential = Up * phidot
    total = generator + kinetic
    return LambdaPartitionBinding(
        allocation_fraction=eta,
        required_dH_dphi=target,
        supplied_dH_dphi=Hphi,
        derivative_residual=Hphi - target,
        generator_exchange_density_rate=generator,
        kinetic_exchange_density_rate=kinetic,
        total_exchange_density_rate=total,
        potential_exchange_density_rate=potential,
        partition_residual=total - potential,
    )


def direct_B_first_order_el_audit(
    relational_phase: float,
    omega: float,
    *,
    kappa: float = KAPPA_INFO,
) -> DirectBELAudit:
    """Helmholtz-style audit of a direct first-order EL assignment to B.

    For any first-order local Lagrangian that is affine in Bdot,

        L=A(B,X,Xdot) Bdot + C(B,X,Xdot),

    the Bdot terms cancel identically in E_B=partial_B L-d/dt(partial_Bdot L).
    RF-F11 carries the generic coefficient X*omega multiplying Bdot.  The
    returned residual records the mismatch; RF-F13 consequently assigns B
    through the canonical momentum P=B X and assigns transport to the
    Hamiltonian/Bianchi balance.
    """

    phi = _finite("relational_phase", relational_phase)
    w = _finite("omega", omega)
    kap = _finite("kappa", kappa)
    X = phi + kap
    target = X * w
    el_coeff = 0.0
    return DirectBELAudit(
        target_Bdot_coefficient=target,
        affine_first_order_EL_Bdot_coefficient=el_coeff,
        generic_assignment_residual=target - el_coeff,
    )


def homogeneous_hamiltonian_transport_identity(
    B_action: float,
    phase_factor: float,
    h_value: float,
    dh_dX: float,
    dh_dphi: float,
    phi_dot: float,
) -> HomogeneousHamiltonianTransport:
    """Exact RF-F11 identity for H_G=P*h(X,phi_L).

    With P=B X and H_G=P*h, Hamilton's equations give

        Xdot=h,
        Pdot=-P*h_X.

    Reconstructing B=P/X and omega=h yields

        X(Bdot*omega+B*omega_dot)+B*omega^2
        = P*h_phi*phi_dot
        = (partial_phi H_G)*phi_dot.

    The dynamic-Lambda RF-F11 target follows when
    partial_phi H_G=-U_L'/n.
    """

    B = _finite("B_action", B_action)
    X = _finite("phase_factor", phase_factor)
    h = _finite("h_value", h_value)
    hx = _finite("dh_dX", dh_dX)
    hphi = _finite("dh_dphi", dh_dphi)
    phidot = _finite("phi_dot", phi_dot)
    if X == 0.0:
        raise VariationalCommonActionError("phase_factor must be nonzero")
    P = B * X
    Pdot = -P * hx
    Bdot = (Pdot * X - P * h) / (X * X)
    omega_dot = hx * h + hphi * phidot
    lhs = X * (Bdot * h + B * omega_dot) + B * h * h
    hdot_external = P * hphi * phidot
    return HomogeneousHamiltonianTransport(
        phase_factor=X,
        canonical_momentum=P,
        phase_rate=h,
        phase_acceleration=omega_dot,
        B_rate=Bdot,
        f11_left_hand_side=lhs,
        explicit_hamiltonian_rate=hdot_external,
        identity_residual=lhs - hdot_external,
    )


def constant_B_linear_hamiltonian_branch(
    B_action: float,
    phase_factor: float,
    invariant_C: float,
) -> ConstantBLinearBranch:
    """Exact RF-F11 constant-B/constant-Lambda realization.

    A degree-one Hamiltonian H=P*h(X) obeys H=P*dH/dP.  Requiring B=P/X
    to stay constant under Hamilton evolution fixes h+X h'=0, hence

        h(X)=C/X,
        omega=C/X,
        H=B*C=const,
        omega_dot=-omega^2/X.
    """

    B = _finite("B_action", B_action)
    X = _finite("phase_factor", phase_factor)
    C = _finite("invariant_C", invariant_C)
    if X == 0.0:
        raise VariationalCommonActionError("phase_factor must be nonzero")
    P = B * X
    h = C / X
    hp_x = -C / (X * X)
    H = P * h
    dH_dX = P * hp_x
    Pdot = -dH_dX
    Xdot = h
    Bdot = (Pdot * X - P * Xdot) / (X * X)
    omega_dot = -C * C / (X**3)
    f11 = X * (Bdot * h + B * omega_dot) + B * h * h
    return ConstantBLinearBranch(
        phase_factor=X,
        canonical_momentum=P,
        phase_rate=h,
        phase_acceleration=omega_dot,
        hamiltonian=H,
        dH_dX=dH_dX,
        momentum_rate=Pdot,
        reconstructed_B_rate=Bdot,
        f11_closed_residual=f11,
    )
