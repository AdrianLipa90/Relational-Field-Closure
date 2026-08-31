from __future__ import annotations

from typing import Sequence

import numpy as np

from src.rfc.rigid_overlap_cocycle_reconstruction import RigidEdge, reconstruct_from_cocycle


def _edge_key(e: RigidEdge) -> tuple[str, str]:
    return (e.source, e.target)


def scale_translation_cocycle(edges: Sequence[RigidEdge], scale: float) -> tuple[RigidEdge, ...]:
    lam = float(scale)
    if not np.isfinite(lam) or lam <= 0.0:
        raise ValueError("scale must be finite and positive")
    return tuple(
        RigidEdge(e.source, e.target, np.array(e.rotation, dtype=float), lam * np.array(e.translation, dtype=float))
        for e in edges
    )


def certify_same_incidence_distinct_numeric_cocycles(
    patch_ids: Sequence[str],
    first: Sequence[RigidEdge],
    second: Sequence[RigidEdge],
    *,
    tol: float = 1e-10,
) -> dict:
    first_keys = tuple(sorted(_edge_key(e) for e in first))
    second_keys = tuple(sorted(_edge_key(e) for e in second))
    if first_keys != second_keys:
        raise ValueError("candidate cocycles must use the same directed incidence edge set")

    rec_a = reconstruct_from_cocycle(patch_ids, first, tol=tol)
    rec_b = reconstruct_from_cocycle(patch_ids, second, tol=tol)

    by_a = {_edge_key(e): e for e in first}
    by_b = {_edge_key(e): e for e in second}
    max_rotation_difference = 0.0
    max_translation_difference = 0.0
    for key in first_keys:
        max_rotation_difference = max(
            max_rotation_difference,
            float(np.max(np.abs(by_a[key].rotation - by_b[key].rotation))),
        )
        max_translation_difference = max(
            max_translation_difference,
            float(np.max(np.abs(by_a[key].translation - by_b[key].translation))),
        )

    distinct = max(max_rotation_difference, max_translation_difference) > tol
    return {
        "schema": "RFC_GSC4H_INCIDENCE_NUMERIC_GEOMETRY_NONIDENTIFIABILITY_V0_1",
        "status": "PASS" if distinct else "FAIL",
        "same_patch_set": True,
        "same_directed_incidence_edge_set": True,
        "first_cocycle_certified": rec_a["status"] == "PASS",
        "second_cocycle_certified": rec_b["status"] == "PASS",
        "max_rotation_difference": max_rotation_difference,
        "max_translation_difference": max_translation_difference,
        "distinct_numeric_cocycles": distinct,
        "inequivalent_mod_global_se3": distinct,
        "incidence_identifies_numeric_cocycle": False if distinct else None,
        "numeric_overlap_cocycle_remains_source_bound": True,
        "production_geometry_promoted": False,
    }


def certify_positive_translation_scaling_family(
    patch_ids: Sequence[str],
    edges: Sequence[RigidEdge],
    scale: float,
    *,
    tol: float = 1e-10,
) -> dict:
    scaled = scale_translation_cocycle(edges, scale)
    result = certify_same_incidence_distinct_numeric_cocycles(
        patch_ids, edges, scaled, tol=tol
    )
    result["scale"] = float(scale)
    result["family"] = "POSITIVE_TRANSLATION_SCALING"
    return result
