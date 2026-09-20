from __future__ import annotations

import importlib.util
import json
import math
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
V017 = ROOT / "experiments" / "toe_solver_candidate_v0_1" / "sp3_source_lapse_lorentz_coframe_v0_17.py"
V019 = ROOT / "experiments" / "toe_solver_candidate_v0_1" / "sp3_stereographic_rfe25_atlas_v0_19.py"
JET = ROOT / "experiments" / "toe_solver_candidate_v0_1" / "metric_jet_provider_candidate.py"
EIN = ROOT / "experiments" / "toe_solver_candidate_v0_1" / "gmn_einstein_provider_candidate.py"
R019 = ROOT / "validation" / "toe_solver_candidate_v0_1" / "SP3_STEREOGRAPHIC_RFE25_ATLAS_V0_19.json"

SCHEMA = "QHTRI_TOE_SP3_GEOMETRY_SOURCE_SIGNATURE_DIAGNOSTIC_V0_23"
ETA = np.diag([-1.0, 1.0, 1.0, 1.0])
S = np.diag([-1.0, 1.0, 1.0])


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


v17 = load_module("v017_source_signature", V017)
v19 = load_module("v019_source_signature", V019)
jet = load_module("metric_jet_source_signature", JET)
ein = load_module("einstein_source_signature", EIN)


def finite_matrix(a) -> bool:
    x = np.asarray(a, dtype=float)
    return bool(np.isfinite(x).all())


def build_context():
    sats, points, betas, centroid, q_exact, beta_coeffs, lapse_coeff, source_logs = v17.build_geometry()
    g0 = np.array([float(x) for x in centroid], dtype=float)
    Q = np.array([[float(x) for x in row] for row in q_exact], dtype=float)
    R = np.linalg.cholesky(Q).T
    Rinv = np.linalg.inv(R)
    sym = v19.symbolic_atlas()
    return {
        "sats": sats,
        "points": points,
        "g0": g0,
        "Q": Q,
        "R": R,
        "Rinv": Rinv,
        "beta_coeffs": beta_coeffs,
        "lapse_coeff": lapse_coeff,
        "source_logs": source_logs,
        "sym": sym,
    }


CTX = build_context()


def chart_geometry(chart: str, coord3):
    c = np.asarray(coord3, dtype=float)
    if c.shape != (3,) or not np.isfinite(c).all():
        raise ValueError("chart coordinate must be finite length-3")
    r2 = float(c @ c)

    if chart == "N":
        den = 1.0 + r2
        u = np.array([
            (r2 - 1.0) / den,
            2.0*c[0] / den,
            2.0*c[1] / den,
            2.0*c[2] / den,
        ], dtype=float)
        T = np.asarray(CTX["sym"]["lambdas"]["TN"](*c), dtype=float)
    elif chart == "S":
        den = 1.0 + r2
        sc = S @ c
        u = np.array([
            (1.0 - r2) / den,
            2.0*sc[0] / den,
            2.0*sc[1] / den,
            2.0*sc[2] / den,
        ], dtype=float)
        T = np.asarray(CTX["sym"]["lambdas"]["TS"](*c), dtype=float)
    else:
        raise ValueError("chart must be N or S")

    y = CTX["g0"] + CTX["Rinv"] @ u
    b = v17.v16.eval_beta(CTX["beta_coeffs"], y) / float(v17.v16.C)
    logN = float(v17.eval_decimal_affine(CTX["lapse_coeff"], y))
    N = math.exp(logN)

    E = np.zeros((4, 4), dtype=float)
    E[0, 0] = N
    E[1:, 0] = b
    E[1:, 1:] = T
    g = E.T @ ETA @ E

    return {
        "u": u,
        "y": y,
        "N": N,
        "b": np.asarray(b, dtype=float),
        "T": T,
        "E": E,
        "g": g,
    }


def metric_fn(chart: str):
    def fn(point4):
        p = np.asarray(point4, dtype=float)
        if p.shape != (4,):
            raise ValueError("metric point must be length-4")
        return chart_geometry(chart, p[1:])["g"].tolist()
    return fn


def einstein_hat(chart: str, coord3, h: float):
    point = [0.0, *[float(x) for x in coord3]]
    g, dg, ddg = jet.metric_jet_4d(metric_fn(chart), point, h=h)
    scalar, ricci, G = ein.curvature_at_point(g, dg, ddg)
    G = np.asarray(G, dtype=float)
    geom = chart_geometry(chart, coord3)
    F = np.linalg.inv(geom["E"])
    Ghat = F.T @ G @ F
    return {
        "Ghat": Ghat,
        "Gcoord": G,
        "scalar_R": float(scalar),
        "g": np.asarray(g, dtype=float),
        "E": geom["E"],
        "N": geom["N"],
        "u": geom["u"],
    }


