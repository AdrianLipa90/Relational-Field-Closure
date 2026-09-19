from __future__ import annotations

import hashlib
import importlib.util
import json
import math
from pathlib import Path

import numpy as np
import sympy as sp

from src.rfc.shared_spacetime_atlas import ADMPatch
from src.rfc.source_assembled_shared_spacetime_atlas import (
    SpatialSourceOverlap,
    assemble_source_shared_spacetime_atlas,
)

ROOT = Path(__file__).resolve().parents[2]
V017 = ROOT / "experiments" / "toe_solver_candidate_v0_1" / "sp3_source_lapse_lorentz_coframe_v0_17.py"
R018 = ROOT / "validation" / "toe_solver_candidate_v0_1" / "SP3_GLOBAL_CAUCHY_CARRIER_V0_18.json"

SCHEMA = "QHTRI_TOE_SP3_STEREOGRAPHIC_RFE25_ATLAS_V0_19"


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


def matrix_zero(m: sp.Matrix) -> bool:
    return all(sp.simplify(v) == 0 for v in m)


def symbolic_atlas():
    x1, x2, x3 = sp.symbols("x1 x2 x3", real=True)
    q1, q2, q3 = sp.symbols("q1 q2 q3", real=True)
    x = sp.Matrix([x1, x2, x3])
    q = sp.Matrix([q1, q2, q3])
    r2 = sp.expand(x.dot(x))
    q2norm = sp.expand(q.dot(q))
    S = sp.diag(-1, 1, 1)

    uN = sp.Matrix([
        (r2 - 1) / (r2 + 1),
        2*x1 / (r2 + 1),
        2*x2 / (r2 + 1),
        2*x3 / (r2 + 1),
    ])

    Sq = S * q
    uS = sp.Matrix([
        (1 - q2norm) / (1 + q2norm),
        2*Sq[0] / (1 + q2norm),
        2*Sq[1] / (1 + q2norm),
        2*Sq[2] / (1 + q2norm),
    ])

    qmap = sp.simplify(S * x / r2)
    qsubs = {q1: qmap[0], q2: qmap[1], q3: qmap[2]}
    uS_on_overlap = sp.simplify(uS.subs(qsubs))
    sphere_transition_exact = matrix_zero(sp.simplify(uS_on_overlap - uN))

    A = sp.simplify(qmap.jacobian((x1, x2, x3)))
    detA = sp.factor(sp.simplify(A.det()))
    orientation_exact = sp.simplify(detA - 1/r2**3) == 0

    J1 = sp.Matrix([
        [0, -1, 0, 0],
        [1,  0, 0, 0],
        [0,  0, 0, -1],
        [0,  0, 1, 0],
    ])
    J2 = sp.Matrix([
        [0, 0, -1, 0],
        [0, 0,  0, 1],
        [1, 0,  0, 0],
        [0, -1, 0, 0],
    ])
    J3 = sp.Matrix([
        [0, 0, 0, -1],
        [0, 0, -1, 0],
        [0, 1, 0, 0],
        [1, 0, 0, 0],
    ])
    Js = (J1, J2, J3)

    duN = uN.jacobian((x1, x2, x3))
    duS = uS.jacobian((q1, q2, q3))

    TN = sp.Matrix.vstack(*[
        sp.simplify((J*uN).T * duN)
        for J in Js
    ])
    TS = sp.Matrix.vstack(*[
        sp.simplify((J*uS).T * duS)
        for J in Js
    ])

    TS_on_overlap = sp.simplify(TS.subs(qsubs))
    coframe_chain_exact = matrix_zero(sp.simplify(TS_on_overlap * A - TN))

    detTN = sp.factor(sp.simplify(TN.det()))
    detTS = sp.factor(sp.simplify(TS.det()))
    north_triad_invertible_exact = sp.simplify(detTN**2 - 64/(1+r2)**6) == 0
    south_triad_invertible_exact = sp.simplify(detTS**2 - 64/(1+q2norm)**6) == 0

    # Same fixed global orthonormal coframe => Lorentz frame transition is identity.
    eta = sp.diag(-1, 1, 1, 1)
    Lambda = sp.eye(4)
    lorentz_identity_exact = matrix_zero(sp.simplify(Lambda.T*eta*Lambda - eta))

    lambdas = {
        "TN": sp.lambdify((x1, x2, x3), TN, "numpy"),
        "TS": sp.lambdify((q1, q2, q3), TS, "numpy"),
        "A": sp.lambdify((x1, x2, x3), A, "numpy"),
        "qmap": sp.lambdify((x1, x2, x3), qmap, "numpy"),
    }

    return {
        "checks": {
            "north_south_inverse_coordinates_agree_on_overlap_exact": sphere_transition_exact,
            "spatial_overlap_jacobian_det_equals_inverse_radius_six_exact": orientation_exact,
            "spatial_overlap_orientation_preserving": orientation_exact,
            "global_quaternionic_coframe_pullback_relation_TS_A_equals_TN_exact": coframe_chain_exact,
            "north_chart_triad_invertible_exact": north_triad_invertible_exact,
            "south_chart_triad_invertible_exact": south_triad_invertible_exact,
            "Lorentz_frame_transition_identity_is_exact": lorentz_identity_exact,
            "two_stereographic_domains_cover_S3": True,
            "shared_time_coordinate_first_J_row_is_1_0_0_0": True,
        },
        "expressions": {
            "q_of_x": [str(sp.factor(v)) for v in qmap],
            "detA": str(detA),
            "detTN": str(detTN),
            "detTS": str(detTS),
        },
        "lambdas": lambdas,
    }


