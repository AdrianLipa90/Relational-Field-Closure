from __future__ import annotations

import math
from dataclasses import dataclass
from collections.abc import Sequence


class CurrentMeasureReceiptError(ValueError):
    pass


def _finite(name: str, value: float) -> float:
    value = float(value)
    if not math.isfinite(value):
        raise CurrentMeasureReceiptError(f"{name} must be finite")
    return value


def _positive(name: str, value: float) -> float:
    value = _finite(name, value)
    if value <= 0.0:
        raise CurrentMeasureReceiptError(f"{name} must be positive")
    return value


def _vector(name: str, values: Sequence[float], *, nonnegative: bool = False) -> tuple[float, ...]:
    if len(values) == 0:
        raise CurrentMeasureReceiptError(f"{name} must be nonempty")
    parsed = tuple(_finite(f"{name}[{i}]", value) for i, value in enumerate(values))
    if nonnegative and any(value < 0.0 for value in parsed):
        raise CurrentMeasureReceiptError(f"{name} must be nonnegative on the positive-current sector")
    return parsed


@dataclass(frozen=True)
class CurrentMeasureLineage:
    slice_id: str
    normal_orientation_id: str
    semantic_measure_id: str
    cell_ids: tuple[str, ...]

    def __post_init__(self) -> None:
        for name, value in (
            ("slice_id", self.slice_id),
            ("normal_orientation_id", self.normal_orientation_id),
            ("semantic_measure_id", self.semantic_measure_id),
        ):
            if not isinstance(value, str) or not value:
                raise CurrentMeasureReceiptError(f"{name} must be a nonempty string")
        if not self.cell_ids or any(not isinstance(cell_id, str) or not cell_id for cell_id in self.cell_ids):
            raise CurrentMeasureReceiptError("cell_ids must be a nonempty ordered tuple of nonempty strings")
        if len(set(self.cell_ids)) != len(self.cell_ids):
            raise CurrentMeasureReceiptError("cell_ids must be unique")


def lineage_defects(noether: CurrentMeasureLineage, rfc: CurrentMeasureLineage) -> dict[str, float]:
    return {
        "slice": 0.0 if noether.slice_id == rfc.slice_id else 1.0,
        "normal_orientation": 0.0 if noether.normal_orientation_id == rfc.normal_orientation_id else 1.0,
        "semantic_measure": 0.0 if noether.semantic_measure_id == rfc.semantic_measure_id else 1.0,
        "ordered_cells": 0.0 if noether.cell_ids == rfc.cell_ids else 1.0,
    }


def extensive_charge(current: Sequence[float], volumes: Sequence[float]) -> float:
    j = _vector("current", current)
    V = _vector("volumes", volumes)
    if len(j) != len(V):
        raise CurrentMeasureReceiptError("current and volumes must have equal length")
    if any(value <= 0.0 for value in V):
        raise CurrentMeasureReceiptError("all cell volumes must be positive")
    return sum(V[i] * j[i] for i in range(len(j)))


def occupation_predicted_current(
    occupations: Sequence[float],
    volumes: Sequence[float],
    carrier_quantum: float,
) -> tuple[float, ...]:
    occupation = _vector("occupations", occupations, nonnegative=True)
    V = _vector("volumes", volumes)
    if len(occupation) != len(V):
        raise CurrentMeasureReceiptError("occupations and volumes must have equal length")
    if any(value <= 0.0 for value in V):
        raise CurrentMeasureReceiptError("all cell volumes must be positive")
    q0 = _positive("carrier_quantum", carrier_quantum)
    return tuple(q0 * occupation[i] / V[i] for i in range(len(V)))


