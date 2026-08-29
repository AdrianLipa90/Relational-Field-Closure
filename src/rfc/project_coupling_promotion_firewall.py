from __future__ import annotations

import math
from dataclasses import dataclass


class ProjectCouplingPromotionError(ValueError):
    pass


def _finite(name: str, value: float) -> float:
    value = float(value)
    if not math.isfinite(value):
        raise ProjectCouplingPromotionError(f"{name} must be finite")
    return value


def _positive(name: str, value: float) -> float:
    value = _finite(name, value)
    if value <= 0.0:
        raise ProjectCouplingPromotionError(f"{name} must be positive")
    return value


def _nonnegative(name: str, value: float) -> float:
    value = _finite(name, value)
    if value < 0.0:
        raise ProjectCouplingPromotionError(f"{name} must be nonnegative")
    return value


def _nonempty(name: str, value: str) -> str:
    if not isinstance(value, str) or not value:
        raise ProjectCouplingPromotionError(f"{name} must be a nonempty string")
    return value


def symmetric_defect(left: float, right: float) -> float:
    a = _finite("left", left)
    b = _finite("right", right)
    denom = abs(a) + abs(b)
    if denom == 0.0:
        return 0.0
    return 2.0 * abs(a - b) / denom


_ALLOWED_AUTHORITIES = {
    "REFERENCE_RECEIPT",
    "INDEPENDENT_MEASUREMENT",
    "DERIVED_PROJECT_ACTION",
}


@dataclass(frozen=True)
class CouplingProvenance:
    bcj_receipt_id: str
    bcj_authority: str
    wilson_source_id: str
    wilson_authority: str
    gamma_source_id: str
    gamma_authority: str
    carrier_scale_source_id: str
    carrier_scale_authority: str
    gravity_output_id: str

    def __post_init__(self) -> None:
        for name, value in (
            ("bcj_receipt_id", self.bcj_receipt_id),
            ("wilson_source_id", self.wilson_source_id),
            ("gamma_source_id", self.gamma_source_id),
            ("carrier_scale_source_id", self.carrier_scale_source_id),
            ("gravity_output_id", self.gravity_output_id),
        ):
            _nonempty(name, value)
        for name, value in (
            ("bcj_authority", self.bcj_authority),
            ("wilson_authority", self.wilson_authority),
            ("gamma_authority", self.gamma_authority),
            ("carrier_scale_authority", self.carrier_scale_authority),
        ):
            _nonempty(name, value)
            if value not in _ALLOWED_AUTHORITIES:
                raise ProjectCouplingPromotionError(
                    f"{name} must be one of {sorted(_ALLOWED_AUTHORITIES)}"
                )


@dataclass(frozen=True)
class ProjectCouplingInputs:
    beta_w: float
    g_ym_squared: float
    gamma_dc: float
    m_star: float
    epsilon_q: float
    carrier_type: str
    bcj_graph_count: int
    bcj_independent_jacobi_rank: int
    bcj_jacobi_defect: float
    bcj_reconstruction_defect: float
    bcj_klt_defect: float
    bcj_ward_defect: float
    gravity_target_used_for_bcj_selection: bool
    gravity_target_used_for_beta_selection: bool
    gravity_target_used_for_gamma_selection: bool
    gravity_target_used_for_mstar_selection: bool
    provenance: CouplingProvenance

    def __post_init__(self) -> None:
        for name, value in (
            ("beta_w", self.beta_w),
            ("g_ym_squared", self.g_ym_squared),
            ("gamma_dc", self.gamma_dc),
            ("m_star", self.m_star),
            ("epsilon_q", self.epsilon_q),
        ):
            _positive(name, value)
        for name, value in (
            ("bcj_jacobi_defect", self.bcj_jacobi_defect),
            ("bcj_reconstruction_defect", self.bcj_reconstruction_defect),
            ("bcj_klt_defect", self.bcj_klt_defect),
            ("bcj_ward_defect", self.bcj_ward_defect),
        ):
            _nonnegative(name, value)
        if self.carrier_type not in {
            "KINETIC_CARRIER",
            "TOTAL_ONSHELL_REST",
            "INDEPENDENT_DERIVED",
        }:
            raise ProjectCouplingPromotionError("unsupported carrier_type")
        if not isinstance(self.bcj_graph_count, int) or self.bcj_graph_count <= 0:
            raise ProjectCouplingPromotionError("bcj_graph_count must be a positive integer")
        if not isinstance(self.bcj_independent_jacobi_rank, int) or self.bcj_independent_jacobi_rank < 0:
            raise ProjectCouplingPromotionError("bcj_independent_jacobi_rank must be a nonnegative integer")


