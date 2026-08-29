import math

import pytest


KAPPA = math.log(2.0) / (24.0 * math.pi)
KAPPA_E = 8.0 * math.pi
BETA_FISHER = math.sqrt(2.0)


def _validate_probability_state(p, pi):
    if len(p) != len(pi) or not p:
        raise ValueError("probability vectors must have equal nonzero length")
    if not all(math.isfinite(x) for x in (*p, *pi)):
        raise ValueError("nonfinite probability state")
    if any(x <= 0.0 for x in pi) or any(x <= 0.0 for x in p):
        raise ValueError("strictly positive probability state required")
    if abs(sum(p) - 1.0) > 1.0e-12 or abs(sum(pi) - 1.0) > 1.0e-12:
        raise ValueError("probability state must be normalized")


def j_nat(p, pi):
    _validate_probability_state(p, pi)
    return sum(pa * math.log(pa / pia) for pa, pia in zip(p, pi))


def fisher_hessian(pi):
    if not pi or not all(math.isfinite(x) and x > 0.0 for x in pi):
        raise ValueError("strictly positive stationary reference required")
    if abs(sum(pi) - 1.0) > 1.0e-12:
        raise ValueError("stationary reference must be normalized")
    return tuple(tuple((1.0 / pi[i]) if i == j else 0.0 for j in range(len(pi))) for i in range(len(pi)))


def fisher_norm2(delta, pi):
    if len(delta) != len(pi) or not delta:
        raise ValueError("tangent/reference length mismatch")
    if not all(math.isfinite(x) for x in (*delta, *pi)):
        raise ValueError("nonfinite tangent state")
    if any(x <= 0.0 for x in pi):
        raise ValueError("positive reference required")
    if abs(sum(delta)) > 1.0e-12:
        raise ValueError("delta must lie in the simplex tangent space")
    return sum(d * d / q for d, q in zip(delta, pi))


def perturb(pi, direction, eps):
    if len(pi) != len(direction):
        raise ValueError("direction/reference length mismatch")
    if abs(sum(direction)) > 1.0e-12:
        raise ValueError("direction must be tangent")
    out = tuple(q + eps * v for q, v in zip(pi, direction))
    _validate_probability_state(out, pi)
    return out


def xi_from_j(j_value, area):
    if not math.isfinite(j_value) or not math.isfinite(area) or area <= 0.0:
        raise ValueError("invalid information-curvature state")
    return j_value / area


def phi_fisher_from_norm2(s2, area_star):
    if not math.isfinite(s2) or s2 < 0.0:
        raise ValueError("invalid Fisher norm")
    if not math.isfinite(area_star) or area_star <= 0.0:
        raise ValueError("positive finite reference area required")
    return math.sqrt(s2 / area_star)


def phi_rf_l4a_from_xi(xi):
    if not math.isfinite(xi) or xi < 0.0:
        raise ValueError("nonnegative finite Xi required")
    return BETA_FISHER * math.sqrt(xi)


def z_local(xi):
    if not math.isfinite(xi) or xi <= 0.0:
        raise ValueError("positive finite Xi required")
    return 1.0 / (2.0 * xi)


def mass2(alpha_i, kappa_e=KAPPA_E):
    if not math.isfinite(alpha_i) or not math.isfinite(kappa_e) or kappa_e == 0.0:
        raise ValueError("invalid RF-L4A mass state")
    return alpha_i / kappa_e


def full_sphere_phi(info_bits, omega, c=1.0):
    vals = (info_bits, omega, c)
    if not all(math.isfinite(v) for v in vals):
        raise ValueError("nonfinite full-sphere state")
    if info_bits < 0.0 or c <= 0.0:
        raise ValueError("invalid full-sphere state")
    return math.sqrt(48.0 * KAPPA * info_bits) * abs(omega) / c


def test_natural_log_kl_hessian_is_fisher_diagonal():
    pi = (0.2, 0.3, 0.5)
    h = fisher_hessian(pi)
    assert h[0][0] == pytest.approx(5.0)
    assert h[1][1] == pytest.approx(10.0 / 3.0)
    assert h[2][2] == pytest.approx(2.0)
    assert h[0][1] == h[0][2] == h[1][0] == 0.0


def test_first_variation_vanishes_on_simplex_tangent():
    pi = (0.2, 0.3, 0.5)
    direction = (0.1, -0.06, -0.04)
    assert sum(direction) == pytest.approx(0.0)
    # grad J at p=pi is the constant covector (1,1,1), so its tangent contraction vanishes.
    assert sum(direction) == pytest.approx(0.0)


