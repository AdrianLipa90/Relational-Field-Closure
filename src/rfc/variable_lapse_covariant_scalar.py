from __future__ import annotations

import math
from typing import Tuple

import numpy as np


def _positive_finite(name: str, value: float) -> float:
    value = float(value)
    if not math.isfinite(value) or value <= 0.0:
        raise ValueError(f"{name} must be positive finite")
    return value


def _finite_vector(name: str, value) -> np.ndarray:
    arr = np.asarray(value, dtype=float)
    if arr.ndim != 1 or not np.all(np.isfinite(arr)):
        raise ValueError(f"{name} must be a finite vector")
    return arr


def _finite_square(name: str, value, n: int) -> np.ndarray:
    arr = np.asarray(value, dtype=float)
    if arr.shape != (n, n) or not np.all(np.isfinite(arr)):
        raise ValueError(f"{name} must be a finite {n}x{n} matrix")
    return arr


def adm_scalar_densitized_flux(
    lapse: float,
    sqrt_h: float,
    shift,
    h_inverse,
    phi_0: float,
    grad_phi,
) -> Tuple[float, np.ndarray]:
    """Return J^mu = sqrt(-g) g^{mu nu} partial_nu phi for RF-E8 ADM data."""
    lapse = _positive_finite("lapse", lapse)
    sqrt_h = _positive_finite("sqrt_h", sqrt_h)
    shift = _finite_vector("shift", shift)
    grad_phi = _finite_vector("grad_phi", grad_phi)
    if grad_phi.shape != shift.shape:
        raise ValueError("grad_phi and shift must have the same dimension")
    h_inverse = _finite_square("h_inverse", h_inverse, shift.size)
    phi_0 = float(phi_0)
    if not math.isfinite(phi_0):
        raise ValueError("phi_0 must be finite")

    d0_phi = phi_0 - float(np.dot(shift, grad_phi))
    j0 = -(sqrt_h / lapse) * d0_phi
    ji = lapse * sqrt_h * (h_inverse @ grad_phi) + (sqrt_h / lapse) * shift * d0_phi
    return float(j0), ji


def box_from_densitized_flux_divergence(
    lapse: float,
    sqrt_h: float,
    d_j0_dx0: float,
    spatial_divergence_ji: float,
) -> float:
    """Return Box(phi) from partial_mu J^mu divided by sqrt(-g)=N sqrt(h)."""
    lapse = _positive_finite("lapse", lapse)
    sqrt_h = _positive_finite("sqrt_h", sqrt_h)
    values = (float(d_j0_dx0), float(spatial_divergence_ji))
    if not all(math.isfinite(v) for v in values):
        raise ValueError("flux divergences must be finite")
    return (values[0] + values[1]) / (lapse * sqrt_h)


def time_only_zero_shift_box(
    phi_0: float,
    phi_00: float,
    lapse: float,
    lapse_0: float,
    log_sqrt_h_0: float = 0.0,
) -> float:
    """Exact Box(phi) for spatially homogeneous phi with b=0."""
    lapse = _positive_finite("lapse", lapse)
    vals = tuple(float(v) for v in (phi_0, phi_00, lapse_0, log_sqrt_h_0))
    if not all(math.isfinite(v) for v in vals):
        raise ValueError("derivative data must be finite")
    p0, p00, n0, theta_h = vals
    return -(p00 / lapse**2) - (theta_h * p0 / lapse**2) + (n0 * p0 / lapse**3)


def static_zero_shift_1d_box(
    phi_x: float,
    phi_xx: float,
    lapse: float,
    lapse_x: float,
    h_xx: float,
    h_xx_x: float,
) -> float:
    """Exact static 1D reduction for ds^2=-N^2(dx0)^2+h_xx dx^2."""
    lapse = _positive_finite("lapse", lapse)
    h_xx = _positive_finite("h_xx", h_xx)
    vals = tuple(float(v) for v in (phi_x, phi_xx, lapse_x, h_xx_x))
    if not all(math.isfinite(v) for v in vals):
        raise ValueError("derivative data must be finite")
    px, pxx, nx, hx = vals
    return pxx / h_xx + px * (nx / (lapse * h_xx) - hx / (2.0 * h_xx**2))


def constant_adm_kg_dispersion_residual(
    omega: float,
    wave_number: float,
    lapse: float,
    shift: float,
    h_xx: float,
    mass_sq: float,
) -> float:
    """1D constant-coefficient residual for Box(phi)-m^2 phi=0."""
    lapse = _positive_finite("lapse", lapse)
    h_xx = _positive_finite("h_xx", h_xx)
    mass_sq = float(mass_sq)
    vals = tuple(float(v) for v in (omega, wave_number, shift))
    if not all(math.isfinite(v) for v in vals) or not math.isfinite(mass_sq) or mass_sq < 0.0:
        raise ValueError("dispersion data must be finite and mass_sq nonnegative")
    omega, k, shift = vals
    return ((omega + shift * k) ** 2) / lapse**2 - k**2 / h_xx - mass_sq


def information_mass_sq(alpha_i: float, kappa_e: float) -> float:
    alpha_i = float(alpha_i)
    kappa_e = _positive_finite("kappa_e", kappa_e)
    if not math.isfinite(alpha_i) or alpha_i < 0.0:
        raise ValueError("alpha_i must be finite and nonnegative")
    return alpha_i / kappa_e
