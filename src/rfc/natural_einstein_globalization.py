"""RF-GSC5A natural Einstein globalization input-reduction certifier.

Given a smooth shared metric atlas and patchwise RF-E24 solution receipts with
common constants, the Einstein overlap law is inherited from naturality.  The
stress-tensor and residual overlap laws then follow from the local field
equation.  This certifier validates the reduced dependency packet.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import isfinite
from typing import Sequence


class NaturalEinsteinGlobalizationError(ValueError):
    """Raised when a declared GSC5A reduced witness fails closed."""


Matrix = tuple[tuple[float, ...], ...]


def _finite(value: float, label: str) -> float:
    out = float(value)
    if not isfinite(out):
        raise NaturalEinsteinGlobalizationError(f"{label} must be finite")
    return out


def _matrix(value: Sequence[Sequence[float]], label: str) -> Matrix:
    if len(value) != 4 or any(len(row) != 4 for row in value):
        raise NaturalEinsteinGlobalizationError(f"{label} must be 4x4")
    return tuple(
        tuple(_finite(x, f"{label}[{i}][{j}]") for j, x in enumerate(row))
        for i, row in enumerate(value)
    )


def _transpose(a: Matrix) -> Matrix:
    return tuple(tuple(a[j][i] for j in range(4)) for i in range(4))


def _matmul(a: Matrix, b: Matrix) -> Matrix:
    return tuple(
        tuple(sum(a[i][k] * b[k][j] for k in range(4)) for j in range(4))
        for i in range(4)
    )


def _subtract(a: Matrix, b: Matrix) -> Matrix:
    return tuple(tuple(a[i][j] - b[i][j] for j in range(4)) for i in range(4))


def _max_abs(a: Matrix) -> float:
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
    scale = 1.0 + max(abs(a), abs(b))
    if residual > atol * scale:
        raise NaturalEinsteinGlobalizationError(
            f"{label} mismatch: residual={residual:.17g}"
        )


def _close_matrix(a: Matrix, b: Matrix, atol: float, label: str) -> float:
    residual = _max_abs(_subtract(a, b))
    scale = 1.0 + max(_max_abs(a), _max_abs(b))
    if residual > atol * scale:
        raise NaturalEinsteinGlobalizationError(
            f"{label} residual {residual:.17g} exceeds tolerance"
        )
    return residual


def pullback_covariant(jacobian: Matrix, target_tensor: Matrix) -> Matrix:
    return _matmul(_transpose(jacobian), _matmul(target_tensor, jacobian))


@dataclass(frozen=True)
class NaturalEinsteinPatch:
    name: str
    metric: Sequence[Sequence[float]]
    cosmological_constant: float
    kappa_e: float
    source_field_lineage_id: str
    local_solution_receipt_id: str
    local_solution_certified: bool = True
    einstein_operator_lineage_id: str = "RF-E24:EINSTEIN_OPERATOR"

    def __post_init__(self) -> None:
        if not isinstance(self.name, str) or not self.name:
            raise NaturalEinsteinGlobalizationError("patch name must be non-empty")
        metric = _matrix(self.metric, f"{self.name}.metric")
        if abs(_det(metric)) <= 1.0e-14:
            raise NaturalEinsteinGlobalizationError("patch metric must be nondegenerate")
        _close_matrix(metric, _transpose(metric), 1.0e-12, f"{self.name}.metric symmetry")
        lam = _finite(self.cosmological_constant, f"{self.name}.Lambda")
        kappa = _finite(self.kappa_e, f"{self.name}.kappa_e")
        if kappa <= 0.0:
            raise NaturalEinsteinGlobalizationError("kappa_e must be strictly positive")
        if not self.source_field_lineage_id:
            raise NaturalEinsteinGlobalizationError("source field lineage id must be non-empty")
        if not self.local_solution_receipt_id:
            raise NaturalEinsteinGlobalizationError("local solution receipt id must be non-empty")
        if not self.einstein_operator_lineage_id:
            raise NaturalEinsteinGlobalizationError("Einstein operator lineage id must be non-empty")
        object.__setattr__(self, "metric", metric)
        object.__setattr__(self, "cosmological_constant", lam)
        object.__setattr__(self, "kappa_e", kappa)


@dataclass(frozen=True)
class MetricAtlasOverlap:
    source: str
    target: str
    jacobian: Sequence[Sequence[float]]

    def __post_init__(self) -> None:
        if not self.source or not self.target or self.source == self.target:
            raise NaturalEinsteinGlobalizationError(
                "overlap must join two distinct non-empty patch ids"
            )
        jac = _matrix(self.jacobian, f"{self.source}->{self.target}.jacobian")
        if abs(_det(jac)) <= 1.0e-14:
            raise NaturalEinsteinGlobalizationError("overlap Jacobian must be invertible")
        object.__setattr__(self, "jacobian", jac)


@dataclass(frozen=True)
class NaturalEinsteinGlobalizationCertificate:
    patch_count: int
    overlap_count: int
    common_constants: bool
    common_source_lineage: bool
    common_operator_lineage: bool
    patchwise_solution_receipts: bool
    metric_overlap_gluing: bool
    connected_atlas: bool
    shared_atlas_certified: bool
    smooth_atlas_certified: bool
    domain_coverage_certified: bool
    einstein_overlap_covariance: str
    stress_overlap_covariance: str
    residual_overlap_covariance: str
    global_einstein_carrier: bool
    max_metric_overlap_residual: float
    production_status: str


def certify_natural_einstein_globalization(
    patches: Sequence[NaturalEinsteinPatch],
    overlaps: Sequence[MetricAtlasOverlap],
    *,
    shared_atlas_certified: bool = False,
    smooth_atlas_certified: bool = False,
    domain_coverage_certified: bool = False,
    atol: float = 1.0e-10,
) -> NaturalEinsteinGlobalizationCertificate:
    tol = _finite(atol, "atol")
    if tol < 0.0:
        raise NaturalEinsteinGlobalizationError("atol must be non-negative")

    patch_list = tuple(patches)
    if not patch_list:
        raise NaturalEinsteinGlobalizationError("at least one patch is required")
    if any(not isinstance(p, NaturalEinsteinPatch) for p in patch_list):
        raise NaturalEinsteinGlobalizationError(
            "all patches must be NaturalEinsteinPatch instances"
        )

    by_name: dict[str, NaturalEinsteinPatch] = {}
    for patch in patch_list:
        if patch.name in by_name:
            raise NaturalEinsteinGlobalizationError(f"duplicate patch name {patch.name!r}")
        if not patch.local_solution_certified:
            raise NaturalEinsteinGlobalizationError(
                f"patch {patch.name!r} requires a certified RF-E24 local solution receipt"
            )
        by_name[patch.name] = patch

    lam0 = patch_list[0].cosmological_constant
    kappa0 = patch_list[0].kappa_e
    source0 = patch_list[0].source_field_lineage_id
    operator0 = patch_list[0].einstein_operator_lineage_id
    for patch in patch_list[1:]:
        _close_scalar(patch.cosmological_constant, lam0, tol, "cosmological constant")
        _close_scalar(patch.kappa_e, kappa0, tol, "kappa_e")
        if patch.source_field_lineage_id != source0:
            raise NaturalEinsteinGlobalizationError("source field lineage mismatch")
        if patch.einstein_operator_lineage_id != operator0:
            raise NaturalEinsteinGlobalizationError("Einstein operator lineage mismatch")

    overlap_list = tuple(overlaps)
    if any(not isinstance(o, MetricAtlasOverlap) for o in overlap_list):
        raise NaturalEinsteinGlobalizationError(
            "all overlaps must be MetricAtlasOverlap instances"
        )

    adjacency: dict[str, set[str]] = {name: set() for name in by_name}
    max_metric = 0.0
    for overlap in overlap_list:
        if overlap.source not in by_name or overlap.target not in by_name:
            raise NaturalEinsteinGlobalizationError("overlap references an unknown patch")
        p = by_name[overlap.source]
        q = by_name[overlap.target]
        residual = _close_matrix(
            p.metric,
            pullback_covariant(overlap.jacobian, q.metric),
            tol,
            f"{overlap.source}->{overlap.target} metric pullback",
        )
        max_metric = max(max_metric, residual)
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
            raise NaturalEinsteinGlobalizationError("declared metric atlas is disconnected")

    naturality_active = bool(shared_atlas_certified) and bool(smooth_atlas_certified)
    global_carrier = naturality_active and bool(domain_coverage_certified)

    return NaturalEinsteinGlobalizationCertificate(
        patch_count=len(patch_list),
        overlap_count=len(overlap_list),
        common_constants=True,
        common_source_lineage=True,
        common_operator_lineage=True,
        patchwise_solution_receipts=True,
        metric_overlap_gluing=True,
        connected_atlas=True,
        shared_atlas_certified=bool(shared_atlas_certified),
        smooth_atlas_certified=bool(smooth_atlas_certified),
        domain_coverage_certified=bool(domain_coverage_certified),
        einstein_overlap_covariance=(
            "DERIVED_FROM_METRIC_NATURALITY" if naturality_active else "PARENT_REGULARITY_OPEN"
        ),
        stress_overlap_covariance=(
            "DERIVED_FROM_LOCAL_EQUATION" if naturality_active else "PARENT_REGULARITY_OPEN"
        ),
        residual_overlap_covariance=(
            "DERIVED_ZERO_TENSOR" if naturality_active else "PARENT_REGULARITY_OPEN"
        ),
        global_einstein_carrier=global_carrier,
        max_metric_overlap_residual=max_metric,
        production_status=(
            "GSC5A_REDUCED_CONTRACT_PASS_ON_SUPPLIED_PARENTS"
            if global_carrier
            else "PRODUCTION_SMOOTH_ATLAS_SOLUTION_AND_OR_COVERAGE_PARENT_OPEN"
        ),
    )
