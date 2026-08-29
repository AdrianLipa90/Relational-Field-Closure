import math

import pytest

from src.rfc.tir_premetric_cell_chart_binding import (
    TIRPremetricCellChartBindingError,
    chart_h_defect,
    chart_length_defect,
    gamma_x_from_cell,
    physical_tir_edge,
    physical_zeta,
    premetric_eta,
    reduced_scale_coupling_defect,
    required_eta,
    required_r_alpha,
    rfl5a_gamma_x,
    rfl5a_mu_lambda,
    sigma_x,
    tetra_edge_hat,
    tetra_fs_shape_coefficient,
    zeta_from_rfs2,
)


def test_tir_tetra_edge_is_exact_normalized_shape_value():
    assert tetra_edge_hat() == pytest.approx(math.sqrt(8.0 / 3.0))


def test_common_cell_chart_binding_cancels_normalized_edge():
    ell_s = 2.7
    h = tetra_edge_hat()
    l_h = physical_tir_edge(ell_s)
    gamma_x = gamma_x_from_cell(l_h, h)

    assert chart_h_defect(h) == pytest.approx(0.0)
    assert chart_length_defect(l_h, ell_s) == pytest.approx(0.0)
    assert gamma_x == pytest.approx(ell_s)
    assert sigma_x(ell_s, gamma_x) == pytest.approx(1.0)


def test_edge_cancellation_is_independent_of_physical_scale():
    for ell_s in (0.2, 1.0, 3.7, 11.0):
        h = tetra_edge_hat()
        gamma_x = gamma_x_from_cell(physical_tir_edge(ell_s), h)
        assert gamma_x == pytest.approx(ell_s)


def test_rfs2_zeta_reduces_to_premetric_eta_on_chart_binding():
    mu_lambda = 2.4
    m_eff = 1.7
    eta = premetric_eta(mu_lambda, m_eff)
    assert zeta_from_rfs2(1.0, mu_lambda, m_eff) == pytest.approx(eta)


def test_rfl5a_roundtrip_matches_physical_spatial_mass_coordinate():
    gamma_t = 1.8
    c = 3.0
    m_i = 0.7
    m_eff = 2.5

    mu_lambda = rfl5a_mu_lambda(gamma_t, c, m_i)
    gamma_x = rfl5a_gamma_x(gamma_t, c, m_eff)
    ell_s = gamma_x

    eta = premetric_eta(mu_lambda, m_eff)
    zeta = physical_zeta(m_i, ell_s)
    assert eta == pytest.approx(zeta)
    assert sigma_x(ell_s, gamma_x) == pytest.approx(1.0)


def test_required_coupling_closes_reduced_premetric_target():
    for mu_lambda, m_eff in ((1.7, 0.8), (2.4, 3.0), (0.9, 1.2)):
        r_alpha = required_r_alpha(mu_lambda, m_eff)
        assert reduced_scale_coupling_defect(
            r_alpha, mu_lambda, m_eff
        ) == pytest.approx(0.0, abs=2.0e-12)


def test_required_eta_is_inverse_map_of_required_coupling():
    for r_alpha in (0.4, 1.0, 2.3):
        eta = required_eta(r_alpha)
        recovered = required_r_alpha(eta, 1.0)
        assert recovered == pytest.approx(r_alpha)


def test_unit_coupling_premetric_target_recovers_tetra_scale_number():
    eta = required_eta(1.0)
    expected = (9.0 * math.sqrt(3.0) * math.pi / 8.0) ** (1.0 / 3.0)
    assert eta == pytest.approx(expected)
    assert eta == pytest.approx(1.82931154035502)
    assert 1.0 / tetra_fs_shape_coefficient() == pytest.approx(
        9.0 * math.sqrt(3.0) * math.pi / 8.0
    )


def test_chart_defects_detect_coordinate_or_physical_width_mismatch():
    ell_s = 1.5
    assert chart_h_defect(1.2 * tetra_edge_hat()) > 0.0
    assert chart_length_defect(0.8 * physical_tir_edge(ell_s), ell_s) > 0.0


@pytest.mark.parametrize("bad", [0.0, -1.0, math.inf, math.nan])
def test_positive_scale_inputs_fail_closed(bad):
    with pytest.raises(TIRPremetricCellChartBindingError):
        gamma_x_from_cell(bad, 1.0)
    with pytest.raises(TIRPremetricCellChartBindingError):
        premetric_eta(1.0, bad)
    with pytest.raises(TIRPremetricCellChartBindingError):
        required_eta(bad)
