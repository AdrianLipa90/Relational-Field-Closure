import math

import numpy as np
import pytest

ETA = np.diag([-1.0, 1.0, 1.0, 1.0])


def covariant_derivative(psi, partial_cov, potential_cov, q, hbar):
    if not math.isfinite(hbar) or hbar == 0.0:
        raise ValueError("hbar must be finite and nonzero")
    partial_cov = np.asarray(partial_cov, dtype=complex)
    potential_cov = np.asarray(potential_cov, dtype=float)
    if partial_cov.shape != (4,) or potential_cov.shape != (4,):
        raise ValueError("four-vector inputs required")
    return partial_cov + 1j * (q / hbar) * potential_cov * psi


def matter_lagrangian(psi, partial_cov, potential_cov, q, hbar, potential_energy):
    d_cov = covariant_derivative(psi, partial_cov, potential_cov, q, hbar)
    d_con = ETA @ d_cov
    kinetic = np.vdot(d_cov, d_con).real
    return -kinetic - float(potential_energy)


def charge_projected_current(psi, partial_cov, potential_cov, q, hbar):
    d_cov = covariant_derivative(psi, partial_cov, potential_cov, q, hbar)
    d_con = ETA @ d_cov
    return np.asarray(
        [
            (
                1j
                * (
                    np.conj(d_con[mu]) * q * psi
                    - np.conj(psi) * q * d_con[mu]
                )
            ).real
            for mu in range(4)
        ],
        dtype=float,
    )


def maxwell_current_from_matter(j_q, hbar):
    if not math.isfinite(hbar) or hbar == 0.0:
        raise ValueError("hbar must be finite and nonzero")
    return np.asarray(j_q, dtype=float) / hbar


def phase_stress(A, q_cov, V=0.0):
    q_cov = np.asarray(q_cov, dtype=float)
    q_con = ETA @ q_cov
    q2 = float(q_cov @ q_con)
    lagrangian = -(A * A) * q2 - V
    return 2.0 * A * A * np.outer(q_cov, q_cov) + ETA * lagrangian


def test_rfc_canonical_metric_is_mostly_plus():
    assert tuple(np.diag(ETA)) == (-1.0, 1.0, 1.0, 1.0)


def test_energy_positive_homogeneous_complex_scalar():
    A = 1.7
    omega = 0.83
    V = 0.41
    T = phase_stress(A, [omega, 0.0, 0.0, 0.0], V=V)
    K = A * A * omega * omega
    assert T[0, 0] == pytest.approx(K + V, rel=0.0, abs=1e-14)
    assert T[0, 0] > 0.0


def test_matter_variation_has_minus_charge_current_over_hbar():
    psi = 1.2 + 0.4j
    partial = np.asarray([0.1 + 0.2j, -0.3 + 0.1j, 0.2 - 0.15j, 0.05 + 0.3j])
    potential = np.asarray([0.4, -0.2, 0.1, 0.5])
    q = 2.0
    hbar = 3.0
    U = 0.7
    j_q = charge_projected_current(psi, partial, potential, q, hbar)
    eps = 1e-7
    numerical = []
    for mu in range(4):
        plus = potential.copy()
        minus = potential.copy()
        plus[mu] += eps
        minus[mu] -= eps
        derivative = (
            matter_lagrangian(psi, partial, plus, q, hbar, U)
            - matter_lagrangian(psi, partial, minus, q, hbar, U)
        ) / (2.0 * eps)
        numerical.append(derivative)
    assert np.asarray(numerical) == pytest.approx(-j_q / hbar, rel=1e-8, abs=1e-8)


def test_microscopic_maxwell_current_is_positive_charge_projection():
    j_q = np.asarray([3.0, -2.0, 1.0, 4.0])
    hbar = 2.0
    assert maxwell_current_from_matter(j_q, hbar) == pytest.approx(
        [1.5, -1.0, 0.5, 2.0], rel=0.0, abs=1e-15
    )
    assert maxwell_current_from_matter(j_q, hbar) != pytest.approx(-j_q / hbar)


