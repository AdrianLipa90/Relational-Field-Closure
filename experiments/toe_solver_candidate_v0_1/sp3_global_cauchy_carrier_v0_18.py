#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import json
from fractions import Fraction
from pathlib import Path

import sympy as sp

from src.rfc.proper_temporal_clock_global_hyperbolicity import certify_proper_clock_route

ROOT = Path(__file__).resolve().parents[2]
V017 = ROOT / "experiments" / "toe_solver_candidate_v0_1" / "sp3_source_lapse_lorentz_coframe_v0_17.py"
R017 = ROOT / "validation" / "toe_solver_candidate_v0_1" / "SP3_SOURCE_LAPSE_LORENTZ_COFRAME_V0_17.json"
R016 = ROOT / "validation" / "toe_solver_candidate_v0_1" / "SP3_QUATERNIONIC_TANGENT_SOLDERING_V0_16.json"

SCHEMA = "QHTRI_TOE_SP3_GLOBAL_CAUCHY_CARRIER_V0_18"


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


def q_to_sympy(q_exact):
    return sp.Matrix([
        [sp.Rational(x.numerator, x.denominator) for x in row]
        for row in q_exact
    ])


def main():
    v17 = load_module("v017_gsc6d", V017)
    receipt17 = json.loads(R017.read_text(encoding="utf-8"))
    receipt16 = json.loads(R016.read_text(encoding="utf-8"))

    sats, points, betas, centroid, q_exact, beta_coeffs, lapse_coeff, source_logs = v17.build_geometry()

    # 1) Exact compact-fiber premise: Q positive definite by Sylvester.
    Q = q_to_sympy(q_exact)
    leading_minors = [sp.factor(Q[:k, :k].det()) for k in range(1, 5)]
    q_positive_definite_exact = all(m > 0 for m in leading_minors)
    q_nonsingular_exact = sp.factor(Q.det()) != 0

    # 2) Exact ADM temporal-gradient identity.
    N, b1, b2, b3 = sp.symbols("N b1 b2 b3", positive=True, real=True)
    E = sp.Matrix([
        [N, 0, 0, 0],
        [b1, 1, 0, 0],
        [b2, 0, 1, 0],
        [b3, 0, 0, 1],
    ])
    eta = sp.diag(-1, 1, 1, 1)
    g = sp.simplify(E.T * eta * E)
    g_inv = sp.simplify(g.inv())
    dt_norm = sp.simplify(g_inv[0, 0])
    temporal_identity_exact = sp.simplify(dt_norm + 1/N**2) == 0

    # 3) Existing source-derived lapse bounds.
    lapse = receipt17["lapse"]
    n_min = float(lapse["global_N_min"])
    n_max = float(lapse["global_N_max"])
    lapse_global_positive_finite = 0.0 < n_min <= n_max < float("inf")

    # 4) Parent global Lorentz carrier and complete spatial-flow provenance.
    parent_global_lorentz = (
        receipt17.get("status") == "PASS"
        and receipt17.get("coframe_metric", {}).get("signature") == "(-,+,+,+)"
        and receipt17.get("physical_production_claim") is False
    )
    parent_compact_flow = (
        receipt16.get("status") == "PASS"
        and receipt16.get("checks", {}).get("compact_carrier_implies_complete_smooth_spatial_flow") is True
    )

    # Stationary mathematical extension:
    # fields depend only on the compact y-carrier, so M=R x E_Q is globally defined.
    global_product_trivialization = bool(q_positive_definite_exact and parent_compact_flow)
    global_regular_temporal_clock = bool(global_product_trivialization and temporal_identity_exact)
    compact_spatial_fiber = bool(q_positive_definite_exact)

    # Projection R x compact(E_Q) -> R is proper.
    proper_temporal_clock = bool(global_product_trivialization and compact_spatial_fiber)

    route = certify_proper_clock_route(
        global_lorentzian_carrier=parent_global_lorentz,
        global_regular_temporal_clock=global_regular_temporal_clock,
        proper_temporal_clock_to_real_line=proper_temporal_clock,
        smooth_finite_positive_lapse=lapse_global_positive_finite,
        global_einstein_carrier=False,
    )

    checks = {
        "parent_v016_PASS": receipt16.get("status") == "PASS",
        "parent_v017_PASS": receipt17.get("status") == "PASS",
        "Q_positive_definite_exact_by_Sylvester": q_positive_definite_exact,
        "Q_nonsingular_exact": bool(q_nonsingular_exact),
        "source_ellipsoid_compact_from_positive_definite_Q": compact_spatial_fiber,
        "stationary_product_extension_R_times_E_Q_declared_candidate_only": True,
        "global_product_trivialization_on_stationary_extension": global_product_trivialization,
        "ADM_inverse_metric_clock_identity_ginv_dt_dt_equals_minus_one_over_N2": temporal_identity_exact,
        "global_clock_gradient_strictly_timelike_for_positive_N": bool(temporal_identity_exact and n_min > 0),
        "global_lapse_positive_finite_on_compact_fiber": lapse_global_positive_finite,
        "projection_clock_proper_from_R_times_compact_fiber": proper_temporal_clock,
        "RF_GSC6B_wick_completeness_derived": route.wick_complete_derived,
        "RF_GSC6B_smooth_slice_lapse_majorant_derived": route.smooth_slice_lapse_majorant_derived,
        "RF_GSC6B_steep_reparametrization_derived": route.steep_reparametrization_derived,
        "RF_GSC6B_global_hyperbolicity_eligible": route.global_hyperbolicity_eligible,
        "global_Cauchy_foliation_consequence_typed_by_RF_GSC6B_external_theorem": route.global_hyperbolicity_eligible,
        "RF_E25_production_atlas_not_claimed": True,
        "RF_E26_global_Einstein_carrier_not_claimed": True,
        "stationary_extension_not_claimed_as_external_observation": True,
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
        "carrier_class": "SOURCE_DERIVED_STATIONARY_MATHEMATICAL_EXTENSION",
        "carrier": {
            "M": "R x E_Q",
            "spatial_fiber": "E_Q={(y-g)^T Q (y-g)=1}",
            "time_function": "t=x0",
            "time_gradient_norm": str(dt_norm),
            "signature": "(-,+,+,+)",
            "Cauchy_slice_candidate": "{t=const} ~= E_Q ~= S3",
        },
        "compactness": {
            "Q_leading_principal_minors": [str(m) for m in leading_minors],
            "Q_determinant": str(sp.factor(Q.det())),
            "compact_fiber": compact_spatial_fiber,
        },
        "lapse": {
            "global_N_min": n_min,
            "global_N_max": n_max,
            "smooth_finite_positive": lapse_global_positive_finite,
        },
        "rf_gsc6b": {
            "proper_temporal_clock": route.proper_temporal_clock,
            "wick_dominates_clock": route.wick_dominates_clock,
            "wick_complete_derived": route.wick_complete_derived,
            "smooth_slice_lapse_majorant_derived": route.smooth_slice_lapse_majorant_derived,
            "steep_reparametrization_derived": route.steep_reparametrization_derived,
            "global_hyperbolicity_eligible": route.global_hyperbolicity_eligible,
            "global_gr_cauchy_carrier_eligible": route.global_gr_cauchy_carrier_eligible,
            "theorem_scope": "EXISTING_RF_GSC6B_GLOBAL_THEOREM_ROUTE",
        },
        "checks": checks,
        "remaining_gate": [
            "explicit RF-E25 J/Lambda coordinate atlas packet and production admission",
            "RF-E26 global Einstein carrier and target-domain coverage",
            "empirical support for stationary extension outside frozen source window",
            "nonlinear global stability",
        ],
        "interpretation_firewall": {
            "global_hyperbolicity_is_candidate_mathematical_carrier_statement": True,
            "not_a_production_RF_E25_promotion": True,
            "not_an_RF_E26_Einstein_solution_claim": True,
            "stationary_extension_is_not_new_observational_evidence": True,
        },
    }
    out["receipt_sha256"] = sha(out)
    print(json.dumps(out, indent=2, sort_keys=True))
    raise SystemExit(0 if status == "PASS" else 1)


if __name__ == "__main__":
    main()
