import math

import pytest

from src.rfc.gamma_carrier_identifiability_firewall import (
    GammaCarrierIdentifiabilityError,
    GammaCarrierInputs,
    IdentifiabilityProvenance,
    build_gamma_carrier_identifiability_receipt,
    receipt_passes,
)


def provenance(**overrides):
    values = dict(
        alpha_c_source_id="RFG4_ALPHA_SOURCE",
        source_operator_receipt_id="RFC_SOURCE_OPERATOR_RECEIPT",
        current_receipt_id="RF_F24_CURRENT_RECEIPT",
        phase_rate_receipt_id="RF_F21_RATE_RECEIPT",
        gamma_source_id="PROJECT_GAMMA_NORMALIZATION_RECEIPT",
        carrier_type_source_id="RFN1C4_CARRIER_TYPE_RECEIPT",
        gravity_output_id="RF_F25_GRAVITY_OUTPUT",
        horizon_provenance_id=None,
    )
    values.update(overrides)
    return IdentifiabilityProvenance(**values)


def inputs(**overrides):
    values = dict(
        alpha_c=0.5,
        omega_q=4.0,
        source_s_r=2.0,
        current_j_q=2.0,
        gamma_dc=1.0,
        zeta_m=1.0,
        provenance=provenance(),
    )
    values.update(overrides)
    return GammaCarrierInputs(**values)


def test_source_route_identifies_gamma_over_zeta_not_gamma_alone():
    receipt = build_gamma_carrier_identifiability_receipt(inputs())
    assert receipt_passes(receipt)
    assert receipt["gamma_over_zeta_source"] == pytest.approx(1.0)
    assert receipt["gamma_from_source_given_zeta"] == pytest.approx(1.0)


def test_source_reduced_scale_and_kappa_close_exactly():
    receipt = build_gamma_carrier_identifiability_receipt(inputs())
    assert receipt["g_source"] == pytest.approx(1.0 / (8.0 * math.pi))
    assert receipt["mbar_source"] == pytest.approx(1.0)
    assert receipt["kappa_e_source"] == pytest.approx(1.0)


def test_total_rest_branch_requires_double_gamma_for_same_gravity_scale():
    kinetic = build_gamma_carrier_identifiability_receipt(inputs())
    rest = build_gamma_carrier_identifiability_receipt(inputs(gamma_dc=2.0, zeta_m=2.0))
    assert receipt_passes(rest)
    assert rest["gamma_over_zeta_candidate"] == pytest.approx(
        kinetic["gamma_over_zeta_candidate"]
    )
    assert rest["branch_gamma_ratio"] == pytest.approx(2.0)
    assert rest["gamma_total_rest_branch"] == pytest.approx(2.0)


def test_same_gamma_on_rest_branch_fails_ratio_gate():
    receipt = build_gamma_carrier_identifiability_receipt(inputs(zeta_m=2.0))
    assert receipt["defects"]["gamma_over_zeta_source"] > 0.0
    assert not receipt_passes(receipt)


def test_general_independent_zeta_scales_gamma_linearly():
    receipt = build_gamma_carrier_identifiability_receipt(
        inputs(gamma_dc=1.5, zeta_m=1.5)
    )
    assert receipt_passes(receipt)
    assert receipt["gamma_from_source_given_zeta"] == pytest.approx(1.5)


def test_source_formula_is_alpha_sqrt_omega_s_over_j():
    receipt = build_gamma_carrier_identifiability_receipt(inputs())
    expected = 0.5 * math.sqrt(4.0 * 2.0 / 2.0)
    assert receipt["gamma_over_zeta_source"] == pytest.approx(expected)


def test_independent_horizon_route_closes_same_ratio_and_holonomy():
    p = provenance(horizon_provenance_id="INDEPENDENT_HORIZON_RECEIPT")
    receipt = build_gamma_carrier_identifiability_receipt(
        inputs(provenance=p, horizon_mass=4.0, horizon_temperature=0.25)
    )
    assert receipt_passes(receipt)
    assert receipt["horizon"]["mbar_horizon"] == pytest.approx(1.0)
    assert receipt["horizon"]["gamma_over_zeta_horizon"] == pytest.approx(1.0)
    assert receipt["horizon"]["source_horizon_left"] == pytest.approx(
        receipt["horizon"]["source_horizon_right"]
    )


def test_perturbed_horizon_detects_cross_route_failure():
    p = provenance(horizon_provenance_id="INDEPENDENT_HORIZON_RECEIPT")
    receipt = build_gamma_carrier_identifiability_receipt(
        inputs(provenance=p, horizon_mass=4.0, horizon_temperature=0.30)
    )
    assert receipt["defects"]["source_horizon_ratio"] > 0.0
    assert receipt["defects"]["source_horizon_holonomy"] > 0.0
    assert not receipt_passes(receipt)


def test_horizon_provenance_cannot_reuse_gravity_output():
    p = provenance(horizon_provenance_id="RF_F25_GRAVITY_OUTPUT")
    receipt = build_gamma_carrier_identifiability_receipt(
        inputs(provenance=p, horizon_mass=4.0, horizon_temperature=0.25)
    )
    assert receipt["defects"]["horizon_provenance_independence"] == 1.0
    assert not receipt_passes(receipt)


def test_gravity_target_cannot_select_gamma_or_carrier_type():
    gamma_fit = build_gamma_carrier_identifiability_receipt(
        inputs(gravity_target_used_for_gamma_selection=True)
    )
    type_fit = build_gamma_carrier_identifiability_receipt(
        inputs(gravity_target_used_for_carrier_type_selection=True)
    )
    assert not receipt_passes(gamma_fit)
    assert not receipt_passes(type_fit)


def test_input_provenance_cannot_collide_with_gravity_output():
    p = provenance(gamma_source_id="RF_F25_GRAVITY_OUTPUT")
    receipt = build_gamma_carrier_identifiability_receipt(inputs(provenance=p))
    assert receipt["defects"]["provenance_collision"] == 1.0
    assert not receipt_passes(receipt)


def test_horizon_inputs_must_be_complete_and_provenanced():
    with pytest.raises(GammaCarrierIdentifiabilityError):
        inputs(horizon_mass=4.0)
    with pytest.raises(GammaCarrierIdentifiabilityError):
        inputs(horizon_mass=4.0, horizon_temperature=0.25)


def test_nonpositive_or_nonfinite_inputs_fail_closed():
    with pytest.raises(GammaCarrierIdentifiabilityError):
        inputs(zeta_m=0.0)
    with pytest.raises(GammaCarrierIdentifiabilityError):
        inputs(alpha_c=math.nan)


def test_horizon_route_is_optional():
    receipt = build_gamma_carrier_identifiability_receipt(inputs())
    assert receipt["horizon"] is None
    assert receipt_passes(receipt)


def test_tolerance_is_explicit():
    receipt = build_gamma_carrier_identifiability_receipt(inputs(gamma_dc=1.0 + 1e-12))
    assert not receipt_passes(receipt)
    assert receipt_passes(receipt, atol=2e-12)
