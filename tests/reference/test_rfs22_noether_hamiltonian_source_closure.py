import math

import pytest

from src.rfc.noether_hamiltonian_source_closure import (
    NoetherHamiltonianSourceClosureError,
    close_source_from_noether_hamiltonian,
    h_over_q_energy_per_charge,
    hamiltonian_profile_density,
    uniform_generator_occupation,
)
from src.rfc.relational_generator_source_density import KAPPA_INFO


def test_extensive_hamiltonian_fixes_total_occupation_for_nonuniform_carrier_energy():
    H = 123.0
    j = (1.0, 3.0, 2.0)
    volumes = (2.0, 1.0, 4.0)
    B = (2.0, 1.0, 4.0)
    omega = (5.0, 7.0, 3.0)
    phase = (0.2, 0.1, 0.4)
    out = close_source_from_noether_hamiltonian(H, j, volumes, B, omega, phase)
    mean = sum(out.noether_profile[i] * out.carrier_energies[i] for i in range(3))
    assert math.isclose(out.mean_carrier_energy, mean, rel_tol=1e-15)
    assert math.isclose(out.inferred_total_occupation, H / mean, rel_tol=1e-15)
    assert math.isclose(sum(out.occupations), out.inferred_total_occupation, rel_tol=1e-15)
    assert math.isclose(out.integrated_source_energy, H, rel_tol=1e-15)


def test_uniform_generator_reduces_to_H_over_B_omega_phase_factor():
    H = 10.0
    B = 2.0
    omega = 5.0
    phi = 0.25
    expected = H / (B * omega * (phi + KAPPA_INFO))
    assert math.isclose(uniform_generator_occupation(H, B, omega, phi), expected, rel_tol=1e-15)


def test_uniform_carrier_energy_source_is_H_over_Q_times_noether_current():
    H = 50.0
    j = (2.0, 1.0, 4.0)
    volumes = (1.0, 3.0, 2.0)
    B = (2.0, 2.0, 2.0)
    omega = (3.0, 3.0, 3.0)
    phase = (0.4, 0.4, 0.4)
    out = close_source_from_noether_hamiltonian(H, j, volumes, B, omega, phase)
    direct = hamiltonian_profile_density(H, j, volumes)
    assert all(math.isclose(a, b, rel_tol=1e-15, abs_tol=1e-15) for a, b in zip(out.source_energy_densities, direct))
    Q = sum(j[i] * volumes[i] for i in range(3))
    assert math.isclose(h_over_q_energy_per_charge(H, Q), H / Q, rel_tol=1e-15)


def test_global_current_scaling_changes_Q_but_not_hamiltonian_profile_source():
    H = 20.0
    j = (1.0, 2.0, 5.0)
    volumes = (2.0, 3.0, 1.0)
    base = hamiltonian_profile_density(H, j, volumes)
    scaled = hamiltonian_profile_density(H, tuple(17.0 * x for x in j), volumes)
    assert all(math.isclose(a, b, rel_tol=1e-15, abs_tol=1e-15) for a, b in zip(base, scaled))


def test_generator_source_integral_is_exactly_H_even_when_local_energies_vary():
    H = 88.0
    j = (1.0, 5.0, 2.0, 3.0)
    volumes = (1.0, 2.0, 3.0, 4.0)
    B = (1.0, 2.0, 3.0, 4.0)
    omega = (4.0, 3.0, 2.0, 1.0)
    phase = (0.6, 0.5, 0.4, 0.3)
    out = close_source_from_noether_hamiltonian(H, j, volumes, B, omega, phase)
    integrated = sum(out.source_energy_densities[i] * volumes[i] for i in range(4))
    assert math.isclose(integrated, H, rel_tol=1e-15)


def test_zero_hamiltonian_closes_to_zero_occupation():
    out = close_source_from_noether_hamiltonian(
        0.0,
        (1.0, 2.0),
        (1.0, 1.0),
        (1.0, 1.0),
        (1.0, 1.0),
        (-KAPPA_INFO, -KAPPA_INFO),
    )
    assert out.inferred_total_occupation == 0.0
    assert out.integrated_source_energy == 0.0


def test_fail_closed_for_nonpositive_mean_energy_with_positive_H_and_invalid_inputs():
    bad_calls = (
        lambda: close_source_from_noether_hamiltonian(1.0, (1.0,), (1.0,), (1.0,), (-1.0,), (1.0,)),
        lambda: close_source_from_noether_hamiltonian(-1.0, (1.0,), (1.0,), (1.0,), (1.0,), (1.0,)),
        lambda: close_source_from_noether_hamiltonian(1.0, (-1.0,), (1.0,), (1.0,), (1.0,), (1.0,)),
        lambda: close_source_from_noether_hamiltonian(1.0, (1.0,), (0.0,), (1.0,), (1.0,), (1.0,)),
        lambda: uniform_generator_occupation(1.0, 1.0, 0.0, -KAPPA_INFO),
        lambda: h_over_q_energy_per_charge(1.0, 0.0),
        lambda: hamiltonian_profile_density(1.0, (0.0,), (1.0,)),
    )
    for call in bad_calls:
        with pytest.raises(NoetherHamiltonianSourceClosureError):
            call()
