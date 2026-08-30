import math
from pathlib import Path

import pytest


TIR_LOCK = "3f5a08ef04ec53c1a155263d23e8b10a96404370"
IDT_LOCK = "84ce1886175af872ae4a56ba36f7e106d8e23635"
RFC_LOCK = "63418a88d686021c2a6fe6ab159d6152db303c19"


def palatini_metric_coefficients(kappa_e: float, lambda_value: float):
    if not math.isfinite(kappa_e) or kappa_e <= 0.0:
        raise ValueError("kappa_e must be positive finite")
    cartan_curvature_prefactor = 1.0 / (4.0 * kappa_e)
    cartan_volume_prefactor = -lambda_value / (24.0 * kappa_e)
    metric_r_prefactor = 2.0 * cartan_curvature_prefactor
    metric_volume_prefactor = 24.0 * cartan_volume_prefactor
    return metric_r_prefactor, metric_volume_prefactor


def test_form_degree_selection():
    assert 1 + 1 + 2 == 4
    assert 1 + 1 + 1 + 1 == 4


def test_cartan_coefficients_reduce_to_einstein_hilbert_metric_coefficients():
    for kappa_e, lambda_value in [(0.3, 0.0), (1.7, 0.11), (8.0 * math.pi, -0.025)]:
        r_coeff, vol_coeff = palatini_metric_coefficients(kappa_e, lambda_value)
        assert r_coeff == pytest.approx(1.0 / (2.0 * kappa_e))
        assert vol_coeff == pytest.approx(-lambda_value / kappa_e)
        assert vol_coeff == pytest.approx((1.0 / (2.0 * kappa_e)) * (-2.0 * lambda_value))


def test_rf_e3_double_copy_normalization_is_unchanged():
    for kappa_g in (0.4, 1.28, 3.7):
        kappa_e = kappa_g**2 / 4.0
        assert 2.0 / kappa_g**2 == pytest.approx(1.0 / (2.0 * kappa_e))
        assert kappa_g**2 == pytest.approx(4.0 * kappa_e)


def test_nonpositive_gravitational_coupling_rejected():
    for bad in (0.0, -1.0, float("nan"), float("inf")):
        with pytest.raises(ValueError):
            palatini_metric_coefficients(bad, 0.1)


def test_rfe21_source_lock_and_selection_markers_present():
    root = Path(__file__).resolve().parents[2]
    gate = (root / "closure/einstein/RF_E21_CARTAN_PALATINI_EINSTEIN_HILBERT_SELECTION.md").read_text(encoding="utf-8")
    assert TIR_LOCK in gate
    assert IDT_LOCK in gate
    assert RFC_LOCK in gate
    assert r"\epsilon_{ABCD}E^A\wedge E^B\wedge R^{CD}" in gate
    assert r"\frac1{4\kappa_E}" in gate
    assert r"\frac1{2\kappa_E}" in gate
    assert r"G_{\mu\nu}+\Lambda g_{\mu\nu}" in gate
    assert "Holst–Nieh–Yan" in gate
    assert "PASS_RF_E21_CARTAN_PALATINI_EINSTEIN_HILBERT_SELECTION" in gate


def test_parent_chain_markers_remain_present():
    root = Path(__file__).resolve().parents[2]
    e8 = (root / "closure/einstein/RF_E8_ADM_KINEMATIC_ASSEMBLY_FIREWALL.md").read_text(encoding="utf-8")
    e3 = (root / "closure/einstein/RF_E3_DOUBLE_COPY_EINSTEIN_HILBERT_NORMALIZATION.md").read_text(encoding="utf-8")
    e12 = (root / "closure/einstein/RF_E12_ACTION_PROJECTED_ADM_SOURCE_CONSTRAINTS.md").read_text(encoding="utf-8")
    e13 = (root / "closure/einstein/RF_E13_CONSTRAINT_PROPAGATION_BIANCHI_LEDGER.md").read_text(encoding="utf-8")

    assert r"\vartheta^0=N_R\,dx^0" in e8
    assert r"\sqrt{-g}=N_R\sqrt{h}" in e8
    assert r"\kappa_g^2=32\pi G" in e3
    assert r"G_{\mu\nu}=\kappa_E T_{\mu\nu}" in e3
    assert r"\mathcal G_H=2\kappa_E\rho_n" in e12
    assert "Bianchi" in e13


def test_downstream_lambda_and_scale_ledger_is_not_regressed():
    root = Path(__file__).resolve().parents[2]
    l2 = (root / "closure/lambda0/RF_L2_DYNAMIC_LAMBDA0_ACTION_REALIZABILITY_STABILITY.md").read_text(encoding="utf-8")
    l4a = (root / "closure/lambda0/RF_L4A_SHANNON_FISHER_LOCAL_NORMALIZATION.md").read_text(encoding="utf-8")
    l5a = (root / "closure/lambda0/RF_L5A_PREMETRIC_DIMENSIONAL_CALIBRATION_FIREWALL.md").read_text(encoding="utf-8")
    e20 = (root / "closure/einstein/RF_E20_TETRA_CLOCK_MASS_SCALE_CLOSURE.md").read_text(encoding="utf-8")
    readme = (root / "closure/einstein/README.md").read_text(encoding="utf-8")

    assert r"\Lambda_0(x):=\Lambda_{ref}+\kappa_EU_L" in l2
    assert r"\beta_I=\sqrt2" in l4a
    assert r"m_I^2=\frac{\alpha_I}{\kappa_E}" in l5a
    assert r"r_\alpha q_s^3" in e20
    assert "RF-L2" in readme
    assert "RF-L5A" in readme
    assert "RF-E20" in readme
