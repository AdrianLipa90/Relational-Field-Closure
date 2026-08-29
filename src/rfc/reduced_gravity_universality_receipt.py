from __future__ import annotations

import math
from dataclasses import dataclass
from collections.abc import Sequence


class ReducedGravityReceiptError(ValueError):
    pass


def _finite(name: str, value: float) -> float:
    value = float(value)
    if not math.isfinite(value):
        raise ReducedGravityReceiptError(f"{name} must be finite")
    return value


def _positive(name: str, value: float) -> float:
    value = _finite(name, value)
    if value <= 0.0:
        raise ReducedGravityReceiptError(f"{name} must be positive")
    return value


def _nonempty(name: str, value: str) -> str:
    if not isinstance(value, str) or not value:
        raise ReducedGravityReceiptError(f"{name} must be a nonempty string")
    return value


def symmetric_defect(left: float, right: float) -> float:
    a = _finite("left", left)
    b = _finite("right", right)
    denom = abs(a) + abs(b)
    if denom == 0.0:
        return 0.0
    return 2.0 * abs(a - b) / denom


@dataclass(frozen=True)
class CouplingProvenance:
    current_measure_receipt_id: str
    phase_rate_receipt_id: str
    source_operator_receipt_id: str
    gauge_normalization_receipt_id: str
    double_copy_receipt_id: str
    carrier_scale_receipt_id: str
    horizon_provenance_id: str | None = None

    def __post_init__(self) -> None:
        for name, value in (
            ("current_measure_receipt_id", self.current_measure_receipt_id),
            ("phase_rate_receipt_id", self.phase_rate_receipt_id),
            ("source_operator_receipt_id", self.source_operator_receipt_id),
            ("gauge_normalization_receipt_id", self.gauge_normalization_receipt_id),
            ("double_copy_receipt_id", self.double_copy_receipt_id),
            ("carrier_scale_receipt_id", self.carrier_scale_receipt_id),
        ):
            _nonempty(name, value)
        if self.horizon_provenance_id is not None:
            _nonempty("horizon_provenance_id", self.horizon_provenance_id)


@dataclass(frozen=True)
class CouplingSystem:
    system_id: str
    gravity_sector_id: str
    beta_w: float
    gamma_dc: float
    g_ym_squared: float
    m_star: float
    omega_q: float
    current_j_q: float
    source_s_r: float
    provenance: CouplingProvenance
    horizon_mass: float | None = None
    horizon_kappa: float | None = None
    horizon_temperature: float | None = None

    def __post_init__(self) -> None:
        _nonempty("system_id", self.system_id)
        _nonempty("gravity_sector_id", self.gravity_sector_id)
        for name, value in (
            ("beta_w", self.beta_w),
            ("gamma_dc", self.gamma_dc),
            ("g_ym_squared", self.g_ym_squared),
            ("m_star", self.m_star),
            ("omega_q", self.omega_q),
            ("current_j_q", self.current_j_q),
            ("source_s_r", self.source_s_r),
        ):
            _positive(name, value)
        horizon_values = (self.horizon_mass, self.horizon_kappa, self.horizon_temperature)
        if any(value is not None for value in horizon_values):
            if self.horizon_mass is None:
                raise ReducedGravityReceiptError("horizon_mass is required when a horizon estimator is supplied")
            _positive("horizon_mass", self.horizon_mass)
            if self.horizon_kappa is not None:
                _positive("horizon_kappa", self.horizon_kappa)
            if self.horizon_temperature is not None:
                _positive("horizon_temperature", self.horizon_temperature)
            if self.horizon_kappa is None and self.horizon_temperature is None:
                raise ReducedGravityReceiptError("horizon_kappa or horizon_temperature is required with horizon_mass")
            if self.provenance.horizon_provenance_id is None:
                raise ReducedGravityReceiptError("horizon_provenance_id is required for a horizon estimator")


