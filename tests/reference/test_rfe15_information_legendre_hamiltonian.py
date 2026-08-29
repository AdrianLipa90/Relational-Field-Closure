import math

import pytest

from src.rfc.information_legendre_hamiltonian import (
    InformationLegendreHamiltonianError,
    directional_dual,
    fenchel_defect,
    phi,
    phi_prime,
    phi_second,
    psi,
    scaled_primal_dual,
    x_from_conjugate,
)


def test_phi_is_strictly_convex():
    for x in (0.2, 0.5, 1.0, 2.0, 7.0):
        assert phi_second(x) > 0.0


def test_gradient_inverse_is_exact():
    for x in (0.2, 0.7, 1.0, 1.8, 5.0):
        p = phi_prime(x)
        assert x_from_conjugate(p) == pytest.approx(x)


def test_legendre_dual_closed_form_and_fenchel_equality():
    for p in (-0.8, -0.2, 0.0, 0.3, 0.8):
        x = x_from_conjugate(p)
        expected = -math.log(1.0 - p)
        assert psi(p) == pytest.approx(expected)
        assert fenchel_defect(x, p) == pytest.approx(0.0, abs=1.0e-14)


def test_adm_shift_is_exact_conjugate_coordinate():
    for beta in (-0.7, -0.3, 0.0, 0.2, 0.65):
        state = directional_dual(beta)
        assert state["p_co"] == pytest.approx(beta)
        assert state["p_counter"] == pytest.approx(-beta)


def test_dual_even_odd_coordinates_are_log_gamma_and_rapidity():
    for beta in (-0.75, -0.2, 0.0, 0.31, 0.8):
        state = directional_dual(beta)
        assert state["psi_even"] == pytest.approx(state["log_gamma"])
        assert state["psi_odd"] == pytest.approx(state["rapidity"])


def test_primal_branch_is_px_minus_dual():
    beta = 0.41
    state = directional_dual(beta)
    assert state["phi_co"] == pytest.approx(state["p_co"] * state["x_co"] - state["psi_co"])
    assert state["phi_counter"] == pytest.approx(
        state["p_counter"] * state["x_counter"] - state["psi_counter"]
    )


def test_primal_and_dual_scaled_candidates_are_distinct_coordinates():
    beta = 0.3
    scaled = scaled_primal_dual(beta, 4.2)
    assert scaled["E_phi_co"] != pytest.approx(scaled["E_psi_co"])
    assert scaled["E_phi_counter"] != pytest.approx(scaled["E_psi_counter"])


def test_zero_shift_reference():
    state = directional_dual(0.0)
    assert state["x_co"] == pytest.approx(1.0)
    assert state["x_counter"] == pytest.approx(1.0)
    assert state["p_co"] == pytest.approx(0.0)
    assert state["p_counter"] == pytest.approx(0.0)
    assert state["phi_co"] == pytest.approx(0.0)
    assert state["phi_counter"] == pytest.approx(0.0)
    assert state["psi_co"] == pytest.approx(0.0)
    assert state["psi_counter"] == pytest.approx(0.0)


@pytest.mark.parametrize("x", [0.0, -1.0, math.inf, math.nan])
def test_invalid_primal_domain_fails_closed(x):
    with pytest.raises(InformationLegendreHamiltonianError):
        phi(x)


@pytest.mark.parametrize("p", [1.0, 1.1, math.inf, math.nan])
def test_invalid_dual_domain_fails_closed(p):
    with pytest.raises(InformationLegendreHamiltonianError):
        psi(p)


@pytest.mark.parametrize("beta", [-1.0, 1.0, 1.1, -1.2, math.inf, math.nan])
def test_invalid_directional_domain_fails_closed(beta):
    with pytest.raises(InformationLegendreHamiltonianError):
        directional_dual(beta)
