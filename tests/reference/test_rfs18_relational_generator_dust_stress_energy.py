import math

import pytest

from src.rfc.relational_generator_dust_stress_energy import (
    C_LIGHT,
    RelationalGeneratorDustError,
    adm_dust_source_terms,
    dust_adm_state,
    dust_momentum_stress_residual,
    dust_trace_residual,
    generator_dust_adm_state,
    reconstruct_beta_from_adm,
    reconstruct_rest_density,
)
from src.rfc.relational_generator_source_density import KAPPA_INFO


def test_rest_source_reduces_to_pure_energy_density():
    rho0 = 12.5
    state = dust_adm_state(rho0, (0.0, 0.0, 0.0))
    assert state.gamma == 1.0
    assert state.rho_n == rho0
    assert state.j_i == (0.0, 0.0, 0.0)
    assert state.S_trace == 0.0
    assert state.T_cov[0][0] == rho0
    assert all(state.T_cov[0][i] == 0.0 for i in range(1, 4))


def test_rf_e11_sign_convention_and_adm_projections_are_exact():
    rho0 = 4.0
    v = (0.3 * C_LIGHT, -0.2 * C_LIGHT, 0.1 * C_LIGHT)
    state = dust_adm_state(rho0, v)

    assert math.isclose(state.T_cov[0][0], state.rho_n, rel_tol=1e-15)
    for i in range(3):
        assert math.isclose(state.T_cov[0][i + 1], -state.j_i[i], rel_tol=1e-15)
        for j in range(3):
            assert math.isclose(state.T_cov[i + 1][j + 1], state.S_ij[i][j], rel_tol=1e-15)


def test_dust_trace_recovers_rest_energy_density():
    state = dust_adm_state(9.0, (0.45 * C_LIGHT, 0.0, -0.25 * C_LIGHT))
    assert abs(dust_trace_residual(state)) < 1e-13
    assert math.isclose(reconstruct_rest_density(state), state.rest_energy_density, rel_tol=1e-14)


def test_rank_one_dust_momentum_stress_identity():
    state = dust_adm_state(7.0, (0.2 * C_LIGHT, 0.15 * C_LIGHT, 0.1 * C_LIGHT))
    assert abs(dust_momentum_stress_residual(state)) < 1e-12


def test_velocity_is_reconstructed_from_adm_momentum_over_energy_density():
    state = dust_adm_state(5.0, (-0.4 * C_LIGHT, 0.1 * C_LIGHT, 0.2 * C_LIGHT))
    beta = reconstruct_beta_from_adm(state)
    assert all(math.isclose(a, b, rel_tol=1e-15) for a, b in zip(beta, state.beta, strict=True))


def test_generator_lifts_to_relativistic_dust_without_changing_rest_density():
    B = 3.0e-34
    omega = 4.0e10
    N = 8.0
    A = 2.0e-3
    R = 0.75
    phi = 0.6
    expected_rho0 = (B * omega * N / (A * R)) * (phi + KAPPA_INFO)

    state = generator_dust_adm_state(
        B,
        omega,
        N,
        A,
        R,
        phi,
        (0.25 * C_LIGHT, 0.0, 0.0),
    )
    assert math.isclose(state.rest_energy_density, expected_rho0, rel_tol=1e-15)
    assert state.rho_n > state.rest_energy_density
    assert state.j_i[0] > 0.0


def test_rf_e12_and_rf_e13_source_terms_are_exact():
    state = dust_adm_state(6.0, (0.3 * C_LIGHT, 0.0, 0.0))
    kappa_E = 2.5e-43
    terms = adm_dust_source_terms(state, kappa_E)

    assert math.isclose(terms.hamiltonian_rhs, 2.0 * kappa_E * state.rho_n, rel_tol=1e-15)
    assert all(
        math.isclose(a, kappa_E * b, rel_tol=1e-15)
        for a, b in zip(terms.momentum_rhs, state.j_i, strict=True)
    )
    for i in range(3):
        for j in range(3):
            expected = kappa_E * (
                0.5 * (state.S_trace - state.rho_n) * (1.0 if i == j else 0.0)
                - state.S_ij[i][j]
            )
            assert math.isclose(terms.evolution_matter_term[i][j], expected, rel_tol=1e-15, abs_tol=1e-60)


def test_ultrarelativistic_approach_increases_eulerian_energy_without_crossing_c():
    slow = dust_adm_state(1.0, (0.1 * C_LIGHT, 0.0, 0.0))
    fast = dust_adm_state(1.0, (0.99 * C_LIGHT, 0.0, 0.0))
    assert fast.gamma > slow.gamma
    assert fast.rho_n > slow.rho_n


def test_fail_closed_invalid_source_or_velocity():
    bad_calls = (
        lambda: dust_adm_state(-1.0, (0.0, 0.0, 0.0)),
        lambda: dust_adm_state(1.0, (0.0, 0.0)),
        lambda: dust_adm_state(1.0, (C_LIGHT, 0.0, 0.0)),
        lambda: dust_adm_state(1.0, (float("nan"), 0.0, 0.0)),
        lambda: adm_dust_source_terms(dust_adm_state(1.0, (0.0, 0.0, 0.0)), 0.0),
        lambda: generator_dust_adm_state(1.0, -1.0, 1.0, 1.0, 1.0, 0.0, (0.0, 0.0, 0.0)),
    )
    for call in bad_calls:
        with pytest.raises((RelationalGeneratorDustError, ValueError)):
            call()
