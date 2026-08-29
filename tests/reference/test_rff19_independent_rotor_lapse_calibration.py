import math

import pytest

from src.rfc.independent_rotor_lapse_calibration import (
    C_LIGHT,
    RotorLapseCalibrationError,
    calibration_log_metric_response,
    coordinate_rate_binding_defect,
    eta_one_scale_response_stress_correction,
    flrw_phase_scale,
    occupation_density_from_phase_scale,
    omega_magnitude_from_phase_scale,
    phase_cell_volume_from_phase_scale,
    phase_scale_from_rotor_lapse,
    projector_scale_response_correction,
    proper_rate_binding_defect,
    proper_rotor_rate,
    pure_normal_projector_from_rates,
    spacetime_log_phase_scale_rate,
)


ZERO4 = tuple(tuple(0.0 for _ in range(4)) for _ in range(4))


def test_phase_scale_from_independent_rotor_lapse_rate():
    rate = 12.0
    lapse = 3.0
    mu = phase_scale_from_rotor_lapse(rate, lapse)
    assert mu == pytest.approx(4.0 / C_LIGHT)


def test_proper_rotor_rate_is_lapse_reduced_coordinate_rate():
    assert proper_rotor_rate(15.0, 5.0) == pytest.approx(3.0)


def test_zero_defect_independent_field_rotor_coordinate_rates():
    assert coordinate_rate_binding_defect(7.5, 7.5) == pytest.approx(0.0)
    assert coordinate_rate_binding_defect(8.0, 7.5) > 0.0


def test_zero_defect_proper_rate_binding():
    assert proper_rate_binding_defect(2.0, 6.0, 3.0) == pytest.approx(0.0)


def test_zero_defect_pure_normal_projector_is_one():
    assert pure_normal_projector_from_rates(2.0, 6.0, 3.0) == pytest.approx(1.0)


def test_pure_normal_projector_tracks_rate_mismatch_quadratically():
    assert pure_normal_projector_from_rates(3.0, 6.0, 3.0) == pytest.approx(2.25)


def test_independent_metric_response_can_be_zero_while_spacetime_scale_evolves():
    scale_response = calibration_log_metric_response(ZERO4, ZERO4)
    assert scale_response == ZERO4
    assert spacetime_log_phase_scale_rate(0.2, -0.1) == pytest.approx(0.3)


def test_metric_response_difference_is_retained():
    rotor = [list(row) for row in ZERO4]
    lapse = [list(row) for row in ZERO4]
    rotor[0][0] = 0.2
    lapse[0][0] = 0.05
    response = calibration_log_metric_response(rotor, lapse)
    assert response[0][0] == pytest.approx(0.15)
    assert projector_scale_response_correction(1.0, response)[0][0] == pytest.approx(-0.3)


def test_eta_one_scale_response_stress_has_expected_sign():
    response = [list(row) for row in ZERO4]
    response[1][1] = 0.25
    correction = eta_one_scale_response_stress_correction(8.0, 0.5, response)
    assert correction[1][1] == pytest.approx(4.0)


def test_common_rate_binding_gives_omega_equal_c_mu():
    mu = phase_scale_from_rotor_lapse(10.0, 2.0)
    omega = omega_magnitude_from_phase_scale(mu)
    assert omega == pytest.approx(5.0)


def test_phase_cell_volume_rewrites_as_a_fs_over_mu_cubed():
    mu = 2.0
    a_fs = math.pi
    volume_mu = phase_cell_volume_from_phase_scale(mu, a_fs)
    omega = omega_magnitude_from_phase_scale(mu)
    volume_omega = a_fs * C_LIGHT**3 / omega**3
    assert volume_mu == pytest.approx(volume_omega)


def test_occupation_density_rewrites_from_phase_scale():
    assert occupation_density_from_phase_scale(6.0, 2.0, 4.0) == pytest.approx(12.0)


def test_flrw_a_mu_is_constant():
    mu2 = flrw_phase_scale(2.0, 3.0, 6.0)
    assert mu2 == pytest.approx(1.0)
    assert 2.0 * 3.0 == pytest.approx(6.0 * mu2)


def test_fail_closed_inputs():
    with pytest.raises(RotorLapseCalibrationError):
        phase_scale_from_rotor_lapse(0.0, 1.0)
    with pytest.raises(RotorLapseCalibrationError):
        phase_scale_from_rotor_lapse(1.0, 0.0)
    with pytest.raises(RotorLapseCalibrationError):
        phase_cell_volume_from_phase_scale(0.0, 1.0)
    with pytest.raises(RotorLapseCalibrationError):
        occupation_density_from_phase_scale(-1.0, 1.0, 1.0)
