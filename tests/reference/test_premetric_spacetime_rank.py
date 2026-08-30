import math

import pytest

from src.rfc.premetric_spacetime_rank import (
    I2,
    PAULI_BASIS,
    PremetricTransversalityError,
    basis_pairing_matrix,
    canonical_lift,
    certificate,
    dual_coordinates,
    reconstruct,
    spatial_projector,
    temporal_projector,
    trace,
)


def test_dual_pauli_identity_pairing_closes_four_rank():
    assert basis_pairing_matrix() == (
        (1.0, 0.0, 0.0, 0.0),
        (0.0, 1.0, 0.0, 0.0),
        (0.0, 0.0, 1.0, 0.0),
        (0.0, 0.0, 0.0, 1.0),
    )


def test_trace_covector_annihilates_all_spatial_pauli_generators():
    for sigma in PAULI_BASIS[1:]:
        assert trace(sigma) == 0j
        assert dual_coordinates(sigma)[0] == 0.0


def test_spatial_dual_covectors_annihilate_identity_direction():
    assert dual_coordinates(I2) == (1.0, 0.0, 0.0, 0.0)


def test_temporal_and_spatial_projectors_are_complementary():
    a = reconstruct((2.0, -3.0, 5.0, 7.0))
    pt = temporal_projector(a)
    ps = spatial_projector(a)
    assert reconstruct(
        tuple(x + y for x, y in zip(dual_coordinates(pt), dual_coordinates(ps), strict=True))
    ) == a
    assert dual_coordinates(pt) == (2.0, 0.0, 0.0, 0.0)
    assert dual_coordinates(ps) == (0.0, -3.0, 5.0, 7.0)


def test_certificate_passes_all_premetric_transversality_checks():
    cert = certificate()
    assert cert.pairing_identity
    assert cert.temporal_kills_spatial
    assert cert.spatial_kills_temporal
    assert cert.projector_reconstruction
    assert cert.four_volume_nonzero


def test_worldline_firewall_radial_lift_can_have_spatial_components():
    x = canonical_lift(8.0, (0.25, -0.5, 0.125))
    coords = dual_coordinates(x)
    assert coords[0] == 4.0
    assert coords[1:] == (1.0, -2.0, 0.5)
    assert any(abs(v) > 0.0 for v in coords[1:])


def test_canonical_lift_trace_recovers_positive_scale():
    x = canonical_lift(9.0, (0.0, 0.0, 0.0))
    assert math.isclose(trace(x).real, 9.0, rel_tol=0.0, abs_tol=1e-15)


def test_fail_closed_nonhermitian_nonfinite_and_outside_bloch_inputs():
    with pytest.raises(PremetricTransversalityError):
        dual_coordinates(((1.0 + 0j, 1.0 + 0j), (0j, 1.0 + 0j)))
    with pytest.raises(PremetricTransversalityError):
        reconstruct((1.0, 2.0, float("nan"), 4.0))
    with pytest.raises(PremetricTransversalityError):
        canonical_lift(1.0, (2.0, 0.0, 0.0))
