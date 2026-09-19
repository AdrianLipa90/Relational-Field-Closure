from __future__ import annotations

import importlib.util
import json
import math
from pathlib import Path

import numpy as np

from src.rfc.shared_spacetime_atlas import ADMPatch

ROOT = Path(__file__).resolve().parents[2]
V022 = ROOT / "experiments" / "toe_solver_candidate_v0_1" / "sp3_vacuum_lambda_falsification_v0_22.py"

SCHEMA = "QHTRI_TOE_SP3_DUST_LAMBDA_SOURCE_CLASS_V0_23"
H_SWEEP = (3e-3, 1e-3, 3e-4, 1e-4)

COMPATIBLE_RESIDUAL_TOL = 1e-4
COMPATIBLE_OFFDIAGONAL_TOL = 1e-4
COMPATIBLE_ANISOTROPY_TOL = 1e-4
COMPATIBLE_PARAMETER_RELATIVE_SPREAD = 1e-3
ROBUST_REJECT_RESIDUAL_LOWER_BOUND = 1e-2


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


v22 = load_module("v022_dust_lambda", V022)


def source_geometry_context():
    metric_fn, anchors = v22.north_chart_geometry()
    sats, points, betas, centroid, Q_exact, beta_coeffs, lapse_coeff, source_logs = (
        v22.v17.build_geometry()
    )
    sym = v22.v19.symbolic_atlas()
    TN_fn = sym["lambdas"]["TN"]
    return metric_fn, anchors, beta_coeffs, lapse_coeff, TN_fn


def coframe_at_anchor(anchor, beta_coeffs, lapse_coeff, TN_fn):
    x = np.asarray(anchor["x"], dtype=float)
    y = np.asarray(anchor["y"], dtype=float)
    TN = np.asarray(TN_fn(*x), dtype=float)

    b_frame = (
        v22.v17.v16.eval_beta(beta_coeffs, y)
        / float(v22.v17.v16.C)
    )
    shift = np.linalg.solve(TN, b_frame)
    logN = float(v22.v17.eval_decimal_affine(lapse_coeff, y))
    lapse = math.exp(logN)

    patch = ADMPatch(
        name="dust-lambda-eval",
        lapse=lapse,
        triad=tuple(tuple(float(v) for v in row) for row in TN),
        shift=tuple(float(v) for v in shift),
    )
    E = np.asarray(patch.coframe, dtype=float)
    return E, np.asarray(patch.metric, dtype=float)


def orthonormal_einstein(G_coord, E):
    Einv = np.linalg.inv(E)
    return Einv.T @ np.asarray(G_coord, dtype=float) @ Einv


def fit_common_dust_lambda(ghats):
    spatial = []
    temporal = []
    for item in ghats:
        Ghat = item["Ghat"]
        temporal.append(float(Ghat[0, 0]))
        spatial.extend(float(Ghat[i, i]) for i in range(1, 4))

    lam = -float(np.mean(spatial))
    A = float(np.mean(temporal)) - lam
    model = np.diag([A + lam, -lam, -lam, -lam])

    residual_sq = 0.0
    g_sq = 0.0
    model_sq = 0.0
    max_abs_residual = 0.0
    max_offdiag = 0.0
    max_spatial_anisotropy = 0.0
    per_anchor = {}

    for item in ghats:
        sat = item["sat"]
        Ghat = item["Ghat"]
        R = Ghat - model

        residual_sq += float(np.sum(R * R))
        g_sq += float(np.sum(Ghat * Ghat))
        model_sq += float(np.sum(model * model))
        max_abs_residual = max(max_abs_residual, float(np.max(np.abs(R))))

        offdiag = Ghat - np.diag(np.diag(Ghat))
        anchor_offdiag = float(np.max(np.abs(offdiag)))
        max_offdiag = max(max_offdiag, anchor_offdiag)

        spatial_diag = np.diag(Ghat)[1:4]
        anis = float(np.max(spatial_diag) - np.min(spatial_diag))
        max_spatial_anisotropy = max(max_spatial_anisotropy, abs(anis))

        per_anchor[sat] = {
            "Ghat": Ghat.tolist(),
            "Ghat_diag": [float(v) for v in np.diag(Ghat)],
            "offdiag_max_abs": anchor_offdiag,
            "spatial_diag_anisotropy": anis,
            "model_residual_max_abs": float(np.max(np.abs(R))),
        }

    residual_fro = math.sqrt(residual_sq)
    norm_scale = math.sqrt(g_sq) + math.sqrt(model_sq)
    normalized_residual = residual_fro / max(norm_scale, 1e-30)

    return {
        "Lambda_star": lam,
        "A_star_kappa_rho": A,
        "normalized_residual": normalized_residual,
        "residual_fro": residual_fro,
        "max_abs_residual": max_abs_residual,
        "max_offdiag": max_offdiag,
        "max_spatial_anisotropy": max_spatial_anisotropy,
        "per_anchor": per_anchor,
    }


