import pytest

from src.rfc.beta_match_shift_source_binding import (
    BetaMatchShiftBindingError,
    audit_beta_match_shift_source_binding,
    matching_overlap,
    matching_patch,
    require_exact_source_binding,
)

C = 299792458.0


def exact_fixture():
    b_p = (0.10, -0.20, 0.05)
    v_t = (3.0, -6.0, 1.5)
    b_q = tuple(b_p[i] - v_t[i] / C for i in range(3))
    beta_p = tuple(C * x for x in b_p)
    beta_q = tuple(C * x for x in b_q)
    patches = [
        matching_patch("p", beta_p, b_p),
        matching_patch("q", beta_q, b_q),
    ]
    overlaps = [matching_overlap("p", "q", ((1, 0, 0), (0, 1, 0), (0, 0, 1)), v_t)]
    return patches, overlaps


def test_exact_binding_passes_on_same_realization_and_clock():
    patches, overlaps = exact_fixture()
    cert = audit_beta_match_shift_source_binding(
        patches,
        overlaps,
        tir_realization_id="R1",
        rfc_realization_id="R1",
        tir_clock_id="clock-05H",
        rfc_clock_id="clock-05H",
    )
    assert cert.source_binding_exact is True
    assert cert.overlap_covariance_pass is True
    assert cert.max_source_binding_defect == pytest.approx(0.0, abs=1e-12)
    assert cert.production_status == "SOURCE_BINDING_CERTIFIED_ON_SUPPLIED_REALIZATION"
    require_exact_source_binding(cert)


def test_nonzero_covariant_w_preserves_both_overlap_laws_but_keeps_binding_open():
    patches, overlaps = exact_fixture()
    w = (5.0, -7.0, 11.0)
    shifted = [
        matching_patch(
            p.patch_id,
            tuple(p.beta_t[i] + w[i] for i in range(3)),
            p.b_x0,
        )
        for p in patches
    ]
    cert = audit_beta_match_shift_source_binding(
        shifted,
        overlaps,
        tir_realization_id="R1",
        rfc_realization_id="R1",
        tir_clock_id="clock-05H",
        rfc_clock_id="clock-05H",
    )
    assert cert.overlap_covariance_pass is True
    assert cert.max_beta_overlap_defect == pytest.approx(0.0, abs=1e-9)
    assert cert.max_shift_overlap_defect == pytest.approx(0.0, abs=1e-15)
    assert cert.max_homogeneous_w_defect == pytest.approx(0.0, abs=1e-9)
    assert cert.source_binding_exact is False
    assert cert.production_status == "PRODUCTION_SOURCE_BINDING_OPEN"
    with pytest.raises(BetaMatchShiftBindingError, match="requires beta_match"):
        require_exact_source_binding(cert)


def test_nontrivial_spatial_jacobian_transports_w_homogeneously():
    a = ((0.0, -1.0, 0.0), (1.0, 0.0, 0.0), (0.0, 0.0, 1.0))
    v_t = (2.0, 4.0, -1.0)
    b_p = (0.2, -0.1, 0.04)
    a_b = (0.1, 0.2, 0.04)
    b_q = tuple(a_b[i] - v_t[i] / C for i in range(3))
    w_p = (3.0, 5.0, 7.0)
    w_q = (-5.0, 3.0, 7.0)
    beta_p = tuple(C * b_p[i] + w_p[i] for i in range(3))
    beta_q = tuple(C * b_q[i] + w_q[i] for i in range(3))
    cert = audit_beta_match_shift_source_binding(
        [matching_patch("p", beta_p, b_p), matching_patch("q", beta_q, b_q)],
        [matching_overlap("p", "q", a, v_t)],
        tir_realization_id="shared",
        rfc_realization_id="shared",
        tir_clock_id="t",
        rfc_clock_id="t",
    )
    assert cert.overlap_covariance_pass is True
    assert cert.source_binding_exact is False
    assert cert.w_by_patch["q"] == pytest.approx(w_q)


def test_mismatched_realization_id_fails_closed():
    patches, overlaps = exact_fixture()
    with pytest.raises(BetaMatchShiftBindingError, match="realization_id"):
        audit_beta_match_shift_source_binding(
            patches,
            overlaps,
            tir_realization_id="TIR-R",
            rfc_realization_id="RFC-R",
            tir_clock_id="clock",
            rfc_clock_id="clock",
        )


def test_mismatched_clock_id_fails_closed():
    patches, overlaps = exact_fixture()
    with pytest.raises(BetaMatchShiftBindingError, match="clock_id"):
        audit_beta_match_shift_source_binding(
            patches,
            overlaps,
            tir_realization_id="R",
            rfc_realization_id="R",
            tir_clock_id="clock-a",
            rfc_clock_id="clock-b",
        )


def test_broken_beta_overlap_covariance_fails_closed():
    patches, overlaps = exact_fixture()
    bad = [patches[0], matching_patch("q", (patches[1].beta_t[0] + 100.0, *patches[1].beta_t[1:]), patches[1].b_x0)]
    with pytest.raises(BetaMatchShiftBindingError, match="covariance defect"):
        audit_beta_match_shift_source_binding(
            bad,
            overlaps,
            tir_realization_id="R",
            rfc_realization_id="R",
            tir_clock_id="clock",
            rfc_clock_id="clock",
        )


def test_broken_shift_overlap_covariance_fails_closed():
    patches, overlaps = exact_fixture()
    bad_b = (patches[1].b_x0[0] + 0.01, patches[1].b_x0[1], patches[1].b_x0[2])
    bad = [patches[0], matching_patch("q", patches[1].beta_t, bad_b)]
    with pytest.raises(BetaMatchShiftBindingError, match="covariance defect"):
        audit_beta_match_shift_source_binding(
            bad,
            overlaps,
            tir_realization_id="R",
            rfc_realization_id="R",
            tir_clock_id="clock",
            rfc_clock_id="clock",
        )


@pytest.mark.parametrize("bad_c", [0.0, -1.0, float("nan"), float("inf")])
def test_invalid_coordinate_scale_fails_closed(bad_c):
    patches, overlaps = exact_fixture()
    with pytest.raises(BetaMatchShiftBindingError):
        audit_beta_match_shift_source_binding(
            patches,
            overlaps,
            tir_realization_id="R",
            rfc_realization_id="R",
            tir_clock_id="clock",
            rfc_clock_id="clock",
            c=bad_c,
        )
