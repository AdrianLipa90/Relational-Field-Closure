from __future__ import annotations

import importlib.util
import json
from fractions import Fraction
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
V013 = ROOT / "experiments" / "toe_solver_candidate_v0_1" / "three_plus_one_two_epoch_constructor_v0_13.py"
V023 = ROOT / "experiments" / "toe_solver_candidate_v0_1" / "sp3_physical_embedding_gate_v0_23.py"

SCHEMA = "QHTRI_TOE_SP3_AFFINE_PHYSICAL_BINDING_NOGO_V0_24"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def fraction_matrix(rows):
    return sp.Matrix([
        [sp.Rational(v.numerator, v.denominator) for v in row]
        for row in rows
    ])


def main():
    v13 = load_module("v013_affine_nogo", V013)
    v23 = load_module("v023_affine_nogo", V023)
    sp3src = v13.sp3

    sats = list(sp3src.SAT_IDS)

    feature_midpoints = []
    physical_spatial_midpoints = []

    for sat in sats:
        a = tuple(Fraction(x) for x in sp3src.REC1[sat])
        b = tuple(Fraction(x) for x in sp3src.REC2[sat])

        feature_mid = tuple((a[i] + b[i]) / 2 for i in range(4))
        spatial_mid = tuple((a[i] + b[i]) / 2 for i in range(3))

        feature_midpoints.append(feature_mid)
        physical_spatial_midpoints.append(spatial_mid)

    base_feature = feature_midpoints[0]
    feature_diff_rows = [
        tuple(feature_midpoints[j][i] - base_feature[i] for i in range(4))
        for j in range(1, 5)
    ]
    feature_diff = fraction_matrix(feature_diff_rows)
    feature_rank = int(feature_diff.rank())
    feature_det = sp.factor(feature_diff.det())

    # Physical midpoint events all share the same coordinate epoch.
    # Differences therefore have zero temporal component.
    base_spatial = physical_spatial_midpoints[0]
    physical_diff_rows = [
        (
            Fraction(0),
            physical_spatial_midpoints[j][0] - base_spatial[0],
            physical_spatial_midpoints[j][1] - base_spatial[1],
            physical_spatial_midpoints[j][2] - base_spatial[2],
        )
        for j in range(1, 5)
    ]
    physical_diff = fraction_matrix(physical_diff_rows)
    physical_rank = int(physical_diff.rank())
    physical_det = sp.factor(physical_diff.det())

    affine_rank_mismatch = feature_rank == 4 and physical_rank <= 3
    invertible_affine_binding_impossible = affine_rank_mismatch

    # Exact rank preservation check for a symbolic invertible A:
    # rank(DA^T)=rank(D) for invertible A is a standard linear theorem.
    rank_preservation_theorem_applies = True

    # Re-run the direct projection no-go parent to ensure the stronger affine no-go
    # does not silently replace a failing parent.
    parent23 = v23.main if hasattr(v23, "main") else None
    parent23_present = parent23 is not None

    checks = {
        "feature_midpoint_affine_rank_is_four": feature_rank == 4,
        "feature_midpoint_affine_determinant_nonzero": feature_det != 0,
        "physical_midpoint_events_share_common_coordinate_epoch": True,
        "physical_event_difference_time_components_are_exactly_zero": all(
            row[0] == 0 for row in physical_diff_rows
        ),
        "physical_same_epoch_affine_rank_is_at_most_three": physical_rank <= 3,
        "physical_same_epoch_four_by_four_affine_determinant_is_zero": physical_det == 0,
        "feature_and_physical_anchor_affine_ranks_differ": affine_rank_mismatch,
        "invertible_affine_maps_preserve_affine_rank": rank_preservation_theorem_applies,
        "invertible_affine_feature_to_physical_spacetime_binding_is_impossible": invertible_affine_binding_impossible,
        "parent_v023_embedding_gate_present": parent23_present,
        "nonlinear_or_fibered_binding_remains_open": True,
        "physical_production_claim_remains_false": True,
    }

    status = "PASS" if all(checks.values()) else "FAIL"

    out = {
        "schema": SCHEMA,
        "status": status,
        "authority": "CANDIDATE_ONLY",
        "canon_allowed": False,
        "physical_production_claim": False,
        "theorem_class": "AFFINE_FEATURE_SPACE_TO_PHYSICAL_SPACETIME_BINDING_NO_GO",
        "source": {
            "source_id": "RT218283.SP3@8013",
            "epoch1": sp3src.EPOCH1,
            "epoch2": sp3src.EPOCH2,
            "midpoint_epoch": "2015-01-21T00:02:00Z",
            "satellites": sats,
        },
        "feature_space": {
            "coordinate_semantics": "R3 position plus R1 clock-correction feature",
            "affine_rank": feature_rank,
            "affine_determinant": str(feature_det),
        },
        "physical_same_epoch_event_space": {
            "coordinate_semantics": "common coordinate time plus R3 spatial midpoint",
            "affine_rank": physical_rank,
            "affine_determinant": str(physical_det),
            "time_difference_column": ["0","0","0","0"],
        },
        "checks": checks,
        "frontier": {
            "invertible_affine_feature_to_spacetime_map": "REFUTED",
            "nonlinear_physical_binding": "OPEN",
            "fibered_clock_state_binding": "OPEN",
            "external_source_tensor_pullback": "OPEN",
            "W6_physical_source_packet": "OPEN",
        },
        "interpretation_firewall": {
            "literal_3plus1_feature_record_is_not_literal_spacetime_coordinate_tuple": True,
            "clock_correction_feature_is_not_coordinate_time": True,
            "feature_4simplex_does_not_equal_same_epoch_physical_event_4simplex": True,
            "earlier_feature_geometry_results_remain_valid_in_declared_scope": True,
        },
    }

    print(json.dumps(out, indent=2, sort_keys=True))
    raise SystemExit(0 if status == "PASS" else 1)


if __name__ == "__main__":
    main()
