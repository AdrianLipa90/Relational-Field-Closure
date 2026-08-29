import math

import pytest

from src.rfc.joint_kl_clock_radial_action_composition import (
    JointKLCompositionError,
    additivity_defect,
    basis_residuals,
    c_delta_fs,
    chain_components,
    coupling_ratio,
    decomposed_potential,
    discrete_kl,
    factorization_defect,
    joint_potential,
    mutual_information,
    phi,
    product_kl,
    rate_kl,
    xi,
    zeta_unity_coupling,
)


def test_rate_kl_matches_rfi1_phi_exact_formula():
    for r_s, r_0 in ((1.2, 2.0), (2.0, 2.0), (3.7, 1.4)):
        assert rate_kl(r_s, r_0) == pytest.approx(phi(r_0 / r_s))


def test_product_radial_clock_kl_is_additive():
    p = (0.65, 0.25, 0.10)
    pi = (0.50, 0.30, 0.20)
    j_r = discrete_kl(p, pi)
    j_c = rate_kl(1.7, 2.3)
    assert product_kl(j_r, j_c) == pytest.approx(j_r + j_c)
    area = 4.2
    assert xi(product_kl(j_r, j_c), area) == pytest.approx(
        xi(j_r, area) + xi(j_c, area)
    )


def test_factorized_discrete_joint_has_zero_mutual_information():
    p_r = (0.7, 0.3)
    p_c = (0.4, 0.6)
    joint = tuple(tuple(a * b for b in p_c) for a in p_r)
    assert mutual_information(joint) == pytest.approx(0.0, abs=2.0e-15)
    assert factorization_defect(mutual_information(joint)) == pytest.approx(0.0)


def test_general_joint_chain_rule_against_product_reference():
    joint = (
        (0.36, 0.14),
        (0.09, 0.41),
    )
    pi_r = (0.6, 0.4)
    pi_c = (0.45, 0.55)
    j_joint, j_r, j_c, j_x = chain_components(joint, pi_r, pi_c)
    assert j_x > 0.0
    assert j_joint == pytest.approx(j_r + j_c + j_x, abs=2.0e-14)
    assert additivity_defect(j_joint, j_r, j_c, j_x) == pytest.approx(
        0.0, abs=2.0e-14
    )
    assert 0.0 < factorization_defect(j_x) < 1.0


def test_common_area_joint_curvature_decomposes_exactly():
    area = 3.8
    j_r, j_c, j_x = 0.2, 0.3, 0.1
    assert xi(j_r + j_c + j_x, area) == pytest.approx(
        xi(j_r, area) + xi(j_c, area) + xi(j_x, area)
    )


def test_joint_and_decomposed_actions_match_for_one_common_coefficient():
    alpha = 2.7
    kappa_e = 0.31
    coords = (0.2, 0.5, 0.07)
    assert joint_potential(alpha, kappa_e, *coords) == pytest.approx(
        decomposed_potential(alpha, alpha, alpha, kappa_e, *coords)
    )
    assert basis_residuals(alpha, alpha, alpha, alpha, kappa_e) == pytest.approx(
        (0.0, 0.0, 0.0)
    )
    assert coupling_ratio(alpha, alpha) == pytest.approx(1.0)


def test_independent_basis_variations_detect_each_coefficient_mismatch():
    residuals = basis_residuals(
        alpha_joint=2.0,
        alpha_i=2.0,
        alpha_clk=3.0,
        alpha_x=4.0,
        kappa_e=0.5,
    )
    assert residuals[0] == pytest.approx(0.0)
    assert residuals[1] != pytest.approx(0.0)
    assert residuals[2] != pytest.approx(0.0)


def test_unity_coupling_reduces_scale_coordinate_to_cubic_shape_constant():
    target = (9.0 * math.sqrt(3.0) * math.pi / 8.0) ** (1.0 / 3.0)
    assert 1.0 / c_delta_fs() == pytest.approx(
        9.0 * math.sqrt(3.0) * math.pi / 8.0
    )
    assert zeta_unity_coupling() == pytest.approx(target)
    assert zeta_unity_coupling() == pytest.approx(1.82931154035502)


@pytest.mark.parametrize("bad", [0.0, -1.0, math.inf, math.nan])
def test_rate_and_area_domains_fail_closed(bad):
    with pytest.raises(JointKLCompositionError):
        rate_kl(bad, 1.0)
    with pytest.raises(JointKLCompositionError):
        xi(0.2, bad)


def test_invalid_probabilities_and_zero_coupling_denominator_fail_closed():
    with pytest.raises(JointKLCompositionError):
        discrete_kl((0.2, 0.2), (0.5, 0.5))
    with pytest.raises(JointKLCompositionError):
        discrete_kl((0.5, 0.5), (1.0, 0.0))
    with pytest.raises(JointKLCompositionError):
        coupling_ratio(1.0, 0.0)
