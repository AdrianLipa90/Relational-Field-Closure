import math

import pytest

from src.rfc.lightcone_spectral_scale_reduction import (
    LightconeSpectralScaleReductionError,
    kg_frequency_physical,
    phase_energy_ratio,
    phase_frequency_physical,
    phase_length_from_rho_mass,
    q_s_from_premetric,
    q_s_reduced,
    reduced_closure_defect,
    reduced_energy_scale_natural,
    required_zeta_s,
    spatial_mass_coordinate,
    spectral_ratio,
    tetra_fs_shape_coefficient,
    zeta_from_premetric,
)


def test_spectral_ratio_is_same_in_lambda_and_physical_time():
    gamma_t = 2.7
    mu_lambda = 1.9
    rho = 1.35
    omega_lambda_phase = -rho * mu_lambda

    ratio_lambda = spectral_ratio(omega_lambda_phase, mu_lambda)
    omega_phase_t = abs(phase_frequency_physical(omega_lambda_phase, gamma_t))
    omega_kg_t = mu_lambda / gamma_t

    assert ratio_lambda == pytest.approx(rho)
    assert omega_phase_t / omega_kg_t == pytest.approx(rho)


def test_rfl5a_mass_frequency_and_01l_phase_length_reduce_exactly():
    c = 3.0
    m_i = 0.4
    rho = 1.5

    omega_kg_t = kg_frequency_physical(c, m_i)
    omega_phase_t = rho * omega_kg_t
    ell_phi_from_01l = c / omega_phase_t

    assert ell_phi_from_01l == pytest.approx(phase_length_from_rho_mass(rho, m_i))
    assert m_i * ell_phi_from_01l == pytest.approx(1.0 / rho)
    assert phase_energy_ratio(rho) == pytest.approx(rho)


def test_rf_s1_q_reduces_to_rho_times_spatial_mass_coordinate():
    m_i = 0.7
    ell_s = 2.2
    rho = 0.8
    zeta = spatial_mass_coordinate(m_i, ell_s)
    ell_phi = phase_length_from_rho_mass(rho, m_i)

    assert q_s_reduced(rho, zeta) == pytest.approx(ell_s / ell_phi)


def test_premetric_lightcone_representation_matches_physical_spatial_coordinate():
    gamma_t = 2.0
    c = 3.0
    m_i = 0.4
    m_eff = 4.0
    sigma_x = 1.2
    rho = 1.5

    mu_lambda = gamma_t * c * m_i
    gamma_x = c * gamma_t / math.sqrt(m_eff)
    ell_s = sigma_x * gamma_x

    zeta_physical = spatial_mass_coordinate(m_i, ell_s)
    zeta_premetric = zeta_from_premetric(sigma_x, mu_lambda, m_eff)

    assert zeta_premetric == pytest.approx(zeta_physical)
    assert q_s_from_premetric(rho, sigma_x, mu_lambda, m_eff) == pytest.approx(
        q_s_reduced(rho, zeta_physical)
    )


def test_reduced_energy_scale_matches_rf_s1_expression():
    r_alpha = 1.3
    rho = 0.9
    zeta = 1.7
    m_i = 2.4

    q_s = rho * zeta
    e_phi = rho * m_i
    rf_s1 = (
        r_alpha
        * tetra_fs_shape_coefficient()
        * q_s**3
        * m_i**2
        / e_phi
    )

    assert reduced_energy_scale_natural(r_alpha, rho, zeta, m_i) == pytest.approx(
        rf_s1
    )


def test_required_zeta_closes_reduced_target_equation():
    for r_alpha, rho, r_m in ((1.0, 1.0, 1.0), (2.3, 0.7, 1.4), (0.4, 2.0, 3.0)):
        zeta = required_zeta_s(r_alpha, rho, r_m)
        assert reduced_closure_defect(r_alpha, rho, zeta, r_m) == pytest.approx(
            0.0, abs=2.0e-12
        )


def test_unit_spectral_coupling_target_specialization_recovers_rf_s1_number():
    expected = (9.0 * math.sqrt(3.0) * math.pi / 8.0) ** (1.0 / 3.0)
    zeta = required_zeta_s(1.0, 1.0, 1.0)
    assert zeta == pytest.approx(expected)
    assert zeta == pytest.approx(1.82931154035502)


def test_common_lambda_rate_rescaling_preserves_spectral_ratio():
    base = spectral_ratio(-3.4, 1.7)
    for scale in (0.2, 3.0, 11.0):
        assert spectral_ratio(scale * -3.4, scale * 1.7) == pytest.approx(base)


@pytest.mark.parametrize("bad", [0.0, -1.0, math.inf, math.nan])
def test_positive_coordinates_fail_closed(bad):
    with pytest.raises(LightconeSpectralScaleReductionError):
        phase_length_from_rho_mass(bad, 1.0)
    with pytest.raises(LightconeSpectralScaleReductionError):
        spatial_mass_coordinate(1.0, bad)
    with pytest.raises(LightconeSpectralScaleReductionError):
        zeta_from_premetric(1.0, 1.0, bad)


def test_zero_or_nonfinite_phase_rate_fails_closed():
    for bad in (0.0, math.inf, -math.inf, math.nan):
        with pytest.raises(LightconeSpectralScaleReductionError):
            spectral_ratio(bad, 1.0)
