"""Fail-closed RF-E21 Einstein uniqueness selection ledger."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping


@dataclass(frozen=True)
class LovelockPremises:
    dimension_four: bool
    lorentzian_metric: bool
    levi_civita: bool
    natural_covariant_metric_tensor: bool
    at_most_second_metric_derivatives: bool
    symmetric_rank_two: bool
    divergence_free: bool


def lovelock_term_status(dimension: int, curvature_order: int) -> str:
    """Classify the Lovelock density of order k in spacetime dimension D."""
    if dimension <= 0:
        raise ValueError("dimension must be positive")
    if curvature_order < 0:
        raise ValueError("curvature_order must be nonnegative")
    if curvature_order == 0:
        return "DYNAMIC"
    critical = 2 * curvature_order
    if dimension > critical:
        return "DYNAMIC"
    if dimension == critical:
        return "TOPOLOGICAL"
    return "ZERO"


def tensor_selection_status(p: LovelockPremises) -> str:
    """Promote only when every theorem premise is explicitly admitted."""
    if all((
        p.dimension_four,
        p.lorentzian_metric,
        p.levi_civita,
        p.natural_covariant_metric_tensor,
        p.at_most_second_metric_derivatives,
        p.symmetric_rank_two,
        p.divergence_free,
    )):
        return "EINSTEIN_PLUS_METRIC_TERM_SELECTED"
    return "PROJECT_PREMISES_OPEN"


PROJECT_PREMISE_LEDGER: Mapping[str, str] = {
    "local_rank3_spatial_carrier": "PASS_LOCAL_CARRIER",
    "temporal_orientation": "PASS_PARENT_IDT",
    "lorentzian_signature": "PASS_THEOREM_ON_CARRIER",
    "positive_lapse_adm_metric": "PASS_KINEMATIC",
    "local_metric_torsion_free_connection": "PASS_LOCAL_ON_REFERENCE_TORSION_FREE_SURFACE",
    "global_refinement_levi_civita": "OPEN",
    "full_4d_naturality_covariance": "OPEN",
    "second_order_locality": "OPEN",
    "divergence_free_selection_binding": "OPEN_SELECTION_BINDING",
    "rf_e3_coupling_normalization": "PASS_ALGEBRA_PHYSICAL_VALUE_CONDITIONAL",
}

HKT_LEDGER: Mapping[str, str] = {
    "spatial_metric_hij": "PRESENT",
    "lapse_N": "PRESENT",
    "shift_bi": "PRESENT_TYPED_INPUT",
    "independent_gravitational_piij": "OPEN",
    "independent_hypersurface_deformation_algebra": "OPEN",
    "independent_hkt_crosscheck": "OPEN",
}


def project_ready_for_lovelock_promotion() -> bool:
    return not any(value.startswith("OPEN") for value in PROJECT_PREMISE_LEDGER.values())


def hkt_independent_route_ready() -> bool:
    return not any(value.startswith("OPEN") for value in HKT_LEDGER.values())


def four_dimensional_lovelock_spectrum(max_order: int = 5) -> dict[int, str]:
    if max_order < 0:
        raise ValueError("max_order must be nonnegative")
    return {k: lovelock_term_status(4, k) for k in range(max_order + 1)}
