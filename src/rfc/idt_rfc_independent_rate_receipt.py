from __future__ import annotations

import math
from dataclasses import dataclass


C_LIGHT = 299_792_458.0


class IndependentRateReceiptError(ValueError):
    pass


def _finite(name: str, value: float) -> float:
    value = float(value)
    if not math.isfinite(value):
        raise IndependentRateReceiptError(f"{name} must be finite")
    return value


def _positive(name: str, value: float) -> float:
    value = _finite(name, value)
    if value <= 0.0:
        raise IndependentRateReceiptError(f"{name} must be positive")
    return value


def _nonzero(name: str, value: float) -> float:
    value = _finite(name, value)
    if value == 0.0:
        raise IndependentRateReceiptError(f"{name} must be nonzero")
    return value


def normalized_defect(lhs: float, rhs: float, *, denominator: float | None = None) -> float:
    left = _finite("lhs", lhs)
    right = _finite("rhs", rhs)
    denom = abs(_nonzero("denominator", right if denominator is None else denominator))
    return abs(left - right) / denom


@dataclass(frozen=True)
class LineageIDs:
    bundle: str
    phase_patch: str
    connection: str
    clock: str
    coframe: str
    measure: str
    support: str

    def __post_init__(self) -> None:
        for name, value in (
            ("bundle", self.bundle),
            ("phase_patch", self.phase_patch),
            ("connection", self.connection),
            ("clock", self.clock),
            ("coframe", self.coframe),
            ("measure", self.measure),
            ("support", self.support),
        ):
            if not isinstance(value, str) or not value:
                raise IndependentRateReceiptError(f"{name} id must be a nonempty string")


def lineage_defects(field: LineageIDs, rotor: LineageIDs) -> dict[str, float]:
    return {
        "bundle": 0.0 if field.bundle == rotor.bundle else 1.0,
        "phase_patch": 0.0 if field.phase_patch == rotor.phase_patch else 1.0,
        "connection": 0.0 if field.connection == rotor.connection else 1.0,
        "clock": 0.0 if field.clock == rotor.clock else 1.0,
        "coframe": 0.0 if field.coframe == rotor.coframe else 1.0,
        "measure": 0.0 if field.measure == rotor.measure else 1.0,
        "support": 0.0 if field.support == rotor.support else 1.0,
    }


def phase_scale_from_independent_rotor_proper_rate(
    rotor_proper_rate: float,
    *,
    c_light: float = C_LIGHT,
) -> float:
    rate = _nonzero("rotor_proper_rate", rotor_proper_rate)
    c = _positive("c_light", c_light)
    return abs(rate) / c


def build_independent_rate_receipt(
    *,
    lapse_ratio: float,
    field_coordinate_rate: float,
    field_normal_proper_rate: float,
    rotor_coordinate_rate: float,
    rotor_proper_rate: float,
    field_inertia: float,
    rotor_inertia: float,
    rfc_omega: float,
    field_lineage: LineageIDs,
    rotor_lineage: LineageIDs,
    c_light: float = C_LIGHT,
) -> dict[str, object]:
    """Audit IDT 01AC/01AD <-> RFC RF-N1B2M/N/F3 using independent inputs."""
    lapse = _positive("lapse_ratio", lapse_ratio)
    field_coord = _nonzero("field_coordinate_rate", field_coordinate_rate)
    field_proper = _nonzero("field_normal_proper_rate", field_normal_proper_rate)
    rotor_coord = _nonzero("rotor_coordinate_rate", rotor_coordinate_rate)
    rotor_proper = _nonzero("rotor_proper_rate", rotor_proper_rate)
    I_A = _positive("field_inertia", field_inertia)
    I_phi = _positive("rotor_inertia", rotor_inertia)
    omega = _nonzero("rfc_omega", rfc_omega)
    c = _positive("c_light", c_light)

    Q_theta = I_A * field_proper
    P_phi = I_phi * rotor_proper

    defects = {
        "coordinate_rate": normalized_defect(field_coord, rotor_coord),
        "field_lapse_rate": normalized_defect(field_coord, lapse * field_proper, denominator=field_coord),
        "rotor_lapse_rate": normalized_defect(rotor_coord, lapse * rotor_proper, denominator=rotor_coord),
        "proper_rate": normalized_defect(field_proper, rotor_proper),
        "inertia": normalized_defect(I_A, I_phi),
        "generator": normalized_defect(Q_theta, P_phi),
        "rfc_omega": normalized_defect(omega, field_proper),
    }
    defects.update({f"lineage_{key}": value for key, value in lineage_defects(field_lineage, rotor_lineage).items()})

    mu_vartheta = abs(rotor_proper) / c

    return {
        "lapse_ratio": lapse,
        "field_coordinate_rate": field_coord,
        "field_normal_proper_rate": field_proper,
        "rotor_coordinate_rate": rotor_coord,
        "rotor_proper_rate": rotor_proper,
        "field_generator": Q_theta,
        "rotor_generator": P_phi,
        "rfc_omega": omega,
        "mu_vartheta": mu_vartheta,
        "defects": defects,
        "max_defect": max(float(value) for value in defects.values()),
    }


def receipt_passes(receipt: dict[str, object], *, atol: float = 0.0) -> bool:
    tol = _finite("atol", atol)
    if tol < 0.0:
        raise IndependentRateReceiptError("atol must be nonnegative")
    if "defects" not in receipt or not isinstance(receipt["defects"], dict):
        raise IndependentRateReceiptError("receipt must contain a defects mapping")
    return all(abs(_finite(f"defect[{name}]", value)) <= tol for name, value in receipt["defects"].items())
