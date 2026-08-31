import pytest

from src.rfc.beta_shift_interface_alias import (
    BetaShiftInterfaceAliasError,
    certify_beta_shift_interface_alias,
)


I3 = (
    (1.0, 0.0, 0.0),
    (0.0, 1.0, 0.0),
    (0.0, 0.0, 1.0),
)


def test_rf_e8_specialization_beta_equals_c_times_shift():
    c = 299792458.0
    cert = certify_beta_shift_interface_alias(
        tir_patch_id="P",
        rfc_patch_id="P",
        tir_clock_id="clock-1",
        rfc_clock_id="clock-1",
        temporal_scale=c,
        beta_theta=(c * 0.1, c * -0.2, c * 0.3),
        b_zero=(0.1, -0.2, 0.3),
        atol=1.0e-7,
    )
    assert cert.compatible is True
    assert cert.temporal_scale == pytest.approx(c)
    assert cert.coefficient_residual <= 1.0e-7


def test_general_positive_temporal_scale():
    cert = certify_beta_shift_interface_alias(
        tir_patch_id="P",
        rfc_patch_id="P",
        tir_clock_id="theta",
        rfc_clock_id="theta",
        temporal_scale=2.5,
        beta_theta=(1.0, -2.0, 0.5),
        b_zero=(0.4, -0.8, 0.2),
    )
    assert cert.compatible is True


def test_patch_identity_is_explicit_gate():
    with pytest.raises(BetaShiftInterfaceAliasError, match="same patch identity"):
        certify_beta_shift_interface_alias(
            tir_patch_id="TIR-P",
            rfc_patch_id="RFC-P",
            tir_clock_id="clock",
            rfc_clock_id="clock",
            temporal_scale=1.0,
            beta_theta=(0.0, 0.0, 0.0),
            b_zero=(0.0, 0.0, 0.0),
        )


def test_clock_identity_is_explicit_gate():
    with pytest.raises(BetaShiftInterfaceAliasError, match="same clock identity"):
        certify_beta_shift_interface_alias(
            tir_patch_id="P",
            rfc_patch_id="P",
            tir_clock_id="clock-A",
            rfc_clock_id="clock-B",
            temporal_scale=1.0,
            beta_theta=(0.0, 0.0, 0.0),
            b_zero=(0.0, 0.0, 0.0),
        )


def test_coefficient_mismatch_fails_closed():
    with pytest.raises(BetaShiftInterfaceAliasError, match="coefficient alias"):
        certify_beta_shift_interface_alias(
            tir_patch_id="P",
            rfc_patch_id="P",
            tir_clock_id="clock",
            rfc_clock_id="clock",
            temporal_scale=2.0,
            beta_theta=(2.0, 0.0, 0.0),
            b_zero=(0.5, 0.0, 0.0),
        )


def test_time_dependent_spatial_relabeling_preserves_alias():
    alpha = 4.0
    beta_p = (4.0, 8.0, -4.0)
    b_p = (1.0, 2.0, -1.0)
    v_zero = (0.5, -0.25, 1.0)
    v_theta = tuple(alpha * x for x in v_zero)
    beta_q = tuple(beta_p[i] - v_theta[i] for i in range(3))
    b_q = tuple(b_p[i] - v_zero[i] for i in range(3))

    cert = certify_beta_shift_interface_alias(
        tir_patch_id="P",
        rfc_patch_id="P",
        tir_clock_id="clock",
        rfc_clock_id="clock",
        temporal_scale=alpha,
        beta_theta=beta_p,
        b_zero=b_p,
        spatial_jacobian=I3,
        drift_theta=v_theta,
        drift_zero=v_zero,
        beta_theta_target=beta_q,
        b_zero_target=b_q,
    )
    assert cert.drift_scale_residual == pytest.approx(0.0)
    assert cert.target_alias_residual == pytest.approx(0.0)


def test_overlap_requires_complete_data_bundle():
    with pytest.raises(BetaShiftInterfaceAliasError, match="complete overlap data"):
        certify_beta_shift_interface_alias(
            tir_patch_id="P",
            rfc_patch_id="P",
            tir_clock_id="clock",
            rfc_clock_id="clock",
            temporal_scale=1.0,
            beta_theta=(0.0, 0.0, 0.0),
            b_zero=(0.0, 0.0, 0.0),
            spatial_jacobian=I3,
        )