def model_diagnostics(Ghat):
    G = np.asarray(Ghat, dtype=float)
    scale = max(float(np.max(np.abs(G))), 1e-18)

    symmetry = float(np.max(np.abs(G - G.T)))
    flux = float(np.max(np.abs(G[0, 1:])))
    spatial = G[1:, 1:]
    spatial_offdiag = spatial - np.diag(np.diag(spatial))
    spatial_offdiag_max = float(np.max(np.abs(spatial_offdiag)))

    rho = float(G[0, 0])
    pvals = np.diag(spatial).astype(float)
    pmean = float(np.mean(pvals))
    anisotropy = float(np.max(np.abs(pvals - pmean)))

    pf_target = np.diag([rho, pmean, pmean, pmean])
    perfect_fluid_residual = float(np.max(np.abs(G - pf_target)))
    perfect_fluid_relative = perfect_fluid_residual / scale

    lambda_fit = float((G[0, 0] - G[1, 1] - G[2, 2] - G[3, 3]) / 4.0)
    lambda_target = np.diag([lambda_fit, -lambda_fit, -lambda_fit, -lambda_fit])
    lambda_residual = float(np.max(np.abs(G - lambda_target)))
    lambda_relative = lambda_residual / scale

    w = None
    if abs(rho) > 1e-18:
        w = pmean / rho

    return {
        "scale_Ghat_max_abs": scale,
        "symmetry_residual": symmetry,
        "flux_max_abs": flux,
        "spatial_offdiag_max_abs": spatial_offdiag_max,
        "rho_like": rho,
        "p_components": [float(x) for x in pvals],
        "p_mean": pmean,
        "anisotropy_max_abs": anisotropy,
        "perfect_fluid_relative_residual": perfect_fluid_relative,
        "lambda_fit": lambda_fit,
        "lambda_relative_residual": lambda_relative,
        "w_p_over_rho": w,
    }


def source_anchor_samples():
    out = []
    for sat in CTX["sats"]:
        y = np.array([float(x) for x in CTX["points"][sat]], dtype=float)
        u = CTX["R"] @ (y - CTX["g0"])
        if float(u[0]) <= 0.0:
            coord = u[1:] / (1.0 - u[0])
            chart = "N"
        else:
            coord = S @ (u[1:] / (1.0 + u[0]))
            chart = "S"
        out.append((f"anchor:{sat}", chart, coord))
    return out


def deterministic_samples():
    base = [
        ("N:origin", "N", np.array([0.0, 0.0, 0.0])),
        ("N:x", "N", np.array([0.30, 0.0, 0.0])),
        ("N:y", "N", np.array([0.0, -0.40, 0.0])),
        ("N:z", "N", np.array([0.0, 0.0, 0.55])),
        ("N:mixed", "N", np.array([0.50, -0.25, 0.35])),
        ("S:origin", "S", np.array([0.0, 0.0, 0.0])),
        ("S:x", "S", np.array([-0.35, 0.0, 0.0])),
        ("S:y", "S", np.array([0.0, 0.45, 0.0])),
        ("S:z", "S", np.array([0.0, 0.0, -0.60])),
        ("S:mixed", "S", np.array([-0.45, 0.30, -0.20])),
    ]
    return base + source_anchor_samples()


def classify(sample_metrics):
    pf = np.array([x["diagnostics"]["perfect_fluid_relative_residual"] for x in sample_metrics], dtype=float)
    lm = np.array([x["diagnostics"]["lambda_relative_residual"] for x in sample_metrics], dtype=float)
    ws = [x["diagnostics"]["w_p_over_rho"] for x in sample_metrics if x["diagnostics"]["w_p_over_rho"] is not None and math.isfinite(x["diagnostics"]["w_p_over_rho"])]

    max_pf = float(np.max(pf))
    median_pf = float(np.median(pf))
    max_lm = float(np.max(lm))
    median_lm = float(np.median(lm))
    median_w = float(np.median(ws)) if ws else None
    max_w_spread = float(np.max(np.abs(np.array(ws)-median_w))) if ws else None

    if max_lm < 1e-2:
        family = "NEAR_LAMBDA_ONLY_ON_FINITE_SAMPLE"
    elif max_pf < 1e-2:
        if median_w is not None and abs(median_w - 1.0/3.0) < 0.05:
            family = "NEAR_COMOVING_RADIATION_LIKE_ON_FINITE_SAMPLE"
        elif median_w is not None and abs(median_w) < 0.05:
            family = "NEAR_COMOVING_DUST_LIKE_ON_FINITE_SAMPLE"
        else:
            family = "NEAR_COMOVING_PERFECT_FLUID_OTHER_W_ON_FINITE_SAMPLE"
    else:
        family = "ANISOTROPIC_OR_FLUX_CARRYING_ON_FINITE_SAMPLE"

    return {
        "family": family,
        "perfect_fluid_relative_residual_max": max_pf,
        "perfect_fluid_relative_residual_median": median_pf,
        "lambda_relative_residual_max": max_lm,
        "lambda_relative_residual_median": median_lm,
        "median_w_p_over_rho": median_w,
        "max_w_spread_from_median": max_w_spread,
    }


