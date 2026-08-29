import math

import pytest

from src.rfc.reduced_gravity_universality_receipt import (
    CouplingProvenance,
    CouplingSystem,
    ReducedGravityReceiptError,
    build_reduced_gravity_universality_receipt,
    receipt_passes,
)


def provenance(tag: str, *, horizon: bool = True, same_horizon_as_dc: bool = False):
    dc = f"dc:{tag}"
    return CouplingProvenance(
        current_measure_receipt_id=f"f24:{tag}",
        phase_rate_receipt_id=f"f21:{tag}",
        source_operator_receipt_id=f"source:{tag}",
        gauge_normalization_receipt_id=f"gauge:{tag}",
        double_copy_receipt_id=dc,
        carrier_scale_receipt_id=f"carrier:{tag}",
        horizon_provenance_id=(dc if same_horizon_as_dc else f"horizon:{tag}") if horizon else None,
    )


def system_a(**overrides):
    values = dict(
        system_id="A",
        gravity_sector_id="gravity:common",
        beta_w=6.0,
        gamma_dc=1.0,
        g_ym_squared=1.0,
        m_star=2.0,
        omega_q=4.0,
        current_j_q=3.0,
        source_s_r=0.75,
        provenance=provenance("A"),
        horizon_mass=8.0 * math.pi,
        horizon_kappa=1.0,
        horizon_temperature=1.0 / (2.0 * math.pi),
    )
    values.update(overrides)
    return CouplingSystem(**values)


def system_b(**overrides):
    values = dict(
        system_id="B",
        gravity_sector_id="gravity:common",
        beta_w=12.0,
        gamma_dc=2.0,
        g_ym_squared=0.5,
        m_star=2.0,
        omega_q=4.0,
        current_j_q=2.0,
        source_s_r=0.5,
        provenance=provenance("B"),
        horizon_mass=4.0 * math.pi,
        horizon_kappa=2.0,
        horizon_temperature=1.0 / math.pi,
    )
    values.update(overrides)
    return CouplingSystem(**values)


def test_two_independent_systems_close_same_reduced_gravity_scale():
    receipt = build_reduced_gravity_universality_receipt((system_a(), system_b()), require_horizon=True)
    assert receipt_passes(receipt)
    assert receipt["max_defect"] == pytest.approx(0.0)
    assert receipt["systems"][0]["mbar_dc"] == pytest.approx(2.0)
    assert receipt["systems"][1]["mbar_dc"] == pytest.approx(2.0)


def test_universal_reduced_scale_implies_universal_g_coordinate():
    receipt = build_reduced_gravity_universality_receipt((system_a(), system_b()), require_horizon=True)
    assert receipt["max_mbar_universality_defect"] == pytest.approx(0.0)
    assert receipt["max_g_universality_defect"] == pytest.approx(0.0)
    expected_g = 1.0 / (32.0 * math.pi)
    assert receipt["systems"][0]["g_dc_natural_units"] == pytest.approx(expected_g)


def test_wilson_normalization_mismatch_is_detected():
    receipt = build_reduced_gravity_universality_receipt((system_a(g_ym_squared=1.1), system_b()))
    assert receipt["systems"][0]["defects"]["wilson_gauge_normalization"] > 0.0
    assert not receipt_passes(receipt)


def test_carrier_scale_mstar_vs_half_omega_is_independently_detected():
    receipt = build_reduced_gravity_universality_receipt((system_a(omega_q=5.0), system_b()))
    assert receipt["systems"][0]["defects"]["carrier_scale_local"] > 0.0
    assert not receipt_passes(receipt)


def test_source_route_perturbation_is_detected():
    receipt = build_reduced_gravity_universality_receipt((system_a(source_s_r=0.8), system_b()))
    assert receipt["systems"][0]["defects"]["source_general"] > 0.0
    assert receipt["systems"][0]["defects"]["source_local"] > 0.0
    assert not receipt_passes(receipt)


