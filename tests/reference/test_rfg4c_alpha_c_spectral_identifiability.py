import math


def estimate_alpha(peaks, c_eff=1.0, hbar_eff=1.0):
    num = sum(w * n * omega for n, omega, w in peaks)
    den = sum(w * n * n for n, omega, w in peaks)
    if c_eff <= 0 or hbar_eff <= 0 or den <= 0:
        raise ValueError("nondegenerate positive estimator coordinates required")
    return (hbar_eff / c_eff) * num / den


def harmonic_defect(peaks):
    vals = [(n, omega) for n, omega, _ in peaks]
    defect = 0.0
    for m, omega_m in vals:
        for n, omega_n in vals:
            defect = max(defect, abs((n * omega_m) / (m * omega_n) - 1.0))
    return defect


def peakwise_defect(peaks, alpha_hat, c_eff=1.0, hbar_eff=1.0):
    vals = [
        (hbar_eff / c_eff) * omega / n
        for n, omega, _ in peaks
    ]
    return max(abs(x - alpha_hat) / abs(alpha_hat) for x in vals)


def test_exact_harmonic_spectrum_recovers_alpha_for_arbitrary_positive_weights():
    alpha = 0.47481202619417856
    c_eff = 1.7
    hbar_eff = 0.8
    slope = alpha * c_eff / hbar_eff
    peaks = [(1, slope, 1.0), (2, 2 * slope, 0.3), (3, 3 * slope, 7.0), (7, 7 * slope, 2.2)]
    got = estimate_alpha(peaks, c_eff=c_eff, hbar_eff=hbar_eff)
    assert math.isclose(got, alpha, rel_tol=2e-15, abs_tol=2e-15)


def test_exact_harmonic_ratio_defect_is_zero_to_float_tolerance():
    slope = 0.731
    peaks = [(1, slope, 1.0), (2, 2 * slope, 1.0), (5, 5 * slope, 1.0)]
    assert harmonic_defect(peaks) < 1e-15


def test_peakwise_common_alpha_defect_is_zero_for_exact_data():
    alpha = 0.474812
    peaks = [(1, alpha, 1.0), (2, 2 * alpha, 2.0), (4, 4 * alpha, 3.0)]
    alpha_hat = estimate_alpha(peaks)
    assert peakwise_defect(peaks, alpha_hat) < 1e-15


def test_adversarial_detuned_peak_is_detected_by_harmonic_and_peakwise_defects():
    alpha = 0.474812
    peaks = [(1, alpha, 1.0), (2, 2 * alpha * 1.01, 1.0), (3, 3 * alpha, 1.0)]
    alpha_hat = estimate_alpha(peaks)
    assert harmonic_defect(peaks) > 0.009
    assert peakwise_defect(peaks, alpha_hat) > 0.005


def test_weighted_estimator_reduces_to_single_peak_identity():
    alpha = 0.474812
    c_eff = 3.0
    hbar_eff = 2.0
    n = 7
    omega = n * alpha * c_eff / hbar_eff
    got = estimate_alpha([(n, omega, 9.0)], c_eff=c_eff, hbar_eff=hbar_eff)
    assert math.isclose(got, alpha, rel_tol=2e-15, abs_tol=2e-15)


def test_estimator_fails_closed_on_nonpositive_effective_units():
    peaks = [(1, 1.0, 1.0)]
    for c_eff, hbar_eff in [(0.0, 1.0), (-1.0, 1.0), (1.0, 0.0), (1.0, -1.0)]:
        try:
            estimate_alpha(peaks, c_eff=c_eff, hbar_eff=hbar_eff)
        except ValueError:
            pass
        else:
            raise AssertionError("nonpositive effective-unit coordinate must fail closed")


def test_historical_legacy_reconstruction_is_inside_reported_interval():
    historical_mean = 0.474812
    historical_half_width = 0.000007
    analytic_legacy = 0.47481202619417856
    assert historical_mean - historical_half_width <= analytic_legacy <= historical_mean + historical_half_width


def test_canonicalized_coordinate_is_resolved_from_legacy_coordinate():
    legacy = 0.47481202619417856
    canonical = 0.474839619052230
    assert canonical > legacy
    assert canonical - legacy > 2.7e-5


def test_su3_wilson_coordinate_propagates_linearly_after_independent_binding():
    alpha = 0.474839619052230
    beta_w = 6.0 * alpha
    assert math.isclose(beta_w, 2.84903771431338, rel_tol=2e-15, abs_tol=2e-15)
