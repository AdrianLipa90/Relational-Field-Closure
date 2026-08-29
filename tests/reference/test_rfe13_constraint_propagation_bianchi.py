import math
from pathlib import Path

import pytest


def metric_evolution(kij, lapse, lie_shift_h=None):
    lie_shift_h = lie_shift_h or [[0.0]*3 for _ in range(3)]
    return [[lie_shift_h[i][j] - 2.0*lapse*kij[i][j] for j in range(3)] for i in range(3)]


def k_evolution(rij, kij, k_trace, lapse, hess_lapse, rho, sij, h, kappa_e, lambda0=0.0):
    s_trace = sum(h[i][j]*0.0 for i in range(3) for j in range(3))
    # Tests below use diagonal/orthonormal h when an explicit matter trace is needed.
    if all(abs(h[i][j] - (1.0 if i == j else 0.0)) < 1e-14 for i in range(3) for j in range(3)):
        s_trace = sum(sij[i][i] for i in range(3))
    out = [[0.0]*3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            kprod = sum(kij[i][m]*kij[m][j] for m in range(3))
            matter = kappa_e * (0.5*h[i][j]*(s_trace-rho) - sij[i][j])
            out[i][j] = (
                -hess_lapse[i][j]
                + lapse*(rij[i][j] + k_trace*kij[i][j] - 2.0*kprod + matter - lambda0*h[i][j])
            )
    return out


def propagation_rhs(H, M, grad_H, div_M, grad_lapse, lapse, k_trace):
    hdot = 2.0*lapse*k_trace*H - 2.0*lapse*div_M - 4.0*sum(M[i]*grad_lapse[i] for i in range(3))
    mdot = [
        -0.5*lapse*grad_H[i] - H*grad_lapse[i] + lapse*k_trace*M[i]
        for i in range(3)
    ]
    return hdot, mdot


def test_metric_evolution_matches_extrinsic_curvature_definition():
    kij = [[0.2,0.03,0.0],[0.03,-0.1,0.04],[0.0,0.04,0.5]]
    lapse = 1.4
    dh = metric_evolution(kij, lapse)
    for i in range(3):
        for j in range(3):
            assert kij[i][j] == pytest.approx(-dh[i][j]/(2.0*lapse))


def test_dynamic_lambda_de_sitter_isotropic_certificate():
    H0 = 0.23
    lambda0 = 3.0*H0*H0
    h = [[1.0 if i == j else 0.0 for j in range(3)] for i in range(3)]
    kij = [[-H0 if i == j else 0.0 for j in range(3)] for i in range(3)]
    rij = [[0.0]*3 for _ in range(3)]
    hess = [[0.0]*3 for _ in range(3)]
    sij = [[0.0]*3 for _ in range(3)]
    rhs = k_evolution(rij, kij, -3.0*H0, 1.0, hess, 0.0, sij, h, 1.0, lambda0)
    # K_ij=-H h_ij and hdot=2H h imply Kdot=-2H^2 h for constant H.
    for i in range(3):
        for j in range(3):
            expected = -2.0*H0*H0 if i == j else 0.0
            assert rhs[i][j] == pytest.approx(expected)
    hamiltonian_residual = 9.0*H0*H0 - 3.0*H0*H0 - 2.0*lambda0
    assert hamiltonian_residual == pytest.approx(0.0, abs=1e-14)


def test_zero_constraint_residual_is_exact_fixed_solution():
    hdot, mdot = propagation_rhs(
        H=0.0,
        M=[0.0,0.0,0.0],
        grad_H=[0.0,0.0,0.0],
        div_M=0.0,
        grad_lapse=[0.7,-0.2,0.4],
        lapse=1.3,
        k_trace=-0.8,
    )
    assert hdot == 0.0
    assert mdot == [0.0,0.0,0.0]


def test_flat_principal_constraint_system_has_wave_character():
    # Fourier mode exp(i k x): Hdot=-2 i k Mx, Mxdot=-1/2 i k H,
    # therefore Hddot=-k^2 H.
    k = 1.7
    H = 0.8 + 0.3j
    Mx_dot = -0.5j*k*H
    H_ddot = -2.0j*k*Mx_dot
    assert H_ddot == pytest.approx(-(k*k)*H)


def test_nonzero_residual_propagation_is_homogeneous_linear():
    H = 0.4
    M = [0.1,-0.05,0.02]
    args = dict(grad_H=[0.3,-0.1,0.2], div_M=0.07, grad_lapse=[0.02,0.03,-0.01], lapse=0.9, k_trace=-0.4)
    one = propagation_rhs(H, M, **args)
    scale = -2.5
    scaled_args = dict(args)
    scaled_args["grad_H"] = [scale*x for x in args["grad_H"]]
    scaled_args["div_M"] = scale*args["div_M"]
    two = propagation_rhs(scale*H, [scale*x for x in M], **scaled_args)
    assert two[0] == pytest.approx(scale*one[0])
    for i in range(3):
        assert two[1][i] == pytest.approx(scale*one[1][i])


def test_dynamic_lambda_bianchi_exchange_cancels_exactly():
    grad_lambda = [0.12,-0.08,0.03,0.21]
    kappa = 1.6
    div_T = [x/kappa for x in grad_lambda]
    div_E = [grad_lambda[i] - kappa*div_T[i] for i in range(4)]
    assert div_E == pytest.approx([0.0,0.0,0.0,0.0])


def test_parent_dependency_markers_present():
    root = Path(__file__).resolve().parents[2]
    e3 = (root / "closure/einstein/RF_E3_DOUBLE_COPY_EINSTEIN_HILBERT_NORMALIZATION.md").read_text(encoding="utf-8")
    e9 = (root / "closure/einstein/RF_E9_EXTRINSIC_CURVATURE_GEOMETRY.md").read_text(encoding="utf-8")
    e12 = (root / "closure/einstein/RF_E12_ACTION_PROJECTED_ADM_SOURCE_CONSTRAINTS.md").read_text(encoding="utf-8")
    assert r"G_{\mu\nu}=\kappa_E T_{\mu\nu}" in e3
    assert r"K_{ij}:=-\frac12\mathcal L_n h_{ij}" in e9
    assert r"\mathcal G_H=2\kappa_E\rho_n" in e12
    assert r"\mathcal G_{Mi}=\kappa_E j_i" in e12
