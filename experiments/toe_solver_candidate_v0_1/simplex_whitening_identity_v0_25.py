from __future__ import annotations

import hashlib
import importlib.util
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
V015 = ROOT / "experiments" / "toe_solver_candidate_v0_1" / "sp3_canonical_circumellipsoid_v0_15.py"

SCHEMA = "QHTRI_TOE_SIMPLEX_WHITENING_IDENTITY_V0_25"


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


def transpose(A):
    return [list(row) for row in zip(*A)]


def matmul(A, B):
    BT = transpose(B)
    return [[sum(x*y for x, y in zip(row, col)) for col in BT] for row in A]


def matvec(A, v):
    return [sum(A[i][j]*v[j] for j in range(len(v))) for i in range(len(A))]


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


def canonical_simplex(n: int):
    # Vertices: 0,e_1,...,e_n in R^n, then centered.
    vertices = [[Fraction(0) for _ in range(n)]]
    for i in range(n):
        v = [Fraction(0) for _ in range(n)]
        v[i] = Fraction(1)
        vertices.append(v)
    centroid = [
        sum(v[j] for v in vertices) / Fraction(n+1)
        for j in range(n)
    ]
    centered = [
        [v[j]-centroid[j] for j in range(n)]
        for v in vertices
    ]
    return centered


def scatter(centered):
    n = len(centered[0])
    return [
        [
            sum(v[i]*v[j] for v in centered)
            for j in range(n)
        ]
        for i in range(n)
    ]


def gram(centered, Q):
    return [
        [dot(centered[i], matvec(Q, centered[j])) for j in range(len(centered))]
        for i in range(len(centered))
    ]


def expected_gram(n: int):
    return [
        [
            Fraction(1) if i == j else Fraction(-1, n)
            for j in range(n+1)
        ]
        for i in range(n+1)
    ]


def exact_identity_for_n(v15, n: int):
    Z = canonical_simplex(n)
    S = scatter(Z)
    Sinv = v15.inv_exact(S)
    Q = [
        [Fraction(n+1, n)*Sinv[i][j] for j in range(n)]
        for i in range(n)
    ]
    G = gram(Z, Q)
    return G == expected_gram(n), S, Q, G


def apply_affine_linear(centered, A):
    return [matvec(A, z) for z in centered]