def evaluate_h(metric_fn, anchors, beta_coeffs, lapse_coeff, TN_fn, h):
    ghats = []
    metric_coframe_residual = 0.0
    all_finite = True
    all_lorentzian = True

    for sat, anchor in anchors.items():
        point = [0.0, *[float(v) for v in anchor["x"]]]
        g, dg, ddg = v22.jet.metric_jet_4d(metric_fn, point, h=h)
        scalar, ricci, G = v22.ein.curvature_at_point(g, dg, ddg)

        g_np = np.asarray(g, dtype=float)
        G_np = np.asarray(G, dtype=float)
        E, g_from_coframe = coframe_at_anchor(
            anchor, beta_coeffs, lapse_coeff, TN_fn
        )

        metric_coframe_residual = max(
            metric_coframe_residual,
            float(np.max(np.abs(g_np - g_from_coframe))),
        )

        Ghat = orthonormal_einstein(G_np, E)
        all_finite = all_finite and bool(
            np.isfinite(g_np).all()
            and np.isfinite(G_np).all()
            and np.isfinite(Ghat).all()
        )

        eig = np.linalg.eigvalsh(g_np)
        all_lorentzian = all_lorentzian and (
            int(np.sum(eig < 0.0)) == 1
            and int(np.sum(eig > 0.0)) == 3
            and float(np.linalg.det(g_np)) < 0.0
        )

        ghats.append(
            {
                "sat": sat,
                "Ghat": Ghat,
                "scalar_R": float(scalar),
            }
        )

    fit = fit_common_dust_lambda(ghats)
    fit.update(
        {
            "h": h,
            "all_finite": all_finite,
            "all_metrics_lorentzian": all_lorentzian,
            "metric_coframe_residual": metric_coframe_residual,
            "scalar_R_by_anchor": {
                item["sat"]: item["scalar_R"] for item in ghats
            },
        }
    )
    return fit


def relative_spread(values):
    values = [float(v) for v in values]
    denom = max(1e-30, max(abs(v) for v in values))
    return (max(values) - min(values)) / denom


def classify(sweep):
    if not all(
        item["all_finite"] and item["all_metrics_lorentzian"]
        for item in sweep
    ):
        return "INCONCLUSIVE_NUMERICAL_STABILITY"

    residuals = [item["normalized_residual"] for item in sweep]
    offdiags = [item["max_offdiag"] for item in sweep]
    anisotropies = [item["max_spatial_anisotropy"] for item in sweep]
    lambdas = [item["Lambda_star"] for item in sweep]
    As = [item["A_star_kappa_rho"] for item in sweep]

    lambda_spread = relative_spread(lambdas)
    A_spread = relative_spread(As)

    if (
        max(residuals) < COMPATIBLE_RESIDUAL_TOL
        and max(offdiags) < COMPATIBLE_OFFDIAGONAL_TOL
        and max(anisotropies) < COMPATIBLE_ANISOTROPY_TOL
        and lambda_spread < COMPATIBLE_PARAMETER_RELATIVE_SPREAD
        and A_spread < COMPATIBLE_PARAMETER_RELATIVE_SPREAD
        and min(As) > 0.0
    ):
        return "DUST_PLUS_LAMBDA_EFFECTIVE_CLASS_COMPATIBLE_NUMERIC"

    if min(residuals) > ROBUST_REJECT_RESIDUAL_LOWER_BOUND:
        return "DUST_PLUS_LAMBDA_EFFECTIVE_CLASS_REJECTED_NUMERIC"

    return "INCONCLUSIVE_NUMERICAL_STABILITY"


