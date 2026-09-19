from __future__ import annotations

import hashlib
import importlib.util
import json
from fractions import Fraction
from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CTOR = ROOT / "experiments" / "toe_solver_candidate_v0_1" / "three_plus_one_two_epoch_constructor_v0_13.py"
AFFINE = ROOT / "experiments" / "toe_solver_candidate_v0_1" / "sp3_affine_matching_field_v0_14.py"

spec = importlib.util.spec_from_file_location("ctor_v013", CTOR)
if spec is None or spec.loader is None:
    raise RuntimeError("cannot load v0.13 source constructor")
ctor = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ctor)
sp3 = ctor.sp3

spec2 = importlib.util.spec_from_file_location("affine_v014", AFFINE)
if spec2 is None or spec2.loader is None:
    raise RuntimeError("cannot load v0.14 affine matching field")
aff = importlib.util.module_from_spec(spec2)
spec2.loader.exec_module(aff)

SCHEMA = "QHTRI_TOE_SP3_CANONICAL_CIRCUMELLIPSOID_V0_15"
C = Fraction(299792458, 1000)
MICROSECOND = Fraction(1, 10**6)
DT = Fraction(120, 1)


def sha(obj):
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    ).hexdigest()


def det_fraction(matrix):
    return aff.det_fraction(matrix)


def inv_exact(A):
    n = len(A)
    aug = [
        list(row) + [Fraction(int(i == j)) for j in range(n)]
        for i, row in enumerate(A)
    ]
    for i in range(n):
        pivot = next((r for r in range(i, n) if aug[r][i] != 0), None)
        if pivot is None:
            raise ValueError("singular matrix")
        if pivot != i:
            aug[i], aug[pivot] = aug[pivot], aug[i]
        pv = aug[i][i]
        aug[i] = [x / pv for x in aug[i]]
        for r in range(n):
            if r == i:
                continue
            factor = aug[r][i]
            if factor == 0:
                continue
            aug[r] = [aug[r][j] - factor * aug[i][j] for j in range(2 * n)]
    return [row[n:] for row in aug]


def matvec(A, v):
    return [sum(A[i][j] * v[j] for j in range(len(v))) for i in range(len(A))]


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def quad(a, Q, b):
    return dot(a, matvec(Q, b))


def leading_principal_minors(A):
    out = []
    for k in range(1, len(A) + 1):
        out.append(det_fraction([row[:k] for row in A[:k]]))
    return out


