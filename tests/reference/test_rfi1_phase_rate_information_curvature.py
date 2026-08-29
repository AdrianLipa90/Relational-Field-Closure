import math

import pytest

from src.rfc.phase_rate_information_curvature import (
    PhaseRateInformationCurvatureError,
    clock_scalar_potential_density,
    constant_cell_information_curvature,
    constant_phase_clock_area,
    directional_rate_ratio,
    homogeneous_clock_action_energy,
    information_curvature,
    phase_rate_information_nats,
    phi,
)


def test_idt_05f_rate_information_is_exact_phi_of_inverse_ratio():
    rs, r0 = 1.4, 2.0
    ratio, x = directional_rate_ratio(rs, r0)
    assert ratio == pytest.approx(rs / r0)
    assert x == pytest.approx(r0 / rs)
    assert phase_rate_information_nats(rs, r0) == pytest.approx(phi(x))


def test_rfe16_directional_specialization_matches_rfe14_branch():
    r0 = 2.3
    b = 0.27
    for s in (-1, 1):
        rs = r0 * (1.0 - s * b)
        j = phase_rate_information_nats(rs, r0)
        x = 1.0 / (1.0 - s * b)
        expected = math.log(1.0 - s * b) + (s * b) / (1.0 - s * b)
        assert j == pytest.approx(phi(x))
        assert j == pytest.approx(expected)


def test_common_phase_rate_scale_preserves_information_numerator():
    rs, r0 = 1.3, 2.1
    base = phase_rate_information_nats(rs, r0)
    for scale in (0.25, 3.0, 11.0):
        assert phase_rate_information_nats(scale * rs, scale * r0) == pytest.approx(base)


def test_01k_area_binding_has_inverse_area_scaling():
    rs, r0 = 1.3, 2.1
    area = 4.2
    xi = information_curvature(rs, r0, area)
    assert xi == pytest.approx(phase_rate_information_nats(rs, r0) / area)
    assert information_curvature(rs, r0, 9.0 * area) == pytest.approx(xi / 9.0)


def test_constant_phase_clock_cell_matches_01k_formula():
    rs, r0 = 1.5, 2.4
    a_fs = math.pi
    c = 3.0
    area = constant_phase_clock_area(r0, a_fs, c)
    expected_area = (c * c / (r0 * r0)) * a_fs
    assert area == pytest.approx(expected_area)

    xi = constant_cell_information_curvature(rs, r0, a_fs, c)
    expected_xi = (phase_rate_information_nats(rs, r0) / a_fs) * (r0 / c) ** 2
    assert xi == pytest.approx(expected_xi)


def test_rf_l3_rfe17_potential_route_is_exact_composition():
    rs, r0 = 1.6, 2.2
    area = 3.7
    alpha = 0.45
    kappa_e = 1.8
    xi = information_curvature(rs, r0, area)
    u = clock_scalar_potential_density(rs, r0, area, alpha, kappa_e)
    assert u == pytest.approx((alpha / kappa_e) * xi)
    assert u == pytest.approx((alpha / (kappa_e * area)) * phase_rate_information_nats(rs, r0))


def test_homogeneous_cell_recovers_rfe17_Estar_phi_factorization():
    rs, r0 = 1.2, 2.0
    area = 2.5
    volume = 4.1
    alpha = 0.6
    kappa_e = 1.7
    h, e_star, j = homogeneous_clock_action_energy(rs, r0, area, volume, alpha, kappa_e)
    assert e_star == pytest.approx((alpha / kappa_e) * volume / area)
    assert j == pytest.approx(phase_rate_information_nats(rs, r0))
    assert h == pytest.approx(e_star * j)


def test_equal_phase_rates_give_zero_information_curvature_and_potential():
    r = 1.8
    area = 3.0
    assert phase_rate_information_nats(r, r) == pytest.approx(0.0, abs=1.0e-15)
    assert information_curvature(r, r, area) == pytest.approx(0.0, abs=1.0e-15)
    assert clock_scalar_potential_density(r, r, area, 0.5, 2.0) == pytest.approx(0.0, abs=1.0e-15)


def test_information_source_does_not_require_activity_lapse_identity():
    # The RF-I1 source is the phase-rate pair itself. An unrelated activity lapse
    # can differ without changing the exact phase-rate information value.
    rs, r0 = 1.4, 2.0
    unrelated_activity_lapse = 3.7
    j = phase_rate_information_nats(rs, r0)
    assert j == pytest.approx(phi(r0 / rs))
    assert unrelated_activity_lapse != pytest.approx(r0 / rs)


@pytest.mark.parametrize("bad", [0.0, -1.0, math.inf, math.nan])
def test_invalid_positive_carriers_fail_closed(bad):
    with pytest.raises(PhaseRateInformationCurvatureError):
        phase_rate_information_nats(bad, 1.0)
    with pytest.raises(PhaseRateInformationCurvatureError):
        information_curvature(1.0, 2.0, bad)
    with pytest.raises(PhaseRateInformationCurvatureError):
        constant_phase_clock_area(1.0, bad)
