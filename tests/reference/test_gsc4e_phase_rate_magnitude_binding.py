import pytest

from src.rfc.phase_rate_magnitude_binding import (
    PhaseMagnitudeBindingError,
    certify_phase_rate_magnitude_binding,
    phase_magnitude_patch,
    require_spatial_scale_binding,
)


def test_equal_magnitudes_certify_spatial_scale_binding():
    p = phase_magnitude_patch("p", "clock-1", "nu-field", 5.0)
    q = phase_magnitude_patch("q", "clock-1", "nu-field", 5.0)
    cert = certify_phase_rate_magnitude_binding([p, q], [("p", "q")])
    assert cert.spatial_scale_binding_certified is True
    assert cert.max_magnitude_defect == pytest.approx(0.0)
    assert cert.max_scale_defect == pytest.approx(0.0)
    require_spatial_scale_binding(cert)


def test_sign_flip_preserves_spatial_scale_without_signed_rate_identity():
    p = phase_magnitude_patch("p", "clock-1", "nu-field", 7.0)
    q = phase_magnitude_patch("q", "clock-1", "nu-field", -7.0)
    cert = certify_phase_rate_magnitude_binding([p, q], [("p", "q")])
    ov = cert.overlaps[0]
    assert ov.spatial_scale_binding is True
    assert ov.signed_rate_equal is False
    assert cert.signed_rate_identity_required is False
    assert p.spatial_scale == pytest.approx(q.spatial_scale)


def test_magnitude_mismatch_fails_binding():
    p = phase_magnitude_patch("p", "clock-1", "nu-field", 5.0)
    q = phase_magnitude_patch("q", "clock-1", "nu-field", -6.0)
    cert = certify_phase_rate_magnitude_binding([p, q], [("p", "q")])
    assert cert.spatial_scale_binding_certified is False
    with pytest.raises(PhaseMagnitudeBindingError):
        require_spatial_scale_binding(cert)


def test_field_identity_mismatch_fails_even_when_numeric_magnitude_matches():
    p = phase_magnitude_patch("p", "clock-1", "nu-a", 5.0)
    q = phase_magnitude_patch("q", "clock-1", "nu-b", -5.0)
    cert = certify_phase_rate_magnitude_binding([p, q], [("p", "q")])
    assert cert.overlaps[0].magnitude_defect == pytest.approx(0.0)
    assert cert.spatial_scale_binding_certified is False


def test_clock_identity_mismatch_fails_even_when_field_and_magnitude_match():
    p = phase_magnitude_patch("p", "clock-a", "nu-field", 5.0)
    q = phase_magnitude_patch("q", "clock-b", "nu-field", -5.0)
    cert = certify_phase_rate_magnitude_binding([p, q], [("p", "q")])
    assert cert.spatial_scale_binding_certified is False


def test_zero_and_nonfinite_rates_fail_closed():
    for bad in (0.0, float("nan"), float("inf"), -float("inf")):
        with pytest.raises(PhaseMagnitudeBindingError):
            phase_magnitude_patch("p", "clock-1", "nu-field", bad)


def test_unknown_overlap_patch_fails_closed():
    p = phase_magnitude_patch("p", "clock-1", "nu-field", 5.0)
    with pytest.raises(PhaseMagnitudeBindingError):
        certify_phase_rate_magnitude_binding([p], [("p", "q")])


def test_production_source_remains_open_after_reference_certification():
    p = phase_magnitude_patch("p", "clock-1", "nu-field", 5.0)
    cert = certify_phase_rate_magnitude_binding([p], [])
    assert cert.spatial_scale_binding_certified is True
    assert cert.production_status == "PRODUCTION_PHASE_MAGNITUDE_FIELD_SOURCE_OPEN"
