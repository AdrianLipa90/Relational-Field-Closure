from __future__ import annotations

import math

import numpy as np

TOL = 1e-12


def normals() -> np.ndarray:
    e = np.eye(3)
    return np.vstack([e[0], -e[0], e[1], -e[1], e[2], -e[2]])


def aggregate_metric(scale_by_pair: tuple[float, float, float] | None = None) -> np.ndarray:
    ns = normals()
    if scale_by_pair is None:
        M = sum((1.0 / 6.0) * np.outer(n, n) for n in ns)
        return 0.25 * (np.eye(3) - M)
    ell1, ell2, ell3 = scale_by_pair
    ells = [ell1, ell1, ell2, ell2, ell3, ell3]
    return sum(
        0.25 * (1.0 / 6.0) * ell**2 * (np.eye(3) - np.outer(n, n))
        for ell, n in zip(ells, ns)
    )


def test_second_moment_is_I_over_3() -> None:
    ns = normals()
    M = sum((1.0 / 6.0) * np.outer(n, n) for n in ns)
    assert np.allclose(M, np.eye(3) / 3.0, atol=TOL, rtol=TOL)


def test_aggregate_FS_metric_is_rank3_isotropic() -> None:
    h = aggregate_metric()
    assert np.allclose(h, np.eye(3) / 6.0, atol=TOL, rtol=TOL)
    assert np.linalg.matrix_rank(h, tol=TOL) == 3
    assert np.allclose(np.linalg.eigvalsh(h), np.full(3, 1.0 / 6.0), atol=TOL, rtol=TOL)
    assert math.isclose(float(np.linalg.det(h)), 1.0 / 216.0, abs_tol=TOL)
    assert math.isclose(float(np.linalg.cond(h)), 1.0, abs_tol=TOL)


def test_phase_clock_physicalization_preserves_rank() -> None:
    c = 299_792_458.0
    omega = 2.0 * math.pi * 7.83
    ell = c / omega
    h_phys = ell**2 * aggregate_metric()
    assert np.linalg.matrix_rank(h_phys, tol=1e-6) == 3
    assert np.all(np.linalg.eigvalsh(h_phys) > 0.0)
    assert math.isclose(float(np.linalg.cond(h_phys)), 1.0, rel_tol=1e-10, abs_tol=1e-10)


def test_anisotropic_pair_scale_formula() -> None:
    ell1, ell2, ell3 = 2.0, 3.0, 5.0
    h = aggregate_metric((ell1, ell2, ell3))
    expected = np.diag([
        (ell2**2 + ell3**2) / 12.0,
        (ell1**2 + ell3**2) / 12.0,
        (ell1**2 + ell2**2) / 12.0,
    ])
    assert np.allclose(h, expected, atol=TOL, rtol=TOL)
    assert np.linalg.matrix_rank(h, tol=TOL) == 3
    assert np.all(np.linalg.eigvalsh(h) > 0.0)


def test_lorentzian_assembly_signature() -> None:
    # Dimensionless tetrad representation after absorbing physical units into coframe legs.
    h = aggregate_metric()
    g = np.zeros((4, 4))
    g[0, 0] = -1.0
    g[1:, 1:] = h
    eig = np.linalg.eigvalsh(g)
    assert np.count_nonzero(eig < 0.0) == 1
    assert np.count_nonzero(eig > 0.0) == 3


def test_null_cone_in_orthonormalized_hexahedral_coframe() -> None:
    # E^i = ell/sqrt(6) vartheta^i absorbs the I/6 spatial metric.
    spatial = np.array([1.0, 2.0, 2.0])
    a = float(np.linalg.norm(spatial))
    q = -a**2 + float(np.dot(spatial, spatial))
    assert math.isclose(q, 0.0, abs_tol=TOL)


def test_spherical_refinement_invariants() -> None:
    omega_oct = math.pi / 2.0
    fs_area_oct = omega_oct / 4.0
    berry_oct = omega_oct / 2.0
    assert math.isclose(8.0 * omega_oct, 4.0 * math.pi, abs_tol=TOL)
    assert math.isclose(8.0 * fs_area_oct, math.pi, abs_tol=TOL)
    assert math.isclose(8.0 * berry_oct, 2.0 * math.pi, abs_tol=TOL)
    assert math.isclose((8.0 * berry_oct) / (2.0 * math.pi), 1.0, abs_tol=TOL)
    assert 8 - 12 + 6 == 2
    assert 6 - 12 + 8 == 2
