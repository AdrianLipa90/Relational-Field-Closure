import math

import pytest

from src.rfc.phase_clock_relational_volume import (
    FACE,
    FULL_TETRA_CP1,
    PhaseClockRelationalVolumeError,
    normalized_density_from_action_scale,
    phase_clock_relational_volume,
    reduced_generator_density,
)
from src.rfc.relational_generator_source_density import C_LIGHT, KAPPA_INFO


def test_full_tetra_phase_clock_volume_is_pi_c3_over_abs_omega3():
    omega = 8.0e6
    out = phase_clock_relational_volume(omega)
    assert out.scope == FULL_TETRA_CP1
    assert math.isclose(out.projective_area_m2, math.pi * C_LIGHT**2 / omega**2, rel_tol=1e-15)
    assert math.isclose(out.phase_clock_length_m, C_LIGHT / omega, rel_tol=1e-15)
    assert math.isclose(out.relational_volume_m3, math.pi * C_LIGHT**3 / omega**3, rel_tol=1e-15)


def test_face_volume_is_one_quarter_of_full_tetra_volume():
    omega = 4.0e5
    full = phase_clock_relational_volume(omega, scope=FULL_TETRA_CP1)
    face = phase_clock_relational_volume(omega, scope=FACE)
    assert math.isclose(face.relational_volume_m3, full.relational_volume_m3 / 4.0, rel_tol=1e-15)


def test_generator_reduces_exactly_to_signed_omega_abs_omega_cubed_form():
    B = 2.5e-34
    omega = 7.0e9
    N = 11.0
    phi = 0.42
    out = reduced_generator_density(B, omega, N, phi)

    expected = B * N * omega**4 * (phi + KAPPA_INFO) / (math.pi * C_LIGHT**3)
    assert math.isclose(out.energy_density_j_m3, out.closed_form_j_m3, rel_tol=1e-15)
    assert math.isclose(out.energy_density_j_m3, expected, rel_tol=1e-15)


def test_negative_rate_preserves_generator_sign_while_geometry_uses_rate_magnitude():
    positive = reduced_generator_density(1.0, 3.0, 2.0, 0.5)
    negative = reduced_generator_density(1.0, -3.0, 2.0, 0.5)
    assert math.isclose(positive.geometry.relational_volume_m3, negative.geometry.relational_volume_m3, rel_tol=1e-15)
    assert math.isclose(negative.energy_density_j_m3, -positive.energy_density_j_m3, rel_tol=1e-15)


def test_positive_frequency_density_has_omega_four_scaling():
    rho1 = reduced_generator_density(1.0, 2.0, 3.0, 0.4).energy_density_j_m3
    rho2 = reduced_generator_density(1.0, 4.0, 3.0, 0.4).energy_density_j_m3
    assert math.isclose(rho2 / rho1, 16.0, rel_tol=1e-15)


def test_half_and_total_action_normalizations_preserve_rf_e5_factor_two():
    hbar = 1.054571817e-34
    omega = 2.3e12
    N = 5.0
    kinetic = normalized_density_from_action_scale(
        omega,
        N,
        hbar,
        carrier_fraction=0.5,
    )
    total = normalized_density_from_action_scale(
        omega,
        N,
        hbar,
        carrier_fraction=1.0,
    )
    expected_kinetic = hbar * N * omega**4 / (2.0 * math.pi * C_LIGHT**3)
    expected_total = hbar * N * omega**4 / (math.pi * C_LIGHT**3)
    assert math.isclose(kinetic, expected_kinetic, rel_tol=1e-15)
    assert math.isclose(total, expected_total, rel_tol=1e-15)
    assert math.isclose(total / kinetic, 2.0, rel_tol=1e-15)


def test_fail_closed_geometry_and_normalization_inputs():
    bad_calls = (
        lambda: phase_clock_relational_volume(0.0),
        lambda: phase_clock_relational_volume(float("nan")),
        lambda: phase_clock_relational_volume(1.0, scope="UNKNOWN"),
        lambda: reduced_generator_density(1.0, 1.0, -1.0, 0.0),
        lambda: normalized_density_from_action_scale(1.0, 1.0, 0.0, carrier_fraction=0.5),
        lambda: normalized_density_from_action_scale(1.0, 1.0, 1.0, carrier_fraction=-1.0),
    )
    for call in bad_calls:
        with pytest.raises(PhaseClockRelationalVolumeError):
            call()
