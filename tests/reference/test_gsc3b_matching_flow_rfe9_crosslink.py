from __future__ import annotations

import pytest


def sub(a, b):
    return [[a[i][j] - b[i][j] for j in range(3)] for i in range(3)]


def scale(a, factor):
    return [[factor * a[i][j] for j in range(3)] for i in range(3)]


def lie_x0_h(hdot_x0, sym_shift_grad_x0):
    return sub(hdot_x0, sym_shift_grad_x0)


def rfe9_extrinsic(hdot_x0, sym_shift_grad_x0, lapse):
    if lapse <= 0.0:
        raise ValueError("lapse must be positive")
    return scale(sub(sym_shift_grad_x0, hdot_x0), 1.0 / (2.0 * lapse))


def max_abs(a, b):
    return max(abs(a[i][j] - b[i][j]) for i in range(3) for j in range(3))


def test_rfe9_is_minus_lie_x0_h_over_two_lapse_for_nonzero_shift():
    hdot = [
        [0.8, 0.1, -0.2],
        [0.1, -0.4, 0.05],
        [-0.2, 0.05, 0.3],
    ]
    sym_shift = [
        [0.2, -0.3, 0.1],
        [-0.3, 0.6, 0.25],
        [0.1, 0.25, -0.1],
    ]
    lapse = 1.7
    k = rfe9_extrinsic(hdot, sym_shift, lapse)
    via_matching_flow = scale(lie_x0_h(hdot, sym_shift), -1.0 / (2.0 * lapse))
    assert max_abs(k, via_matching_flow) == pytest.approx(0.0, abs=1e-15)


def test_coordinate_time_representation_carries_exact_factor_c():
    c = 299792458.0
    hdot_x0 = [
        [0.3, 0.02, 0.0],
        [0.02, -0.1, 0.04],
        [0.0, 0.04, 0.2],
    ]
    sym_shift_x0 = [
        [0.05, -0.01, 0.03],
        [-0.01, 0.07, 0.0],
        [0.03, 0.0, -0.02],
    ]
    lapse = 0.9
    lie_x0 = lie_x0_h(hdot_x0, sym_shift_x0)
    lie_xt = scale(lie_x0, c)
    k_x0 = scale(lie_x0, -1.0 / (2.0 * lapse))
    k_t = scale(lie_xt, -1.0 / (2.0 * lapse * c))
    assert max_abs(k_x0, k_t) == pytest.approx(0.0, abs=1e-15)


def test_beta_t_equals_c_times_dimensionless_rfe8_shift():
    c = 299792458.0
    b_x0 = (0.1, -0.25, 0.04)
    beta_t = tuple(c * value for value in b_x0)
    assert tuple(value / c for value in beta_t) == pytest.approx(b_x0)


def test_static_killing_shift_control_is_preserved():
    zero = [[0.0, 0.0, 0.0] for _ in range(3)]
    assert rfe9_extrinsic(zero, zero, 2.0) == zero
    assert lie_x0_h(zero, zero) == zero


def test_expanding_metric_zero_shift_preserves_rfe9_sign():
    hdot = [[0.4 if i == j else 0.0 for j in range(3)] for i in range(3)]
    zero = [[0.0, 0.0, 0.0] for _ in range(3)]
    k = rfe9_extrinsic(hdot, zero, 1.0)
    for i in range(3):
        assert k[i][i] == pytest.approx(-0.2)
    assert max_abs(k, scale(lie_x0_h(hdot, zero), -0.5)) == pytest.approx(0.0)


def test_nonpositive_lapse_remains_fail_closed():
    zero = [[0.0, 0.0, 0.0] for _ in range(3)]
    with pytest.raises(ValueError, match="positive"):
        rfe9_extrinsic(zero, zero, 0.0)