def main():
    metric_fn, anchors, beta_coeffs, lapse_coeff, TN_fn = (
        source_geometry_context()
    )
    sweep = [
        evaluate_h(
            metric_fn,
            anchors,
            beta_coeffs,
            lapse_coeff,
            TN_fn,
            h,
        )
        for h in H_SWEEP
    ]

    classification = classify(sweep)
    residuals = [item["normalized_residual"] for item in sweep]
    offdiags = [item["max_offdiag"] for item in sweep]
    anisotropies = [item["max_spatial_anisotropy"] for item in sweep]
    lambdas = [item["Lambda_star"] for item in sweep]
    As = [item["A_star_kappa_rho"] for item in sweep]

    checks = {
        "all_five_source_anchors_included": len(anchors) == 5,
        "all_sweep_metrics_finite": all(item["all_finite"] for item in sweep),
        "all_sweep_metrics_Lorentzian": all(
            item["all_metrics_lorentzian"] for item in sweep
        ),
        "coframe_metric_matches_metric_callable": max(
            item["metric_coframe_residual"] for item in sweep
        ) < 1e-10,
        "one_common_Lambda_and_A_fit_used_for_all_five_anchors": True,
        "effective_source_class_only_not_W6_evidence": True,
        "no_physical_dust_source_claim": True,
        "no_physical_cosmological_constant_claim": True,
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
        "diagnostic_class": "EFFECTIVE_SOURCE_CLASS_NOT_PHYSICAL_SOURCE_EVIDENCE",
        "classification": classification,
        "thresholds": {
            "compatible_normalized_residual_max": COMPATIBLE_RESIDUAL_TOL,
            "compatible_offdiagonal_max": COMPATIBLE_OFFDIAGONAL_TOL,
            "compatible_spatial_anisotropy_max": COMPATIBLE_ANISOTROPY_TOL,
            "compatible_parameter_relative_spread_max": COMPATIBLE_PARAMETER_RELATIVE_SPREAD,
            "robust_reject_normalized_residual_min": ROBUST_REJECT_RESIDUAL_LOWER_BOUND,
        },
        "ideal_unit_static_S3_reference": {
            "Ghat": [[3.0,0.0,0.0,0.0],[0.0,-1.0,0.0,0.0],[0.0,0.0,-1.0,0.0],[0.0,0.0,0.0,-1.0]],
            "Lambda": 1.0,
            "A_kappa_rho": 2.0,
            "imposed_as_fit_value": False,
        },
        "sweep": sweep,
        "summary": {
            "normalized_residual_min": min(residuals),
            "normalized_residual_max": max(residuals),
            "max_offdiag_max": max(offdiags),
            "max_spatial_anisotropy_max": max(anisotropies),
            "Lambda_star_min": min(lambdas),
            "Lambda_star_max": max(lambdas),
            "Lambda_relative_spread": relative_spread(lambdas),
            "A_star_kappa_rho_min": min(As),
            "A_star_kappa_rho_max": max(As),
            "A_relative_spread": relative_spread(As),
        },
        "checks": checks,
        "frontier": {
            "effective_required_source_class": classification,
            "actual_independent_W6_source_evidence": "OPEN",
        },
        "interpretation_firewall": {
            "effective_fit_is_not_independent_source_provenance": True,
            "normalized_Lambda_is_not_observed_cosmological_constant": True,
            "normalized_A_is_not_SI_density_without_scale_binding": True,
            "W6_v021_contract_still_required": True,
        },
    }
    print(json.dumps(out, indent=2, sort_keys=True))
    raise SystemExit(0 if status == "PASS" else 1)


if __name__ == "__main__":
    main()
