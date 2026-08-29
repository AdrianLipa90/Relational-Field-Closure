import math

import pytest

from src.rfc.noether_shannon_radial_source_binding import (
    NoetherShannonRadialBindingError,
    baseline_adjusted_information,
    fisher_radial_norm_sq,
    local_fisher_quadratic_curvature,
    local_fisher_residual,
    noether_radial_amplitude_sq,
    shannon_radial_curvature,
    shannon_relative_information_nats,
    source_binding_defect,
    source_binding_defect_product_form,
    source_binding_ratio,
    source_binding_residual,
    stationary_zero_baseline_residual,
)


def test_shannon_relative_information_is_computed_from_probability_data():
    p = (0.75, 0.25)
    pi = (0.5, 0.5)
    expected = 0.75 * math.log(1.5) + 0.25 * math.log(0.5)
    assert shannon_relative_information_nats(p, pi) == pytest.approx(expected)


def test_exact_zero_baseline_binding_from_independent_kl_and_noether_inputs():
    p = (0.61, 0.29, 0.10)
    pi = (0.50, 0.30, 0.20)
    j_pi = shannon_relative_information_nats(p, pi)
    area = 3.7
    r_s = 1.9
    xi = j_pi / area
    j_vartheta = 2.0 * r_s * xi

    assert shannon_radial_curvature(j_pi, area, 0.0) == pytest.approx(xi)
    assert noether_radial_amplitude_sq(j_vartheta, r_s) == pytest.approx(xi)
    assert stationary_zero_baseline_residual(
        j_pi, area, j_vartheta, r_s
    ) == pytest.approx(0.0, abs=2.0e-14)
    assert source_binding_defect(
        j_pi, area, 0.0, j_vartheta, r_s
    ) == pytest.approx(0.0, abs=2.0e-14)
    assert source_binding_ratio(
        j_pi, area, 0.0, j_vartheta, r_s
    ) == pytest.approx(1.0)


def test_nonzero_baseline_roundtrip_is_exact():
    area = 5.0
    xi_star = 0.02
    xi_bar = 0.11
    j_pi = area * (xi_star + xi_bar)
    r_s = 1.7
    j_vartheta = 2.0 * r_s * xi_bar

    assert baseline_adjusted_information(j_pi, area, xi_star) == pytest.approx(
        area * xi_bar
    )
    assert shannon_radial_curvature(j_pi, area, xi_star) == pytest.approx(xi_bar)
    assert source_binding_residual(
        j_pi, area, xi_star, j_vartheta, r_s
    ) == pytest.approx(0.0, abs=2.0e-14)
    assert source_binding_defect(
        j_pi, area, xi_star, j_vartheta, r_s
    ) == pytest.approx(0.0, abs=2.0e-14)


def test_field_form_and_product_form_defects_are_identical():
    j_pi = 0.41
    area = 2.8
    xi_star = 0.03
    j_vartheta = 0.52
    r_s = 1.4
    defect_field = source_binding_defect(
        j_pi, area, xi_star, j_vartheta, r_s
    )
    defect_product = source_binding_defect_product_form(
        j_pi, area, xi_star, j_vartheta, r_s
    )
    assert defect_field == pytest.approx(defect_product)
    assert 0.0 <= defect_field <= 1.0


def test_stationary_reference_with_nonzero_noether_support_has_unit_defect():
    p = (0.4, 0.6)
    pi = (0.4, 0.6)
    j_pi = shannon_relative_information_nats(p, pi)
    assert j_pi == pytest.approx(0.0)
    assert source_binding_defect(
        j_pi,
        3.0,
        0.0,
        0.8,
        1.2,
    ) == pytest.approx(1.0)
    with pytest.raises(NoetherShannonRadialBindingError):
        source_binding_ratio(j_pi, 3.0, 0.0, 0.8, 1.2)


def test_local_fisher_hessian_limit_matches_quadratic_kl_coefficient():
    eps = 1.0e-3
    pi = (0.5, 0.5)
    p = (0.5 + eps, 0.5 - eps)
    s_f_sq = fisher_radial_norm_sq(p, pi)
    j_pi = shannon_relative_information_nats(p, pi)
    assert j_pi == pytest.approx(0.5 * s_f_sq, rel=3.0e-6)

    area_star = 4.0
    assert local_fisher_quadratic_curvature(
        s_f_sq, area_star
    ) == pytest.approx(s_f_sq / (2.0 * area_star))


def test_local_fisher_source_residual_zero_on_quadratic_binding_surface():
    s_f_sq = 0.08
    area_star = 4.0
    r_s = 1.5
    j_vartheta = r_s * s_f_sq / area_star
    assert local_fisher_residual(
        s_f_sq, area_star, j_vartheta, r_s
    ) == pytest.approx(0.0, abs=2.0e-14)


@pytest.mark.parametrize(
    "p,pi",
    [
        ((0.2, 0.2), (0.5, 0.5)),
        ((0.5, 0.5), (1.0, 0.0)),
        ((0.5, -0.5, 1.0), (0.3, 0.3, 0.4)),
    ],
)
def test_invalid_probability_states_fail_closed(p, pi):
    with pytest.raises(NoetherShannonRadialBindingError):
        shannon_relative_information_nats(p, pi)


def test_negative_baseline_adjusted_information_fails_closed():
    with pytest.raises(NoetherShannonRadialBindingError):
        baseline_adjusted_information(0.1, 2.0, 0.2)


@pytest.mark.parametrize("bad", [0.0, -1.0, math.inf, math.nan])
def test_positive_noether_and_area_inputs_fail_closed(bad):
    with pytest.raises(NoetherShannonRadialBindingError):
        noether_radial_amplitude_sq(bad, 1.0)
    with pytest.raises(NoetherShannonRadialBindingError):
        noether_radial_amplitude_sq(1.0, bad)
    with pytest.raises(NoetherShannonRadialBindingError):
        shannon_radial_curvature(0.2, bad, 0.0)
