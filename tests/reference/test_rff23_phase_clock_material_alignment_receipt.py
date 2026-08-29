import pytest

from src.rfc.phase_clock_material_alignment_receipt import (
    AlignmentLineage,
    PhaseClockMaterialAlignmentError,
    metric_inverse_defect,
    normalized_material_current,
    phase_clock_material_alignment_receipt,
    receipt_passes,
)


MINK = (
    (-1.0, 0.0, 0.0, 0.0),
    (0.0, 1.0, 0.0, 0.0),
    (0.0, 0.0, 1.0, 0.0),
    (0.0, 0.0, 0.0, 1.0),
)
COMMON = AlignmentLineage(
    u1_bundle="U1:ABE:v1",
    phase_patch="patch:alpha",
    connection="ABE:conn:01",
    slice_id="Sigma:01",
    coframe="RFN0:zero-shift",
    measure="measure:01",
    support="support:01",
)


def make_receipt(**overrides):
    values = dict(
        metric=MINK,
        inverse_metric=MINK,
        phase_covector=(-2.0, 0.0, 0.0, 0.0),
        phase_scale=2.0,
        material_current=(3.0, 0.0, 0.0, 0.0),
        slice_normal=(1.0, 0.0, 0.0, 0.0),
        phase_lineage=COMMON,
        current_lineage=COMMON,
    )
    values.update(overrides)
    return phase_clock_material_alignment_receipt(**values)


def test_exact_aligned_future_timelike_receipt_passes():
    receipt = make_receipt()
    assert receipt_passes(receipt)
    assert receipt["gamma_vartheta_j"] == pytest.approx(1.0)
    assert receipt["delta_vartheta_j"] == pytest.approx(0.0)


def test_phase_scale_is_independent_and_projector_mismatch_is_detected():
    receipt = make_receipt(phase_scale=1.0)
    assert receipt["phase_projector"] == pytest.approx(4.0)
    assert receipt["defects"]["phase_projector"] == pytest.approx(3.0)
    assert not receipt_passes(receipt)


def test_relative_boost_produces_positive_alignment_defect():
    receipt = make_receipt(material_current=(1.25, 0.75, 0.0, 0.0))
    assert receipt["gamma_vartheta_j"] == pytest.approx(1.25)
    assert receipt["delta_vartheta_j"] == pytest.approx(0.25)
    assert not receipt_passes(receipt)


def test_current_positive_rescaling_does_not_change_material_velocity_or_alignment():
    a = make_receipt(material_current=(3.0, 0.0, 0.0, 0.0))
    b = make_receipt(material_current=(30.0, 0.0, 0.0, 0.0))
    assert a["material_velocity"] == pytest.approx(b["material_velocity"])
    assert a["gamma_vartheta_j"] == pytest.approx(b["gamma_vartheta_j"])


def test_normalized_material_current_is_unit_timelike():
    nu = normalized_material_current(MINK, (2.5, 1.5, 0.0, 0.0))
    norm = -nu[0] ** 2 + nu[1] ** 2 + nu[2] ** 2 + nu[3] ** 2
    assert norm == pytest.approx(-1.0)


def test_past_directed_current_fails_orientation_and_alignment():
    receipt = make_receipt(material_current=(-3.0, 0.0, 0.0, 0.0))
    assert receipt["defects"]["current_future_orientation"] == pytest.approx(1.0)
    assert receipt["delta_vartheta_j"] == pytest.approx(2.0)
    assert not receipt_passes(receipt)


def test_past_directed_phase_clock_fails_orientation():
    receipt = make_receipt(phase_covector=(2.0, 0.0, 0.0, 0.0))
    assert receipt["defects"]["phase_future_orientation"] == pytest.approx(1.0)
    assert not receipt_passes(receipt)


def test_lineage_mismatch_blocks_numeric_alignment_pass():
    other = AlignmentLineage(
        u1_bundle=COMMON.u1_bundle,
        phase_patch=COMMON.phase_patch,
        connection="ABE:conn:02",
        slice_id=COMMON.slice_id,
        coframe=COMMON.coframe,
        measure=COMMON.measure,
        support=COMMON.support,
    )
    receipt = make_receipt(current_lineage=other)
    assert receipt["delta_vartheta_j"] == pytest.approx(0.0)
    assert receipt["defects"]["lineage_connection"] == pytest.approx(1.0)
    assert not receipt_passes(receipt)


def test_slice_normal_unit_defect_is_explicit():
    receipt = make_receipt(slice_normal=(2.0, 0.0, 0.0, 0.0))
    assert receipt["defects"]["slice_unit"] == pytest.approx(3.0)
    assert not receipt_passes(receipt)


def test_metric_inverse_defect_is_explicit():
    bad_inverse = [list(row) for row in MINK]
    bad_inverse[1][1] = 2.0
    assert metric_inverse_defect(MINK, bad_inverse) == pytest.approx(1.0)
    receipt = make_receipt(inverse_metric=bad_inverse)
    assert receipt["defects"]["metric_inverse"] == pytest.approx(1.0)
    assert not receipt_passes(receipt)


def test_spacelike_or_null_current_is_rejected_by_rfe19_domain_gate():
    with pytest.raises(PhaseClockMaterialAlignmentError):
        make_receipt(material_current=(1.0, 2.0, 0.0, 0.0))
    with pytest.raises(PhaseClockMaterialAlignmentError):
        make_receipt(material_current=(1.0, 1.0, 0.0, 0.0))


def test_explicit_numeric_tolerance_can_admit_tiny_alignment_residual():
    receipt = make_receipt(material_current=(1.0 + 1e-13, 0.0, 0.0, 0.0))
    assert receipt_passes(receipt, atol=1e-12)


def test_fail_closed_on_nonpositive_phase_scale():
    with pytest.raises(PhaseClockMaterialAlignmentError):
        make_receipt(phase_scale=0.0)
