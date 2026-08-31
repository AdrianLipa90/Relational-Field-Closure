"""RF-GSC4A constructor for a source-assembled RF-E25 atlas packet."""
from __future__ import annotations

from dataclasses import dataclass
from math import isfinite
from typing import Iterable, Mapping, Sequence

from src.rfc.shared_spacetime_atlas import (
    ADMPatch,
    AtlasOverlap,
    SharedAtlasCertificate,
    SharedSpacetimeAtlasError,
    certify_shared_spacetime_atlas,
    det,
    matmul,
    max_abs,
    subtract,
    transpose,
)


class SourceAssembledAtlasError(ValueError):
    """Raised when the source packet fails the GSC4A assembly gate."""


Matrix3 = tuple[tuple[float, float, float], ...]
Vector3 = tuple[float, float, float]


def _finite(value: float, label: str) -> float:
    out = float(value)
    if not isfinite(out):
        raise SourceAssembledAtlasError(f"{label} must be finite")
    return out


def _vec3(values: Sequence[float], label: str) -> Vector3:
    if len(values) != 3:
        raise SourceAssembledAtlasError(f"{label} must have length 3")
    return tuple(_finite(x, label) for x in values)  # type: ignore[return-value]


def _mat3(values: Sequence[Sequence[float]], label: str) -> Matrix3:
    if len(values) != 3 or any(len(row) != 3 for row in values):
        raise SourceAssembledAtlasError(f"{label} must be 3x3")
    return tuple(tuple(_finite(x, label) for x in row) for row in values)  # type: ignore[return-value]


def _mv(a: Matrix3, v: Vector3) -> Vector3:
    return tuple(sum(a[i][k] * v[k] for k in range(3)) for i in range(3))  # type: ignore[return-value]


def _subv(a: Vector3, b: Vector3) -> Vector3:
    return tuple(a[i] - b[i] for i in range(3))  # type: ignore[return-value]


def _mat4_jacobian(a: Matrix3, v: Vector3) -> tuple[tuple[float, ...], ...]:
    return (
        (1.0, 0.0, 0.0, 0.0),
        (v[0], a[0][0], a[0][1], a[0][2]),
        (v[1], a[1][0], a[1][1], a[1][2]),
        (v[2], a[2][0], a[2][1], a[2][2]),
    )


def _mat4_lorentz(r: Matrix3) -> tuple[tuple[float, ...], ...]:
    return (
        (1.0, 0.0, 0.0, 0.0),
        (0.0, r[0][0], r[0][1], r[0][2]),
        (0.0, r[1][0], r[1][1], r[1][2]),
        (0.0, r[2][0], r[2][1], r[2][2]),
    )


def _identity3() -> Matrix3:
    return ((1.0, 0.0, 0.0), (0.0, 1.0, 0.0), (0.0, 0.0, 1.0))


def _residual_matrix3(a: Matrix3, b: Matrix3) -> float:
    return max(abs(a[i][j] - b[i][j]) for i in range(3) for j in range(3))


def _residual_vec3(a: Vector3, b: Vector3) -> float:
    return max(abs(a[i] - b[i]) for i in range(3))


@dataclass(frozen=True)
class SpatialSourceOverlap:
    source: str
    target: str
    spatial_jacobian: Sequence[Sequence[float]]
    temporal_drift: Sequence[float]
    spatial_rotation: Sequence[Sequence[float]]

    def normalized(self) -> tuple[Matrix3, Vector3, Matrix3]:
        if not self.source or not self.target or self.source == self.target:
            raise SourceAssembledAtlasError("source and target must be distinct non-empty patch IDs")
        return (
            _mat3(self.spatial_jacobian, "spatial_jacobian"),
            _vec3(self.temporal_drift, "temporal_drift"),
            _mat3(self.spatial_rotation, "spatial_rotation"),
        )


