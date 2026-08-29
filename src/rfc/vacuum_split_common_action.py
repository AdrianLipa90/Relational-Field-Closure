from __future__ import annotations

import math
from dataclasses import dataclass


class VacuumSplitError(ValueError):
    pass


@dataclass(frozen=True)
class VacuumReferenceState:
    lambda_ref: float
    kappa_e: float
    rho_c: float
    u_ref: float
    lambda_star: float


@dataclass(frozen=True)
class ExchangePartition:
    eta: float
    generator_fraction: float
    kinetic_fraction: float


def _finite(name: str, value: float) -> float:
    value = float(value)
    if not math.isfinite(value):
        raise VacuumSplitError(f"{name} must be finite")
    return value


def _positive(name: str, value: float) -> float:
    value = _finite(name, value)
    if value <= 0.0:
        raise VacuumSplitError(f"{name} must be positive")
    return value


def vacuum_reference_state(
    lambda_ref: float,
    kappa_e: float,
    rho_c: float,
    u_ref: float,
) -> VacuumReferenceState:
    """Absorb all constant metric-proportional vacuum pieces into Lambda_*."""
    lam = _finite("lambda_ref", lambda_ref)
    kap = _positive("kappa_e", kappa_e)
    rho = _finite("rho_c", rho_c)
    u0 = _finite("u_ref", u_ref)
    return VacuumReferenceState(
        lambda_ref=lam,
        kappa_e=kap,
        rho_c=rho,
        u_ref=u0,
        lambda_star=lam + kap * (rho + u0),
    )


def dynamic_lambda(lambda_star: float, kappa_e: float, u_hat: float) -> float:
    lam_star = _finite("lambda_star", lambda_star)
    kap = _positive("kappa_e", kappa_e)
    uh = _finite("u_hat", u_hat)
    return lam_star + kap * uh


def vacuum_split_invariant(
    lambda_ref: float,
    kappa_e: float,
    rho_c: float,
    u_value: float,
) -> float:
    """Geometry sees only Lambda_ref + kappa_E (rho_C + U)."""
    lam = _finite("lambda_ref", lambda_ref)
    kap = _positive("kappa_e", kappa_e)
    rho = _finite("rho_c", rho_c)
    u = _finite("u_value", u_value)
    return lam + kap * (rho + u)


def exchange_partition(eta: float) -> ExchangePartition:
    value = _finite("eta", eta)
    if value < 0.0 or value > 1.0:
        raise VacuumSplitError("eta must lie in [0,1] for the allocation branch")
    return ExchangePartition(
        eta=value,
        generator_fraction=value,
        kinetic_fraction=1.0 - value,
    )


def source_modified_transport_rhs(
    x_ratio: float,
    v_ratio: float,
    eta: float,
    kinetic_density: float,
    duhat_dlnomega: float,
) -> float:
    """RF-F16 sourced extension of dD/dln|omega|.

    D' = 2(1-x-2v) - eta/K * d(Uhat)/dln|omega|.
    """
    x = _finite("x_ratio", x_ratio)
    v = _finite("v_ratio", v_ratio)
    part = exchange_partition(eta)
    K = _positive("kinetic_density", kinetic_density)
    du = _finite("duhat_dlnomega", duhat_dlnomega)
    return 2.0 * (1.0 - x - 2.0 * v) - part.eta * du / K


def fixed_x_generator_potential(
    kinetic_density: float,
    x_ratio: float,
    rho_c: float,
    eta: float,
    u_hat: float,
) -> float:
    """Exact fixed-x solution V_G=(1-x)K/2 + rho_C - eta Uhat."""
    K = _positive("kinetic_density", kinetic_density)
    x = _finite("x_ratio", x_ratio)
    rho = _finite("rho_c", rho_c)
    part = exchange_partition(eta)
    uh = _finite("u_hat", u_hat)
    return 0.5 * (1.0 - x) * K + rho - part.eta * uh


def fixed_x_generator_rho_p(
    kinetic_density: float,
    x_ratio: float,
    rho_c: float,
    eta: float,
    u_hat: float,
) -> tuple[float, float]:
    """Generator stress after source-deformed fixed-x transport."""
    K = _positive("kinetic_density", kinetic_density)
    x = _finite("x_ratio", x_ratio)
    V = fixed_x_generator_potential(K, x, rho_c, eta, u_hat)
    rho = K * (1.0 + x) + V
    p = K * (1.0 - x / 3.0) - V
    return rho, p


def interaction_lagrangian_derivative(eta: float, u_prime: float) -> float:
    """For L_G,int=+eta Uhat, dL_G/dphi=eta U'."""
    part = exchange_partition(eta)
    up = _finite("u_prime", u_prime)
    return part.eta * up


def kinetic_divergence_coefficient(eta: float, u_prime: float) -> float:
    """On the common scalar EOM, div T_kin=(1-eta) U' grad(phi)."""
    part = exchange_partition(eta)
    up = _finite("u_prime", u_prime)
    return part.kinetic_fraction * up


def total_nonvacuum_divergence_coefficient(eta: float, u_prime: float) -> float:
    """Generator + kinetic divergence coefficient equals U' exactly."""
    return interaction_lagrangian_derivative(eta, u_prime) + kinetic_divergence_coefficient(eta, u_prime)


def effective_scalar_mass_sq(eta: float, u_second: float) -> float:
    """Linearized minimal common-action mass: m_eff^2=(1-eta) U''."""
    part = exchange_partition(eta)
    u2 = _finite("u_second", u_second)
    return part.kinetic_fraction * u2


def minimal_common_potential_coefficient(eta: float) -> float:
    """Total minimal action contains -(1-eta) Uhat."""
    return exchange_partition(eta).kinetic_fraction
