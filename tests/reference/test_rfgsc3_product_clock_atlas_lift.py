import pytest

from src.rfc.product_clock_atlas_lift import (
    ProductClockAtlasLiftError,
    SpatialAtlasTransition,
    certify_product_clock_atlas_lift,
    det3,
)


I3 = (
    (1.0, 0.0, 0.0),
    (0.0, 1.0, 0.0),
    (0.0, 0.0, 1.0),
)


def test_single_patch_product_clock_is_regular_four_dimensional():
    cert = certify_product_clock_atlas_lift(["A"], [])
    assert cert.compatible is True
    assert cert.spacetime_dimension == 4
    assert cert.shared_clock_first_row is True
    assert cert.dt_nowhere_zero is True
    assert cert.connected is True
    assert cert.physical_product_realization_status == "OPEN_INPUT"


def test_time_dependent_spatial_relabeling_preserves_shared_clock_row_and_det():
    overlap = SpatialAtlasTransition(
        "A",
        "B",
        I3,
        time_drift=(0.25, -0.5, 0.75),
    )
    cert = certify_product_clock_atlas_lift(["A", "B"], [overlap])
    assert overlap.spacetime_jacobian[0] == (1.0, 0.0, 0.0, 0.0)
    assert det3(overlap.spatial_jacobian) == pytest.approx(1.0)
    assert cert.min_spatial_orientation_det == pytest.approx(1.0)
    assert cert.dt_nowhere_zero is True


def test_declared_triple_inherits_spatial_and_time_drift_cocycle():
    a_qp = (
        (2.0, 0.0, 0.0),
        (0.0, 1.0, 0.0),
        (0.0, 0.0, 1.0),
    )
    a_rq = (
        (1.0, 1.0, 0.0),
        (0.0, 1.0, 0.0),
        (0.0, 0.0, 1.0),
    )
    a_rp = (
        (2.0, 1.0, 0.0),
        (0.0, 1.0, 0.0),
        (0.0, 0.0, 1.0),
    )
    v_qp = (1.0, 2.0, 3.0)
    v_rq = (0.5, -1.0, 2.0)
    # v_rp = v_rq + A_rq v_qp = (0.5,-1,2) + (3,2,3)
    v_rp = (3.5, 1.0, 5.0)

    transitions = [
        SpatialAtlasTransition("P", "Q", a_qp, v_qp),
        SpatialAtlasTransition("Q", "R", a_rq, v_rq),
        SpatialAtlasTransition("P", "R", a_rp, v_rp),
    ]
    cert = certify_product_clock_atlas_lift(
        ["P", "Q", "R"],
        transitions,
        triangles=[("P", "Q", "R")],
    )
    assert cert.triangle_count == 1
    assert cert.max_spatial_cocycle_residual == pytest.approx(0.0)
    assert cert.max_time_drift_cocycle_residual == pytest.approx(0.0)


def test_orientation_reversing_spatial_overlap_fails_closed():
    reflection = (
        (-1.0, 0.0, 0.0),
        (0.0, 1.0, 0.0),
        (0.0, 0.0, 1.0),
    )
    with pytest.raises(ProductClockAtlasLiftError, match="orientation preserving"):
        certify_product_clock_atlas_lift(
            ["A", "B"],
            [SpatialAtlasTransition("A", "B", reflection)],
        )


def test_disconnected_product_atlas_fails_connected_domain_claim():
    with pytest.raises(ProductClockAtlasLiftError, match="disconnected"):
        certify_product_clock_atlas_lift(["A", "B"], [])


def test_bad_time_drift_cocycle_fails_closed():
    transitions = [
        SpatialAtlasTransition("P", "Q", I3, (1.0, 0.0, 0.0)),
        SpatialAtlasTransition("Q", "R", I3, (0.0, 1.0, 0.0)),
        SpatialAtlasTransition("P", "R", I3, (0.0, 0.0, 0.0)),
    ]
    with pytest.raises(ProductClockAtlasLiftError, match="time-drift cocycle"):
        certify_product_clock_atlas_lift(
            ["P", "Q", "R"],
            transitions,
            triangles=[("P", "Q", "R")],
        )
