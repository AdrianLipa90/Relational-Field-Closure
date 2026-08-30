import math

import pytest

from rfc.shared_spacetime_atlas import (
    ADMPatch,
    AtlasOverlap,
    SharedSpacetimeAtlasError,
    certify_shared_spacetime_atlas,
)


I3 = (
    (1.0, 0.0, 0.0),
    (0.0, 1.0, 0.0),
    (0.0, 0.0, 1.0),
)
I4 = (
    (1.0, 0.0, 0.0, 0.0),
    (0.0, 1.0, 0.0, 0.0),
    (0.0, 0.0, 1.0, 0.0),
    (0.0, 0.0, 0.0, 1.0),
)
R90 = (
    (1.0, 0.0, 0.0, 0.0),
    (0.0, 0.0, -1.0, 0.0),
    (0.0, 1.0, 0.0, 0.0),
    (0.0, 0.0, 0.0, 1.0),
)
R180 = (
    (1.0, 0.0, 0.0, 0.0),
    (0.0, -1.0, 0.0, 0.0),
    (0.0, 0.0, -1.0, 0.0),
    (0.0, 0.0, 0.0, 1.0),
)


def patch(name, *, lapse=1.0, triad=I3, shift=(0.0, 0.0, 0.0)):
    return ADMPatch(name, lapse, triad, shift)


def overlap(source, target, jacobian=I4, lorentz=I4):
    return AtlasOverlap(source, target, jacobian, lorentz)


def test_single_patch_adm_coframe_is_rank_four_and_lorentzian():
    p = patch("p", lapse=1.7, shift=(0.2, -0.1, 0.05))
    cert = certify_shared_spacetime_atlas([p], [])
    assert cert.compatible
    assert cert.patch_count == 1
    assert p.metric[0][0] < 0.0
    assert cert.production_input_status == "OPEN_INPUT"


def test_identity_overlap_passes():
    cert = certify_shared_spacetime_atlas(
        [patch("p"), patch("q")],
        [overlap("p", "q")],
    )
    assert cert.compatible
    assert cert.max_coframe_residual == pytest.approx(0.0)
    assert cert.max_metric_residual == pytest.approx(0.0)


def test_spatial_rotation_is_valid_joint_coordinate_and_frame_transition():
    cert = certify_shared_spacetime_atlas(
        [patch("p"), patch("q")],
        [overlap("p", "q", R90, R90)],
    )
    assert cert.compatible
    assert cert.max_lorentz_residual == pytest.approx(0.0)


def test_nonzero_shift_identity_overlap_passes_when_patch_data_agree():
    cert = certify_shared_spacetime_atlas(
        [
            patch("p", lapse=1.2, shift=(0.1, 0.2, -0.1)),
            patch("q", lapse=1.2, shift=(0.1, 0.2, -0.1)),
        ],
        [overlap("p", "q")],
    )
    assert cert.compatible


def test_wrong_coframe_gluing_fails_closed():
    with pytest.raises(SharedSpacetimeAtlasError, match="matrix compatibility residual"):
        certify_shared_spacetime_atlas(
            [patch("p"), patch("q", lapse=1.1)],
            [overlap("p", "q")],
        )


@pytest.mark.parametrize("lapse", [0.0, -1.0, math.inf, math.nan])
def test_invalid_lapse_fails_closed(lapse):
    with pytest.raises(SharedSpacetimeAtlasError):
        patch("p", lapse=lapse)


def test_singular_triad_fails_closed():
    singular = (
        (1.0, 0.0, 0.0),
        (0.0, 1.0, 0.0),
        (0.0, 0.0, 0.0),
    )
    with pytest.raises(SharedSpacetimeAtlasError, match="triad must be invertible"):
        patch("p", triad=singular)


def test_non_lorentz_frame_transition_fails_closed():
    bad = (
        (2.0, 0.0, 0.0, 0.0),
        (0.0, 1.0, 0.0, 0.0),
        (0.0, 0.0, 1.0, 0.0),
        (0.0, 0.0, 0.0, 1.0),
    )
    with pytest.raises(SharedSpacetimeAtlasError, match="matrix compatibility residual"):
        certify_shared_spacetime_atlas(
            [patch("p"), patch("q")],
            [overlap("p", "q", I4, bad)],
        )


def test_improper_spatial_reflection_fails_orientation_gate():
    reflection = (
        (1.0, 0.0, 0.0, 0.0),
        (0.0, -1.0, 0.0, 0.0),
        (0.0, 0.0, 1.0, 0.0),
        (0.0, 0.0, 0.0, 1.0),
    )
    with pytest.raises(SharedSpacetimeAtlasError, match="Jacobian must preserve atlas orientation"):
        certify_shared_spacetime_atlas(
            [patch("p"), patch("q")],
            [overlap("p", "q", reflection, reflection)],
        )


def test_time_reversal_fails_shared_clock_gate():
    reverse_time = (
        (-1.0, 0.0, 0.0, 0.0),
        (0.0, -1.0, 0.0, 0.0),
        (0.0, 0.0, 1.0, 0.0),
        (0.0, 0.0, 0.0, 1.0),
    )
    with pytest.raises(SharedSpacetimeAtlasError, match="shared scalar clock"):
        certify_shared_spacetime_atlas(
            [patch("p"), patch("q")],
            [overlap("p", "q", reverse_time, reverse_time)],
        )


def test_time_coordinate_mixing_fails_shared_scalar_clock_gate():
    mixed = (
        (1.0, 0.1, 0.0, 0.0),
        (0.0, 1.0, 0.0, 0.0),
        (0.0, 0.0, 1.0, 0.0),
        (0.0, 0.0, 0.0, 1.0),
    )
    with pytest.raises(SharedSpacetimeAtlasError, match="shared scalar clock"):
        certify_shared_spacetime_atlas(
            [patch("p"), patch("q")],
            [overlap("p", "q", mixed, I4)],
        )


def test_triple_overlap_cocycle_passes():
    cert = certify_shared_spacetime_atlas(
        [patch("p"), patch("q"), patch("r")],
        [
            overlap("p", "q", R90, R90),
            overlap("q", "r", R90, R90),
            overlap("p", "r", R180, R180),
        ],
        triangles=[("p", "q", "r")],
    )
    assert cert.triangle_count == 1
    assert cert.max_jacobian_cocycle_residual == pytest.approx(0.0)
    assert cert.max_lorentz_cocycle_residual == pytest.approx(0.0)


def test_triple_overlap_cocycle_mismatch_fails_closed():
    with pytest.raises(SharedSpacetimeAtlasError, match="matrix compatibility residual"):
        certify_shared_spacetime_atlas(
            [patch("p"), patch("q"), patch("r")],
            [
                overlap("p", "q", R90, R90),
                overlap("q", "r", R90, R90),
                overlap("p", "r", I4, I4),
            ],
            triangles=[("p", "q", "r")],
        )


def test_disconnected_atlas_fails_closed():
    with pytest.raises(SharedSpacetimeAtlasError, match="overlap graph must be connected"):
        certify_shared_spacetime_atlas([patch("p"), patch("q")], [])


def test_metric_pullback_is_consequence_of_coframe_and_lorentz_gluing():
    cert = certify_shared_spacetime_atlas(
        [patch("p"), patch("q")],
        [overlap("p", "q", R90, R90)],
    )
    assert cert.max_metric_residual == pytest.approx(0.0)
