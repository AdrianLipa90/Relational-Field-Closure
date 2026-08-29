from __future__ import annotations

import math
from collections.abc import Sequence


class NoetherShannonRadialBindingError(ValueError):
    pass


def _finite(name: str, value: float) -> float:
    value = float(value)
    if not math.isfinite(value):
        raise NoetherShannonRadialBindingError(f"{name} must be finite")
    return value


def _positive(name: str, value: float) -> float:
    value = _finite(name, value)
    if value <= 0.0:
        raise NoetherShannonRadialBindingError(f"{name} must be positive")
    return value


def _nonnegative(name: str, value: float) -> float:
    value = _finite(name, value)
    if value < 0.0:
        raise NoetherShannonRadialBindingError(f"{name} must be nonnegative")
    return value


def _probability_vector(
    name: str,
    values: Sequence[float],
    *,
    strictly_positive: bool,
) -> tuple[float, ...]:
    if not values:
        raise NoetherShannonRadialBindingError(f"{name} must be nonempty")

    out = tuple(_finite(f"{name}[{i}]", value) for i, value in enumerate(values))
    if strictly_positive:
        if any(value <= 0.0 for value in out):
            raise NoetherShannonRadialBindingError(
                f"{name} entries must be positive"
            )
    elif any(value < 0.0 for value in out):
        raise NoetherShannonRadialBindingError(
            f"{name} entries must be nonnegative"
        )

    total = math.fsum(out)
    if not math.isclose(total, 1.0, rel_tol=0.0, abs_tol=1.0e-12):
        raise NoetherShannonRadialBindingError(
            f"{name} must sum to one"
        )
    return out


def shannon_relative_information_nats(
    p: Sequence[float],
    pi: Sequence[float],
) -> float:
    p_vec = _probability_vector("p", p, strictly_positive=False)
    pi_vec = _probability_vector("pi", pi, strictly_positive=True)
    if len(p_vec) != len(pi_vec):
        raise NoetherShannonRadialBindingError(
            "p and pi must have the same length"
        )

    value = math.fsum(
        p_a * math.log(p_a / pi_a)
        for p_a, pi_a in zip(p_vec, pi_vec)
        if p_a > 0.0
    )
    if value < -1.0e-13:
        raise NoetherShannonRadialBindingError(
            "KL relative information became negative"
        )
    return max(0.0, value)


def fisher_radial_norm_sq(
    p: Sequence[float],
    pi: Sequence[float],
) -> float:
    p_vec = _probability_vector("p", p, strictly_positive=False)
    pi_vec = _probability_vector("pi", pi, strictly_positive=True)
    if len(p_vec) != len(pi_vec):
        raise NoetherShannonRadialBindingError(
            "p and pi must have the same length"
        )
    return math.fsum(
        (p_a - pi_a) ** 2 / pi_a
        for p_a, pi_a in zip(p_vec, pi_vec)
    )


def baseline_adjusted_information(
    j_pi: float,
    area_rel: float,
    xi_star: float = 0.0,
) -> float:
    j_pi = _nonnegative("j_pi", j_pi)
    area_rel = _positive("area_rel", area_rel)
    xi_star = _nonnegative("xi_star", xi_star)
    value = j_pi - xi_star * area_rel
    if value < -1.0e-13:
        raise NoetherShannonRadialBindingError(
            "baseline-adjusted information must be nonnegative"
        )
    return max(0.0, value)


def shannon_radial_curvature(
    j_pi: float,
    area_rel: float,
    xi_star: float = 0.0,
) -> float:
    area_rel = _positive("area_rel", area_rel)
    return baseline_adjusted_information(j_pi, area_rel, xi_star) / area_rel


def noether_radial_amplitude_sq(
    j_vartheta: float,
    r_s: float,
) -> float:
    j_vartheta = _positive("j_vartheta", j_vartheta)
    r_s = _positive("r_s", r_s)
    return j_vartheta / (2.0 * r_s)


def source_binding_residual(
    j_pi: float,
    area_rel: float,
    xi_star: float,
    j_vartheta: float,
    r_s: float,
) -> float:
    area_rel = _positive("area_rel", area_rel)
    j_vartheta = _positive("j_vartheta", j_vartheta)
    r_s = _positive("r_s", r_s)
    j_bar = baseline_adjusted_information(j_pi, area_rel, xi_star)
    return area_rel * j_vartheta - 2.0 * r_s * j_bar


def stationary_zero_baseline_residual(
    j_pi: float,
    area_rel: float,
    j_vartheta: float,
    r_s: float,
) -> float:
    return source_binding_residual(
        j_pi,
        area_rel,
        0.0,
        j_vartheta,
        r_s,
    )


def source_binding_defect(
    j_pi: float,
    area_rel: float,
    xi_star: float,
    j_vartheta: float,
    r_s: float,
) -> float:
    xi_shannon = shannon_radial_curvature(j_pi, area_rel, xi_star)
    a2_noether = noether_radial_amplitude_sq(j_vartheta, r_s)
    denom = xi_shannon + a2_noether
    if denom <= 0.0:
        raise NoetherShannonRadialBindingError(
            "source-binding defect requires nondegenerate support"
        )
    return abs(a2_noether - xi_shannon) / denom


def source_binding_defect_product_form(
    j_pi: float,
    area_rel: float,
    xi_star: float,
    j_vartheta: float,
    r_s: float,
) -> float:
    area_rel = _positive("area_rel", area_rel)
    j_vartheta = _positive("j_vartheta", j_vartheta)
    r_s = _positive("r_s", r_s)
    j_bar = baseline_adjusted_information(j_pi, area_rel, xi_star)
    left = area_rel * j_vartheta
    right = 2.0 * r_s * j_bar
    denom = left + right
    if denom <= 0.0:
        raise NoetherShannonRadialBindingError(
            "product-form defect requires nondegenerate support"
        )
    return abs(left - right) / denom


def source_binding_ratio(
    j_pi: float,
    area_rel: float,
    xi_star: float,
    j_vartheta: float,
    r_s: float,
) -> float:
    area_rel = _positive("area_rel", area_rel)
    j_vartheta = _positive("j_vartheta", j_vartheta)
    r_s = _positive("r_s", r_s)
    j_bar = baseline_adjusted_information(j_pi, area_rel, xi_star)
    if j_bar <= 0.0:
        raise NoetherShannonRadialBindingError(
            "source-binding ratio requires positive Shannon radial support"
        )
    return area_rel * j_vartheta / (2.0 * r_s * j_bar)


def local_fisher_quadratic_curvature(
    s_f_sq: float,
    area_star: float,
) -> float:
    s_f_sq = _nonnegative("s_f_sq", s_f_sq)
    area_star = _positive("area_star", area_star)
    return s_f_sq / (2.0 * area_star)


def local_fisher_residual(
    s_f_sq: float,
    area_star: float,
    j_vartheta: float,
    r_s: float,
) -> float:
    s_f_sq = _nonnegative("s_f_sq", s_f_sq)
    area_star = _positive("area_star", area_star)
    j_vartheta = _positive("j_vartheta", j_vartheta)
    r_s = _positive("r_s", r_s)
    return area_star * j_vartheta - r_s * s_f_sq
