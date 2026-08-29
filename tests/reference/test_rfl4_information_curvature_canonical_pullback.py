import math

import pytest


KAPPA = math.log(2.0) / (24.0 * math.pi)
KAPPA_E = 8.0 * math.pi


def dynamic_xi(xi_i: float, xi_star: float) -> float:
    vals = (xi_i, xi_star)
    if not all(math.isfinite(v) for v in vals):
        raise ValueError("nonfinite RF-L4 state")
    out = xi_i - xi_star
    if out < 0.0:
        raise ValueError("Xi_I below admitted baseline")
    return out


def phi_from_xi(xi_i: float, xi_star: float = 0.0, beta_i: float = 1.0) -> float:
    if not math.isfinite(beta_i) or beta_i <= 0.0:
        raise ValueError("beta_I must be finite and positive")
    return beta_i * math.sqrt(dynamic_xi(xi_i, xi_star))


def xi_from_phi(phi_i: float, xi_star: float = 0.0, beta_i: float = 1.0) -> float:
    vals = (phi_i, xi_star, beta_i)
    if not all(math.isfinite(v) for v in vals):
        raise ValueError("nonfinite RF-L4 state")
    if beta_i <= 0.0:
        raise ValueError("beta_I must be positive")
    return xi_star + (phi_i / beta_i) ** 2


def lambda_star(lambda_ref: float, alpha_i: float, xi_star: float) -> float:
    vals = (lambda_ref, alpha_i, xi_star)
    if not all(math.isfinite(v) for v in vals):
        raise ValueError("nonfinite RF-L4 state")
    return lambda_ref + alpha_i * xi_star


def lambda0_xi(lambda_ref: float, alpha_i: float, xi_i: float) -> float:
    vals = (lambda_ref, alpha_i, xi_i)
    if not all(math.isfinite(v) for v in vals):
        raise ValueError("nonfinite RF-L4 state")
    return lambda_ref + alpha_i * xi_i


def lambda0_phi(lambda_ref: float, alpha_i: float, xi_star: float, phi_i: float, beta_i: float) -> float:
    return lambda_star(lambda_ref, alpha_i, xi_star) + alpha_i * phi_i**2 / beta_i**2


def potential_phi(phi_i: float, alpha_i: float, beta_i: float = 1.0, kappa_e: float = KAPPA_E) -> float:
    vals = (phi_i, alpha_i, beta_i, kappa_e)
    if not all(math.isfinite(v) for v in vals):
        raise ValueError("nonfinite RF-L4 state")
    if beta_i <= 0.0 or kappa_e == 0.0:
        raise ValueError("invalid RF-L4 normalization")
    return alpha_i * phi_i**2 / (kappa_e * beta_i**2)


def mass2(alpha_i: float, beta_i: float = 1.0, kappa_e: float = KAPPA_E) -> float:
    vals = (alpha_i, beta_i, kappa_e)
    if not all(math.isfinite(v) for v in vals):
        raise ValueError("nonfinite RF-L4 state")
    if beta_i <= 0.0 or kappa_e == 0.0:
        raise ValueError("invalid RF-L4 normalization")
    return 2.0 * alpha_i / (kappa_e * beta_i**2)


def kinetic_metric_xi(xi_i: float, xi_star: float = 0.0, beta_i: float = 1.0) -> float:
    bar = dynamic_xi(xi_i, xi_star)
    if bar == 0.0:
        raise ValueError("Xi chart boundary; use regular phi chart")
    if not math.isfinite(beta_i) or beta_i <= 0.0:
        raise ValueError("beta_I must be finite and positive")
    return beta_i**2 / (4.0 * bar)


def bloch_sphere_xi(info_bits: float, omega: float, c: float = 1.0) -> float:
    vals = (info_bits, omega, c)
    if not all(math.isfinite(v) for v in vals):
        raise ValueError("nonfinite IDT specialization")
    if info_bits < 0.0 or c <= 0.0:
        raise ValueError("invalid IDT specialization")
    return 24.0 * KAPPA * info_bits * (omega / c) ** 2


@pytest.mark.parametrize(
    "xi_i,xi_star,beta_i",
    [(4.0, 0.0, 1.0), (9.5, 0.5, 2.0), (1.0e-8, 0.0, 0.25)],
)
def test_square_root_coordinate_roundtrip(xi_i, xi_star, beta_i):
    phi_i = phi_from_xi(xi_i, xi_star, beta_i)
    assert xi_from_phi(phi_i, xi_star, beta_i) == pytest.approx(xi_i)


def test_baseline_shift_preserves_lambda0_exactly():
    lambda_ref = 3.0
    alpha_i = 0.4
    xi_star = 2.0
    xi_i = 7.0
    phi_i = phi_from_xi(xi_i, xi_star, 1.5)
    assert lambda0_phi(lambda_ref, alpha_i, xi_star, phi_i, 1.5) == pytest.approx(
        lambda0_xi(lambda_ref, alpha_i, xi_i)
    )


def test_quadratic_potential_matches_mass_parameterization():
    phi_i = 1.75
    alpha_i = 0.3
    beta_i = 1.2
    m2 = mass2(alpha_i, beta_i)
    assert potential_phi(phi_i, alpha_i, beta_i) == pytest.approx(0.5 * m2 * phi_i**2)


def test_alpha_mass_relation_roundtrip():
    alpha_i = 0.7
    beta_i = 1.3
    m2 = mass2(alpha_i, beta_i)
    recovered_alpha = 0.5 * KAPPA_E * beta_i**2 * m2
    assert recovered_alpha == pytest.approx(alpha_i)


def test_kinetic_jacobian_matches_direct_derivative():
    xi_i = 5.0
    xi_star = 1.0
    beta_i = 2.0
    bar = xi_i - xi_star
    dphi_dxi = beta_i / (2.0 * math.sqrt(bar))
    assert kinetic_metric_xi(xi_i, xi_star, beta_i) == pytest.approx(dphi_dxi**2)


def test_bianchi_transfer_same_in_xi_and_phi_charts():
    alpha_i = 0.25
    beta_i = 1.4
    phi_i = 2.0
    dphi = -0.3
    dxi = 2.0 * phi_i * dphi / beta_i**2
    via_xi = alpha_i * dxi
    via_phi = 2.0 * alpha_i * phi_i * dphi / beta_i**2
    assert via_phi == pytest.approx(via_xi)


def test_full_bloch_sphere_specialization():
    info_bits = 3.0
    omega = 2.5
    xi_i = bloch_sphere_xi(info_bits, omega)
    phi_i = phi_from_xi(xi_i)
    expected = math.sqrt(24.0 * KAPPA * info_bits) * abs(omega)
    assert phi_i == pytest.approx(expected)


def test_positive_alpha_gives_nonnegative_mass2_in_positive_kappa_sector():
    assert mass2(0.25) > 0.0
    assert mass2(0.0) == 0.0


def test_baseline_boundary_is_regular_in_phi_chart():
    xi_star = 4.0
    assert phi_from_xi(xi_star, xi_star) == 0.0
    with pytest.raises(ValueError):
        kinetic_metric_xi(xi_star, xi_star)


@pytest.mark.parametrize("bad_xi", [-1.0, -1.0e-12])
def test_negative_dynamic_curvature_fails_closed(bad_xi):
    with pytest.raises(ValueError):
        phi_from_xi(bad_xi, 0.0)


@pytest.mark.parametrize("bad_beta", [0.0, -1.0, math.inf, math.nan])
def test_invalid_beta_fails_closed(bad_beta):
    with pytest.raises(ValueError):
        phi_from_xi(1.0, 0.0, bad_beta)
