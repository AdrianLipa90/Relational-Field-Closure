from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Sequence

import numpy as np


@dataclass(frozen=True)
class RigidEdge:
    source: str
    target: str
    rotation: np.ndarray
    translation: np.ndarray


@dataclass(frozen=True)
class ReconstructedChart:
    patch_id: str
    anchor: np.ndarray
    frame: np.ndarray


def _vec3(x: Iterable[float]) -> np.ndarray:
    a = np.asarray(tuple(x), dtype=float)
    if a.shape != (3,) or not np.all(np.isfinite(a)):
        raise ValueError("translation must be one finite 3-vector")
    return a


def _rot3(x: Iterable[Iterable[float]], tol: float = 1e-10) -> np.ndarray:
    q = np.asarray(x, dtype=float)
    if q.shape != (3, 3) or not np.all(np.isfinite(q)):
        raise ValueError("rotation must be one finite 3x3 matrix")
    if not np.allclose(q.T @ q, np.eye(3), atol=tol, rtol=0.0):
        raise ValueError("rotation must be orthogonal")
    if not np.isclose(np.linalg.det(q), 1.0, atol=tol, rtol=0.0):
        raise ValueError("rotation must have determinant +1")
    return q


def edge(source: str, target: str, rotation, translation, tol: float = 1e-10) -> RigidEdge:
    s, t = str(source), str(target)
    if not s or not t or s == t:
        raise ValueError("edge requires two distinct nonempty patch ids")
    return RigidEdge(s, t, _rot3(rotation, tol=tol), _vec3(translation))


def inverse_edge(e: RigidEdge) -> RigidEdge:
    a_inv = e.rotation.T
    t_inv = -(a_inv @ e.translation)
    return RigidEdge(e.target, e.source, a_inv, t_inv)


def compose_edges(first: RigidEdge, second: RigidEdge) -> RigidEdge:
    """Compose p->q followed by q->r."""
    if first.target != second.source:
        raise ValueError("edge composition requires matching middle patch")
    a = second.rotation @ first.rotation
    t = second.rotation @ first.translation + second.translation
    return RigidEdge(first.source, second.target, a, t)


def _chart_overlap(p: ReconstructedChart, q: ReconstructedChart) -> tuple[np.ndarray, np.ndarray]:
    a = q.frame.T @ p.frame
    t = q.frame.T @ (p.anchor - q.anchor)
    return a, t


def reconstruct_from_cocycle(
    patch_ids: Sequence[str],
    edges: Sequence[RigidEdge],
    *,
    root: str | None = None,
    tol: float = 1e-10,
) -> dict:
    ids = tuple(dict.fromkeys(str(x) for x in patch_ids))
    if not ids or any(not x for x in ids):
        raise ValueError("patch_ids must be nonempty")
    if len(ids) != len(patch_ids):
        raise ValueError("patch_ids must be unique")
    root_id = root or ids[0]
    if root_id not in ids:
        raise ValueError("root must be one declared patch")

    adjacency: dict[str, list[RigidEdge]] = {p: [] for p in ids}
    validated: list[RigidEdge] = []
    seen_directed: set[tuple[str, str]] = set()
    for item in edges:
        if item.source not in adjacency or item.target not in adjacency:
            raise ValueError("edge references undeclared patch")
        a = _rot3(item.rotation, tol=tol)
        t = _vec3(item.translation)
        key = (item.source, item.target)
        if key in seen_directed:
            raise ValueError("duplicate directed edge")
        seen_directed.add(key)
        e = RigidEdge(item.source, item.target, a, t)
        validated.append(e)
        adjacency[e.source].append(e)
        adjacency[e.target].append(inverse_edge(e))

    charts: dict[str, ReconstructedChart] = {
        root_id: ReconstructedChart(root_id, np.zeros(3), np.eye(3))
    }
    queue = [root_id]
    max_path_rotation_defect = 0.0
    max_path_translation_defect = 0.0

    while queue:
        p = queue.pop(0)
        cp = charts[p]
        for e in adjacency[p]:
            q = e.target
            q_frame = cp.frame @ e.rotation.T
            q_anchor = cp.anchor - q_frame @ e.translation
            candidate = ReconstructedChart(q, q_anchor, q_frame)
            if q not in charts:
                charts[q] = candidate
                queue.append(q)
            else:
                cq = charts[q]
                max_path_rotation_defect = max(
                    max_path_rotation_defect,
                    float(np.max(np.abs(cq.frame - candidate.frame))),
                )
                max_path_translation_defect = max(
                    max_path_translation_defect,
                    float(np.max(np.abs(cq.anchor - candidate.anchor))),
                )

    if len(charts) != len(ids):
        missing = sorted(set(ids) - set(charts))
        raise ValueError(f"overlap graph is disconnected: missing={missing}")

    max_edge_rotation_defect = 0.0
    max_edge_translation_defect = 0.0
    for e in validated:
        a, t = _chart_overlap(charts[e.source], charts[e.target])
        max_edge_rotation_defect = max(
            max_edge_rotation_defect,
            float(np.max(np.abs(a - e.rotation))),
        )
        max_edge_translation_defect = max(
            max_edge_translation_defect,
            float(np.max(np.abs(t - e.translation))),
        )

    passed = (
        max_path_rotation_defect <= tol
        and max_path_translation_defect <= tol
        and max_edge_rotation_defect <= tol
        and max_edge_translation_defect <= tol
    )

    if not passed:
        raise ValueError(
            "rigid overlap cocycle fails path-independence/holonomy closure: "
            f"path_rotation={max_path_rotation_defect}, "
            f"path_translation={max_path_translation_defect}, "
            f"edge_rotation={max_edge_rotation_defect}, "
            f"edge_translation={max_edge_translation_defect}"
        )

    return {
        "schema": "RFC_GSC4G_RIGID_OVERLAP_COCYCLE_RECONSTRUCTION_V0_1",
        "status": "PASS",
        "root": root_id,
        "patch_count": len(ids),
        "supplied_directed_edge_count": len(validated),
        "minimal_tree_edge_count": len(ids) - 1,
        "minimal_continuous_relative_dof": 6 * (len(ids) - 1),
        "charts": charts,
        "max_path_rotation_defect": max_path_rotation_defect,
        "max_path_translation_defect": max_path_translation_defect,
        "max_edge_rotation_defect": max_edge_rotation_defect,
        "max_edge_translation_defect": max_edge_translation_defect,
        "global_se3_gauge_fixed": True,
        "relative_rigid_geometry_reconstructed": True,
        "production_geometry_promoted": False,
    }
