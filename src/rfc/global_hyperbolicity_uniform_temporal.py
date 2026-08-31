"""RF-L8 completely-uniform relational-clock global-hyperbolicity gate.

For the ADM metric

    g = -N^2 dt^2 + h_ij (dx^i + b^i dt)(dx^j + b^j dt),

a future causal vector v with a = dt(v) > 0 and shifted spatial norm
q = h(Y,Y) obeys q <= N^2 a^2.  The Wick metric

    W = dt^2 + h_ij (dx^i + b^i dt)(dx^j + b^j dt)

therefore satisfies W(v,v) <= (1 + N_max^2) a^2 when a certified global
lapse bound N <= N_max is supplied.  With epsilon = 1/sqrt(1+N_max^2),
H = epsilon^2 W gives dt(v) >= ||v||_H.

Global hyperbolicity is promoted only when the global carrier, regular clock,
certified lapse bound, and Wick-metric completeness witness are all supplied.
The imported Bernard-Suhr/Minguzzi theorem is typed in the RF-L8 external
theorem ledger; this module does not infer completeness from finite samples.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import isfinite, sqrt


class GlobalHyperbolicityWitnessError(ValueError):
    """Raised when a declared RF-L8 witness leaves its mathematical domain."""


def _positive_finite(value: float, label: str) -> float:
    out = float(value)
    if not isfinite(out) or out <= 0.0:
        raise GlobalHyperbolicityWitnessError(f"{label} must be finite and strictly positive")
    return out


def _nonnegative_finite(value: float, label: str) -> float:
    out = float(value)
    if not isfinite(out) or out < 0.0:
        raise GlobalHyperbolicityWitnessError(f"{label} must be finite and non-negative")
    return out


def uniform_temporal_scale(lapse_upper_bound: float) -> float:
    """Return epsilon=(1+N_max^2)^(-1/2)."""

    nmax = _positive_finite(lapse_upper_bound, "lapse_upper_bound")
    return 1.0 / sqrt(1.0 + nmax * nmax)


@dataclass(frozen=True)
class CausalSteepnessCertificate:
    lapse: float
    lapse_upper_bound: float
    dt_component: float
    shifted_spatial_norm_sq: float
    causal_margin: float
    wick_norm_sq: float
    scaled_wick_norm: float
    steepness_margin: float
    epsilon: float
    future_directed: bool
    causal: bool
    steepness_pass: bool


def certify_causal_vector_steepness(
    *,
    lapse: float,
    lapse_upper_bound: float,
    dt_component: float,
    shifted_spatial_norm_sq: float,
    atol: float = 1.0e-12,
) -> CausalSteepnessCertificate:
    """Certify the RF-L8 ADM steepness inequality for one declared causal vector.

    ``shifted_spatial_norm_sq`` is h(Y,Y) with Y=X+b*dt(v).  It must already
    be evaluated using the positive spatial metric.  The function fails closed
    if the vector is not future-directed causal or if the local lapse exceeds
    the declared global bound.
    """

    n = _positive_finite(lapse, "lapse")
    nmax = _positive_finite(lapse_upper_bound, "lapse_upper_bound")
    a = _positive_finite(dt_component, "dt_component")
    q = _nonnegative_finite(shifted_spatial_norm_sq, "shifted_spatial_norm_sq")
    tol = _nonnegative_finite(atol, "atol")

    if n > nmax + tol * (1.0 + max(abs(n), abs(nmax))):
        raise GlobalHyperbolicityWitnessError("local lapse exceeds declared global upper bound")

    causal_limit = n * n * a * a
    causal_margin = causal_limit - q
    if causal_margin < -tol * (1.0 + causal_limit + q):
        raise GlobalHyperbolicityWitnessError(
            "declared vector violates ADM causal inequality h(Y,Y) <= N^2 dt(v)^2"
        )

    wick_sq = a * a + q
    epsilon = uniform_temporal_scale(nmax)
    scaled_norm = epsilon * sqrt(wick_sq)
    steep_margin = a - scaled_norm
    if steep_margin < -tol * (1.0 + a + scaled_norm):
        raise GlobalHyperbolicityWitnessError("derived completely-uniform steepness inequality failed")

    return CausalSteepnessCertificate(
        lapse=n,
        lapse_upper_bound=nmax,
        dt_component=a,
        shifted_spatial_norm_sq=q,
        causal_margin=causal_margin,
        wick_norm_sq=wick_sq,
        scaled_wick_norm=scaled_norm,
        steepness_margin=steep_margin,
        epsilon=epsilon,
        future_directed=True,
        causal=True,
        steepness_pass=True,
    )


@dataclass(frozen=True)
class GlobalHyperbolicityCertificate:
    lapse_upper_bound: float
    epsilon: float
    global_lorentzian_carrier_supplied: bool
    global_regular_clock_supplied: bool
    global_lapse_upper_bound_certified: bool
    wick_metric_complete_supplied: bool
    completely_uniform_temporal: bool
    global_hyperbolicity: bool
    cauchy_foliation: bool
    global_einstein_carrier_supplied: bool
    global_gr_cauchy_carrier: bool
    theorem_authority: str = "BERNARD_SUHR_COMPLETELY_UNIFORM_TEMPORAL"
    nonlinear_global_stability: str = "OPEN_SEPARATE_GATE"


def certify_global_hyperbolicity(
    lapse_upper_bound: float,
    *,
    global_lorentzian_carrier_supplied: bool = False,
    global_regular_clock_supplied: bool = False,
    global_lapse_upper_bound_certified: bool = False,
    wick_metric_complete_supplied: bool = False,
    global_einstein_carrier_supplied: bool = False,
) -> GlobalHyperbolicityCertificate:
    """Compose the RF-L8 proof-carrying global-hyperbolicity promotion gate.

    The numerical value of ``lapse_upper_bound`` defines the exact steepness
    scale, but global promotion also requires an explicit certification that it
    is a bound on the entire target domain.  Likewise Wick completeness is an
    independent global analytic/topological input and is never inferred here.
    """

    nmax = _positive_finite(lapse_upper_bound, "lapse_upper_bound")
    epsilon = uniform_temporal_scale(nmax)

    carrier = bool(global_lorentzian_carrier_supplied)
    clock = bool(global_regular_clock_supplied)
    bound = bool(global_lapse_upper_bound_certified)
    complete = bool(wick_metric_complete_supplied)
    einstein = bool(global_einstein_carrier_supplied)

    completely_uniform = carrier and clock and bound and complete
    globally_hyperbolic = completely_uniform
    cauchy = globally_hyperbolic
    gr_cauchy = globally_hyperbolic and einstein

    return GlobalHyperbolicityCertificate(
        lapse_upper_bound=nmax,
        epsilon=epsilon,
        global_lorentzian_carrier_supplied=carrier,
        global_regular_clock_supplied=clock,
        global_lapse_upper_bound_certified=bound,
        wick_metric_complete_supplied=complete,
        completely_uniform_temporal=completely_uniform,
        global_hyperbolicity=globally_hyperbolic,
        cauchy_foliation=cauchy,
        global_einstein_carrier_supplied=einstein,
        global_gr_cauchy_carrier=gr_cauchy,
    )
