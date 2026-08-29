import math

import pytest

from src.rfc.fourcurrent_dust_tensor_closure import (
    FourCurrentDustClosureError,
    current_normalization_rescale,
    dust_rank_one_residual,
    dust_trace_residual,
    fourcurrent_dust_state,
    minkowski_norm_squared,
    tensor_frobenius_defect,
)


def test_proper_charge_and_four_velocity_normalization():
    state = fourcurrent_dust_state((5.0, 3.0, 0.0, 0.0), 7.0)
    assert math.isclose(state.proper_charge_density, 4.0, rel_tol=0.0, abs_tol=1e-15)
    u = state.four_velocity_contravariant
    norm = -u[0] * u[0] + sum(x * x for x in u[1:])
    assert math.isclose(norm, -1.0, rel_tol=0.0, abs_tol=1e-15)
    assert math.isclose(state.gamma, 1.25, rel_tol=0.0, abs_tol=1e-15)
    assert state.beta == (0.6, 0.0, 0.0)


def test_rest_energy_density_is_energy_per_charge_times_proper_charge_density():
    state = fourcurrent_dust_state((10.0, 6.0, 0.0, 0.0), 2.5)
    assert math.isclose(
        state.rest_energy_density,
        state.energy_per_charge * state.proper_charge_density,
        rel_tol=1e-15,
    )


def test_rf_e11_projection_signs_follow_from_current_tensor():
    state = fourcurrent_dust_state((8.0, 2.0, -1.0, 3.0), 4.0)
    assert math.isclose(state.T_cov[0][0], state.rho_n, rel_tol=1e-15)
    for i in range(3):
        assert math.isclose(state.T_cov[0][i + 1], -state.j_i[i], rel_tol=1e-15)
        for j in range(3):
            assert math.isclose(state.T_cov[i + 1][j + 1], state.S_ij[i][j], rel_tol=1e-15)


def test_current_directly_reconstructs_velocity_without_extra_input():
    state = fourcurrent_dust_state((20.0, -6.0, 8.0, 0.0), 1.0)
    assert state.beta == (-0.3, 0.4, 0.0)
    beta2 = sum(x * x for x in state.beta)
    assert math.isclose(state.gamma, 1.0 / math.sqrt(1.0 - beta2), rel_tol=1e-15)


def test_dust_trace_and_rank_one_identities_close():
    state = fourcurrent_dust_state((13.0, 3.0, 4.0, 5.0), 2.0)
    assert abs(dust_trace_residual(state)) < 1e-12
    assert abs(dust_rank_one_residual(state)) < 1e-10


def test_carrier_normalization_rescaling_leaves_full_tensor_invariant():
    J = (12.0, 2.0, 3.0, -4.0)
    epsilon = 5.0
    base = fourcurrent_dust_state(J, epsilon)
    J2, epsilon2 = current_normalization_rescale(J, epsilon, 17.0)
    scaled = fourcurrent_dust_state(J2, epsilon2)

    assert tensor_frobenius_defect(base.T_cov, scaled.T_cov) < 1e-15
    assert math.isclose(base.rest_energy_density, scaled.rest_energy_density, rel_tol=1e-15)
    assert all(math.isclose(a, b, rel_tol=1e-15) for a, b in zip(base.beta, scaled.beta, strict=True))


def test_static_current_reduces_to_rest_dust():
    state = fourcurrent_dust_state((9.0, 0.0, 0.0, 0.0), 3.0)
    assert state.gamma == 1.0
    assert state.rest_energy_density == 27.0
    assert state.rho_n == 27.0
    assert state.j_i == (0.0, 0.0, 0.0)
    assert state.S_trace == 0.0


def test_minkowski_current_norm_is_negative_for_admitted_timelike_current():
    J = (5.0, 1.0, 2.0, 1.0)
    assert minkowski_norm_squared(J) < 0.0
    state = fourcurrent_dust_state(J, 1.0)
    assert math.isclose(
        state.proper_charge_density**2,
        -minkowski_norm_squared(J),
        rel_tol=1e-15,
    )


def test_fail_closed_nonfuture_null_spacelike_and_invalid_inputs():
    bad_calls = (
        lambda: fourcurrent_dust_state((0.0, 0.0, 0.0, 0.0), 1.0),
        lambda: fourcurrent_dust_state((-2.0, 0.0, 0.0, 0.0), 1.0),
        lambda: fourcurrent_dust_state((1.0, 1.0, 0.0, 0.0), 1.0),
        lambda: fourcurrent_dust_state((1.0, 2.0, 0.0, 0.0), 1.0),
        lambda: fourcurrent_dust_state((2.0, 0.0, 0.0, 0.0), -1.0),
        lambda: fourcurrent_dust_state((float("nan"), 0.0, 0.0, 0.0), 1.0),
        lambda: current_normalization_rescale((2.0, 0.0, 0.0, 0.0), 1.0, 0.0),
    )
    for call in bad_calls:
        with pytest.raises(FourCurrentDustClosureError):
            call()
