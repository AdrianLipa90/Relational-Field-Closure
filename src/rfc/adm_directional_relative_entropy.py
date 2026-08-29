from __future__ import annotations

import math


class ADMDirectionalRelativeEntropyError(ValueError):
    pass


def _finite(name: str, value: float) -> float:
    value = float(value)
    if not math.isfinite(value):
        raise ADMDirectionalRelativeEntropyError(f"{name} must be finite")
    return value


def _positive(name: str, value: float) -> float:
    value = _finite(name, value)
    if value <= 0.0:
        raise ADMDirectionalRelativeEntropyError(f"{name} must be positive")
    return value


def phi_ratio(x: float) -> float:
    x = _positive("x", x)
    return x - 1.0 - math.log(x)


def adm_null_characteristics(lapse: float, h11: float, shift: float) -> tuple[float, float]:
    """Return the two 1+1 ADM null coordinate speeds dx/dx0."""
    lapse = _positive("lapse", lapse)
    h11 = _positive("h11", h11)
    shift = _finite("shift", shift)
    normal_speed = lapse / math.sqrt(h11)
    return -shift + normal_speed, -shift - normal_speed


def normalized_directional_rates(lapse: float, h11: float, shift: float) -> tuple[float, float, float]:
    """Return beta_shift and positive co/counter-oriented null-rate ratios."""
    lapse = _positive("lapse", lapse)
    h11 = _positive("h11", h11)
    shift = _finite("shift", shift)
    beta_shift = shift * math.sqrt(h11) / lapse
    if not abs(beta_shift) < 1.0:
        raise ADMDirectionalRelativeEntropyError("subluminal shift ratio |b|sqrt(h)/N < 1 required")
    return beta_shift, 1.0 - beta_shift, 1.0 + beta_shift


def directional_information_from_shift(lapse: float, h11: float, shift: float) -> dict[str, float]:
    beta, r_co, r_counter = normalized_directional_rates(lapse, h11, shift)
    x_co = 1.0 / r_co
    x_counter = 1.0 / r_counter
    i_co = phi_ratio(x_co)
    i_counter = phi_ratio(x_counter)
    gamma = 1.0 / math.sqrt(1.0 - beta * beta)
    eta = math.atanh(beta)
    return {
        "beta_shift": beta,
        "rate_co": r_co,
        "rate_counter": r_counter,
        "x_co": x_co,
        "x_counter": x_counter,
        "I_co": i_co,
        "I_counter": i_counter,
        "I_even": 0.5 * (i_co + i_counter),
        "I_odd": 0.5 * (i_co - i_counter),
        "gamma": gamma,
        "rapidity": eta,
    }


def directional_information_flat(beta: float) -> tuple[float, float]:
    state = directional_information_from_shift(1.0, 1.0, beta)
    return state["I_co"], state["I_counter"]


def scaled_directional_candidate(beta: float, energy_scale: float) -> tuple[float, float]:
    energy_scale = _positive("energy_scale", energy_scale)
    i_co, i_counter = directional_information_flat(beta)
    return energy_scale * i_co, energy_scale * i_counter
