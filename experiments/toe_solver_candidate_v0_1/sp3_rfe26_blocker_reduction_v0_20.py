from __future__ import annotations

import json
from pathlib import Path

from src.rfc.canonical_atlas_domain_coverage import (
    certify_canonical_atlas_domain_coverage,
)
from src.rfc.natural_einstein_globalization import (
    MetricAtlasOverlap,
    NaturalEinsteinGlobalizationError,
    NaturalEinsteinPatch,
    certify_natural_einstein_globalization,
)

ROOT = Path(__file__).resolve().parents[2]
R019 = ROOT / "validation" / "toe_solver_candidate_v0_1" / "SP3_STEREOGRAPHIC_RFE25_ATLAS_V0_19.json"

SCHEMA = "QHTRI_TOE_SP3_RFE26_BLOCKER_REDUCTION_V0_20"

PATCHES = ("SP3_STEREO_N", "SP3_STEREO_S")
DOMAIN = "SP3_STATIONARY_PRODUCT_DOMAIN_V0_18_V0_19"

I4 = (
    (1.0, 0.0, 0.0, 0.0),
    (0.0, 1.0, 0.0, 0.0),
    (0.0, 0.0, 1.0, 0.0),
    (0.0, 0.0, 0.0, 1.0),
)
ETA = (
    (-1.0, 0.0, 0.0, 0.0),
    (0.0, 1.0, 0.0, 0.0),
    (0.0, 0.0, 1.0, 0.0),
    (0.0, 0.0, 0.0, 1.0),
)


