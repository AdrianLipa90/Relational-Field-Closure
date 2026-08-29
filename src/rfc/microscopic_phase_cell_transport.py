from __future__ import annotations

import math
from dataclasses import dataclass

from src.rfc.foundational_phase_source_formalism import C_LIGHT, FULL_TETRA_FS_AREA


class MicroscopicPhaseCellTransportError(ValueError):
    pass


@dataclass(frozen=True)
class CurrentCellBinding:
    occupation: float
    carrier_action_quantum: float
    phase_rate: float
    phase_cell_volume: float
    occupation_density: float
    action_charge_density: float
    amplitude_squared: float


@dataclass(frozen=True)
class TransportCompatibility:
    spatial_ratio: float
    potential_ratio: float
    energy_factor: float
    microscopic_w: float
    d_spatial_ratio_dlnomega: float
    d_potential_ratio_dlnomega: float
    supplied_energy_factor_derivative: float
    required_energy_factor_derivative: float
    differential_residual: float


@dataclass(frozen=True)
class RadiationBranch:
    spatial_ratio: float
    potential_ratio: float
    energy_factor: float
    generator_prefactor_ratio: float
    microscopic_w: float
    density_scaling_power_omega: float


@dataclass(frozen=True)
class FixedSpatialRatioSolution:
    spatial_ratio: float
    phase_rate: float
    integration_constant_rate4: float
    potential_ratio: float
    energy_factor: float
    generator_prefactor_ratio: float
    radiation_density: float
    vacuum_density: float
    total_density: float
    total_pressure: float
    eos: float
    differential_residual: float


@dataclass(frozen=True)
class DustTransportSolution:
    phase_rate: float
    dust_rate_constant: float
    spatial_ratio: float
    potential_ratio: float
    energy_factor: float
    generator_prefactor_ratio: float
    energy_per_action_charge_rate: float
    density: float
    pressure: float
    density_scaling_power_omega: float
    differential_residual: float


def _finite(name: str, value: float) -> float:
    out = float(value)
    if not math.isfinite(out):
        raise MicroscopicPhaseCellTransportError(f"{name} must be finite")
    return out


def current_phase_cell_binding(
    occupation: float,
    carrier_action_quantum: float,
    phase_rate: float,
    *,
    area_fs_dimensionless: float = FULL_TETRA_FS_AREA,
    c_light: float = C_LIGHT,
) -> CurrentCellBinding:
    """RF-F14/RF-S16 current binding on the RF-F3 phase cell.

    With positive omega,

        V_R = a_FS c^3 / omega^3,
        n = N/V_R,
        j_Q = q0*n,
        j_theta = 2 A^2 omega.

    Exact current binding j_Q=j_theta therefore fixes

        A^2 = q0*N*omega^2/(2 a_FS c^3).
    """

    N = _finite("occupation", occupation)
    q0 = _finite("carrier_action_quantum", carrier_action_quantum)
    omega = _finite("phase_rate", phase_rate)
    a_fs = _finite("area_fs_dimensionless", area_fs_dimensionless)
    c = _finite("c_light", c_light)
    if N < 0.0:
        raise MicroscopicPhaseCellTransportError("occupation must be nonnegative")
    if q0 <= 0.0:
        raise MicroscopicPhaseCellTransportError("carrier_action_quantum must be positive")
    if omega <= 0.0:
        raise MicroscopicPhaseCellTransportError("phase_rate must be positive on this oriented branch")
    if a_fs <= 0.0 or c <= 0.0:
        raise MicroscopicPhaseCellTransportError("phase-cell geometry coefficients must be positive")
    volume = a_fs * c**3 / omega**3
    n = N / volume
    j = q0 * n
    A2 = j / (2.0 * omega)
    return CurrentCellBinding(
        occupation=N,
        carrier_action_quantum=q0,
        phase_rate=omega,
        phase_cell_volume=volume,
        occupation_density=n,
        action_charge_density=j,
        amplitude_squared=A2,
    )


def transport_compatibility(
    spatial_ratio: float,
    potential_ratio: float,
    d_spatial_ratio_dlnomega: float,
    d_potential_ratio_dlnomega: float,
) -> TransportCompatibility:
    """Microscopic-stress <-> RF-F8 phase-cell transport equation.

    Let

        x = k^2/omega^2,
        v = V/(A^2 omega^2),
        D = 1+x+v.

    Current/phase-cell binding gives A^2 proportional to omega^2, while the
    complete scalar energy/action-charge ratio gives P/q0=D/2.  Equating the
    RF-E7 microscopic EOS to the RF-F8 separately-conserved phase-cell EOS
    yields exactly

        dD/dln|omega| = 2(1-x-2v).
    """

    x = _finite("spatial_ratio", spatial_ratio)
    v = _finite("potential_ratio", potential_ratio)
    dx = _finite("d_spatial_ratio_dlnomega", d_spatial_ratio_dlnomega)
    dv = _finite("d_potential_ratio_dlnomega", d_potential_ratio_dlnomega)
    if x < 0.0 or v < 0.0:
        raise MicroscopicPhaseCellTransportError("spatial_ratio and potential_ratio must be nonnegative")
    D = 1.0 + x + v
    w = (1.0 - x / 3.0 - v) / D
    supplied = dx + dv
    required = 2.0 * (1.0 - x - 2.0 * v)
    return TransportCompatibility(
        spatial_ratio=x,
        potential_ratio=v,
        energy_factor=D,
        microscopic_w=w,
        d_spatial_ratio_dlnomega=dx,
        d_potential_ratio_dlnomega=dv,
        supplied_energy_factor_derivative=supplied,
        required_energy_factor_derivative=required,
        differential_residual=supplied - required,
    )


