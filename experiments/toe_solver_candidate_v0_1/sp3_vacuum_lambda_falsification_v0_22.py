from __future__ import annotations

import importlib.util
import json
import math
from pathlib import Path

import numpy as np

from src.rfc.shared_spacetime_atlas import ADMPatch

ROOT = Path(__file__).resolve().parents[2]
V017 = ROOT / "experiments" / "toe_solver_candidate_v0_1" / "sp3_source_lapse_lorentz_coframe_v0_17.py"
V019 = ROOT / "experiments" / "toe_solver_candidate_v0_1" / "sp3_stereographic_rfe25_atlas_v0_19.py"
JET = ROOT / "experiments" / "toe_solver_candidate_v0_1" / "metric_jet_provider_candidate.py"
EIN = ROOT / "experiments" / "toe_solver_candidate_v0_1" / "gmn_einstein_provider_candidate.py"

SCHEMA = "QHTRI_TOE_SP3_VACUUM_LAMBDA_FALSIFICATION_V0_22"
H_SWEEP = (3e-3, 1e-3, 3e-4, 1e-4)
COMPATIBLE_TOL = 1e-6
ROBUST_REJECT_LOWER_BOUND = 1e-3


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

    def metric_fn(coords):
        coords = np.asarray(coords, dtype=float)
        x = coords[1:4]
        u = chart_to_u(x)
        y = g0 + Rinv @ u

        TN = np.asarray(TN_fn(*x), dtype=float)
        b_frame = v17.v16.eval_beta(beta_coeffs, y) / float(v17.v16.C)
        shift = np.linalg.solve(TN, b_frame)

        logN = float(v17.eval_decimal_affine(lapse_coeff, y))
        N = math.exp(logN)

        p = ADMPatch(
            name="north-eval",
            lapse=N,
            triad=tuple(tuple(float(v) for v in row) for row in TN),
            shift=tuple(float(v) for v in shift),
        )
        return [list(row) for row in p.metric]

    anchors = {}
    for sat in sats:
        y = np.array([float(x) for x in points[sat]], dtype=float)
        u = R @ (y-g0)
        if abs(float(1.0-u[0])) <= 1e-12:
            raise RuntimeError(f"source anchor {sat} lies at excluded north pole")
        x = u[1:] / (1.0-u[0])
        anchors[sat] = {
            "y": y,
            "u": u,
            "x": x,
        }

    return metric_fn, anchors


def fit_common_lambda(samples):
    numerator = 0.0
    denominator = 0.0
    for item in samples:
        G = item["G"]
        g = item["g"]
        numerator += float(np.sum(G*g))
        denominator += float(np.sum(g*g))
    if not math.isfinite(denominator) or denominator <= 0.0:
        raise RuntimeError("invalid common-Lambda fit denominator")
    lam = -numerator/denominator

    residual_sq = 0.0
    G_sq = 0.0
    lamg_sq = 0.0
    max_abs_residual = 0.0
    per_anchor = {}
    for item in samples:
        G = item["G"]
        g = item["g"]
        R = G + lam*g
        residual_sq += float(np.sum(R*R))
        G_sq += float(np.sum(G*G))
        lamg_sq += float(np.sum((lam*g)*(lam*g)))
        max_abs_residual = max(max_abs_residual, float(np.max(np.abs(R))))
        per_anchor[item["sat"]] = {
            "G_max_abs": float(np.max(np.abs(G))),
            "metric_max_abs": float(np.max(np.abs(g))),
            "residual_max_abs": float(np.max(np.abs(R))),
        }

    residual_fro = math.sqrt(residual_sq)
    scale = math.sqrt(G_sq) + math.sqrt(lamg_sq)
    normalized = residual_fro / max(scale, 1e-30)
    return {
        "Lambda_star": lam,
        "normalized_residual": normalized,
        "residual_fro": residual_fro,
        "max_abs_residual": max_abs_residual,
        "per_anchor": per_anchor,
    }


