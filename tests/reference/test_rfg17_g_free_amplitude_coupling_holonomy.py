import math
import numpy as np


def coupling_from_kappa(kappa_g):
    return kappa_g * kappa_g / 4.0


def mbar_from_kappa(kappa_g):
    return 2.0 / kappa_g


def coupling_from_mbar(mbar):
    return 1.0 / (mbar * mbar)


def coupling_from_horizon(MH, TH):
    return 1.0 / (MH * TH)


def gamma_from_local(alpha_c, omega_q, MH, TH):
    return alpha_c * omega_q / (2.0 * math.sqrt(MH * TH))


def coupling_from_local(alpha_c, omega_q, gamma_dc):
    return 4.0 * gamma_dc * gamma_dc / (alpha_c * alpha_c * omega_q * omega_q)


def test_kappa_mbar_einstein_triangle():
    for kg in (0.07, 0.3, 1.1, 2.7):
        m = mbar_from_kappa(kg)
        assert math.isclose(coupling_from_kappa(kg), coupling_from_mbar(m), rel_tol=2e-15)


def test_horizon_reduced_scale_gives_same_einstein_coupling():
    for MH, TH in ((2.0, 0.3), (7.0, 0.04), (0.8, 1.7)):
        mbar = math.sqrt(MH * TH)
        assert math.isclose(coupling_from_mbar(mbar), coupling_from_horizon(MH, TH), rel_tol=2e-15)


def test_local_gamma_horizon_binding_closes_prefactor():
    rng = np.random.default_rng(20260902)
    for _ in range(1000):
        alpha = float(rng.uniform(0.2, 2.0))
        omega = float(rng.uniform(0.1, 4.0))
        MH = float(rng.uniform(0.2, 8.0))
        TH = float(rng.uniform(0.02, 2.0))
        gamma = gamma_from_local(alpha, omega, MH, TH)
        a = coupling_from_local(alpha, omega, gamma)
        b = coupling_from_horizon(MH, TH)
        assert abs(a - b) < 5e-14 * max(1.0, abs(a), abs(b))


def test_amplitude_prefactor_is_G_free_on_horizon_surface():
    rng = np.random.default_rng(20260903)
    for _ in range(100):
        MH = float(rng.uniform(0.3, 9.0))
        TH = float(rng.uniform(0.03, 2.0))
        core = float(rng.normal())
        a = coupling_from_horizon(MH, TH) * core
        mbar = math.sqrt(MH * TH)
        b = coupling_from_mbar(mbar) * core
        assert math.isclose(a, b, rel_tol=2e-15, abs_tol=2e-15)


def test_amplitude_prefactor_is_G_free_on_local_carrier_surface():
    alpha = 0.47483961905223004
    omega = 1.37
    MH = 5.3
    TH = 0.17
    gamma = gamma_from_local(alpha, omega, MH, TH)
    core = -2.41
    local = coupling_from_local(alpha, omega, gamma) * core
    horizon = coupling_from_horizon(MH, TH) * core
    assert math.isclose(local, horizon, rel_tol=2e-15)


def test_no_numerical_Newton_constant_is_required():
    alpha = 0.47483961905223004
    omega = 0.83
    gamma = 0.12
    kappa_e = coupling_from_local(alpha, omega, gamma)
    assert kappa_e > 0.0 and math.isfinite(kappa_e)
