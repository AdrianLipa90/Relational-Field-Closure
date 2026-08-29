import math

import pytest


KAPPA_E = 8.0 * math.pi


def _positive_finite(value, name):
    if not math.isfinite(value) or value <= 0.0:
        raise ValueError(f"{name} must be positive and finite")
    return value


def calibrated_wave_speed2(m_eff, gamma_x, gamma_t):
    _positive_finite(m_eff, "M_eff")
    _positive_finite(gamma_x, "Gamma_x")
    _positive_finite(gamma_t, "Gamma_t")
    return m_eff * (gamma_x / gamma_t) ** 2


def calibrated_mass_frequency2(mu_lambda2, gamma_t):
    if not math.isfinite(mu_lambda2) or mu_lambda2 < 0.0:
        raise ValueError("mu_lambda^2 must be nonnegative and finite")
    _positive_finite(gamma_t, "Gamma_t")
    return mu_lambda2 / gamma_t**2


def required_gamma_ratio(m_eff, c):
    _positive_finite(m_eff, "M_eff")
    _positive_finite(c, "c")
    return c / math.sqrt(m_eff)


def mass2(alpha_i, kappa_e=KAPPA_E):
    if not math.isfinite(alpha_i) or alpha_i < 0.0:
        raise ValueError("alpha_I must be nonnegative and finite")
    _positive_finite(kappa_e, "kappa_E")
    return alpha_i / kappa_e


def premetric_gap2(alpha_i, gamma_t, c, kappa_e=KAPPA_E):
    m2 = mass2(alpha_i, kappa_e)
    _positive_finite(gamma_t, "Gamma_t")
    _positive_finite(c, "c")
    return gamma_t**2 * c**2 * m2


def gamma_t_from_05c(t_ref, phi_ref):
    _positive_finite(t_ref, "T_ref")
    _positive_finite(phi_ref, "phi_ref")
    return t_ref * phi_ref


def gamma_x_from_cell(l_h, h):
    _positive_finite(l_h, "L_h")
    _positive_finite(h, "h")
    return l_h / h


def physical_kg_frequency2(mu_lambda2, gamma_t):
    return calibrated_mass_frequency2(mu_lambda2, gamma_t)


def test_affine_wave_coefficient_transformation():
    m_eff = 2.5
    gamma_x = 4.0
    gamma_t = 5.0
    assert calibrated_wave_speed2(m_eff, gamma_x, gamma_t) == pytest.approx(
        m_eff * gamma_x**2 / gamma_t**2
    )


def test_lightcone_ratio_is_exact():
    m_eff = 3.2
    c = 2.75
    ratio = required_gamma_ratio(m_eff, c)
    gamma_t = 1.7
    gamma_x = ratio * gamma_t
    assert calibrated_wave_speed2(m_eff, gamma_x, gamma_t) == pytest.approx(c**2)


def test_premetric_mass_gap_maps_to_physical_kg_mass_frequency():
    alpha_i = 0.45
    gamma_t = 3.0
    c = 1.8
    mu2 = premetric_gap2(alpha_i, gamma_t, c)
    expected = c**2 * mass2(alpha_i)
    assert calibrated_mass_frequency2(mu2, gamma_t) == pytest.approx(expected)


def test_05c_clock_factor_enters_mass_slot_exactly():
    t_ref = 2.0
    phi_ref = 1.25
    gamma_t = gamma_t_from_05c(t_ref, phi_ref)
    alpha_i = 0.2
    c = 3.0
    mu2 = premetric_gap2(alpha_i, gamma_t, c)
    assert mu2 == pytest.approx((t_ref * phi_ref) ** 2 * c**2 * alpha_i / KAPPA_E)


def test_cell_width_calibration_enters_lightcone_ratio():
    h = 0.5
    l_h = 1.2
    gamma_x = gamma_x_from_cell(l_h, h)
    gamma_t = 0.8
    c = 2.0
    m_eff = (c * gamma_t / gamma_x) ** 2
    assert calibrated_wave_speed2(m_eff, gamma_x, gamma_t) == pytest.approx(c**2)


def test_unit_calibration_specialization_recovers_simple_meff_condition():
    c = 2.3
    gamma_t = gamma_x = 1.0
    m_eff = c**2
    assert calibrated_wave_speed2(m_eff, gamma_x, gamma_t) == pytest.approx(c**2)


def test_natural_unit_specialization_maps_gap_directly():
    alpha_i = 0.6
    gamma_t = 1.0
    c = 1.0
    mu2 = premetric_gap2(alpha_i, gamma_t, c)
    assert mu2 == pytest.approx(mass2(alpha_i))


def test_physical_homogeneous_frequency_relation():
    alpha_i = 0.72
    gamma_t = 2.4
    c = 1.6
    mu2 = premetric_gap2(alpha_i, gamma_t, c)
    omega2 = physical_kg_frequency2(mu2, gamma_t)
    assert omega2 == pytest.approx(c**2 * alpha_i / KAPPA_E)


@pytest.mark.parametrize("bad", [0.0, -1.0, math.inf, math.nan])
def test_bad_time_calibration_fails_closed(bad):
    with pytest.raises(ValueError):
        calibrated_wave_speed2(1.0, 1.0, bad)


@pytest.mark.parametrize("bad", [0.0, -1.0, math.inf, math.nan])
def test_bad_length_calibration_fails_closed(bad):
    with pytest.raises(ValueError):
        gamma_x_from_cell(bad, 1.0)


@pytest.mark.parametrize("bad", [-1.0, math.inf, math.nan])
def test_bad_premetric_gap_fails_closed(bad):
    with pytest.raises(ValueError):
        calibrated_mass_frequency2(bad, 1.0)
