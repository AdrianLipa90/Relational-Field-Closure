import pytest

from src.rfc.flow_adapted_zero_shift_atlas import (
    FlowAdaptedAtlasError,
    FlowAdaptedPatchSource,
    FlowAdaptedSpatialOverlap,
    assemble_flow_adapted_shared_spacetime_atlas,
)

I3 = ((1.0, 0.0, 0.0), (0.0, 1.0, 0.0), (0.0, 0.0, 1.0))
RZ90 = ((0.0, -1.0, 0.0), (1.0, 0.0, 0.0), (0.0, 0.0, 1.0))


def test_identity_overlap_passes_with_zero_shift_and_zero_drift():
    cert = assemble_flow_adapted_shared_spacetime_atlas(
        [FlowAdaptedPatchSource("p", 1.2, I3), FlowAdaptedPatchSource("q", 1.2, I3)],
        [FlowAdaptedSpatialOverlap("p", "q", I3, I3)],
        product_trivialization_certified=True,
    )
    assert cert.compatible is True
    assert cert.product_trivialization_parent is True
    assert cert.zero_shift_exact is True
    assert cert.zero_temporal_drift_exact is True
    assert cert.source_assembled.rf_e25.compatible is True


def test_rotated_spatial_overlap_passes_without_matching_shift_packet():
    cert = assemble_flow_adapted_shared_spacetime_atlas(
        [FlowAdaptedPatchSource("p", 0.8, I3), FlowAdaptedPatchSource("q", 0.8, I3)],
        [FlowAdaptedSpatialOverlap("p", "q", RZ90, RZ90)],
        product_trivialization_certified=True,
    )
    assert cert.source_assembled.max_shift_residual == pytest.approx(0.0)
    assert cert.source_assembled.max_spatial_coframe_residual == pytest.approx(0.0)


def test_missing_product_parent_fails_closed():
    with pytest.raises(FlowAdaptedAtlasError, match="product-trivialization parent"):
        assemble_flow_adapted_shared_spacetime_atlas(
            [FlowAdaptedPatchSource("p", 1.0, I3)],
            [],
            product_trivialization_certified=False,
        )


def test_lapse_mismatch_still_fails_through_gsc4a():
    with pytest.raises(FlowAdaptedAtlasError, match="shared lapse"):
        assemble_flow_adapted_shared_spacetime_atlas(
            [FlowAdaptedPatchSource("p", 1.0, I3), FlowAdaptedPatchSource("q", 1.1, I3)],
            [FlowAdaptedSpatialOverlap("p", "q", I3, I3)],
            product_trivialization_certified=True,
        )


def test_spatial_coframe_mismatch_still_fails_through_gsc4a():
    bad = ((2.0, 0.0, 0.0), (0.0, 1.0, 0.0), (0.0, 0.0, 1.0))
    with pytest.raises(FlowAdaptedAtlasError, match="spatial coframe"):
        assemble_flow_adapted_shared_spacetime_atlas(
            [FlowAdaptedPatchSource("p", 1.0, I3), FlowAdaptedPatchSource("q", 1.0, bad)],
            [FlowAdaptedSpatialOverlap("p", "q", I3, I3)],
            product_trivialization_certified=True,
        )


def test_orientation_reversal_remains_rejected():
    reflection = ((-1.0, 0.0, 0.0), (0.0, 1.0, 0.0), (0.0, 0.0, 1.0))
    with pytest.raises(FlowAdaptedAtlasError, match="preserve orientation"):
        assemble_flow_adapted_shared_spacetime_atlas(
            [FlowAdaptedPatchSource("p", 1.0, I3), FlowAdaptedPatchSource("q", 1.0, I3)],
            [FlowAdaptedSpatialOverlap("p", "q", reflection, I3)],
            product_trivialization_certified=True,
        )
