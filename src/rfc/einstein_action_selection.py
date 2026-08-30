"""RF-E21: conditional 4D Einstein-action selection helpers.

The mathematical uniqueness theorem is an external theorem-level parent
(4D Lovelock). This module validates the declared admissibility surface,
source/support ownership, exact coefficient transfer, and the deliberately
small project-native promotion frontier.
"""
from __future__ import annotations

from dataclasses import dataclass
import math


class EinsteinActionSelectionError(ValueError):
    pass


SUPPORT_SURFACES = (
    "RF-F13:COVARIANT_COMMON_ACTION_ARCHITECTURE",
    "RFG18:LINEARIZED_DIFFEO_WARD",
    "RFG20:FOUR_POINT_EINSTEIN_MHV_NORMALIZATION",
    "RFG27:FIVE_POINT_NORMALIZATION_FIREWALL",
    "RFG29:FIVE_POINT_BCJ_ROOT_VALIDATION",
    "RFG30:FIVE_POINT_PRE_KLT_CLOSURE",
    "RF-F25:REDUCED_GRAVITY_UNIVERSALITY_COORDINATE",
    "RF-F26:PROJECT_COUPLING_PROMOTION_FIREWALL",
)

NATIVE_FRONTIER = (
    "NONLINEAR_ALL_ORDERS_GRAVITATIONAL_COVARIANCE_PROMOTION",
    "NATIVE_LOCAL_SECOND_ORDER_METRIC_GRAVITY_SELECTION",
    "REALIZED_INDEPENDENT_REDUCED_GRAVITY_UNIVERSALITY_ADMISSION",
)


@dataclass(frozen=True)
class Admissibility:
    spacetime_dimension: int
    lorentzian_metric: bool
    diffeomorphism_covariant: bool
    metric_local_bulk: bool
    second_order_metric_equations: bool

    @property
    def lovelock_4d_ready(self) -> bool:
        return (
            self.spacetime_dimension == 4
            and self.lorentzian_metric
            and self.diffeomorphism_covariant
            and self.metric_local_bulk
            and self.second_order_metric_equations
        )


def selected_bulk_basis(admissibility: Admissibility) -> tuple[str, ...]:
    """Return the 4D Lovelock bulk basis affecting local metric equations.

    Gauss-Bonnet/Euler and boundary densities may remain in the action ledger,
    but carry no additional local 4D metric equation under this conditional
    gate.
    """
    if not admissibility.lovelock_4d_ready:
        raise EinsteinActionSelectionError(
            "RF-E21 action selection requires the complete 4D Lovelock admissibility surface"
        )
    return ("cosmological_density", "ricci_scalar")


def support_surface_names() -> tuple[str, ...]:
    return SUPPORT_SURFACES


def native_promotion_frontier() -> tuple[str, ...]:
    return NATIVE_FRONTIER


def conditional_gr_closure_ready(
    admissibility: Admissibility,
    *,
    rf_e3_normalization: bool,
    rf_e12_e13_adm_dynamics: bool,
) -> bool:
    """Conditional closure requires explicit admissibility, normalization, and ADM parents."""
    return (
        admissibility.lovelock_4d_ready
        and rf_e3_normalization
        and rf_e12_e13_adm_dynamics
    )


def eh_action_prefactor_si(G: float, c: float) -> float:
    """A = c^4/(16 pi G), so S_g = A integral sqrt(-g) (R-2 Lambda)."""
    if not (math.isfinite(G) and G > 0.0 and math.isfinite(c) and c > 0.0):
        raise EinsteinActionSelectionError("G and c must be finite and positive")
    return c**4 / (16.0 * math.pi * G)


def einstein_coupling_from_prefactor(prefactor: float) -> float:
    """Metric variation with T=-2/sqrt(-g) delta S_m/delta g gives kappa_E=1/(2A)."""
    if not (math.isfinite(prefactor) and prefactor > 0.0):
        raise EinsteinActionSelectionError("action prefactor must be finite and positive")
    return 1.0 / (2.0 * prefactor)


def einstein_coupling_si(G: float, c: float) -> float:
    if not (math.isfinite(G) and G > 0.0 and math.isfinite(c) and c > 0.0):
        raise EinsteinActionSelectionError("G and c must be finite and positive")
    return 8.0 * math.pi * G / c**4


def coupling_closure_ratio(G: float, c: float) -> float:
    A = eh_action_prefactor_si(G, c)
    return einstein_coupling_from_prefactor(A) / einstein_coupling_si(G, c)


def lorentz_signature(spatial_rank: int, temporal_rank: int = 1) -> tuple[int, ...]:
    if spatial_rank < 0 or temporal_rank < 0:
        raise EinsteinActionSelectionError("ranks must be nonnegative")
    return (-1,) * temporal_rank + (1,) * spatial_rank


def source_bound_3plus1_ready(spatial_rank: int, temporal_rank: int, positive_lapse: bool) -> bool:
    return spatial_rank == 3 and temporal_rank == 1 and positive_lapse
