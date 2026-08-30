"""Premetric trace/traceless spacetime-rank reference checks.

Candidate-only executable support for PREMETRIC_TEMPORAL_SPATIAL_TRANSVERSALITY_V0_5.
No metric or Lorentzian signature is assumed in this module.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import isfinite
from typing import TypeAlias

Matrix2: TypeAlias = tuple[tuple[complex, complex], tuple[complex, complex]]

I2: Matrix2 = ((1.0 + 0j, 0j), (0j, 1.0 + 0j))
SIGMA_X: Matrix2 = ((0j, 1.0 + 0j), (1.0 + 0j, 0j))
SIGMA_Y: Matrix2 = ((0j, -1j), (1j, 0j))
SIGMA_Z: Matrix2 = ((1.0 + 0j, 0j), (0j, -1.0 + 0j))
PAULI_BASIS: tuple[Matrix2, Matrix2, Matrix2, Matrix2] = (
    I2,
    SIGMA_X,
    SIGMA_Y,
    SIGMA_Z,
)


class PremetricTransversalityError(ValueError):
    """Fail-closed error for invalid 2x2 Hermitian inputs."""


def _finite_complex(z: complex) -> bool:
    return isfinite(z.real) and isfinite(z.imag)


def _validate_matrix(a: Matrix2) -> None:
    if len(a) != 2 or any(len(row) != 2 for row in a):
        raise PremetricTransversalityError("expected a 2x2 matrix")
    if not all(_finite_complex(z) for row in a for z in row):
        raise PremetricTransversalityError("matrix entries must be finite")
    if a[0][0] != a[0][0].conjugate() or a[1][1] != a[1][1].conjugate():
        raise PremetricTransversalityError("diagonal entries must be real")
    if a[0][1] != a[1][0].conjugate():
        raise PremetricTransversalityError("matrix must be Hermitian")


def _add(a: Matrix2, b: Matrix2) -> Matrix2:
    return tuple(
        tuple(a[i][j] + b[i][j] for j in range(2))
        for i in range(2)
    )  # type: ignore[return-value]


def _sub(a: Matrix2, b: Matrix2) -> Matrix2:
    return tuple(
        tuple(a[i][j] - b[i][j] for j in range(2))
        for i in range(2)
    )  # type: ignore[return-value]


def _scale(s: complex, a: Matrix2) -> Matrix2:
    return tuple(
        tuple(s * a[i][j] for j in range(2))
        for i in range(2)
    )  # type: ignore[return-value]


def _mul(a: Matrix2, b: Matrix2) -> Matrix2:
    return tuple(
        tuple(sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2))
        for i in range(2)
    )  # type: ignore[return-value]


def trace(a: Matrix2) -> complex:
    _validate_matrix(a)
    return a[0][0] + a[1][1]


def temporal_projector(a: Matrix2) -> Matrix2:
    """P_T(A) = Tr(A) I / 2."""
    t = trace(a)
    return _scale(0.5 * t, I2)


def spatial_projector(a: Matrix2) -> Matrix2:
    """P_S(A) = A - Tr(A) I / 2."""
    _validate_matrix(a)
    return _sub(a, temporal_projector(a))


def dual_coordinates(a: Matrix2) -> tuple[float, float, float, float]:
    """Return x^mu from A = x^0 I + x^i sigma_i."""
    _validate_matrix(a)
    values = [0.5 * trace(a)]
    for sigma in (SIGMA_X, SIGMA_Y, SIGMA_Z):
        product = _mul(a, sigma)
        values.append(0.5 * (product[0][0] + product[1][1]))
    if any(abs(v.imag) > 1e-15 for v in values):
        raise PremetricTransversalityError("Hermitian coordinate pairing must be real")
    return tuple(float(v.real) for v in values)  # type: ignore[return-value]


def reconstruct(coords: tuple[float, float, float, float]) -> Matrix2:
    if len(coords) != 4 or not all(isfinite(x) for x in coords):
        raise PremetricTransversalityError("coordinates must be four finite reals")
    out = _scale(coords[0], I2)
    for coefficient, sigma in zip(coords[1:], (SIGMA_X, SIGMA_Y, SIGMA_Z), strict=True):
        out = _add(out, _scale(coefficient, sigma))
    return out


def basis_pairing_matrix() -> tuple[tuple[float, ...], ...]:
    """Return theta^mu(e_nu); exact result is I_4."""
    columns = [dual_coordinates(b) for b in PAULI_BASIS]
    return tuple(
        tuple(columns[col][row] for col in range(4))
        for row in range(4)
    )


def canonical_lift(ell: float, bloch: tuple[float, float, float]) -> Matrix2:
    """X = ell rho for rho=(I+r.sigma)/2; used only for the worldline firewall."""
    if not isfinite(ell) or ell <= 0:
        raise PremetricTransversalityError("ell must be finite and positive")
    if len(bloch) != 3 or not all(isfinite(x) for x in bloch):
        raise PremetricTransversalityError("Bloch coordinates must be three finite reals")
    if sum(x * x for x in bloch) > 1.0 + 1e-15:
        raise PremetricTransversalityError("Bloch vector lies outside the unit ball")
    rho = _scale(0.5, I2)
    for coefficient, sigma in zip(bloch, (SIGMA_X, SIGMA_Y, SIGMA_Z), strict=True):
        rho = _add(rho, _scale(0.5 * coefficient, sigma))
    return _scale(ell, rho)


@dataclass(frozen=True)
class PremetricCertificate:
    pairing_identity: bool
    temporal_kills_spatial: bool
    spatial_kills_temporal: bool
    projector_reconstruction: bool
    four_volume_nonzero: bool


def certificate() -> PremetricCertificate:
    pairing = basis_pairing_matrix()
    identity = tuple(
        tuple(1.0 if i == j else 0.0 for j in range(4))
        for i in range(4)
    )
    sample = reconstruct((2.0, -3.0, 5.0, 7.0))
    reconstructed = _add(temporal_projector(sample), spatial_projector(sample))
    return PremetricCertificate(
        pairing_identity=pairing == identity,
        temporal_kills_spatial=all(dual_coordinates(sigma)[0] == 0.0 for sigma in PAULI_BASIS[1:]),
        spatial_kills_temporal=dual_coordinates(I2)[1:] == (0.0, 0.0, 0.0),
        projector_reconstruction=reconstructed == sample,
        four_volume_nonzero=pairing == identity,
    )
