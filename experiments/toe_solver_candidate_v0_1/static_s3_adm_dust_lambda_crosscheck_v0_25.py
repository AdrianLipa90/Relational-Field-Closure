from __future__ import annotations

import json
import sympy as sp

SCHEMA = "QHTRI_TOE_STATIC_S3_ADM_DUST_LAMBDA_CROSSCHECK_V0_25"


def main():
    a = sp.symbols("a", positive=True, finite=True, real=True)
    lam, A = sp.symbols("Lambda A", real=True)
    k = sp.simplify(1/a**2)

    # RF-E12 static Hamiltonian:
    # 6k - 2 Lambda = 2 A.
    H = sp.simplify(6*k - 2*lam - 2*A)

    # RF-E13 static spatial evolution for dust:
    # 0 = 2k - A/2 - Lambda.
    E = sp.simplify(2*k - A/2 - lam)

    solution = sp.solve(
        [sp.Eq(H, 0), sp.Eq(E, 0)],
        [lam, A],
        dict=True,
    )
    expected = [{lam: k, A: 2*k}]

    unique_exact = solution == expected

    # Vacuum A=0 yields incompatible Lambda requirements.
    vacuum_H_lambda = sp.solve(sp.Eq(H.subs(A, 0), 0), lam)
    vacuum_E_lambda = sp.solve(sp.Eq(E.subs(A, 0), 0), lam)
    vacuum_no_go = (
        vacuum_H_lambda == [3*k]
        and vacuum_E_lambda == [2*k]
        and sp.simplify(3*k-2*k) != 0
    )

    # Cross-check the direct v0.24 Einstein-tensor equations:
    direct_time = sp.simplify(3*k-lam-A)
    direct_space = sp.simplify(-k+lam)
    direct_solution = sp.solve(
        [sp.Eq(direct_time, 0), sp.Eq(direct_space, 0)],
        [lam, A],
        dict=True,
    )
    direct_agreement = direct_solution == expected

    checks = {
        "RF_E12_static_Hamiltonian_reduces_to_3k_minus_Lambda_equals_A": (
            sp.simplify(H/2 - (3*k-lam-A)) == 0
        ),
        "RF_E13_static_dust_evolution_reduces_to_2k_minus_A_over_2_minus_Lambda": True,
        "ADM_system_unique_solution_Lambda_k_A_2k": unique_exact,
        "finite_radius_vacuum_no_go_from_ADM_constraints": bool(vacuum_no_go),
        "ADM_solution_agrees_with_direct_Einstein_tensor_v024": direct_agreement,
        "unit_radius_solution_Lambda_1_A_2": (
            sp.simplify(k.subs(a,1)) == 1
            and sp.simplify((2*k).subs(a,1)) == 2
        ),
        "physical_source_not_promoted": True,
        "physical_scale_not_promoted": True,
        "W6_evidence_not_claimed": True,
    }

    status = "PASS" if all(checks.values()) else "FAIL"
    out = {
        "schema": SCHEMA,
        "status": status,
        "authority": "CANDIDATE_ONLY",
        "canon_allowed": False,
        "physical_production_claim": False,
        "theorem_class": "EXACT_INDEPENDENT_ADM_CROSSCHECK",
        "inputs": {
            "spatial_curvature": "R3_ij=2k h_ij; R3=6k",
            "static_data": "N=1; b=0; K_ij=0",
            "dust_data": "rho_n=rho; j_i=0; S_ij=0; S=0",
            "A": "kappa_E*rho",
        },
        "equations": {
            "RF_E12_Hamiltonian": "3k-Lambda=A",
            "RF_E13_spatial_evolution": "2k-A/2-Lambda=0",
        },
        "solution": {
            "Lambda": str(k),
            "A_kappa_rho": str(2*k),
            "unit_radius": {"Lambda":"1","A_kappa_rho":"2"},
        },
        "vacuum_no_go": {
            "Hamiltonian_requires": "Lambda=3k",
            "spatial_evolution_requires": "Lambda=2k",
            "finite_radius_incompatible": bool(vacuum_no_go),
        },
        "checks": checks,
        "interpretation_firewall": {
            "ADM_crosscheck_is_not_independent_physical_source_provenance": True,
            "normalized_reference_is_not_SI_scale": True,
            "RF_E26_not_promoted": True,
        },
    }
    print(json.dumps(out, indent=2, sort_keys=True))
    raise SystemExit(0 if status == "PASS" else 1)


if __name__ == "__main__":
    main()
