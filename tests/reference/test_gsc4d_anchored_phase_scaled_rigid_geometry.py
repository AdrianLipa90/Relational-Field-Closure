import math

import pytest

from src.rfc.anchored_phase_scaled_rigid_geometry import (
    AnchoredRigidGeometryError,
    anchored_phase_patch,
    certify_anchored_phase_scaled_rigid_geometry,
    overlap_phase_rate_sample,
)

I3 = ((1.0, 0.0, 0.0), (0.0, 1.0, 0.0), (0.0, 0.0, 1.0))
RZ90 = ((0.0, -1.0, 0.0), (1.0, 0.0, 0.0), (0.0, 0.0, 1.0))


def assert_matrix_close(actual, expected):
    assert len(actual) == len(expected)
    for actual_row, expected_row in zip(actual, expected):
        assert actual_row == pytest.approx(expected_row)


def test_identity_anchored_overlap_gives_a_equals_r_and_scaled_identity_coframe():
    p = anchored_phase_patch("p", (0, 0, 0), I3, 2.0)
    q = anchored_phase_patch("q", (1, 0, 0), I3, 2.0)
    cert = certify_anchored_phase_scaled_rigid_geometry([p, q], [("p", "q")])
    ov = cert.overlaps[0]
    assert_matrix_close(ov.spatial_jacobian, I3)
    assert_matrix_close(ov.spatial_rotation, I3)
    assert ov.translation == pytest.approx((-1.0, 0.0, 0.0))
    assert cert.max_coframe_residual == pytest.approx(0.0)
    assert cert.phase_field_sampling_mode == "PATCH_CONSTANT_REFERENCE_FIXTURE"
    assert p.coframe[0][0] == pytest.approx(299792458.0 / (math.sqrt(6.0) * 2.0))


def test_rotated_anchored_frames_give_same_rigid_jacobian_and_rotation():
    p = anchored_phase_patch("p", (0, 0, 0), I3, -5.0)
    q = anchored_phase_patch("q", (0, 0, 0), RZ90, 5.0)
    cert = certify_anchored_phase_scaled_rigid_geometry([p, q], [("p", "q")])
    ov = cert.overlaps[0]
    expected = ((0.0, 1.0, 0.0), (-1.0, 0.0, 0.0), (0.0, 0.0, 1.0))
    assert_matrix_close(ov.spatial_jacobian, expected)
    assert_matrix_close(ov.spatial_rotation, expected)
    assert cert.max_coframe_residual == pytest.approx(0.0)


def test_phase_rate_sign_does_not_change_spatial_scale():
    p = anchored_phase_patch("p", (0, 0, 0), I3, 7.0)
    q = anchored_phase_patch("q", (1, 2, 3), I3, -7.0)
    cert = certify_anchored_phase_scaled_rigid_geometry([p, q], [("p", "q")])
    assert cert.max_scale_residual == pytest.approx(0.0)


def test_patch_reference_phase_scale_mismatch_fails_closed():
    p = anchored_phase_patch("p", (0, 0, 0), I3, 2.0)
    q = anchored_phase_patch("q", (0, 0, 0), I3, 3.0)
    with pytest.raises(AnchoredRigidGeometryError, match=r"phase-clock spatial scale mismatch"):
        certify_anchored_phase_scaled_rigid_geometry([p, q], [("p", "q")])


