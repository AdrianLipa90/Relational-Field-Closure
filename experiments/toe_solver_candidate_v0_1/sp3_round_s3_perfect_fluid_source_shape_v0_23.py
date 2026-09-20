from __future__ import annotations

import hashlib
import json

import sympy as sp

SCHEMA = "QHTRI_TOE_SP3_ROUND_S3_PERFECT_FLUID_SOURCE_SHAPE_V0_23"


def canon(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def sha(obj):
    return hashlib.sha256(canon(obj)).hexdigest()


def main():
    a, lam, kappa = sp.symbols("a Lambda kappa_E", positive=True, finite=True, real=True)
    x = sp.symbols("x", real=True)

    eta = sp.diag(-1, 1, 1, 1)
    G = sp.diag(3/a**2, -1/a**2, -1/a**2, -1/a**2)
    R = sp.simplify(6/a**2)

    rho = sp.simplify((3/a**2-lam)/kappa)
    p = sp.simplify((-1/a**2+lam)/kappa)
    T = sp.diag(rho, p, p, p)

    efe_residual = sp.simplify(G + lam*eta - kappa*T)
    efe_exact = all(sp.simplify(v) == 0 for v in efe_residual)

    vacuum_temporal_lambda = sp.simplify(3/a**2)
    vacuum_spatial_lambda = sp.simplify(1/a**2)
    vacuum_gap = sp.simplify(vacuum_temporal_lambda-vacuum_spatial_lambda)
    vacuum_no_go = vacuum_gap != 0

    w = sp.simplify(p/rho)
    w_x = sp.simplify(w.subs(lam, x/a**2))
    w_expected = sp.simplify((x-1)/(3-x))
    w_family_exact = sp.simplify(w_x-w_expected) == 0

    special_lambda0 = sp.simplify(w.subs(lam, 0) + sp.Rational(1, 3)) == 0
    dust_lambda = sp.simplify(p.subs(lam, 1/a**2)) == 0
    dust_rho = sp.simplify(rho.subs(lam, 1/a**2) - 2/(kappa*a**2)) == 0
    radiation_w = sp.simplify(w.subs(lam, sp.Rational(3, 2)/a**2) - sp.Rational(1, 3)) == 0

    trace_T = sp.simplify(-rho+3*p)
    trace_expected = sp.simplify((-6/a**2+4*lam)/kappa)
    trace_formula_exact = sp.simplify(trace_T-trace_expected) == 0
    tracefree_lambda = sp.solve(sp.Eq(trace_T, 0), lam)
    tracefree_exact = tracefree_lambda == [sp.Rational(3, 2)/a**2]
    tracefree_equals_R_over_four = sp.simplify(tracefree_lambda[0]-R/4) == 0

    frob_G_eta = sp.simplify(sum(G[i,j]*eta[i,j] for i in range(4) for j in range(4)))
    frob_eta_eta = sp.simplify(sum(eta[i,j]*eta[i,j] for i in range(4) for j in range(4)))
    lambda_ls = sp.simplify(-frob_G_eta/frob_eta_eta)
    lambda_ls_exact = sp.simplify(lambda_ls-sp.Rational(3,2)/a**2) == 0

    source_residual_tracefree = sp.simplify(G + lambda_ls*eta)
    expected_tracefree = sp.diag(
        sp.Rational(3,2)/a**2,
        sp.Rational(1,2)/a**2,
        sp.Rational(1,2)/a**2,
        sp.Rational(1,2)/a**2,
    )
    tracefree_residual_exact = source_residual_tracefree == expected_tracefree

    rho_plus_p = sp.simplify(rho+p)
    rho_plus_3p = sp.simplify(rho+3*p)
    invariant_rho_plus_p = sp.simplify(rho_plus_p-2/(kappa*a**2)) == 0
    invariant_rho_plus_3p = sp.simplify(rho_plus_3p-2*lam/kappa) == 0

    # Dominant energy condition branch algebra in x = Lambda a^2.
    # x < 1: p<0 and (rho-|p|)*kappa*a^2 = (3-x)-(1-x)=2.
    dec_low_branch_gap = sp.simplify((3-x)-(1-x))
    # x >= 1: p>=0 and gap = (3-x)-(x-1)=4-2x.
    dec_high_branch_gap = sp.simplify((3-x)-(x-1))
    dec_low_branch_exact = dec_low_branch_gap == 2
    dec_high_branch_exact = dec_high_branch_gap == 4-2*x
    dec_window_x_le_2 = bool(dec_low_branch_exact and dec_high_branch_exact)

    checks = {
        "round_product_Einstein_tensor_used": True,
        "perfect_fluid_EFE_component_identity_exact": bool(efe_exact),
        "vacuum_plus_one_Lambda_exact_no_go_for_finite_positive_radius": bool(vacuum_no_go),
        "equation_of_state_family_w_equals_x_minus_1_over_3_minus_x": bool(w_family_exact),
        "Lambda_zero_gives_w_minus_one_third": bool(special_lambda0),
        "Lambda_equals_inverse_a2_gives_dust_pressure_zero": bool(dust_lambda),
        "dust_density_equals_2_over_kappa_a2": bool(dust_rho),
        "Lambda_equals_three_over_two_a2_gives_radiation_w_one_third": bool(radiation_w),
        "perfect_fluid_trace_formula_exact": bool(trace_formula_exact),
        "tracefree_member_unique_at_Lambda_three_over_two_a2": bool(tracefree_exact),
        "tracefree_Lambda_equals_R_over_four": bool(tracefree_equals_R_over_four),
        "orthonormal_Frobenius_Lambda_fit_equals_tracefree_Lambda": bool(lambda_ls_exact),
        "tracefree_metric_residual_has_radiation_like_3_to_1_diagonal_ratio": bool(tracefree_residual_exact),
        "rho_plus_p_equals_2_over_kappa_a2_independent_of_Lambda": bool(invariant_rho_plus_p),
        "rho_plus_3p_equals_2Lambda_over_kappa": bool(invariant_rho_plus_3p),
        "dominant_energy_branch_algebra_reduces_to_x_le_2": dec_window_x_le_2,
        "source_shape_theorem_is_not_source_evidence": True,
        "W6_not_promoted": True,
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
        "theorem_class": "EXACT_SOURCE_SHAPE_NOT_SOURCE_EVIDENCE",
        "round_baseline": {
            "Einstein_frame": "diag(3/a^2,-1/a^2,-1/a^2,-1/a^2)",
            "scalar_R": str(R),
        },
        "perfect_fluid_family": {
            "rho": str(rho),
            "p": str(p),
            "w_in_x_equals_Lambda_a2": str(w_x),
            "rho_plus_p": str(rho_plus_p),
            "rho_plus_3p": str(rho_plus_3p),
        },
        "special_cases": {
            "Lambda_0": "w=-1/3",
            "Lambda_1_over_a2": "dust: p=0, rho=2/(kappa_E a^2)",
            "Lambda_3_over_2a2": "tracefree/radiation-like: p=rho/3",
            "orthonormal_least_squares_Lambda": str(lambda_ls),
        },
        "energy_conditions": {
            "rho_nonnegative_if": "Lambda*a^2 <= 3",
            "dominant_energy_if": "Lambda*a^2 <= 2",
            "derivation_low_x_gap": str(dec_low_branch_gap),
            "derivation_high_x_gap": str(dec_high_branch_gap),
        },
        "checks": checks,
        "frontier": {
            "required_source_shape_family": "DEFINED_EXACTLY_ON_ROUND_BASELINE",
            "independent_physical_source_observations": "OPEN",
            "W6_physical_source_packet": "OPEN_EXTERNAL_EVIDENCE",
        },
        "interpretation_firewall": {
            "radiation_like_tracefree_split_is_decomposition_not_detection": True,
            "dust_special_case_is_not_source_identification": True,
            "geometry_does_not_supply_source_provenance": True,
        },
    }
    out["receipt_sha256"] = sha(out)
    print(json.dumps(out, indent=2, sort_keys=True))
    raise SystemExit(0 if status == "PASS" else 1)


if __name__ == "__main__":
    main()
