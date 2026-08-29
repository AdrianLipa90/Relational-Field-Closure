import pytest

from src.rfc.current_measure_realization_receipt import (
    CurrentMeasureLineage,
    CurrentMeasureReceiptError,
    build_current_measure_receipt,
    occupation_predicted_current,
    receipt_passes,
)


COMMON = CurrentMeasureLineage(
    slice_id="Sigma:01",
    normal_orientation_id="future:n:01",
    semantic_measure_id="dV_h:01",
    cell_ids=("C0", "C1", "C2"),
)


def make_receipt(**overrides):
    values = dict(
        noether_current=(1.0, 2.0, 3.0),
        noether_volumes=(1.0, 1.0, 1.0),
        rfc_current=(1.0, 2.0, 3.0),
        rfc_volumes=(1.0, 1.0, 1.0),
        noether_lineage=COMMON,
        rfc_lineage=COMMON,
        side_flux=0.0,
    )
    values.update(overrides)
    return build_current_measure_receipt(**values)


def test_zero_defect_current_measure_receipt_passes():
    receipt = make_receipt()
    assert receipt_passes(receipt)
    assert receipt["noether_charge"] == pytest.approx(6.0)
    assert receipt["rfc_charge"] == pytest.approx(6.0)
    assert receipt["max_defect"] == pytest.approx(0.0)


def test_exact_defect_bound_is_respected():
    receipt = make_receipt(rfc_current=(1.1, 1.8, 3.2), rfc_volumes=(1.0, 1.2, 0.9))
    d = receipt["defects"]
    assert d["extensive_charge"] <= d["local_current"] + d["measure"] + 1e-15
    assert d["defect_bound_margin"] == pytest.approx(0.0)


def test_integrated_charge_equality_does_not_promote_local_current_identity():
    lineage = CurrentMeasureLineage(
        slice_id="Sigma:01",
        normal_orientation_id="future:n:01",
        semantic_measure_id="dV_h:01",
        cell_ids=("C0", "C1"),
    )
    receipt = build_current_measure_receipt(
        noether_current=(1.0, 3.0),
        noether_volumes=(1.0, 1.0),
        rfc_current=(2.0, 2.0),
        rfc_volumes=(1.0, 1.0),
        noether_lineage=lineage,
        rfc_lineage=lineage,
        side_flux=0.0,
    )
    assert receipt["defects"]["extensive_charge"] == pytest.approx(0.0)
    assert receipt["defects"]["local_current"] == pytest.approx(0.5)
    assert not receipt_passes(receipt)


def test_measure_mismatch_is_independent_from_current_mismatch():
    receipt = make_receipt(rfc_volumes=(1.0, 2.0, 1.0))
    assert receipt["defects"]["local_current"] == pytest.approx(0.0)
    assert receipt["defects"]["measure"] > 0.0
    assert not receipt_passes(receipt)


def test_side_flux_is_an_independent_conservation_defect():
    receipt = make_receipt(side_flux=0.01)
    assert receipt["defects"]["side_flux"] == pytest.approx(0.01)
    assert not receipt_passes(receipt)


def test_ordered_cell_lineage_mismatch_blocks_numeric_pass():
    other = CurrentMeasureLineage(
        slice_id=COMMON.slice_id,
        normal_orientation_id=COMMON.normal_orientation_id,
        semantic_measure_id=COMMON.semantic_measure_id,
        cell_ids=("C1", "C0", "C2"),
    )
    receipt = make_receipt(rfc_lineage=other)
    assert receipt["defects"]["lineage_ordered_cells"] == pytest.approx(1.0)
    assert not receipt_passes(receipt)


def test_semantic_measure_lineage_mismatch_blocks_numeric_pass():
    other = CurrentMeasureLineage(
        slice_id=COMMON.slice_id,
        normal_orientation_id=COMMON.normal_orientation_id,
        semantic_measure_id="other-measure",
        cell_ids=COMMON.cell_ids,
    )
    receipt = make_receipt(rfc_lineage=other)
    assert receipt["defects"]["lineage_semantic_measure"] == pytest.approx(1.0)
    assert not receipt_passes(receipt)


def test_profiles_are_exactly_identical_on_zero_defect_surface():
    receipt = make_receipt()
    assert receipt["noether_profile"] == pytest.approx(receipt["rfc_profile"])
    assert sum(receipt["rfc_profile"]) == pytest.approx(1.0)


def test_rf_s16_occupation_current_map_roundtrips():
    predicted = occupation_predicted_current(
        occupations=(2.0, 6.0, 12.0),
        volumes=(1.0, 2.0, 3.0),
        carrier_quantum=0.5,
    )
    assert predicted == pytest.approx((1.0, 1.5, 2.0))


def test_optional_occupation_audit_is_independent_and_passes_when_consistent():
    receipt = build_current_measure_receipt(
        noether_current=(1.0, 1.5, 2.0),
        noether_volumes=(1.0, 2.0, 3.0),
        rfc_current=(1.0, 1.5, 2.0),
        rfc_volumes=(1.0, 2.0, 3.0),
        noether_lineage=COMMON,
        rfc_lineage=COMMON,
        side_flux=0.0,
        occupations=(2.0, 6.0, 12.0),
        carrier_quantum=0.5,
    )
    assert receipt["defects"]["occupation_current"] == pytest.approx(0.0)
    assert receipt["defects"]["occupation_extensive_charge"] == pytest.approx(0.0)
    assert receipt["defects"]["occupation_profile_l1"] == pytest.approx(0.0)
    assert receipt_passes(receipt)


def test_optional_occupation_audit_detects_same_total_different_local_profile():
    receipt = build_current_measure_receipt(
        noether_current=(2.0, 2.0, 2.0),
        noether_volumes=(1.0, 1.0, 1.0),
        rfc_current=(2.0, 2.0, 2.0),
        rfc_volumes=(1.0, 1.0, 1.0),
        noether_lineage=COMMON,
        rfc_lineage=COMMON,
        side_flux=0.0,
        occupations=(1.0, 2.0, 3.0),
        carrier_quantum=1.0,
    )
    assert receipt["defects"]["occupation_extensive_charge"] == pytest.approx(0.0)
    assert receipt["defects"]["occupation_current"] > 0.0
    assert not receipt_passes(receipt)


def test_explicit_tolerance_can_admit_only_small_numeric_residuals():
    receipt = make_receipt(rfc_current=(1.0 + 1e-13, 2.0, 3.0))
    assert not receipt_passes(receipt)
    assert receipt_passes(receipt, atol=1e-12)


def test_fail_closed_on_nonpositive_volume_or_negative_current():
    with pytest.raises(CurrentMeasureReceiptError):
        make_receipt(rfc_volumes=(1.0, 0.0, 1.0))
    with pytest.raises(CurrentMeasureReceiptError):
        make_receipt(rfc_current=(1.0, -1.0, 3.0))


def test_fail_closed_on_zero_total_charge():
    with pytest.raises(CurrentMeasureReceiptError):
        make_receipt(
            noether_current=(0.0, 0.0, 0.0),
            rfc_current=(0.0, 0.0, 0.0),
        )


def test_fail_closed_when_optional_occupation_inputs_are_incomplete():
    with pytest.raises(CurrentMeasureReceiptError):
        make_receipt(occupations=(1.0, 2.0, 3.0))
