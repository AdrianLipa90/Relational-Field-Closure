import math

import pytest

from src.rfc.fixed_amplitude_clock_radial_state_separation import (
    FixedAmplitudeClockRadialStateError,
    amplitude_sq_from_noether,
    clock_radial_ratio,
    clock_radial_ratio_closed_form,
    clock_radial_state_defect,
    directional_rate,
    phase_curvature_second_derivative_at_reference,
    phase_information_curvature,
    phi,
    pointwise_crossing_residual,
    radial_curvature_second_derivative_fixed_amplitude,
    reciprocal_rate_factor,
)


def test_reference_clock_information_curvature_is_zero():
    r0 = 2.3
    area = 4.1
    assert reciprocal_rate_factor(r0, r0) == pytest.approx(1.0)
    assert phi(1.0) == pytest.approx(0.0)
    assert phase_information_curvature(r0, r0, area) == pytest.approx(0.0)


def test_nonzero_fixed_amplitude_radial_coordinate_is_separated_at_reference():
    r0 = 2.3
    amplitude_sq = 0.7
    j = 2.0 * amplitude_sq * r0
    assert amplitude_sq_from_noether(j, r0) == pytest.approx(amplitude_sq)
    assert clock_radial_ratio(r0, r0, 4.1, j) == pytest.approx(0.0)
    assert clock_radial_state_defect(r0, r0, 4.1, j) == pytest.approx(1.0)


def test_noether_amplitude_reconstruction_is_directionally_invariant_for_fixed_amplitude():
    r0 = 1.9
    amplitude_sq = 0.42
    for s in (-1, 1):
        for b in (-0.4, -0.1, 0.2, 0.55):
            rs = directional_rate(r0, b, s)
            j = 2.0 * amplitude_sq * rs
            assert amplitude_sq_from_noether(j, rs) == pytest.approx(amplitude_sq)


def test_closed_form_clock_radial_ratio_matches_reconstructed_form():
    r0 = 2.0
    rs = 1.35
    area = 3.7
    amplitude_sq = 0.81
    j = 2.0 * amplitude_sq * rs
    assert clock_radial_ratio(r0, rs, area, j) == pytest.approx(
        clock_radial_ratio_closed_form(r0, rs, area, j)
    )


def test_pointwise_crossing_condition_gives_unit_ratio_and_zero_defect():
    r0 = 2.0
    rs = 1.3
    area = 2.7
    xi_phase = phase_information_curvature(r0, rs, area)
    assert xi_phase > 0.0
    j = 2.0 * rs * xi_phase
    assert pointwise_crossing_residual(r0, rs, area, j) == pytest.approx(
        0.0, abs=2.0e-12
    )
    assert clock_radial_ratio(r0, rs, area, j) == pytest.approx(1.0)
    assert clock_radial_state_defect(r0, rs, area, j) == pytest.approx(
        0.0, abs=2.0e-12
    )


def test_directional_clock_second_curvature_is_positive_while_fixed_radial_is_zero():
    area = 3.2
    assert phase_curvature_second_derivative_at_reference(area) == pytest.approx(
        1.0 / area
    )
    assert radial_curvature_second_derivative_fixed_amplitude() == pytest.approx(0.0)


def test_numeric_second_derivative_matches_analytic_reference_curvature():
    r0 = 2.4
    area = 5.0
    h = 1.0e-4
    for s in (-1, 1):
        f0 = phase_information_curvature(r0, directional_rate(r0, 0.0, s), area)
        fp = phase_information_curvature(r0, directional_rate(r0, h, s), area)
        fm = phase_information_curvature(r0, directional_rate(r0, -h, s), area)
        second = (fp - 2.0 * f0 + fm) / h**2
        assert second == pytest.approx(1.0 / area, rel=2.0e-4)


def test_phi_is_nonnegative_on_positive_rate_ratios():
    for x in (0.2, 0.8, 1.0, 1.3, 7.0):
        assert phi(x) >= -1.0e-15


@pytest.mark.parametrize("bad", [0.0, -1.0, math.inf, math.nan])
def test_positive_rate_area_current_inputs_fail_closed(bad):
    with pytest.raises(FixedAmplitudeClockRadialStateError):
        reciprocal_rate_factor(bad, 1.0)
    with pytest.raises(FixedAmplitudeClockRadialStateError):
        phase_information_curvature(1.0, 1.0, bad)
    with pytest.raises(FixedAmplitudeClockRadialStateError):
        amplitude_sq_from_noether(bad, 1.0)


def test_directional_coordinate_domain_fails_closed():
    with pytest.raises(FixedAmplitudeClockRadialStateError):
        directional_rate(1.0, 1.0, 1)
    with pytest.raises(FixedAmplitudeClockRadialStateError):
        directional_rate(1.0, 0.2, 0)
