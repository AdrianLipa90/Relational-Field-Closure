from __future__ import annotations

import math
from dataclasses import dataclass
from collections.abc import Sequence

from src.rfc.relational_generator_source_density import relational_generator_source


class RelationalGeneratorDustError(ValueError):
    pass


Vector3 = tuple[float, float, float]
Matrix3 = tuple[Vector3, Vector3, Vector3]
Matrix4 = tuple[
    tuple[float, float, float, float],
    tuple[float, float, float, float],
    tuple[float, float, float, float],
    tuple[float, float, float, float],
]

C_LIGHT = 299_792_458.0


@dataclass(frozen=True)
class DustADMState:
    rest_energy_density: float
    velocity_m_s: Vector3
    beta: Vector3
    beta2: float
    gamma: float
    rho_n: float
    j_i: Vector3
    S_ij: Matrix3
    S_trace: float
    T_cov: Matrix4


@dataclass(frozen=True)
class ADMDustSourceTerms:
    hamiltonian_rhs: float
    momentum_rhs: Vector3
    evolution_matter_term: Matrix3


def _finite(name: str, value: float) -> float:
    value = float(value)
    if not math.isfinite(value):
        raise RelationalGeneratorDustError(f"{name} must be finite")
    return value


def _velocity3(values: Sequence[float]) -> Vector3:
    if len(values) != 3:
        raise RelationalGeneratorDustError("velocity must contain exactly three components")
    return tuple(_finite(f"velocity[{i}]", x) for i, x in enumerate(values))  # type: ignore[return-value]


def dust_adm_state(rest_energy_density: float, velocity_m_s: Sequence[float]) -> DustADMState:
    """Lift a rest-frame dust energy density to the RF-E11 ADM projections.

    With signature (-,+,+,+), local Eulerian normal n^mu=(1,0,0,0),
    beta_i=v_i/c and gamma=(1-beta^2)^(-1/2):

        T_{mu nu}=rho_0 u_mu u_nu,
        u_mu=(-gamma, gamma beta_i).

    Hence RF-E11 gives

        rho_n = rho_0 gamma^2,
        j_i   = rho_0 gamma^2 beta_i,
        S_ij  = rho_0 gamma^2 beta_i beta_j.
    """

    rho0 = _finite("rest_energy_density", rest_energy_density)
    if rho0 < 0.0:
        raise RelationalGeneratorDustError("rest_energy_density must be nonnegative")
    v = _velocity3(velocity_m_s)
    beta = tuple(x / C_LIGHT for x in v)
    beta2 = math.fsum(x * x for x in beta)
    if beta2 >= 1.0:
        raise RelationalGeneratorDustError("velocity must be strictly subluminal")
    gamma = 1.0 / math.sqrt(1.0 - beta2)
    rho_n = rho0 * gamma * gamma
    j = tuple(rho_n * x for x in beta)
    S = tuple(tuple(rho_n * beta[i] * beta[jj] for jj in range(3)) for i in range(3))
    S_trace = math.fsum(S[i][i] for i in range(3))

    u_cov = (-gamma, gamma * beta[0], gamma * beta[1], gamma * beta[2])
    T_cov = tuple(
        tuple(rho0 * u_cov[mu] * u_cov[nu] for nu in range(4))
        for mu in range(4)
    )

    return DustADMState(
        rest_energy_density=rho0,
        velocity_m_s=v,
        beta=beta,  # type: ignore[arg-type]
        beta2=beta2,
        gamma=gamma,
        rho_n=rho_n,
        j_i=j,  # type: ignore[arg-type]
        S_ij=S,  # type: ignore[arg-type]
        S_trace=S_trace,
        T_cov=T_cov,  # type: ignore[arg-type]
    )


def generator_dust_adm_state(
    B_action_joule_second: float,
    omega_rad_s: float,
    occupation: float,
    area_m2: float,
    radial_length_m: float,
    phase: float,
    velocity_m_s: Sequence[float],
) -> DustADMState:
    source = relational_generator_source(
        B_action_joule_second,
        omega_rad_s,
        occupation,
        area_m2,
        radial_length_m,
        phase,
    )
    if source.energy_density_j_m3 < 0.0:
        raise RelationalGeneratorDustError("dust lift requires the nonnegative source-energy branch")
    return dust_adm_state(source.energy_density_j_m3, velocity_m_s)


def dust_trace_residual(state: DustADMState) -> float:
    """Return (-rho_n+S_trace)+rho_0, which vanishes identically for dust."""
    return -state.rho_n + state.S_trace + state.rest_energy_density


def dust_momentum_stress_residual(state: DustADMState) -> float:
    """Return |j|^2-rho_n*S, an exact rank-one dust identity."""
    j2 = math.fsum(x * x for x in state.j_i)
    return j2 - state.rho_n * state.S_trace


def reconstruct_rest_density(state: DustADMState) -> float:
    return state.rho_n - state.S_trace


def reconstruct_beta_from_adm(state: DustADMState) -> Vector3:
    if state.rho_n == 0.0:
        return (0.0, 0.0, 0.0)
    return tuple(x / state.rho_n for x in state.j_i)  # type: ignore[return-value]


def adm_dust_source_terms(state: DustADMState, kappa_E: float) -> ADMDustSourceTerms:
    """Return the matter sides appearing in RF-E12/RF-E13.

    RF-E12:
      H_rhs = 2 kappa_E rho_n
      M_i   = kappa_E j_i

    RF-E13 matter term in K_ij evolution:
      kappa_E [ 1/2 delta_ij (S-rho_n) - S_ij ]

    This is evaluated in the local orthonormal spatial frame.
    """

    kappa = _finite("kappa_E", kappa_E)
    if kappa <= 0.0:
        raise RelationalGeneratorDustError("kappa_E must be positive")
    h_rhs = 2.0 * kappa * state.rho_n
    m_rhs = tuple(kappa * x for x in state.j_i)
    evo = tuple(
        tuple(
            kappa
            * (
                0.5 * (state.S_trace - state.rho_n) * (1.0 if i == j else 0.0)
                - state.S_ij[i][j]
            )
            for j in range(3)
        )
        for i in range(3)
    )
    return ADMDustSourceTerms(
        hamiltonian_rhs=h_rhs,
        momentum_rhs=m_rhs,  # type: ignore[arg-type]
        evolution_matter_term=evo,  # type: ignore[arg-type]
    )
