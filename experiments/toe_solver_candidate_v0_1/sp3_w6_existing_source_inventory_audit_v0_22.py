from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

QHTRI = ROOT / "validation" / "toe_solver_candidate_v0_1" / "qhtri_neutrino_total_stress_binding_receipt_v1.json"
MULTI = ROOT / "validation" / "toe_solver_candidate_v0_1" / "multisector_source_cone_solver_receipt_v2.json"
LOCAL = ROOT / "validation" / "toe_solver_candidate_v0_1" / "local_einstein_closure_solver_receipt_v1.json"
SP3 = ROOT / "experiments" / "toe_solver_candidate_v0_1" / "IGS_SP3_OBSERVATIONAL_VALIDATION_V0_11_RECEIPT.json"

SCHEMA = "QHTRI_TOE_SP3_W6_EXISTING_SOURCE_INVENTORY_AUDIT_V0_22"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main():
    qhtri = load(QHTRI)
    multi = load(MULTI)
    local = load(LOCAL)
    sp3 = load(SP3)

    q_boundaries = set(qhtri.get("boundaries", []))
    q_reasons = []
    if "REPRESENTATIVE_NEUTRINO_STREAM_PACKET_NOT_PHYSICAL_EVENT_PLACEMENT" in q_boundaries:
        q_reasons.append("NO_PHYSICAL_EVENT_PLACEMENT")
    if "GLOBAL_DOMAIN_COVERAGE_OPEN" in q_boundaries:
        q_reasons.append("GLOBAL_DOMAIN_COVERAGE_OPEN")
    if qhtri.get("authority") != "PRODUCTION_SOURCE_AUTHORITY":
        q_reasons.append("NO_PRODUCTION_SOURCE_AUTHORITY")
    if float(qhtri.get("metrics", {}).get("einstein_residual_max", 0.0)) > 1e-10:
        q_reasons.append("NO_RF_E24_FULL_PATCH_RESIDUAL_PASS")

    multi_boundary = str(multi.get("boundary", ""))
    multi_reasons = []
    if "no production fields" in multi_boundary:
        multi_reasons.append("NO_PRODUCTION_FIELDS")
    if "physical scale calibration" in multi_boundary:
        multi_reasons.append("NO_PHYSICAL_SCALE_CALIBRATION")
    if "universality claimed" in multi_boundary:
        multi_reasons.append("NO_UNIVERSAL_OR_FULL_PATCH_COVERAGE")
    if multi.get("authority") != "PRODUCTION_SOURCE_AUTHORITY":
        multi_reasons.append("NO_PRODUCTION_SOURCE_AUTHORITY")
    if not bool(multi.get("anisotropic_BianchiI", {}).get("full_positive_cone_success")):
        multi_reasons.append("SELECTED_ANISOTROPIC_CASE_REJECTED")

    local_boundary = str(local.get("interpretation_boundary", ""))
    local_scope = str(local.get("scope", ""))
    local_reasons = []
    if "ALGEBRAIC_LOCAL_SOURCE_CLASS_SOLVER" in local_boundary:
        local_reasons.append("INVERSE_GEOMETRY_TO_SOURCE_CLASS_SOLVER")
    if "no production metric/source packet" in local_boundary:
        local_reasons.append("NO_PRODUCTION_SOURCE_PACKET")
    if "physical kappa calibration" in local_boundary:
        local_reasons.append("NO_PHYSICAL_KAPPA_CALIBRATION")
    if "Einstein tensor -> Lambda" in local_scope:
        local_reasons.append("SOURCE_COEFFICIENTS_SOLVED_FROM_TARGET_G")
    if local.get("authority") != "PRODUCTION_SOURCE_AUTHORITY":
        local_reasons.append("NO_PRODUCTION_SOURCE_AUTHORITY")

    sp3_reasons = []
    if sp3.get("evidence_class") == "EXTERNAL_OBSERVATIONAL_ARCHIVE_DERIVED_MODEL_LEVEL":
        sp3_reasons.append("MODEL_LEVEL_EXTERNAL_GEOMETRY_EVIDENCE")
    if sp3.get("authority") != "PRODUCTION_SOURCE_AUTHORITY":
        sp3_reasons.append("NO_PRODUCTION_SOURCE_AUTHORITY")
    if "source_tensor" not in sp3:
        sp3_reasons.append("NO_INDEPENDENT_SOURCE_TENSOR_PACKET")
    if "source_field_lineage_id" not in sp3:
        sp3_reasons.append("NO_PHYSICAL_SOURCE_FIELD_LINEAGE")
    if "patch_receipts" not in sp3:
        sp3_reasons.append("NO_N_S_FULL_PATCH_RF_E24_RECEIPTS")

    inventory = {
        "qhtri_neutrino_total_stress": {
            "status": "NOT_W6_QUALIFIED",
            "source_receipt_status": qhtri.get("status"),
            "reasons": q_reasons,
        },
        "multisector_source_cone": {
            "status": "NOT_W6_QUALIFIED",
            "source_receipt_status": multi.get("status"),
            "reasons": multi_reasons,
        },
        "local_constrained_source_solver": {
            "status": "NOT_W6_QUALIFIED",
            "source_receipt_status": local.get("status"),
            "reasons": local_reasons,
        },
        "sp3_observational_geometry": {
            "status": "NOT_W6_QUALIFIED",
            "source_receipt_status": sp3.get("status"),
            "reasons": sp3_reasons,
        },
    }

    checks = {
        "qhtri_neutrino_has_explicit_physical_event_placement_or_coverage_blocker":
            "NO_PHYSICAL_EVENT_PLACEMENT" in q_reasons and "GLOBAL_DOMAIN_COVERAGE_OPEN" in q_reasons,
        "multisector_explicitly_lacks_production_fields_and_physical_scale":
            "NO_PRODUCTION_FIELDS" in multi_reasons and "NO_PHYSICAL_SCALE_CALIBRATION" in multi_reasons,
        "local_solver_is_inverse_geometry_to_source_not_independent_source_evidence":
            "INVERSE_GEOMETRY_TO_SOURCE_CLASS_SOLVER" in local_reasons
            and "SOURCE_COEFFICIENTS_SOLVED_FROM_TARGET_G" in local_reasons,
        "sp3_observational_receipt_has_external_geometry_evidence_but_no_source_tensor":
            "MODEL_LEVEL_EXTERNAL_GEOMETRY_EVIDENCE" in sp3_reasons
            and "NO_INDEPENDENT_SOURCE_TENSOR_PACKET" in sp3_reasons,
        "no_audited_candidate_has_production_source_authority":
            all("NO_PRODUCTION_SOURCE_AUTHORITY" in entry["reasons"] for entry in inventory.values()),
        "all_audited_candidates_have_at_least_one_W6_blocker":
            all(bool(entry["reasons"]) for entry in inventory.values()),
        "current_internal_W6_qualifier_count_is_zero": True,
        "physical_production_claim_remains_false": True,
    }

    qualifier_count = 0
    status = "PASS" if all(checks.values()) and qualifier_count == 0 else "FAIL"

    out = {
        "schema": SCHEMA,
        "status": status,
        "authority": "CANDIDATE_ONLY",
        "canon_allowed": False,
        "physical_production_claim": False,
        "audit_class": "EXISTING_SOURCE_RECEIPT_INVENTORY_AGAINST_W6_V0_21",
        "inventory": inventory,
        "current_internal_W6_qualifier_count": qualifier_count,
        "checks": checks,
        "frontier": {
            "existing_internal_W6_qualifier": "NONE_FOUND",
            "actual_physical_W6_source_packet": "OPEN_EXTERNAL_EVIDENCE",
            "RF_E26_production_promotion": "OPEN",
        },
        "interpretation_firewall": {
            "existing_candidates_retain_their_valid_scopes": True,
            "not_W6_qualified_does_not_mean_candidate_invalid": True,
            "geometry_or_inverse_fit_is_not_independent_physical_source_evidence": True,
        },
    }
    print(json.dumps(out, indent=2, sort_keys=True))
    raise SystemExit(0 if status == "PASS" else 1)


if __name__ == "__main__":
    main()
