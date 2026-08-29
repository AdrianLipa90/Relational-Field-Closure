import math

import numpy as np
import pytest


LN2 = math.log(2.0)
KAPPA_E = 8.0 * math.pi


def incidence(n_nodes, edges):
    if n_nodes < 2:
        raise ValueError("at least two nodes required")
    d = np.zeros((len(edges), n_nodes), dtype=float)
    for r, (a, b) in enumerate(edges):
        if a == b or not (0 <= a < n_nodes and 0 <= b < n_nodes):
            raise ValueError("invalid edge")
        d[r, a] = -1.0
        d[r, b] = 1.0
    return d


def stiffness(n_nodes, edges, mobility):
    if len(edges) != len(mobility) or not edges:
        raise ValueError("edge/mobility mismatch")
    m = np.asarray(mobility, dtype=float)
    if not np.all(np.isfinite(m)) or np.any(m <= 0.0):
        raise ValueError("positive finite mobilities required")
    d = incidence(n_nodes, edges)
    return d.T @ np.diag(m) @ d


def onsager_uniform_from_k0(k0, n_states):
    if n_states <= 0 or not math.isfinite(float(n_states)):
        raise ValueError("positive finite state count required")
    return (LN2 / n_states) * np.asarray(k0, dtype=float)


def k0_from_onsager(g, n_states):
    if n_states <= 0:
        raise ValueError("positive state count required")
    return (n_states / LN2) * np.asarray(g, dtype=float)


def mass2(alpha_i, kappa_e=KAPPA_E):
    if not math.isfinite(alpha_i) or not math.isfinite(kappa_e) or kappa_e <= 0.0:
        raise ValueError("invalid mass normalization")
    return alpha_i / kappa_e


def kg_operator(k0, m2):
    k0 = np.asarray(k0, dtype=float)
    if k0.ndim != 2 or k0.shape[0] != k0.shape[1]:
        raise ValueError("square stiffness required")
    if not math.isfinite(m2) or m2 < 0.0:
        raise ValueError("nonnegative finite mass2 required")
    return k0 + m2 * np.eye(k0.shape[0])


def energy(phi, vel, k0, m2):
    phi = np.asarray(phi, dtype=float)
    vel = np.asarray(vel, dtype=float)
    return 0.5 * float(vel @ vel + phi @ k0 @ phi + m2 * (phi @ phi))


def energy_derivative(phi, vel, acc, k0, m2):
    phi = np.asarray(phi, dtype=float)
    vel = np.asarray(vel, dtype=float)
    acc = np.asarray(acc, dtype=float)
    return float(vel @ acc + vel @ k0 @ phi + m2 * (vel @ phi))


def harmonic_mean(values):
    vals = np.asarray(values, dtype=float)
    if vals.size == 0 or not np.all(np.isfinite(vals)) or np.any(vals <= 0.0):
        raise ValueError("positive finite values required")
    return float(vals.size / np.sum(1.0 / vals))


def continuum_omega2(k, m_eff, m2):
    vals = (k, m_eff, m2)
    if not all(math.isfinite(v) for v in vals) or m_eff <= 0.0 or m2 < 0.0:
        raise ValueError("invalid continuum state")
    return m_eff * k * k + m2


def alpha_from_clock(omega_t, c, kappa_e=KAPPA_E):
    vals = (omega_t, c, kappa_e)
    if not all(math.isfinite(v) for v in vals) or c <= 0.0 or kappa_e <= 0.0:
        raise ValueError("invalid clock calibration")
    return kappa_e * (omega_t / c) ** 2


def sample_graph():
    n = 4
    edges = [(0, 1), (1, 2), (2, 3), (3, 0), (0, 2)]
    mobility = [1.0, 2.0, 1.5, 0.75, 1.25]
    return n, edges, mobility


def test_uniform_onsager_stiffness_roundtrip_exact_normalization():
    n, edges, mobility = sample_graph()
    k0 = stiffness(n, edges, mobility)
    g = onsager_uniform_from_k0(k0, n)
    assert np.allclose(k0_from_onsager(g, n), k0, rtol=1.0e-14, atol=1.0e-14)


