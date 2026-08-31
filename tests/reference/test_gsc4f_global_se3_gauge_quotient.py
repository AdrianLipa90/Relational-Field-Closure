import numpy as np
import pytest

from src.rfc.global_se3_gauge_quotient import (
    apply_global_se3,
    canonical_reference_gauge,
    certify_global_se3_quotient,
    chart,
    overlap,
)


def rz(theta):
    c, s = np.cos(theta), np.sin(theta)
    return np.array([[c, -s, 0.0], [s, c, 0.0], [0.0, 0.0, 1.0]])


def test_reference_patch_is_canonicalized_to_origin_and_identity():
    charts = (
        chart([1.0, 2.0, 3.0], rz(0.3)),
        chart([2.0, -1.0, 0.5], rz(-0.4)),
    )
    normalized = canonical_reference_gauge(charts, reference=0)
    assert normalized[0].anchor == pytest.approx(np.zeros(3))
    assert normalized[0].frame == pytest.approx(np.eye(3))


def test_pairwise_rotation_and_translation_are_global_se3_invariant():
    charts = (
        chart([1.0, 0.0, 0.0], rz(0.2)),
        chart([0.0, 2.0, 0.5], rz(-0.5)),
    )
    transformed = apply_global_se3(charts, rz(0.9), [4.0, -2.0, 3.0])
    before = overlap(charts[0], charts[1])
    after = overlap(transformed[0], transformed[1])
    assert after.rotation == pytest.approx(before.rotation)
    assert after.translation == pytest.approx(before.translation)


def test_certifier_removes_six_global_gauge_coordinates():
    charts = (
        chart([1.0, 2.0, 3.0], rz(0.3)),
        chart([2.0, -1.0, 0.5], rz(-0.4)),
        chart([-2.0, 0.25, 1.5], rz(1.1)),
    )
    receipt = certify_global_se3_quotient(charts, reference=1)
    assert receipt["status"] == "PASS"
    assert receipt["global_gauge_dof_removed"] == 6
    assert receipt["relative_rigid_configuration_retained"] is True
    assert receipt["production_geometry_promoted"] is False


def test_uniform_translation_is_gauge():
    charts = (
        chart([1.0, 0.0, 0.0], np.eye(3)),
        chart([2.0, 1.0, 0.0], np.eye(3)),
    )
    shifted = apply_global_se3(charts, np.eye(3), [9.0, -7.0, 4.0])
    assert overlap(shifted[0], shifted[1]).translation == pytest.approx(
        overlap(charts[0], charts[1]).translation
    )


def test_uniform_rotation_is_gauge():
    charts = (
        chart([1.0, 0.0, 0.0], rz(0.1)),
        chart([0.0, 1.0, 0.0], rz(0.7)),
    )
    rotated = apply_global_se3(charts, rz(-1.2), [0.0, 0.0, 0.0])
    assert overlap(rotated[0], rotated[1]).rotation == pytest.approx(
        overlap(charts[0], charts[1]).rotation
    )


def test_relative_scale_remains_source_geometry():
    charts = (
        chart([0.0, 0.0, 0.0], np.eye(3)),
        chart([1.0, 0.0, 0.0], np.eye(3)),
    )
    scaled = (
        chart([0.0, 0.0, 0.0], np.eye(3)),
        chart([2.0, 0.0, 0.0], np.eye(3)),
    )
    assert overlap(scaled[0], scaled[1]).translation != pytest.approx(
        overlap(charts[0], charts[1]).translation
    )


def test_independent_patch_rotation_changes_relative_overlap():
    charts = (
        chart([0.0, 0.0, 0.0], np.eye(3)),
        chart([1.0, 0.0, 0.0], np.eye(3)),
    )
    locally_changed = (
        charts[0],
        chart([1.0, 0.0, 0.0], rz(0.4)),
    )
    assert overlap(locally_changed[0], locally_changed[1]).rotation != pytest.approx(
        overlap(charts[0], charts[1]).rotation
    )


def test_invalid_frame_fails_closed():
    with pytest.raises(ValueError):
        chart([0.0, 0.0, 0.0], np.diag([1.0, 1.0, 2.0]))


def test_reflection_fails_closed():
    with pytest.raises(ValueError):
        chart([0.0, 0.0, 0.0], np.diag([1.0, 1.0, -1.0]))
