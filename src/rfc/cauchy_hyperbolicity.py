from __future__ import annotations

import math
from typing import Tuple

import numpy as np


def _positive_finite(name: str, value: float) -> float:
    value = float(value)
    if not math.isfinite(value) or value <= 0.0:
        raise ValueError(f"{name} must be positive finite")
    return value


def _vector(name: str, value) -> np.ndarray:
    arr = np.asarray(value, dtype=float)
    if arr.ndim != 1 or not np.all(np.isfinite(arr)):
        raise ValueError(f"{name} must be a finite vector")
    return arr


def _positive_definite_inverse_metric(value, n: int) -> np.ndarray:
    h_inv = np.asarray(value, dtype=float)
    if h_inv.shape != (n, n) or not np.all(np.isfinite(h_inv)):
        raise ValueError("h_inverse must be a finite square matrix matching the spatial dimension")
    if not np.allclose(h_inv, h_inv.T, rtol=0.0, atol=1e-12):
        raise ValueError("h_inverse must be symmetric")
    eig = np.linalg.eigvalsh(h_inv)
    if not np.all(eig > 0.0):
        raise ValueError("h_inverse must be positive definite")
    return h_inv


def spatial_quadratic_form(h_inverse, covector) -> float:
    k = _vector("covector", covector)
    h_inv = _positive_definite_inverse_metric(h_inverse, k.size)
    return float(k @ h_inv @ k)


def principal_symbol(xi0: float, covector, lapse: float, shift, h_inverse) -> float:
    lapse = _positive_finite("lapse", lapse)
    k = _vector("covector", covector)
    b = _vector("shift", shift)
    if b.shape != k.shape:
        raise ValueError("shift and covector must have the same dimension")
    h_inv = _positive_definite_inverse_metric(h_inverse, k.size)
    xi0 = float(xi0)
    if not math.isfinite(xi0):
        raise ValueError("xi0 must be finite")
    b_dot_k = float(np.dot(b, k))
    q_h = float(k @ h_inv @ k)
    return -((xi0 - b_dot_k) ** 2) / lapse**2 + q_h


def characteristic_roots(lapse: float, shift, h_inverse, covector) -> Tuple[float, float]:
    lapse = _positive_finite("lapse", lapse)
    k = _vector("covector", covector)
    b = _vector("shift", shift)
    if b.shape != k.shape:
        raise ValueError("shift and covector must have the same dimension")
    h_inv = _positive_definite_inverse_metric(h_inverse, k.size)
    q_h = float(k @ h_inv @ k)
    if not q_h > 0.0:
        raise ValueError("strict hyperbolicity requires a nonzero spatial covector")
    center = float(np.dot(b, k))
    half_gap = lapse * math.sqrt(q_h)
    return center - half_gap, center + half_gap


def hyperbolicity_gap(lapse: float, h_inverse, covector) -> float:
    lapse = _positive_finite("lapse", lapse)
    k = _vector("covector", covector)
    h_inv = _positive_definite_inverse_metric(h_inverse, k.size)
    q_h = float(k @ h_inv @ k)
    if not q_h > 0.0:
        raise ValueError("strict hyperbolicity requires a nonzero spatial covector")
    return 2.0 * lapse * math.sqrt(q_h)


def normal_derivative(phi_0: float, lapse: float, shift, grad_phi) -> float:
    lapse = _positive_finite("lapse", lapse)
    b = _vector("shift", shift)
    grad = _vector("grad_phi", grad_phi)
    if b.shape != grad.shape:
        raise ValueError("shift and grad_phi must have the same dimension")
    phi_0 = float(phi_0)
    if not math.isfinite(phi_0):
        raise ValueError("phi_0 must be finite")
    return (phi_0 - float(np.dot(b, grad))) / lapse


def coordinate_time_derivative(pi: float, lapse: float, shift, grad_phi) -> float:
    lapse = _positive_finite("lapse", lapse)
    b = _vector("shift", shift)
    grad = _vector("grad_phi", grad_phi)
    if b.shape != grad.shape:
        raise ValueError("shift and grad_phi must have the same dimension")
    pi = float(pi)
    if not math.isfinite(pi):
        raise ValueError("pi must be finite")
    return lapse * pi + float(np.dot(b, grad))


def cauchy_energy_density(pi: float, phi: float, grad_phi, h_inverse, mass_sq: float) -> float:
    grad = _vector("grad_phi", grad_phi)
    h_inv = _positive_definite_inverse_metric(h_inverse, grad.size)
    pi = float(pi)
    phi = float(phi)
    mass_sq = float(mass_sq)
    if not all(math.isfinite(v) for v in (pi, phi, mass_sq)) or mass_sq < 0.0:
        raise ValueError("pi, phi and nonnegative mass_sq must be finite")
    spatial = float(grad @ h_inv @ grad)
    return 0.5 * (pi**2 + spatial + mass_sq * phi**2)
