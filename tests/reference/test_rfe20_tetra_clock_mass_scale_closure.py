import math

import pytest

from src.rfc.tetra_clock_mass_scale_closure import (
    TetraClockMassScaleClosureError,
    closure_defect,
    directional_energy_natural,
    directional_phi,
    energy_scale_natural,
    inverse_shape_coefficient,
    kappa_shape_coefficient,
    physical_directional_energy_natural,
    physical_directional_phi,
    required_q_s,
    required_r_alpha,
    tetra_fs_shape_coefficient,
    volume_area_ratio,
)


def test_exact_tetra_fs_shape_coefficient():
    c = tetra_fs_shape_coefficient()
    assert c == pytest.approx(8.0/(9.0*math.sqrt(3.0)*math.pi))
    assert inverse_shape_coefficient() == pytest.approx(9.0*math.sqrt(3.0)*math.pi/8.0)


def test_kappa_rewrite_is_exact_for_canonical_kappa():
    kappa = math.log(2.0)/(24.0*math.pi)
    assert kappa_shape_coefficient(kappa) == pytest.approx(tetra_fs_shape_coefficient())


def test_two_scale_volume_area_ratio():
    ell_phi = 2.7
    q = 1.4
    ell_s = q * ell_phi
    expected = tetra_fs_shape_coefficient() * q**3 * ell_phi
    assert volume_area_ratio(ell_s, ell_phi) == pytest.approx(expected)


def test_rf_l4a_energy_scale_composition():
    r_alpha = 0.8
    q = 1.3
    m_i = 2.2
    e_phi = 1.7
    expected = r_alpha * tetra_fs_shape_coefficient() * q**3 * m_i**2 / e_phi
    assert energy_scale_natural(r_alpha, q, m_i, e_phi) == pytest.approx(expected)


def test_general_dimensionless_closure_equation():
    r_alpha = 1.7
    mu_phi = 0.9
    r_m = 1.2
    q = required_q_s(r_alpha, mu_phi, r_m)
    assert closure_defect(r_alpha, q, mu_phi, r_m) == pytest.approx(0.0, abs=1e-13)


def test_unit_binding_specialization_forces_nontrivial_q():
    q = required_q_s(1.0, 1.0, 1.0)
    expected = (9.0*math.sqrt(3.0)*math.pi/8.0)**(1.0/3.0)
    assert q == pytest.approx(expected)
    assert q == pytest.approx(1.82931154035502)
    assert not math.isclose(q, 1.0, rel_tol=0.0, abs_tol=1e-12)


def test_common_scale_specialization_forces_coupling_ratio():
    r_alpha = required_r_alpha(1.0, 1.0, 1.0)
    assert r_alpha == pytest.approx(9.0*math.sqrt(3.0)*math.pi/8.0)
    assert r_alpha == pytest.approx(6.12157285429049)


def test_unit_binding_q_closes_energy_scale_to_mass():
    m_i = 3.4
    q = required_q_s(1.0, 1.0, 1.0)
    e_star = energy_scale_natural(1.0, q, m_i, m_i)
    assert e_star == pytest.approx(m_i)


def test_unity_scale_and_unity_coupling_exposes_shape_mismatch():
    m_i = 2.0
    e_star = energy_scale_natural(1.0, 1.0, m_i, m_i)
    assert e_star / m_i == pytest.approx(tetra_fs_shape_coefficient())
    assert e_star != pytest.approx(m_i)


def test_directional_energy_branch_after_scale_closure():
    beta = 0.24
    mass = 1.6
    e_plus = directional_energy_natural(beta, +1, mass)
    e_minus = directional_energy_natural(beta, -1, mass)
    expected_plus = mass * (math.log(1.0-beta)+beta/(1.0-beta))
    expected_minus = mass * (math.log(1.0+beta)-beta/(1.0+beta))
    assert e_plus == pytest.approx(expected_plus)
    assert e_minus == pytest.approx(expected_minus)


def test_superseded_rfe19_physical_directional_api_is_preserved_as_rfe20_alias():
    beta = 0.37
    mass = 2.3
    for orientation in (-1, 1):
        assert physical_directional_phi(beta, orientation) == pytest.approx(
            directional_phi(beta, orientation)
        )
        assert physical_directional_energy_natural(beta, orientation, mass) == pytest.approx(
            directional_energy_natural(beta, orientation, mass)
        )


@pytest.mark.parametrize("value", [0.0, -1.0, math.inf, math.nan])
def test_positive_scale_inputs_fail_closed(value):
    with pytest.raises(TetraClockMassScaleClosureError):
        required_q_s(value, 1.0, 1.0)


@pytest.mark.parametrize("beta", [-1.0,1.0,-1.1,1.1,math.inf,math.nan])
def test_directional_domain_fails_closed(beta):
    with pytest.raises(TetraClockMassScaleClosureError):
        directional_energy_natural(beta, +1, 1.0)
    with pytest.raises(TetraClockMassScaleClosureError):
        physical_directional_energy_natural(beta, +1, 1.0)
