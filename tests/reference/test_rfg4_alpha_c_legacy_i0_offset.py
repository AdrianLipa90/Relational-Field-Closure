import math


ARCHIVE_ALPHA_C = 0.474812
I0_LEGACY = 0.009
L3 = 7.0
PHI = (1.0 + math.sqrt(5.0)) / 2.0
KAPPA = math.log(2.0) / (24.0 * math.pi)


def alpha_base(kappa=KAPPA):
    return math.log(PHI) - kappa * math.log(2.0)


def alpha_legacy_reconstruction(i0=I0_LEGACY, kappa=KAPPA, l3=L3):
    return alpha_base(kappa) - (kappa - i0) / l3


def test_legacy_i0_and_canonical_kappa_have_expected_displacement():
    delta_i = KAPPA - I0_LEGACY
    assert math.isclose(delta_i, 0.00019315000636048463, rel_tol=0.0, abs_tol=1e-15)
    assert math.isclose(delta_i / L3, 2.7592858051497805e-05, rel_tol=0.0, abs_tol=1e-15)


def test_recovered_legacy_expression_matches_archived_six_decimal_coordinate():
    candidate = alpha_legacy_reconstruction()
    assert round(candidate, 6) == ARCHIVE_ALPHA_C
    assert abs(candidate - ARCHIVE_ALPHA_C) < 3e-8


def test_recovered_legacy_expression_has_small_relative_residual():
    candidate = alpha_legacy_reconstruction()
    relative = abs(candidate - ARCHIVE_ALPHA_C) / ARCHIVE_ALPHA_C
    assert relative < 6e-8


def test_canonical_reduction_closes_legacy_offset():
    candidate = alpha_legacy_reconstruction(i0=KAPPA)
    assert math.isclose(candidate, alpha_base(), rel_tol=0.0, abs_tol=1e-15)
    assert math.isclose(candidate, 0.47483961905223004, rel_tol=0.0, abs_tol=1e-15)


def test_canonical_candidate_propagates_to_g_and_wilson_beta():
    alpha_c = alpha_base()
    g = 1.0 / math.sqrt(alpha_c)
    beta_w = 6.0 * alpha_c
    assert math.isclose(g, 1.4511975150435787, rel_tol=0.0, abs_tol=1e-14)
    assert math.isclose(beta_w, 2.8490377143133805, rel_tol=0.0, abs_tol=1e-14)


def test_adversarial_offset_sign_fails_archive_reconstruction():
    wrong = alpha_base() + (KAPPA - I0_LEGACY) / L3
    assert round(wrong, 6) != ARCHIVE_ALPHA_C
