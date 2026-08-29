from __future__ import annotations

import math
from collections.abc import Sequence


C_LIGHT = 299_792_458.0


class RotorLapseCalibrationError(ValueError):
    pass


def _finite(name: str, value: float) -> float:
    value = float(value)
    if not math.isfinite(value):
        raise RotorLapseCalibrationError(f"{name} must be finite")
    return value


def _positive(name: str, value: float) -> float:
    value = _finite(name, value)
    if value <= 0.0:
        raise RotorLapseCalibrationError(f"{name} must be positive")
    return value


def _mat4(name: str, values: Sequence[Sequence[float]]) -> tuple[tuple[float, ...], ...]:
    if len(values) != 4 or any(len(row) != 4 for row in values):
        raise RotorLapseCalibrationError(f"{name} must be 4x4")
    return tuple(
        tuple(_finite(f"{name}[{i}][{j}]", value) for j, value in enumerate(row))
        for i, row in enumerate(values)
    )


def phase_scale_from_rotor_lapse(
    rotor_coordinate_rate: float,
    lapse_ratio: float,
    *,
    c_light: float = C_LIGHT,
) -> float:
    """mu_vartheta=|D_t chi|_rotor/(N_R c)."""
    rate = _finite("rotor_coordinate_rate", rotor_coordinate_rate)
    if rate == 0.0:
        raise RotorLapseCalibrationError("rotor_coordinate_rate must be nonzero")
    lapse = _positive("lapse_ratio", lapse_ratio)
    c = _positive("c_light", c_light)
    return abs(rate) / (lapse * c)


def proper_rotor_rate(rotor_coordinate_rate: float, lapse_ratio: float) -> float:
    rate = _finite("rotor_coordinate_rate", rotor_coordinate_rate)
    lapse = _positive("lapse_ratio", lapse_ratio)
    return rate / lapse


def coordinate_rate_binding_defect(field_coordinate_rate: float, rotor_coordinate_rate: float) -> float:
    field = _finite("field_coordinate_rate", field_coordinate_rate)
    rotor = _finite("rotor_coordinate_rate", rotor_coordinate_rate)
    if rotor == 0.0:
        raise RotorLapseCalibrationError("rotor_coordinate_rate must be nonzero")
    return abs(field - rotor) / abs(rotor)


def proper_rate_binding_defect(
    field_proper_rate: float,
    rotor_coordinate_rate: float,
    lapse_ratio: float,
) -> float:
    field = _finite("field_proper_rate", field_proper_rate)
    rotor_proper = proper_rotor_rate(rotor_coordinate_rate, lapse_ratio)
    if rotor_proper == 0.0:
        raise RotorLapseCalibrationError("rotor proper rate must be nonzero")
    return abs(field - rotor_proper) / abs(rotor_proper)


def pure_normal_projector_from_rates(
    field_proper_rate: float,
    rotor_coordinate_rate: float,
    lapse_ratio: float,
) -> float:
    """On a pure-normal phase one-form, C=(r_field_proper/r_rotor_proper)^2."""
    field = _finite("field_proper_rate", field_proper_rate)
    rotor_proper = proper_rotor_rate(rotor_coordinate_rate, lapse_ratio)
    if rotor_proper == 0.0:
        raise RotorLapseCalibrationError("rotor proper rate must be nonzero")
    return (field / rotor_proper) ** 2


def calibration_log_metric_response(
    rotor_rate_log_metric_response: Sequence[Sequence[float]],
    lapse_log_metric_response: Sequence[Sequence[float]],
) -> tuple[tuple[float, ...], ...]:
    """S_mn=partial ln(mu)/partial g^{mn}=S_rotor-S_lapse."""
    rotor = _mat4("rotor_rate_log_metric_response", rotor_rate_log_metric_response)
    lapse = _mat4("lapse_log_metric_response", lapse_log_metric_response)
    return tuple(tuple(rotor[i][j] - lapse[i][j] for j in range(4)) for i in range(4))


def projector_scale_response_correction(
    projector_value: float,
    scale_log_metric_response: Sequence[Sequence[float]],
) -> tuple[tuple[float, ...], ...]:
    """Additional metric derivative from variable mu: -2 C S_mn."""
    C = _finite("projector_value", projector_value)
    response = _mat4("scale_log_metric_response", scale_log_metric_response)
    return tuple(tuple(-2.0 * C * response[i][j] for j in range(4)) for i in range(4))


def eta_one_scale_response_stress_correction(
    u_hat_value: float,
    f_prime_at_one: float,
    scale_log_metric_response: Sequence[Sequence[float]],
) -> tuple[tuple[float, ...], ...]:
    """At C=1, eta=1 the scale-response stress correction is +4 U f'(1) S_mn."""
    U = _finite("u_hat_value", u_hat_value)
    fp = _finite("f_prime_at_one", f_prime_at_one)
    response = _mat4("scale_log_metric_response", scale_log_metric_response)
    return tuple(tuple(4.0 * U * fp * response[i][j] for j in range(4)) for i in range(4))


def spacetime_log_phase_scale_rate(
    rotor_coordinate_rate_log_derivative: float,
    lapse_log_derivative: float,
) -> float:
    """Along spacetime flow: d ln(mu)/d tau=d ln|r_t^rot|/d tau-d ln N_R/d tau."""
    return _finite("rotor_coordinate_rate_log_derivative", rotor_coordinate_rate_log_derivative) - _finite(
        "lapse_log_derivative", lapse_log_derivative
    )


def omega_magnitude_from_phase_scale(mu_phase: float, *, c_light: float = C_LIGHT) -> float:
    mu = _positive("mu_phase", mu_phase)
    c = _positive("c_light", c_light)
    return c * mu


def phase_cell_volume_from_phase_scale(mu_phase: float, area_fs_dimensionless: float) -> float:
    mu = _positive("mu_phase", mu_phase)
    area = _positive("area_fs_dimensionless", area_fs_dimensionless)
    return area / (mu**3)


def occupation_density_from_phase_scale(
    occupation: float,
    mu_phase: float,
    area_fs_dimensionless: float,
) -> float:
    N = _finite("occupation", occupation)
    if N < 0.0:
        raise RotorLapseCalibrationError("occupation must be nonnegative")
    mu = _positive("mu_phase", mu_phase)
    area = _positive("area_fs_dimensionless", area_fs_dimensionless)
    return N * mu**3 / area


def flrw_phase_scale(a_reference: float, mu_reference: float, a_value: float) -> float:
    """RF-F12 a|omega|=const and |omega|=c mu imply a mu=const."""
    a0 = _positive("a_reference", a_reference)
    mu0 = _positive("mu_reference", mu_reference)
    a = _positive("a_value", a_value)
    return a0 * mu0 / a
