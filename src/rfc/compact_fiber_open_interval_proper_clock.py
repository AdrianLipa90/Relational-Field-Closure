from __future__ import annotations

from dataclasses import dataclass
import math
from typing import Optional


@dataclass(frozen=True)
class OpenInterval:
    lower: Optional[float] = None
    upper: Optional[float] = None

    def __post_init__(self) -> None:
        if self.lower is not None and not math.isfinite(float(self.lower)):
            raise ValueError("lower endpoint must be finite or None")
        if self.upper is not None and not math.isfinite(float(self.upper)):
            raise ValueError("upper endpoint must be finite or None")
        if self.lower is not None and self.upper is not None:
            if not float(self.lower) < float(self.upper):
                raise ValueError("open interval requires lower < upper")

    def contains(self, value: float) -> bool:
        x = float(value)
        if not math.isfinite(x):
            return False
        if self.lower is not None and not x > float(self.lower):
            return False
        if self.upper is not None and not x < float(self.upper):
            return False
        return True


def interval_to_real(value: float, interval: OpenInterval) -> float:
    """Orientation-preserving smooth diffeomorphism from an open interval to R."""
    x = float(value)
    if not interval.contains(x):
        raise ValueError("clock value lies outside the declared open interval")

    lo, hi = interval.lower, interval.upper
    if lo is None and hi is None:
        return x
    if lo is not None and hi is None:
        return math.log(x - float(lo))
    if lo is None and hi is not None:
        return -math.log(float(hi) - x)

    assert lo is not None and hi is not None
    return math.log((x - float(lo)) / (float(hi) - x))


def interval_to_real_derivative(value: float, interval: OpenInterval) -> float:
    x = float(value)
    if not interval.contains(x):
        raise ValueError("clock value lies outside the declared open interval")

    lo, hi = interval.lower, interval.upper
    if lo is None and hi is None:
        return 1.0
    if lo is not None and hi is None:
        return 1.0 / (x - float(lo))
    if lo is None and hi is not None:
        return 1.0 / (float(hi) - x)

    assert lo is not None and hi is not None
    return 1.0 / (x - float(lo)) + 1.0 / (float(hi) - x)


@dataclass(frozen=True)
class CompactFiberProperClockRoute:
    open_interval_clock_derived: bool
    compact_spatial_fiber_admitted: bool
    proper_real_clock_derived: bool
    temporal_orientation_preserved: bool
    gsc6b_proper_clock_input_derived: bool
    global_hyperbolicity_eligible: bool
    global_gr_cauchy_carrier_eligible: bool


def certify_compact_fiber_product_route(
    *,
    global_product_trivialization: bool,
    global_regular_clock: bool,
    spatial_fiber_compact: bool,
    rf_e25_global_lorentzian_adm_carrier: bool,
    smooth_finite_positive_lapse: bool,
    global_einstein_carrier: bool = False,
) -> CompactFiberProperClockRoute:
    # On the GSC3A route, a surjective regular scalar clock with product image
    # I is a submersion onto an open interval I subset R.
    open_interval = bool(global_product_trivialization and global_regular_clock)
    compact_fiber = bool(spatial_fiber_compact)

    # Every open interval admits an orientation-preserving diffeomorphism psi:I->R.
    # For tau=psi o t, compact K subset R pulls back to
    # psi^{-1}(K) x Sigma, compact when Sigma is compact.
    proper_real_clock = bool(open_interval and compact_fiber)
    temporal_orientation = bool(open_interval)
    gsc6b_input = bool(proper_real_clock and temporal_orientation)

    gh = bool(
        gsc6b_input
        and rf_e25_global_lorentzian_adm_carrier
        and smooth_finite_positive_lapse
    )

    return CompactFiberProperClockRoute(
        open_interval_clock_derived=open_interval,
        compact_spatial_fiber_admitted=compact_fiber,
        proper_real_clock_derived=proper_real_clock,
        temporal_orientation_preserved=temporal_orientation,
        gsc6b_proper_clock_input_derived=gsc6b_input,
        global_hyperbolicity_eligible=gh,
        global_gr_cauchy_carrier_eligible=bool(gh and global_einstein_carrier),
    )
