import pytest

from src.rfc.shared_spacetime_atlas import ADMPatch
from src.rfc.source_assembled_shared_spacetime_atlas import (
    SourceAssembledAtlasError,
    SpatialSourceOverlap,
    assemble_source_shared_spacetime_atlas,
)


I3 = (
    (1.0, 0.0, 0.0),
    (0.0, 1.0, 0.0),
    (0.0, 0.0, 1.0),
)

RZ90 = (
    (0.0, -1.0, 0.0),
    (1.0, 0.0, 0.0),
    (0.0, 0.0, 1.0),
)


def test_identity_spatial_overlap_with_nonzero_temporal_drift_assembles_rfe25():
    p = ADMPatch("p", 2.0, I3, (0.2, -0.1, 0.3))
    q = ADMPatch("q", 2.0, I3, (0.15, -0.12, 0.34))
    overlap = SpatialSourceOverlap("p", "q", I3, (0.05, 0.02, -0.04), I3)

    cert = assemble_source_shared_spacetime_atlas([p, q], [overlap])
    assert cert.compatible is True
    assert cert.rf_e25.compatible is True
    assert cert.rf_e25.max_coframe_residual == pytest.approx(0.0)
    assert cert.rf_e25.max_metric_residual == pytest.approx(0.0)


def test_nontrivial_spatial_rotation_builds_proper_lorentz_transition():
    p = ADMPatch("p", 1.5, I3, (1.0, 0.0, 0.0))
    q = ADMPatch("q", 1.5, I3, (-0.2, 0.7, 0.0))
    overlap = SpatialSourceOverlap("p", "q", RZ90, (0.2, 0.3, 0.0), RZ90)

    cert = assemble_source_shared_spacetime_atlas([p, q], [overlap])
    assert cert.max_rotation_residual == pytest.approx(0.0)
    assert cert.rf_e25.max_lorentz_residual == pytest.approx(0.0)


def test_source_cocycles_inherit_full_rfe25_triple_cocycle():
    p = ADMPatch("p", 1.0, I3, (1.0, 2.0, 3.0))
    v_pq = (0.1, -0.2, 0.3)
    v_qr = (-0.4, 0.5, 0.2)
    v_pr = tuple(v_pq[i] + v_qr[i] for i in range(3))
    q_shift = tuple(p.shift[i] - v_pq[i] for i in range(3))
    r_shift = tuple(p.shift[i] - v_pr[i] for i in range(3))
    q = ADMPatch("q", 1.0, I3, q_shift)
    r = ADMPatch("r", 1.0, I3, r_shift)

    overlaps = [
        SpatialSourceOverlap("p", "q", I3, v_pq, I3),
        SpatialSourceOverlap("q", "r", I3, v_qr, I3),
        SpatialSourceOverlap("p", "r", I3, v_pr, I3),
    ]
    cert = assemble_source_shared_spacetime_atlas(
        [p, q, r], overlaps, triangles=[("p", "q", "r")]
    )
    assert cert.rf_e25.triangle_count == 1
    assert cert.rf_e25.max_jacobian_cocycle_residual == pytest.approx(0.0)
    assert cert.rf_e25.max_lorentz_cocycle_residual == pytest.approx(0.0)


def test_shared_lapse_scalar_is_source_gate():
    p = ADMPatch("p", 1.0, I3, (0.0, 0.0, 0.0))
    q = ADMPatch("q", 1.1, I3, (0.0, 0.0, 0.0))
    overlap = SpatialSourceOverlap("p", "q", I3, (0.0, 0.0, 0.0), I3)
    with pytest.raises(SourceAssembledAtlasError, match="lapse"):
        assemble_source_shared_spacetime_atlas([p, q], [overlap])


def test_spatial_coframe_source_relation_is_fail_closed():
    p = ADMPatch("p", 1.0, I3, (0.0, 0.0, 0.0))
    q = ADMPatch("q", 1.0, ((2.0, 0.0, 0.0), (0.0, 1.0, 0.0), (0.0, 0.0, 1.0)), (0.0, 0.0, 0.0))
    overlap = SpatialSourceOverlap("p", "q", I3, (0.0, 0.0, 0.0), I3)
    with pytest.raises(SourceAssembledAtlasError, match="spatial coframe"):
        assemble_source_shared_spacetime_atlas([p, q], [overlap])


def test_matching_shift_source_relation_is_fail_closed():
    p = ADMPatch("p", 1.0, I3, (0.3, 0.0, 0.0))
    q = ADMPatch("q", 1.0, I3, (0.3, 0.0, 0.0))
    overlap = SpatialSourceOverlap("p", "q", I3, (0.1, 0.0, 0.0), I3)
    with pytest.raises(SourceAssembledAtlasError, match="matching shift"):
        assemble_source_shared_spacetime_atlas([p, q], [overlap])


def test_spatial_orientation_and_so3_rotation_are_explicit_gates():
    p = ADMPatch("p", 1.0, I3, (0.0, 0.0, 0.0))
    q = ADMPatch("q", 1.0, I3, (0.0, 0.0, 0.0))
    reflection = ((-1.0, 0.0, 0.0), (0.0, 1.0, 0.0), (0.0, 0.0, 1.0))
    with pytest.raises(SourceAssembledAtlasError, match="orientation"):
        assemble_source_shared_spacetime_atlas(
            [p, q], [SpatialSourceOverlap("p", "q", reflection, (0.0, 0.0, 0.0), I3)]
        )
    with pytest.raises(SourceAssembledAtlasError, match="SO\(3\)"):
        assemble_source_shared_spacetime_atlas(
            [p, q], [SpatialSourceOverlap("p", "q", I3, (0.0, 0.0, 0.0), reflection)]
        )
