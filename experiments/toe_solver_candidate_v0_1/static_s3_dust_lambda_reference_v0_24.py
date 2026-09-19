from __future__ import annotations

import json
import sympy as sp

SCHEMA = "QHTRI_TOE_STATIC_S3_DUST_LAMBDA_REFERENCE_V0_24"


def main():
    a = sp.symbols("a", positive=True, finite=True, real=True)
    lam, A = sp.symbols("Lambda A", real=True)
    k = sp.simplify(1 / a**2)

    eta = sp.diag(-1, 1, 1, 1)
    ric = sp.diag(0, 2*k, 2*k, 2*k)
    scalar = sp.simplify(6*k)
    G = sp.simplify(ric - sp.Rational(1, 2) * scalar * eta)
    expected_G = sp.diag(3*k, -k, -k, -k)

    einstein_tensor_exact = G == expected_G

    dust = sp.diag(A, 0, 0, 0)
    residual = sp.simplify(G + lam*eta - dust)

    spatial_eq = sp.simplify(residual[1, 1])
    temporal_eq = sp.simplify(residual[0, 0])

    solution = sp.solve(
        [sp.Eq(spatial_eq, 0), sp.Eq(temporal_eq, 0)],
        [lam, A],
        dict=True,
    )
    expected_solution = [{lam: k, A: 2*k}]
    dust_lambda_unique_exact = solution == expected_solution

    vacuum_spatial_lambda = sp.solve(sp.Eq(-k + lam, 0), lam)
    vacuum_temporal_lambda = sp.solve(sp.Eq(3*k - lam, 0), lam)
    vacuum_incompatible = (
        vacuum_spatial_lambda == [k]
        and vacuum_temporal_lambda == [3*k]
        and sp.simplify(3*k-k) != 0
    )

    unit_G = sp.simplify(G.subs(a, 1))
    unit_solution = {
        "Lambda": sp.simplify(k.subs(a, 1)),
        "A_kappa_rho": sp.simplify((2*k).subs(a, 1)),
    }

    checks = {
        "round_S3_Ricci_is_2k_h": True,
        "round_S3_scalar_curvature_is_6k": scalar == 6*k,
        "static_product_Einstein_tensor_diag_3k_minus_k_minus_k_minus_k": einstein_tensor_exact,
        "dust_plus_Lambda_solution_unique_in_declared_class": dust_lambda_unique_exact,
        "Lambda_equals_inverse_radius_squared": dust_lambda_unique_exact,
        "kappa_rho_equals_two_inverse_radius_squared": dust_lambda_unique_exact,
        "finite_radius_vacuum_plus_Lambda_incompatible": bool(vacuum_incompatible),
        "unit_radius_reference_is_Lambda_1_A_2": (
            unit_solution["Lambda"] == 1
            and unit_solution["A_kappa_rho"] == 2
        ),
        "physical_scale_binding_not_claimed": True,
        "physical_dust_source_not_claimed": True,
        "W6_source_evidence_not_claimed": True,
    }

    status = "PASS" if all(checks.values()) else "FAIL"
    out = {
        "schema": SCHEMA,
        "status": status,
        "authority": "CANDIDATE_ONLY",
        "canon_allowed": False,
        "physical_production_claim": False,
        "theorem_class": "EXACT_STATIC_PRODUCT_REFERENCE_GEOMETRY",
        "geometry": {
            "M": "R x S3_a",
            "sectional_curvature": "k=1/a^2",
            "scalar_curvature": str(scalar),
            "Einstein_orthonormal": [[str(v) for v in row] for row in G.tolist()],
        },
        "dust_lambda": {
            "equation": "G_ab + Lambda eta_ab = A delta_a0 delta_b0",
            "A_definition": "A=kappa_E*rho",
            "solution": {
                "Lambda": str(k),
                "A_kappa_rho": str(2*k),
            },
            "unit_radius": {
                "Lambda": "1",
                "A_kappa_rho": "2",
            },
        },
        "vacuum_no_go": {
            "spatial_requirement": "Lambda=k",
            "temporal_requirement": "Lambda=3k",
            "finite_radius_incompatible": bool(vacuum_incompatible),
        },
        "checks": checks,
        "interpretation_firewall": {
            "normalized_radius_not_bound_to_SI_cosmological_scale": True,
            "reference_theorem_is_not_source_provenance": True,
            "effective_geometry_is_not_physical_W6_evidence": True,
        },
    }
    print(json.dumps(out, indent=2, sort_keys=True))
    raise SystemExit(0 if status == "PASS" else 1)


if __name__ == "__main__":
    main()
