import pytest

from rfc.global_einstein_carrier import (
    EinsteinPatch,
    GlobalEinsteinCarrierError,
    TensorOverlap,
    certify_global_einstein_carrier,
)


ETA = (
    (-1.0, 0.0, 0.0, 0.0),
    (0.0, 1.0, 0.0, 0.0),
    (0.0, 0.0, 1.0, 0.0),
    (0.0, 0.0, 0.0, 1.0),
)
ZERO = tuple(tuple(0.0 for _ in range(4)) for _ in range(4))
IDENTITY = (
    (1.0, 0.0, 0.0, 0.0),
    (0.0, 1.0, 0.0, 0.0),
    (0.0, 0.0, 1.0, 0.0),
    (0.0, 0.0, 0.0, 1.0),
)
SPATIAL_ROTATION = (
    (1.0, 0.0, 0.0, 0.0),
    (0.0, 0.0, -1.0, 0.0),
    (0.0, 1.0, 0.0, 0.0),
    (0.0, 0.0, 0.0, 1.0),
)


def patch(name: str, *, g=ETA, G=ZERO, T=ZERO, lam=0.0, kappa=2.0):
    return EinsteinPatch(name, g, G, T, lam, kappa)


def test_single_patch_promotes_only_with_e25_and_coverage_witnesses():
    cert = certify_global_einstein_carrier(
        [patch("p")],
        [],
        shared_atlas_certified=True,
        domain_coverage_certified=True,
    )
    assert cert.global_einstein_carrier
    assert cert.local_einstein_equations
    assert cert.tensor_overlap_gluing
    assert cert.global_hyperbolicity == "OPEN_SEPARATE_RF_L7_GATE"


def test_missing_domain_coverage_keeps_global_promotion_open():
    cert = certify_global_einstein_carrier(
        [patch("p")],
        [],
        shared_atlas_certified=True,
        domain_coverage_certified=False,
    )
    assert not cert.global_einstein_carrier
    assert cert.shared_atlas_certified
    assert not cert.domain_coverage_certified


def test_missing_e25_parent_keeps_global_promotion_open():
    cert = certify_global_einstein_carrier(
        [patch("p")],
        [],
        shared_atlas_certified=False,
        domain_coverage_certified=True,
    )
    assert not cert.global_einstein_carrier


def test_two_patch_spatial_rotation_glues_metric_and_zero_sources():
    cert = certify_global_einstein_carrier(
        [patch("p"), patch("q")],
        [TensorOverlap("p", "q", SPATIAL_ROTATION)],
        shared_atlas_certified=True,
        domain_coverage_certified=True,
    )
    assert cert.patch_count == 2
    assert cert.overlap_count == 1
    assert cert.max_local_residual == pytest.approx(0.0)
    assert cert.max_overlap_residual == pytest.approx(0.0)
    assert cert.global_einstein_carrier


def test_nonzero_local_einstein_residual_fails_closed():
    bad_G = (
        (1.0, 0.0, 0.0, 0.0),
        (0.0, 0.0, 0.0, 0.0),
        (0.0, 0.0, 0.0, 0.0),
        (0.0, 0.0, 0.0, 0.0),
    )
    with pytest.raises(GlobalEinsteinCarrierError, match="Einstein residual"):
        certify_global_einstein_carrier([patch("p", G=bad_G)], [])


def test_exact_nonvacuum_patch_passes_local_equation():
    stress = (
        (2.0, 0.0, 0.0, 0.0),
        (0.0, 1.0, 0.0, 0.0),
        (0.0, 0.0, 3.0, 0.0),
        (0.0, 0.0, 0.0, 4.0),
    )
    einstein = tuple(tuple(2.0 * stress[i][j] for j in range(4)) for i in range(4))
    cert = certify_global_einstein_carrier(
        [patch("p", G=einstein, T=stress, kappa=2.0)],
        [],
    )
    assert cert.max_local_residual == pytest.approx(0.0)


