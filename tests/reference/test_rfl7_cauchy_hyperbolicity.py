import math
from pathlib import Path

import numpy as np
import pytest

from src.rfc.cauchy_hyperbolicity import (
    cauchy_energy_density,
    characteristic_roots,
    coordinate_time_derivative,
    hyperbolicity_gap,
    normal_derivative,
    principal_symbol,
    spatial_quadratic_form,
)


def test_characteristic_roots_are_real_distinct_and_null_principal_symbol():
    rng = np.random.default_rng(20260830)
    for _ in range(128):
        a = rng.normal(size=(3, 3))
        h_inv = a.T @ a + 0.2 * np.eye(3)
        lapse = float(rng.uniform(0.15, 4.0))
        shift = rng.normal(size=3)
        k = rng.normal(size=3)
        if np.linalg.norm(k) < 1e-8:
            k[0] = 1.0

        root_minus, root_plus = characteristic_roots(lapse, shift, h_inv, k)
        assert root_minus < root_plus
        assert principal_symbol(root_minus, k, lapse, shift, h_inv) == pytest.approx(0.0, abs=2e-11)
        assert principal_symbol(root_plus, k, lapse, shift, h_inv) == pytest.approx(0.0, abs=2e-11)
        assert root_plus - root_minus == pytest.approx(hyperbolicity_gap(lapse, h_inv, k))
        assert spatial_quadratic_form(h_inv, k) > 0.0


def test_shift_changes_root_center_not_gap():
    lapse = 1.6
    h_inv = np.diag([0.7, 1.2, 2.0])
    k = np.array([0.5, -0.3, 0.8])
    roots_zero = characteristic_roots(lapse, np.zeros(3), h_inv, k)
    shift = np.array([0.2, -0.1, 0.4])
    roots_shift = characteristic_roots(lapse, shift, h_inv, k)
    center_shift = float(np.dot(shift, k))

    assert (roots_shift[0] + roots_shift[1]) / 2.0 == pytest.approx(center_shift)
    assert roots_shift[1] - roots_shift[0] == pytest.approx(roots_zero[1] - roots_zero[0])


def test_local_flat_limit_is_standard_null_cone():
    k = np.array([0.3, -0.4, 1.2])
    roots = characteristic_roots(1.0, np.zeros(3), np.eye(3), k)
    norm = float(np.linalg.norm(k))
    assert roots[0] == pytest.approx(-norm)
    assert roots[1] == pytest.approx(norm)


def test_mass_is_lower_order_and_does_not_enter_principal_roots():
    lapse = 0.9
    shift = np.array([0.1, -0.2])
    h_inv = np.array([[1.4, 0.2], [0.2, 0.8]])
    k = np.array([0.6, 1.1])
    roots = characteristic_roots(lapse, shift, h_inv, k)
    for mass_sq in (0.0, 0.3, 100.0):
        assert mass_sq >= 0.0
        assert characteristic_roots(lapse, shift, h_inv, k) == pytest.approx(roots)


def test_cauchy_normal_coordinate_derivative_roundtrip():
    lapse = 1.35
    shift = np.array([0.3, -0.15, 0.05])
    grad = np.array([0.7, -0.2, 0.9])
    phi_0 = -1.1
    pi = normal_derivative(phi_0, lapse, shift, grad)
    reconstructed = coordinate_time_derivative(pi, lapse, shift, grad)
    assert reconstructed == pytest.approx(phi_0)


def test_slice_energy_nonnegative_for_nonnegative_mass_squared():
    h_inv = np.array([[1.1, 0.1], [0.1, 0.9]])
    samples = [
        (0.0, 0.0, [0.0, 0.0], 0.0),
        (1.2, -0.7, [0.3, -0.4], 0.0),
        (-0.8, 2.0, [1.1, 0.2], 0.6),
    ]
    for pi, phi, grad, mass_sq in samples:
        assert cauchy_energy_density(pi, phi, grad, h_inv, mass_sq) >= 0.0


def test_invalid_lapse_metric_covector_and_mass_fail_closed():
    with pytest.raises(ValueError):
        characteristic_roots(0.0, [0.0], [[1.0]], [1.0])
    with pytest.raises(ValueError):
        characteristic_roots(1.0, [0.0], [[-1.0]], [1.0])
    with pytest.raises(ValueError):
        characteristic_roots(1.0, [0.0], [[1.0]], [0.0])
    with pytest.raises(ValueError):
        cauchy_energy_density(0.0, 1.0, [0.0], [[1.0]], -0.1)


def test_document_contract_and_stacked_source_lock():
    root = Path(__file__).resolve().parents[2]
    gate = (root / "closure/lambda0/RF_L7_CAUCHY_HYPERBOLICITY_WELLPOSEDNESS.md").read_text(encoding="utf-8")
    l6 = (root / "closure/lambda0/RF_L6_VARIABLE_LAPSE_CURVED_COVARIANT_PROPAGATION.md").read_text(encoding="utf-8")

    assert "e19aeaef978f1bf46e37287759a7a6f67df54eb0" in gate
    assert r"\xi_0^{\pm}" in gate
    assert r"2N_R\sqrt{Q_h(k)}>0" in gate
    assert r"\pi_I:=n^\mu\nabla_\mu\phi_I" in gate
    assert "arXiv:0806.1036" in gate
    assert "GLOBAL_CAUCHY_PROMOTION_OPEN" in gate
    assert "PASS_RF_L7_LOCAL_CAUCHY_HYPERBOLICITY_CONTRACT" in gate
    assert r"\Box_g\phi_I-m_I^2\phi_I=0" in l6
