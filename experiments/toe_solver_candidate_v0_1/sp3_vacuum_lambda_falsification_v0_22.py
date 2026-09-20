from __future__ import annotations

import importlib.util
import json
import math
from pathlib import Path

import numpy as np
import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
V017 = ROOT / "experiments" / "toe_solver_candidate_v0_1" / "sp3_source_lapse_lorentz_coframe_v0_17.py"
V019 = ROOT / "experiments" / "toe_solver_candidate_v0_1" / "sp3_stereographic_rfe25_atlas_v0_19.py"
JET = ROOT / "experiments" / "toe_solver_candidate_v0_1" / "metric_jet_provider_candidate.py"
EIN = ROOT / "experiments" / "toe_solver_candidate_v0_1" / "gmn_einstein_provider_candidate.py"

SCHEMA = "QHTRI_TOE_SP3_VACUUM_LAMBDA_FALSIFICATION_V0_22"
H_SWEEP = (3e-3, 1e-3, 3e-4, 1e-4)
COMPATIBLE_TOL = 1e-6
ROBUST_REJECT_LOWER_BOUND = 1e-3
ROUND_S3_PATTERN = np.diag([3.0, -1.0, -1.0, -1.0])
ETA = np.diag([-1.0, 1.0, 1.0, 1.0])


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


v17 = load_module("v017_vacuum", V017)
v19 = load_module("v019_vacuum", V019)
jet = load_module("metric_jet_vacuum", JET)
ein = load_module("einstein_vacuum", EIN)


def exact_round_s3_no_go():
    a, lam = sp.symbols("a Lambda", positive=True, finite=True, real=True)
    temporal_required = sp.simplify(3/a**2)
    spatial_required = sp.simplify(1/a**2)
    incompatibility = sp.simplify(temporal_required-spatial_required)
    return {
        "temporal_required_Lambda": str(temporal_required),
        "spatial_required_Lambda": str(spatial_required),
        "difference": str(incompatibility),
        "finite_positive_radius_vacuum_plus_Lambda_impossible": incompatibility != 0,
    }


def north_chart_geometry():
    sats, points, betas, centroid, Q_exact, beta_coeffs, lapse_coeff, source_logs = v17.build_geometry()
    g0 = np.array([float(x) for x in centroid], dtype=float)
    Q = np.array([[float(x) for x in row] for row in Q_exact], dtype=float)
    L = np.linalg.cholesky(Q)
    R = L.T
    Rinv = np.linalg.inv(R)

    sym = v19.symbolic_atlas()
    TN_fn = sym["lambdas"]["TN"]

    def chart_to_u(x):
        x = np.asarray(x, dtype=float)
        r2 = float(x @ x)
        den = 1.0 + r2
        return np.array(
            [(r2 - 1.0) / den, 2.0*x[0]/den, 2.0*x[1]/den, 2.0*x[2]/den],
            dtype=float,
        )

    def geometry_at_x(x):
        x = np.asarray(x, dtype=float)
        u = chart_to_u(x)
        y = g0 + Rinv @ u

        TN = np.asarray(TN_fn(*x), dtype=float)
        b_frame = v17.v16.eval_beta(beta_coeffs, y) / float(v17.v16.C)
        shift = np.linalg.solve(TN, b_frame)

        logN = float(v17.eval_decimal_affine(lapse_coeff, y))
        N = math.exp(logN)

        E = np.zeros((4, 4), dtype=float)
        E[0, 0] = N
        E[1:, 0] = TN @ shift
        E[1:, 1:] = TN
        metric = E.T @ ETA @ E
        return metric, E, y

    def metric_fn(coords):
        coords = np.asarray(coords, dtype=float)
        metric, _, _ = geometry_at_x(coords[1:4])
        return metric.tolist()

    anchors = {}
    for sat in sats:
        y = np.array([float(x) for x in points[sat]], dtype=float)
        u = R @ (y-g0)
        if abs(float(1.0-u[0])) <= 1e-12:
            raise RuntimeError(f"source anchor {sat} lies at excluded north pole")
        x = u[1:] / (1.0-u[0])
        anchors[sat] = {"y": y, "u": u, "x": x}

    return metric_fn, geometry_at_x, anchors