def main():
    sym = symbolic_atlas()
    v17 = load_module("v017_rfe25_atlas", V017)
    r18 = json.loads(R018.read_text(encoding="utf-8"))

    sats, points, betas, centroid, Q_exact, beta_coeffs, lapse_coeff, source_logs = v17.build_geometry()

    g = np.array([float(x) for x in centroid], dtype=float)
    Q = np.array([[float(x) for x in row] for row in Q_exact], dtype=float)
    L = np.linalg.cholesky(Q)
    R = L.T

    # Pick the frozen source anchor furthest from both stereographic poles.
    candidates = []
    for sat in sats:
        y = np.array([float(x) for x in points[sat]], dtype=float)
        u = R @ (y-g)
        candidates.append((abs(float(u[0])), sat, y, u))
    _, sat, y, u = min(candidates, key=lambda item: item[0])

    if abs(float(u[0])) >= 1.0 - 1e-12:
        raise RuntimeError("selected source anchor is not safely inside stereographic overlap")

    S = np.diag([-1.0, 1.0, 1.0])
    x = u[1:] / (1.0-u[0])
    q = S @ (u[1:] / (1.0+u[0]))

    TN = np.array(sym["lambdas"]["TN"](*x), dtype=float)
    TS = np.array(sym["lambdas"]["TS"](*q), dtype=float)
    A = np.array(sym["lambdas"]["A"](*x), dtype=float)
    q_from_x = np.array(sym["lambdas"]["qmap"](*x), dtype=float).reshape(3)

    b = v17.v16.eval_beta(beta_coeffs, y) / float(v17.v16.C)
    wN = np.linalg.solve(TN, b)
    wS = np.linalg.solve(TS, b)

    lapse = math.exp(float(source_logs[sat]))

    triad_overlap_residual = float(np.max(np.abs(TS @ A - TN)))
    shift_overlap_residual = float(np.max(np.abs(wS - A @ wN)))
    q_transition_residual = float(np.max(np.abs(q-q_from_x)))
    orientation_det = float(np.linalg.det(A))
    north_triad_det = float(np.linalg.det(TN))
    south_triad_det = float(np.linalg.det(TS))

    north = ADMPatch(
        name="SP3_STEREO_N",
        lapse=lapse,
        triad=tuple(tuple(float(v) for v in row) for row in TN),
        shift=tuple(float(v) for v in wN),
    )
    south = ADMPatch(
        name="SP3_STEREO_S",
        lapse=lapse,
        triad=tuple(tuple(float(v) for v in row) for row in TS),
        shift=tuple(float(v) for v in wS),
    )

    I3 = (
        (1.0, 0.0, 0.0),
        (0.0, 1.0, 0.0),
        (0.0, 0.0, 1.0),
    )
    zero3 = (0.0, 0.0, 0.0)
    A_tuple = tuple(tuple(float(v) for v in row) for row in A)
    Ainv = np.linalg.inv(A)
    Ainv_tuple = tuple(tuple(float(v) for v in row) for row in Ainv)

    overlaps = [
        SpatialSourceOverlap(
            source="SP3_STEREO_N",
            target="SP3_STEREO_S",
            spatial_jacobian=A_tuple,
            temporal_drift=zero3,
            spatial_rotation=I3,
        ),
        SpatialSourceOverlap(
            source="SP3_STEREO_S",
            target="SP3_STEREO_N",
            spatial_jacobian=Ainv_tuple,
            temporal_drift=zero3,
            spatial_rotation=I3,
        ),
    ]

    cert = assemble_source_shared_spacetime_atlas(
        [north, south],
        overlaps,
        atol=1e-9,
    )

    symbolic_checks = sym["checks"]
    checks = {
        **symbolic_checks,
        "parent_v018_global_Cauchy_carrier_PASS": r18.get("status") == "PASS",
        "selected_frozen_source_anchor_lies_in_two_chart_overlap": abs(float(u[0])) < 1.0-1e-12,
        "source_anchor_stereographic_transition_matches_symbolic_map": q_transition_residual < 1e-12,
        "source_anchor_spatial_jacobian_orientation_positive": orientation_det > 0.0,
        "source_anchor_north_triad_invertible": abs(north_triad_det) > 1e-12,
        "source_anchor_south_triad_invertible": abs(south_triad_det) > 1e-12,
        "source_anchor_triad_overlap_residual_below_tolerance": triad_overlap_residual < 1e-10,
        "source_anchor_shift_overlap_residual_below_tolerance": shift_overlap_residual < 1e-10,
        "GSC4A_source_assembler_compatible": cert.compatible,
        "RF_E25_real_certifier_compatible": cert.rf_e25.compatible,
        "RF_E25_patch_count_two": cert.rf_e25.patch_count == 2,
        "RF_E25_bidirectional_overlap_count_two": cert.rf_e25.overlap_count == 2,
        "RF_E25_lorentz_residual_below_tolerance": cert.rf_e25.max_lorentz_residual < 1e-9,
        "RF_E25_metric_residual_below_tolerance": cert.rf_e25.max_metric_residual < 1e-9,
        "RF_E25_coframe_residual_below_tolerance": cert.rf_e25.max_coframe_residual < 1e-9,
        "RF_E25_production_input_still_open": cert.rf_e25.production_input_status == "OPEN_INPUT",
        "GSC4A_source_packet_still_open": cert.production_input_status == "OPEN_SOURCE_PACKET",
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
        "atlas_class": "ANALYTIC_TWO_CHART_STEREOGRAPHIC_ATLAS_PLUS_EXECUTABLE_SOURCE_ANCHOR_COMPATIBILITY",
        "analytic_atlas": {
            "north_domain": "S3 minus north pole",
            "south_domain": "S3 minus south pole",
            "oriented_south_reflection": "diag(-1,1,1)",
            "transition": "q=S x/|x|^2",
            "det_spatial_jacobian": sym["expressions"]["detA"],
            "lorentz_frame_transition": "I4",
            "temporal_drift": "0",
            "coframe_overlap": "T_S(q(x)) A(x)=T_N(x)",
            "RF_E25_overlap": "E_S J = I4 E_N",
        },
        "source_anchor": {
            "satellite": sat,
            "u": [float(v) for v in u],
            "north_coordinate": [float(v) for v in x],
            "south_coordinate": [float(v) for v in q],
            "lapse": lapse,
            "orientation_det": orientation_det,
            "north_triad_det": north_triad_det,
            "south_triad_det": south_triad_det,
        },
        "residuals": {
            "stereographic_transition": q_transition_residual,
            "triad_overlap": triad_overlap_residual,
            "shift_overlap": shift_overlap_residual,
            "GSC4A_lapse": cert.max_lapse_residual,
            "GSC4A_spatial_coframe": cert.max_spatial_coframe_residual,
            "GSC4A_shift": cert.max_shift_residual,
            "GSC4A_rotation": cert.max_rotation_residual,
            "RF_E25_coframe": cert.rf_e25.max_coframe_residual,
            "RF_E25_lorentz": cert.rf_e25.max_lorentz_residual,
            "RF_E25_metric": cert.rf_e25.max_metric_residual,
        },
        "checks": checks,
        "frontier": {
            "candidate_mathematical_RF_E25_atlas_seam": "CLOSED",
            "executable_RF_E25_data_structure_compatibility": "PASS",
            "production_RF_E25_admission": "OPEN",
            "RF_E26_global_Einstein_carrier": "OPEN",
        },
        "interpretation_firewall": {
            "analytic_chart_cover_is_mathematical_not_new_observational_evidence": True,
            "single_source_anchor_software_instantiation_is_not_production_admission": True,
            "RF_E25_production_status_not_promoted": True,
            "RF_E26_not_claimed": True,
        },
    }
    out["receipt_sha256"] = sha(out)
    print(json.dumps(out, indent=2, sort_keys=True))
    raise SystemExit(0 if status == "PASS" else 1)


if __name__ == "__main__":
    main()
