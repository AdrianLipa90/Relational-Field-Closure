from __future__ import annotations

import hashlib
import importlib.util
import json
from fractions import Fraction
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
CTOR = ROOT / "experiments" / "toe_solver_candidate_v0_1" / "three_plus_one_two_epoch_constructor_v0_13.py"
AFFINE = ROOT / "experiments" / "toe_solver_candidate_v0_1" / "sp3_affine_matching_field_v0_14.py"
ELLIPSOID = ROOT / "experiments" / "toe_solver_candidate_v0_1" / "sp3_canonical_circumellipsoid_v0_15.py"


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


ctor = load_module("ctor_v013", CTOR)
aff = load_module("affine_v014", AFFINE)
ell = load_module("ellipsoid_v015", ELLIPSOID)
sp3 = ctor.sp3

SCHEMA = "QHTRI_TOE_SP3_QUATERNIONIC_TANGENT_SOLDERING_V0_16"
C = Fraction(299792458, 1000)
MICROSECOND = Fraction(1, 10**6)
DT = Fraction(120, 1)

J1 = np.array([
    [0.0, -1.0, 0.0, 0.0],
    [1.0,  0.0, 0.0, 0.0],
    [0.0,  0.0, 0.0, -1.0],
    [0.0,  0.0, 1.0, 0.0],
])
J2 = np.array([
    [0.0, 0.0, -1.0, 0.0],
    [0.0, 0.0,  0.0, 1.0],
    [1.0, 0.0,  0.0, 0.0],
    [0.0, -1.0, 0.0, 0.0],
])
J3 = np.array([
    [0.0, 0.0, 0.0, -1.0],
    [0.0, 0.0, -1.0, 0.0],
    [0.0, 1.0, 0.0, 0.0],
    [1.0, 0.0, 0.0, 0.0],
])
JS = (J1, J2, J3)


def sha(obj):
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    ).hexdigest()


def build_source_geometry():
    sats = list(sp3.SAT_IDS)
    points = {}
    betas = {}
    for sat in sats:
        a = [Fraction(x) for x in sp3.REC1[sat]]
        b = [Fraction(x) for x in sp3.REC2[sat]]
        spatial_mid = [(a[i] + b[i]) / 2 for i in range(3)]
        clock_mid_us = (a[3] + b[3]) / 2
        points[sat] = tuple(spatial_mid + [C * MICROSECOND * clock_mid_us])
        betas[sat] = tuple((b[i] - a[i]) / DT for i in range(3))

    centroid = tuple(
        sum(points[s][mu] for s in sats) / Fraction(len(sats))
        for mu in range(4)
    )
    centered = {
        s: tuple(points[s][mu] - centroid[mu] for mu in range(4))
        for s in sats
    }

    S = [
        [
            sum(centered[s][i] * centered[s][j] for s in sats)
            for j in range(4)
        ]
        for i in range(4)
    ]
    Sinv = ell.inv_exact(S)
    Q = [[Fraction(5, 4) * Sinv[i][j] for j in range(4)] for i in range(4)]

    A = [[Fraction(1)] + list(points[s]) for s in sats]
    coeffs = [
        aff.solve_exact(A, [betas[s][component] for s in sats])
        for component in range(3)
    ]
    return sats, points, betas, centroid, Q, coeffs


def eval_beta(coeffs, y):
    return np.array(
        [
            float(aff.eval_affine(coeffs[k], tuple(Fraction(str(x)) for x in y)))
            for k in range(3)
        ],
        dtype=float,
    )


