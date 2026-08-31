from __future__ import annotations

from dataclasses import dataclass
from math import exp, isfinite, log

from src.rfc.proper_temporal_clock_global_hyperbolicity import (
    ProperClockRoute,
    certify_proper_clock_route,
)


@dataclass(frozen=True)
class OpenInterval:
    """A nonempty open interval with ``None`` representing an infinite endpoint."""

    left: float | None = None
    right: float | None = None

    def __post_init__(self) -> None:
        if self.left is not None and not isfinite(float(self.left)):
            raise ValueError("left endpoint must be finite or None")
        if self.right is not None and not isfinite(float(self.right)):
            raise ValueError("right endpoint must be finite or None")
        if self.left is not None and self.right is not None:
            if not float(self.left) < float(self.right):
                raise ValueError("open interval must satisfy left < right")

    @property
    def kind(self) -> str:
        if self.left is None and self.right is None:
            return "REAL_LINE"
        if self.left is not None and self.right is None:
            return "RIGHT_HALF_LINE"
        if self.left is None and self.right is not None:
            return "LEFT_HALF_LINE"
        return "BOUNDED_OPEN_INTERVAL"

    def contains(self, x: float) -> bool:
        value = float(x)
        if not isfinite(value):
            return False
        if self.left is not None and not value > float(self.left):
            return False
        if self.right is not None and not value < float(self.right):
            return False
        return True

    def to_real(self, x: float) -> float:
        """Canonical orientation-preserving diffeomorphism ``psi:I->R``."""

        value = float(x)
        if not self.contains(value):
            raise ValueError("x must lie in the open interval")

        if self.left is None and self.right is None:
            return value
        if self.left is not None and self.right is None:
            return log(value - float(self.left))
        if self.left is None and self.right is not None:
            return -log(float(self.right) - value)

        left = float(self.left)
        right = float(self.right)
        return log((value - left) / (right - value))

    def derivative(self, x: float) -> float:
        """Derivative of the canonical ``psi``; it is strictly positive on ``I``."""

        value = float(x)
        if not self.contains(value):
            raise ValueError("x must lie in the open interval")

        if self.left is None and self.right is None:
            return 1.0
        if self.left is not None and self.right is None:
            return 1.0 / (value - float(self.left))
        if self.left is None and self.right is not None:
            return 1.0 / (float(self.right) - value)

        left = float(self.left)
        right = float(self.right)
        return 1.0 / (value - left) + 1.0 / (right - value)

    def from_real(self, y: float) -> float:
        """Inverse of the canonical orientation-preserving diffeomorphism."""

        value = float(y)
        if not isfinite(value):
            raise ValueError("y must be finite")

        if self.left is None and self.right is None:
            return value
        if self.left is not None and self.right is None:
            return float(self.left) + exp(value)
        if self.left is None and self.right is not None:
            return float(self.right) - exp(-value)

        left = float(self.left)
        right = float(self.right)
        ey = exp(value)
        return (left + right * ey) / (1.0 + ey)


@dataclass(frozen=True)
class OpenIntervalProductRoute:
    interval_kind: str
    finite_a5_spatial_carrier: bool
    a5_closed_3manifold_certified: bool
    compact_spatial_fiber_derived: bool
    global_product_trivialization: bool
    orientation_preserving_interval_diffeomorphism_derived: bool
    proper_real_temporal_clock_derived: bool
    proper_clock_route: ProperClockRoute

    @property
    def global_hyperbolicity_eligible(self) -> bool:
        return self.proper_clock_route.global_hyperbolicity_eligible

    @property
    def global_gr_cauchy_carrier_eligible(self) -> bool:
        return self.proper_clock_route.global_gr_cauchy_carrier_eligible


def certify_open_interval_product_route(
    *,
    interval: OpenInterval,
    finite_a5_spatial_carrier: bool,
    a5_closed_3manifold_certified: bool,
    global_product_trivialization: bool,
    global_regular_product_clock: bool,
    global_lorentzian_carrier: bool,
    smooth_finite_positive_lapse: bool,
    global_einstein_carrier: bool = False,
) -> OpenIntervalProductRoute:
    """Compose the finite-A5 + open-interval product route with RF-GSC6B.

    A finite A5-certified simplicial realization has compact geometric realization.
    For a global product ``M=I x Sigma`` with compact ``Sigma``, projection to ``I``
    is proper. Every nonempty open interval is orientation-preserving diffeomorphic
    to ``R``; composition with that diffeomorphism gives a proper real-valued
    temporal clock. The remaining hyperbolicity implications are delegated to
    the existing RF-GSC6B certifier.
    """

    compact_sigma = bool(finite_a5_spatial_carrier and a5_closed_3manifold_certified)
    interval_diffeomorphism = True  # guaranteed constructively by OpenInterval
    proper_real_clock = bool(
        compact_sigma
        and global_product_trivialization
        and global_regular_product_clock
        and interval_diffeomorphism
    )

    proper_route = certify_proper_clock_route(
        global_lorentzian_carrier=global_lorentzian_carrier,
        global_regular_temporal_clock=global_regular_product_clock,
        proper_temporal_clock_to_real_line=proper_real_clock,
        smooth_finite_positive_lapse=smooth_finite_positive_lapse,
        global_einstein_carrier=global_einstein_carrier,
    )

    return OpenIntervalProductRoute(
        interval_kind=interval.kind,
        finite_a5_spatial_carrier=bool(finite_a5_spatial_carrier),
        a5_closed_3manifold_certified=bool(a5_closed_3manifold_certified),
        compact_spatial_fiber_derived=compact_sigma,
        global_product_trivialization=bool(global_product_trivialization),
        orientation_preserving_interval_diffeomorphism_derived=interval_diffeomorphism,
        proper_real_temporal_clock_derived=proper_real_clock,
        proper_clock_route=proper_route,
    )