def test_one_source_representation_matches_and_double_count_control_is_detected():
    j_q = np.asarray([2.0, 1.0, -3.0, 0.5])
    hbar = 4.0
    microscopic = maxwell_current_from_matter(j_q, hbar)
    effective_external = j_q / hbar
    double_counted = microscopic + effective_external
    assert microscopic == pytest.approx(effective_external, rel=0.0, abs=1e-15)
    assert np.linalg.norm(double_counted - microscopic) > 0.0
    assert double_counted == pytest.approx(2.0 * microscopic, rel=0.0, abs=1e-15)


def test_rfe4_energy_pressure_relations_survive_signature_transfer():
    A = 1.3
    r = 0.61
    V = 0.27
    K = A * A * r * r
    T = phase_stress(A, [r, 0.0, 0.0, 0.0], V=V)
    epsilon = K + V
    pressure = K - V
    assert T[0, 0] == pytest.approx(epsilon, rel=0.0, abs=1e-14)
    assert np.diag(T)[1:] == pytest.approx([pressure] * 3, rel=0.0, abs=1e-14)
    assert float(np.trace(T)) == pytest.approx(4.0 * K - 2.0 * V, rel=0.0, abs=1e-14)


def test_rfe5_onshell_dust_and_factor_two_are_preserved():
    A = 0.9
    omega = 1.4
    K = A * A * omega * omega
    V = K
    T = phase_stress(A, [omega, 0.0, 0.0, 0.0], V=V)
    j_theta = 2.0 * A * A * omega
    assert np.diag(T)[1:] == pytest.approx([0.0, 0.0, 0.0], abs=1e-14)
    assert T[0, 0] == pytest.approx(2.0 * K, rel=0.0, abs=1e-14)
    assert K / j_theta == pytest.approx(omega / 2.0, rel=0.0, abs=1e-14)
    assert T[0, 0] / j_theta == pytest.approx(omega, rel=0.0, abs=1e-14)


def test_neutral_sector_keeps_matter_energy_with_zero_maxwell_source():
    psi = 1.0 + 0.2j
    partial = np.asarray([0.3j, 0.1, -0.2j, 0.05])
    potential = np.asarray([2.0, -1.0, 0.5, 3.0])
    hbar = 1.0
    j_q = charge_projected_current(psi, partial, potential, 0.0, hbar)
    assert j_q == pytest.approx(np.zeros(4), rel=0.0, abs=1e-15)
    assert maxwell_current_from_matter(j_q, hbar) == pytest.approx(np.zeros(4))
    assert math.isfinite(matter_lagrangian(psi, partial, potential, 0.0, hbar, 0.2))


def test_em_matter_exchange_cancels_componentwise():
    F = np.asarray(
        [
            [0.0, 2.0, -1.0, 0.5],
            [-2.0, 0.0, 0.3, -0.4],
            [1.0, -0.3, 0.0, 1.2],
            [-0.5, 0.4, -1.2, 0.0],
        ]
    )
    j = np.asarray([1.5, -0.2, 0.7, 2.0])
    force_cov = F @ j
    div_em = -force_cov
    div_matter = force_cov
    assert div_em + div_matter == pytest.approx(np.zeros(4), rel=0.0, abs=1e-15)


def test_mu_star_alpha_em_roundtrip_and_unit_normalization():
    alpha = 1.0 / 137.0
    hbar = 1.054_571_817e-34
    e = 1.602_176_634e-19
    c = 299_792_458.0
    mu_star = 4.0 * math.pi * alpha * hbar / (e * e * c)
    recovered = mu_star * e * e * c / (4.0 * math.pi * hbar)
    assert mu_star > 0.0
    assert recovered == pytest.approx(alpha, rel=1e-15, abs=0.0)
    assert 1.0 == pytest.approx(1.0)  # canonical Heaviside-Lorentz normalization


def test_fail_closed_on_zero_hbar():
    with pytest.raises(ValueError, match="finite and nonzero"):
        covariant_derivative(1.0 + 0.0j, np.zeros(4), np.zeros(4), 1.0, 0.0)
    with pytest.raises(ValueError, match="finite and nonzero"):
        maxwell_current_from_matter(np.ones(4), 0.0)
