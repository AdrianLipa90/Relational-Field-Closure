import math

import pytest

from src.rfc.adm_shift_noether_phase_energy import (
    ADMShiftNoetherPhaseEnergyError,
    directional_null_phase_rate,
    normal_phase_rate,
    phase_energy_coordinates,
    scaled_information_candidate,
)


def test_full_adm_normal_phase_rate_reduces_to_zero_shift_parent():
    rate = normal_phase_rate(1.7, 0.0, 3.4, 1.2)
    assert rate == pytest.approx(3.4 / 1.7)


def test_directional_null_phase_rate_matches_rf_e14_rate_carrier():
    beta = 0.27
    omega = 5.3
    co = directional_null_phase_rate(beta, omega, +1)
    counter = directional_null_phase_rate(beta, omega, -1)
    assert co["R"] == pytest.approx(1.0 - beta)
    assert counter["R"] == pytest.approx(1.0 + beta)
    assert co["x"] == pytest.approx(1.0 / (1.0 - beta))
    assert counter["x"] == pytest.approx(1.0 / (1.0 + beta))


def test_shift_conjugate_coordinate_is_orientation_signed_beta():
    beta = 0.39
    co = directional_null_phase_rate(beta, 2.0, +1)
    counter = directional_null_phase_rate(beta, 2.0, -1)
    assert co["p"] == pytest.approx(beta)
    assert counter["p"] == pytest.approx(-beta)


def test_information_branch_matches_log_rational_closed_form():
    beta = 0.33
    co = directional_null_phase_rate(beta, 4.0, +1)
    counter = directional_null_phase_rate(beta, 4.0, -1)
    assert co["information"] == pytest.approx(math.log(1.0-beta)+beta/(1.0-beta))
    assert counter["information"] == pytest.approx(math.log(1.0+beta)-beta/(1.0+beta))


def test_phase_energy_per_carrier_and_density_share_common_rate_carrier():
    beta = 0.22
    omega = 3.7
    co = directional_null_phase_rate(beta, omega, +1)
    base = phase_energy_coordinates(1.4, omega)
    shifted = phase_energy_coordinates(1.4, co["r_n"])
    assert shifted["epsilon"] / base["epsilon"] == pytest.approx(co["R"])
    assert shifted["energy_density"] / base["energy_density"] == pytest.approx(co["R"]**2)


def test_scaled_information_uses_existing_zero_shift_energy_per_carrier_scale():
    omega = 6.0
    info = 0.125
    assert scaled_information_candidate(omega, info) == pytest.approx(3.0 * info)


def test_dual_rate_dictionary_is_exact():
    beta = -0.41
    state = directional_null_phase_rate(beta, 2.3, +1)
    assert state["dual"] == pytest.approx(-math.log(1.0-state["p"]))
    assert state["information"] + state["dual"] == pytest.approx(state["p"] * state["x"])


def test_zero_shift_all_directional_ratios_return_reference():
    for orientation in (-1, 1):
        state = directional_null_phase_rate(0.0, 2.5, orientation)
        assert state["R"] == pytest.approx(1.0)
        assert state["x"] == pytest.approx(1.0)
        assert state["information"] == pytest.approx(0.0)
        assert state["p"] == pytest.approx(0.0)
        assert state["dual"] == pytest.approx(0.0)


@pytest.mark.parametrize("orientation", [0, 2, -2])
def test_invalid_orientation_fails_closed(orientation):
    with pytest.raises(ADMShiftNoetherPhaseEnergyError):
        directional_null_phase_rate(0.2, 1.0, orientation)


@pytest.mark.parametrize("beta", [-1.0, 1.0, 1.2, -1.1, math.inf, math.nan])
def test_invalid_shift_domain_fails_closed(beta):
    with pytest.raises(ADMShiftNoetherPhaseEnergyError):
        directional_null_phase_rate(beta, 1.0, +1)


def test_nonpositive_normal_phase_rate_energy_fails_closed():
    with pytest.raises(ADMShiftNoetherPhaseEnergyError):
        phase_energy_coordinates(1.0, 0.0)
