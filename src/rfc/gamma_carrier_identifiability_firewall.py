from __future__ import annotations

import math
from dataclasses import dataclass


class GammaCarrierIdentifiabilityError(ValueError):
    pass


def _finite(name: str, value: float) -> float:
    value = float(value)
    if not math.isfinite(value):
        raise GammaCarrierIdentifiabilityError(f"{name} must be finite")
    return value


def _positive(name: str, value: float) -> float:
    value = _finite(name, value)
    if value <= 0.0:
        raise GammaCarrierIdentifiabilityError(f"{name} must be positive")
    return value


def _nonempty(name: str, value: str) -> str:
    if not isinstance(value, str) or not value:
        raise GammaCarrierIdentifiabilityError(f"{name} must be a nonempty string")
    return value


def symmetric_defect(left: float, right: float) -> float:
    a = _finite("left", left)
    b = _finite("right", right)
    denom = abs(a) + abs(b)
    if denom == 0.0:
        return 0.0
    return 2.0 * abs(a - b) / denom


@dataclass(frozen=True)
class IdentifiabilityProvenance:
    alpha_c_source_id: str
    source_operator_receipt_id: str
    current_receipt_id: str
    phase_rate_receipt_id: str
    gamma_source_id: str
    carrier_type_source_id: str
    gravity_output_id: str
    horizon_provenance_id: str | None = None

    def __post_init__(self) -> None:
        for name, value in (
            ("alpha_c_source_id", self.alpha_c_source_id),
            ("source_operator_receipt_id", self.source_operator_receipt_id),
            ("current_receipt_id", self.current_receipt_id),
            ("phase_rate_receipt_id", self.phase_rate_receipt_id),
            ("gamma_source_id", self.gamma_source_id),
            ("carrier_type_source_id", self.carrier_type_source_id),
            ("gravity_output_id", self.gravity_output_id),
        ):
            _nonempty(name, value)
        if self.horizon_provenance_id is not None:
            _nonempty("horizon_provenance_id", self.horizon_provenance_id)


@dataclass(frozen=True)
class GammaCarrierInputs:
    alpha_c: float
    omega_q: float
    source_s_r: float
    current_j_q: float
    gamma_dc: float
    zeta_m: float
    provenance: IdentifiabilityProvenance
    gravity_target_used_for_gamma_selection: bool = False
    gravity_target_used_for_carrier_type_selection: bool = False
    horizon_mass: float | None = None
    horizon_temperature: float | None = None

    def __post_init__(self) -> None:
        for name, value in (
            ("alpha_c", self.alpha_c),
            ("omega_q", self.omega_q),
            ("source_s_r", self.source_s_r),
            ("current_j_q", self.current_j_q),
            ("gamma_dc", self.gamma_dc),
            ("zeta_m", self.zeta_m),
        ):
            _positive(name, value)
        if (self.horizon_mass is None) != (self.horizon_temperature is None):
            raise GammaCarrierIdentifiabilityError(
                "horizon_mass and horizon_temperature must be supplied together"
            )
        if self.horizon_mass is not None:
            _positive("horizon_mass", self.horizon_mass)
            _positive("horizon_temperature", self.horizon_temperature)
            if self.provenance.horizon_provenance_id is None:
                raise GammaCarrierIdentifiabilityError(
                    "horizon_provenance_id is required with horizon inputs"
                )


def build_gamma_carrier_identifiability_receipt(
    inputs: GammaCarrierInputs,
) -> dict[str, object]:
    alpha = _positive("alpha_c", inputs.alpha_c)
    omega = _positive("omega_q", inputs.omega_q)
    source = _positive("source_s_r", inputs.source_s_r)
    current = _positive("current_j_q", inputs.current_j_q)
    gamma = _positive("gamma_dc", inputs.gamma_dc)
    zeta = _positive("zeta_m", inputs.zeta_m)

    # RF-N1C Newton/source route in natural units:
    # G_N = S_R/(2*pi*omega_Q*j_Q), Mbar_G = 1/sqrt(8*pi*G_N).
    g_source = source / (2.0 * math.pi * omega * current)
    mbar_source = math.sqrt(omega * current / (4.0 * source))
    kappa_e_source = 1.0 / (mbar_source * mbar_source)

    # RFG4G + RF-N1C4:
    # Mbar_G = zeta_M*alpha_c*omega_Q/(2*Gamma_DC).
    ratio_source = alpha * math.sqrt(omega * source / current)
    ratio_candidate = gamma / zeta
    gamma_from_source_given_zeta = zeta * ratio_source

    defects: dict[str, float] = {
        "gamma_over_zeta_source": symmetric_defect(ratio_candidate, ratio_source),
        "gravity_selection_independence": 1.0
        if (
            inputs.gravity_target_used_for_gamma_selection
            or inputs.gravity_target_used_for_carrier_type_selection
        )
        else 0.0,
    }

    gravity_id = inputs.provenance.gravity_output_id
    provenance_collision = 0.0
    for source_id in (
        inputs.provenance.alpha_c_source_id,
        inputs.provenance.source_operator_receipt_id,
        inputs.provenance.current_receipt_id,
        inputs.provenance.phase_rate_receipt_id,
        inputs.provenance.gamma_source_id,
        inputs.provenance.carrier_type_source_id,
    ):
        if source_id == gravity_id:
            provenance_collision = 1.0
    defects["provenance_collision"] = provenance_collision

    horizon: dict[str, float] | None = None
    if inputs.horizon_mass is not None:
        mass = _positive("horizon_mass", inputs.horizon_mass)
        temp = _positive("horizon_temperature", inputs.horizon_temperature)
        mbar_horizon = math.sqrt(mass * temp)
        ratio_horizon = alpha * omega / (2.0 * mbar_horizon)
        source_horizon_left = 4.0 * mass * temp * source
        source_horizon_right = omega * current
        defects["source_horizon_ratio"] = symmetric_defect(ratio_source, ratio_horizon)
        defects["source_horizon_holonomy"] = symmetric_defect(
            source_horizon_left,
            source_horizon_right,
        )
        horizon_circularity = 0.0
        if inputs.provenance.horizon_provenance_id in {
            gravity_id,
            inputs.provenance.gamma_source_id,
        }:
            horizon_circularity = 1.0
        defects["horizon_provenance_independence"] = horizon_circularity
        horizon = {
            "mbar_horizon": mbar_horizon,
            "gamma_over_zeta_horizon": ratio_horizon,
            "source_horizon_left": source_horizon_left,
            "source_horizon_right": source_horizon_right,
        }

    return {
        "units": "natural",
        "g_source": g_source,
        "mbar_source": mbar_source,
        "kappa_e_source": kappa_e_source,
        "gamma_over_zeta_source": ratio_source,
        "gamma_over_zeta_candidate": ratio_candidate,
        "gamma_from_source_given_zeta": gamma_from_source_given_zeta,
        "gamma_kinetic_branch": ratio_source,
        "gamma_total_rest_branch": 2.0 * ratio_source,
        "branch_gamma_ratio": 2.0,
        "horizon": horizon,
        "defects": defects,
        "max_defect": max(defects.values()),
    }


def receipt_passes(receipt: dict[str, object], *, atol: float = 0.0) -> bool:
    tol = _finite("atol", atol)
    if tol < 0.0:
        raise GammaCarrierIdentifiabilityError("atol must be nonnegative")
    return _finite("max_defect", receipt.get("max_defect", float("nan"))) <= tol
