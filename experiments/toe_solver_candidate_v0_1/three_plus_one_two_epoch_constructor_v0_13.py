from __future__ import annotations

import importlib.util
import json
from decimal import Decimal, localcontext
from fractions import Fraction
from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PARENT = ROOT / "experiments" / "toe_solver_candidate_v0_1" / "igs_sp3_observational_e2e_v0_11.py"

spec = importlib.util.spec_from_file_location("igs_sp3_v011", PARENT)
if spec is None or spec.loader is None:
    raise RuntimeError("cannot load archived SP3 E2E parent")
sp3 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sp3)

SCHEMA = "QHTRI_TOE_3PLUS1_TWO_EPOCH_CONSTRUCTOR_V0_13"


def dec4(record):
    return tuple(Decimal(x) for x in record)


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

def midpoint_and_rate(a, b, dt):
    with localcontext() as ctx:
        ctx.prec = 80
        mid = tuple((x + y) / Decimal(2) for x, y in zip(a, b))
        rate = tuple((y - x) / dt for x, y in zip(a, b))
    return mid, rate


def reconstruct(mid, rate, dt):
    with localcontext() as ctx:
        ctx.prec = 80
        half = dt / Decimal(2)
        a = tuple(m - half * r for m, r in zip(mid, rate))
        b = tuple(m + half * r for m, r in zip(mid, rate))
    return a, b


