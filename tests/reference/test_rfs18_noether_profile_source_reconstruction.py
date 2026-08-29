import math

import pytest

from src.rfc.noether_profile_source_reconstruction import (
    NoetherProfileSourceError,
    current_rescaling_source_defect,
    normalized_noether_profile,
    reconstruct_generator_source_from_noether_profile,
    reconstruct_occupation_from_noether_profile,
)
from src.rfc.relational_generator_source_density import KAPPA_INFO


def test_noether_profile_is_normalized_on_nonuniform_cells():
    j = (2.0, 3.0, 5.0)
    volumes = (1.0, 2.0, 4.0)
    p = normalized_noether_profile(j, volumes)
    expected_charge = (2.0, 6.0, 20.0)
    total = sum(expected_charge)
    assert math.isclose(sum(p), 1.0, rel_tol=0.0, abs_tol=1e-15)
    assert all(math.isclose(p[i], expected_charge[i] / total, rel_tol=1e-15) for i in range(3))


def test_total_occupation_and_profile_reconstruct_local_density_without_q0():
    j = (1.0, 4.0, 2.0)
    volumes = (2.0, 1.0, 3.0)
    N_total = 21.0
    occupations, densities, Q = reconstruct_occupation_from_noether_profile(j, volumes, N_total)
    assert math.isclose(sum(occupations), N_total, rel_tol=0.0, abs_tol=1e-14)
    for i in range(3):
        assert math.isclose(densities[i], N_total * j[i] / Q, rel_tol=1e-15)
        assert math.isclose(occupations[i], densities[i] * volumes[i], rel_tol=1e-15)


def test_global_current_rescaling_leaves_occupation_and_source_density_invariant():
    j = (1.0, 2.0, 7.0, 3.0)
    volumes = (1.5, 0.5, 2.0, 3.0)
    B = (2.0, 2.5, 1.5, 3.0)
    omega = (3.0, 4.0, 5.0, 6.0)
    phase = (0.2, 0.3, 0.4, 0.5)
    N_total = 17.0

    base = reconstruct_generator_source_from_noether_profile(j, volumes, N_total, B, omega, phase)
    scaled = reconstruct_generator_source_from_noether_profile(tuple(13.0 * x for x in j), volumes, N_total, B, omega, phase)

    assert all(math.isclose(a, b, rel_tol=1e-15, abs_tol=1e-15) for a, b in zip(base.profile, scaled.profile))
    assert all(math.isclose(a, b, rel_tol=1e-15, abs_tol=1e-15) for a, b in zip(base.occupations, scaled.occupations))
    assert all(math.isclose(a, b, rel_tol=1e-15, abs_tol=1e-15) for a, b in zip(base.source_energy_densities, scaled.source_energy_densities))
    assert math.isclose(scaled.total_noether_charge, 13.0 * base.total_noether_charge, rel_tol=1e-15)
    assert current_rescaling_source_defect(j, volumes, N_total, B, omega, phase, 13.0) < 1e-15


def test_reconstructed_source_matches_direct_orbital_generator_cellwise():
    j = (2.0, 5.0, 1.0)
    volumes = (4.0, 2.0, 1.0)
    N_total = 12.0
    B = (1.2, 2.3, 3.4)
    omega = (7.0, 8.0, 9.0)
    phase = (0.1, 0.2, 0.3)

    out = reconstruct_generator_source_from_noether_profile(j, volumes, N_total, B, omega, phase)
    for i in range(3):
        direct = (out.occupations[i] / volumes[i]) * B[i] * omega[i] * (phase[i] + KAPPA_INFO)
        assert math.isclose(out.source_energy_densities[i], direct, rel_tol=1e-15)
    direct_integrated = sum(out.occupations[i] * out.carrier_energies[i] for i in range(3))
    assert math.isclose(out.integrated_source_energy, direct_integrated, rel_tol=1e-15)


def test_uniform_carrier_energy_gives_total_energy_N_times_epsilon():
    j = (1.0, 4.0, 2.0)
    volumes = (1.0, 2.0, 3.0)
    N_total = 10.0
    B = (2.0, 2.0, 2.0)
    omega = (5.0, 5.0, 5.0)
    phase = (0.25, 0.25, 0.25)

    out = reconstruct_generator_source_from_noether_profile(j, volumes, N_total, B, omega, phase)
    epsilon = 2.0 * 5.0 * (0.25 + KAPPA_INFO)
    assert math.isclose(out.integrated_source_energy, N_total * epsilon, rel_tol=1e-15)


def test_zero_total_occupation_has_zero_source_but_retains_current_profile():
    j = (1.0, 2.0)
    volumes = (1.0, 3.0)
    out = reconstruct_generator_source_from_noether_profile(j, volumes, 0.0, (1.0, 1.0), (2.0, 2.0), (0.0, 0.0))
    assert out.occupations == (0.0, 0.0)
    assert out.occupation_densities == (0.0, 0.0)
    assert out.source_energy_densities == (0.0, 0.0)
    assert out.integrated_source_energy == 0.0


def test_fail_closed_on_invalid_current_measure_or_shape():
    bad_calls = (
        lambda: normalized_noether_profile((0.0, 0.0), (1.0, 1.0)),
        lambda: normalized_noether_profile((-1.0, 2.0), (1.0, 1.0)),
        lambda: normalized_noether_profile((1.0,), (0.0,)),
        lambda: reconstruct_occupation_from_noether_profile((1.0,), (1.0,), -1.0),
        lambda: reconstruct_generator_source_from_noether_profile((1.0, 2.0), (1.0,), 1.0, (1.0, 1.0), (1.0, 1.0), (1.0, 1.0)),
        lambda: current_rescaling_source_defect((1.0,), (1.0,), 1.0, (1.0,), (1.0,), (1.0,), 0.0),
    )
    for call in bad_calls:
        with pytest.raises(NoetherProfileSourceError):
            call()
