from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Sequence

import numpy as np


@dataclass(frozen=True)
class RigidChart:
    anchor: np.ndarray
    frame: np.ndarray


@dataclass(frozen=True)
class OverlapInvariant:
    rotation: np.ndarray
    translation: np.ndarray


def _vec3(x: Iterable[float]) -> np.ndarray:
    a = np.asarray(tuple(x), dtype=float)
    if a.shape != (3,) or not np.all(np.isfinite(a)):
        raise ValueError("anchor must be one finite 3-vector")
    return a


def _rot3(x: Iterable[Iterable[float]], tol: float = 1e-10) -> np.ndarray:
    q = np.asarray(x, dtype=float)
    if q.shape != (3, 3) or not np.all(np.isfinite(q)):
        raise ValueError("frame must be one finite 3x3 matrix")
    if not np.allclose(q.T @ q, np.eye(3), atol=tol, rtol=0.0):
        raise ValueError("frame must be orthogonal")
    if not np.isclose(np.linalg.det(q), 1.0, atol=tol, rtol=0.0):
        raise ValueError("frame must have determinant +1")
    return q


def chart(anchor: Iterable[float], frame: Iterable[Iterable[float]], tol: float = 1e-10) -> RigidChart:
    return RigidChart(anchor=_vec3(anchor), frame=_rot3(frame, tol=tol))


def overlap(p: RigidChart, q: RigidChart) -> OverlapInvariant:
    """Return the rigid overlap x_q = A_qp x_p + t_qp."""
    a_qp = q.frame.T @ p.frame
    t_qp = q.frame.T @ (p.anchor - q.anchor)
    return OverlapInvariant(rotation=a_qp, translation=t_qp)


def apply_global_se3(
    charts: Sequence[RigidChart],
    rotation: Iterable[Iterable[float]],
    translation: Iterable[float],
    tol: float = 1e-10,
) -> tuple[RigidChart, ...]:
    """Apply one common ambient Euclidean gauge to every rigid chart.

    r'_p = S^T (r_p-a),   Q'_p = S^T Q_p.
    """
    s = _rot3(rotation, tol=tol)
    a = _vec3(translation)
    out = []
    for item in charts:
        out.append(
            RigidChart(
                anchor=s.T @ (item.anchor - a),
                frame=s.T @ item.frame,
            )
        )
    return tuple(out)


def canonical_reference_gauge(
    charts: Sequence[RigidChart], reference: int = 0, tol: float = 1e-10
) -> tuple[RigidChart, ...]:
    if not charts:
        raise ValueError("at least one chart is required")
    if reference < 0 or reference >= len(charts):
        raise IndexError("reference chart index out of range")
    ref = charts[reference]
    normalized = apply_global_se3(charts, ref.frame, ref.anchor, tol=tol)
    return normalized


def pairwise_overlap_table(charts: Sequence[RigidChart]) -> dict[tuple[int, int], OverlapInvariant]:
    return {
        (p, q): overlap(charts[p], charts[q])
        for p in range(len(charts))
        for q in range(len(charts))
        if p != q
    }


def certify_global_se3_quotient(
    charts: Sequence[RigidChart], reference: int = 0, tol: float = 1e-10
) -> dict:
    """Certify that one global SE(3) gauge removes only ambient origin/orientation.

    The returned overlap packet is invariant under the canonical reference-patch
    gauge. Relative translations/rotations remain explicit source geometry.
    """
    if not charts:
        raise ValueError("at least one chart is required")
    normalized = canonical_reference_gauge(charts, reference=reference, tol=tol)
    before = pairwise_overlap_table(charts)
    after = pairwise_overlap_table(normalized)

    max_rotation_defect = 0.0
    max_translation_defect = 0.0
    for key in before:
        max_rotation_defect = max(
            max_rotation_defect,
            float(np.max(np.abs(before[key].rotation - after[key].rotation))),
        )
        max_translation_defect = max(
            max_translation_defect,
            float(np.max(np.abs(before[key].translation - after[key].translation))),
        )

    ref = normalized[reference]
    reference_anchor_defect = float(np.max(np.abs(ref.anchor)))
    reference_frame_defect = float(np.max(np.abs(ref.frame - np.eye(3))))
    passed = (
        max_rotation_defect <= tol
        and max_translation_defect <= tol
        and reference_anchor_defect <= tol
        and reference_frame_defect <= tol
    )

    return {
        "schema": "RFC_GSC4F_GLOBAL_SE3_GAUGE_QUOTIENT_V0_1",
        "status": "PASS" if passed else "FAIL",
        "reference": int(reference),
        "chart_count": len(charts),
        "global_gauge_dof_removed": 6,
        "max_rotation_invariance_defect": max_rotation_defect,
        "max_translation_invariance_defect": max_translation_defect,
        "reference_anchor_defect": reference_anchor_defect,
        "reference_frame_defect": reference_frame_defect,
        "relative_rigid_configuration_retained": True,
        "phase_scale_field_retained": True,
        "production_geometry_promoted": False,
    }
