import math

import pytest

from src.rfc.project_coupling_promotion_firewall import (
    CouplingProvenance,
    ProjectCouplingInputs,
    ProjectCouplingPromotionError,
    build_project_coupling_promotion_receipt,
    receipt_passes,
)


def provenance(**overrides):
    values = dict(
        bcj_receipt_id="RFG29_RFG30_REFERENCE_RECEIPTS",
        bcj_authority="REFERENCE_RECEIPT",
        wilson_source_id="PROJECT_WILSON_ACTION_RECEIPT",
        wilson_authority="DERIVED_PROJECT_ACTION",
        gamma_source_id="PROJECT_DOUBLE_COPY_NORMALIZATION_RECEIPT",
        gamma_authority="REFERENCE_RECEIPT",
        carrier_scale_source_id="RFN1C4_CARRIER_SCALE_RECEIPT",
        carrier_scale_authority="REFERENCE_RECEIPT",
        gravity_output_id="RF_F25_REDUCED_GRAVITY_OUTPUT",
    )
    values.update(overrides)
    return CouplingProvenance(**values)


def inputs(**overrides):
    values = dict(
        beta_w=6.0,
        g_ym_squared=1.0,
        gamma_dc=2.0,
        m_star=3.0,
        epsilon_q=3.0,
        carrier_type="KINETIC_CARRIER",
        bcj_graph_count=15,
        bcj_independent_jacobi_rank=9,
        bcj_jacobi_defect=0.0,
        bcj_reconstruction_defect=0.0,
        bcj_klt_defect=0.0,
        bcj_ward_defect=0.0,
        gravity_target_used_for_bcj_selection=False,
        gravity_target_used_for_beta_selection=False,
        gravity_target_used_for_gamma_selection=False,
        gravity_target_used_for_mstar_selection=False,
        provenance=provenance(),
    )
    values.update(overrides)
    return ProjectCouplingInputs(**values)


def test_zero_defect_kinetic_surface_passes():
    receipt = build_project_coupling_promotion_receipt(inputs())
    assert receipt_passes(receipt)
    assert receipt["zeta_m"] == pytest.approx(1.0)
    assert receipt["mbar_g"] == pytest.approx(1.5)
    assert receipt["kappa_e_natural"] == pytest.approx(4.0 / 9.0)


def test_total_rest_surface_has_quarter_kinetic_kappa():
    kinetic = build_project_coupling_promotion_receipt(inputs())
    rest = build_project_coupling_promotion_receipt(
        inputs(m_star=6.0, carrier_type="TOTAL_ONSHELL_REST")
    )
    assert receipt_passes(rest)
    assert rest["zeta_m"] == pytest.approx(2.0)
    assert rest["kappa_e_natural"] == pytest.approx(kinetic["kappa_e_natural"] / 4.0)


def test_wilson_mismatch_fails():
    receipt = build_project_coupling_promotion_receipt(inputs(g_ym_squared=1.2))
    assert receipt["defects"]["wilson_normalization"] > 0.0
    assert not receipt_passes(receipt)


def test_bcj_jacobi_mismatch_fails():
    receipt = build_project_coupling_promotion_receipt(inputs(bcj_jacobi_defect=1e-6))
    assert receipt["defects"]["bcj"] == pytest.approx(1e-6)
    assert not receipt_passes(receipt)


def test_wrong_five_point_graph_count_fails_structural_gate():
    receipt = build_project_coupling_promotion_receipt(inputs(bcj_graph_count=14))
    assert receipt["defects"]["bcj"] == pytest.approx(1.0)
    assert not receipt_passes(receipt)


def test_wrong_independent_jacobi_rank_fails_structural_gate():
    receipt = build_project_coupling_promotion_receipt(inputs(bcj_independent_jacobi_rank=8))
    assert receipt["defects"]["bcj"] == pytest.approx(1.0)
    assert not receipt_passes(receipt)


def test_klt_or_ward_mismatch_fails():
    klt = build_project_coupling_promotion_receipt(inputs(bcj_klt_defect=2e-5))
    ward = build_project_coupling_promotion_receipt(inputs(bcj_ward_defect=3e-5))
    assert not receipt_passes(klt)
    assert not receipt_passes(ward)


def test_gravity_target_used_to_select_gamma_fails_independence():
    receipt = build_project_coupling_promotion_receipt(
        inputs(gravity_target_used_for_gamma_selection=True)
    )
    assert receipt["defects"]["gravity_selection_independence"] == 1.0
    assert not receipt_passes(receipt)


def test_gravity_output_provenance_collision_fails():
    bad_provenance = provenance(gamma_source_id="RF_F25_REDUCED_GRAVITY_OUTPUT")
    receipt = build_project_coupling_promotion_receipt(inputs(provenance=bad_provenance))
    assert receipt["defects"]["provenance_collision"] == 1.0
    assert not receipt_passes(receipt)


def test_gremlin_candidate_is_not_promotion_authority():
    with pytest.raises(ProjectCouplingPromotionError):
        provenance(bcj_authority="GREMLIN_CANDIDATE")


def test_carrier_type_mismatch_fails():
    receipt = build_project_coupling_promotion_receipt(inputs(m_star=6.0))
    assert receipt["defects"]["carrier_type"] > 0.0
    assert not receipt_passes(receipt)


def test_independent_derived_carrier_type_allows_independently_frozen_scale():
    receipt = build_project_coupling_promotion_receipt(
        inputs(m_star=4.5, carrier_type="INDEPENDENT_DERIVED")
    )
    assert receipt["zeta_m"] == pytest.approx(1.5)
    assert receipt["defects"]["carrier_type"] == 0.0
    assert receipt_passes(receipt)


def test_gamma_changes_coupling_only_after_independent_input_is_frozen():
    a = build_project_coupling_promotion_receipt(inputs(gamma_dc=1.0))
    b = build_project_coupling_promotion_receipt(inputs(gamma_dc=2.0))
    assert b["kappa_e_natural"] == pytest.approx(4.0 * a["kappa_e_natural"])


def test_nonfinite_and_nonpositive_inputs_fail_closed():
    with pytest.raises(ProjectCouplingPromotionError):
        inputs(gamma_dc=0.0)
    with pytest.raises(ProjectCouplingPromotionError):
        inputs(beta_w=math.nan)


def test_tolerance_is_explicit():
    receipt = build_project_coupling_promotion_receipt(inputs(bcj_reconstruction_defect=1e-12))
    assert not receipt_passes(receipt)
    assert receipt_passes(receipt, atol=1e-11)
