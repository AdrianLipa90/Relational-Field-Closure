import math

import pytest

from src.rfc.clock_information_scalar_action import (
    ClockInformationScalarActionError,
    clock_information_scalar,
    directional_x,
    homogeneous_cell_energy,
    mass_scale_defect,
    phi,
    scalar_potential_density,
)


def test_directional_information_scalar_uses_exact_rf_e14_branch():
    beta = 0.28
    area = 2.4
    xi_co = clock_information_scalar(beta, +1, area)
    xi_counter = clock_information_scalar(beta, -1, area)
    expected_co = (math.log(1.0-beta)+beta/(1.0-beta)) / area
    expected_counter = (math.log(1.0+beta)-beta/(1.0+beta)) / area
    assert xi_co == pytest.approx(expected_co)
    assert xi_counter == pytest.approx(expected_counter)


def test_rf_l3_potential_roundtrip_form():
    beta = 0.31
    area = 1.7
    alpha = 0.42
    kappa = 3.1
    xi = clock_information_scalar(beta, +1, area)
    u = scalar_potential_density(beta, +1, area, alpha, kappa)
    assert kappa * u == pytest.approx(alpha * xi)


def test_homogeneous_cell_energy_factorizes_into_energy_scale_times_information():
    state = homogeneous_cell_energy(
        beta=0.35,
        orientation=+1,
        area_rel=2.0,
        volume_cell=5.0,
        alpha_clk=0.6,
        kappa_e=4.0,
    )
    assert state["H_clk"] == pytest.approx(state["E_star"] * state["information"])
    assert state["E_star"] == pytest.approx(0.6 * 5.0 / (4.0 * 2.0))


def test_zero_shift_has_zero_information_energy_but_finite_scale():
    state = homogeneous_cell_energy(0.0, +1, 2.0, 3.0, 0.8, 5.0)
    assert state["x"] == pytest.approx(1.0)
    assert state["information"] == pytest.approx(0.0)
    assert state["H_clk"] == pytest.approx(0.0)
    assert state["E_star"] == pytest.approx(0.8 * 3.0 / (5.0 * 2.0))


def test_newtonian_matching_forces_energy_scale_mc2():
    mass = 1.8
    c = 2.5
    target = mass * c * c
    area = 1.4
    kappa = 2.1
    volume = 3.7
    alpha = target * kappa * area / volume
    assert mass_scale_defect(mass, c, area, volume, alpha, kappa) == pytest.approx(0.0)

    beta = 1.0e-5
    state = homogeneous_cell_energy(beta, +1, area, volume, alpha, kappa)
    newton = 0.5 * mass * (beta*c)**2
    assert state["H_clk"] / newton == pytest.approx(1.0, rel=2.0e-5)


def test_parity_conjugacy_survives_action_routing():
    beta = 0.43
    args = dict(area_rel=2.3, volume_cell=4.1, alpha_clk=0.9, kappa_e=3.7)
    co = homogeneous_cell_energy(beta, +1, **args)
    mirrored = homogeneous_cell_energy(-beta, -1, **args)
    assert co["H_clk"] == pytest.approx(mirrored["H_clk"])


def test_positive_coupling_gives_nonnegative_information_potential_energy():
    for beta in (-0.8, -0.3, 0.0, 0.4, 0.8):
        for s in (-1, 1):
            state = homogeneous_cell_energy(beta, s, 1.5, 2.0, 0.7, 4.0)
            assert state["information"] >= -1.0e-15
            assert state["H_clk"] >= -1.0e-15


def test_directional_x_matches_common_rate_reciprocal():
    beta = -0.26
    assert directional_x(beta, +1) == pytest.approx(1.0/(1.0-beta))
    assert directional_x(beta, -1) == pytest.approx(1.0/(1.0+beta))


@pytest.mark.parametrize("beta", [-1.0,1.0,-1.2,1.2,math.inf,math.nan])
def test_invalid_beta_fails_closed(beta):
    with pytest.raises(ClockInformationScalarActionError):
        directional_x(beta, +1)


@pytest.mark.parametrize("area,volume", [(0.0,1.0),(1.0,0.0),(-1.0,1.0),(1.0,-2.0)])
def test_invalid_cell_geometry_fails_closed(area, volume):
    with pytest.raises(ClockInformationScalarActionError):
        homogeneous_cell_energy(0.2, +1, area, volume, 1.0, 1.0)


def test_zero_kappa_fails_closed():
    with pytest.raises(ClockInformationScalarActionError):
        scalar_potential_density(0.2, +1, 1.0, 1.0, 0.0)
