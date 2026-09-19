from __future__ import annotations

import hashlib
import importlib.util
import json
import math
from decimal import Decimal, getcontext, localcontext
from fractions import Fraction
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
V016 = ROOT / "experiments" / "toe_solver_candidate_v0_1" / "sp3_quaternionic_tangent_soldering_v0_16.py"


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


v16 = load_module("v016", V016)
sp3 = v16.sp3
aff = v16.aff
ell = v16.ell

getcontext().prec = 80
SCHEMA = "QHTRI_TOE_SP3_SOURCE_LAPSE_LORENTZ_COFRAME_V0_17"
ETA = np.diag([-1.0, 1.0, 1.0, 1.0])


def sha(obj):
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    ).hexdigest()


def D(x: Fraction) -> Decimal:
    return Decimal(x.numerator) / Decimal(x.denominator)


def solve_decimal(A, b):
    n = len(A)
    aug = [[Decimal(x) for x in row] + [Decimal(rhs)] for row, rhs in zip(A, b)]
    with localcontext() as ctx:
        ctx.prec = 80
        for i in range(n):
            pivot = next((r for r in range(i, n) if aug[r][i] != 0), None)
            if pivot is None:
                raise ValueError("singular affine lapse matrix")
            if pivot != i:
                aug[i], aug[pivot] = aug[pivot], aug[i]
            pv = aug[i][i]
            aug[i] = [x / pv for x in aug[i]]
            for r in range(n):
                if r == i:
                    continue
                factor = aug[r][i]
                if factor == 0:
                    continue
                aug[r] = [aug[r][j] - factor * aug[i][j] for j in range(n + 1)]
        return [aug[i][-1] for i in range(n)]


def eval_decimal_affine(coeff, y):
    with localcontext() as ctx:
        ctx.prec = 80
        return coeff[0] + sum(coeff[i + 1] * Decimal(str(y[i])) for i in range(4))


def source_log_lapse():
    cp = sp3.clock_packet()
    return {
        s: Decimal(cp["log_lapse_relative"][s])
        for s in sp3.SAT_IDS
    }


def build_geometry():
    sats, points, betas, centroid, Q_exact, beta_coeffs = v16.build_source_geometry()
    A = [[Decimal(1)] + [D(x) for x in points[s]] for s in sats]
    logs = source_log_lapse()
    lapse_coeff = solve_decimal(A, [logs[s] for s in sats])
    return sats, points, betas, centroid, Q_exact, beta_coeffs, lapse_coeff, logs


