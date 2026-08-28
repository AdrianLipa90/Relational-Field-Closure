import math


ARCHIVE_ALPHA_C = 0.474812
I0_LEGACY = 0.009
KAPPA = math.log(2.0) / (24.0 * math.pi)
PHI_EXACT = (1.0 + math.sqrt(5.0)) / 2.0
PHI_CIEL_2025 = 1.618034
L3 = 7.0

DEFINITE_KERNEL_SHA256 = "ba1f2ce6b6f8cc0c716a0c5b0cafceabd1a569e7374b6f8a50326a09508c9fcc"
GEOMETRIA_SHA256 = "720e87f3073bdc27490d95f7e5172c4efc7a936b8b62b82a624502515677ca02"
REFACTORED_DEFINITE_KERNEL_SHA256 = "a9d810e0e7cbdf0c39cf486c8d2b16b327a75270ea14ff0daa9e6a3535405fef"


def alpha_reconstruction(phi=PHI_EXACT, i0=I0_LEGACY, l3=L3):
    return math.log(phi) - KAPPA * math.log(2.0) - (KAPPA - i0) / l3


def test_frozen_source_hashes_are_content_addressed():
    for digest in (
        DEFINITE_KERNEL_SHA256,
        GEOMETRIA_SHA256,
        REFACTORED_DEFINITE_KERNEL_SHA256,
    ):
        assert len(digest) == 64
        int(digest, 16)
    assert len({DEFINITE_KERNEL_SHA256, GEOMETRIA_SHA256, REFACTORED_DEFINITE_KERNEL_SHA256}) == 3


def test_exact_phi_reconstructs_archive_at_six_decimals():
    candidate = alpha_reconstruction(PHI_EXACT)
    assert round(candidate, 6) == ARCHIVE_ALPHA_C
    assert math.isclose(candidate, 0.47481202619417856, rel_tol=0.0, abs_tol=1e-15)


def test_historical_ciel_phi_precision_reconstructs_same_archive_coordinate():
    candidate = alpha_reconstruction(PHI_CIEL_2025)
    assert round(candidate, 6) == ARCHIVE_ALPHA_C
    assert math.isclose(candidate, 0.47481203314712583, rel_tol=0.0, abs_tol=1e-15)


def test_phi_precision_shift_is_below_one_hundred_millionth():
    shift = abs(alpha_reconstruction(PHI_CIEL_2025) - alpha_reconstruction(PHI_EXACT))
    assert shift < 1e-8
    assert math.isclose(shift, 6.952947273486387e-09, rel_tol=0.0, abs_tol=1e-16)


def test_l3_is_locally_selective_for_archived_six_decimal_coordinate():
    matches = []
    for l_value in range(5, 11):
        candidate = alpha_reconstruction(PHI_EXACT, l3=float(l_value))
        if round(candidate, 6) == ARCHIVE_ALPHA_C:
            matches.append(l_value)
    assert matches == [7]


def test_canonical_information_limit_removes_structural_depth_offset():
    for l_value in (5.0, 7.0, 10.0):
        canonical = alpha_reconstruction(PHI_EXACT, i0=KAPPA, l3=l_value)
        expected = math.log(PHI_EXACT) - KAPPA * math.log(2.0)
        assert math.isclose(canonical, expected, rel_tol=0.0, abs_tol=1e-15)