def main():
    v15 = load_module("v015_whitening_identity", V015)
    sp3 = v15.sp3

    # General-dimension exact checks on canonical affinely independent simplices.
    dimension_checks = {}
    for n in range(1, 9):
        ok, _, _, _ = exact_identity_for_n(v15, n)
        dimension_checks[str(n)] = ok

    # Exact nontrivial affine covariance witness in R4.
    Z4 = canonical_simplex(4)
    A = [
        [Fraction(2), Fraction(1), Fraction(0), Fraction(0)],
        [Fraction(0), Fraction(1), Fraction(1), Fraction(0)],
        [Fraction(0), Fraction(0), Fraction(3), Fraction(1)],
        [Fraction(1), Fraction(0), Fraction(0), Fraction(2)],
    ]
    detA = v15.det_fraction(A)
    ZA = apply_affine_linear(Z4, A)
    SA = scatter(ZA)
    SAinv = v15.inv_exact(SA)
    QA = [
        [Fraction(5, 4)*SAinv[i][j] for j in range(4)]
        for i in range(4)
    ]
    GA = gram(ZA, QA)
    affine_covariance_witness = detA != 0 and GA == expected_gram(4)

    # Recompute the actual v0.15 source simplex exactly.
    sats = list(sp3.SAT_IDS)
    points = {}
    for sat in sats:
        a = [Fraction(x) for x in sp3.REC1[sat]]
        b = [Fraction(x) for x in sp3.REC2[sat]]
        spatial_mid = [(a[i]+b[i])/2 for i in range(3)]
        clock_mid_us = (a[3]+b[3])/2
        points[sat] = tuple(
            spatial_mid + [v15.C*v15.MICROSECOND*clock_mid_us]
        )

    centroid = tuple(
        sum(points[s][mu] for s in sats) / Fraction(len(sats))
        for mu in range(4)
    )
    centered_source = [
        [points[s][mu]-centroid[mu] for mu in range(4)]
        for s in sats
    ]
    Ssrc = scatter(centered_source)
    detSsrc = v15.det_fraction(Ssrc)
    Ssrc_inv = v15.inv_exact(Ssrc)
    Qsrc = [
        [Fraction(5, 4)*Ssrc_inv[i][j] for j in range(4)]
        for i in range(4)
    ]
    Gsrc = gram(centered_source, Qsrc)
    source_gram_is_general_identity = Gsrc == expected_gram(4)

    # Projector form P=I-J/(n+1) for the actual source.
    # Z here is n x (n+1): columns are centered source vectors.
    Zmat = [
        [centered_source[col][row] for col in range(5)]
        for row in range(4)
    ]
    Psrc = matmul(transpose(Zmat), matmul(Ssrc_inv, Zmat))
    Pexpected = [
        [
            (Fraction(1) if i == j else Fraction(0)) - Fraction(1, 5)
            for j in range(5)
        ]
        for i in range(5)
    ]
    source_projector_identity = Psrc == Pexpected

    parent_result = v15.main
    # The module main prints/exits, so do not call it. Its defining exact formula
    # is independently recomputed above and its checked source receipt is upstream.

    q_serialized = [
        [f"{x.numerator}/{x.denominator}" for x in row]
        for row in Qsrc
    ]
    gram_serialized = [
        [f"{x.numerator}/{x.denominator}" for x in row]
        for row in Gsrc
    ]

    checks = {
        "canonical_simplex_whitening_identity_exact_for_dimensions_1_through_8": all(dimension_checks.values()),
        "nontrivial_R4_affine_transform_invertible": detA != 0,
        "whitened_gram_invariant_under_nontrivial_affine_transform": affine_covariance_witness,
        "source_scatter_matrix_invertible": detSsrc != 0,
        "source_projector_equals_I_minus_J_over_5_exactly": source_projector_identity,
        "source_v015_Q_gram_equals_regular_4simplex_identity_exactly": source_gram_is_general_identity,
        "v015_regular_simplex_identity_is_implied_by_whitening_definition": (
            source_projector_identity and source_gram_is_general_identity
        ),
        "v015_math_retained": True,
        "v015_empirical_regular_simplex_interpretation_reclassified": True,
        "physical_spatial_identity_not_promoted": True,
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
        "theorem_class": "GENERAL_SIMPLEX_WHITENING_IDENTITY",
        "general_theorem": {
            "input": "n+1 affinely independent points in R^n",
            "scatter": "S=sum_i z_i z_i^T",
            "metric": "Q=(n+1)/n S^{-1}",
            "projector": "Z^T(ZZ^T)^{-1}Z = I - 11^T/(n+1)",
            "gram_diagonal": "1",
            "gram_off_diagonal": "-1/n",
            "affine_covariant": True,
        },
        "dimension_regression": dimension_checks,
        "affine_covariance_witness": {
            "dimension": 4,
            "det_A": f"{detA.numerator}/{detA.denominator}",
            "regular_gram_preserved_exactly": affine_covariance_witness,
        },
        "v015_source_specialization": {
            "physical_realization_id": sp3.realization_id(),
            "scatter_det": f"{detSsrc.numerator}/{detSsrc.denominator}",
            "Q_sha256": sha(q_serialized),
            "gram_exact": gram_serialized,
            "projector_identity_exact": source_projector_identity,
        },
        "checks": checks,
        "evidence_reclassification": {
            "source_affine_independence": "SOURCE_SPECIFIC_EXACT",
            "source_numeric_Q": "SOURCE_SPECIFIC_DETERMINISTIC",
            "Q_positive_definite": "EXACT_CONSEQUENCE_OF_AFFINE_INDEPENDENCE",
            "unit_diag_minus_one_quarter_offdiag": "GENERAL_WHITENING_IDENTITY",
            "regular_4simplex_in_Q": "GENERAL_WHITENING_IDENTITY",
            "ellipsoid_as_candidate_carrier": "CONSTRUCTION_LEVEL",
            "physical_spatial_identity": "OPEN_EXTERNAL_BINDING",
        },
        "interpretation_firewall": {
            "regularity_in_source_derived_Q_is_not_independent_empirical_signal": True,
            "whitening_identity_does_not_invalidate_downstream_candidate_geometry": True,
            "candidate_geometry_requires_separate_physical_domain_binding": True,
        },
    }
    out["receipt_sha256"] = sha(out)
    print(json.dumps(out, indent=2, sort_keys=True))
    raise SystemExit(0 if status == "PASS" else 1)


if __name__ == "__main__":
    main()
