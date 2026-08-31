from __future__ import annotations

from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class ProperClockRoute:
    proper_temporal_clock: bool
    wick_dominates_clock: bool
    wick_complete_derived: bool
    smooth_slice_lapse_majorant_derived: bool
    steep_reparametrization_derived: bool
    global_hyperbolicity_eligible: bool
    global_gr_cauchy_carrier_eligible: bool


def wick_norm_sq(dt_value: float, spatial_norm_sq: float) -> float:
    a = float(dt_value)
    hyy = float(spatial_norm_sq)
    if not np.isfinite(a) or not np.isfinite(hyy):
        raise ValueError("Wick inputs must be finite")
    if hyy < 0.0:
        raise ValueError("spatial_norm_sq must be nonnegative")
    return a * a + hyy


def wick_dominates_clock(dt_value: float, spatial_norm_sq: float, tol: float = 1e-12) -> bool:
    a = float(dt_value)
    return wick_norm_sq(a, spatial_norm_sq) + tol >= a * a


def certify_proper_clock_route(
    *,
    global_lorentzian_carrier: bool,
    global_regular_temporal_clock: bool,
    proper_temporal_clock_to_real_line: bool,
    smooth_finite_positive_lapse: bool,
    global_einstein_carrier: bool = False,
) -> ProperClockRoute:
    proper_clock = bool(global_regular_temporal_clock and proper_temporal_clock_to_real_line)
    wick_domination = bool(global_lorentzian_carrier and proper_clock)

    # Mathematical theorem encoded by the certifier contract:
    # W >= dt^2 and proper t:M->R imply Riemannian completeness of W.
    wick_complete = bool(wick_domination)

    # Properness makes each compact time slab compact. A smooth finite lapse is
    # bounded on each slab; its slice supremum is locally bounded on R and hence
    # admits a smooth positive majorant m(t). Integrating m gives a steep
    # reparametrization tau(t).
    majorant = bool(proper_clock and smooth_finite_positive_lapse)
    steep = bool(wick_complete and majorant)
    gh = bool(global_lorentzian_carrier and steep)

    return ProperClockRoute(
        proper_temporal_clock=proper_clock,
        wick_dominates_clock=wick_domination,
        wick_complete_derived=wick_complete,
        smooth_slice_lapse_majorant_derived=majorant,
        steep_reparametrization_derived=steep,
        global_hyperbolicity_eligible=gh,
        global_gr_cauchy_carrier_eligible=bool(gh and global_einstein_carrier),
    )


def certify_product_projection_properness(
    *,
    global_product_trivialization: bool,
    time_axis_is_real_line: bool,
    spatial_fiber_compact: bool,
) -> dict:
    proper = bool(global_product_trivialization and time_axis_is_real_line and spatial_fiber_compact)
    return {
        "schema": "RFC_GSC6B_PRODUCT_PROPER_CLOCK_COROLLARY_V0_1",
        "product_clock_proper": proper,
        "properness_basis": "preimage([a,b])=[a,b]xSigma compact" if proper else None,
        "global_hyperbolicity_promoted": False,
        "requires_rf_l8_or_gsc6b_composition": True,
    }
