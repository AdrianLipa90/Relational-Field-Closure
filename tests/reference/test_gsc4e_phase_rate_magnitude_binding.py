import pytest

from src.rfc.phase_rate_magnitude_binding import (
    PhaseMagnitudeBindingError,
    certify_phase_rate_magnitude_binding,
    phase_magnitude_overlap_sample,
    require_spatial_scale_binding,
)


def sample(source, target, sid, source_rate, target_rate, *, clock="clock-1", field="nu-field"):
    return phase_magnitude_overlap_sample(
        source, target, sid, clock, field, source_rate, target_rate
    )


def test_equal_magnitudes_certify_spatial_scale_binding():
    cert = certify_phase_rate_magnitude_binding([sample("p", "q", "x", 5.0, 5.0)])
    assert cert.spatial_scale_binding_certified is True
    assert cert.max_magnitude_defect == pytest.approx(0.0)
    assert cert.max_scale_defect == pytest.approx(0.0)
    assert cert.overlap_local_field_semantics is True
    require_spatial_scale_binding(cert)


def test_sign_flip_preserves_spatial_scale_without_signed_rate_identity():
    cert = certify_phase_rate_magnitude_binding([sample("p", "q", "x", 7.0, -7.0)])
    result = cert.samples[0]
    assert result.spatial_scale_binding is True
    assert result.signed_rate_equal is False
    assert cert.signed_rate_identity_required is False
    assert cert.max_scale_defect == pytest.approx(0.0)


def test_connected_cover_can_use_different_magnitudes_at_different_overlap_samples():
    cert = certify_phase_rate_magnitude_binding(
        [
            sample("p", "q", "x-pq", 2.0, -2.0),
            sample("q", "r", "y-qr", 3.0, -3.0),
        ]
    )
    assert cert.spatial_scale_binding_certified is True
    assert cert.samples[0].magnitude_defect == pytest.approx(0.0)
    assert cert.samples[1].magnitude_defect == pytest.approx(0.0)
    assert cert.samples[0].scale_defect == pytest.approx(0.0)
    assert cert.samples[1].scale_defect == pytest.approx(0.0)


def test_one_overlap_can_have_multiple_points_with_different_field_values():
    cert = certify_phase_rate_magnitude_binding(
        [
            sample("p", "q", "x0", 2.0, 2.0),
            sample("p", "q", "x1", 4.0, -4.0),
        ]
    )
    assert cert.spatial_scale_binding_certified is True
    assert cert.samples[0].signed_rate_equal is True
    assert cert.samples[1].signed_rate_equal is False


def test_magnitude_mismatch_fails_binding():
    cert = certify_phase_rate_magnitude_binding([sample("p", "q", "x", 5.0, -6.0)])
    assert cert.spatial_scale_binding_certified is False
    with pytest.raises(PhaseMagnitudeBindingError):
        require_spatial_scale_binding(cert)


def test_clock_and_magnitude_field_ids_are_explicit_source_provenance():
    s = sample("p", "q", "x", 5.0, -5.0, clock="clock-prod", field="nu-prod")
    cert = certify_phase_rate_magnitude_binding([s])
    result = cert.samples[0]
    assert result.clock_id == "clock-prod"
    assert result.phase_magnitude_field_id == "nu-prod"


def test_empty_source_identifiers_fail_closed():
    with pytest.raises(PhaseMagnitudeBindingError):
        phase_magnitude_overlap_sample("p", "q", "", "clock", "nu", 2.0, 2.0)
    with pytest.raises(PhaseMagnitudeBindingError):
        phase_magnitude_overlap_sample("p", "q", "x", "", "nu", 2.0, 2.0)
    with pytest.raises(PhaseMagnitudeBindingError):
        phase_magnitude_overlap_sample("p", "q", "x", "clock", "", 2.0, 2.0)


def test_zero_and_nonfinite_rates_fail_closed():
    for bad in (0.0, float("nan"), float("inf"), -float("inf")):
        with pytest.raises(PhaseMagnitudeBindingError):
            phase_magnitude_overlap_sample("p", "q", "x", "clock", "nu", bad, 2.0)
        with pytest.raises(PhaseMagnitudeBindingError):
            phase_magnitude_overlap_sample("p", "q", "x", "clock", "nu", 2.0, bad)


def test_duplicate_sample_identity_fails_closed():
    x = sample("p", "q", "x", 2.0, 2.0)
    with pytest.raises(PhaseMagnitudeBindingError, match="unique"):
        certify_phase_rate_magnitude_binding([x, x])


def test_production_source_remains_open_after_reference_certification():
    cert = certify_phase_rate_magnitude_binding([sample("p", "q", "x", 5.0, -5.0)])
    assert cert.spatial_scale_binding_certified is True
    assert cert.production_status == "PRODUCTION_OVERLAP_LOCAL_PHASE_MAGNITUDE_FIELD_SOURCE_OPEN"