def main():
    r19 = json.loads(R019.read_text(encoding="utf-8"))

    h_main = 4e-4
    h_check = 2e-4
    records = []
    max_symmetry_relative = 0.0
    max_step_relative = 0.0

    for label, chart, coord in deterministic_samples():
        a = einstein_hat(chart, coord, h_main)
        b = einstein_hat(chart, coord, h_check)

        if not all(finite_matrix(x) for x in (a["Ghat"], a["Gcoord"], a["g"], a["E"])):
            raise RuntimeError(f"nonfinite metric/Einstein output at {label}")

        diag = model_diagnostics(a["Ghat"])
        scale = max(diag["scale_Ghat_max_abs"], 1e-18)
        symmetry_relative = diag["symmetry_residual"] / scale
        step_relative = float(np.max(np.abs(a["Ghat"] - b["Ghat"]))) / max(
            float(np.max(np.abs(a["Ghat"]))),
            float(np.max(np.abs(b["Ghat"]))),
            1e-18,
        )
        max_symmetry_relative = max(max_symmetry_relative, symmetry_relative)
        max_step_relative = max(max_step_relative, step_relative)

        records.append({
            "label": label,
            "chart": chart,
            "coordinate": [float(x) for x in coord],
            "u": [float(x) for x in a["u"]],
            "lapse": float(a["N"]),
            "scalar_R": float(a["scalar_R"]),
            "Ghat": [[float(v) for v in row] for row in a["Ghat"]],
            "diagnostics": diag,
            "finite_difference_step_relative": step_relative,
        })

    # Same physical point represented in both charts.
    x = np.array([0.40, -0.30, 0.20], dtype=float)
    q = np.asarray(CTX["sym"]["lambdas"]["qmap"](*x), dtype=float).reshape(3)
    gn = einstein_hat("N", x, h_main)
    gs = einstein_hat("S", q, h_main)
    overlap_scale = max(
        float(np.max(np.abs(gn["Ghat"]))),
        float(np.max(np.abs(gs["Ghat"]))),
        1e-18,
    )
    overlap_residual = float(np.max(np.abs(gn["Ghat"] - gs["Ghat"])))
    overlap_relative = overlap_residual / overlap_scale

    aggregate = classify(records)

    checks = {
        "parent_v019_PASS": r19.get("status") == "PASS",
        "all_sample_outputs_finite": True,
        "orthonormal_Einstein_tensor_symmetric_within_numeric_tolerance": max_symmetry_relative < 1e-6,
        "finite_difference_step_stability_below_5_percent": max_step_relative < 5e-2,
        "north_south_overlap_Ghat_agreement_below_5_percent": overlap_relative < 5e-2,
        "diagnostic_does_not_supply_independent_source_provenance": True,
        "diagnostic_does_not_promote_W6": True,
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
        "diagnostic_class": "FINITE_GEOMETRY_DERIVED_SOURCE_SIGNATURE_NOT_W6_EVIDENCE",
        "numerics": {
            "main_metric_jet_step": h_main,
            "check_metric_jet_step": h_check,
            "max_step_relative_change": max_step_relative,
            "max_symmetry_relative_residual": max_symmetry_relative,
            "north_south_overlap_Ghat_relative_residual": overlap_relative,
            "sample_count": len(records),
        },
        "aggregate_source_signature": aggregate,
        "samples": records,
        "checks": checks,
        "frontier": {
            "geometry_implied_source_signature": aggregate["family"],
            "independent_physical_source_packet": "OPEN_EXTERNAL_EVIDENCE",
            "W6": "OPEN",
            "RF_E26": "OPEN",
        },
        "interpretation_firewall": {
            "T_from_geometry_not_used_as_physical_evidence": True,
            "fitted_source_family_is_search_target_only": True,
            "finite_sample_classification_is_not_global_source_theorem": True,
        },
    }
    print(json.dumps(out, indent=2, sort_keys=True))
    raise SystemExit(0 if status == "PASS" else 1)


if __name__ == "__main__":
    main()
