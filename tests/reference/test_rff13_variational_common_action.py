import math

import pytest

from src.rfc.foundational_phase_source_formalism import KAPPA_INFO
from src.rfc.variational_common_action import (
    VariationalCommonActionError,
    canonical_phase_state,
    constant_B_linear_hamiltonian_branch,
    direct_B_first_order_el_audit,
    hamiltonian_binding,
    homogeneous_hamiltonian_transport_identity,
    lambda_partition_binding,
    lambda_potential_allocation_binding,
    noether_hamiltonian_binding,
)


def test_canonical_momentum_is_B_times_phase_factor_and_energy_is_P_omega():
    B = 3.0
    phase = 0.4
    omega = 5.0
    out = canonical_phase_state(B, phase, omega)
    X = phase + KAPPA_INFO
    assert math.isclose(out.canonical_momentum, B * X, rel_tol=0.0, abs_tol=1e-15)
    assert math.isclose(out.energy_per_occupation, B * X * omega, rel_tol=0.0, abs_tol=1e-15)


def test_degree_one_hamiltonian_closes_rate_homogeneity_and_source_energy():
    B = 2.0
    phase = 0.7
    omega = 4.0
    X = phase + KAPPA_INFO
    P = B * X
    H = P * omega
    out = hamiltonian_binding(B, phase, omega, H, omega)
    assert abs(out.euler_homogeneity_residual) < 1e-15
    assert abs(out.phase_rate_residual) < 1e-15
    assert abs(out.source_energy_residual) < 1e-15


def test_hamiltonian_homogeneity_firewall_detects_wrong_energy():
    out = hamiltonian_binding(2.0, 0.5, 3.0, hamiltonian=11.0, dH_dP=3.0)
    assert out.euler_homogeneity_residual != 0.0
    assert out.source_energy_residual != 0.0


def test_noether_hamiltonian_binding_respects_carrier_quantum_normalization():
    B = 2.5
    phase = 0.2
    omega = 6.0
    q0 = 7.0
    Q = 14.0
    X = phase + KAPPA_INFO
    eps_q = B * omega * X / q0
    H = Q * eps_q
    out = noether_hamiltonian_binding(H, Q, B, phase, omega, carrier_quantum=q0)
    assert abs(out.residual) < 1e-15


def test_noether_binding_is_covariant_under_positive_carrier_rescaling():
    B = 1.5
    phase = 0.3
    omega = 2.0
    q0 = 5.0
    Q = 10.0
    X = phase + KAPPA_INFO
    H = Q * B * omega * X / q0
    base = noether_hamiltonian_binding(H, Q, B, phase, omega, carrier_quantum=q0)
    lam = 11.0
    rescaled = noether_hamiltonian_binding(
        H,
        lam * Q,
        B,
        phase,
        omega,
        carrier_quantum=lam * q0,
    )
    assert abs(base.residual) < 1e-15
    assert abs(rescaled.residual) < 1e-15
    assert math.isclose(
        rescaled.noether_energy_per_charge,
        base.noether_energy_per_charge / lam,
        rel_tol=1e-15,
    )


def test_lambda_allocation_derivative_reproduces_full_rf_f7_exchange():
    Up = 12.0
    n = 3.0
    phidot = 2.5
    target_Hphi = -Up / n
    out = lambda_potential_allocation_binding(Up, n, target_Hphi, phidot)
    assert abs(out.derivative_residual) < 1e-15
    assert abs(out.transport_residual) < 1e-15
    assert math.isclose(out.hamiltonian_exchange_rate, -(Up / n) * phidot, rel_tol=1e-15)


def test_lambda_allocation_firewall_exposes_partial_transfer():
    out = lambda_potential_allocation_binding(10.0, 2.0, -2.0, 3.0)
    assert out.derivative_residual != 0.0
    assert out.transport_residual != 0.0


def test_lambda_partition_interpolates_rf_l2_and_rf_f7_with_exact_total_exchange():
    Up = 8.0
    n = 2.0
    phidot = 3.0
    for eta in (0.0, 0.25, 1.0):
        Hphi = -eta * Up / n
        out = lambda_partition_binding(Up, n, eta, Hphi, phidot)
        assert abs(out.derivative_residual) < 1e-15
        assert abs(out.partition_residual) < 1e-15
        assert math.isclose(
            out.generator_exchange_density_rate + out.kinetic_exchange_density_rate,
            Up * phidot,
            rel_tol=1e-15,
        )
    rf_l2 = lambda_partition_binding(Up, n, 0.0, 0.0, phidot)
    rf_f7 = lambda_partition_binding(Up, n, 1.0, -Up / n, phidot)
    assert rf_l2.generator_exchange_density_rate == 0.0
    assert rf_f7.kinetic_exchange_density_rate == 0.0


def test_direct_B_first_order_el_audit_exposes_generic_Bdot_coefficient_gap():
    phase = 0.8
    omega = 4.0
    out = direct_B_first_order_el_audit(phase, omega)
    assert out.affine_first_order_EL_Bdot_coefficient == 0.0
    assert math.isclose(
        out.target_Bdot_coefficient,
        (phase + KAPPA_INFO) * omega,
        rel_tol=0.0,
        abs_tol=1e-15,
    )
    assert out.generic_assignment_residual != 0.0


def test_homogeneous_degree_one_hamiltonian_reproduces_full_f11_left_side():
    B = 2.0
    X = 3.0
    h = 5.0
    hx = -0.7
    hphi = 0.4
    phidot = 1.25
    out = homogeneous_hamiltonian_transport_identity(B, X, h, hx, hphi, phidot)
    assert abs(out.identity_residual) < 1e-14
    assert math.isclose(out.f11_left_hand_side, B * X * hphi * phidot, rel_tol=1e-15)


def test_constant_B_linear_hamiltonian_branch_roundtrips_rf_f11():
    out = constant_B_linear_hamiltonian_branch(B_action=2.0, phase_factor=3.0, invariant_C=5.0)
    assert abs(out.reconstructed_B_rate) < 1e-15
    assert abs(out.f11_closed_residual) < 1e-15
    assert math.isclose(out.phase_rate * out.phase_factor, 5.0, rel_tol=1e-15)
    assert math.isclose(out.hamiltonian, 10.0, rel_tol=1e-15)
    assert math.isclose(
        out.phase_acceleration,
        -(out.phase_rate**2) / out.phase_factor,
        rel_tol=1e-15,
    )


def test_fail_closed_inputs():
    bad_calls = (
        lambda: canonical_phase_state(1.0, -KAPPA_INFO, 1.0),
        lambda: canonical_phase_state(float("nan"), 0.0, 1.0),
        lambda: noether_hamiltonian_binding(1.0, 0.0, 1.0, 0.1, 1.0),
        lambda: noether_hamiltonian_binding(1.0, 1.0, 1.0, 0.1, 1.0, carrier_quantum=0.0),
        lambda: lambda_potential_allocation_binding(1.0, 0.0, 1.0, 1.0),
        lambda: lambda_partition_binding(1.0, 1.0, 1.5, -1.0, 1.0),
        lambda: constant_B_linear_hamiltonian_branch(1.0, 0.0, 1.0),
    )
    for call in bad_calls:
        with pytest.raises(VariationalCommonActionError):
            call()
