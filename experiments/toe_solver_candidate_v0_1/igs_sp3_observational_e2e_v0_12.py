from __future__ import annotations

import copy
import json

import igs_sp3_observational_e2e_v0_11 as v11

SCHEMA = "QHTRI_TOE_IGS_SP3_OBSERVATIONAL_E2E_V0_12"
EVIDENCE_CLASS = "EXTERNAL_OBSERVATIONAL_ARCHIVE_DERIVED_MODEL_LEVEL"

_ORIGINAL_REALIZATION_ID = v11.realization_id
_ORIGINAL_SPATIAL_PACKET = v11.spatial_packet


def observational_realization_id() -> str:
    return "observational:igs-sp3:sha256:" + v11.sha(v11.source_records())


def spatial_packet():
    packet = copy.deepcopy(_ORIGINAL_SPATIAL_PACKET())
    source = packet["capture"]["source"]
    source["source_class"] = "CANDIDATE_SOURCE"
    source.pop("capture_receipt_sha256", None)
    source["evidence_class"] = EVIDENCE_CLASS
    source["production_admission_eligible"] = False
    packet["capture"]["physical_realization_id"] = observational_realization_id()
    return packet


def run():
    # Re-run the v0.11 numerical/geometry path with corrected evidence typing.
    # The monkeypatch is strictly scoped and restored even on failure.
    old_rid = v11.realization_id
    old_spatial = v11.spatial_packet
    try:
        v11.realization_id = observational_realization_id
        v11.spatial_packet = spatial_packet
        out = v11.run()
    finally:
        v11.realization_id = old_rid
        v11.spatial_packet = old_spatial

    sp = spatial_packet()
    source = sp["capture"]["source"]
    checks = dict(out.get("checks", {}))
    checks.update({
        "observational_realization_id_typed": out.get("physical_realization_id", "").startswith("observational:igs-sp3:sha256:"),
        "observational_spatial_source_nonproduction": source.get("source_class") == "CANDIDATE_SOURCE",
        "observational_spatial_has_no_production_receipt": "capture_receipt_sha256" not in source,
        "observational_spatial_production_admission_false": source.get("production_admission_eligible") is False,
        "physical_production_claim_false": out.get("physical_production_claim") is False,
    })
    status = "PASS" if out.get("status") == "PASS" and all(checks.values()) else "FAIL"
    corrected = dict(out)
    corrected.update({
        "schema": SCHEMA,
        "status": status,
        "authority": "CANDIDATE_ONLY",
        "canon_allowed": False,
        "physical_production_claim": False,
        "evidence_class": EVIDENCE_CLASS,
        "physical_realization_id": observational_realization_id(),
        "checks": checks,
        "claim_boundary_correction": {
            "supersedes_observational_source_typing_only": "V0_11",
            "numerical_geometry_changed": False,
            "source_class": "CANDIDATE_SOURCE",
            "production_admission_eligible": False,
            "physical_realization_prefix_removed": True,
        },
    })
    corrected["receipt_sha256"] = v11.sha({k: val for k, val in corrected.items() if k != "receipt_sha256"})
    return corrected


if __name__ == "__main__":
    result = run()
    print(json.dumps(result, indent=2, sort_keys=True))
    raise SystemExit(0 if result["status"] == "PASS" else 1)