def main():
    r19 = json.loads(R019.read_text(encoding="utf-8"))

    # Current state: no physical RF-E24 local-solution receipts are admitted.
    current_cov = certify_canonical_atlas_domain_coverage(
        atlas_patch_ids=PATCHES,
        local_solution_patch_ids=("SP3_STEREO_N",),
        target_domain_id=DOMAIN,
        atlas_domain_id=DOMAIN,
        canonical_atlas_coverage_certified=True,
    )

    # Sufficiency test only: if W6 eventually supplies both exact atlas patch ids,
    # W7 domain coverage is derived by the existing GSC5B certifier.
    complete_cov = certify_canonical_atlas_domain_coverage(
        atlas_patch_ids=PATCHES,
        local_solution_patch_ids=PATCHES,
        target_domain_id=DOMAIN,
        atlas_domain_id=DOMAIN,
        canonical_atlas_coverage_certified=True,
    )

    foreign_cov = certify_canonical_atlas_domain_coverage(
        atlas_patch_ids=PATCHES,
        local_solution_patch_ids=PATCHES + ("FOREIGN_PATCH",),
        target_domain_id=DOMAIN,
        atlas_domain_id=DOMAIN,
        canonical_atlas_coverage_certified=True,
    )

    # GSC5A must fail closed when a declared local RF-E24 solution receipt is absent.
    gsc5a_missing_w6_failclosed = False
    try:
        certify_natural_einstein_globalization(
            [
                NaturalEinsteinPatch(
                    name="SP3_STEREO_N",
                    metric=ETA,
                    cosmological_constant=0.0,
                    kappa_e=1.0,
                    source_field_lineage_id="OPEN_PHYSICAL_SOURCE_LINEAGE",
                    local_solution_receipt_id="OPEN:SP3_STEREO_N",
                    local_solution_certified=False,
                )
            ],
            [],
            shared_atlas_certified=True,
            smooth_atlas_certified=True,
            domain_coverage_certified=False,
        )
    except NaturalEinsteinGlobalizationError as exc:
        gsc5a_missing_w6_failclosed = "local solution receipt" in str(exc)

    # GSC5A must also fail closed on mixed source lineage even when receipt flags are true.
    gsc5a_lineage_mismatch_failclosed = False
    try:
        certify_natural_einstein_globalization(
            [
                NaturalEinsteinPatch(
                    name="SP3_STEREO_N",
                    metric=ETA,
                    cosmological_constant=0.0,
                    kappa_e=1.0,
                    source_field_lineage_id="physical-source-A",
                    local_solution_receipt_id="receipt:N",
                    local_solution_certified=True,
                ),
                NaturalEinsteinPatch(
                    name="SP3_STEREO_S",
                    metric=ETA,
                    cosmological_constant=0.0,
                    kappa_e=1.0,
                    source_field_lineage_id="physical-source-B",
                    local_solution_receipt_id="receipt:S",
                    local_solution_certified=True,
                ),
            ],
            [MetricAtlasOverlap("SP3_STEREO_N", "SP3_STEREO_S", I4)],
            shared_atlas_certified=True,
            smooth_atlas_certified=True,
            domain_coverage_certified=True,
        )
    except NaturalEinsteinGlobalizationError as exc:
        gsc5a_lineage_mismatch_failclosed = "source field lineage mismatch" in str(exc)

    # Type-level sufficiency demonstration with declared complete parents.
    # This is NOT current evidence and is explicitly not promoted.
    counterfactual_complete = certify_natural_einstein_globalization(
        [
            NaturalEinsteinPatch(
                name="SP3_STEREO_N",
                metric=ETA,
                cosmological_constant=0.0,
                kappa_e=1.0,
                source_field_lineage_id="DEMO_COMMON_SOURCE_LINEAGE_NOT_EVIDENCE",
                local_solution_receipt_id="DEMO_RF_E24_N_NOT_EVIDENCE",
                local_solution_certified=True,
            ),
            NaturalEinsteinPatch(
                name="SP3_STEREO_S",
                metric=ETA,
                cosmological_constant=0.0,
                kappa_e=1.0,
                source_field_lineage_id="DEMO_COMMON_SOURCE_LINEAGE_NOT_EVIDENCE",
                local_solution_receipt_id="DEMO_RF_E24_S_NOT_EVIDENCE",
                local_solution_certified=True,
            ),
        ],
        [MetricAtlasOverlap("SP3_STEREO_N", "SP3_STEREO_S", I4)],
        shared_atlas_certified=True,
        smooth_atlas_certified=True,
        domain_coverage_certified=complete_cov.domain_coverage_derived,
    )

    checks = {
        "parent_v019_PASS": r19.get("status") == "PASS",
        "parent_v019_mathematical_RF_E25_atlas_seam_closed": r19.get("frontier", {}).get(
            "candidate_mathematical_RF_E25_atlas_seam"
        ) == "CLOSED",
        "parent_v019_executable_RF_E25_compatibility_PASS": r19.get("frontier", {}).get(
            "executable_RF_E25_data_structure_compatibility"
        ) == "PASS",
        "current_missing_one_W6_patch_keeps_GSC5B_domain_coverage_open": not current_cov.domain_coverage_derived,
        "complete_two_patch_W6_set_derives_GSC5B_domain_coverage": complete_cov.domain_coverage_derived,
        "foreign_solution_patch_id_keeps_GSC5B_open": not foreign_cov.domain_coverage_derived,
        "GSC5A_missing_local_solution_receipt_fails_closed": gsc5a_missing_w6_failclosed,
        "GSC5A_source_lineage_mismatch_fails_closed": gsc5a_lineage_mismatch_failclosed,
        "GSC5A_reduced_contract_sufficient_when_all_declared_parents_supplied": counterfactual_complete.global_einstein_carrier,
        "counterfactual_complete_packet_is_not_current_evidence": True,
        "effective_stress_from_geometry_not_promoted_as_physical_source": True,
        "physical_W6_receipts_remain_open": True,
        "common_physical_source_field_lineage_remains_open": True,
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
        "reduction_class": "DEPENDENCY_REDUCTION_NOT_SOURCE_COMPLETION",
        "atlas": {
            "patch_ids": list(PATCHES),
            "target_domain_id": DOMAIN,
            "atlas_cover_status": "EXACT_PARENT_V019",
            "smooth_shared_metric_atlas_status": "CANDIDATE_PASS_PARENT_V019",
        },
        "current": {
            "admitted_physical_RF_E24_solution_patch_ids": [],
            "GSC5B_domain_coverage_currently_promoted": False,
            "reason": "W6 physical local-solution receipt set is not supplied",
        },
        "derived_if_W6_complete": {
            "required_exact_patch_set": list(PATCHES),
            "GSC5B_domain_coverage": complete_cov.domain_coverage_derived,
            "GSC5A_tensor_overlap_covariance": counterfactual_complete.einstein_overlap_covariance,
            "GSC5A_stress_overlap_covariance": counterfactual_complete.stress_overlap_covariance,
            "GSC5A_residual_overlap_covariance": counterfactual_complete.residual_overlap_covariance,
            "note": "type-level sufficiency only; demo receipt ids are not evidence",
        },
        "checks": checks,
        "frontier": {
            "independent_W7_domain_coverage_blocker": "REDUCED_TO_W6_PATCH_COMPLETENESS_ON_THIS_TWO_CHART_ROUTE",
            "W6_physical_RF_E24_local_solution_receipts": "OPEN",
            "common_physical_source_field_lineage": "OPEN",
            "RF_E26_production_promotion": "OPEN",
        },
        "interpretation_firewall": {
            "no_T_equals_G_over_kappa_physical_source_promotion": True,
            "counterfactual_dependency_packet_is_not_observational_evidence": True,
            "geometry_does_not_supply_physical_source_lineage": True,
        },
    }
    print(json.dumps(out, indent=2, sort_keys=True))
    raise SystemExit(0 if status == "PASS" else 1)


if __name__ == "__main__":
    main()
