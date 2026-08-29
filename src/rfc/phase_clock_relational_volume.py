from __future__ import annotations

import math
from dataclasses import dataclass

from src.rfc.relational_generator_source_density import (
    C_LIGHT,
    KAPPA_INFO,
    relational_generator_source,
)


class PhaseClockRelationalVolumeError(ValueError):
    pass


FULL_TETRA_CP1 = "FULL_TETRA_CP1"
FACE = "FACE"


@dataclass(frozen=True)
class PhaseClockRelationalVolume:
    omega_rad_s: float
    scope: str
    phase_clock_length_m: float
    projective_area_m2: float
    relational_volume_m3: float
    area_fs_dimensionless: float


@dataclass(frozen=True)
class ReducedGeneratorDensity:
    geometry: PhaseClockRelationalVolume
    B_action_joule_second: float
    occupation: float
    phase: float
    kappa: float
    energy_density_j_m3: float
    closed_form_j_m3: float


def _finite(name: str, value: float) -> float:
    value = float(value)
    if not math.isfinite(value):
        raise PhaseClockRelationalVolumeError(f"{name} must be finite")
    return value


def _scope_area(scope: str) -> float:
    if scope == FULL_TETRA_CP1:
        return math.pi
    if scope == FACE:
        return math.pi / 4.0
    raise PhaseClockRelationalVolumeError("scope must be FULL_TETRA_CP1 or FACE")


def phase_clock_relational_volume(
    omega_rad_s: float,
    *,
    scope: str = FULL_TETRA_CP1,
) -> PhaseClockRelationalVolume:
    """Compose RF-S10 projective area with the RFC phase-clock length.

    RF-S10 gives A_rel=(c^2/omega^2) a_FS.
    RF-02H/README gives ell_phi=c/|omega|.
    RF-S15 identifies R=ell_phi on the common phase-clock carrier and returns

        V_R = A_rel R = a_FS c^3 / |omega|^3.
    """

    omega = _finite("omega_rad_s", omega_rad_s)
    if omega == 0.0:
        raise PhaseClockRelationalVolumeError("omega_rad_s must be nonzero")
    a_fs = _scope_area(scope)
    rate = abs(omega)
    length = C_LIGHT / rate
    area = (C_LIGHT * C_LIGHT / (rate * rate)) * a_fs
    volume = area * length
    return PhaseClockRelationalVolume(
        omega_rad_s=omega,
        scope=scope,
        phase_clock_length_m=length,
        projective_area_m2=area,
        relational_volume_m3=volume,
        area_fs_dimensionless=a_fs,
    )


def reduced_generator_density(
    B_action_joule_second: float,
    omega_rad_s: float,
    occupation: float,
    phase: float,
    *,
    scope: str = FULL_TETRA_CP1,
    kappa: float = KAPPA_INFO,
) -> ReducedGeneratorDensity:
    """Evaluate the RF-S13 generator after RF-S15 closes A*R geometrically."""

    B = _finite("B_action_joule_second", B_action_joule_second)
    omega = _finite("omega_rad_s", omega_rad_s)
    N = _finite("occupation", occupation)
    phi = _finite("phase", phase)
    kap = _finite("kappa", kappa)
    if N < 0.0:
        raise PhaseClockRelationalVolumeError("occupation must be nonnegative")

    geometry = phase_clock_relational_volume(omega, scope=scope)
    source = relational_generator_source(
        B,
        omega,
        N,
        geometry.projective_area_m2,
        geometry.phase_clock_length_m,
        phi,
        kappa=kap,
    )

    # V_R=a_FS*c^3/|omega|^3, so the signed generator reduces to
    # B*N*omega*|omega|^3*(phi+kappa)/(a_FS*c^3).
    closed = (
        B
        * N
        * omega
        * abs(omega) ** 3
        * (phi + kap)
        / (geometry.area_fs_dimensionless * C_LIGHT**3)
    )
    return ReducedGeneratorDensity(
        geometry=geometry,
        B_action_joule_second=B,
        occupation=N,
        phase=phi,
        kappa=kap,
        energy_density_j_m3=source.energy_density_j_m3,
        closed_form_j_m3=closed,
    )


def normalized_density_from_action_scale(
    omega_rad_s: float,
    occupation: float,
    action_scale_joule_second: float,
    *,
    carrier_fraction: float,
    scope: str = FULL_TETRA_CP1,
) -> float:
    """Return rho_E after fixing epsilon=carrier_fraction*q_A*omega.

    carrier_fraction=1/2 reproduces the RF-N1B2N/RF-E5 kinetic carrier.
    carrier_fraction=1 reproduces the RF-04/RF-E5 total on-shell carrier.
    """

    omega = _finite("omega_rad_s", omega_rad_s)
    N = _finite("occupation", occupation)
    q_A = _finite("action_scale_joule_second", action_scale_joule_second)
    fraction = _finite("carrier_fraction", carrier_fraction)
    if omega == 0.0:
        raise PhaseClockRelationalVolumeError("omega_rad_s must be nonzero")
    if N < 0.0:
        raise PhaseClockRelationalVolumeError("occupation must be nonnegative")
    if q_A <= 0.0:
        raise PhaseClockRelationalVolumeError("action_scale_joule_second must be positive")
    if fraction < 0.0:
        raise PhaseClockRelationalVolumeError("carrier_fraction must be nonnegative")

    geometry = phase_clock_relational_volume(omega, scope=scope)
    energy_per_carrier = fraction * q_A * omega
    number_density = N / geometry.relational_volume_m3
    return number_density * energy_per_carrier
