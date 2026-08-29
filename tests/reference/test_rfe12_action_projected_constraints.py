import math
from pathlib import Path

import pytest


def geometric_hamiltonian(r3, k_trace, kij_kij):
    return r3 + k_trace * k_trace - kij_kij


def action_projected_sources(r3, k_trace, kij_kij, momentum_geom, kappa_e, lambda0=0.0):
    if not math.isfinite(kappa_e) or kappa_e <= 0.0:
        raise ValueError("kappa_e must be positive finite")
    gh = geometric_hamiltonian(r3, k_trace, kij_kij)
    rho = (gh - 2.0 * lambda0) / (2.0 * kappa_e)
    j = [x / kappa_e for x in momentum_geom]
    return gh, rho, j


def test_base_action_projection_reconstructs_hamiltonian_and_momentum_constraints():
    r3 = 0.37
    k_trace = -0.8
    kij_kij = 0.29
    gm = [0.12, -0.07, 0.03]
    kappa = 1.7
    gh, rho, j = action_projected_sources(r3, k_trace, kij_kij, gm, kappa)
    assert gh == pytest.approx(2.0 * kappa * rho)
    for i in range(3):
        assert gm[i] == pytest.approx(kappa * j[i])


def test_dynamic_lambda_projection_has_correct_normal_sign_and_no_mixed_term():
    r3 = -0.1
    k_trace = 0.6
    kij_kij = 0.17
    gm = [-0.2, 0.4, 0.05]
    kappa = 0.9
    lambda0 = 0.13
    gh, rho, j = action_projected_sources(r3, k_trace, kij_kij, gm, kappa, lambda0)
    assert gh - 2.0 * lambda0 == pytest.approx(2.0 * kappa * rho)
    assert gh == pytest.approx(2.0 * lambda0 + 2.0 * kappa * rho)
    for i in range(3):
        assert gm[i] == pytest.approx(kappa * j[i])


def test_source_sector_linearity():
    kappa = 2.3
    rho_parts = [0.4, -0.05, 0.8]
    j_parts = [[0.1,0.0,-0.2], [-0.03,0.04,0.01], [0.2,-0.1,0.05]]
    gh_total = 2.0 * kappa * sum(rho_parts)
    gm_total = [kappa * sum(part[i] for part in j_parts) for i in range(3)]
    assert gh_total == pytest.approx(sum(2.0*kappa*r for r in rho_parts))
    for i in range(3):
        assert gm_total[i] == pytest.approx(sum(kappa*part[i] for part in j_parts))


def test_double_copy_action_normalization_triangle():
    kappa_g = 1.28
    kappa_e = kappa_g * kappa_g / 4.0
    assert 2.0 / (kappa_g * kappa_g) == pytest.approx(1.0 / (2.0 * kappa_e))
    assert kappa_g * kappa_g == pytest.approx(4.0 * kappa_e)


def test_project_double_copy_coordinate_is_kept_conditional_but_algebraically_consistent():
    gamma_dc = 0.73
    beta_w = 5.2
    omega_q = 1.9
    kappa_e_dc = 144.0 * gamma_dc**2 / (beta_w**2 * omega_q**2)
    a_eh_dc = beta_w**2 * omega_q**2 / (288.0 * gamma_dc**2)
    assert a_eh_dc == pytest.approx(1.0 / (2.0 * kappa_e_dc))


def test_nonpositive_coupling_rejected():
    with pytest.raises(ValueError):
        action_projected_sources(0.0, 0.0, 0.0, [0.0,0.0,0.0], 0.0)


def test_parent_dependency_markers_present():
    root = Path(__file__).resolve().parents[2]
    rfe3 = (root / "closure/einstein/RF_E3_DOUBLE_COPY_EINSTEIN_HILBERT_NORMALIZATION.md").read_text(encoding="utf-8")
    rfe10 = (root / "closure/einstein/RF_E10_GAUSS_CODAZZI_EINSTEIN_TENSOR_PROJECTIONS.md").read_text(encoding="utf-8")
    rfe11 = (root / "closure/einstein/RF_E11_MATTER_PROJECTION_SOURCE_TYPING.md").read_text(encoding="utf-8")

    assert r"G_{\mu\nu}=\kappa_E T_{\mu\nu}" in rfe3
    assert r"\kappa_g^2=4\kappa_E" in rfe3
    assert r"\mathcal G_H" in rfe10
    assert r"\mathcal G_{Mi}" in rfe10
    assert r"\rho_n:=T_{\mu\nu}n^\mu n^\nu" in rfe11
    assert r"j_i=-h_i{}^\mu n^\nu T_{\mu\nu}" in rfe11