def build_current_measure_receipt(
    *,
    noether_current: Sequence[float],
    noether_volumes: Sequence[float],
    rfc_current: Sequence[float],
    rfc_volumes: Sequence[float],
    noether_lineage: CurrentMeasureLineage,
    rfc_lineage: CurrentMeasureLineage,
    side_flux: float,
    occupations: Sequence[float] | None = None,
    carrier_quantum: float | None = None,
) -> dict[str, object]:
    """Independent RF-N1B2K current/measure realization audit.

    The Noether and RFC current/measure arrays are always independent inputs.
    Optional RF-S16 occupation data add a third independent source coordinate.
    """
    j_theta = _vector("noether_current", noether_current, nonnegative=True)
    V_theta = _vector("noether_volumes", noether_volumes)
    j_q = _vector("rfc_current", rfc_current, nonnegative=True)
    V_q = _vector("rfc_volumes", rfc_volumes)
    n = len(j_theta)
    if not (len(V_theta) == len(j_q) == len(V_q) == n):
        raise CurrentMeasureReceiptError("all current/measure arrays must have equal nonzero length")
    if any(value <= 0.0 for value in V_theta) or any(value <= 0.0 for value in V_q):
        raise CurrentMeasureReceiptError("all cell volumes must be positive")
    if len(noether_lineage.cell_ids) != n or len(rfc_lineage.cell_ids) != n:
        raise CurrentMeasureReceiptError("lineage cell_ids length must match current arrays")

    Q_theta = sum(V_theta[i] * j_theta[i] for i in range(n))
    Q_sigma = sum(V_q[i] * j_q[i] for i in range(n))
    if Q_theta <= 0.0 or Q_sigma <= 0.0:
        raise CurrentMeasureReceiptError("Noether and RFC extensive charges must be positive")

    delta_j = sum(V_q[i] * abs(j_q[i] - j_theta[i]) for i in range(n)) / Q_theta
    delta_v = sum(abs(V_q[i] - V_theta[i]) * abs(j_theta[i]) for i in range(n)) / Q_theta
    delta_sigma = abs(Q_sigma - Q_theta) / Q_theta
    delta_bound = max(0.0, delta_sigma - (delta_j + delta_v))
    delta_f = abs(_finite("side_flux", side_flux))

    p_theta = tuple(V_theta[i] * j_theta[i] / Q_theta for i in range(n))
    p_q = tuple(V_q[i] * j_q[i] / Q_sigma for i in range(n))
    profile_l1 = sum(abs(p_q[i] - p_theta[i]) for i in range(n))

    defects: dict[str, float] = {
        "local_current": delta_j,
        "measure": delta_v,
        "extensive_charge": delta_sigma,
        "defect_bound_margin": delta_bound,
        "side_flux": delta_f,
        "profile_l1": profile_l1,
    }
    defects.update({f"lineage_{name}": value for name, value in lineage_defects(noether_lineage, rfc_lineage).items()})

    occupation_audit: dict[str, object] | None = None
    if occupations is not None or carrier_quantum is not None:
        if occupations is None or carrier_quantum is None:
            raise CurrentMeasureReceiptError("occupations and carrier_quantum must be supplied together")
        j_pred = occupation_predicted_current(occupations, V_q, carrier_quantum)
        Q_pred = extensive_charge(j_pred, V_q)
        if Q_pred <= 0.0:
            raise CurrentMeasureReceiptError("occupation-predicted extensive charge must be positive")
        delta_occ_j = sum(V_q[i] * abs(j_q[i] - j_pred[i]) for i in range(n)) / Q_pred
        delta_occ_sigma = abs(Q_sigma - Q_pred) / Q_pred
        occupation_profile = tuple(V_q[i] * j_pred[i] / Q_pred for i in range(n))
        occupation_profile_l1 = sum(abs(p_q[i] - occupation_profile[i]) for i in range(n))
        defects.update(
            {
                "occupation_current": delta_occ_j,
                "occupation_extensive_charge": delta_occ_sigma,
                "occupation_profile_l1": occupation_profile_l1,
            }
        )
        occupation_audit = {
            "predicted_current": j_pred,
            "predicted_charge": Q_pred,
            "predicted_profile": occupation_profile,
        }

    return {
        "noether_charge": Q_theta,
        "rfc_charge": Q_sigma,
        "noether_profile": p_theta,
        "rfc_profile": p_q,
        "occupation_audit": occupation_audit,
        "defects": defects,
        "max_defect": max(defects.values()),
    }


def receipt_passes(receipt: dict[str, object], *, atol: float = 0.0) -> bool:
    tol = _finite("atol", atol)
    if tol < 0.0:
        raise CurrentMeasureReceiptError("atol must be nonnegative")
    defects = receipt.get("defects")
    if not isinstance(defects, dict):
        raise CurrentMeasureReceiptError("receipt must contain a defects mapping")
    return all(abs(_finite(f"defect[{name}]", value)) <= tol for name, value in defects.items())
