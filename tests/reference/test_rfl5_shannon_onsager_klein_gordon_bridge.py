import math

import numpy as np
import pytest


LN2 = math.log(2.0)


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


def spectral_operator(k0, gap2):
    k0 = np.asarray(k0, dtype=float)
    if k0.ndim != 2 or k0.shape[0] != k0.shape[1]:
        raise ValueError("square stiffness required")
    if not math.isfinite(gap2) or gap2 < 0.0:
        raise ValueError("nonnegative finite premetric gap required")
    return k0 + gap2 * np.eye(k0.shape[0])


def energy(phi, vel, k0, gap2):
    phi = np.asarray(phi, dtype=float)
    vel = np.asarray(vel, dtype=float)
    return 0.5 * float(vel @ vel + phi @ k0 @ phi + gap2 * (phi @ phi))


def energy_derivative(phi, vel, acc, k0, gap2):
    phi = np.asarray(phi, dtype=float)
    vel = np.asarray(vel, dtype=float)
    acc = np.asarray(acc, dtype=float)
    return float(vel @ acc + vel @ k0 @ phi + gap2 * (vel @ phi))


def harmonic_mean(values):
    vals = np.asarray(values, dtype=float)
    if vals.size == 0 or not np.all(np.isfinite(vals)) or np.any(vals <= 0.0):
        raise ValueError("positive finite values required")
    return float(vals.size / np.sum(1.0 / vals))


def continuum_omega_lambda2(k_xi, m_eff, gap2):
    vals = (k_xi, m_eff, gap2)
    if not all(math.isfinite(v) for v in vals) or m_eff <= 0.0 or gap2 < 0.0:
        raise ValueError("invalid premetric continuum state")
    return m_eff * k_xi * k_xi + gap2


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


def test_premetric_gap_lifts_every_mode_by_gap2():
    n, edges, mobility = sample_graph()
    k0 = stiffness(n, edges, mobility)
    gap2 = 0.37
    eig0 = np.linalg.eigvalsh(k0)
    eig_gap = np.linalg.eigvalsh(spectral_operator(k0, gap2))
    assert np.allclose(eig_gap, eig0 + gap2, rtol=1.0e-13, atol=1.0e-13)


def test_uniform_mode_is_premetric_homogeneous_gap():
    n, edges, mobility = sample_graph()
    k0 = stiffness(n, edges, mobility)
    gap2 = 0.031
    one = np.ones(n)
    assert np.allclose(spectral_operator(k0, gap2) @ one, gap2 * one)


def test_modal_ordering_frequency_squared_is_lambda_plus_gap2():
    n, edges, mobility = sample_graph()
    k0 = stiffness(n, edges, mobility)
    gap2 = 0.21
    for lam in np.linalg.eigvalsh(k0):
        omega_lambda2 = lam + gap2
        assert omega_lambda2 >= 0.0
        assert omega_lambda2 == pytest.approx(lam + gap2)


def test_conservative_graph_energy_derivative_is_zero():
    n, edges, mobility = sample_graph()
    k0 = stiffness(n, edges, mobility)
    gap2 = 0.4
    phi = np.array([0.7, -0.2, 0.4, -0.9])
    vel = np.array([0.1, 0.3, -0.25, 0.05])
    acc = -spectral_operator(k0, gap2) @ phi
    assert energy(phi, vel, k0, gap2) > 0.0
    assert energy_derivative(phi, vel, acc, k0, gap2) == pytest.approx(0.0, abs=1.0e-13)


def test_dissipative_overlay_has_negative_semidefinite_energy_derivative():
    n, edges, mobility = sample_graph()
    k0 = stiffness(n, edges, mobility)
    c_eta = stiffness(n, edges, [0.5, 0.8, 0.6, 0.9, 0.7])
    gap2 = 0.25
    phi = np.array([0.7, -0.2, 0.4, -0.9])
    vel = np.array([0.1, 0.3, -0.25, 0.05])
    acc = -c_eta @ vel - spectral_operator(k0, gap2) @ phi
    dedl = energy_derivative(phi, vel, acc, k0, gap2)
    expected = -float(vel @ c_eta @ vel)
    assert dedl == pytest.approx(expected, abs=1.0e-13)
    assert dedl <= 1.0e-13


def test_heterogeneous_premetric_continuum_dispersion():
    mobility = [0.8, 1.2, 2.4, 1.5]
    m_eff = harmonic_mean(mobility)
    k_xi = 0.15
    gap2 = 0.32
    assert continuum_omega_lambda2(k_xi, m_eff, gap2) == pytest.approx(
        m_eff * k_xi**2 + gap2
    )


@pytest.mark.parametrize("bad", [0.0, -1.0, math.inf, math.nan])
def test_invalid_mobility_fails_closed(bad):
    with pytest.raises(ValueError):
        stiffness(2, [(0, 1)], [bad])


@pytest.mark.parametrize("bad_gap2", [-1.0, math.inf, math.nan])
def test_invalid_premetric_gap_fails_closed(bad_gap2):
    with pytest.raises(ValueError):
        spectral_operator(np.eye(2), bad_gap2)
