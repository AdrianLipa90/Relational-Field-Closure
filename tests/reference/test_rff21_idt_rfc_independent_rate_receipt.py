import pytest

from src.rfc.idt_rfc_independent_rate_receipt import (
    C_LIGHT,
    IndependentRateReceiptError,
    LineageIDs,
    build_independent_rate_receipt,
    phase_scale_from_independent_rotor_proper_rate,
    receipt_passes,
)


COMMON = LineageIDs(
    bundle="U1:ABE:v1",
    phase_patch="patch:alpha",
    connection="ABE:conn:01",
    clock="clock:reference:t",
    coframe="RFN0:zero-shift",
    measure="Sigma:measure:01",
    support="support:ordered:01",
)


def make_receipt(**overrides):
    values = dict(
        lapse_ratio=3.0,
        field_coordinate_rate=6.0,
        field_normal_proper_rate=2.0,
        rotor_coordinate_rate=6.0,
        rotor_proper_rate=2.0,
        field_inertia=5.0,
        rotor_inertia=5.0,
        rfc_omega=2.0,
        field_lineage=COMMON,
        rotor_lineage=COMMON,
    )
    values.update(overrides)
    return build_independent_rate_receipt(**values)


def test_zero_defect_reference_receipt_passes():
    receipt = make_receipt()
    assert receipt_passes(receipt)
    assert receipt["max_defect"] == pytest.approx(0.0)


def test_inputs_remain_independent_coordinates():
    receipt = make_receipt(field_coordinate_rate=6.1)
    assert receipt["defects"]["coordinate_rate"] > 0.0
    assert receipt["defects"]["field_lapse_rate"] > 0.0
    assert not receipt_passes(receipt)


def test_field_lapse_identity_is_a_separate_defect():
    receipt = make_receipt(field_normal_proper_rate=1.9)
    assert receipt["defects"]["field_lapse_rate"] > 0.0
    assert receipt["defects"]["proper_rate"] > 0.0


def test_rotor_lapse_identity_is_a_separate_defect():
    receipt = make_receipt(rotor_proper_rate=2.1)
    assert receipt["defects"]["rotor_lapse_rate"] > 0.0
    assert receipt["defects"]["proper_rate"] > 0.0


def test_inertia_mismatch_is_detected_independently():
    receipt = make_receipt(rotor_inertia=4.5)
    assert receipt["defects"]["inertia"] > 0.0
    assert receipt["defects"]["generator"] > 0.0


def test_generator_equality_follows_on_zero_defect_surface():
    receipt = make_receipt()
    assert receipt["field_generator"] == pytest.approx(10.0)
    assert receipt["rotor_generator"] == pytest.approx(10.0)
    assert receipt["defects"]["generator"] == pytest.approx(0.0)


def test_rfc_omega_is_independently_audited_against_field_proper_rate():
    receipt = make_receipt(rfc_omega=2.2)
    assert receipt["defects"]["rfc_omega"] > 0.0


def test_phase_scale_comes_from_independent_rotor_proper_rate():
    receipt = make_receipt()
    assert receipt["mu_vartheta"] == pytest.approx(2.0 / C_LIGHT)
    assert phase_scale_from_independent_rotor_proper_rate(2.0) == pytest.approx(2.0 / C_LIGHT)


def test_bundle_lineage_mismatch_is_detected():
    other = LineageIDs(
        bundle="U1:other",
        phase_patch=COMMON.phase_patch,
        connection=COMMON.connection,
        clock=COMMON.clock,
        coframe=COMMON.coframe,
        measure=COMMON.measure,
        support=COMMON.support,
    )
    receipt = make_receipt(rotor_lineage=other)
    assert receipt["defects"]["lineage_bundle"] == pytest.approx(1.0)
    assert not receipt_passes(receipt)


def test_connection_lineage_mismatch_is_detected():
    other = LineageIDs(
        bundle=COMMON.bundle,
        phase_patch=COMMON.phase_patch,
        connection="ABE:conn:02",
        clock=COMMON.clock,
        coframe=COMMON.coframe,
        measure=COMMON.measure,
        support=COMMON.support,
    )
    receipt = make_receipt(rotor_lineage=other)
    assert receipt["defects"]["lineage_connection"] == pytest.approx(1.0)


def test_tolerance_can_admit_small_numeric_residual_only_when_explicit():
    receipt = make_receipt(field_coordinate_rate=6.0 + 1e-12)
    assert not receipt_passes(receipt)
    assert receipt_passes(receipt, atol=1e-11)


def test_fail_closed_on_invalid_rate_or_lapse():
    with pytest.raises(IndependentRateReceiptError):
        make_receipt(lapse_ratio=0.0)
    with pytest.raises(IndependentRateReceiptError):
        make_receipt(rotor_proper_rate=0.0)


def test_fail_closed_on_empty_lineage_id():
    with pytest.raises(IndependentRateReceiptError):
        LineageIDs(
            bundle="",
            phase_patch="patch",
            connection="conn",
            clock="clock",
            coframe="coframe",
            measure="measure",
            support="support",
        )
