import math

import pytest

from src.rfc.anchored_phase_scaled_rigid_geometry import (
    AnchoredRigidGeometryError,
    anchored_phase_patch,
    certify_anchored_phase_scaled_rigid_geometry,
)

I3 = ((1.0, 0.0, 0.0), (0.0, 1.0, 0.0), (0.0, 0.0, 1.0))
RZ90 = ((0.0, -1.0, 0.0), (1.0, 0.0, 0.0), (0.0, 0.0, 1.0))


def test_identity_anchored_overlap_gives_a_equals_r_and_scaled_identity_coframe():
    p = anchored_phase_patch("p", (0, 0, 0), I3, 2.0)
    q = anchored_phase_patch("q", (1, 0, 0), I3, 2.0)
    cert = certify_anchored_phase_scaled_rigid_geometry([p, q], [("p", "q")])
    ov = cert.overlaps[0]
    assert ov.spatial_jacobian == pytest.approx(I3)
    assert ov.spatial_rotation == pytest.approx(I3)
    assert ov.translation == pytest.approx((-1.0, 0.0, 0.0))
    assert cert.max_coframe_residual == pytest.approx(0.0)
    assert p.coframe[0][0] == pytest.approx(299792458.0 / (math.sqrt(6.0) * 2.0))


def test_rotated_anchored_frames_give_same_rigid_jacobian_and_rotation():
    p = anchored_phase_patch("p", (0, 0, 0), I3, -5.0)
    q = anchored_phase_patch("q", (0, 0, 0), RZ90, 5.0)
    cert = certify_anchored_phase_scaled_rigid_geometry([p, q], [("p", "q")])
    ov = cert.overlaps[0]
    expected = ((0.0, 1.0, 0.0), (-1.0, 0.0, 0.0), (0.0, 0.0, 1.0))
    assert ov.spatial_jacobian == pytest.approx(expected)
    assert ov.spatial_rotation == pytest.approx(expected)
    assert cert.max_coframe_residual == pytest.approx(0.0)


def test_phase_rate_sign_does_not_change_spatial_scale():
    p = anchored_phase_patch("p", (0, 0, 0), I3, 7.0)
    q = anchored_phase_patch("q", (1, 2, 3), I3, -7.0)
    cert = certify_anchored_phase_scaled_rigid_geometry([p, q], [("p", "q")])
    assert cert.max_scale_residual == pytest.approx(0.0)


def test_phase_scale_mismatch_fails_closed():
    p = anchored_phase_patch("p", (0, 0, 0), I3, 2.0)
    q = anchored_phase_patch("q", (0, 0, 0), I3, 3.0)
    with pytest.raises(AnchoredRigidGeometryError, match="phase-clock spatial scale mismatch"):
        certify_anchored_phase_scaled_rigid_geometry([p, q], [("p", "q")])


def test_non_so3_frame_fails_closed():
    shear = ((1.0, 0.2, 0.0), (0.0, 1.0, 0.0), (0.0, 0.0, 1.0))
    with pytest.raises(AnchoredRigidGeometryError, match="SO\(3\)"):
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
    assert cert.production_status == "ANCHOR_FRAME_PHASE_RATE_SOURCE_PACKET_OPEN"