def build_project_coupling_promotion_receipt(inputs: ProjectCouplingInputs) -> dict[str, object]:
    beta = _positive("beta_w", inputs.beta_w)
    g2 = _positive("g_ym_squared", inputs.g_ym_squared)
    gamma = _positive("gamma_dc", inputs.gamma_dc)
    m_star = _positive("m_star", inputs.m_star)
    epsilon = _positive("epsilon_q", inputs.epsilon_q)

    g2_wilson = 6.0 / beta
    zeta_m = m_star / epsilon
    expected_zeta: float | None
    if inputs.carrier_type == "KINETIC_CARRIER":
        expected_zeta = 1.0
    elif inputs.carrier_type == "TOTAL_ONSHELL_REST":
        expected_zeta = 2.0
    else:
        expected_zeta = None

    carrier_type_defect = 0.0 if expected_zeta is None else symmetric_defect(zeta_m, expected_zeta)
    bcj_structural_defect = 0.0
    if inputs.bcj_graph_count != 15 or inputs.bcj_independent_jacobi_rank != 9:
        bcj_structural_defect = 1.0

    bcj_max_defect = max(
        _nonnegative("bcj_jacobi_defect", inputs.bcj_jacobi_defect),
        _nonnegative("bcj_reconstruction_defect", inputs.bcj_reconstruction_defect),
        _nonnegative("bcj_klt_defect", inputs.bcj_klt_defect),
        _nonnegative("bcj_ward_defect", inputs.bcj_ward_defect),
        bcj_structural_defect,
    )

    selection_flags = (
        inputs.gravity_target_used_for_bcj_selection,
        inputs.gravity_target_used_for_beta_selection,
        inputs.gravity_target_used_for_gamma_selection,
        inputs.gravity_target_used_for_mstar_selection,
    )
    selection_independence_defect = 1.0 if any(selection_flags) else 0.0

    gravity_id = inputs.provenance.gravity_output_id
    provenance_collision_defect = 0.0
    for source_id in (
        inputs.provenance.bcj_receipt_id,
        inputs.provenance.wilson_source_id,
        inputs.provenance.gamma_source_id,
        inputs.provenance.carrier_scale_source_id,
    ):
        if source_id == gravity_id:
            provenance_collision_defect = 1.0

    mbar_g = m_star / (gamma * g2)
    kappa_e_natural = 1.0 / (mbar_g * mbar_g)

    defects = {
        "wilson_normalization": symmetric_defect(g2, g2_wilson),
        "carrier_type": carrier_type_defect,
        "bcj": bcj_max_defect,
        "gravity_selection_independence": selection_independence_defect,
        "provenance_collision": provenance_collision_defect,
    }

    return {
        "units": "natural",
        "g_ym_squared_wilson": g2_wilson,
        "zeta_m": zeta_m,
        "carrier_type": inputs.carrier_type,
        "mbar_g": mbar_g,
        "kappa_e_natural": kappa_e_natural,
        "gamma_dc": gamma,
        "bcj_graph_count": inputs.bcj_graph_count,
        "bcj_independent_jacobi_rank": inputs.bcj_independent_jacobi_rank,
        "defects": defects,
        "max_defect": max(defects.values()),
        "gamma_dc_is_independent_input": True,
        "numerical_gravity_target_used_for_selection": any(selection_flags),
    }


def receipt_passes(receipt: dict[str, object], *, atol: float = 0.0) -> bool:
    tol = _nonnegative("atol", atol)
    return _finite("max_defect", receipt.get("max_defect", float("nan"))) <= tol
