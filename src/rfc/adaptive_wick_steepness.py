from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

import numpy as np


@dataclass(frozen=True)
class AdaptiveSteepnessResult:
    lapse: float
    dt_value: float
    spatial_norm_sq: float
    wick_norm_sq: float
    adaptive_norm_sq: float
    causal_defect: float
    steepness_defect: float
    passed: bool


def _finite_scalar(value: float, name: str) -> float:
    out = float(value)
    if not np.isfinite(out):
        raise ValueError(f"{name} must be finite")
    return out


def adaptive_scale(lapse: float) -> float:
    n = _finite_scalar(lapse, "lapse")
    if n <= 0.0:
        raise ValueError("lapse must be positive")
    return 1.0 / (1.0 + n * n)


def adaptive_wick_norm_sq(lapse: float, dt_value: float, spatial_norm_sq: float) -> float:
    n = _finite_scalar(lapse, "lapse")
    a = _finite_scalar(dt_value, "dt_value")
    hyy = _finite_scalar(spatial_norm_sq, "spatial_norm_sq")
    if n <= 0.0:
        raise ValueError("lapse must be positive")
    if hyy < 0.0:
        raise ValueError("spatial_norm_sq must be nonnegative")
    wick = a * a + hyy
    return wick / (1.0 + n * n)


def certify_adaptive_steepness(
    *,
    lapse: float,
    dt_value: float,
    spatial_norm_sq: float,
    future_causal: bool = True,
    tol: float = 1e-12,
) -> AdaptiveSteepnessResult:
    n = _finite_scalar(lapse, "lapse")
    a = _finite_scalar(dt_value, "dt_value")
    hyy = _finite_scalar(spatial_norm_sq, "spatial_norm_sq")
    if n <= 0.0:
        raise ValueError("lapse must be positive")
    if hyy < 0.0:
        raise ValueError("spatial_norm_sq must be nonnegative")
    if future_causal and a <= 0.0:
        raise ValueError("future-causal vector requires dt(v)>0")

    causal_bound = n * n * a * a
    causal_defect = max(0.0, hyy - causal_bound)
    wick = a * a + hyy
    adaptive = wick / (1.0 + n * n)
    steepness_defect = max(0.0, adaptive - a * a)
    passed = (
        (not future_causal or causal_defect <= tol)
        and (not future_causal or steepness_defect <= tol)
    )
    return AdaptiveSteepnessResult(
        lapse=n,
        dt_value=a,
        spatial_norm_sq=hyy,
        wick_norm_sq=wick,
        adaptive_norm_sq=adaptive,
        causal_defect=causal_defect,
        steepness_defect=steepness_defect,
        passed=passed,
    )


def certify_adaptive_global_promotion(
    *,
    global_lorentzian_carrier: bool,
    global_regular_clock: bool,
    adaptive_metric_complete: bool,
    global_einstein_carrier: bool = False,
) -> dict:
    causal_geometry = bool(
        global_lorentzian_carrier
        and global_regular_clock
        and adaptive_metric_complete
    )
    return {
        "schema": "RFC_GSC6A_ADAPTIVE_WICK_STEEPNESS_V0_1",
        "adaptive_metric": "H_N=(1+N^2)^(-1) W",
        "global_lapse_upper_bound_required_on_this_route": False,
        "global_wick_W_completeness_required_on_this_route": False,
        "adaptive_metric_completeness_required": True,
        "global_hyperbolicity_eligible": causal_geometry,
        "global_gr_cauchy_carrier_eligible": bool(causal_geometry and global_einstein_carrier),
        "nonlinear_global_stability_promoted": False,
    }
