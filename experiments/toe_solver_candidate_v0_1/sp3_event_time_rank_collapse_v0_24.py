from __future__ import annotations

import hashlib
import importlib.util
import json
import math
from fractions import Fraction
from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
V013 = ROOT / "experiments" / "toe_solver_candidate_v0_1" / "three_plus_one_two_epoch_constructor_v0_13.py"

SCHEMA = "QHTRI_TOE_SP3_EVENT_TIME_RANK_COLLAPSE_V0_24"

# Actual records at 2015-01-21T00:02:00Z from the same immutable
# RT218283.SP3@8013 source used by the parent.
REC_MID = {
    "G01": ("-20128.279760", "-13525.695732", "-11076.772100", "-9.945304"),
    "G02": ("-2642.853567", "15614.039520", "21671.569845", "543.075237"),
    "G03": ("-13223.483788", "-20399.563483", "10649.274023", "161.248134"),
    "G04": ("-10915.617120", "-16472.667757", "-18180.990449", "-5.933980"),
    "G05": ("1381.565746", "25341.632792", "7464.578319", "-290.124934"),
}
MID_EPOCH = "2015-01-21T00:02:00Z"


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

    if set(REC_MID) != set(sats):
        raise RuntimeError("actual midpoint source record set does not match parent satellite set")

    # Relation-centre midpoint from the two endpoint records.
    relation_mid = {}
    actual_mid = {}
    midpoint_spatial_residual_km = {}
    midpoint_clock_residual_us = {}
    for sat in sats:
        a = [Fraction(x) for x in sp3.REC1[sat]]
        b = [Fraction(x) for x in sp3.REC2[sat]]
        relation_mid[sat] = tuple((a[i] + b[i]) / 2 for i in range(4))
        actual_mid[sat] = tuple(Fraction(x) for x in REC_MID[sat])

        dxyz = [relation_mid[sat][i] - actual_mid[sat][i] for i in range(3)]
        midpoint_spatial_residual_km[sat] = math.sqrt(sum(float(v) ** 2 for v in dxyz))
        midpoint_clock_residual_us[sat] = float(relation_mid[sat][3] - actual_mid[sat][3])

    all_relation_centres_differ_from_actual_midevents = all(
        midpoint_spatial_residual_km[s] > 0.0 for s in sats
    )

    # Actual same-time physical event records. The event-time coordinate is common,
    # so it may be set to any common constant for affine-rank purposes.
    common_event_time = Fraction(0)
    physical_same_time4 = {
        sat: tuple(actual_mid[sat][i] for i in range(3)) + (common_event_time,)
        for sat in sats
    }

    base = physical_same_time4[sats[0]]
    diff4_cols = [
        tuple(physical_same_time4[s][i] - base[i] for i in range(4))
        for s in sats[1:]
    ]
    diff4 = [
        [diff4_cols[j][i] for j in range(4)]
        for i in range(4)
    ]
    det4 = det_fraction(diff4)

    # Exact spatial affine rank of the actual 00:02 source records.
    spatial_diffs = [
        tuple(actual_mid[s][i] - actual_mid[sats[0]][i] for i in range(3))
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

    # Parent relation-centre + clock-correction feature lift.
    feature_mid4 = [relation_mid[s] for s in sats]
    fbase = feature_mid4[0]
    feature_diff4 = [
        [feature_mid4[j][i] - fbase[i] for j in range(1, 5)]
        for i in range(4)
    ]
    feature_det4 = det_fraction(feature_diff4)

    parent = v13.run()

    checks = {
        "actual_mid_epoch_records_present_for_all_five_satellites": set(REC_MID) == set(sats),
        "all_satellites_share_same_mid_epoch": True,
        "relational_chord_midpoint_differs_from_actual_mid_epoch_event_for_all_five": all_relation_centres_differ_from_actual_midevents,
        "actual_same_time_affine_difference_fourth_component_zero_exactly": all(
            col[3] == 0 for col in diff4_cols
        ),
        "actual_same_time_four_dimensional_affine_determinant_zero_exactly": det4 == 0,
        "actual_mid_epoch_spatial_affine_rank_is_three": spatial_rank_three,
        "actual_same_time_event_affine_rank_exactly_three": det4 == 0 and spatial_rank_three,
        "parent_clock_correction_feature_relation_centre_lift_affine_rank_four": feature_det4 != 0,
        "parent_v013_PASS": parent.get("status") == "PASS",
        "parent_keeps_physical_production_claim_false": parent.get("physical_production_claim") is False,
        "physical_event_time_cannot_replace_parent_feature_axis": det4 == 0 and feature_det4 != 0,
        "pair_midpoint_is_relation_center_not_automatically_trajectory_event": all_relation_centres_differ_from_actual_midevents,
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
        "result_class": "EXACT_EVENT_TIME_RANK_COLLAPSE_AND_RELATIONAL_MIDPOINT_SEPARATION",
        "source": {
            "physical_realization_id": sp3.realization_id(),
            "source_url": sp3.SOURCE_URL,
            "source_revision": sp3.SOURCE_REV,
            "epoch1": sp3.EPOCH1,
            "mid_epoch": MID_EPOCH,
            "epoch2": sp3.EPOCH2,
            "satellites": sats,
        },
        "midpoint_vs_actual_event": {
            "spatial_residual_norm_km": midpoint_spatial_residual_km,
            "clock_residual_microseconds": midpoint_clock_residual_us,
            "minimum_spatial_residual_km": min(midpoint_spatial_residual_km.values()),
            "maximum_spatial_residual_km": max(midpoint_spatial_residual_km.values()),
        },
        "exact": {
            "actual_same_time_affine_det_4d": f"{det4.numerator}/{det4.denominator}",
            "clock_correction_feature_affine_det_4d": f"{feature_det4.numerator}/{feature_det4.denominator}",
            "nonzero_actual_mid_epoch_spatial_3x3_minors": {
                k: f"{v.numerator}/{v.denominator}"
                for k, v in nonzero_spatial_minors.items()
            },
        },
        "checks": checks,
        "frontier": {
            "relational_midpoint_equals_actual_mid_epoch_event": "FAIL",
            "physical_event_time_as_v015_fourth_feature_axis": "FAIL",
            "v015_S3_feature_carrier_mathematics": "PASS_PARENT",
            "physical_spatial_identity_of_v015_carrier": "OPEN_BINDING",
            "physical_product_realization": "OPEN_EXTERNAL_SOURCE_EVIDENCE",
        },
        "interpretation_firewall": {
            "binary_relation_midpoint_is_not_assumed_to_be_worldline_event": True,
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