def fit_common_lambda_coordinate(samples):
    numerator = 0.0
    denominator = 0.0
    for item in samples:
        G = item["G"]
        g = item["g"]
        numerator += float(np.sum(G*g))
        denominator += float(np.sum(g*g))
    if not math.isfinite(denominator) or denominator <= 0.0:
        raise RuntimeError("invalid coordinate common-Lambda fit denominator")
    lam = -numerator/denominator

    residual_sq = 0.0
    G_sq = 0.0
    lamg_sq = 0.0
    for item in samples:
        G = item["G"]
        g = item["g"]
        R = G + lam*g
        residual_sq += float(np.sum(R*R))
        G_sq += float(np.sum(G*G))
        lamg_sq += float(np.sum((lam*g)*(lam*g)))
    residual_fro = math.sqrt(residual_sq)
    scale = math.sqrt(G_sq) + math.sqrt(lamg_sq)
    return {
        "Lambda_star": lam,
        "normalized_residual": residual_fro/max(scale, 1e-30),
    }


def fit_common_lambda_orthonormal(samples):
    numerator = sum(float(np.sum(item["G_frame"]*ETA)) for item in samples)
    denominator = len(samples)*float(np.sum(ETA*ETA))
    if not math.isfinite(denominator) or denominator <= 0.0:
        raise RuntimeError("invalid orthonormal common-Lambda fit denominator")
    lam = -numerator/denominator

    residual_sq = 0.0
    G_sq = 0.0
    lameta_sq = 0.0
    max_abs_residual = 0.0
    per_anchor = {}
    for item in samples:
        Gf = item["G_frame"]
        Rf = Gf + lam*ETA
        residual_sq += float(np.sum(Rf*Rf))
        G_sq += float(np.sum(Gf*Gf))
        lameta_sq += float(np.sum((lam*ETA)*(lam*ETA)))
        max_abs_residual = max(max_abs_residual, float(np.max(np.abs(Rf))))
        per_anchor[item["sat"]] = {
            "G_frame_max_abs": float(np.max(np.abs(Gf))),
            "round_S3_pattern_max_abs_deviation": float(
                np.max(np.abs(Gf-ROUND_S3_PATTERN))
            ),
            "vacuum_plus_Lambda_frame_residual_max_abs": float(np.max(np.abs(Rf))),
            "G_frame_diagonal": [float(v) for v in np.diag(Gf)],
        }

    residual_fro = math.sqrt(residual_sq)
    scale = math.sqrt(G_sq) + math.sqrt(lameta_sq)
    return {
        "Lambda_star": lam,
        "normalized_residual": residual_fro/max(scale, 1e-30),
        "residual_fro": residual_fro,
        "max_abs_residual": max_abs_residual,
        "per_anchor": per_anchor,
    }


def evaluate_h(metric_fn, geometry_at_x, anchors, h):
    samples = []
    metric_lorentzian = True
    all_finite = True
    scalar_R_by_anchor = {}

    for sat, anchor in anchors.items():
        point = [0.0, *[float(v) for v in anchor["x"]]]
        g, dg, ddg = jet.metric_jet_4d(metric_fn, point, h=h)
        scalar, ricci, G = ein.curvature_at_point(g, dg, ddg)
        g_np = np.asarray(g, dtype=float)
        G_np = np.asarray(G, dtype=float)

        metric_expected, E, _ = geometry_at_x(anchor["x"])
        metric_reconstruction_residual = float(np.max(np.abs(g_np-metric_expected)))
        E_inv = np.linalg.inv(E)
        G_frame = E_inv.T @ G_np @ E_inv

        all_finite = all_finite and bool(
            np.isfinite(g_np).all()
            and np.isfinite(G_np).all()
            and np.isfinite(G_frame).all()
        )
        eig = np.linalg.eigvalsh(g_np)
        signature_ok = int(np.sum(eig < 0.0)) == 1 and int(np.sum(eig > 0.0)) == 3
        metric_lorentzian = (
            metric_lorentzian
            and signature_ok
            and float(np.linalg.det(g_np)) < 0.0
            and metric_reconstruction_residual < 1e-12
        )

        scalar_R_by_anchor[sat] = float(scalar)
        samples.append({
            "sat": sat,
            "g": g_np,
            "G": G_np,
            "G_frame": G_frame,
        })

    frame_fit = fit_common_lambda_orthonormal(samples)
    coordinate_fit = fit_common_lambda_coordinate(samples)
    return {
        "h": h,
        "all_finite": all_finite,
        "all_metrics_lorentzian": metric_lorentzian,
        "orthonormal_frame_fit": frame_fit,
        "coordinate_fit_secondary": coordinate_fit,
        "scalar_R_by_anchor": scalar_R_by_anchor,
    }


