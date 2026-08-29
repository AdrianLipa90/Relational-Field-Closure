import math

import pytest


def normal_relative_velocity(w, b, lapse):
    if not math.isfinite(lapse) or lapse <= 0.0:
        raise ValueError("positive finite lapse required")
    if not math.isfinite(w) or not math.isfinite(b):
        raise ValueError("finite rates required")
    return (w + b) / lapse


def translated_chart(w, b, xi_dot):
    if not all(math.isfinite(v) for v in (w, b, xi_dot)):
        raise ValueError("finite chart rates required")
    return w + xi_dot, b - xi_dot


def null_coordinate_rates(b, lapse):
    if not math.isfinite(lapse) or lapse <= 0.0:
        raise ValueError("positive finite lapse required")
    if not math.isfinite(b):
        raise ValueError("finite shift required")
    return -b + lapse, -b - lapse


def phi(x):
    if not math.isfinite(x) or x <= 0.0:
        raise ValueError("positive finite relative carrier required")
    return x - 1.0 - math.log(x)


def phi_shift_branch(b, s):
    if s not in (-1, 1):
        raise ValueError("orientation must be +/-1")
    den = 1.0 - s * b
    if den <= 0.0:
        raise ValueError("directional shift carrier outside domain")
    return phi(1.0 / den)


def phi_physical_branch(beta, s):
    if s not in (-1, 1):
        raise ValueError("orientation must be +/-1")
    if not math.isfinite(beta) or abs(beta) >= 1.0:
        raise ValueError("physical beta must satisfy |beta|<1")
    return phi(1.0 / (1.0 - s * beta))


def test_normal_relative_velocity_is_invariant_under_time_dependent_translation():
    w, b, n = 0.17, -0.22, 1.3
    xi_dot = 0.41
    wp, bp = translated_chart(w, b, xi_dot)
    assert normal_relative_velocity(wp, bp, n) == pytest.approx(normal_relative_velocity(w, b, n))
    assert wp + bp == pytest.approx(w + b)


def test_shift_alone_is_gauge_dependent_while_physical_velocity_is_not():
    w, b, n = 0.0, 0.31, 1.0
    v0 = normal_relative_velocity(w, b, n)
    phi0 = phi_shift_branch(b, 1)

    wp, bp = translated_chart(w, b, 0.12)
    v1 = normal_relative_velocity(wp, bp, n)
    phi1 = phi_shift_branch(bp, 1)

    assert v1 == pytest.approx(v0)
    assert bp != pytest.approx(b)
    assert phi1 != pytest.approx(phi0)


def test_null_coordinate_rate_asymmetry_collapses_to_unit_normal_relative_speed():
    b, n = 0.37, 1.2
    wp, wm = null_coordinate_rates(b, n)
    vp = normal_relative_velocity(wp, b, n)
    vm = normal_relative_velocity(wm, b, n)
    assert vp == pytest.approx(1.0)
    assert vm == pytest.approx(-1.0)


def test_material_adapted_chart_gives_v_equals_b_over_n():
    b, n = -0.42, 1.4
    assert normal_relative_velocity(0.0, b, n) == pytest.approx(b / n)


def test_local_orthonormal_material_adapted_specialization_recovers_oriented_beta():
    beta = 0.28
    assert normal_relative_velocity(0.0, beta, 1.0) == pytest.approx(beta)
    assert normal_relative_velocity(0.0, -beta, 1.0) == pytest.approx(-beta)


def test_physical_directional_branch_is_parity_conjugate():
    beta = 0.23
    assert phi_physical_branch(beta, 1) == pytest.approx(phi_physical_branch(-beta, -1))
    assert phi_physical_branch(beta, -1) == pytest.approx(phi_physical_branch(-beta, 1))


def test_physical_branch_matches_closed_form():
    beta = 0.31
    forward = math.log(1.0 - beta) + beta / (1.0 - beta)
    backward = math.log(1.0 + beta) - beta / (1.0 + beta)
    assert phi_physical_branch(beta, 1) == pytest.approx(forward)
    assert phi_physical_branch(beta, -1) == pytest.approx(backward)


def test_newtonian_quadratic_coefficient_is_one_half():
    # phi_s(beta)/beta^2 -> 1/2 as beta -> 0 for either orientation.
    for s in (-1, 1):
        b1 = 1.0e-4
        b2 = 5.0e-5
        q1 = phi_physical_branch(b1, s) / (b1 * b1)
        q2 = phi_physical_branch(b2, s) / (b2 * b2)
        assert q1 == pytest.approx(0.5, rel=2.0e-4)
        assert q2 == pytest.approx(0.5, rel=1.0e-4)


def test_oriented_cubic_coefficient_changes_sign():
    # Remove the universal quadratic term and divide by beta^3 -> +/- 2/3.
    beta = 2.0e-4
    cp = (phi_physical_branch(beta, 1) - 0.5 * beta**2) / beta**3
    cm = (phi_physical_branch(beta, -1) - 0.5 * beta**2) / beta**3
    assert cp == pytest.approx(2.0 / 3.0, rel=5.0e-4)
    assert cm == pytest.approx(-2.0 / 3.0, rel=5.0e-4)


@pytest.mark.parametrize("lapse", [0.0, -1.0, math.inf, math.nan])
def test_invalid_lapse_fails_closed(lapse):
    with pytest.raises(ValueError):
        normal_relative_velocity(0.0, 0.0, lapse)


@pytest.mark.parametrize("beta", [-1.0, 1.0, 1.2, math.inf, math.nan])
def test_invalid_physical_beta_fails_closed(beta):
    with pytest.raises(ValueError):
        phi_physical_branch(beta, 1)
