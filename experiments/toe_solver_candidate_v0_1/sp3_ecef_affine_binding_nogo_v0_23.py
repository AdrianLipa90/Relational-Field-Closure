from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
V015 = ROOT / "experiments" / "toe_solver_candidate_v0_1" / "sp3_canonical_circumellipsoid_v0_15.py"

SCHEMA = "QHTRI_TOE_SP3_ECEF_AFFINE_BINDING_NOGO_V0_23"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def sha(obj):
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    ).hexdigest()


def main():
    v15 = load_module("v015_ecef_affine_nogo", V015)
    sp3 = v15.sp3
    sats = list(sp3.SAT_IDS)

    points4 = {}
    ecef = {}
    for sat in sats:
        a = [v15.Fraction(x) for x in sp3.REC1[sat]]
        b = [v15.Fraction(x) for x in sp3.REC2[sat]]
        spatial_mid = [(a[i] + b[i]) / 2 for i in range(3)]
        clock_mid_us = (a[3] + b[3]) / 2
        ecef[sat] = np.array([float(v) for v in spatial_mid], dtype=float)
        points4[sat] = tuple(
            spatial_mid + [v15.C * v15.MICROSECOND * clock_mid_us]
        )

    centroid = tuple(
        sum(points4[s][mu] for s in sats) / v15.Fraction(len(sats))
        for mu in range(4)
    )
    centered = {
        s: np.array([float(points4[s][mu] - centroid[mu]) for mu in range(4)], dtype=float)
        for s in sats
    }

    S = np.zeros((4, 4), dtype=float)
    for sat in sats:
        S += np.outer(centered[sat], centered[sat])
    Q = 1.25 * np.linalg.inv(S)
    R = np.linalg.cholesky(Q).T

    u = {sat: R @ centered[sat] for sat in sats}
    chart = {
        sat: u[sat][1:] / (1.0 - u[sat][0])
        for sat in sats
    }

    all_finite = all(np.isfinite(chart[s]).all() for s in sats)
    sphere_residual = max(abs(float(u[s] @ u[s] - 1.0)) for s in sats)

    # Design matrix for affine maps R3 -> R3.
    A5 = np.column_stack([
        np.ones(len(sats), dtype=float),
        np.array([ecef[s] for s in sats], dtype=float),
    ])
    X5 = np.array([chart[s] for s in sats], dtype=float)

    rank5 = int(np.linalg.matrix_rank(A5, tol=1e-10))

    # Four-anchor unique affine fit, fifth-anchor independent test.
    fit_sats = sats[:4]
    test_sat = sats[4]
    A4 = np.column_stack([
        np.ones(4, dtype=float),
        np.array([ecef[s] for s in fit_sats], dtype=float),
    ])
    X4 = np.array([chart[s] for s in fit_sats], dtype=float)
    rank4 = int(np.linalg.matrix_rank(A4, tol=1e-10))

    coeff = np.linalg.solve(A4, X4)
    fit_residual = A4 @ coeff - X4
    max_fit_residual = float(np.max(np.abs(fit_residual)))

    test_row = np.concatenate([[1.0], ecef[test_sat]])
    predicted = test_row @ coeff
    fifth_residual = predicted - chart[test_sat]
    fifth_residual_norm = float(np.linalg.norm(fifth_residual))
    fifth_residual_max_abs = float(np.max(np.abs(fifth_residual)))

    # All-five least-squares fit. If an exact affine map existed, this residual
    # would fall to numerical precision.
    coeff_ls, residuals_ls, rank_ls, singular_values = np.linalg.lstsq(
        A5, X5, rcond=None
    )
    residual_matrix = A5 @ coeff_ls - X5
    ls_max_abs = float(np.max(np.abs(residual_matrix)))
    ls_rms = float(np.sqrt(np.mean(residual_matrix**2)))

    # Left-null compatibility test: A5 has rank 4, so one normalized left-null
    # vector n spans ker(A5^T). Exact affine compatibility requires n^T X5 = 0.
    U, sv, Vt = np.linalg.svd(A5, full_matrices=True)
    left_null = U[:, -1]
    left_null /= np.linalg.norm(left_null)
    compatibility_defect = left_null @ X5
    compatibility_defect_norm = float(np.linalg.norm(compatibility_defect))

    # Scale-aware threshold. Source ECEF coordinates are O(1e4 km), chart
    # coordinates O(1), and observed defects are O(1), so 1e-8 is conservative.
    nogo_floor = 1e-8

    checks = {
        "all_five_candidate_north_chart_coordinates_finite": all_finite,
        "candidate_source_points_remain_on_S3_within_numeric_tolerance": sphere_residual < 1e-12,
        "five_ECEF_midpoints_have_affine_design_rank_four": rank5 == 4,
        "chosen_four_anchor_design_is_invertible": rank4 == 4,
        "four_anchor_affine_fit_recovers_training_anchors_to_roundoff": max_fit_residual < 1e-10,
        "fifth_anchor_rejects_same_affine_map": fifth_residual_norm > nogo_floor,
        "all_five_least_squares_residual_nonzero_above_nogo_floor": ls_max_abs > nogo_floor,
        "left_null_affine_compatibility_condition_fails": compatibility_defect_norm > nogo_floor,
        "no_global_ECEF_to_candidate_chart_affine_binding_on_five_anchors": (
            fifth_residual_norm > nogo_floor
            and ls_max_abs > nogo_floor
            and compatibility_defect_norm > nogo_floor
        ),
        "nonlinear_or_full_3plus1_binding_not_refuted": True,
        "physical_production_claim_remains_false": True,
    }

    status = "PASS" if all(checks.values()) else "FAIL"
    out = {
        "schema": SCHEMA,
        "status": status,
        "authority": "CANDIDATE_ONLY",
        "canon_allowed": False,
        "physical_production_claim": False,
        "result_class": "AFFINE_SPATIAL_BINDING_NOGO_ON_FROZEN_FIVE_ANCHOR_SOURCE",
        "source": {
            "physical_realization_id": sp3.realization_id(),
            "satellites": sats,
            "physical_coordinate": "ECEF midpoint km",
            "candidate_coordinate": "v0.19 north stereographic chart of v0.15 E_Q",
        },
        "metrics": {
            "sphere_max_abs_norm_residual": sphere_residual,
            "design_rank_all_five": rank5,
            "design_rank_fit_four": rank4,
            "training_max_abs_residual": max_fit_residual,
            "fifth_anchor_residual_vector": [float(v) for v in fifth_residual],
            "fifth_anchor_residual_norm": fifth_residual_norm,
            "fifth_anchor_residual_max_abs": fifth_residual_max_abs,
            "all_five_least_squares_max_abs": ls_max_abs,
            "all_five_least_squares_rms": ls_rms,
            "left_null_compatibility_defect": [float(v) for v in compatibility_defect],
            "left_null_compatibility_defect_norm": compatibility_defect_norm,
            "nogo_floor": nogo_floor,
            "design_singular_values": [float(v) for v in singular_values],
        },
        "checks": checks,
        "frontier": {
            "single_global_ECEF_to_candidate_chart_affine_map": "FAIL",
            "nonlinear_spatial_binding": "OPEN",
            "piecewise_atlas_binding": "OPEN",
            "full_3plus1_binding": "OPEN",
            "physical_product_realization": "OPEN_EXTERNAL_SOURCE_EVIDENCE",
        },
        "interpretation_firewall": {
            "affine_no_go_does_not_refute_candidate_carrier": True,
            "affine_no_go_does_not_refute_nonlinear_binding": True,
            "five_anchor_test_is_not_full_domain_physical_validation": True,
        },
    }
    out["receipt_sha256"] = sha(out)
    print(json.dumps(out, indent=2, sort_keys=True))
    raise SystemExit(0 if status == "PASS" else 1)


if __name__ == "__main__":
    main()
