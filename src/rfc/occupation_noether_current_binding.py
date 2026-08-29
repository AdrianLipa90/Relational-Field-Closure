from __future__ import annotations

import math
from dataclasses import dataclass
from collections.abc import Sequence

from src.rfc.relational_generator_source_density import KAPPA_INFO


class OccupationNoetherBindingError(ValueError):
    pass


@dataclass(frozen=True)
class OccupationCurrentLedger:
    occupations: tuple[float, ...]
    cell_volumes: tuple[float, ...]
    carrier_quantum: float
    predicted_current_densities: tuple[float, ...]
    total_occupation: float
    total_charge: float
    occupation_profile: tuple[float, ...]
    charge_profile: tuple[float, ...]


@dataclass(frozen=True)
class OccupationCurrentBindingDiagnostic:
    predicted: OccupationCurrentLedger
    observed_current_densities: tuple[float, ...]
    observed_total_charge: float
    local_current_defect: float
    total_charge_defect: float
    bound_margin: float
    observed_profile: tuple[float, ...] | None


def _finite(name: str, value: float) -> float:
    value = float(value)
    if not math.isfinite(value):
        raise OccupationNoetherBindingError(f"{name} must be finite")
    return value


def _positive_sequence(name: str, values: Sequence[float]) -> tuple[float, ...]:
    if len(values) < 1:
        raise OccupationNoetherBindingError(f"{name} must be nonempty")
    out = tuple(_finite(f"{name}[{i}]", v) for i, v in enumerate(values))
    if any(v <= 0.0 for v in out):
        raise OccupationNoetherBindingError(f"{name} entries must be positive")
    return out


def _nonnegative_sequence(name: str, values: Sequence[float]) -> tuple[float, ...]:
    if len(values) < 1:
        raise OccupationNoetherBindingError(f"{name} must be nonempty")
    out = tuple(_finite(f"{name}[{i}]", v) for i, v in enumerate(values))
    if any(v < 0.0 for v in out):
        raise OccupationNoetherBindingError(f"{name} entries must be nonnegative")
    return out


def occupation_current_ledger(
    occupations: Sequence[float],
    cell_volumes: Sequence[float],
    *,
    carrier_quantum: float = 1.0,
) -> OccupationCurrentLedger:
    """Map finite-cell occupation into a conserved-current density coordinate.

    For each cell C_a with volume V_a and occupation N_a,

        j_Q,a = q_0 N_a / V_a.

    Therefore the extensive charge is

        Q_Sigma = sum_a V_a j_Q,a = q_0 sum_a N_a.

    On the positive-total sector the normalized charge profile is exactly the
    normalized occupation profile, independent of the cell volumes.
    """

    occ = _nonnegative_sequence("occupations", occupations)
    vol = _positive_sequence("cell_volumes", cell_volumes)
    if len(occ) != len(vol):
        raise OccupationNoetherBindingError("occupations and cell_volumes must have equal length")
    q0 = _finite("carrier_quantum", carrier_quantum)
    if q0 <= 0.0:
        raise OccupationNoetherBindingError("carrier_quantum must be positive")

    total_occupation = math.fsum(occ)
    if total_occupation <= 0.0:
        raise OccupationNoetherBindingError("total occupation must be positive")

    currents = tuple(q0 * n / v for n, v in zip(occ, vol, strict=True))
    total_charge = q0 * total_occupation
    occupation_profile = tuple(n / total_occupation for n in occ)
    charge_profile = tuple(v * j / total_charge for v, j in zip(vol, currents, strict=True))

    return OccupationCurrentLedger(
        occupations=occ,
        cell_volumes=vol,
        carrier_quantum=q0,
        predicted_current_densities=currents,
        total_occupation=total_occupation,
        total_charge=total_charge,
        occupation_profile=occupation_profile,
        charge_profile=charge_profile,
    )