def _system_receipt(system: CouplingSystem) -> dict[str, object]:
    beta = _positive("beta_w", system.beta_w)
    gamma = _positive("gamma_dc", system.gamma_dc)
    g2 = _positive("g_ym_squared", system.g_ym_squared)
    m_star = _positive("m_star", system.m_star)
    omega = _positive("omega_q", system.omega_q)
    j_q = _positive("current_j_q", system.current_j_q)
    source = _positive("source_s_r", system.source_s_r)

    g2_wilson = 6.0 / beta
    mbar_dc = m_star / (gamma * g2)
    mbar_wilson = beta * m_star / (6.0 * gamma)
    epsilon_q_local = omega / 2.0
    mbar_local = beta * omega / (12.0 * gamma)
    g_dc = 1.0 / (8.0 * math.pi * mbar_dc * mbar_dc)

    source_pred_general = (gamma * gamma * g2 * g2 / (4.0 * m_star * m_star)) * omega * j_q
    source_pred_local = 36.0 * gamma * gamma * j_q / (beta * beta * omega)

    defects: dict[str, float] = {
        "wilson_gauge_normalization": symmetric_defect(g2, g2_wilson),
        "dc_wilson_reduced_scale": symmetric_defect(mbar_dc, mbar_wilson),
        "carrier_scale_local": symmetric_defect(m_star, epsilon_q_local),
        "dc_local_reduced_scale": symmetric_defect(mbar_dc, mbar_local),
        "source_general": symmetric_defect(source, source_pred_general),
        "source_local": symmetric_defect(source, source_pred_local),
    }

    horizon: dict[str, float | None] | None = None
    if system.horizon_mass is not None:
        m_h = _positive("horizon_mass", system.horizon_mass)
        mbar_h: float | None = None
        mbar_t: float | None = None
        if system.horizon_kappa is not None:
            kappa_h = _positive("horizon_kappa", system.horizon_kappa)
            mbar_h = math.sqrt(m_h * kappa_h / (2.0 * math.pi))
            defects["dc_horizon_reduced_scale"] = symmetric_defect(mbar_dc, mbar_h)
        if system.horizon_temperature is not None:
            t_h = _positive("horizon_temperature", system.horizon_temperature)
            mbar_t = math.sqrt(m_h * t_h)
            defects["dc_thermal_reduced_scale"] = symmetric_defect(mbar_dc, mbar_t)
        if system.horizon_kappa is not None and system.horizon_temperature is not None:
            defects["horizon_thermal_conversion"] = symmetric_defect(
                system.horizon_kappa,
                2.0 * math.pi * system.horizon_temperature,
            )
        horizon = {
            "mbar_h": mbar_h,
            "mbar_t": mbar_t,
        }
        if system.provenance.horizon_provenance_id == system.provenance.double_copy_receipt_id:
            defects["horizon_provenance_independence"] = 1.0
        else:
            defects["horizon_provenance_independence"] = 0.0

    return {
        "system_id": system.system_id,
        "gravity_sector_id": system.gravity_sector_id,
        "g_ym_squared_wilson": g2_wilson,
        "epsilon_q_local": epsilon_q_local,
        "mbar_dc": mbar_dc,
        "mbar_wilson": mbar_wilson,
        "mbar_local": mbar_local,
        "g_dc_natural_units": g_dc,
        "source_pred_general": source_pred_general,
        "source_pred_local": source_pred_local,
        "horizon": horizon,
        "defects": defects,
        "max_local_defect": max(defects.values()),
    }


def build_reduced_gravity_universality_receipt(
    systems: Sequence[CouplingSystem],
    *,
    require_horizon: bool = False,
) -> dict[str, object]:
    if len(systems) < 2:
        raise ReducedGravityReceiptError("cross-system universality requires at least two systems")
    system_ids = [system.system_id for system in systems]
    if len(set(system_ids)) != len(system_ids):
        raise ReducedGravityReceiptError("system_id values must be unique")
    sectors = {system.gravity_sector_id for system in systems}
    if len(sectors) != 1:
        raise ReducedGravityReceiptError("all systems must belong to the same gravity_sector_id")
    if require_horizon and any(system.horizon_mass is None for system in systems):
        raise ReducedGravityReceiptError("require_horizon=True requires a horizon estimator for every system")

    local = tuple(_system_receipt(system) for system in systems)
    pairwise: list[dict[str, object]] = []
    universality_defects: list[float] = []
    local_candidate_defects: list[float] = []
    g_defects: list[float] = []
    for i in range(len(local)):
        for j in range(i + 1, len(local)):
            mbar_defect = symmetric_defect(local[i]["mbar_dc"], local[j]["mbar_dc"])
            local_defect = symmetric_defect(local[i]["mbar_local"], local[j]["mbar_local"])
            g_defect = symmetric_defect(local[i]["g_dc_natural_units"], local[j]["g_dc_natural_units"])
            pairwise.append(
                {
                    "left": local[i]["system_id"],
                    "right": local[j]["system_id"],
                    "mbar_dc": mbar_defect,
                    "mbar_local": local_defect,
                    "g_dc": g_defect,
                }
            )
            universality_defects.append(mbar_defect)
            local_candidate_defects.append(local_defect)
            g_defects.append(g_defect)

    all_defects = [item["max_local_defect"] for item in local]
    all_defects.extend(universality_defects)
    all_defects.extend(local_candidate_defects)
    all_defects.extend(g_defects)

    return {
        "units": "natural",
        "gravity_sector_id": next(iter(sectors)),
        "systems": local,
        "pairwise": tuple(pairwise),
        "max_mbar_universality_defect": max(universality_defects),
        "max_local_candidate_universality_defect": max(local_candidate_defects),
        "max_g_universality_defect": max(g_defects),
        "max_defect": max(all_defects),
    }


def receipt_passes(receipt: dict[str, object], *, atol: float = 0.0) -> bool:
    tol = _finite("atol", atol)
    if tol < 0.0:
        raise ReducedGravityReceiptError("atol must be nonnegative")
    if "max_defect" not in receipt:
        raise ReducedGravityReceiptError("receipt must contain max_defect")
    return abs(_finite("max_defect", receipt["max_defect"])) <= tol