def test_overlap_local_samples_allow_spatially_varying_phase_scale_across_connected_cover():
    p = anchored_phase_patch("p", (0, 0, 0), I3, 99.0)
    q = anchored_phase_patch("q", (1, 0, 0), I3, 98.0)
    r = anchored_phase_patch("r", (2, 0, 0), I3, 97.0)
    samples = [
        overlap_phase_rate_sample("p", "q", "x-pq", 2.0, -2.0),
        overlap_phase_rate_sample("q", "r", "y-qr", 3.0, -3.0),
    ]
    cert = certify_anchored_phase_scaled_rigid_geometry(
        [p, q, r],
        [("p", "q"), ("q", "r")],
        overlap_phase_samples=samples,
    )
    assert cert.phase_field_sampling_mode == "OVERLAP_LOCAL_PHASE_FIELD"
    assert cert.spatially_varying_phase_scale_supported is True
    assert cert.max_scale_residual == pytest.approx(0.0)
    assert cert.max_coframe_residual == pytest.approx(0.0)
    assert cert.overlaps[0].source_phase_scale != pytest.approx(cert.overlaps[1].source_phase_scale)


def test_multiple_samples_on_one_overlap_allow_field_variation_but_require_pointwise_gluing():
    p = anchored_phase_patch("p", (0, 0, 0), I3, 1.0)
    q = anchored_phase_patch("q", (1, 0, 0), I3, 1.0)
    samples = [
        overlap_phase_rate_sample("p", "q", "x0", 2.0, -2.0),
        overlap_phase_rate_sample("p", "q", "x1", 4.0, 4.0),
    ]
    cert = certify_anchored_phase_scaled_rigid_geometry(
        [p, q], [("p", "q")], overlap_phase_samples=samples
    )
    assert len(cert.overlaps) == 2
    assert cert.overlaps[0].source_phase_scale != pytest.approx(cert.overlaps[1].source_phase_scale)
    assert all(overlap.scale_residual == pytest.approx(0.0) for overlap in cert.overlaps)


def test_overlap_local_magnitude_mismatch_fails_closed():
    p = anchored_phase_patch("p", (0, 0, 0), I3, 1.0)
    q = anchored_phase_patch("q", (1, 0, 0), I3, 1.0)
    bad = [overlap_phase_rate_sample("p", "q", "bad", 2.0, 3.0)]
    with pytest.raises(AnchoredRigidGeometryError, match=r"phase-clock spatial scale mismatch"):
        certify_anchored_phase_scaled_rigid_geometry(
            [p, q], [("p", "q")], overlap_phase_samples=bad
        )


def test_explicit_phase_field_mode_requires_a_sample_for_every_declared_overlap():
    p = anchored_phase_patch("p", (0, 0, 0), I3, 1.0)
    q = anchored_phase_patch("q", (1, 0, 0), I3, 1.0)
    r = anchored_phase_patch("r", (2, 0, 0), I3, 1.0)
    samples = [overlap_phase_rate_sample("p", "q", "pq", 2.0, 2.0)]
    with pytest.raises(AnchoredRigidGeometryError, match=r"every declared overlap"):
        certify_anchored_phase_scaled_rigid_geometry(
            [p, q, r],
            [("p", "q"), ("q", "r")],
            overlap_phase_samples=samples,
        )


def test_non_so3_frame_fails_closed():
    shear = ((1.0, 0.2, 0.0), (0.0, 1.0, 0.0), (0.0, 0.0, 1.0))
    with pytest.raises(AnchoredRigidGeometryError, match=r"SO\(3\)"):
        anchored_phase_patch("p", (0, 0, 0), shear, 2.0)


def test_zero_or_nonfinite_phase_rate_fails_closed():
    for bad in (0.0, float("nan"), float("inf")):
        with pytest.raises(AnchoredRigidGeometryError):
            anchored_phase_patch("p", (0, 0, 0), I3, bad)


def test_rigid_route_keeps_general_spatial_atlas_separate():
    p = anchored_phase_patch("p", (0, 0, 0), I3, 1.0)
    cert = certify_anchored_phase_scaled_rigid_geometry([p], [])
    assert cert.rigid_route_exact is True
    assert cert.general_spatial_atlas_status == "GENERAL_GSC4A_ROUTE_SEPARATE"
    assert cert.production_status == "ANCHOR_FRAME_OVERLAP_LOCAL_PHASE_FIELD_SOURCE_PACKET_OPEN"