def test_horizon_reduced_scale_perturbation_is_detected():
    receipt = build_reduced_gravity_universality_receipt((system_a(horizon_kappa=1.1), system_b()), require_horizon=True)
    assert receipt["systems"][0]["defects"]["dc_horizon_reduced_scale"] > 0.0
    assert not receipt_passes(receipt)


def test_hawking_conversion_is_an_independent_defect():
    receipt = build_reduced_gravity_universality_receipt(
        (system_a(horizon_temperature=0.2), system_b()), require_horizon=True
    )
    assert receipt["systems"][0]["defects"]["horizon_thermal_conversion"] > 0.0
    assert not receipt_passes(receipt)


def test_horizon_provenance_cannot_reuse_double_copy_receipt_id():
    bad = system_a(provenance=provenance("A", same_horizon_as_dc=True))
    receipt = build_reduced_gravity_universality_receipt((bad, system_b()), require_horizon=True)
    assert receipt["systems"][0]["defects"]["horizon_provenance_independence"] == pytest.approx(1.0)
    assert not receipt_passes(receipt)


def test_c2_falsification_fixed_beta_gamma_with_changed_omega_breaks_local_universality():
    other = CouplingSystem(
        system_id="C",
        gravity_sector_id="gravity:common",
        beta_w=6.0,
        gamma_dc=1.0,
        g_ym_squared=1.0,
        m_star=4.0,
        omega_q=8.0,
        current_j_q=3.0,
        source_s_r=0.375,
        provenance=provenance("C", horizon=False),
    )
    receipt = build_reduced_gravity_universality_receipt((system_a(horizon_mass=None, horizon_kappa=None, horizon_temperature=None, provenance=provenance("A0", horizon=False)), other))
    assert receipt["max_local_candidate_universality_defect"] > 0.0
    assert receipt["max_g_universality_defect"] > 0.0
    assert not receipt_passes(receipt)


def test_optional_horizon_route_can_be_omitted_when_not_required():
    a = system_a(horizon_mass=None, horizon_kappa=None, horizon_temperature=None, provenance=provenance("A0", horizon=False))
    b = system_b(horizon_mass=None, horizon_kappa=None, horizon_temperature=None, provenance=provenance("B0", horizon=False))
    receipt = build_reduced_gravity_universality_receipt((a, b), require_horizon=False)
    assert receipt_passes(receipt)
    assert receipt["systems"][0]["horizon"] is None


def test_require_horizon_fails_closed_if_any_system_lacks_horizon_estimator():
    a = system_a(horizon_mass=None, horizon_kappa=None, horizon_temperature=None, provenance=provenance("A0", horizon=False))
    with pytest.raises(ReducedGravityReceiptError):
        build_reduced_gravity_universality_receipt((a, system_b()), require_horizon=True)


def test_cross_system_comparison_requires_same_gravity_sector():
    with pytest.raises(ReducedGravityReceiptError):
        build_reduced_gravity_universality_receipt((system_a(), system_b(gravity_sector_id="gravity:other")))


def test_cross_system_comparison_requires_unique_system_ids():
    with pytest.raises(ReducedGravityReceiptError):
        build_reduced_gravity_universality_receipt((system_a(), system_b(system_id="A")))


def test_cross_system_comparison_requires_at_least_two_systems():
    with pytest.raises(ReducedGravityReceiptError):
        build_reduced_gravity_universality_receipt((system_a(),))


def test_horizon_output_uses_none_not_nan_when_only_one_horizon_estimator_is_supplied():
    a = system_a(horizon_temperature=None)
    b = system_b(horizon_temperature=None)
    receipt = build_reduced_gravity_universality_receipt((a, b), require_horizon=True)
    assert receipt["systems"][0]["horizon"]["mbar_t"] is None


def test_explicit_tolerance_can_admit_tiny_numeric_residual_only_when_selected():
    receipt = build_reduced_gravity_universality_receipt((system_a(source_s_r=0.75 + 1e-13), system_b()))
    assert not receipt_passes(receipt)
    assert receipt_passes(receipt, atol=1e-12)
