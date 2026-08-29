import math

import pytest

from src.rfc.onshell_matter_information_mass_spectral_firewall import (
    OnShellMatterInformationMassSpectralError,
    information_gap_frequency,
    mass_match_defect,
    matter_information_mass_ratio,
    onshell_matter_phase_frequency,
    onshell_spectral_ratio,
    phase_kinetic_energy_per_carrier,
    required_zeta_same_matter_target,
    rfs2_target_defect_on_matter_branch,
    same_matter_target_ratio,
    same_target_reduced_closure_defect,
    spectral_match_defect,
    spectral_ratio_from_frequencies,
    tetra_fs_shape_coefficient,
    total_onshell_energy_per_carrier,
)


def test_onshell_phase_to_information_spectral_ratio_is_mass_ratio():
    c = 3.0
    m_psi = 1.7
    m_i = 0.8
    omega_psi = onshell_matter_phase_frequency(c, m_psi)
    omega_i = information_gap_frequency(c, m_i)

    assert spectral_ratio_from_frequencies(omega_psi, omega_i) == pytest.approx(
        m_psi / m_i
    )
    assert onshell_spectral_ratio(c, m_psi, m_i) == pytest.approx(
        matter_information_mass_ratio(m_psi, m_i)
    )


def test_speed_conversion_cancels_from_onshell_ratio():
    m_psi = 2.2
    m_i = 1.1
    base = onshell_spectral_ratio(1.0, m_psi, m_i)
    for c in (0.2, 3.0, 11.0, 299792458.0):
        assert onshell_spectral_ratio(c, m_psi, m_i) == pytest.approx(base)


def test_spectral_match_defect_equals_mass_match_defect_on_branch():
    for m_psi, m_i in ((1.0, 1.0), (2.0, 1.5), (0.7, 2.4)):
        rho = matter_information_mass_ratio(m_psi, m_i)
        assert spectral_match_defect(rho) == pytest.approx(
            mass_match_defect(m_psi, m_i)
        )


def test_same_matter_target_ratio_equals_rho_on_branch():
    c = 4.0
    m_psi = 1.3
    m_i = 0.9
    assert same_matter_target_ratio(m_psi, m_i) == pytest.approx(
        onshell_spectral_ratio(c, m_psi, m_i)
    )


def test_same_target_rf_s2_equation_reduces_by_positive_mass_ratio():
    r_alpha = 1.4
    r_mass = 0.7
    zeta = 1.6
    unreduced = rfs2_target_defect_on_matter_branch(r_alpha, r_mass, zeta)
    reduced = same_target_reduced_closure_defect(r_alpha, r_mass, zeta)
    assert unreduced == pytest.approx(r_mass * reduced)


def test_required_zeta_closes_same_matter_target_equation():
    for r_alpha, r_mass in ((1.0, 1.0), (2.4, 0.8), (0.3, 3.2)):
        zeta = required_zeta_same_matter_target(r_alpha, r_mass)
        assert same_target_reduced_closure_defect(
            r_alpha, r_mass, zeta
        ) == pytest.approx(0.0, abs=2.0e-12)


def test_unit_mass_and_coupling_surface_recovers_tetra_scale_number():
    expected = (9.0 * math.sqrt(3.0) * math.pi / 8.0) ** (1.0 / 3.0)
    zeta = required_zeta_same_matter_target(1.0, 1.0)
    assert zeta == pytest.approx(expected)
    assert zeta == pytest.approx(1.82931154035502)
    assert 1.0 / tetra_fs_shape_coefficient() == pytest.approx(
        9.0 * math.sqrt(3.0) * math.pi / 8.0
    )


def test_rf_e5_factor_two_firewall_is_preserved():
    omega = 7.4
    kinetic = phase_kinetic_energy_per_carrier(omega)
    total = total_onshell_energy_per_carrier(omega)
    assert kinetic == pytest.approx(omega / 2.0)
    assert total == pytest.approx(omega)
    assert total == pytest.approx(2.0 * kinetic)


def test_common_rescaling_of_both_mass_coordinates_preserves_ratio():
    base = matter_information_mass_ratio(2.1, 0.7)
    for scale in (0.2, 3.0, 11.0):
        assert matter_information_mass_ratio(
            scale * 2.1, scale * 0.7
        ) == pytest.approx(base)


@pytest.mark.parametrize("bad", [0.0, -1.0, math.inf, math.nan])
def test_invalid_mass_coordinates_fail_closed(bad):
    with pytest.raises(OnShellMatterInformationMassSpectralError):
        matter_information_mass_ratio(bad, 1.0)
    with pytest.raises(OnShellMatterInformationMassSpectralError):
        matter_information_mass_ratio(1.0, bad)


def test_invalid_frequency_or_coupling_coordinates_fail_closed():
    for bad in (0.0, -1.0, math.inf, math.nan):
        with pytest.raises(OnShellMatterInformationMassSpectralError):
            spectral_ratio_from_frequencies(bad, 1.0)
        with pytest.raises(OnShellMatterInformationMassSpectralError):
            required_zeta_same_matter_target(bad, 1.0)
