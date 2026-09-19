from __future__ import annotations

import hashlib
import json

import evidence_boundary_audit_v0_12 as v12
import three_plus_one_two_epoch_constructor_v0_13 as ctor

SCHEMA = "QHTRI_TOE_EVIDENCE_BOUNDARY_AUDIT_V0_13"


def sha(obj):
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def run():
    old = v12.run()
    new = ctor.run()

    old_topology = old["evidence_reclassification"]["sp3_topology"]
    simplex = new["affine_4simplex"]
    checks = {
        "v012_audit_preserved_pass": old["status"] == "PASS",
        "v013_constructor_pass": new["status"] == "PASS",
        "v012_historical_topology_label_detected": old_topology == "MODEL_DERIVED_TOPOLOGY_CONTROL_NOT_PRODUCTION_SOURCE",
        "five_midpoint_events_affinely_independent": simplex["affine_rank_four"] is True,
        "boundary_facets_match_existing_spatial_packet": simplex["boundary_facets_match_spatial_packet"] is True,
        "same_external_archive_parent": old["sp3_source_extract_sha256"] == new["source"]["realization_id"].split(":")[-1],
        "no_physical_production_promotion": new["physical_production_claim"] is False,
        "no_canon_promotion": new["canon_allowed"] is False,
    }

    status = "PASS" if all(checks.values()) else "FAIL"
    out = {
        "schema": SCHEMA,
        "status": status,
        "authority": "CANDIDATE_ONLY",
        "canon_allowed": False,
        "physical_production_claim": False,
        "empirical_theory_confirmation": False,
        "historical_v012_preserved": True,
        "checks": checks,
        "affine_4simplex_witness": simplex,
        "evidence_reclassification_v013": {
            "sp3_clock": "EXTERNAL_OBSERVATIONAL_ARCHIVE_DERIVED_CLOCK_CONTROL",
            "sp3_topology": "EXTERNAL_OBSERVATIONAL_ARCHIVE_DERIVED_AFFINE_4SIMPLEX_BOUNDARY_CANDIDATE_NOT_GLOBAL_PRODUCTION",
            "sp3_matching": "EXTERNAL_OBSERVATIONAL_ARCHIVE_DERIVED_TANGENT_FIELD_WITH_MODELLED_OVERLAP_BINDING",
            "sp3_metric": "MODEL_FIT_FROM_ARCHIVE_DERIVED_FIELDS",
            "sp3_bianchi": "NUMERICAL_COVARIANT_IDENTITY_VALIDATION_ON_MODEL_FIT",
            "sp3_same_id": "DETERMINISTIC_COMMON_SOURCE_PARENT_BINDING_NOT_INDEPENDENT_PHYSICAL_REALIZATION_PROOF",
        },
        "what_changed": {
            "old_arbitrariness_assumption_rejected": True,
            "reason": "the five midpoint 3+1 events are affinely independent and therefore define a unique nondegenerate affine 4-simplex whose five tetrahedral facets equal the existing spatial packet incidence",
            "global_physical_spatial_manifold_claim": False,
            "production_source_admission": False,
        },
        "remaining_physical_gate": "EXPLICIT_BINDING_FROM_FINITE_OBSERVATIONAL_AFFINE_4SIMPLEX_BOUNDARY_TO_THE_INTENDED_GLOBAL_PHYSICAL_SPATIAL_CARRIER",
    }
    out["receipt_sha256"] = sha(out)
    return out


if __name__ == "__main__":
    result = run()
    print(json.dumps(result, indent=2, sort_keys=True))
    raise SystemExit(0 if result["status"] == "PASS" else 1)