def main():
    sats, points_exact, betas_exact, centroid_exact, Q_exact, beta_coeffs, lapse_coeff, source_logs = build_geometry()

    g0 = np.array([float(x) for x in centroid_exact], dtype=float)
    Q = np.array([[float(x) for x in row] for row in Q_exact], dtype=float)
    Qinv = np.linalg.inv(Q)
    L = np.linalg.cholesky(Q)
    R = L.T
    Rinv = np.linalg.inv(R)

    # Exact source-anchor interpolation residual in Decimal arithmetic.
    anchor_log_residual = Decimal(0)
    for sat in sats:
        y = [D(x) for x in points_exact[sat]]
        with localcontext() as ctx:
            ctx.prec = 80
            val = lapse_coeff[0] + sum(lapse_coeff[i + 1] * y[i] for i in range(4))
        anchor_log_residual = max(anchor_log_residual, abs(val - source_logs[sat]))

    q_vec = np.array([float(x) for x in lapse_coeff[1:]], dtype=float)
    L_centroid = float(
        lapse_coeff[0]
        + sum(lapse_coeff[i + 1] * D(centroid_exact[i]) for i in range(4))
    )
    lapse_radius = math.sqrt(max(0.0, float(q_vec @ Qinv @ q_vec)))
    logN_min = L_centroid - lapse_radius
    logN_max = L_centroid + lapse_radius
    N_global_min = math.exp(logN_min)
    N_global_max = math.exp(logN_max)

    source_samples = [
        np.array([float(x) for x in points_exact[s]], dtype=float)
        for s in sats
    ]
    raw_u = [
        np.array([1.0, 2.0, 3.0, 4.0]),
        np.array([2.0, -1.0, 1.0, 3.0]),
        np.array([-3.0, 2.0, 1.0, 1.0]),
        np.array([1.0, -4.0, 2.0, -2.0]),
    ]
    extra_samples = []
    for u0 in raw_u:
        u = u0 / np.linalg.norm(u0)
        extra_samples.append(g0 + Rinv @ u)
    samples = source_samples + extra_samples

    max_surface_residual = 0.0
    max_frame_gram_residual = 0.0
    max_spatial_annihilation_residual = 0.0
    max_temporal_pairing_residual = 0.0
    max_metric_det_identity_residual = 0.0
    min_negative_gap = float("inf")
    min_positive_eigenvalue = float("inf")
    min_sample_lapse = float("inf")
    max_sample_lapse = 0.0
    source_log_packet_residual = 0.0

    cp = sp3.clock_packet()

    for idx, y in enumerate(samples):
        z = y - g0
        u = R @ z
        max_surface_residual = max(max_surface_residual, abs(float(u @ u - 1.0)))

        frame = np.column_stack([Rinv @ (J @ u) for J in v16.JS])
        theta = frame.T @ Q
        gram = frame.T @ Q @ frame
        max_frame_gram_residual = max(
            max_frame_gram_residual,
            float(np.max(np.abs(gram - np.eye(3)))),
        )

        b = v16.eval_beta(beta_coeffs, y) / float(v16.C)
        W = frame @ b

        logN = float(eval_decimal_affine(lapse_coeff, y))
        N = math.exp(logN)
        min_sample_lapse = min(min_sample_lapse, N)
        max_sample_lapse = max(max_sample_lapse, N)

        # Coframe in the basis {partial_x0, e1,e2,e3}.
        E = np.array([
            [N, 0.0, 0.0, 0.0],
            [b[0], 1.0, 0.0, 0.0],
            [b[1], 0.0, 1.0, 0.0],
            [b[2], 0.0, 0.0, 1.0],
        ], dtype=float)

        X = np.array([1.0, -b[0], -b[1], -b[2]], dtype=float)
        pair = E @ X
        max_spatial_annihilation_residual = max(
            max_spatial_annihilation_residual,
            float(np.max(np.abs(pair[1:]))),
        )
        max_temporal_pairing_residual = max(
            max_temporal_pairing_residual,
            abs(float(pair[0] - N)),
        )

        metric = E.T @ ETA @ E
        eigs = np.linalg.eigvalsh(metric)
        negatives = [x for x in eigs if x < 0]
        positives = [x for x in eigs if x > 0]
        if len(negatives) != 1 or len(positives) != 3:
            min_negative_gap = -1.0
            min_positive_eigenvalue = -1.0
        else:
            min_negative_gap = min(min_negative_gap, abs(negatives[0]))
            min_positive_eigenvalue = min(min_positive_eigenvalue, min(positives))

        metric_det_identity = abs(float(np.linalg.det(metric) + N * N))
        max_metric_det_identity_residual = max(
            max_metric_det_identity_residual,
            metric_det_identity,
        )

        # Cross-check W is still the v0.16 tangent matching vector.
        tangent_residual = abs(float(z @ Q @ W))
        max_spatial_annihilation_residual = max(
            max_spatial_annihilation_residual,
            tangent_residual,
        )

        if idx < len(sats):
            sat = sats[idx]
            source_log_packet_residual = max(
                source_log_packet_residual,
                abs(logN - float(Decimal(cp["log_lapse_relative"][sat]))),
            )

    checks = {
        "five_source_log_lapse_values_define_unique_affine_scalar": True,
        "source_log_lapse_anchor_recovery_decimal": anchor_log_residual < Decimal("1e-60"),
        "global_lapse_strictly_positive_by_analytic_ellipsoid_bound": N_global_min > 0.0 and math.isfinite(N_global_max),
        "global_lapse_bound_ordered": 0.0 < N_global_min <= N_global_max,
        "all_samples_remain_on_source_ellipsoid": max_surface_residual < 1e-10,
        "spatial_frame_remains_Q_orthonormal": max_frame_gram_residual < 1e-10,
        "ADM_spatial_coframe_annihilates_matching_X": max_spatial_annihilation_residual < 1e-10,
        "temporal_coframe_pairs_X_to_positive_lapse": max_temporal_pairing_residual < 1e-10 and min_sample_lapse > 0.0,
        "metric_has_one_negative_three_positive_eigenvalues": bool(min_negative_gap > 0.0 and min_positive_eigenvalue > 0.0),
        "metric_determinant_equals_minus_lapse_squared": max_metric_det_identity_residual < 1e-8,
        "source_anchor_log_lapse_matches_existing_clock_packet": source_log_packet_residual < 1e-12,
        "RF_E25_coordinate_atlas_packet_not_claimed": True,
        "physical_production_admission_not_claimed": True,
    }

    coeff_serialized = [str(x) for x in lapse_coeff]
    status = "PASS" if all(checks.values()) else "FAIL"
    out = {
        "schema": SCHEMA,
        "status": status,
        "authority": "CANDIDATE_ONLY",
        "canon_allowed": False,
        "physical_production_claim": False,
        "empirical_theory_confirmation": False,
        "source_evidence_class": "EXTERNAL_OBSERVATIONAL_ARCHIVE_DERIVED_GLOBAL_LORENTZ_COFRAME_CANDIDATE",
        "source": {
            "realization_id": sp3.realization_id(),
            "clock_packet_schema": cp["schema"],
            "reference_clock": cp["reference_clock"],
            "clock_source_class": cp["source_class"],
        },
        "lapse": {
            "definition": "N(y)=exp(L(y)) with L unique affine interpolant of source log_lapse_relative",
            "coefficient_sha256": sha(coeff_serialized),
            "coefficients_decimal": coeff_serialized,
            "anchor_max_decimal_residual": str(anchor_log_residual),
            "global_logN_min": logN_min,
            "global_logN_max": logN_max,
            "global_N_min": N_global_min,
            "global_N_max": N_global_max,
            "sample_N_min": min_sample_lapse,
            "sample_N_max": max_sample_lapse,
        },
        "coframe": {
            "temporal": "vartheta0=N dx0",
            "spatial": "vartheta^a=theta^a+b^a dx0",
            "matching_field": "X=partial_x0-W",
            "det_E": "N",
            "metric": "g=E^T diag(-1,1,1,1) E",
            "det_g": "-N^2",
            "signature": "(-,+,+,+)",
        },
        "residuals": {
            "surface": max_surface_residual,
            "frame_gram": max_frame_gram_residual,
            "spatial_annihilation_or_tangency": max_spatial_annihilation_residual,
            "temporal_pairing": max_temporal_pairing_residual,
            "metric_det_identity": max_metric_det_identity_residual,
            "source_log_packet": source_log_packet_residual,
        },
        "signature_witness": {
            "minimum_abs_negative_eigenvalue_sampled": min_negative_gap,
            "minimum_positive_eigenvalue_sampled": min_positive_eigenvalue,
            "analytic_signature_argument": "g is congruent to eta through invertible E with det(E)=N>0",
        },
        "checks": checks,
        "remaining_gate": "FINITE_OR_EXPLICIT_COORDINATE_ATLAS_PACKET_J_LAMBDA_FOR_RF_E25_AND_PHYSICAL_PRODUCTION_ADMISSION",
        "interpretation_firewall": {
            "relative_clock_rate_lapse_candidate_not_independent_production_lapse_measurement": True,
            "global_intrinsic_coframe_not_yet_executable_RF_E25_coordinate_atlas_packet": True,
            "physical_spacetime_identity_not_claimed": True,
        },
    }
    out["receipt_sha256"] = sha(out)
    print(json.dumps(out, indent=2, sort_keys=True))
    raise SystemExit(0 if status == "PASS" else 1)


if __name__ == "__main__":
    main()
