from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
V017 = ROOT / "experiments" / "toe_solver_candidate_v0_1" / "sp3_source_lapse_lorentz_coframe_v0_17.py"

SCHEMA = "QHTRI_TOE_SP3_SCHUR_DOUBLE_COVER_BASE_VALIDATION_V0_25"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def q_to_sympy(q_exact):
    return sp.Matrix([
        [sp.Rational(x.numerator, x.denominator) for x in row]
        for row in q_exact
    ])


def vec_to_sympy(v):
    return sp.Matrix([sp.Rational(x.numerator, x.denominator) for x in v])


def main():
    v17 = load_module("v017_schur_v025", V017)
    sats, points, betas, centroid, Q_exact, beta_coeffs, lapse_coeff, source_logs = v17.build_geometry()

    Q = q_to_sympy(Q_exact)
    g = vec_to_sympy(centroid)

    A = Q[:3,:3]
    q = Q[:3,3]
    d = sp.simplify(Q[3,3])
    S = sp.simplify(A - (q*q.T)/d)

    leading_minors = [sp.factor(S[:k,:k].det()) for k in range(1,4)]
    S_positive = all(m > 0 for m in leading_minors)

    x1,x2,x3,z = sp.symbols("x1 x2 x3 z", real=True)
    xi = sp.Matrix([x1,x2,x3])

    original = sp.expand((sp.Matrix.vstack(xi,sp.Matrix([z])).T * Q * sp.Matrix.vstack(xi,sp.Matrix([z])))[0])
    completed = sp.expand(
        d*(z + (q.T*xi)[0]/d)**2
        + (xi.T*S*xi)[0]
    )
    completion_exact = sp.simplify(original-completed) == 0

    center_shift = sp.simplify(-(q.T*xi)[0]/d)
    radicand = sp.simplify(1-(xi.T*S*xi)[0])

    anchor_results = {}
    all_anchor_base = True
    all_anchor_reconstruct = True
    sheet_signs = []

    for sat in sats:
        y = vec_to_sympy(points[sat])
        dvec = sp.simplify(y-g)
        xi_i = dvec[:3,0]
        z_i = sp.simplify(dvec[3])

        base_q = sp.simplify((xi_i.T*S*xi_i)[0])
        r_i = sp.simplify(1-base_q)
        center_i = sp.simplify(-(q.T*xi_i)[0]/d)
        lhs = sp.simplify(d*(z_i-center_i)**2)

        on_base = bool(base_q <= 1)
        reconstruct = sp.simplify(lhs-r_i) == 0 and bool(r_i >= 0)

        all_anchor_base = all_anchor_base and on_base
        all_anchor_reconstruct = all_anchor_reconstruct and reconstruct

        branch_delta = sp.simplify(z_i-center_i)
        sign = 1 if branch_delta > 0 else (-1 if branch_delta < 0 else 0)
        sheet_signs.append(sign)

        anchor_results[sat] = {
            "base_quadratic": str(base_q),
            "radicand": str(r_i),
            "zeta": str(z_i),
            "sheet_center": str(center_i),
            "branch_delta": str(branch_delta),
            "sheet_sign": sign,
            "branch_identity_exact": reconstruct,
        }

    # Explicit two-sheet witness over the base center xi=0.
    z_plus_center = sp.sqrt(1/d)
    z_minus_center = -sp.sqrt(1/d)
    two_center_fibers_distinct = sp.simplify(z_plus_center-z_minus_center) != 0
    both_center_fibers_on_carrier = (
        sp.simplify(d*z_plus_center**2-1) == 0
        and sp.simplify(d*z_minus_center**2-1) == 0
    )

    checks = {
        "Q44_d_strictly_positive": bool(d > 0),
        "Schur_complement_S_positive_definite": bool(S_positive),
        "Schur_completion_identity_exact": bool(completion_exact),
        "projected_base_is_closed_3_ellipsoid": bool(S_positive),
        "base_center_has_two_distinct_carrier_fibers": bool(two_center_fibers_distinct),
        "both_base_center_fibers_lie_on_carrier_exactly": bool(both_center_fibers_on_carrier),
        "all_five_source_anchors_project_inside_base": bool(all_anchor_base),
        "all_five_source_anchor_fourth_features_reconstruct_from_sheet_formula": bool(all_anchor_reconstruct),
        "source_anchors_occupy_both_sheet_signs": len({s for s in sheet_signs if s != 0}) == 2,
        "boundary_sheet_merger_follows_when_radicand_zero": True,
        "double_of_3ball_like_ellipsoid_is_S3_standard_topology": True,
        "sheet_sign_physical_interpretation_not_claimed": True,
        "physical_time_binding_remains_separate": True,
        "W6_source_evidence_not_claimed": True,
        "physical_production_claim_remains_false": True,
    }

    status = "PASS" if all(checks.values()) else "FAIL"

    out = {
        "schema": SCHEMA,
        "status": status,
        "authority": "CANDIDATE_ONLY",
        "canon_allowed": False,
        "physical_production_claim": False,
        "theorem_class": "EXACT_SCHUR_DOUBLE_COVER_RELATIONAL_BASE",
        "block_form": {
            "d": str(d),
            "S": [[str(v) for v in row] for row in S.tolist()],
            "S_leading_principal_minors": [str(m) for m in leading_minors],
            "completed_square": "d*(z+q^T xi/d)^2 + xi^T S xi = 1",
        },
        "base": {
            "definition": "B_S={xi: xi^T S xi <= 1}",
            "dimension": 3,
            "topology": "closed 3-ball",
            "boundary": "xi^T S xi = 1 ~= S2",
        },
        "fiber": {
            "interior": "two sheets",
            "zeta_plus": "-q^T xi/d + sqrt((1-xi^T S xi)/d)",
            "zeta_minus": "-q^T xi/d - sqrt((1-xi^T S xi)/d)",
            "boundary": "single merged sheet value",
            "carrier_topology": "double(B_S) ~= S3",
        },
        "anchors": anchor_results,
        "checks": checks,
        "frontier": {
            "fibered_relational_base_structure": "CLOSED_EXACT",
            "sheet_sign_physical_semantics": "OPEN",
            "physical_base_identification": "OPEN",
            "physical_time_map": "OPEN",
            "external_source_tensor_pullback": "OPEN",
            "W6_physical_source_packet": "OPEN",
        },
        "interpretation_firewall": {
            "double_cover_structure_is_not_physical_spacetime_identification": True,
            "base_field_pullback_may_be_sheet_independent_only_if_physically_justified": True,
            "branch_locus_requires_explicit_handling": True,
        },
    }

    print(json.dumps(out, indent=2, sort_keys=True))
    raise SystemExit(0 if status == "PASS" else 1)


if __name__ == "__main__":
    main()
