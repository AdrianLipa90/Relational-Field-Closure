import pytest

from src.rfc.total_einstein_source_assembly import (
    EinsteinSourceAssemblyError,
    assemble_dynamic_lambda_source,
    assemble_fixed_reference_source,
    dynamic_bianchi_residual_from_fixed,
    dynamic_lambda_u_sector,
    fixed_dynamic_residual_pair,
    fixed_reference_u_sector,
    lambda0_from_reference,
    max_abs_matrix_difference,
    projector_interaction_stress_from_f20,
    source_repartition_difference,
)


MINK = (
    (-1.0, 0.0, 0.0, 0.0),
    (0.0, 1.0, 0.0, 0.0),
    (0.0, 0.0, 1.0, 0.0),
    (0.0, 0.0, 0.0, 1.0),
)
ZERO4 = tuple(tuple(0.0 for _ in range(4)) for _ in range(4))


def diag(a, b, c, d):
    return (
        (a, 0.0, 0.0, 0.0),
        (0.0, b, 0.0, 0.0),
        (0.0, 0.0, c, 0.0),
        (0.0, 0.0, 0.0, d),
    )


def assert_matrix_close(actual, expected, *, abs_tol=1e-12):
    assert max_abs_matrix_difference(actual, expected) <= abs_tol


def test_dynamic_minus_fixed_source_is_exactly_u_hat_metric():
    rest = diag(3.0, 1.0, 2.0, 4.0)
    D = diag(0.2, 0.3, 0.4, 0.5)
    fixed = assemble_fixed_reference_source(rest, MINK, eta=0.37, u_hat=7.0, projector_stress=D)
    dynamic = assemble_dynamic_lambda_source(rest, MINK, eta=0.37, u_hat=7.0, projector_stress=D)
    difference = source_repartition_difference(dynamic, fixed)
    expected = tuple(tuple(7.0 * MINK[i][j] for j in range(4)) for i in range(4))
    assert_matrix_close(difference, expected)


def test_einstein_residual_is_identical_under_lambda_repartition():
    G = diag(1.3, -0.4, 0.7, 2.1)
    rest = diag(4.0, 1.5, -0.2, 0.6)
    D = diag(0.1, -0.3, 0.8, 0.2)
    fixed_residual, dynamic_residual = fixed_dynamic_residual_pair(
        einstein_tensor=G,
        metric=MINK,
        lambda_star=0.4,
        kappa_e=2.5,
        rest_source=rest,
        eta=0.62,
        u_hat=1.7,
        projector_stress=D,
    )
    assert max_abs_matrix_difference(fixed_residual, dynamic_residual) == pytest.approx(0.0)


def test_lambda0_shift_is_kappa_times_u_hat():
    assert lambda0_from_reference(1.2, 3.0, 0.4) == pytest.approx(2.4)


def test_eta_zero_recovers_l2_repartition_endpoint():
    fixed = fixed_reference_u_sector(MINK, eta=0.0, u_hat=5.0, projector_stress=ZERO4)
    dynamic = dynamic_lambda_u_sector(MINK, eta=0.0, u_hat=5.0, projector_stress=ZERO4)
    expected_fixed = tuple(tuple(-5.0 * MINK[i][j] for j in range(4)) for i in range(4))
    assert_matrix_close(fixed, expected_fixed)
    assert_matrix_close(dynamic, ZERO4)


def test_eta_one_fixed_ledger_keeps_only_projector_stress():
    D = diag(1.0, 2.0, 3.0, 4.0)
    fixed = fixed_reference_u_sector(MINK, eta=1.0, u_hat=5.0, projector_stress=D)
    dynamic = dynamic_lambda_u_sector(MINK, eta=1.0, u_hat=5.0, projector_stress=D)
    assert_matrix_close(fixed, D)
    expected_difference = tuple(tuple(5.0 * MINK[i][j] for j in range(4)) for i in range(4))
    assert_matrix_close(source_repartition_difference(dynamic, fixed), expected_difference)


def test_frozen_f20_response_eta_one_half_slope_gives_rank_one_u_vv():
    stress = projector_interaction_stress_from_f20(
        eta=1.0,
        u_hat=8.0,
        f_prime_at_one=0.5,
        phase_covector=(2.0, 0.0, 0.0, 0.0),
        phase_scale=2.0,
        contracted_abe_response=ZERO4,
    )
    assert stress[0][0] == pytest.approx(8.0)
    assert stress[1][1] == pytest.approx(0.0)


def test_nonzero_abe_response_is_retained_in_both_ledgers():
    R = [list(row) for row in ZERO4]
    R[1][1] = 0.5
    stress = projector_interaction_stress_from_f20(
        eta=1.0,
        u_hat=8.0,
        f_prime_at_one=0.5,
        phase_covector=(2.0, 0.0, 0.0, 0.0),
        phase_scale=2.0,
        contracted_abe_response=R,
    )
    assert stress[1][1] == pytest.approx(2.0)
    fixed = fixed_reference_u_sector(MINK, eta=1.0, u_hat=8.0, projector_stress=stress)
    dynamic = dynamic_lambda_u_sector(MINK, eta=1.0, u_hat=8.0, projector_stress=stress)
    assert fixed[1][1] == pytest.approx(2.0)
    assert dynamic[1][1] == pytest.approx(10.0)


def test_nonzero_phase_scale_response_is_retained():
    S = [list(row) for row in ZERO4]
    S[2][2] = 0.25
    stress = projector_interaction_stress_from_f20(
        eta=1.0,
        u_hat=8.0,
        f_prime_at_one=0.5,
        phase_covector=(2.0, 0.0, 0.0, 0.0),
        phase_scale=2.0,
        contracted_abe_response=ZERO4,
        scale_log_metric_response=S,
    )
    assert stress[2][2] == pytest.approx(4.0)


def test_dynamic_bianchi_residual_equals_kappa_times_fixed_divergence():
    fixed_div = (0.1, -0.2, 0.3, -0.4)
    grad_u = (2.0, 3.0, -5.0, 7.0)
    residual = dynamic_bianchi_residual_from_fixed(4.0, fixed_div, grad_u)
    assert residual == pytest.approx(tuple(4.0 * value for value in fixed_div))


def test_conserved_fixed_action_implies_dynamic_lambda_exchange_closure():
    residual = dynamic_bianchi_residual_from_fixed(4.0, (0.0, 0.0, 0.0, 0.0), (2.0, 3.0, -5.0, 7.0))
    assert residual == pytest.approx((0.0, 0.0, 0.0, 0.0))


def test_constant_u_hat_reduces_dynamic_bianchi_to_fixed_conservation():
    fixed_div = (0.2, 0.0, 0.0, -0.1)
    residual = dynamic_bianchi_residual_from_fixed(3.0, fixed_div, (0.0, 0.0, 0.0, 0.0))
    assert residual == pytest.approx((0.6, 0.0, 0.0, -0.3))


def test_fail_closed_on_eta_outside_partition_interval():
    with pytest.raises(EinsteinSourceAssemblyError):
        fixed_reference_u_sector(MINK, eta=1.1, u_hat=1.0, projector_stress=ZERO4)


def test_fail_closed_on_nonpositive_kappa_e():
    with pytest.raises(EinsteinSourceAssemblyError):
        lambda0_from_reference(0.0, 0.0, 1.0)
