import math

import pytest

from src.rfc.adm_directional_relative_entropy import (
    ADMDirectionalRelativeEntropyError,
    adm_null_characteristics,
    directional_information_flat,
    directional_information_from_shift,
    phi_ratio,
    scaled_directional_candidate,
)


def test_local_orthonormal_adm_null_rates_are_one_plus_minus_shift():
    u_co, u_counter = adm_null_characteristics(1.0, 1.0, 0.23)
    assert u_co == pytest.approx(1.0 - 0.23)
    assert u_counter == pytest.approx(-(1.0 + 0.23))


def test_relative_entropy_composition_gives_exact_log_rational_pair():
    beta = 0.31
    i_co, i_counter = directional_information_flat(beta)
    expected_co = math.log(1.0 - beta) + beta / (1.0 - beta)
    expected_counter = math.log(1.0 + beta) - beta / (1.0 + beta)
    assert i_co == pytest.approx(expected_co)
    assert i_counter == pytest.approx(expected_counter)


def test_parity_conjugacy_is_exact():
    for beta in (-0.7, -0.3, 0.0, 0.2, 0.65):
        co, counter = directional_information_flat(beta)
        co_mirror, counter_mirror = directional_information_flat(-beta)
        assert co == pytest.approx(counter_mirror)
        assert counter == pytest.approx(co_mirror)


def test_rapidity_factorization_of_reciprocal_rates():
    beta = 0.42
    state = directional_information_from_shift(1.0, 1.0, beta)
    gamma = state["gamma"]
    eta = state["rapidity"]
    assert state["x_co"] == pytest.approx(gamma * math.exp(eta))
    assert state["x_counter"] == pytest.approx(gamma * math.exp(-eta))


def test_even_odd_closed_forms():
    beta = 0.37
    state = directional_information_from_shift(1.0, 1.0, beta)
    gamma = state["gamma"]
    eta = state["rapidity"]
    assert state["I_even"] == pytest.approx(gamma * gamma - 1.0 - math.log(gamma))
    assert state["I_odd"] == pytest.approx(beta * gamma * gamma - eta)


def test_small_shift_common_quadratic_and_opposite_cubic():
    beta = 1.0e-3
    co, counter = directional_information_flat(beta)
    co_series = 0.5 * beta**2 + (2.0/3.0) * beta**3 + 0.75 * beta**4
    counter_series = 0.5 * beta**2 - (2.0/3.0) * beta**3 + 0.75 * beta**4
    assert co == pytest.approx(co_series, rel=2.0e-6, abs=1.0e-15)
    assert counter == pytest.approx(counter_series, rel=2.0e-6, abs=1.0e-15)


def test_newton_scale_is_forced_by_quadratic_coefficient_if_energy_binding_is_admitted():
    mass = 2.4
    c = 3.0
    beta = 1.0e-5
    e_co, e_counter = scaled_directional_candidate(beta, mass * c * c)
    newton = 0.5 * mass * (beta * c)**2
    # Cubic directional correction is O(beta^3), so the ratio converges to one.
    assert e_co / newton == pytest.approx(1.0, rel=2.0e-5)
    assert e_counter / newton == pytest.approx(1.0, rel=2.0e-5)


def test_standard_sr_even_series_differs_at_cubic_order():
    beta = 0.02
    co, counter = directional_information_flat(beta)
    sr = 1.0 / math.sqrt(1.0 - beta**2) - 1.0
    assert co - counter > 0.0
    assert abs((co + counter) / 2.0 - sr) > 1.0e-8


def test_phi_is_nonnegative_on_directional_factors():
    for beta in (-0.9, -0.4, 0.0, 0.4, 0.9):
        state = directional_information_from_shift(1.0, 1.0, beta)
        assert phi_ratio(state["x_co"]) >= -1.0e-15
        assert phi_ratio(state["x_counter"]) >= -1.0e-15


@pytest.mark.parametrize("beta", [-1.0, 1.0, -1.2, 1.2, math.inf, math.nan])
def test_invalid_shift_domain_fails_closed(beta):
    with pytest.raises(ADMDirectionalRelativeEntropyError):
        directional_information_from_shift(1.0, 1.0, beta)


@pytest.mark.parametrize("lapse,h11", [(0.0,1.0), (-1.0,1.0), (1.0,0.0), (1.0,-1.0)])
def test_invalid_adm_metric_inputs_fail_closed(lapse, h11):
    with pytest.raises(ADMDirectionalRelativeEntropyError):
        adm_null_characteristics(lapse, h11, 0.0)
