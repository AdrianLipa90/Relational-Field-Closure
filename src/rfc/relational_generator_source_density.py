from __future__ import annotations

import math
from dataclasses import dataclass


KAPPA_INFO = math.log(2.0) / (24.0 * math.pi)
C_LIGHT = 299_792_458.0


class RelationalGeneratorSourceError(ValueError):
    pass


@dataclass(frozen=True)
class RelationalGeneratorSource:
    B_action_joule_second: float
    omega_rad_s: float
    occupation: float
    area_m2: float
    radial_length_m: float
    phase: float
    kappa: float
    phase_factor: float
    volume_m3: float
    occupation_density_m3: float
    carrier_energy_joule: float
    energy_density_j_m3: float
    mass_density_kg_m3: float
    positive_source_admitted: bool


def _finite(name: str, value: float) -> float:
    value = float(value)
    if not math.isfinite(value):
        raise RelationalGeneratorSourceError(f"{name} must be finite")
    return value


def relational_generator_source(
    B_action_joule_second: float,
    omega_rad_s: float,
    occupation: float,
    area_m2: float,
    radial_length_m: float,
    phase: float,
    *,
    kappa: float = KAPPA_INFO,
) -> RelationalGeneratorSource:
    """Evaluate the RFC source-density realization of

        [B(t) * omega(t) * N(t) / (A * R)] * (phi + kappa).

    The source interpretation used by RF-S13 is dimensionally typed as follows:
    B carries action units J s, omega carries s^-1, N is a dimensionless
    occupation, A is an area, R is a radial length, and phi+kappa is
    dimensionless.  Therefore B*omega*(phi+kappa) is an energy per occupied
    carrier and N/(A R) is an occupation density.

    The signed formula is preserved exactly.  ``positive_source_admitted``
    records whether the resulting matter-energy density belongs to the
    nonnegative source sector.
    """

    B = _finite("B_action_joule_second", B_action_joule_second)
    omega = _finite("omega_rad_s", omega_rad_s)
    N = _finite("occupation", occupation)
    area = _finite("area_m2", area_m2)
    radius = _finite("radial_length_m", radial_length_m)
    phi = _finite("phase", phase)
    kap = _finite("kappa", kappa)

    if N < 0.0:
        raise RelationalGeneratorSourceError("occupation must be nonnegative")
    if area <= 0.0:
        raise RelationalGeneratorSourceError("area_m2 must be positive")
    if radius <= 0.0:
        raise RelationalGeneratorSourceError("radial_length_m must be positive")

    phase_factor = phi + kap
    volume = area * radius
    number_density = N / volume
    carrier_energy = B * omega * phase_factor
    energy_density = number_density * carrier_energy
    mass_density = energy_density / (C_LIGHT * C_LIGHT)

    return RelationalGeneratorSource(
        B_action_joule_second=B,
        omega_rad_s=omega,
        occupation=N,
        area_m2=area,
        radial_length_m=radius,
        phase=phi,
        kappa=kap,
        phase_factor=phase_factor,
        volume_m3=volume,
        occupation_density_m3=number_density,
        carrier_energy_joule=carrier_energy,
        energy_density_j_m3=energy_density,
        mass_density_kg_m3=mass_density,
        positive_source_admitted=energy_density >= 0.0,
    )


def einstein_kappa_from_newton_G(G_m3_kg_s2: float) -> float:
    G = _finite("G_m3_kg_s2", G_m3_kg_s2)
    if G <= 0.0:
        raise RelationalGeneratorSourceError("G_m3_kg_s2 must be positive")
    return 8.0 * math.pi * G / (C_LIGHT**4)


def newton_lapse_source_from_energy_density(
    energy_density_j_m3: float,
    G_m3_kg_s2: float,
) -> float:
    """Return S_R in m^-2 from the RFC weak-field normalization.

    With rho_m = rho_E/c^2 and c^2 S_R = 4 pi G rho_m,

        S_R = 4 pi G rho_E / c^4 = (kappa_E/2) rho_E.
    """

    rho_E = _finite("energy_density_j_m3", energy_density_j_m3)
    kappa_E = einstein_kappa_from_newton_G(G_m3_kg_s2)
    return 0.5 * kappa_E * rho_E


def half_rate_action_normalization(
    phase: float,
    *,
    action_quantum_joule_second: float,
    kappa: float = KAPPA_INFO,
) -> float:
    """Return B required to match the RFC half-rate carrier energy.

    RF-N1B2N gives, after restoring an independently chosen action scale q_A,

        epsilon_Q = q_A * omega_Q / 2.

    RF-S13 gives

        epsilon_Q = B * omega_Q * (phi + kappa).

    On the common-rate branch, equality requires

        B * (phi + kappa) = q_A / 2.

    This function performs only that algebraic normalization.  Choosing a
    particular physical q_A is a separate binding.
    """

    phi = _finite("phase", phase)
    kap = _finite("kappa", kappa)
    q_A = _finite("action_quantum_joule_second", action_quantum_joule_second)
    if q_A <= 0.0:
        raise RelationalGeneratorSourceError("action_quantum_joule_second must be positive")
    factor = phi + kap
    if factor == 0.0:
        raise RelationalGeneratorSourceError("phase + kappa must be nonzero")
    return q_A / (2.0 * factor)


def half_rate_normalization_defect(
    B_action_joule_second: float,
    phase: float,
    *,
    action_quantum_joule_second: float,
    kappa: float = KAPPA_INFO,
) -> float:
    B = _finite("B_action_joule_second", B_action_joule_second)
    phi = _finite("phase", phase)
    kap = _finite("kappa", kappa)
    q_A = _finite("action_quantum_joule_second", action_quantum_joule_second)
    if q_A <= 0.0:
        raise RelationalGeneratorSourceError("action_quantum_joule_second must be positive")
    lhs = B * (phi + kap)
    rhs = 0.5 * q_A
    scale = abs(lhs) + abs(rhs)
    return 0.0 if scale == 0.0 else 2.0 * abs(lhs - rhs) / scale
