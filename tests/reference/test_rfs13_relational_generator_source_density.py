import math

import pytest

from src.rfc.relational_generator_source_density import (
    C_LIGHT,
    KAPPA_INFO,
    RelationalGeneratorSourceError,
    einstein_kappa_from_newton_G,
    half_rate_action_normalization,
    half_rate_normalization_defect,
    newton_lapse_source_from_energy_density,
    relational_generator_source,
)


def test_kappa_is_canonical_information_offset():
    assert math.isclose(KAPPA_INFO, math.log(2.0) / (24.0 * math.pi), rel_tol=0.0, abs_tol=1e-18)


def test_exact_user_generator_factorization_into_energy_density():
    B = 3.25e-34
    omega = 7.5e9
    N = 42.0
    A = 2.0e-4
    R = 0.35
    phi = 0.61

    out = relational_generator_source(B, omega, N, A, R, phi)
    direct = (B * omega * N / (A * R)) * (phi + KAPPA_INFO)

    assert math.isclose(out.volume_m3, A * R, rel_tol=0.0, abs_tol=1e-20)
    assert math.isclose(out.occupation_density_m3, N / (A * R), rel_tol=1e-15)
    assert math.isclose(out.carrier_energy_joule, B * omega * (phi + KAPPA_INFO), rel_tol=1e-15)
    assert math.isclose(out.energy_density_j_m3, direct, rel_tol=1e-15)
    assert math.isclose(out.mass_density_kg_m3, direct / C_LIGHT**2, rel_tol=1e-15)
    assert out.positive_source_admitted


def test_occupation_and_relational_volume_scaling_are_exact():
    base = relational_generator_source(2.0, 3.0, 5.0, 7.0, 11.0, 0.25)
    twice_N = relational_generator_source(2.0, 3.0, 10.0, 7.0, 11.0, 0.25)
    twice_A = relational_generator_source(2.0, 3.0, 5.0, 14.0, 11.0, 0.25)
    twice_R = relational_generator_source(2.0, 3.0, 5.0, 7.0, 22.0, 0.25)

    assert math.isclose(twice_N.energy_density_j_m3, 2.0 * base.energy_density_j_m3, rel_tol=1e-15)
    assert math.isclose(twice_A.energy_density_j_m3, 0.5 * base.energy_density_j_m3, rel_tol=1e-15)
    assert math.isclose(twice_R.energy_density_j_m3, 0.5 * base.energy_density_j_m3, rel_tol=1e-15)


def test_signed_formula_is_preserved_and_positive_source_is_typed_separately():
    out = relational_generator_source(1.0, -2.0, 3.0, 4.0, 5.0, 0.7)
    assert out.energy_density_j_m3 < 0.0
    assert not out.positive_source_admitted


def test_newton_and_einstein_source_normalizations_are_identical():
    G = 6.67430e-11
    rho_E = 1.2345e7
    source = newton_lapse_source_from_energy_density(rho_E, G)
    kappa_E = einstein_kappa_from_newton_G(G)

    assert math.isclose(source, 0.5 * kappa_E * rho_E, rel_tol=1e-15)

    rho_m = rho_E / C_LIGHT**2
    lhs = C_LIGHT**2 * source
    rhs = 4.0 * math.pi * G * rho_m
    assert math.isclose(lhs, rhs, rel_tol=1e-15)


def test_half_rate_rfc_normalization_fixes_B_times_phase_factor():
    q_A = 1.054571817e-34
    phi = 0.3
    B = half_rate_action_normalization(phi, action_quantum_joule_second=q_A)

    assert math.isclose(B * (phi + KAPPA_INFO), 0.5 * q_A, rel_tol=1e-15)
    assert half_rate_normalization_defect(
        B,
        phi,
        action_quantum_joule_second=q_A,
    ) < 1e-15

    omega = 8.0e12
    source = relational_generator_source(B, omega, 1.0, 1.0, 1.0, phi)
    assert math.isclose(source.carrier_energy_joule, 0.5 * q_A * omega, rel_tol=1e-15)


def test_half_rate_normalization_rejects_zero_phase_factor():
    with pytest.raises(RelationalGeneratorSourceError):
        half_rate_action_normalization(
            -KAPPA_INFO,
            action_quantum_joule_second=1.0,
        )


def test_source_binding_fails_closed_on_invalid_inputs():
    bad_calls = (
        lambda: relational_generator_source(float("nan"), 1.0, 1.0, 1.0, 1.0, 0.0),
        lambda: relational_generator_source(1.0, float("inf"), 1.0, 1.0, 1.0, 0.0),
        lambda: relational_generator_source(1.0, 1.0, -1.0, 1.0, 1.0, 0.0),
        lambda: relational_generator_source(1.0, 1.0, 1.0, 0.0, 1.0, 0.0),
        lambda: relational_generator_source(1.0, 1.0, 1.0, 1.0, -1.0, 0.0),
        lambda: einstein_kappa_from_newton_G(0.0),
    )
    for call in bad_calls:
        with pytest.raises(RelationalGeneratorSourceError):
            call()