def occupations_from_current(
    current_densities: Sequence[float],
    cell_volumes: Sequence[float],
    *,
    carrier_quantum: float = 1.0,
) -> tuple[float, ...]:
    current = _nonnegative_sequence("current_densities", current_densities)
    vol = _positive_sequence("cell_volumes", cell_volumes)
    if len(current) != len(vol):
        raise OccupationNoetherBindingError("current_densities and cell_volumes must have equal length")
    q0 = _finite("carrier_quantum", carrier_quantum)
    if q0 <= 0.0:
        raise OccupationNoetherBindingError("carrier_quantum must be positive")
    return tuple(v * j / q0 for v, j in zip(vol, current, strict=True))


def occupation_current_binding_diagnostic(
    occupations: Sequence[float],
    cell_volumes: Sequence[float],
    observed_current_densities: Sequence[float],
    *,
    carrier_quantum: float = 1.0,
) -> OccupationCurrentBindingDiagnostic:
    """Compare independently supplied Noether/RFC current data to occupation.

    With a common cell measure,

        Delta_Sigma <= Delta_J,

    where Delta_J is the volume-weighted local-current mismatch normalized by
    the predicted positive total charge.  The returned ``bound_margin`` is
    max(0, Delta_Sigma-Delta_J), which must vanish up to arithmetic precision.
    """

    predicted = occupation_current_ledger(
        occupations,
        cell_volumes,
        carrier_quantum=carrier_quantum,
    )
    observed = _nonnegative_sequence("observed_current_densities", observed_current_densities)
    if len(observed) != len(predicted.cell_volumes):
        raise OccupationNoetherBindingError("observed currents must match the occupation cell count")

    q_pred = predicted.total_charge
    q_obs = math.fsum(
        v * j for v, j in zip(predicted.cell_volumes, observed, strict=True)
    )
    local = math.fsum(
        v * abs(j_obs - j_pred)
        for v, j_obs, j_pred in zip(
            predicted.cell_volumes,
            observed,
            predicted.predicted_current_densities,
            strict=True,
        )
    ) / q_pred
    total = abs(q_obs - q_pred) / q_pred
    bound_margin = max(0.0, total - local)

    observed_profile: tuple[float, ...] | None
    if q_obs > 0.0:
        observed_profile = tuple(
            v * j / q_obs for v, j in zip(predicted.cell_volumes, observed, strict=True)
        )
    else:
        observed_profile = None

    return OccupationCurrentBindingDiagnostic(
        predicted=predicted,
        observed_current_densities=observed,
        observed_total_charge=q_obs,
        local_current_defect=local,
        total_charge_defect=total,
        bound_margin=bound_margin,
        observed_profile=observed_profile,
    )


def carrier_energy_per_charge(
    B_action_joule_second: float,
    omega_rad_s: float,
    phase: float,
    *,
    carrier_quantum: float = 1.0,
    kappa: float = KAPPA_INFO,
) -> float:
    B = _finite("B_action_joule_second", B_action_joule_second)
    omega = _finite("omega_rad_s", omega_rad_s)
    phi = _finite("phase", phase)
    kap = _finite("kappa", kappa)
    q0 = _finite("carrier_quantum", carrier_quantum)
    if q0 <= 0.0:
        raise OccupationNoetherBindingError("carrier_quantum must be positive")
    return B * omega * (phi + kap) / q0


def generator_density_from_current(
    B_action_joule_second: float,
    omega_rad_s: float,
    current_density: float,
    phase: float,
    *,
    carrier_quantum: float = 1.0,
    kappa: float = KAPPA_INFO,
) -> float:
    """Rewrite the RF-S13 generator directly in conserved-current form.

    Since j_Q=q_0 N/(A R),

        rho_G = [B omega/q_0] (phi+kappa) j_Q.
    """

    j_q = _finite("current_density", current_density)
    if j_q < 0.0:
        raise OccupationNoetherBindingError("current_density must be nonnegative")
    epsilon_q = carrier_energy_per_charge(
        B_action_joule_second,
        omega_rad_s,
        phase,
        carrier_quantum=carrier_quantum,
        kappa=kappa,
    )
    return epsilon_q * j_q