def main():
    sats = list(sp3.SAT_IDS)

    # Homogeneous length coordinates: spatial km + c * midpoint clock correction.
    points = {}
    betas = {}
    for sat in sats:
        a = [Fraction(x) for x in sp3.REC1[sat]]
        b = [Fraction(x) for x in sp3.REC2[sat]]
        spatial_mid = [(a[i] + b[i]) / 2 for i in range(3)]
        clock_mid_us = (a[3] + b[3]) / 2
        points[sat] = tuple(spatial_mid + [C * MICROSECOND * clock_mid_us])
        betas[sat] = tuple((b[i] - a[i]) / DT for i in range(3))

    centroid = tuple(
        sum(points[s][mu] for s in sats) / Fraction(len(sats))
        for mu in range(4)
    )
    centered = {
        s: tuple(points[s][mu] - centroid[mu] for mu in range(4))
        for s in sats
    }

    S = [
        [
            sum(centered[s][i] * centered[s][j] for s in sats)
            for j in range(4)
        ]
        for i in range(4)
    ]
    detS = det_fraction(S)
    Sinv = inv_exact(S)
    Q = [[Fraction(5, 4) * Sinv[i][j] for j in range(4)] for i in range(4)]

    q_diag = {s: quad(centered[s], Q, centered[s]) for s in sats}
    q_off = {
        f"{a}:{b}": quad(centered[a], Q, centered[b])
        for a, b in combinations(sats, 2)
    }

    principal_S = leading_principal_minors(S)
    principal_Q = leading_principal_minors(Q)

    # Recompute the unique affine beta interpolant in these homogeneous coordinates.
    A = [[Fraction(1)] + list(points[s]) for s in sats]
    detA = det_fraction(A)
    coeffs = [
        aff.solve_exact(A, [betas[s][component] for s in sats])
        for component in range(3)
    ]
    recovered = {
        s: tuple(aff.eval_affine(coeffs[k], points[s]) for k in range(3))
        for s in sats
    }

    checks = {
        "centered_source_spans_R4": detS != 0,
        "S_positive_definite_by_sylvester": all(x > 0 for x in principal_S),
        "Q_positive_definite_by_sylvester": all(x > 0 for x in principal_Q),
        "all_five_source_points_lie_on_Q_unit_ellipsoid_exactly": all(v == 1 for v in q_diag.values()),
        "all_pairwise_Q_inner_products_equal_minus_one_quarter_exactly": all(v == Fraction(-1, 4) for v in q_off.values()),
        "affine_beta_interpolant_exists_in_homogeneous_coordinates": detA != 0,
        "affine_beta_interpolant_recovers_all_source_values_exactly": all(recovered[s] == betas[s] for s in sats),
        "smooth_coefficient_field_on_ellipsoid_follows_from_affine_restriction": True,
        "physical_tangent_soldering_not_claimed": True,
        "raw_clock_correction_not_promoted_to_event_trace_scale": True,
    }

    q_serialized = [
        [f"{x.numerator}/{x.denominator}" for x in row]
        for row in Q
    ]
    coeff_serialized = [
        [f"{x.numerator}/{x.denominator}" for x in row]
        for row in coeffs
    ]

    status = "PASS" if all(checks.values()) else "FAIL"
    out = {
        "schema": SCHEMA,
        "status": status,
        "authority": "CANDIDATE_ONLY",
        "canon_allowed": False,
        "physical_production_claim": False,
        "empirical_theory_confirmation": False,
        "source_evidence_class": "EXTERNAL_OBSERVATIONAL_ARCHIVE_DERIVED_SMOOTH_CARRIER_CANDIDATE",
        "source": {
            "realization_id": sp3.realization_id(),
            "satellites": sats,
            "coordinate_homogenization": "clock_correction_us -> c * delta_clock seconds -> km",
            "clock_homogenization_is_not_event_trace_binding": True,
        },
        "quadratic_form": {
            "definition": "Q = 5/4 * inverse(sum_i z_i z_i^T)",
            "det_S_exact": f"{detS.numerator}/{detS.denominator}",
            "Q_sha256": sha(q_serialized),
            "Q_exact_fraction": q_serialized,
            "source_point_Q_norms": {
                s: f"{v.numerator}/{v.denominator}" for s, v in q_diag.items()
            },
            "pairwise_Q_inner_products": {
                k: f"{v.numerator}/{v.denominator}" for k, v in q_off.items()
            },
            "leading_principal_minors_S": [
                f"{v.numerator}/{v.denominator}" for v in principal_S
            ],
            "leading_principal_minors_Q": [
                f"{v.numerator}/{v.denominator}" for v in principal_Q
            ],
        },
        "smooth_carrier": {
            "equation": "(y-g)^T Q (y-g) = 1",
            "dimension": 3,
            "compact": True,
            "diffeomorphism_class": "S3",
            "contains_all_five_source_points_exactly": True,
            "parameter_free_from_source_simplex": True,
        },
        "matching_field": {
            "affine_coefficient_sha256": sha(coeff_serialized),
            "affine_interpolant_recovers_source_beta_exactly": all(recovered[s] == betas[s] for s in sats),
            "restriction_to_ellipsoid_is_smooth_R3_valued_field": True,
            "tangent_bundle_soldering_status": "OPEN",
        },
        "checks": checks,
        "remaining_gate": "SMOOTH_R3_COEFFICIENT_FIELD_TO_PHYSICAL_TANGENT_VECTOR_FIELD_AND_RF_E25_COFRAME",
        "interpretation_firewall": {
            "ellipsoid_is_source_derived_candidate_not_global_physical_space_claim": True,
            "clock_unit_homogenization_is_not_clock_trace_identification": True,
            "production_source_admission_remains_false": True,
        },
    }
    out["receipt_sha256"] = sha(out)
    print(json.dumps(out, indent=2, sort_keys=True))
    raise SystemExit(0 if status == "PASS" else 1)


if __name__ == "__main__":
    main()
