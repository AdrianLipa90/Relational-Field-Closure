import math
from pathlib import Path

import numpy as np
import pytest

from src.rfc.variable_lapse_covariant_scalar import (
    adm_scalar_densitized_flux,
    box_from_densitized_flux_divergence,
    constant_adm_kg_dispersion_residual,
    information_mass_sq,
    static_zero_shift_1d_box,
    time_only_zero_shift_box,
)


def test_adm_densitized_flux_matches_direct_inverse_metric_contraction():
    lapse = 1.7
    h = np.array([[1.4, 0.1], [0.1, 0.9]])
    h_inv = np.linalg.inv(h)
    sqrt_h = math.sqrt(np.linalg.det(h))
    shift = np.array([0.2, -0.15])
    grad = np.array([0.7, -0.4])
    phi_0 = -0.3

    j0, ji = adm_scalar_densitized_flux(lapse, sqrt_h, shift, h_inv, phi_0, grad)

    g_inv = np.empty((3, 3))
    g_inv[0, 0] = -1.0 / lapse**2
    g_inv[0, 1:] = shift / lapse**2
    g_inv[1:, 0] = shift / lapse**2
    g_inv[1:, 1:] = h_inv - np.outer(shift, shift) / lapse**2
    dphi = np.concatenate(([phi_0], grad))
    direct = lapse * sqrt_h * (g_inv @ dphi)

    assert j0 == pytest.approx(direct[0])
    assert ji == pytest.approx(direct[1:])


def test_box_divergence_divides_by_adm_volume_density():
    got = box_from_densitized_flux_divergence(2.0, 3.0, -7.0, 1.0)
    assert got == pytest.approx(-1.0)


def test_time_dependent_homogeneous_lapse_term():
    phi_0 = 1.2
    phi_00 = -0.8
    lapse = 1.5
    lapse_0 = 0.4
    theta_h = -0.3
    got = time_only_zero_shift_box(phi_0, phi_00, lapse, lapse_0, theta_h)
    expected = -phi_00 / lapse**2 - theta_h * phi_0 / lapse**2 + lapse_0 * phi_0 / lapse**3
    assert got == pytest.approx(expected)


def test_static_zero_shift_1d_exact_reduction():
    x = 0.4
    lapse = 1.0 + x
    lapse_x = 1.0
    h_xx = 1.0 + x**2
    h_xx_x = 2.0 * x
    phi_x = 3.0 * x**2
    phi_xx = 6.0 * x

    got = static_zero_shift_1d_box(phi_x, phi_xx, lapse, lapse_x, h_xx, h_xx_x)
    expected = phi_xx / h_xx + phi_x * (
        lapse_x / (lapse * h_xx) - h_xx_x / (2.0 * h_xx**2)
    )
    assert got == pytest.approx(expected)


def test_local_flat_rfl5a_limit_and_mass_binding():
    alpha_i = 0.18
    kappa_e = 0.6
    mass_sq = information_mass_sq(alpha_i, kappa_e)
    assert mass_sq == pytest.approx(0.3)

    k = 0.8
    omega = math.sqrt(k**2 + mass_sq)
    residual = constant_adm_kg_dispersion_residual(omega, k, 1.0, 0.0, 1.0, mass_sq)
    assert residual == pytest.approx(0.0, abs=1e-14)


def test_constant_shift_dispersion_uses_normal_frequency_combination():
    lapse = 1.4
    shift = -0.25
    h_xx = 1.2
    mass_sq = 0.35
    k = 0.9
    normal_frequency = lapse * math.sqrt(k**2 / h_xx + mass_sq)
    omega = normal_frequency - shift * k
    assert constant_adm_kg_dispersion_residual(
        omega, k, lapse, shift, h_xx, mass_sq
    ) == pytest.approx(0.0, abs=1e-14)


def test_invalid_geometry_fails_closed():
    for bad_lapse in (0.0, -1.0, float("nan"), float("inf")):
        with pytest.raises(ValueError):
            adm_scalar_densitized_flux(bad_lapse, 1.0, [0.0], [[1.0]], 0.0, [0.0])

    with pytest.raises(ValueError):
        static_zero_shift_1d_box(0.0, 0.0, 1.0, 0.0, 0.0, 0.0)
    with pytest.raises(ValueError):
        constant_adm_kg_dispersion_residual(1.0, 1.0, 1.0, 0.0, 1.0, -0.1)


def test_document_contract_and_parent_markers_present():
    root = Path(__file__).resolve().parents[2]
    gate = (root / "closure/lambda0/RF_L6_VARIABLE_LAPSE_CURVED_COVARIANT_PROPAGATION.md").read_text(encoding="utf-8")
    e8 = (root / "closure/einstein/RF_E8_ADM_KINEMATIC_ASSEMBLY_FIREWALL.md").read_text(encoding="utf-8")
    l2 = (root / "closure/lambda0/RF_L2_DYNAMIC_LAMBDA0_ACTION_REALIZABILITY_STABILITY.md").read_text(encoding="utf-8")
    l5a = (root / "closure/lambda0/RF_L5A_PREMETRIC_DIMENSIONAL_CALIBRATION_FIREWALL.md").read_text(encoding="utf-8")
    idt_lapse = (root / "formalism/RFN0_RELATIONAL_LAPSE_CLOCK_DYNAMICS.md").read_text(encoding="utf-8")

    assert r"\sqrt{-g}=N_R\sqrt{h}" in e8
    assert r"\Box\phi_L-U_L'(\phi_L)=0" in l2
    assert r"M_{eff}\frac{\Gamma_x^2}{\Gamma_t^2}=c^2" in l5a
    assert r"N_R" in idt_lapse
    assert r"\mathcal D_0\phi" in gate
    assert r"\Box_g\phi_I-m_I^2\phi_I=0" in gate
    assert "PASS_RF_L6_VARIABLE_LAPSE_CURVED_COVARIANT_PROPAGATION" in gate
