import math

import pytest

from src.rfc.tree_amplitude_identifiability_no_go import (
    TreeAmplitudeCoordinates,
    TreeAmplitudeIdentifiabilityError,
    build_tree_amplitude_identifiability_receipt,
    receipt_passes,
)


def coords(**overrides):
    values = dict(
        g1=1.0,
        g2=1.0,
        gamma_dc=1.0,
        m_star=3.0,
        epsilon_q=3.0,
        zeta_m=1.0,
    )
    values.update(overrides)
    return TreeAmplitudeCoordinates(**values)


def test_common_gamma_zeta_mstar_scaling_is_exact_null_direction():
    receipt = build_tree_amplitude_identifiability_receipt(
        coords(), scale_lambda=7.3, multiplicities=(3, 4, 5, 6, 7)
    )
    assert receipt_passes(receipt, atol=1e-15)
    assert receipt["null_direction_log_gamma_log_zeta"] == (1.0, 1.0)
    assert receipt["identifiability_rank"] == 1


def test_kappa_g_and_kappa_e_are_invariant_under_null_scaling():
    receipt = build_tree_amplitude_identifiability_receipt(coords(), scale_lambda=2.0)
    assert receipt["base"]["kappa_g"] == pytest.approx(receipt["scaled"]["kappa_g"])
    assert receipt["base"]["kappa_e"] == pytest.approx(receipt["scaled"]["kappa_e"])


def test_reduced_gravity_scale_is_invariant_under_null_scaling():
    receipt = build_tree_amplitude_identifiability_receipt(coords(), scale_lambda=5.0)
    assert receipt["base"]["mbar_g"] == pytest.approx(receipt["scaled"]["mbar_g"])


def test_gamma_over_zeta_is_the_identifiable_combination():
    receipt = build_tree_amplitude_identifiability_receipt(coords(), scale_lambda=11.0)
    assert receipt["identifiable_combination"] == "Gamma_DC/zeta_M"
    assert receipt["base"]["gamma_over_zeta"] == pytest.approx(
        receipt["scaled"]["gamma_over_zeta"]
    )


def test_every_tree_prefactor_is_invariant_for_multiple_multiplicities():
    receipt = build_tree_amplitude_identifiability_receipt(
        coords(), scale_lambda=3.0, multiplicities=tuple(range(3, 10))
    )
    for defect in receipt["prefactor_defects"].values():
        assert defect == pytest.approx(0.0)


def test_tree_prefactor_has_expected_n_minus_two_power():
    receipt = build_tree_amplitude_identifiability_receipt(
        coords(), scale_lambda=1.0, multiplicities=(3, 4, 5)
    )
    kappa_half = receipt["base"]["kappa_g"] / 2.0
    assert receipt["base"]["tree_prefactors"][3] == pytest.approx(kappa_half)
    assert receipt["base"]["tree_prefactors"][4] == pytest.approx(kappa_half**2)
    assert receipt["base"]["tree_prefactors"][5] == pytest.approx(kappa_half**3)


def test_kinetic_and_total_rest_branches_can_be_gravitationally_degenerate():
    kinetic = build_tree_amplitude_identifiability_receipt(
        coords(gamma_dc=1.0, m_star=3.0, zeta_m=1.0), scale_lambda=1.0
    )
    rest = build_tree_amplitude_identifiability_receipt(
        coords(gamma_dc=2.0, m_star=6.0, zeta_m=2.0), scale_lambda=1.0
    )
    assert kinetic["base"]["kappa_g"] == pytest.approx(rest["base"]["kappa_g"])
    assert kinetic["base"]["kappa_e"] == pytest.approx(rest["base"]["kappa_e"])
    assert kinetic["base"]["mbar_g"] == pytest.approx(rest["base"]["mbar_g"])


def test_gamma_change_without_mstar_change_is_observable():
    a = build_tree_amplitude_identifiability_receipt(coords(gamma_dc=1.0), scale_lambda=1.0)
    b = build_tree_amplitude_identifiability_receipt(coords(gamma_dc=2.0), scale_lambda=1.0)
    assert b["base"]["kappa_g"] == pytest.approx(2.0 * a["base"]["kappa_g"])
    assert b["base"]["kappa_e"] == pytest.approx(4.0 * a["base"]["kappa_e"])


def test_mstar_change_without_gamma_change_is_observable():
    a = build_tree_amplitude_identifiability_receipt(coords(m_star=3.0), scale_lambda=1.0)
    b = build_tree_amplitude_identifiability_receipt(
        coords(m_star=6.0, zeta_m=2.0), scale_lambda=1.0
    )
    assert b["base"]["kappa_g"] == pytest.approx(0.5 * a["base"]["kappa_g"])


def test_carrier_relation_is_a_separate_gate():
    receipt = build_tree_amplitude_identifiability_receipt(
        coords(m_star=4.0), scale_lambda=2.0
    )
    assert receipt["defects"]["base_carrier_relation"] > 0.0
    assert not receipt_passes(receipt)


def test_log_sensitivity_has_rank_one_and_common_null_direction():
    receipt = build_tree_amplitude_identifiability_receipt(coords(), scale_lambda=2.0)
    assert receipt["log_sensitivity_kappa_g"] == {"gamma_dc": 1.0, "zeta_m": -1.0}
    assert receipt["log_sensitivity_kappa_e"] == {"gamma_dc": 2.0, "zeta_m": -2.0}
    assert receipt["null_scaling_dimension"] == 1


def test_scale_lambda_must_be_positive():
    with pytest.raises(TreeAmplitudeIdentifiabilityError):
        build_tree_amplitude_identifiability_receipt(coords(), scale_lambda=0.0)


def test_tree_multiplicity_must_be_integer_at_least_three():
    with pytest.raises(TreeAmplitudeIdentifiabilityError):
        build_tree_amplitude_identifiability_receipt(coords(), scale_lambda=1.0, multiplicities=(2, 3))
    with pytest.raises(TreeAmplitudeIdentifiabilityError):
        build_tree_amplitude_identifiability_receipt(coords(), scale_lambda=1.0, multiplicities=())


def test_nonfinite_coordinates_fail_closed():
    with pytest.raises(TreeAmplitudeIdentifiabilityError):
        coords(gamma_dc=math.nan)


def test_tolerance_is_explicit_for_roundoff_only():
    receipt = build_tree_amplitude_identifiability_receipt(
        coords(), scale_lambda=1.1, multiplicities=(3, 4, 5, 8)
    )
    assert receipt_passes(receipt, atol=1e-14)
