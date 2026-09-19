from __future__ import annotations

import hashlib
import importlib.util
import json
from fractions import Fraction
from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CTOR = ROOT / "experiments" / "toe_solver_candidate_v0_1" / "three_plus_one_two_epoch_constructor_v0_13.py"

spec = importlib.util.spec_from_file_location("ctor_v013", CTOR)
if spec is None or spec.loader is None:
    raise RuntimeError("cannot load v0.13 source constructor")
ctor = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ctor)
sp3 = ctor.sp3

SCHEMA = "QHTRI_TOE_SP3_AFFINE_MATCHING_FIELD_V0_14"
C = Fraction(299792458, 1000)
DT = Fraction(120, 1)


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


def solve_exact(A, b):
    aug = [list(row) + [rhs] for row, rhs in zip(A, b)]
    n = len(A)
    for i in range(n):
        pivot = next((r for r in range(i, n) if aug[r][i] != 0), None)
        if pivot is None:
            raise ValueError("singular affine interpolation matrix")
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
            aug[r] = [aug[r][j] - factor * aug[i][j] for j in range(n + 1)]
    return [aug[i][-1] for i in range(n)]


def eval_affine(coeff, y):
    return coeff[0] + sum(coeff[i + 1] * y[i] for i in range(4))


def vec_eq(a, b):
    return all(x == y for x, y in zip(a, b))


def frac_norm_sq(v):
    return sum(x * x for x in v)


def main():
    sats = list(sp3.SAT_IDS)
    points = {}
    betas = {}

    for sat in sats:
        a = [Fraction(x) for x in sp3.REC1[sat]]
        b = [Fraction(x) for x in sp3.REC2[sat]]
        points[sat] = tuple((a[i] + b[i]) / 2 for i in range(4))
        betas[sat] = tuple((b[i] - a[i]) / DT for i in range(3))

    A = [[Fraction(1)] + list(points[s]) for s in sats]
    detA = det_fraction(A)
    coeffs = [
        solve_exact(A, [betas[s][component] for s in sats])
        for component in range(3)
    ]

    recovered = {
        sat: tuple(eval_affine(coeffs[k], points[sat]) for k in range(3))
        for sat in sats
    }
    vertex_recovery_exact = all(vec_eq(recovered[s], betas[s]) for s in sats)

    facets = {
        omitted: tuple(s for s in sats if s != omitted)
        for omitted in sats
    }

    facet_centroid_checks = []
    for omitted, facet in facets.items():
        centroid = tuple(
            sum(points[s][mu] for s in facet) / Fraction(len(facet))
            for mu in range(4)
        )
        global_value = tuple(eval_affine(coeffs[k], centroid) for k in range(3))
        bary_value = tuple(
            sum(betas[s][k] for s in facet) / Fraction(len(facet))
            for k in range(3)
        )
        facet_centroid_checks.append({
            "facet_omits": omitted,
            "pass": vec_eq(global_value, bary_value),
        })

    overlap_checks = []
    for omitted_a, omitted_b in combinations(sats, 2):
        shared = tuple(s for s in sats if s not in {omitted_a, omitted_b})
        centroid = tuple(
            sum(points[s][mu] for s in shared) / Fraction(len(shared))
            for mu in range(4)
        )
        global_value = tuple(eval_affine(coeffs[k], centroid) for k in range(3))
        shared_bary = tuple(
            sum(betas[s][k] for s in shared) / Fraction(len(shared))
            for k in range(3)
        )
        overlap_checks.append({
            "facets_omit": [omitted_a, omitted_b],
            "shared_vertices": list(shared),
            "pass": vec_eq(global_value, shared_bary),
        })

    max_speed_sq = max(frac_norm_sq(betas[s]) for s in sats)
    subluminal_vertices = max_speed_sq < C * C

    # For any convex barycentric combination B(y)=sum lambda_i beta_i,
    # convexity of the norm gives |B(y)| <= max_i |beta_i| < c.
    whole_simplex_subluminal = subluminal_vertices

    mp = sp3.matching_packet()
    packet_beta = {
        p["patch_id"]: tuple(Fraction(str(x)) for x in p["beta_match"])
        for p in mp["patches"]
    }
    packet_vertex_residual = max(
        abs(packet_beta[s][k] - betas[s][k])
        for s in sats
        for k in range(3)
    )

    coeff_serialized = [
        [f"{x.numerator}/{x.denominator}" for x in coeff]
        for coeff in coeffs
    ]

    checks = {
        "five_midpoint_events_affinely_independent": detA != 0,
        "unique_global_affine_interpolant_exists": detA != 0,
        "global_affine_interpolant_recovers_all_source_beta_exactly": vertex_recovery_exact,
        "each_tetrahedral_facet_restriction_matches_barycentric_source_interpolation": all(x["pass"] for x in facet_centroid_checks),
        "all_pairwise_triangular_overlap_restrictions_agree_exactly": all(x["pass"] for x in overlap_checks),
        "existing_v013_matching_packet_vertex_values_recovered": packet_vertex_residual < Fraction(1, 10**12),
        "whole_data_defined_simplex_field_is_subluminal_by_convexity": whole_simplex_subluminal,
        "smooth_physical_tangent_realization_not_claimed": True,
    }

    status = "PASS" if all(checks.values()) else "FAIL"
    out = {
        "schema": SCHEMA,
        "status": status,
        "authority": "CANDIDATE_ONLY",
        "canon_allowed": False,
        "physical_production_claim": False,
        "empirical_theory_confirmation": False,
        "source_evidence_class": "EXTERNAL_OBSERVATIONAL_ARCHIVE_DERIVED_AFFINE_FIELD_CANDIDATE",
        "source": {
            "realization_id": sp3.realization_id(),
            "satellites": sats,
            "dt_s": str(DT),
        },
        "affine_interpolant": {
            "augmented_matrix_determinant_numerator": detA.numerator,
            "augmented_matrix_determinant_denominator": detA.denominator,
            "coefficient_sha256": sha(coeff_serialized),
            "component_coefficients_exact_fraction": coeff_serialized,
            "vertex_recovery_exact": vertex_recovery_exact,
        },
        "boundary": {
            "facet_count": len(facets),
            "pairwise_overlap_count": len(overlap_checks),
            "facet_centroid_checks": facet_centroid_checks,
            "overlap_centroid_checks": overlap_checks,
            "global_overlap_equality_theorem": "restrictions of one ambient affine map are identical on every common face",
        },
        "bounds": {
            "max_vertex_speed_sq_exact": f"{max_speed_sq.numerator}/{max_speed_sq.denominator}",
            "c_sq_exact": f"{(C*C).numerator}/{(C*C).denominator}",
            "whole_simplex_subluminal": whole_simplex_subluminal,
        },
        "existing_packet": {
            "max_vertex_beta_residual": float(packet_vertex_residual),
        },
        "checks": checks,
        "remaining_gate": "PL_AFFINE_BOUNDARY_FIELD_TO_UNIQUE_SOURCE_OWNED_SMOOTH_PHYSICAL_TANGENT_FIELD",
        "interpretation_firewall": {
            "ambient_affine_interpolant_is_not_yet_global_physical_spatial_field": True,
            "simplicial_boundary_smoothing_selection_remains_open": True,
            "production_source_admission_remains_false": True,
        },
    }
    out["receipt_sha256"] = sha(out)
    print(json.dumps(out, indent=2, sort_keys=True))
    raise SystemExit(0 if status == "PASS" else 1)


if __name__ == "__main__":
    main()
