"""RF-E26 local-to-global Einstein carrier promotion certifier.

For dx_q = J_{q<-p} dx_p, covariant rank-two tensors satisfy

    X_p = J^T X_q J.

The gate checks patchwise RF-E24 residuals and overlap compatibility. A global
promotion bit is emitted only when the RF-E25 shared-atlas parent and explicit
target-domain coverage witness are both supplied. RF-L7 global hyperbolicity
remains a separate gate.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import isfinite
from typing import Sequence


class GlobalEinsteinCarrierError(ValueError):
    """Raised when a declared RF-E26 witness fails closed."""


Matrix = tuple[tuple[float, ...], ...]


def _finite(value: float, label: str) -> float:
    out = float(value)
    if not isfinite(out):
        raise GlobalEinsteinCarrierError(f"{label} must be finite")
    return out


def _matrix(value: Sequence[Sequence[float]], label: str) -> Matrix:
    if len(value) != 4:
        raise GlobalEinsteinCarrierError(f"{label} must be 4x4")
    rows: list[tuple[float, ...]] = []
    for i, row in enumerate(value):
        if len(row) != 4:
            raise GlobalEinsteinCarrierError(f"{label} must be 4x4")
        rows.append(tuple(_finite(x, f"{label}[{i}]") for x in row))
    return tuple(rows)


def transpose(a: Matrix) -> Matrix:
    return tuple(tuple(a[j][i] for j in range(4)) for i in range(4))


def matmul(a: Matrix, b: Matrix) -> Matrix:
    return tuple(
        tuple(sum(a[i][k] * b[k][j] for k in range(4)) for j in range(4))
        for i in range(4)
    )


def add(a: Matrix, b: Matrix) -> Matrix:
    return tuple(tuple(a[i][j] + b[i][j] for j in range(4)) for i in range(4))


def subtract(a: Matrix, b: Matrix) -> Matrix:
    return tuple(tuple(a[i][j] - b[i][j] for j in range(4)) for i in range(4))


def scale(scalar: float, a: Matrix) -> Matrix:
    return tuple(tuple(scalar * a[i][j] for j in range(4)) for i in range(4))


def max_abs(a: Matrix) -> float:
    return max(abs(x) for row in a for x in row)


def _det(a: Sequence[Sequence[float]]) -> float:
    n = len(a)
    if n == 1:
        return float(a[0][0])
    total = 0.0
    for j in range(n):
        minor = tuple(
            tuple(row[k] for k in range(n) if k != j)
            for row in a[1:]
        )
        total += ((-1.0) ** j) * float(a[0][j]) * _det(minor)
    return total


def _close_scalar(a: float, b: float, atol: float, label: str) -> None:
    residual = abs(a - b)
    scale0 = 1.0 + max(abs(a), abs(b))
    if residual > atol * scale0:
        raise GlobalEinsteinCarrierError(
            f"{label} mismatch: residual={residual:.17g}"
        )


def _close_matrix(a: Matrix, b: Matrix, atol: float, label: str) -> float:
    residual = max_abs(subtract(a, b))
    scale0 = 1.0 + max(max_abs(a), max_abs(b))
    if residual > atol * scale0:
        raise GlobalEinsteinCarrierError(
            f"{label} residual {residual:.17g} exceeds tolerance"
        )
    return residual


def _require_symmetric(a: Matrix, label: str) -> None:
    _close_matrix(a, transpose(a), 1.0e-12, f"{label} symmetry")


def pullback_covariant(jacobian: Matrix, target_tensor: Matrix) -> Matrix:
    """Return J^T X_q J for dx_q = J dx_p."""

    return matmul(transpose(jacobian), matmul(target_tensor, jacobian))


@dataclass(frozen=True)
class EinsteinPatch:
    name: str
    metric: Sequence[Sequence[float]]
    einstein: Sequence[Sequence[float]]
    stress: Sequence[Sequence[float]]
    cosmological_constant: float
    kappa_e: float

    def __post_init__(self) -> None:
        if not isinstance(self.name, str) or not self.name:
            raise GlobalEinsteinCarrierError("patch name must be a non-empty string")
        metric = _matrix(self.metric, f"{self.name}.metric")
        einstein = _matrix(self.einstein, f"{self.name}.einstein")
        stress = _matrix(self.stress, f"{self.name}.stress")
        lam = _finite(self.cosmological_constant, f"{self.name}.Lambda")
        kappa = _finite(self.kappa_e, f"{self.name}.kappa_e")
        if kappa <= 0.0:
            raise GlobalEinsteinCarrierError("kappa_e must be strictly positive")
        if abs(_det(metric)) <= 1.0e-14:
            raise GlobalEinsteinCarrierError("patch metric must be nondegenerate")
        _require_symmetric(metric, f"{self.name}.metric")
        _require_symmetric(einstein, f"{self.name}.einstein")
        _require_symmetric(stress, f"{self.name}.stress")
        object.__setattr__(self, "metric", metric)
        object.__setattr__(self, "einstein", einstein)
        object.__setattr__(self, "stress", stress)
        object.__setattr__(self, "cosmological_constant", lam)
        object.__setattr__(self, "kappa_e", kappa)

    @property
    def residual(self) -> Matrix:
        return subtract(
            add(self.einstein, scale(self.cosmological_constant, self.metric)),
            scale(self.kappa_e, self.stress),
        )


@dataclass(frozen=True)
class TensorOverlap:
    source: str
    target: str
    jacobian: Sequence[Sequence[float]]

    def __post_init__(self) -> None:
        if not isinstance(self.source, str) or not self.source:
            raise GlobalEinsteinCarrierError("overlap source must be non-empty")
        if not isinstance(self.target, str) or not self.target:
            raise GlobalEinsteinCarrierError("overlap target must be non-empty")
        if self.source == self.target:
            raise GlobalEinsteinCarrierError("overlap must join distinct patches")
        jac = _matrix(self.jacobian, f"{self.source}->{self.target}.jacobian")
        if abs(_det(jac)) <= 1.0e-14:
            raise GlobalEinsteinCarrierError("overlap Jacobian must be invertible")
        object.__setattr__(self, "jacobian", jac)


@dataclass(frozen=True)
class GlobalEinsteinCarrierCertificate:
    patch_count: int
    overlap_count: int
    common_constants: bool
    local_einstein_equations: bool
    tensor_overlap_gluing: bool
    connected_atlas: bool
    shared_atlas_certified: bool
    domain_coverage_certified: bool
    global_einstein_carrier: bool
    max_local_residual: float
    max_overlap_residual: float
    global_hyperbolicity: str = "OPEN_SEPARATE_RF_L7_GATE"


def certify_global_einstein_carrier(
    patches: Sequence[EinsteinPatch],
    overlaps: Sequence[TensorOverlap],
    *,
    shared_atlas_certified: bool = False,
    domain_coverage_certified: bool = False,
    atol: float = 1.0e-10,
) -> GlobalEinsteinCarrierCertificate:
    """Check the RF-E26 local-to-global Einstein carrier promotion contract."""

    tol = _finite(atol, "atol")
    if tol < 0.0:
        raise GlobalEinsteinCarrierError("atol must be non-negative")

    patch_list = tuple(patches)
    if not patch_list:
        raise GlobalEinsteinCarrierError("at least one Einstein patch is required")
    if any(not isinstance(patch, EinsteinPatch) for patch in patch_list):
        raise GlobalEinsteinCarrierError("all patches must be EinsteinPatch instances")

    by_name: dict[str, EinsteinPatch] = {}
    for patch in patch_list:
        if patch.name in by_name:
            raise GlobalEinsteinCarrierError(f"duplicate patch name {patch.name!r}")
        by_name[patch.name] = patch

    lambda0 = patch_list[0].cosmological_constant
    kappa0 = patch_list[0].kappa_e
    for patch in patch_list[1:]:
        _close_scalar(
            patch.cosmological_constant,
            lambda0,
            tol,
            "cosmological constant",
        )
        _close_scalar(patch.kappa_e, kappa0, tol, "kappa_e")

    zero: Matrix = tuple(tuple(0.0 for _ in range(4)) for _ in range(4))
    max_local = 0.0
    for patch in patch_list:
        residual = patch.residual
        max_local = max(max_local, max_abs(residual))
        _close_matrix(residual, zero, tol, f"{patch.name} Einstein residual")

    overlap_list = tuple(overlaps)
    if any(not isinstance(overlap, TensorOverlap) for overlap in overlap_list):
        raise GlobalEinsteinCarrierError("all overlaps must be TensorOverlap instances")

    adjacency: dict[str, set[str]] = {name: set() for name in by_name}
    max_overlap = 0.0

    for overlap in overlap_list:
        if overlap.source not in by_name or overlap.target not in by_name:
            raise GlobalEinsteinCarrierError("overlap references an unknown patch")
        p = by_name[overlap.source]
        q = by_name[overlap.target]
        jac = overlap.jacobian

        metric_r = _close_matrix(
            p.metric,
            pullback_covariant(jac, q.metric),
            tol,
            f"{overlap.source}->{overlap.target} metric pullback",
        )
        einstein_r = _close_matrix(
            p.einstein,
            pullback_covariant(jac, q.einstein),
            tol,
            f"{overlap.source}->{overlap.target} Einstein pullback",
        )
        stress_r = _close_matrix(
            p.stress,
            pullback_covariant(jac, q.stress),
            tol,
            f"{overlap.source}->{overlap.target} stress pullback",
        )
        residual_r = _close_matrix(
            p.residual,
            pullback_covariant(jac, q.residual),
            tol,
            f"{overlap.source}->{overlap.target} residual pullback",
        )
        max_overlap = max(max_overlap, metric_r, einstein_r, stress_r, residual_r)
        adjacency[overlap.source].add(overlap.target)
        adjacency[overlap.target].add(overlap.source)

    if len(by_name) > 1:
        root = next(iter(by_name))
        seen = {root}
        stack = [root]
        while stack:
            current = stack.pop()
            for neighbor in adjacency[current]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    stack.append(neighbor)
        if len(seen) != len(by_name):
            raise GlobalEinsteinCarrierError("declared Einstein atlas is disconnected")

    promoted = bool(shared_atlas_certified) and bool(domain_coverage_certified)
    return GlobalEinsteinCarrierCertificate(
        patch_count=len(patch_list),
        overlap_count=len(overlap_list),
        common_constants=True,
        local_einstein_equations=True,
        tensor_overlap_gluing=True,
        connected_atlas=True,
        shared_atlas_certified=bool(shared_atlas_certified),
        domain_coverage_certified=bool(domain_coverage_certified),
        global_einstein_carrier=promoted,
        max_local_residual=max_local,
        max_overlap_residual=max_overlap,
    )
