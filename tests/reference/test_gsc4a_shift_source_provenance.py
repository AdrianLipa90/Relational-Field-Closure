import pytest

from src.rfc.gsc4a_shift_source_provenance import (
    RFC_INDEPENDENT_SHIFT,
    TIR_BETA_MATCH_BOUND,
    ShiftSourceProvenance,
    ShiftSourceProvenanceError,
    assemble_provenance_typed_source_shared_spacetime_atlas,
    certify_shift_source_provenance,
    rfc_independent_shift_source,
    tir_beta_match_bound_shift_source,
)
from src.rfc.shared_spacetime_atlas import ADMPatch
from src.rfc.source_assembled_shared_spacetime_atlas import SpatialSourceOverlap

I3 = (
    (1.0, 0.0, 0.0),
    (0.0, 1.0, 0.0),
    (0.0, 0.0, 1.0),
)


def two_patch_geometry():
    p = ADMPatch("p", 1.0, I3, (0.2, -0.1, 0.3))
    q = ADMPatch("q", 1.0, I3, (0.15, -0.12, 0.34))
    ov = SpatialSourceOverlap("p", "q", I3, (0.05, 0.02, -0.04), I3)
    return [p, q], [ov]


def independent(pid):
    return rfc_independent_shift_source(
        patch_id=pid,
        realization_id="R1",
        clock_id="clock-05H",
        source_reference=f"RFC:shift:{pid}:receipt",
    )


def tir_bound(pid):
    return tir_beta_match_bound_shift_source(
        patch_id=pid,
        realization_id="R1",
        clock_id="clock-05H",
        source_reference=f"TIR:beta_match:{pid}:receipt",
        gsc3d_alias_receipt="RFC:GSC3D:ae168059",
        gsc3e_w0_receipt="RFC:GSC3E:ab31c1fb",
    )


def test_rfc_independent_shift_route_reaches_exact_gsc4a_geometry_without_gsc3e_receipt():
    patches, overlaps = two_patch_geometry()
    cert = assemble_provenance_typed_source_shared_spacetime_atlas(
        patches,
        overlaps,
        shift_provenance=[independent("p"), independent("q")],
    )
    assert cert.geometry.compatible is True
    assert cert.geometry.rf_e25.compatible is True
    assert set(cert.routes_by_patch.values()) == {RFC_INDEPENDENT_SHIFT}


def test_tir_beta_match_route_requires_and_accepts_gsc3d_plus_gsc3e_receipts():
    patches, overlaps = two_patch_geometry()
    cert = assemble_provenance_typed_source_shared_spacetime_atlas(
        patches,
        overlaps,
        shift_provenance=[tir_bound("p"), tir_bound("q")],
    )
    assert cert.geometry.rf_e25.compatible is True
    assert set(cert.routes_by_patch.values()) == {TIR_BETA_MATCH_BOUND}


def test_tir_route_without_gsc3d_alias_receipt_fails_closed():
    patches, _ = two_patch_geometry()
    records = [
        ShiftSourceProvenance(
            patch_id=pid,
            route=TIR_BETA_MATCH_BOUND,
            source_owner="TIR",
            realization_id="R1",
            clock_id="clock-05H",
            source_reference=f"TIR:{pid}",
            gsc3d_alias_receipt=None,
            gsc3e_w0_receipt="GSC3E:receipt",
        )
        for pid in ("p", "q")
    ]
    with pytest.raises(ShiftSourceProvenanceError, match="gsc3d_alias_receipt"):
        certify_shift_source_provenance(patches, records)


def test_tir_route_without_gsc3e_w0_receipt_fails_closed():
    patches, _ = two_patch_geometry()
    records = [
        ShiftSourceProvenance(
            patch_id=pid,
            route=TIR_BETA_MATCH_BOUND,
            source_owner="TIR",
            realization_id="R1",
            clock_id="clock-05H",
            source_reference=f"TIR:{pid}",
            gsc3d_alias_receipt="GSC3D:receipt",
            gsc3e_w0_receipt=None,
        )
        for pid in ("p", "q")
    ]
    with pytest.raises(ShiftSourceProvenanceError, match="gsc3e_w0_receipt"):
        certify_shift_source_provenance(patches, records)


def test_route_owner_mismatch_fails_closed():
    patches, _ = two_patch_geometry()
    bad = ShiftSourceProvenance(
        patch_id="p",
        route=RFC_INDEPENDENT_SHIFT,
        source_owner="TIR",
        realization_id="R1",
        clock_id="clock-05H",
        source_reference="bad",
    )
    with pytest.raises(ShiftSourceProvenanceError, match="source_owner=RFC"):
        certify_shift_source_provenance(patches, [bad, independent("q")])


def test_provenance_must_cover_exact_patch_set():
    patches, _ = two_patch_geometry()
    with pytest.raises(ShiftSourceProvenanceError, match="coverage mismatch"):
        certify_shift_source_provenance(patches, [independent("p")])


def test_provenance_requires_one_common_realization_and_clock():
    patches, _ = two_patch_geometry()
    q_other_r = rfc_independent_shift_source(
        patch_id="q", realization_id="R2", clock_id="clock-05H", source_reference="RFC:q"
    )
    with pytest.raises(ShiftSourceProvenanceError, match="realization_id"):
        certify_shift_source_provenance(patches, [independent("p"), q_other_r])

    q_other_t = rfc_independent_shift_source(
        patch_id="q", realization_id="R1", clock_id="clock-other", source_reference="RFC:q"
    )
    with pytest.raises(ShiftSourceProvenanceError, match="clock_id"):
        certify_shift_source_provenance(patches, [independent("p"), q_other_t])


def test_mixed_routes_are_admissible_on_one_realization_when_each_route_is_certified():
    patches, overlaps = two_patch_geometry()
    cert = assemble_provenance_typed_source_shared_spacetime_atlas(
        patches,
        overlaps,
        shift_provenance=[independent("p"), tir_bound("q")],
    )
    assert cert.geometry.compatible is True
    assert cert.routes_by_patch == {"p": RFC_INDEPENDENT_SHIFT, "q": TIR_BETA_MATCH_BOUND}
    assert cert.production_source_ownership_status == "SOURCE_CONTROLLED_PROVENANCE_REQUIRED"
