from __future__ import annotations

import math


class InformationLegendreHamiltonianError(ValueError):
    pass


def _finite(name: str, value: float) -> float:
    value = float(value)
    if not math.isfinite(value):
        raise InformationLegendreHamiltonianError(f"{name} must be finite")
    return value


def _positive(name: str, value: float) -> float:
    value = _finite(name, value)
    if value <= 0.0:
        raise InformationLegendreHamiltonianError(f"{name} must be positive")
    return value


def phi(x: float) -> float:
    x = _positive("x", x)
    return x - 1.0 - math.log(x)


def phi_prime(x: float) -> float:
    x = _positive("x", x)
    return 1.0 - 1.0 / x


def phi_second(x: float) -> float:
    x = _positive("x", x)
    return 1.0 / (x * x)


def x_from_conjugate(p: float) -> float:
    p = _finite("p", p)
    if not p < 1.0:
        raise InformationLegendreHamiltonianError("conjugate coordinate p<1 required")
    return 1.0 / (1.0 - p)


def psi(p: float) -> float:
    p = _finite("p", p)
    if not p < 1.0:
        raise InformationLegendreHamiltonianError("conjugate coordinate p<1 required")
    return -math.log(1.0 - p)


def fenchel_defect(x: float, p: float) -> float:
    return phi(x) + psi(p) - p * x


def directional_dual(beta: float) -> dict[str, float]:
    beta = _finite("beta", beta)
    if not abs(beta) < 1.0:
        raise InformationLegendreHamiltonianError("|beta|<1 required")
    x_co = 1.0 / (1.0 - beta)
    x_counter = 1.0 / (1.0 + beta)
    p_co = phi_prime(x_co)
    p_counter = phi_prime(x_counter)
    psi_co = psi(p_co)
    psi_counter = psi(p_counter)
    return {
        "x_co": x_co,
        "x_counter": x_counter,
        "p_co": p_co,
        "p_counter": p_counter,
        "phi_co": phi(x_co),
        "phi_counter": phi(x_counter),
        "psi_co": psi_co,
        "psi_counter": psi_counter,
        "psi_even": 0.5 * (psi_co + psi_counter),
        "psi_odd": 0.5 * (psi_co - psi_counter),
        "rapidity": math.atanh(beta),
        "log_gamma": -0.5 * math.log(1.0 - beta * beta),
    }


def scaled_primal_dual(beta: float, energy_scale: float) -> dict[str, float]:
    energy_scale = _positive("energy_scale", energy_scale)
    state = directional_dual(beta)
    return {
        "E_phi_co": energy_scale * state["phi_co"],
        "E_phi_counter": energy_scale * state["phi_counter"],
        "E_psi_co": energy_scale * state["psi_co"],
        "E_psi_counter": energy_scale * state["psi_counter"],
    }