def run():
    dt = Decimal(str(sp3.DT))
    cp = sp3.clock_packet()
    spp = sp3.spatial_packet()
    mp = sp3.matching_packet()
    _, fit = sp3.fit_fields()

    per_sat = {}
    exact_reconstruction = True
    max_matching_rate_error = 0.0
    max_midpoint_center_error = 0.0
    clock_rate_exact = True

    mids = []
    for sat in sp3.SAT_IDS:
        y1 = dec4(sp3.REC1[sat])
        y2 = dec4(sp3.REC2[sat])
        mid, rate = midpoint_and_rate(y1, y2, dt)
        r1, r2 = reconstruct(mid, rate, dt)
        exact_reconstruction = exact_reconstruction and (r1 == y1 and r2 == y2)
        mids.append(mid[:3])

        beta = next(p["beta_match"] for p in mp["patches"] if p["patch_id"] == sat)
        for i in range(3):
            max_matching_rate_error = max(
                max_matching_rate_error,
                abs(float(rate[i]) - float(beta[i])),
            )

        expected_clock_rate = rate[3] * Decimal("1e-6")
        actual_clock_rate = Decimal(cp["clock_rate_offsets"][sat])
        clock_rate_exact = clock_rate_exact and (expected_clock_rate == actual_clock_rate)

        per_sat[sat] = {
            "midpoint_3plus1": [str(x) for x in mid],
            "tangent_3plus1_per_s": [str(x) for x in rate],
            "reconstruction_exact": r1 == y1 and r2 == y2,
        }

    center = [
        sum(mid[i] for mid in mids) / Decimal(len(mids))
        for i in range(3)
    ]
    for i in range(3):
        max_midpoint_center_error = max(
            max_midpoint_center_error,
            abs(float(center[i]) - float(fit["center_km"][i])),
        )

    common_id = (
        cp["physical_realization_id"]
        == spp["capture"]["physical_realization_id"]
        == mp["physical_realization_id"]
        == sp3.realization_id()
    )

    midpoint4 = []
    for sat in sp3.SAT_IDS:
        a = tuple(Fraction(x) for x in sp3.REC1[sat])
        b = tuple(Fraction(x) for x in sp3.REC2[sat])
        midpoint4.append(tuple((x + y) / 2 for x, y in zip(a, b)))
    base = midpoint4[0]
    diff = [
        [midpoint4[j][i] - base[i] for j in range(1, 5)]
        for i in range(4)
    ]
    affine_det = det_fraction(diff)
    expected_facets = sorted(
        tuple(sorted(face))
        for face in combinations(sp3.SAT_IDS, 4)
    )
    actual_facets = sorted(
        tuple(sorted(cell["vertices"]))
        for cell in spp["capture"]["tetrahedral_cells"]
    )
    source_defined_boundary = affine_det != 0 and actual_facets == expected_facets

    source_hash_reproducible = (
        sp3.realization_id()
        == "physical:igs-sp3:sha256:" + sp3.sha(sp3.source_records())
    )

    with localcontext() as ctx:
        ctx.prec = 80
        scalar_det = Decimal(1) / dt
        four_component_det = scalar_det ** 4

    checks = {
        "source_record_is_literal_3plus1": all(
            len(sp3.REC1[s]) == 4 and len(sp3.REC2[s]) == 4
            for s in sp3.SAT_IDS
        ),
        "two_epoch_transform_nonzero_determinant": four_component_det != 0,
        "two_epoch_reconstruction_exact_decimal": exact_reconstruction,
        "existing_matching_packet_equals_spatial_tangent": max_matching_rate_error < 1e-12,
        "existing_clock_packet_equals_clock_tangent_after_sp3_unit_scale": clock_rate_exact,
        "existing_field_fit_uses_two_epoch_spatial_midpoint": max_midpoint_center_error < 1e-12,
        "clock_spatial_matching_share_one_parent_realization_id": common_id,
        "realization_id_is_reproducible_source_hash": source_hash_reproducible,
        "five_midpoint_3plus1_events_are_affinely_independent": affine_det != 0,
        "spatial_packet_is_exact_boundary_of_data_defined_4simplex": source_defined_boundary,
        "parent_sp3_e2e_pass": sp3.run()["status"] == "PASS",
    }

    status = "PASS" if all(checks.values()) else "FAIL"
    out = {
        "schema": SCHEMA,
        "status": status,
        "authority": "CANDIDATE_ONLY",
        "canon_allowed": False,
        "physical_production_claim": False,
        "empirical_theory_confirmation": False,
        "source_evidence_class": "EXTERNAL_OBSERVATIONAL_ARCHIVE_DERIVED_MODEL_LEVEL",
        "source": {
            "url": sp3.SOURCE_URL,
            "revision": sp3.SOURCE_REV,
            "epoch1": sp3.EPOCH1,
            "epoch2": sp3.EPOCH2,
            "dt_s": str(dt),
            "satellites": list(sp3.SAT_IDS),
            "realization_id": sp3.realization_id(),
        },
        "linear_transform": {
            "input_per_epoch": "R3_position_plus_R1_clock",
            "association_midpoint": "(y1+y2)/2",
            "dissociation_tangent": "(y2-y1)/dt",
            "inverse": "y1=mid-dt*tangent/2; y2=mid+dt*tangent/2",
            "scalar_block_determinant": str(scalar_det),
            "four_component_determinant": str(four_component_det),
            "lossless_for_dt_nonzero": True,
        },
        "affine_4simplex": {
            "midpoint_event_count": len(midpoint4),
            "affine_determinant_numerator": affine_det.numerator,
            "affine_determinant_denominator": affine_det.denominator,
            "affine_rank_four": affine_det != 0,
            "boundary_facets_match_spatial_packet": actual_facets == expected_facets,
            "incidence_derivation": "all four-vertex facets of the unique nondegenerate affine 4-simplex defined by the five midpoint 3+1 events",
        },
        "residuals": {
            "max_matching_rate_error": max_matching_rate_error,
            "max_midpoint_center_error": max_midpoint_center_error,
        },
        "checks": checks,
        "per_satellite": per_sat,
        "interpretation_firewall": {
            "mnemonic_is_not_physical_evidence": True,
            "two_epoch_transform_is_not_collatz_dynamics": True,
            "sp3_tuple_is_not_yet_identified_with_tir_herm2_event_carrier": True,
            "data_defined_affine_simplex_boundary_does_not_by_itself_equal_global_physical_space": True,
            "prior_model_level_evidence_typing_not_silently_overwritten": True,
            "full_physical_3plus1_production_gate_remains_open": True,
        },
    }
    out["receipt_sha256"] = sp3.sha(out)
    return out


if __name__ == "__main__":
    result = run()
    print(json.dumps(result, indent=2, sort_keys=True))
    raise SystemExit(0 if result["status"] == "PASS" else 1)
