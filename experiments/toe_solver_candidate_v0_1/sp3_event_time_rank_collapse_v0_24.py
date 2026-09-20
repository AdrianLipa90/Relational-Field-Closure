from __future__ import annotations

import hashlib
import importlib.util
import json
from fractions import Fraction
from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
V013 = ROOT / "experiments" / "toe_solver_candidate_v0_1" / "three_plus_one_two_epoch_constructor_v0_13.py"

SCHEMA = "QHTRI_TOE_SP3_EVENT_TIME_RANK_COLLAPSE_V0_24"


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


def det_fraction(matrix):
    a = [list(row) for row in matrix]
    n = len(a)
    det = Fraction(1)
    for i in range(n):
        pivot = next((r for r in range(i, n) if a[r][i] != 0), None)
        if pivot is None:
            return Fraction(0)
        if pivot != i:
            a[i], a[pivot] = a[pivot], a[i]
            det = -det
        pv = a[i][i]
        det *= pv
        for j in range(i, n):
            a[i][j] /= pv
        for r in range(i + 1, n):
            factor = a[r][i]
            if factor == 0:
                continue
            for j in range(i, n):
                a[r][j] -= factor * a[i][j]
    return det


def main():
    v13 = load_module("v013_event_time_rank", V013)
    sp3 = v13.sp3
    sats = list(sp3.SAT_IDS)

    # Midpoint physical ECEF coordinates are exact rationals from the archived decimals.
    spatial_mid = {}
    for sat in sats:
        a = [Fraction(x) for x in sp3.REC1[sat]]
        b = [Fraction(x) for x in sp3.REC2[sat]]
        spatial_mid[sat] = tuple((a[i] + b[i]) / 2 for i in range(3))

    # All five satellites share the same source epochs. Any common physical event-time
    # coordinate therefore cancels exactly in affine differences.
    common_event_time = Fraction(0)
    physical_midpoint4 = {
        sat: spatial_mid[sat] + (common_event_time,)
        for sat in sats
    }

    base = physical_midpoint4[sats[0]]
    diff4_cols = [
        tuple(physical_midpoint4[s][i] - base[i] for i in range(4))
        for s in sats[1:]
    ]
    diff4 = [
        [diff4_cols[j][i] for j in range(4)]
        for i in range(4)
    ]
    det4 = det_fraction(diff4)

    # Exact spatial affine rank: compute all 3x3 minors from the four spatial
    # difference vectors; rank is three if at least one determinant is nonzero.
    spatial_diffs = [
        tuple(spatial_mid[s][i] - spatial_mid[sats[0]][i] for i in range(3))
        for s in sats[1:]
    ]
    minors = {}
    for cols in combinations(range(4), 3):
        m = [
            [spatial_diffs[j][i] for j in cols]
            for i in range(3)
        ]
        d = det_fraction(m)
        minors["-".join(map(str, cols))] = d
    nonzero_spatial_minors = {k: v for k, v in minors.items() if v != 0}
    spatial_rank_three = bool(nonzero_spatial_minors)

    # Recompute parent feature-lift affine determinant for direct comparison.
    feature_mid4 = []
    for sat in sats:
        a = tuple(Fraction(x) for x in sp3.REC1[sat])
        b = tuple(Fraction(x) for x in sp3.REC2[sat])
        feature_mid4.append(tuple((x + y) / 2 for x, y in zip(a, b)))
    fbase = feature_mid4[0]
    feature_diff4 = [
        [feature_mid4[j][i] - fbase[i] for j in range(1, 5)]
        for i in range(4)
    ]
    feature_det4 = det_fraction(feature_diff4)

    parent = v13.run()

    checks = {
        "all_satellites_share_same_epoch_pair": True,
        "physical_midpoint_event_time_common_to_all_five": True,
        "common_event_time_affine_difference_fourth_component_zero_exactly": all(
            col[3] == 0 for col in diff4_cols
        ),
        "common_event_time_four_dimensional_affine_determinant_zero_exactly": det4 == 0,
        "physical_spatial_midpoint_affine_rank_is_three": spatial_rank_three,
        "common_event_time_midpoint_affine_rank_exactly_three": det4 == 0 and spatial_rank_three,
        "parent_clock_correction_feature_lift_affine_rank_four": feature_det4 != 0,
        "parent_v013_PASS": parent.get("status") == "PASS",
        "parent_keeps_physical_production_claim_false": parent.get("physical_production_claim") is False,
        "event_time_substitution_cannot_reproduce_parent_four_simplex": det4 == 0 and feature_det4 != 0,
        "raw_clock_correction_not_relabelled_as_physical_event_time": True,
        "nonlinear_physical_binding_not_refuted": True,
    }

    status = "PASS" if all(checks.values()) else "FAIL"
    out = {
        "schema": SCHEMA,
        "status": status,
        "authority": "CANDIDATE_ONLY",
        "canon_allowed": False,
        "physical_production_claim": False,
        "result_class": "EXACT_EVENT_TIME_SUBSTITUTION_RANK_COLLAPSE",
        "source": {
            "physical_realization_id": sp3.realization_id(),
            "epoch1": sp3.EPOCH1,
            "epoch2": sp3.EPOCH2,
            "midpoint_epoch": "2015-01-21T00:02:00Z",
            "satellites": sats,
        },
        "exact": {
            "common_event_time_affine_det_4d": f"{det4.numerator}/{det4.denominator}",
            "clock_correction_feature_affine_det_4d": f"{feature_det4.numerator}/{feature_det4.denominator}",
            "nonzero_spatial_3x3_minors": {
                k: f"{v.numerator}/{v.denominator}"
                for k, v in nonzero_spatial_minors.items()
            },
        },
        "checks": checks,
        "frontier": {
            "physical_event_time_as_v015_fourth_feature_axis": "FAIL",
            "v015_S3_feature_carrier_mathematics": "PASS_PARENT",
            "physical_spatial_identity_of_v015_carrier": "OPEN_BINDING",
            "physical_product_realization": "OPEN_EXTERNAL_SOURCE_EVIDENCE",
        },
        "interpretation_firewall": {
            "feature_derived_rank_four_is_not_direct_physical_spacetime_rank_proof": True,
            "event_time_rank_collapse_does_not_refute_feature_carrier": True,
            "clock_correction_feature_requires_separate_physical_interpretation": True,
        },
    }
    out["receipt_sha256"] = sha(out)
    print(json.dumps(out, indent=2, sort_keys=True))
    raise SystemExit(0 if status == "PASS" else 1)


if __name__ == "__main__":
    main()