@dataclass(frozen=True)
class SourceAssembledAtlasCertificate:
    compatible: bool
    source_overlap_count: int
    max_lapse_residual: float
    max_spatial_coframe_residual: float
    max_shift_residual: float
    max_rotation_residual: float
    rf_e25: SharedAtlasCertificate
    production_input_status: str = "OPEN_SOURCE_PACKET"
    theorem_status: str = "EXACT_SOURCE_ASSEMBLY_THEOREM"


def assemble_source_shared_spacetime_atlas(
    patches: Sequence[ADMPatch],
    source_overlaps: Sequence[SpatialSourceOverlap],
    *,
    triangles: Iterable[tuple[str, str, str]] = (),
    atol: float = 1.0e-10,
) -> SourceAssembledAtlasCertificate:
    """Construct RF-E25 overlaps from TIR/IDT/matching source relations."""
    tol = _finite(atol, "atol")
    if tol < 0.0:
        raise SourceAssembledAtlasError("atol must be non-negative")
    if not patches:
        raise SourceAssembledAtlasError("at least one ADM patch is required")

    patch_map: Mapping[str, ADMPatch] = {patch.name: patch for patch in patches}
    if len(patch_map) != len(patches):
        raise SourceAssembledAtlasError("patch IDs must be unique")

    constructed: list[AtlasOverlap] = []
    max_lapse = max_coframe = max_shift = max_rotation = 0.0

    for item in source_overlaps:
        if item.source not in patch_map or item.target not in patch_map:
            raise SourceAssembledAtlasError("source overlap references an unknown patch")
        a, v, r = item.normalized()
        p = patch_map[item.source]
        q = patch_map[item.target]

        if det(a) <= tol:
            raise SourceAssembledAtlasError("spatial Jacobian must preserve orientation")

        rr_t = matmul(tuple(tuple(x for x in row) for row in transpose(r)), r)
        rotation_residual = _residual_matrix3(rr_t, _identity3())
        if rotation_residual > tol or abs(det(r) - 1.0) > tol:
            raise SourceAssembledAtlasError("spatial rotation must lie in SO(3)")

        lapse_residual = abs(q.lapse - p.lapse)
        if lapse_residual > tol * (1.0 + max(abs(p.lapse), abs(q.lapse))):
            raise SourceAssembledAtlasError("shared lapse scalar mismatch on overlap")

        eqa = matmul(q.triad, a)
        rep = matmul(r, p.triad)
        spatial_coframe_residual = _residual_matrix3(eqa, rep)
        if spatial_coframe_residual > tol * (1.0 + max(max_abs(eqa), max_abs(rep))):
            raise SourceAssembledAtlasError("TIR spatial coframe overlap relation failed")

        expected_shift = _subv(_mv(a, p.shift), v)
        shift_residual = _residual_vec3(q.shift, expected_shift)
        if shift_residual > tol * (1.0 + max(max(abs(x) for x in q.shift), max(abs(x) for x in expected_shift))):
            raise SourceAssembledAtlasError("GSC3 matching shift overlap relation failed")

        constructed.append(
            AtlasOverlap(
                source=item.source,
                target=item.target,
                jacobian=_mat4_jacobian(a, v),
                lorentz=_mat4_lorentz(r),
            )
        )
        max_lapse = max(max_lapse, lapse_residual)
        max_coframe = max(max_coframe, spatial_coframe_residual)
        max_shift = max(max_shift, shift_residual)
        max_rotation = max(max_rotation, rotation_residual)

    try:
        rf_e25 = certify_shared_spacetime_atlas(
            patches,
            constructed,
            triangles=triangles,
            atol=tol,
        )
    except SharedSpacetimeAtlasError as exc:
        raise SourceAssembledAtlasError(f"constructed RF-E25 packet failed: {exc}") from exc

    return SourceAssembledAtlasCertificate(
        compatible=True,
        source_overlap_count=len(source_overlaps),
        max_lapse_residual=max_lapse,
        max_spatial_coframe_residual=max_coframe,
        max_shift_residual=max_shift,
        max_rotation_residual=max_rotation,
        rf_e25=rf_e25,
    )
