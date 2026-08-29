import math

import pytest

from src.rfc.radial_information_matter_action_reclassification import (
    RadialInformationMatterActionError,
    alpha_i_from_mass,
    amplitude_information_defect,
    canonical_matter_radial,
    fisher_information_radial,
    lambda_shift_from_information,
    lambda_shift_from_radial_potential,
    mass_ratio_from_radial_potential_match,
    original_complex_scalar_lagrangian,
    radial_potential_information,
    radial_potential_matter,
    radial_potential_relative_defect,
    reclassified_radial_phase_lagrangian,
    validate_single_radial_representation,
)


def test_sqrt2_normalizations_match_exactly_on_amplitude_curvature_surface():
    amplitude = 1.7
    bar_xi = amplitude**2
    assert canonical_matter_radial(amplitude) == pytest.approx(
        fisher_information_radial(bar_xi)
    )
    assert amplitude_information_defect(amplitude, bar_xi) == pytest.approx(0.0)


def test_amplitude_information_zero_defect_is_sensitive_to_mismatch():
    amplitude = 1.2
    exact = amplitude_information_defect(amplitude, amplitude**2)
    mismatch = amplitude_information_defect(amplitude, 1.4 * amplitude**2)
    assert exact == pytest.approx(0.0)
    assert mismatch > 0.0


def test_original_and_reclassified_actions_match_when_radial_binding_and_masses_match():
    amplitude = 0.9
    phi = canonical_matter_radial(amplitude)
    grad_a_sq = -0.14
    grad_phi_sq = 2.0 * grad_a_sq
    q_sq = -1.7
    mass = 1.3

    original = original_complex_scalar_lagrangian(
        amplitude, grad_a_sq, q_sq, mass
    )
    reclassified = reclassified_radial_phase_lagrangian(
        phi, grad_phi_sq, q_sq, mass
    )
    assert reclassified == pytest.approx(original)


def test_action_difference_localizes_to_mass_coefficient_after_radial_binding():
    amplitude = 1.1
    phi = canonical_matter_radial(amplitude)
    grad_a_sq = 0.3
    grad_phi_sq = 2.0 * grad_a_sq
    q_sq = -0.8
    m_psi = 1.8
    m_i = 1.2

    original = original_complex_scalar_lagrangian(
        amplitude, grad_a_sq, q_sq, m_psi
    )
    reclassified = reclassified_radial_phase_lagrangian(
        phi, grad_phi_sq, q_sq, m_i
    )
    expected = -(m_psi**2 - m_i**2) * amplitude**2
    assert original - reclassified == pytest.approx(expected)


def test_radial_potential_match_forces_unit_positive_mass_ratio():
    amplitude = 1.4
    bar_xi = amplitude**2
    mass = 2.1
    ratio = mass_ratio_from_radial_potential_match(
        amplitude, bar_xi, mass, mass
    )
    assert ratio == pytest.approx(1.0)
    assert radial_potential_relative_defect(
        amplitude, bar_xi, mass, mass
    ) == pytest.approx(0.0)


def test_potential_defect_detects_mass_mismatch_on_bound_radial_coordinate():
    amplitude = 1.4
    bar_xi = amplitude**2
    defect = radial_potential_relative_defect(
        amplitude, bar_xi, 2.0, 1.0
    )
    assert defect > 0.0


def test_information_and_matter_radial_potentials_are_same_coordinate_on_mass_match():
    amplitude = 0.8
    bar_xi = amplitude**2
    phi_i = fisher_information_radial(bar_xi)
    mass = 1.9
    assert radial_potential_matter(amplitude, mass) == pytest.approx(
        radial_potential_information(phi_i, mass)
    )


def test_dynamic_lambda_roundtrip_matches_on_radial_binding_surface():
    kappa_e = 2.3
    m_i = 0.7
    amplitude = 1.6
    bar_xi = amplitude**2
    alpha_i = alpha_i_from_mass(kappa_e, m_i)

    from_potential = lambda_shift_from_radial_potential(
        kappa_e, m_i, amplitude
    )
    from_information = lambda_shift_from_information(alpha_i, bar_xi)
    assert from_information == pytest.approx(from_potential)


def test_single_representation_guard_accepts_exactly_one_radial_ledger():
    assert validate_single_radial_representation(True, False)
    assert validate_single_radial_representation(False, True)
    with pytest.raises(RadialInformationMatterActionError):
        validate_single_radial_representation(True, True)
    with pytest.raises(RadialInformationMatterActionError):
        validate_single_radial_representation(False, False)


def test_mass_ratio_binding_rejects_unbound_amplitude_information_pair():
    with pytest.raises(RadialInformationMatterActionError):
        mass_ratio_from_radial_potential_match(1.0, 1.2, 1.0, 1.0)


@pytest.mark.parametrize("bad", [-1.0, -math.inf, math.inf, math.nan])
def test_invalid_nonnegative_coordinates_fail_closed(bad):
    with pytest.raises(RadialInformationMatterActionError):
        canonical_matter_radial(bad)
    with pytest.raises(RadialInformationMatterActionError):
        fisher_information_radial(bad)


def test_degenerate_zero_support_defect_fails_closed():
    with pytest.raises(RadialInformationMatterActionError):
        amplitude_information_defect(0.0, 0.0)