def radiation_fixed_point(spatial_ratio: float) -> RadiationBranch:
    """Constant-composition solution of the transport equation.

    For dx=dv=0, compatibility fixes x+2v=1.  With V>=0 this branch has
    0<=x<=1, v=(1-x)/2, w=1/3 and constant P/q0=(3+x)/4.
    """

    x = _finite("spatial_ratio", spatial_ratio)
    if x < 0.0 or x > 1.0:
        raise MicroscopicPhaseCellTransportError("radiation fixed-point spatial_ratio must lie in [0,1]")
    v = 0.5 * (1.0 - x)
    D = 1.0 + x + v
    return RadiationBranch(
        spatial_ratio=x,
        potential_ratio=v,
        energy_factor=D,
        generator_prefactor_ratio=0.5 * D,
        microscopic_w=1.0 / 3.0,
        density_scaling_power_omega=4.0,
    )


def fixed_spatial_ratio_solution(
    spatial_ratio: float,
    phase_rate: float,
    integration_constant_rate4: float,
    kinetic_density_coefficient: float,
) -> FixedSpatialRatioSolution:
    """Exact fixed-x transport solution: radiation plus vacuum.

    For constant x the compatibility ODE is

        dv/dln omega + 4v = 2(1-x),

    so

        v=(1-x)/2 + C/omega^4.

    Current binding makes K=A^2 omega^2=K0*omega^4.  The total stress then
    decomposes exactly as

        rho = rho_r + rho_L,
        p   = rho_r/3 - rho_L,

    with rho_L=K0*C constant.
    """

    x = _finite("spatial_ratio", spatial_ratio)
    omega = _finite("phase_rate", phase_rate)
    C = _finite("integration_constant_rate4", integration_constant_rate4)
    K0 = _finite("kinetic_density_coefficient", kinetic_density_coefficient)
    if x < 0.0:
        raise MicroscopicPhaseCellTransportError("spatial_ratio must be nonnegative")
    if omega <= 0.0 or C < 0.0 or K0 <= 0.0:
        raise MicroscopicPhaseCellTransportError("phase_rate and kinetic coefficient must be positive; integration constant nonnegative")
    v = 0.5 * (1.0 - x) + C / omega**4
    if v < 0.0:
        raise MicroscopicPhaseCellTransportError("solution leaves the nonnegative-potential surface")
    D = 1.0 + x + v
    rho_r = K0 * omega**4 * (3.0 + x) / 2.0
    rho_v = K0 * C
    rho = rho_r + rho_v
    pressure = rho_r / 3.0 - rho_v
    w = pressure / rho
    dv_dln = -4.0 * C / omega**4
    compat = transport_compatibility(x, v, 0.0, dv_dln)
    return FixedSpatialRatioSolution(
        spatial_ratio=x,
        phase_rate=omega,
        integration_constant_rate4=C,
        potential_ratio=v,
        energy_factor=D,
        generator_prefactor_ratio=0.5 * D,
        radiation_density=rho_r,
        vacuum_density=rho_v,
        total_density=rho,
        total_pressure=pressure,
        eos=w,
        differential_residual=compat.differential_residual,
    )


def dust_transport_solution(
    phase_rate: float,
    dust_rate_constant: float,
    kinetic_density_coefficient: float,
) -> DustTransportSolution:
    """Exact p=0 transport trajectory compatible with RF-F8 dust scaling.

    The microscopic dust surface is v=1-x/3.  Transport compatibility then
    gives

        dx/dln omega = -(x+3),
        x+3 = C_d/omega.

    Hence

        v = 2-C_d/(3 omega),
        D = 2 C_d/(3 omega),
        P/q0 = C_d/(3 omega),
        epsilon = (P/q0) omega = C_d/3 = const,
        rho proportional to omega^3.

    Nonnegative x and v select 3 omega <= C_d <= 6 omega locally.
    """

    omega = _finite("phase_rate", phase_rate)
    Cd = _finite("dust_rate_constant", dust_rate_constant)
    K0 = _finite("kinetic_density_coefficient", kinetic_density_coefficient)
    if omega <= 0.0 or Cd <= 0.0 or K0 <= 0.0:
        raise MicroscopicPhaseCellTransportError("phase_rate, dust_rate_constant and kinetic coefficient must be positive")
    x = Cd / omega - 3.0
    v = 2.0 - Cd / (3.0 * omega)
    if x < 0.0 or v < 0.0:
        raise MicroscopicPhaseCellTransportError("dust solution requires nonnegative x and v")
    D = 1.0 + x + v
    ratio = 0.5 * D
    eps = ratio * omega
    K = K0 * omega**4
    rho = K * D
    pressure = K * (1.0 - x / 3.0 - v)
    dx_dln = -Cd / omega
    dv_dln = Cd / (3.0 * omega)
    compat = transport_compatibility(x, v, dx_dln, dv_dln)
    return DustTransportSolution(
        phase_rate=omega,
        dust_rate_constant=Cd,
        spatial_ratio=x,
        potential_ratio=v,
        energy_factor=D,
        generator_prefactor_ratio=ratio,
        energy_per_action_charge_rate=eps,
        density=rho,
        pressure=pressure,
        density_scaling_power_omega=3.0,
        differential_residual=compat.differential_residual,
    )