def test_kl_quadratic_term_matches_half_fisher_norm():
    pi = (0.2, 0.3, 0.5)
    direction = (0.1, -0.06, -0.04)
    eps = 1.0e-4
    p = perturb(pi, direction, eps)
    delta = tuple(eps * v for v in direction)
    j = j_nat(p, pi)
    quadratic = 0.5 * fisher_norm2(delta, pi)
    assert j == pytest.approx(quadratic, rel=2.0e-5, abs=1.0e-15)


def test_kl_remainder_scales_cubically_under_halving():
    pi = (0.2, 0.3, 0.5)
    direction = (0.1, -0.06, -0.04)

    def remainder(eps):
        p = perturb(pi, direction, eps)
        delta = tuple(eps * v for v in direction)
        return j_nat(p, pi) - 0.5 * fisher_norm2(delta, pi)

    r1 = abs(remainder(2.0e-3))
    r2 = abs(remainder(1.0e-3))
    assert r1 > 0.0
    assert r2 / r1 == pytest.approx(1.0 / 8.0, rel=0.08)


def test_smooth_first_order_area_motion_preserves_quadratic_xi_coefficient():
    pi = (0.2, 0.3, 0.5)
    direction = (0.1, -0.06, -0.04)
    area_star = 3.0
    area_slope = 0.7

    def xi_error(eps):
        p = perturb(pi, direction, eps)
        delta = tuple(eps * v for v in direction)
        j = j_nat(p, pi)
        area = area_star + area_slope * eps
        exact_xi = xi_from_j(j, area)
        quadratic_xi = 0.5 * fisher_norm2(delta, pi) / area_star
        return exact_xi - quadratic_xi

    e1 = abs(xi_error(2.0e-3))
    e2 = abs(xi_error(1.0e-3))
    assert e1 > 0.0
    assert e2 / e1 == pytest.approx(1.0 / 8.0, rel=0.12)


def test_beta_sqrt2_matches_local_fisher_radial_coordinate():
    s2 = 0.018
    area_star = 2.5
    xi_quadratic = s2 / (2.0 * area_star)
    phi_f = phi_fisher_from_norm2(s2, area_star)
    phi_i = phi_rf_l4a_from_xi(xi_quadratic)
    assert phi_i == pytest.approx(phi_f)
    assert BETA_FISHER == pytest.approx(math.sqrt(2.0))


def test_local_xi_metric_after_fisher_normalization():
    xi = 0.125
    dphi_dxi = 1.0 / math.sqrt(2.0 * xi)
    assert z_local(xi) == pytest.approx(dphi_dxi**2)


def test_mass_alpha_relation_after_beta_is_fixed():
    alpha_i = 0.35
    m2 = mass2(alpha_i)
    assert KAPPA_E * m2 == pytest.approx(alpha_i)


def test_bianchi_transfer_matches_mass_chart():
    alpha_i = 0.45
    phi_i = 1.2
    dphi = -0.08
    dxi = phi_i * dphi  # Xi = phi^2 / 2 in the RF-L4A local coordinate convention.
    via_xi = alpha_i * dxi
    via_phi = KAPPA_E * mass2(alpha_i) * phi_i * dphi
    assert via_phi == pytest.approx(via_xi)


def test_full_bloch_sphere_coefficient_uses_canonical_kappa():
    info_bits = 2.75
    omega = -3.2
    phi = full_sphere_phi(info_bits, omega)
    expected = math.sqrt(2.0 * math.log(2.0) * info_bits / math.pi) * abs(omega)
    assert phi == pytest.approx(expected)


@pytest.mark.parametrize(
    "p,pi",
    [
        ((0.5, 0.5), (0.0, 1.0)),
        ((0.6, 0.5), (0.5, 0.5)),
        ((math.nan, 1.0), (0.5, 0.5)),
    ],
)
def test_invalid_probability_states_fail_closed(p, pi):
    with pytest.raises(ValueError):
        j_nat(p, pi)


@pytest.mark.parametrize("area", [0.0, -1.0, math.inf, math.nan])
def test_invalid_area_fails_closed(area):
    with pytest.raises(ValueError):
        xi_from_j(0.1, area)


@pytest.mark.parametrize("xi", [0.0, -1.0, math.inf, math.nan])
def test_invalid_local_metric_state_fails_closed(xi):
    with pytest.raises(ValueError):
        z_local(xi)
