from __future__ import annotations

import importlib.util
import json
from fractions import Fraction
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
V017 = ROOT / "experiments" / "toe_solver_candidate_v0_1" / "sp3_source_lapse_lorentz_coframe_v0_17.py"
R015 = ROOT / "validation" / "toe_solver_candidate_v0_1" / "SP3_CANONICAL_CIRCUMELLIPSOID_V0_15.json"
R022_DOC = ROOT / "experiments" / "toe_solver_candidate_v0_1" / "RF_GSC5E_CURRENT_SP3_ARCHIVE_W6_SUFFICIENCY_NOGO_V0_22.md"

SCHEMA = "QHTRI_TOE_SP3_PHYSICAL_EMBEDDING_GATE_VALIDATION_V0_23"


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


def main():
    v17 = load_module("v017_embed_v023", V017)
    sats, points, betas, centroid, Q_exact, beta_coeffs, lapse_coeff, source_logs = v17.build_geometry()

    Q = q_to_sympy(Q_exact)
    g = sp.Matrix([sp.Rational(x.numerator, x.denominator) for x in centroid])
    q44 = sp.simplify(Q[3,3])

    e4 = sp.Matrix([0,0,0,1])
    delta = sp.sqrt(1/q44)
    y_plus = sp.simplify(g + delta*e4)
    y_minus = sp.simplify(g - delta*e4)

    def ellipsoid_value(y):
        d = sp.simplify(y-g)
        return sp.simplify((d.T*Q*d)[0])

    plus_on = sp.simplify(ellipsoid_value(y_plus)-1) == 0
    minus_on = sp.simplify(ellipsoid_value(y_minus)-1) == 0
    distinct = sp.simplify(y_plus[3]-y_minus[3]) != 0
    same_projection = all(sp.simplify(y_plus[i]-y_minus[i]) == 0 for i in range(3))

    # Direct first-three projection is non-injective by explicit witness.
    projection_noninjective = bool(plus_on and minus_on and distinct and same_projection)

    # Anchor projection is well-defined but does not determine a global embedding.
    anchor_spatial = {
        sat: [str(points[sat][i]) for i in range(3)]
        for sat in sats
    }
    anchor_count = len(anchor_spatial)

    # Parent v0.15 explicitly protects the raw-clock / physical-time distinction.
    r15 = json.loads(R015.read_text(encoding="utf-8"))
    clock_firewall = bool(
        r15.get("interpretation_firewall", {}).get(
            "clock_unit_homogenization_is_not_clock_trace_identification"
        )
    )

    # The current-archive no-go document must retain the external-source boundary.
    no_go_text = R022_DOC.read_text(encoding="utf-8")
    source_boundary_present = (
        "additional independent physical-source dataset" in no_go_text
        and "physical source-field lineage" in no_go_text
    )

    checks = {
        "Q44_strictly_positive_from_positive_definite_Q": bool(q44.is_positive),
        "y_plus_lies_on_source_ellipsoid_exactly": plus_on,
        "y_minus_lies_on_source_ellipsoid_exactly": minus_on,
        "y_plus_and_y_minus_are_distinct": bool(distinct),
        "direct_first_three_coordinate_projections_are_identical": same_projection,
        "direct_R3_projection_is_globally_noninjective": projection_noninjective,
        "five_source_anchor_spatial_coordinates_remain_available": anchor_count == 5,
        "raw_clock_feature_is_not_promoted_to_physical_event_time": clock_firewall,
        "current_archive_external_source_boundary_retained": source_boundary_present,
        "physical_embedding_remains_open": True,
        "external_source_field_without_embedding_is_not_W6": True,
        "physical_production_claim_remains_false": True,
    }

    status = "PASS" if all(checks.values()) else "FAIL"
    out = {
        "schema": SCHEMA,
        "status": status,
        "authority": "CANDIDATE_ONLY",
        "canon_allowed": False,
        "physical_production_claim": False,
        "theorem_class": "DIRECT_R3_PROJECTION_NO_GO_AND_PHYSICAL_EMBEDDING_GATE",
        "carrier": {
            "equation": "(y-g)^T Q (y-g)=1",
            "ambient_dimension": 4,
            "intrinsic_dimension": 3,
            "Q44": str(q44),
            "projection": "pi(y1,y2,y3,y4)=(y1,y2,y3)",
        },
        "explicit_noninjectivity_witness": {
            "y_plus": [str(v) for v in y_plus],
            "y_minus": [str(v) for v in y_minus],
            "ellipsoid_value_plus": str(ellipsoid_value(y_plus)),
            "ellipsoid_value_minus": str(ellipsoid_value(y_minus)),
            "common_R3_projection": [str(y_plus[i]) for i in range(3)],
            "fourth_coordinate_separation": str(sp.simplify(y_plus[3]-y_minus[3])),
        },
        "source_anchors": anchor_spatial,
        "checks": checks,
        "frontier": {
            "direct_first3_physical_space_identification": "REFUTED",
            "raw_fourth_coordinate_as_physical_time": "REFUTED_PARENT_FIREWALL",
            "physical_embedding_Psi": "OPEN",
            "external_source_frame_transform": "OPEN",
            "full_domain_tensor_pullback": "OPEN",
            "W6_physical_source_packet": "OPEN",
        },
        "required_next_contract": {
            "map": "Psi: I x E_Q -> Omega_phys",
            "requirements": [
                "physical time map",
                "physical spatial map",
                "source and target frame ids",
                "full-rank local Jacobian on each admitted patch",
                "north/south overlap compatibility",
                "source-anchor agreement",
                "immutable frame-transform provenance",
                "full production-domain coverage",
                "rank-two tensor pullback receipt",
            ],
        },
        "interpretation_firewall": {
            "carrier_embedding_coordinates_are_not_automatically_physical_coordinates": True,
            "external_field_lookup_by_y_first3_is_not_globally_valid": True,
            "fourth_ambient_feature_is_not_event_time": True,
            "anchor_agreement_alone_does_not_determine_global_embedding": True,
        },
    }
    print(json.dumps(out, indent=2, sort_keys=True))
    raise SystemExit(0 if status == "PASS" else 1)


if __name__ == "__main__":
    main()
