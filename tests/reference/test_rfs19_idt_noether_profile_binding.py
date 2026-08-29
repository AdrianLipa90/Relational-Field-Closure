import math

import pytest

from src.rfc.idt_noether_profile_binding import (
    IDTNoetherProfileBindingError,
    compare_idt_noether_profiles,
    reconstruct_source_from_idt_profile,
    source_profile_mismatch_bound,
)
from src.rfc.noether_profile_source_reconstruction import reconstruct_generator_source_from_noether_profile


def test_zero_defect_when_idt_matches_noether_profile():
    j = (1.0, 3.0, 2.0)
    volumes = (2.0, 1.0, 4.0)
    charges = tuple(j[i] * volumes[i] for i in range(3))
    total = sum(charges)
    p = tuple(x / total for x in charges)

    out = compare_idt_noether_profiles(p, j, volumes)
    assert out.zero_defect
    assert out.hellinger_squared < 1e-15
    assert out.l1_distance < 1e-15
    assert out.max_abs_distance < 1e-15


def test_profile_defect_detects_role_mismatch():
    p = (0.1, 0.2, 0.7)
    j = (0.7, 0.2, 0.1)
    volumes = (1.0, 1.0, 1.0)
    out = compare_idt_noether_profiles(p, j, volumes)
    assert not out.zero_defect
    assert out.hellinger_squared > 0.0
    assert out.l1_distance > 0.0


def test_global_noether_current_scaling_does_not_change_profile_defect():
    p = (0.2, 0.3, 0.5)
    j = (2.0, 3.0, 5.0)
    volumes = (1.0, 1.0, 1.0)
    a = compare_idt_noether_profiles(p, j, volumes)
    b = compare_idt_noether_profiles(p, tuple(19.0 * x for x in j), volumes)
    assert math.isclose(a.hellinger_squared, b.hellinger_squared, rel_tol=0.0, abs_tol=1e-15)
    assert math.isclose(a.l1_distance, b.l1_distance, rel_tol=0.0, abs_tol=1e-15)
    assert a.zero_defect == b.zero_defect


def test_zero_defect_idt_source_matches_noether_reconstruction():
    j = (1.0, 4.0, 2.0)
    volumes = (2.0, 1.0, 3.0)
    charges = tuple(j[i] * volumes[i] for i in range(3))
    q = sum(charges)
    p = tuple(x / q for x in charges)
    N_total = 13.0
    B = (2.0, 3.0, 4.0)
    omega = (5.0, 6.0, 7.0)
    phase = (0.1, 0.2, 0.3)

    idt = reconstruct_source_from_idt_profile(p, volumes, N_total, B, omega, phase)
    noether = reconstruct_generator_source_from_noether_profile(j, volumes, N_total, B, omega, phase)

    assert all(math.isclose(a, b, rel_tol=1e-15, abs_tol=1e-15) for a, b in zip(idt.occupations, noether.occupations))
    assert all(math.isclose(a, b, rel_tol=1e-15, abs_tol=1e-15) for a, b in zip(idt.source_energy_densities, noether.source_energy_densities))
    assert math.isclose(idt.integrated_source_energy, noether.integrated_source_energy, rel_tol=1e-15)


def test_l1_source_mismatch_bound_is_respected():
    p = (0.1, 0.4, 0.5)
    j = (0.2, 0.3, 0.5)
    volumes = (1.0, 1.0, 1.0)
    N_total = 7.0
    E = (2.0, -1.0, 3.0)
    Emax = max(abs(x) for x in E)

    q = tuple(j[i] / sum(j) for i in range(3))
    actual = abs(N_total * sum(E[i] * (p[i] - q[i]) for i in range(3)))
    bound = source_profile_mismatch_bound(p, j, volumes, N_total, Emax)
    assert actual <= bound + 1e-15


def test_zero_support_entries_are_handled_without_kl_singularity():
    p = (0.0, 0.25, 0.75)
    j = (0.0, 1.0, 3.0)
    volumes = (1.0, 1.0, 1.0)
    out = compare_idt_noether_profiles(p, j, volumes)
    assert out.zero_defect
    assert out.hellinger_squared < 1e-15


def test_fail_closed_on_bad_profiles_or_shapes():
    bad_calls = (
        lambda: compare_idt_noether_profiles((0.2, 0.2), (1.0, 1.0), (1.0, 1.0)),
        lambda: compare_idt_noether_profiles((-0.1, 1.1), (1.0, 1.0), (1.0, 1.0)),
        lambda: compare_idt_noether_profiles((1.0,), (1.0, 2.0), (1.0, 1.0)),
        lambda: compare_idt_noether_profiles((1.0,), (0.0,), (1.0,)),
        lambda: reconstruct_source_from_idt_profile((1.0,), (0.0,), 1.0, (1.0,), (1.0,), (1.0,)),
        lambda: source_profile_mismatch_bound((1.0,), (1.0,), (1.0,), -1.0, 1.0),
    )
    for call in bad_calls:
        with pytest.raises(IDTNoetherProfileBindingError):
            call()