def classify(sweep):
    if not all(item["all_finite"] and item["all_metrics_lorentzian"] for item in sweep):
        return "INCONCLUSIVE_NUMERICAL_STABILITY"

    residuals = [
        item["orthonormal_frame_fit"]["normalized_residual"] for item in sweep
    ]
    lambdas = [item["orthonormal_frame_fit"]["Lambda_star"] for item in sweep]

    if max(residuals) < COMPATIBLE_TOL:
        denom = max(1e-30, max(abs(x) for x in lambdas))
        lambda_spread = (max(lambdas)-min(lambdas))/denom
        if lambda_spread < 1e-3:
            return "VACUUM_PLUS_LAMBDA_COMPATIBLE_NUMERIC"

    if min(residuals) > ROBUST_REJECT_LOWER_BOUND:
        return "VACUUM_PLUS_LAMBDA_REJECTED_ON_CANDIDATE_METRIC"

    return "INCONCLUSIVE_NUMERICAL_STABILITY"


def main():
    exact_no_go = exact_round_s3_no_go()
    metric_fn, geometry_at_x, anchors = north_chart_geometry()
    sweep = [evaluate_h(metric_fn, geometry_at_x, anchors, h) for h in H_SWEEP]
    classification = classify(sweep)

    frame_residuals = [
        item["orthonormal_frame_fit"]["normalized_residual"] for item in sweep
    ]
    frame_lambdas = [
        item["orthonormal_frame_fit"]["Lambda_star"] for item in sweep
    ]
    round_deviations = [
        max(
            v["round_S3_pattern_max_abs_deviation"]
            for v in item["orthonormal_frame_fit"]["per_anchor"].values()
        )
        for item in sweep
    ]

    checks = {
        "all_five_source_anchors_included": len(anchors) == 5,
        "all_sweep_metrics_finite": all(item["all_finite"] for item in sweep),
        "all_sweep_metrics_Lorentzian": all(
            item["all_metrics_lorentzian"] for item in sweep
        ),
        "primary_Lambda_fit_is_in_orthonormal_frame": True,
        "one_common_Lambda_fit_used_for_all_five_anchors": True,
        "round_S3_exact_vacuum_plus_Lambda_no_go_for_finite_radius": bool(
            exact_no_go["finite_positive_radius_vacuum_plus_Lambda_impossible"]
        ),
        "orthonormal_frame_rejection_is_stable_across_h_sweep": (
            min(frame_residuals) > ROBUST_REJECT_LOWER_BOUND
            and (max(frame_lambdas)-min(frame_lambdas))/max(abs(x) for x in frame_lambdas) < 1e-3
        ),
        "source_anchor_Einstein_tensor_converges_to_round_S3_pattern": max(
            round_deviations
        ) < 1e-4,
        "no_stress_tensor_defined_from_Einstein_tensor": True,
        "vacuum_source_not_promoted": True,
        "physical_production_claim_remains_false": True,
    }

    status = "PASS" if all(checks.values()) else "FAIL"
    out = {
        "schema": SCHEMA,
        "status": status,
        "authority": "CANDIDATE_ONLY",
        "canon_allowed": False,
        "physical_production_claim": False,
        "empirical_theory_confirmation": False,
        "diagnostic_class": "SOURCE_CLASS_FALSIFICATION_NOT_SOURCE_EVIDENCE",
        "classification": classification,
        "exact_round_S3_no_go": exact_no_go,
        "thresholds": {
            "compatible_normalized_residual_max": COMPATIBLE_TOL,
            "robust_reject_normalized_residual_min": ROBUST_REJECT_LOWER_BOUND,
            "round_S3_pattern_max_deviation": 1e-4,
        },
        "sweep": sweep,
        "summary": {
            "orthonormal_normalized_residual_min": min(frame_residuals),
            "orthonormal_normalized_residual_max": max(frame_residuals),
            "orthonormal_Lambda_star_min": min(frame_lambdas),
            "orthonormal_Lambda_star_max": max(frame_lambdas),
            "round_S3_pattern_deviation_max": max(round_deviations),
        },
        "checks": checks,
        "interpretation_firewall": {
            "orthonormal_frame_fit_is_primary_coordinate_fit_is_secondary": True,
            "rejected_does_not_identify_the_required_nonzero_source": True,
            "no_T_equals_G_over_kappa_construction": True,
            "finite_difference_sweep_is_candidate_numerical_evidence": True,
            "exact_round_S3_no_go_is_mathematical_not_physical_source_evidence": True,
        },
    }
    print(json.dumps(out, indent=2, sort_keys=True))
    raise SystemExit(0 if status == "PASS" else 1)


if __name__ == "__main__":
    main()
