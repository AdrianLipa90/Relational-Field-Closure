import math


ALPHA_ARCHIVE = 0.474812
HBAR_EFF = 0.892345
C_EFF = 0.956712


def alpha_from_energy(energy, occupation, hbar_eff=HBAR_EFF):
    return energy / (occupation * hbar_eff)


def alpha_from_spectrum(omega, mode_number, hbar_eff=HBAR_EFF, c_eff=C_EFF):
    return omega * hbar_eff / (mode_number * c_eff)


def epsilon_n(phase_rate):
    return 0.5 * phase_rate


def alpha_from_carrier(phase_rate, soldering, occupation, hbar_eff=HBAR_EFF):
    return soldering * epsilon_n(phase_rate) / (occupation * hbar_eff)


def required_soldering(alpha_c, phase_rate, occupation, hbar_eff=HBAR_EFF):
    return 2.0 * alpha_c * occupation * hbar_eff / phase_rate


def test_historical_energy_and_spectral_coordinates_recover_same_alpha():
    n = 4.0
    energy = ALPHA_ARCHIVE * n * HBAR_EFF
    omega = n * ALPHA_ARCHIVE * C_EFF / HBAR_EFF
    alpha_e = alpha_from_energy(energy, n)
    alpha_w = alpha_from_spectrum(omega, n)
    assert math.isclose(alpha_e, ALPHA_ARCHIVE, rel_tol=0.0, abs_tol=1e-15)
    assert math.isclose(alpha_w, ALPHA_ARCHIVE, rel_tol=0.0, abs_tol=1e-15)
    assert math.isclose(alpha_e, alpha_w, rel_tol=0.0, abs_tol=1e-15)


def test_detuned_spectral_peak_is_detected():
    n = 3.0
    energy = ALPHA_ARCHIVE * n * HBAR_EFF
    omega = n * ALPHA_ARCHIVE * C_EFF / HBAR_EFF
    alpha_e = alpha_from_energy(energy, n)
    alpha_w_detuned = alpha_from_spectrum(omega * 1.002, n)
    defect = abs(alpha_e - alpha_w_detuned) / abs(alpha_e)
    assert defect > 1e-3


def test_source_carrier_formula_is_exact_for_independent_coordinates():
    phase_rate = 0.83
    soldering = 1.17
    occupation = 2.5
    alpha_n = alpha_from_carrier(phase_rate, soldering, occupation)
    energy_kernel = soldering * epsilon_n(phase_rate)
    alpha_e = alpha_from_energy(energy_kernel, occupation)
    assert math.isclose(alpha_n, alpha_e, rel_tol=0.0, abs_tol=1e-15)


def test_fixed_soldering_detects_phase_rate_mismatch_against_archive_alpha():
    occupation = 1.0
    soldering = 1.0
    phase_rate = 0.8
    alpha_n = alpha_from_carrier(phase_rate, soldering, occupation)
    defect = abs(alpha_n - ALPHA_ARCHIVE) / ALPHA_ARCHIVE
    assert defect > 0.05


def test_required_soldering_is_an_exact_inverse_diagnostic():
    occupation = 2.0
    phase_rate = 0.91
    s_req = required_soldering(ALPHA_ARCHIVE, phase_rate, occupation)
    recovered = alpha_from_carrier(phase_rate, s_req, occupation)
    assert math.isclose(recovered, ALPHA_ARCHIVE, rel_tol=0.0, abs_tol=1e-15)


def test_occupation_detuning_breaks_consistency_when_energy_and_peak_are_fixed():
    n = 5.0
    energy = ALPHA_ARCHIVE * n * HBAR_EFF
    omega = n * ALPHA_ARCHIVE * C_EFF / HBAR_EFF
    alpha_e_wrong_n = alpha_from_energy(energy, n + 1.0)
    alpha_w_wrong_n = alpha_from_spectrum(omega, n + 1.0)
    assert math.isclose(alpha_e_wrong_n, alpha_w_wrong_n, rel_tol=0.0, abs_tol=1e-15)
    assert not math.isclose(alpha_e_wrong_n, ALPHA_ARCHIVE, rel_tol=0.0, abs_tol=1e-6)