def test_cosmological_term_is_included_in_patch_residual():
    lam = 0.25
    einstein = tuple(tuple(-lam * ETA[i][j] for j in range(4)) for i in range(4))
    cert = certify_global_einstein_carrier([patch("p", G=einstein, lam=lam)], [])
    assert cert.max_local_residual == pytest.approx(0.0)


def test_patchwise_cosmological_constant_mismatch_fails():
    with pytest.raises(GlobalEinsteinCarrierError, match="cosmological constant"):
        certify_global_einstein_carrier(
            [patch("p", lam=0.0), patch("q", lam=0.1)],
            [TensorOverlap("p", "q", IDENTITY)],
        )


def test_patchwise_kappa_mismatch_fails():
    with pytest.raises(GlobalEinsteinCarrierError, match="kappa_e"):
        certify_global_einstein_carrier(
            [patch("p", kappa=2.0), patch("q", kappa=3.0)],
            [TensorOverlap("p", "q", IDENTITY)],
        )


def test_metric_overlap_mismatch_fails_closed():
    bad_metric = (
        (-2.0, 0.0, 0.0, 0.0),
        (0.0, 1.0, 0.0, 0.0),
        (0.0, 0.0, 1.0, 0.0),
        (0.0, 0.0, 0.0, 1.0),
    )
    with pytest.raises(GlobalEinsteinCarrierError, match="metric pullback"):
        certify_global_einstein_carrier(
            [patch("p"), patch("q", g=bad_metric)],
            [TensorOverlap("p", "q", IDENTITY)],
        )


def test_tensor_overlap_mismatch_fails_closed_even_when_each_patch_solves_locally():
    t_p = (
        (1.0, 0.0, 0.0, 0.0),
        (0.0, 1.0, 0.0, 0.0),
        (0.0, 0.0, 1.0, 0.0),
        (0.0, 0.0, 0.0, 1.0),
    )
    t_q = (
        (2.0, 0.0, 0.0, 0.0),
        (0.0, 1.0, 0.0, 0.0),
        (0.0, 0.0, 1.0, 0.0),
        (0.0, 0.0, 0.0, 1.0),
    )
    G_p = tuple(tuple(2.0 * t_p[i][j] for j in range(4)) for i in range(4))
    G_q = tuple(tuple(2.0 * t_q[i][j] for j in range(4)) for i in range(4))
    with pytest.raises(GlobalEinsteinCarrierError, match="Einstein pullback|stress pullback"):
        certify_global_einstein_carrier(
            [patch("p", G=G_p, T=t_p), patch("q", G=G_q, T=t_q)],
            [TensorOverlap("p", "q", IDENTITY)],
        )


def test_disconnected_multi_patch_atlas_fails_closed():
    with pytest.raises(GlobalEinsteinCarrierError, match="disconnected"):
        certify_global_einstein_carrier([patch("p"), patch("q")], [])


@pytest.mark.parametrize("bad_kappa", [0.0, -1.0, float("inf"), float("nan")])
def test_invalid_kappa_fails_closed(bad_kappa):
    with pytest.raises(GlobalEinsteinCarrierError):
        patch("p", kappa=bad_kappa)


def test_singular_overlap_jacobian_fails_closed():
    singular = (
        (1.0, 0.0, 0.0, 0.0),
        (0.0, 1.0, 0.0, 0.0),
        (0.0, 0.0, 0.0, 0.0),
        (0.0, 0.0, 0.0, 1.0),
    )
    with pytest.raises(GlobalEinsteinCarrierError, match="invertible"):
        TensorOverlap("p", "q", singular)


def test_nonsymmetric_patch_tensor_fails_closed():
    nonsymmetric = (
        (-1.0, 1.0, 0.0, 0.0),
        (0.0, 1.0, 0.0, 0.0),
        (0.0, 0.0, 1.0, 0.0),
        (0.0, 0.0, 0.0, 1.0),
    )
    with pytest.raises(GlobalEinsteinCarrierError, match="symmetry"):
        patch("p", g=nonsymmetric)
