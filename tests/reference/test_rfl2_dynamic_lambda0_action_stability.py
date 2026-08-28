import math

import numpy as np
import pytest

ETA = np.diag([-1.0, 1.0, 1.0, 1.0])


def finite4(values, name):
    out = np.asarray(values, dtype=float)
    if out.shape != (4,) or not np.all(np.isfinite(out)):
        raise ValueError(f"{name} must be one finite four-vector")
    return out


def scalar_stress(grad_phi, U):
    grad = finite4(grad_phi, "grad_phi")
    if not math.isfinite(U):
        raise ValueError("U must be finite")
    grad2 = float(grad @ ETA @ grad)
    return np.outer(grad, grad) - ETA * (0.5 * grad2 + U)


def scalar_stress_parts(grad_phi, U):
    grad = finite4(grad_phi, "grad_phi")
    if not math.isfinite(U):
        raise ValueError("U must be finite")
    grad2 = float(grad @ ETA @ grad)
    kinetic = np.outer(grad, grad) - 0.5 * ETA * grad2
    potential = -ETA * U
    return kinetic, potential


def lambda0(lambda_ref, kappa_e, U):
    if not all(math.isfinite(x) for x in (lambda_ref, kappa_e, U)):
        raise ValueError("Lambda_ref, kappa_E and U must be finite")
    if kappa_e <= 0.0:
        raise ValueError("kappa_E must be positive")
    return lambda_ref + kappa_e * U


def homogeneous_energy_pressure(phi_dot, U):
    if not all(math.isfinite(x) for x in (phi_dot, U)):
        raise ValueError("homogeneous state must be finite")
    K = 0.5 * phi_dot * phi_dot
    return K + U, K - U


def homogeneous_transfer(kappa_e, phi_dot, phi_ddot, U_prime):
    if kappa_e <= 0.0:
        raise ValueError("kappa_E must be positive")
    # lower-index nu=0 in (-,+,+,+): div T_kin = -d_t(K) = -phi_dot*phi_ddot
    kappa_div_tkin = kappa_e * (-phi_dot * phi_ddot)
    d_lambda = kappa_e * U_prime * phi_dot
    return kappa_div_tkin, d_lambda


def stability_class(U_second):
    if not math.isfinite(U_second):
        raise ValueError("U_second must be finite")
    if U_second > 0.0:
        return "RESTORING"
    if U_second == 0.0:
        return "MARGINAL"
    return "TACHYONIC_LINEAR_INSTABILITY"


def test_scalar_stress_decomposes_exactly_into_kinetic_and_potential():
    grad = [0.7, -0.2, 0.5, 0.1]
    U = 0.43
    full = scalar_stress(grad, U)
    kinetic, potential = scalar_stress_parts(grad, U)
    assert full == pytest.approx(kinetic + potential, rel=0.0, abs=1e-15)


def test_stationary_scalar_is_exact_metric_proportional_vacuum_stress():
    U0 = 2.3
    T = scalar_stress(np.zeros(4), U0)
    assert T == pytest.approx(-ETA * U0, rel=0.0, abs=1e-15)
    kinetic, _ = scalar_stress_parts(np.zeros(4), U0)
    assert kinetic == pytest.approx(np.zeros((4, 4)), rel=0.0, abs=1e-15)


def test_action_split_maps_potential_to_dynamic_lambda_coordinate():
    lam_ref = 0.12
    kappa_e = 0.8
    U = 0.35
    assert lambda0(lam_ref, kappa_e, U) == pytest.approx(0.4, rel=0.0, abs=1e-15)


def test_homogeneous_dynamic_scalar_equation_of_state():
    phi_dot = 1.4
    U = 0.9
    epsilon, pressure = homogeneous_energy_pressure(phi_dot, U)
    assert epsilon + pressure == pytest.approx(phi_dot * phi_dot, rel=0.0, abs=1e-15)
    T = scalar_stress([phi_dot, 0.0, 0.0, 0.0], U)
    assert T[0, 0] == pytest.approx(epsilon, rel=0.0, abs=1e-15)
    assert np.diag(T)[1:] == pytest.approx([pressure] * 3, rel=0.0, abs=1e-15)


def test_vacuum_equation_of_state_is_stationary_zero_kinetic_surface():
    epsilon, pressure = homogeneous_energy_pressure(0.0, 1.7)
    assert pressure == pytest.approx(-epsilon, rel=0.0, abs=1e-15)
    moving_epsilon, moving_pressure = homogeneous_energy_pressure(0.4, 1.7)
    assert moving_epsilon + moving_pressure > 0.0


def test_bianchi_transfer_follows_from_homogeneous_scalar_eom():
    kappa_e = 0.6
    phi_dot = 0.8
    U_prime = 1.25
    phi_ddot = -U_prime  # homogeneous flat-space scalar EOM
    kappa_div_tkin, d_lambda = homogeneous_transfer(kappa_e, phi_dot, phi_ddot, U_prime)
    assert kappa_div_tkin == pytest.approx(d_lambda, rel=0.0, abs=1e-15)


def test_homogeneous_full_scalar_energy_is_conserved_on_shell():
    phi_dot = 0.73
    U_prime = -0.44
    phi_ddot = -U_prime
    d_energy_dt = phi_dot * phi_ddot + U_prime * phi_dot
    assert d_energy_dt == pytest.approx(0.0, rel=0.0, abs=1e-15)


def test_spatial_gradient_has_anisotropic_kinetic_stress():
    g = 0.9
    kinetic, _ = scalar_stress_parts([0.0, g, 0.0, 0.0], 0.0)
    expected = 0.5 * g * g * np.diag([1.0, 1.0, -1.0, -1.0])
    assert kinetic == pytest.approx(expected, rel=0.0, abs=1e-15)
    # A metric-proportional tensor has equal spatial diagonal entries; this state has a resolved gradient axis.
    assert not math.isclose(kinetic[1, 1], kinetic[2, 2], rel_tol=0.0, abs_tol=1e-15)


def test_stationary_point_linear_stability_classification():
    assert stability_class(2.0) == "RESTORING"
    assert stability_class(0.0) == "MARGINAL"
    assert stability_class(-0.1) == "TACHYONIC_LINEAR_INSTABILITY"


def test_constant_lambda_reference_does_not_change_transfer_gradient_and_fail_closed():
    kappa_e = 0.4
    U_a, U_b = 0.2, 0.7
    delta_a = lambda0(1.0, kappa_e, U_b) - lambda0(1.0, kappa_e, U_a)
    delta_b = lambda0(9.0, kappa_e, U_b) - lambda0(9.0, kappa_e, U_a)
    assert delta_a == pytest.approx(delta_b, rel=0.0, abs=1e-15)
    with pytest.raises(ValueError, match="positive"):
        lambda0(0.0, 0.0, 1.0)
    with pytest.raises(ValueError, match="finite four-vector"):
        scalar_stress([0.0, 1.0], 1.0)
