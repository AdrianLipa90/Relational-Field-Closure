import math


def test_phase_clock_area_scale():
    c = 10.0
    omega = 4.0
    a_fs = 0.7
    ell = c / abs(omega)
    area_a = ell * ell * a_fs
    area_b = (c * c / (omega * omega)) * a_fs
    assert math.isclose(area_a, area_b, rel_tol=1e-15)


def test_xi_area_and_rate_forms_match():
    j = 0.45
    c = 8.0
    omega = 2.5
    a_fs = 0.9
    area = (c * c / (omega * omega)) * a_fs
    xi_area = j / area
    xi_rate = (j / a_fs) * (omega / c) ** 2
    assert math.isclose(xi_area, xi_rate, rel_tol=1e-15)


def test_tir_kappa_form():
    info_bits = 0.55
    kappa = math.log(2.0) / (24.0 * math.pi)
    c = 3.0
    omega = 1.2
    a_fs = 0.65
    j = math.log(2.0) * info_bits
    xi_j = (j / a_fs) * (omega / c) ** 2
    xi_k = (24.0 * math.pi * kappa * info_bits / a_fs) * (omega / c) ** 2
    assert math.isclose(xi_j, xi_k, rel_tol=1e-15)


def test_full_cp1_lambda_information_form():
    alpha_i = 0.8
    info_bits = 0.4
    kappa = math.log(2.0) / (24.0 * math.pi)
    c = 5.5
    omega = 2.2
    lambda_general = alpha_i * (24.0 * math.pi * kappa * info_bits / math.pi) * (omega / c) ** 2
    lambda_full = 24.0 * alpha_i * kappa * info_bits * (omega / c) ** 2
    assert math.isclose(lambda_general, lambda_full, rel_tol=1e-15)


def test_energy_phase_length_equivalence():
    hbar = 1.054_571_817e-34
    c = 299_792_458.0
    omega = 9.1e13
    energy = hbar * abs(omega)
    ell_phase = c / abs(omega)
    ell_energy = hbar * c / energy
    assert math.isclose(ell_phase, ell_energy, rel_tol=1e-15)


def test_projective_spinor_cycle_half_ratio():
    ell = 2.75
    assert math.isclose((2.0 * math.pi * ell) / (4.0 * math.pi * ell), 0.5, rel_tol=0.0, abs_tol=1e-15)
