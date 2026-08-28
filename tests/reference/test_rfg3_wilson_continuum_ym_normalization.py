import cmath
import math

import numpy as np


def g0_squared(beta_w):
    return 6.0 / beta_w


def g_candidate(beta_w, gamma_dc, d_tau_chi):
    return 18.0 * gamma_dc**2 / (math.pi * beta_w**2 * d_tau_chi**2)


def test_project_defect_equals_three_times_normalized_su3_plaquette_defect():
    re_tr_u = 2.713
    d_project = 3.0 - re_tr_u
    d_normalized = 3.0 * (1.0 - re_tr_u / 3.0)
    assert math.isclose(d_project, d_normalized, rel_tol=1e-15, abs_tol=1e-15)


def test_wilson_beta_fixes_bare_su3_gauge_coupling():
    beta_w = 5.9
    g2 = g0_squared(beta_w)
    assert math.isclose(beta_w * g2, 6.0, rel_tol=1e-15, abs_tol=1e-15)


def test_rfg2_and_rfg3_G_forms_are_identical_after_wilson_substitution():
    beta_w = 6.2
    gamma = 0.87
    d_tau_chi = 4.7
    g2 = g0_squared(beta_w)
    g4 = g2 * g2
    epsilon_n = 0.5 * d_tau_chi
    from_rfg2 = gamma**2 * g4 / (8.0 * math.pi * epsilon_n**2)
    from_rfg3 = g_candidate(beta_w, gamma, d_tau_chi)
    assert math.isclose(from_rfg2, from_rfg3, rel_tol=1e-14, abs_tol=1e-14)


def test_beta_doubling_quarters_G_candidate():
    gamma = 0.93
    d_tau_chi = 3.8
    G0 = g_candidate(5.7, gamma, d_tau_chi)
    G1 = g_candidate(11.4, gamma, d_tau_chi)
    assert math.isclose(G1 / G0, 0.25, rel_tol=1e-14, abs_tol=1e-14)


def test_phase_rate_doubling_quarters_G_candidate():
    beta_w = 5.8
    gamma = 1.07
    G0 = g_candidate(beta_w, gamma, 2.9)
    G1 = g_candidate(beta_w, gamma, 5.8)
    assert math.isclose(G1 / G0, 0.25, rel_tol=1e-14, abs_tol=1e-14)


def test_double_copy_normalization_enters_G_quadratically():
    beta_w = 6.0
    d_tau_chi = 4.2
    G0 = g_candidate(beta_w, 1.0, d_tau_chi)
    G1 = g_candidate(beta_w, 1.5, d_tau_chi)
    assert math.isclose(G1 / G0, 2.25, rel_tol=1e-14, abs_tol=1e-14)


def test_adversarial_wrong_beta_g_relation_fails():
    beta_w = 6.0
    g2_wrong = 0.8
    defect = abs(g2_wrong - 6.0 / beta_w)
    assert defect > 0.1


def test_small_su3_plaquette_has_expected_quadratic_defect_coefficient():
    # Use T3=diag(1/2,-1/2,0), Tr(T3^2)=1/2.
    # U=exp(i x T3) has ReTr(U)=2 cos(x/2)+1.
    # Therefore 1-ReTr(U)/3 = x^2/12 + O(x^4), x=g a^2 F.
    g0 = 0.71
    a = 2.0e-3
    F = 1.3
    x = g0 * a * a * F
    re_tr = 2.0 * math.cos(x / 2.0) + 1.0
    defect = 1.0 - re_tr / 3.0
    leading = x * x / 12.0
    # At this very small x the O(x^4) term is negligible relative to x^2.
    assert math.isclose(defect, leading, rel_tol=5e-5, abs_tol=1e-16)


def test_small_plaquette_log_recovers_embedded_field_strength():
    # Same diagonal T3 embedding. Principal phases are +/- x/2,0.
    g0 = 0.64
    a = 1.0e-2
    F = -0.83
    x = g0 * a * a * F
    eigenvalues = np.array([cmath.exp(0.5j * x), cmath.exp(-0.5j * x), 1.0 + 0j])
    phases = np.angle(eigenvalues)
    recovered_x = phases[0] - phases[1]
    recovered_F = recovered_x / (g0 * a * a)
    assert math.isclose(recovered_F, F, rel_tol=1e-12, abs_tol=1e-12)
