from __future__ import annotations

import math


class ADMShiftNoetherPhaseEnergyError(ValueError):
    pass


def _finite(name: str, value: float) -> float:
    value = float(value)
    if not math.isfinite(value):
        raise ADMShiftNoetherPhaseEnergyError(f"{name} must be finite")
    return value


def _positive(name: str, value: float) -> float:
    value = _finite(name, value)
    if value <= 0.0:
        raise ADMShiftNoetherPhaseEnergyError(f"{name} must be positive")
    return value


def normal_phase_rate(
    lapse: float,
    shift: float,
    phase_time_rate: float,
    phase_space_rate_c: float,
) -> float:
    """r_n=(D_t theta-c b D_x theta)/N in a local 1+1 chart."""
    lapse = _positive("lapse", lapse)
    shift = _finite("shift", shift)
    phase_time_rate = _finite("phase_time_rate", phase_time_rate)
    phase_space_rate_c = _finite("phase_space_rate_c", phase_space_rate_c)
    return (phase_time_rate - shift * phase_space_rate_c) / lapse


def directional_null_phase_rate(beta: float, omega: float, orientation: int) -> dict[str, float]:
    beta = _finite("beta", beta)
    omega = _positive("omega", omega)
    if not abs(beta) < 1.0:
        raise ADMShiftNoetherPhaseEnergyError("|beta|<1 required")
    if orientation not in (-1, 1):
        raise ADMShiftNoetherPhaseEnergyError("orientation must be +1 or -1")
    r = normal_phase_rate(1.0, beta, omega, orientation * omega)
    ratio = r / omega
    reciprocal = 1.0 / ratio
    info = reciprocal - 1.0 - math.log(reciprocal)
    conjugate = 1.0 - 1.0 / reciprocal
    dual = -math.log(1.0 - conjugate)
    return {
        "r_n": r,
        "R": ratio,
        "x": reciprocal,
        "information": info,
        "p": conjugate,
        "dual": dual,
        "epsilon_ratio": ratio,
        "phase_energy_density_ratio": ratio * ratio,
    }


def phase_energy_coordinates(amplitude: float, r_n: float) -> dict[str, float]:
    amplitude = _positive("amplitude", amplitude)
    r_n = _positive("r_n", r_n)
    j = 2.0 * amplitude * amplitude * r_n
    energy = amplitude * amplitude * r_n * r_n
    return {
        "j_theta": j,
        "energy_density": energy,
        "epsilon": energy / j,
    }


def scaled_information_candidate(omega: float, information: float) -> float:
    omega = _positive("omega", omega)
    information = _finite("information", information)
    if information < 0.0:
        raise ADMShiftNoetherPhaseEnergyError("information cost must be nonnegative")
    epsilon0 = 0.5 * omega
    return epsilon0 * information