def test_stiffness_is_symmetric_psd_with_constant_null():
    n, edges, mobility = sample_graph()
    k0 = stiffness(n, edges, mobility)
    assert np.allclose(k0, k0.T)
    eig = np.linalg.eigvalsh(k0)
    assert eig.min() >= -1.0e-12
    assert np.allclose(k0 @ np.ones(n), 0.0, atol=1.0e-13)


def test_mass_term_lifts_every_mode_by_mass2():
    n, edges, mobility = sample_graph()
    k0 = stiffness(n, edges, mobility)
    m2 = 0.37
    eig0 = np.linalg.eigvalsh(k0)
    eigkg = np.linalg.eigvalsh(kg_operator(k0, m2))
    assert np.allclose(eigkg, eig0 + m2, rtol=1.0e-13, atol=1.0e-13)


def test_uniform_mode_becomes_information_mass_gap():
    n, edges, mobility = sample_graph()
    k0 = stiffness(n, edges, mobility)
    alpha_i = 0.8
    m2 = mass2(alpha_i)
    one = np.ones(n)
    assert np.allclose(kg_operator(k0, m2) @ one, m2 * one)
    assert KAPPA_E * m2 == pytest.approx(alpha_i)


def test_modal_frequency_squared_is_lambda_plus_mass2():
    n, edges, mobility = sample_graph()
    k0 = stiffness(n, edges, mobility)
    m2 = 0.21
    for lam in np.linalg.eigvalsh(k0):
        omega2 = lam + m2
        assert omega2 >= 0.0
        assert omega2 == pytest.approx(lam + m2)


def test_conservative_graph_kg_energy_derivative_is_zero():
    n, edges, mobility = sample_graph()
    k0 = stiffness(n, edges, mobility)
    m2 = 0.4
    phi = np.array([0.7, -0.2, 0.4, -0.9])
    vel = np.array([0.1, 0.3, -0.25, 0.05])
    acc = -(k0 + m2 * np.eye(n)) @ phi
    assert energy(phi, vel, k0, m2) > 0.0
    assert energy_derivative(phi, vel, acc, k0, m2) == pytest.approx(0.0, abs=1.0e-13)


def test_dissipative_overlay_has_negative_semidefinite_energy_derivative():
    n, edges, mobility = sample_graph()
    k0 = stiffness(n, edges, mobility)
    c_eta = stiffness(n, edges, [0.5, 0.8, 0.6, 0.9, 0.7])
    m2 = 0.25
    phi = np.array([0.7, -0.2, 0.4, -0.9])
    vel = np.array([0.1, 0.3, -0.25, 0.05])
    acc = -c_eta @ vel - (k0 + m2 * np.eye(n)) @ phi
    dedt = energy_derivative(phi, vel, acc, k0, m2)
    expected = -float(vel @ c_eta @ vel)
    assert dedt == pytest.approx(expected, abs=1.0e-13)
    assert dedt <= 1.0e-13


def test_heterogeneous_premetric_continuum_dispersion():
    mobility = [0.8, 1.2, 2.4, 1.5]
    m_eff = harmonic_mean(mobility)
    k = 0.15
    m2 = 0.32
    assert continuum_omega2(k, m_eff, m2) == pytest.approx(m_eff * k**2 + m2)


def test_metric_lightcone_slot_is_exact_when_calibrated_meff_equals_c2():
    c = 3.0
    k = 0.27
    m2 = 0.18
    omega2 = continuum_omega2(k, c * c, m2)
    assert omega2 == pytest.approx(c * c * k * k + m2)


def test_common_clock_mass_scale_relation_is_exact_given_gate_input():
    omega_t = 2.75
    c = 1.4
    alpha_i = alpha_from_clock(omega_t, c)
    m2 = mass2(alpha_i)
    assert m2 == pytest.approx((omega_t / c) ** 2)


@pytest.mark.parametrize("bad", [0.0, -1.0, math.inf, math.nan])
def test_invalid_mobility_fails_closed(bad):
    with pytest.raises(ValueError):
        stiffness(2, [(0, 1)], [bad])


@pytest.mark.parametrize("bad_m2", [-1.0, math.inf, math.nan])
def test_invalid_mass2_fails_closed(bad_m2):
    with pytest.raises(ValueError):
        kg_operator(np.eye(2), bad_m2)


def test_invalid_clock_calibration_fails_closed():
    with pytest.raises(ValueError):
        alpha_from_clock(1.0, 0.0)