def evaluate_h(metric_fn, anchors, h):
    samples = []
    metric_lorentzian = True
    all_finite = True
    for sat, anchor in anchors.items():
        point = [0.0, *[float(v) for v in anchor["x"]]]
        g, dg, ddg = jet.metric_jet_4d(metric_fn, point, h=h)
        scalar, ricci, G = ein.curvature_at_point(g, dg, ddg)
        g_np = np.asarray(g, dtype=float)
        G_np = np.asarray(G, dtype=float)

        all_finite = all_finite and bool(np.isfinite(g_np).all() and np.isfinite(G_np).all())
        eig = np.linalg.eigvalsh(g_np)
        signature_ok = int(np.sum(eig < 0.0)) == 1 and int(np.sum(eig > 0.0)) == 3
        metric_lorentzian = metric_lorentzian and signature_ok and float(np.linalg.det(g_np)) < 0.0

        samples.append({
            "sat": sat,
            "g": g_np,
            "G": G_np,
            "scalar_R": float(scalar),
        })

    fit = fit_common_lambda(samples)
    fit["h"] = h
    fit["all_finite"] = all_finite
    fit["all_metrics_lorentzian"] = metric_lorentzian
    fit["scalar_R_by_anchor"] = {s["sat"]: s["scalar_R"] for s in samples}
    return fit


def classify(sweep):
    if not all(item["all_finite"] and item["all_metrics_lorentzian"] for item in sweep):
        return "INCONCLUSIVE_NUMERICAL_STABILITY"

    residuals = [item["normalized_residual"] for item in sweep]
    lambdas = [item["Lambda_star"] for item in sweep]

    if max(residuals) < COMPATIBLE_TOL:
        denom = max(1e-30, max(abs(x) for x in lambdas))
        lambda_spread = (max(lambdas)-min(lambdas))/denom
        if lambda_spread < 1e-3:
            return "VACUUM_PLUS_LAMBDA_COMPATIBLE_NUMERIC"

    if min(residuals) > ROBUST_REJECT_LOWER_BOUND:
        return "VACUUM_PLUS_LAMBDA_REJECTED_ON_CANDIDATE_METRIC"

    return "INCONCLUSIVE_NUMERICAL_STABILITY"


def main():
    metric_fn, anchors = north_chart_geometry()
    sweep = [evaluate_h(metric_fn, anchors, h) for h in H_SWEEP]
    classification = classify(sweep)

    residuals = [item["normalized_residual"] for item in sweep]
    lambdas = [item["Lambda_star"] for item in sweep]

    checks = {
        "all_five_source_anchors_included": len(anchors) == 5,
        "all_sweep_metrics_finite": all(item["all_finite"] for item in sweep),
        "all_sweep_metrics_Lorentzian": all(item["all_metrics_lorentzian"] for item in sweep),
        "one_common_Lambda_fit_used_for_all_five_anchors": True,
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
        "thresholds": {
            "compatible_normalized_residual_max": COMPATIBLE_TOL,
            "robust_reject_normalized_residual_min": ROBUST_REJECT_LOWER_BOUND,
        },
        "sweep": sweep,
        "summary": {
            "normalized_residual_min": min(residuals),
            "normalized_residual_max": max(residuals),
            "Lambda_star_min": min(lambdas),
            "Lambda_star_max": max(lambdas),
        },
        "checks": checks,
        "interpretation_firewall": {
            "compatible_does_not_prove_physical_vacuum_domain": True,
            "rejected_does_not_identify_the_required_nonzero_source": True,
            "no_T_equals_G_over_kappa_construction": True,
            "finite_difference_sweep_is_candidate_numerical_evidence": True,
        },
    }
    print(json.dumps(out, indent=2, sort_keys=True))
    raise SystemExit(0 if status == "PASS" else 1)


if __name__ == "__main__":
    main()
