import math

import pytest


KAPPA_E = 8.0 * math.pi


def reconstruct_u(xi_i: float, alpha_i: float, kappa_e: float = KAPPA_E) -> float:
    vals = (xi_i, alpha_i, kappa_e)
    if not all(math.isfinite(v) for v in vals):
        raise ValueError("nonfinite RF-L3 state")
    if kappa_e == 0.0:
        raise ValueError("kappa_E must be nonzero")
    return alpha_i * xi_i / kappa_e


def lambda0_from_xi(lambda_ref: float, xi_i: float, alpha_i: float) -> float:
    vals = (lambda_ref, xi_i, alpha_i)
    if not all(math.isfinite(v) for v in vals):
        raise ValueError("nonfinite RF-L3 state")
    return lambda_ref + alpha_i * xi_i


def lambda0_from_u(lambda_ref: float, u_i: float, kappa_e: float = KAPPA_E) -> float:
    vals = (lambda_ref, u_i, kappa_e)
    if not all(math.isfinite(v) for v in vals):
        raise ValueError("nonfinite RF-L3 state")
    return lambda_ref + kappa_e * u_i


def pullback_derivative(xi_derivative: float, alpha_i: float, kappa_e: float = KAPPA_E) -> float:
    vals = (xi_derivative, alpha_i, kappa_e)
    if not all(math.isfinite(v) for v in vals):
        raise ValueError("nonfinite RF-L3 state")
    if kappa_e == 0.0:
        raise ValueError("kappa_E must be nonzero")
    return alpha_i * xi_derivative / kappa_e


def carry_holonomy(tau_r: float) -> float:
    if not math.isfinite(tau_r):
        raise ValueError("nonfinite holonomy")
    return tau_r


@pytest.mark.parametrize(
    "lambda_ref,xi_i,alpha_i",
    [
        (0.0, 2.5, 0.25),
        (7.0, 1.0e-9, 3.0),
        (-4.0, -2.0, 0.5),
        (1.5, 8.0, -0.125),
    ],
)
def test_exact_information_scalar_potential_roundtrip(lambda_ref, xi_i, alpha_i):
    u_i = reconstruct_u(xi_i, alpha_i)
    assert lambda0_from_u(lambda_ref, u_i) == pytest.approx(
        lambda0_from_xi(lambda_ref, xi_i, alpha_i)
    )


def test_constant_reference_shift_does_not_change_dynamic_displacement():
    xi_i = 3.25
    alpha_i = 0.4
    a = lambda0_from_xi(2.0, xi_i, alpha_i) - 2.0
    b = lambda0_from_xi(-11.0, xi_i, alpha_i) - (-11.0)
    assert a == pytest.approx(b)
    assert a == pytest.approx(alpha_i * xi_i)


def test_first_derivative_pullback():
    xi_prime = -0.75
    alpha_i = 2.0
    assert pullback_derivative(xi_prime, alpha_i) == pytest.approx(
        alpha_i * xi_prime / KAPPA_E
    )


def test_second_derivative_stability_pullback_and_alpha_sign():
    xi_second = 5.0
    positive = pullback_derivative(xi_second, 0.3)
    negative = pullback_derivative(xi_second, -0.3)
    assert positive > 0.0
    assert negative < 0.0
    assert negative == pytest.approx(-positive)


def test_zero_coupling_is_explicit_degenerate_reconstruction():
    xi_i = 123.0
    assert reconstruct_u(xi_i, 0.0) == 0.0
    assert lambda0_from_xi(4.0, xi_i, 0.0) == 4.0


def test_holonomy_coordinate_is_transport_invariant_under_scalar_reconstruction():
    tau_r = -1.2345
    _ = reconstruct_u(6.0, 0.25)
    assert carry_holonomy(tau_r) == tau_r


@pytest.mark.parametrize("bad", [math.inf, -math.inf, math.nan])
def test_nonfinite_information_scalar_fails_closed(bad):
    with pytest.raises(ValueError):
        reconstruct_u(bad, 1.0)


@pytest.mark.parametrize("bad", [math.inf, -math.inf, math.nan])
def test_nonfinite_coupling_fails_closed(bad):
    with pytest.raises(ValueError):
        reconstruct_u(1.0, bad)


def test_zero_kappa_e_fails_closed():
    with pytest.raises(ValueError):
        reconstruct_u(1.0, 1.0, 0.0)
