from __future__ import annotations

import math
from dataclasses import dataclass
from collections.abc import Sequence


class TreeAmplitudeIdentifiabilityError(ValueError):
    pass


def _finite(name: str, value: float) -> float:
    value = float(value)
    if not math.isfinite(value):
        raise TreeAmplitudeIdentifiabilityError(f"{name} must be finite")
    return value


def _positive(name: str, value: float) -> float:
    value = _finite(name, value)
    if value <= 0.0:
        raise TreeAmplitudeIdentifiabilityError(f"{name} must be positive")
    return value


def symmetric_defect(left: float, right: float) -> float:
    a = _finite("left", left)
    b = _finite("right", right)
    denom = abs(a) + abs(b)
    if denom == 0.0:
        return 0.0
    return 2.0 * abs(a - b) / denom


@dataclass(frozen=True)
class TreeAmplitudeCoordinates:
    g1: float
    g2: float
    gamma_dc: float
    m_star: float
    epsilon_q: float
    zeta_m: float

    def __post_init__(self) -> None:
        for name, value in (
            ("g1", self.g1),
            ("g2", self.g2),
            ("gamma_dc", self.gamma_dc),
            ("m_star", self.m_star),
            ("epsilon_q", self.epsilon_q),
            ("zeta_m", self.zeta_m),
        ):
            _positive(name, value)


def _validate_multiplicities(multiplicities: Sequence[int]) -> tuple[int, ...]:
    values = tuple(multiplicities)
    if not values:
        raise TreeAmplitudeIdentifiabilityError("at least one multiplicity is required")
    for n in values:
        if not isinstance(n, int) or n < 3:
            raise TreeAmplitudeIdentifiabilityError("tree multiplicities must be integers >= 3")
    return values


def _coordinates_receipt(
    coordinates: TreeAmplitudeCoordinates,
    multiplicities: Sequence[int],
) -> dict[str, object]:
    ns = _validate_multiplicities(multiplicities)
    g1 = _positive("g1", coordinates.g1)
    g2 = _positive("g2", coordinates.g2)
    gamma = _positive("gamma_dc", coordinates.gamma_dc)
    m_star = _positive("m_star", coordinates.m_star)
    epsilon = _positive("epsilon_q", coordinates.epsilon_q)
    zeta = _positive("zeta_m", coordinates.zeta_m)

    kappa_g = 2.0 * gamma * g1 * g2 / m_star
    kappa_e = kappa_g * kappa_g / 4.0
    mbar_g = m_star / (gamma * g1 * g2)
    ratio = gamma / zeta
    prefactors = {n: (kappa_g / 2.0) ** (n - 2) for n in ns}

    return {
        "kappa_g": kappa_g,
        "kappa_e": kappa_e,
        "mbar_g": mbar_g,
        "gamma_over_zeta": ratio,
        "carrier_relation_defect": symmetric_defect(m_star, zeta * epsilon),
        "tree_prefactors": prefactors,
    }


def build_tree_amplitude_identifiability_receipt(
    coordinates: TreeAmplitudeCoordinates,
    *,
    scale_lambda: float,
    multiplicities: Sequence[int] = (3, 4, 5),
) -> dict[str, object]:
    lam = _positive("scale_lambda", scale_lambda)
    ns = _validate_multiplicities(multiplicities)
    base = _coordinates_receipt(coordinates, ns)
    scaled_coordinates = TreeAmplitudeCoordinates(
        g1=coordinates.g1,
        g2=coordinates.g2,
        gamma_dc=lam * coordinates.gamma_dc,
        m_star=lam * coordinates.m_star,
        epsilon_q=coordinates.epsilon_q,
        zeta_m=lam * coordinates.zeta_m,
    )
    scaled = _coordinates_receipt(scaled_coordinates, ns)

    prefactor_defects = {
        n: symmetric_defect(base["tree_prefactors"][n], scaled["tree_prefactors"][n])
        for n in ns
    }
    defects = {
        "base_carrier_relation": base["carrier_relation_defect"],
        "scaled_carrier_relation": scaled["carrier_relation_defect"],
        "kappa_g_scaling": symmetric_defect(base["kappa_g"], scaled["kappa_g"]),
        "kappa_e_scaling": symmetric_defect(base["kappa_e"], scaled["kappa_e"]),
        "mbar_g_scaling": symmetric_defect(base["mbar_g"], scaled["mbar_g"]),
        "gamma_over_zeta_scaling": symmetric_defect(
            base["gamma_over_zeta"], scaled["gamma_over_zeta"]
        ),
        "tree_prefactor_scaling": max(prefactor_defects.values()),
    }

    return {
        "base": base,
        "scaled": scaled,
        "scale_lambda": lam,
        "multiplicities": ns,
        "prefactor_defects": prefactor_defects,
        "log_sensitivity_kappa_g": {"gamma_dc": 1.0, "zeta_m": -1.0},
        "log_sensitivity_kappa_e": {"gamma_dc": 2.0, "zeta_m": -2.0},
        "identifiability_rank": 1,
        "null_direction_log_gamma_log_zeta": (1.0, 1.0),
        "identifiable_combination": "Gamma_DC/zeta_M",
        "null_scaling_dimension": 1,
        "defects": defects,
        "max_defect": max(defects.values()),
    }


def receipt_passes(receipt: dict[str, object], *, atol: float = 0.0) -> bool:
    tol = _finite("atol", atol)
    if tol < 0.0:
        raise TreeAmplitudeIdentifiabilityError("atol must be nonnegative")
    return _finite("max_defect", receipt.get("max_defect", float("nan"))) <= tol
