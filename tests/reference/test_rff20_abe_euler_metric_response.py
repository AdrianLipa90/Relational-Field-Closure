import pytest

from src.rfc.abe_euler_metric_response import (
    ABEMetricResponseError,
    abe_contracted_response,
    eta_one_projector_stress,
    frozen_connection_branch,
    phase_stress_metric_response_correction,
    projector_metric_derivative,
    sum_connection_metric_responses,
    zero_connection_metric_response,
)


ETA = (
    (-1.0, 0.0, 0.0, 0.0),
    (0.0, 1.0, 0.0, 0.0),
    (0.0, 0.0, 1.0, 0.0),
    (0.0, 0.0, 0.0, 1.0),
)
ZERO4 = tuple(tuple(0.0 for _ in range(4)) for _ in range(4))
ZERO_R3 = zero_connection_metric_response()


def response_with(beta: int, m: int, n: int, value: float):
    data = [[[0.0 for _ in range(4)] for _ in range(4)] for _ in range(4)]
    data[beta][m][n] = value
    data[beta][n][m] = value
    return data


def test_zero_abe_response_recovers_frozen_connection_branch():
    q = (2.0, 0.0, 0.0, 0.0)
    R = abe_contracted_response(ETA, q, ZERO_R3, ZERO_R3, ZERO_R3)
    assert R == ZERO4
    assert frozen_connection_branch(R)


def test_abe_response_decomposes_linearly_by_channel():
    ab = response_with(0, 1, 1, 0.1)
    berry = response_with(0, 1, 1, 0.2)
    euler = response_with(0, 1, 1, 0.3)
    total = sum_connection_metric_responses(ab, berry, euler)
    assert total[0][1][1] == pytest.approx(0.6)


def test_euler_only_metric_response_produces_nonzero_R():
    q = (2.0, 0.0, 0.0, 0.0)
    euler = response_with(0, 1, 1, 0.25)
    R = abe_contracted_response(ETA, q, ZERO_R3, ZERO_R3, euler)
    assert R[1][1] == pytest.approx(-0.5)
    assert not frozen_connection_branch(R)


def test_rf_e4_phase_stress_correction_is_four_A2_R():
    R = [list(row) for row in ZERO4]
    R[2][2] = 0.5
    correction = phase_stress_metric_response_correction(3.0, R)
    assert correction[2][2] == pytest.approx(6.0)


def test_projector_derivative_recovers_f18_when_scale_response_zero():
    q = (1.0, 0.0, 0.0, 0.0)
    R = [list(row) for row in ZERO4]
    R[1][1] = 0.25
    derivative = projector_metric_derivative(q, 2.0, R)
    assert derivative[0][0] == pytest.approx(-0.25)
    assert derivative[1][1] == pytest.approx(-0.125)


def test_projector_derivative_includes_f19_scale_response():
    q = (1.0, 0.0, 0.0, 0.0)
    S = [list(row) for row in ZERO4]
    S[3][3] = 0.2
    derivative = projector_metric_derivative(q, 2.0, ZERO4, scale_log_metric_response=S)
    assert derivative[3][3] == pytest.approx(-0.4)


def test_eta_one_projector_stress_reduces_to_rank_one_at_frozen_response():
    q = (2.0, 0.0, 0.0, 0.0)
    stress = eta_one_projector_stress(8.0, 0.5, q, 2.0, ZERO4)
    assert stress[0][0] == pytest.approx(8.0)
    assert stress[1][1] == pytest.approx(0.0)


def test_eta_one_projector_stress_contains_euler_response_correction():
    q = (2.0, 0.0, 0.0, 0.0)
    R = [list(row) for row in ZERO4]
    R[1][1] = 0.5
    stress = eta_one_projector_stress(8.0, 0.5, q, 2.0, R)
    assert stress[1][1] == pytest.approx(2.0)


def test_eta_one_projector_stress_contains_independent_scale_response():
    q = (2.0, 0.0, 0.0, 0.0)
    S = [list(row) for row in ZERO4]
    S[2][2] = 0.25
    stress = eta_one_projector_stress(8.0, 0.5, q, 2.0, ZERO4, scale_log_metric_response=S)
    assert stress[2][2] == pytest.approx(4.0)


def test_channel_cancellation_is_visible_in_total_response():
    ab = response_with(0, 1, 1, 0.2)
    euler = response_with(0, 1, 1, -0.2)
    q = (1.0, 0.0, 0.0, 0.0)
    R = abe_contracted_response(ETA, q, ab, ZERO_R3, euler)
    assert R == ZERO4


def test_fail_closed_on_nonsymmetric_metric_response():
    bad = [[[0.0 for _ in range(4)] for _ in range(4)] for _ in range(4)]
    bad[0][1][2] = 1.0
    with pytest.raises(ABEMetricResponseError):
        sum_connection_metric_responses(bad, ZERO_R3, ZERO_R3)


def test_fail_closed_on_nonpositive_phase_scale():
    with pytest.raises(ABEMetricResponseError):
        projector_metric_derivative((1.0, 0.0, 0.0, 0.0), 0.0, ZERO4)