def main():
    sats, points_exact, betas_exact, centroid_exact, Q_exact, coeffs = build_source_geometry()

    g = np.array([float(x) for x in centroid_exact], dtype=float)
    Q = np.array([[float(x) for x in row] for row in Q_exact], dtype=float)

    # numpy gives Q = L L^T; use R=L^T so Q=R^T R.
    L = np.linalg.cholesky(Q)
    R = L.T
    Rinv = np.linalg.inv(R)

    q_reconstruction_residual = float(np.max(np.abs(R.T @ R - Q)))

    quaternion_skew_residual = max(float(np.max(np.abs(J.T + J))) for J in JS)

    source_samples = [
        np.array([float(x) for x in points_exact[s]], dtype=float)
        for s in sats
    ]

    # Additional deterministic unit-S3 samples, mapped to the ellipsoid.
    raw_u = [
        np.array([1.0, 2.0, 3.0, 4.0]),
        np.array([2.0, -1.0, 1.0, 3.0]),
        np.array([-3.0, 2.0, 1.0, 1.0]),
        np.array([1.0, -4.0, 2.0, -2.0]),
    ]
    extra_samples = []
    for u0 in raw_u:
        u = u0 / np.linalg.norm(u0)
        z = Rinv @ u
        extra_samples.append(g + z)

    samples = source_samples + extra_samples

    max_surface_residual = 0.0
    max_tangent_residual = 0.0
    max_frame_gram_residual = 0.0
    max_dual_residual = 0.0
    max_matching_tangent_residual = 0.0
    max_theta_W_minus_b_residual = 0.0
    max_coframe_annihilation_residual = 0.0
    min_frame_rank = 4

    source_shift_residual = 0.0

    mp = sp3.matching_packet()
    source_shift_map = {
        p["patch_id"]: np.array(p["beta_match"], dtype=float) / float(C)
        for p in mp["patches"]
    }

    for idx, y in enumerate(samples):
        z = y - g
        u = R @ z
        max_surface_residual = max(
            max_surface_residual,
            abs(float(u @ u - 1.0)),
        )

        E = np.column_stack([Rinv @ (J @ u) for J in JS])  # 4x3
        tangent = z @ Q @ E
        max_tangent_residual = max(
            max_tangent_residual,
            float(np.max(np.abs(tangent))),
        )

        gram = E.T @ Q @ E
        max_frame_gram_residual = max(
            max_frame_gram_residual,
            float(np.max(np.abs(gram - np.eye(3)))),
        )
        min_frame_rank = min(min_frame_rank, int(np.linalg.matrix_rank(E, tol=1e-10)))

        theta = E.T @ Q  # 3x4 dual coframe on tangent space
        max_dual_residual = max(
            max_dual_residual,
            float(np.max(np.abs(theta @ E - np.eye(3)))),
        )

        b = eval_beta(coeffs, y) / float(C)
        W = E @ b
        max_matching_tangent_residual = max(
            max_matching_tangent_residual,
            abs(float(z @ Q @ W)),
        )
        max_theta_W_minus_b_residual = max(
            max_theta_W_minus_b_residual,
            float(np.max(np.abs(theta @ W - b))),
        )

        # For X = partial_x0 - W and vartheta^a = theta^a + b^a dx0:
        # vartheta^a(X) = -theta^a(W) + b^a.
        annih = -(theta @ W) + b
        max_coframe_annihilation_residual = max(
            max_coframe_annihilation_residual,
            float(np.max(np.abs(annih))),
        )

        if idx < len(sats):
            sat = sats[idx]
            source_shift_residual = max(
                source_shift_residual,
                float(np.max(np.abs(b - source_shift_map[sat]))),
            )

    checks = {
        "Q_cholesky_reconstruction": q_reconstruction_residual < 1e-10,
        "quaternion_generators_skew": quaternion_skew_residual < 1e-15,
        "all_samples_on_ellipsoid": max_surface_residual < 1e-10,
        "global_frame_is_tangent": max_tangent_residual < 1e-10,
        "global_frame_is_Q_orthonormal": max_frame_gram_residual < 1e-10,
        "global_frame_rank_three_everywhere_sampled": min_frame_rank == 3,
        "dual_coframe_exact_within_numeric_tolerance": max_dual_residual < 1e-10,
        "smooth_matching_vector_is_tangent": max_matching_tangent_residual < 1e-10,
        "dual_coframe_recovers_matching_coefficients": max_theta_W_minus_b_residual < 1e-10,
        "GSC3A_spatial_coframe_annihilation": max_coframe_annihilation_residual < 1e-10,
        "source_anchor_shift_matches_existing_v013_packet": source_shift_residual < 1e-12,
        "compact_carrier_implies_complete_smooth_spatial_flow": True,
        "physical_RF_E25_coframe_identity_not_claimed": True,
    }

    status = "PASS" if all(checks.values()) else "FAIL"
    out = {
        "schema": SCHEMA,
        "status": status,
        "authority": "CANDIDATE_ONLY",
        "canon_allowed": False,
        "physical_production_claim": False,
        "empirical_theory_confirmation": False,
        "source_evidence_class": "EXTERNAL_OBSERVATIONAL_ARCHIVE_DERIVED_TANGENT_SOLDERING_CANDIDATE",
        "construction": {
            "carrier": "(y-g)^T Q (y-g)=1",
            "factorization": "Q=R^T R via positive-diagonal Cholesky",
            "unit_sphere_coordinate": "u=R(y-g)",
            "frame": "e_a=R^{-1} J_a u",
            "dual_coframe": "theta^a(v)=e_a^T Q v",
            "matching_vector": "W=sum_a (B^a/c) e_a",
            "product_matching_field": "X=partial_x0-W",
            "spatial_coframe": "vartheta^a=theta^a+(B^a/c) dx0",
        },
        "residuals": {
            "Q_reconstruction": q_reconstruction_residual,
            "quaternion_skew": quaternion_skew_residual,
            "surface": max_surface_residual,
            "tangent": max_tangent_residual,
            "frame_gram": max_frame_gram_residual,
            "dual": max_dual_residual,
            "matching_tangent": max_matching_tangent_residual,
            "theta_W_minus_b": max_theta_W_minus_b_residual,
            "coframe_annihilation": max_coframe_annihilation_residual,
            "source_shift": source_shift_residual,
        },
        "checks": checks,
        "flow": {
            "carrier_compact": True,
            "matching_field_smooth": True,
            "spatial_flow_complete_by_standard_compact_manifold_theorem": True,
            "GSC3A_interval_complete_candidate_premise": True,
        },
        "remaining_gate": "PHYSICAL_RF_E25_COFRAME_METRIC_IDENTITY_AND_PRODUCTION_ADMISSION",
        "interpretation_firewall": {
            "quaternionic_frame_is_coordinate_canonical_candidate_not_measured_coframe": True,
            "clock_correction_feature_axis_is_not_event_trace_scale": True,
            "global_physical_spacetime_claim_not_made": True,
        },
    }
    out["receipt_sha256"] = sha(out)
    print(json.dumps(out, indent=2, sort_keys=True))
    raise SystemExit(0 if status == "PASS" else 1)


if __name__ == "__main__":
    main()
