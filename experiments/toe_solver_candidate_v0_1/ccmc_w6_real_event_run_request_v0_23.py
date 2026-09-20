from __future__ import annotations

import copy
import json
from typing import Any, Mapping

SCHEMA = "RF_GSC5F_CCMC_W6_REAL_EVENT_RUN_REQUEST_VALIDATION_V0_23"

TARGET_START = "2015-01-21T00:01:00Z"
TARGET_END = "2015-01-21T00:03:00Z"

REQUIRED_FIELDS = {
    "density",
    "pressure",
    "velocity_x",
    "velocity_y",
    "velocity_z",
    "magnetic_field_x",
    "magnetic_field_y",
    "magnetic_field_z",
}

REQUIRED_METADATA = {
    "model_name",
    "model_version",
    "run_type",
    "start_time",
    "end_time",
    "output_coordinate_system",
    "solar_wind_input_source",
    "grid_description",
    "equation_of_state_or_closure",
    "density_convention",
    "pressure_convention",
}


class ManifestError(ValueError):
    pass


def _nonempty(v: Any, label: str) -> str:
    s = str(v).strip()
    if not s:
        raise ManifestError(f"{label} must be nonempty")
    return s


def validate_manifest(m: Mapping[str, Any]) -> dict[str, Any]:
    if m.get("schema") != "RF_GSC5F_CCMC_RUN_REQUEST_MANIFEST_V0_23":
        raise ManifestError("unexpected schema")

    if m.get("submission_authorized") is not False:
        raise ManifestError("manifest must not authorize external submission")

    if m.get("model_family") != "SWMF_GM_BATSRUS":
        raise ManifestError("primary model family must be SWMF/GM/BATSRUS")

    if m.get("run_class") != "REAL_EVENT":
        raise ManifestError("run class must be REAL_EVENT")

    if m.get("output_frame") != "GSM":
        raise ManifestError("output frame must be GSM")

    target = m.get("target_interval")
    if not isinstance(target, Mapping):
        raise ManifestError("target_interval must be an object")
    if target.get("start") != TARGET_START or target.get("end") != TARGET_END:
        raise ManifestError("target interval mismatch")

    driver = m.get("preferred_driver")
    if driver not in {"OMNI", "ACE_LEVEL2"}:
        raise ManifestError("unsupported driver lineage")

    fields = set(m.get("required_fields") or [])
    if not REQUIRED_FIELDS.issubset(fields):
        raise ManifestError("required MHD output field missing")

    required_metadata = set(m.get("required_metadata") or [])
    if not REQUIRED_METADATA.issubset(required_metadata):
        raise ManifestError("required run metadata field missing")

    patches = set(m.get("required_patch_ids") or [])
    if patches != {"SP3_STEREO_N", "SP3_STEREO_S"}:
        raise ManifestError("full two-patch coverage is required")

    if m.get("allow_anchor_only_output") is not False:
        raise ManifestError("anchor-only output must be rejected")

    if m.get("allow_metric_derived_source") is not False:
        raise ManifestError("target-metric-derived source must be rejected")

    return {
        "submission_authorized": False,
        "science_target_fixed": True,
        "primary_model_fixed": True,
        "driver_class_fixed": True,
        "required_fields_complete": True,
        "metadata_contract_complete": True,
        "two_patch_coverage_required": True,
        "metric_source_firewall_active": True,
        "external_run_still_required": True,
    }


def base_manifest():
    return {
        "schema": "RF_GSC5F_CCMC_RUN_REQUEST_MANIFEST_V0_23",
        "submission_authorized": False,
        "model_family": "SWMF_GM_BATSRUS",
        "run_class": "REAL_EVENT",
        "output_frame": "GSM",
        "target_interval": {"start": TARGET_START, "end": TARGET_END},
        "preferred_driver": "OMNI",
        "required_fields": sorted(REQUIRED_FIELDS),
        "required_metadata": sorted(REQUIRED_METADATA),
        "required_patch_ids": ["SP3_STEREO_N", "SP3_STEREO_S"],
        "allow_anchor_only_output": False,
        "allow_metric_derived_source": False,
    }


def rejected(m):
    try:
        validate_manifest(m)
    except ManifestError:
        return True
    return False


def main():
    good = base_manifest()
    accepted = validate_manifest(good)

    submit = copy.deepcopy(good)
    submit["submission_authorized"] = True

    bad_field = copy.deepcopy(good)
    bad_field["required_fields"].remove("pressure")

    anchor_only = copy.deepcopy(good)
    anchor_only["required_patch_ids"] = ["SP3_STEREO_N"]

    metric_leak = copy.deepcopy(good)
    metric_leak["allow_metric_derived_source"] = True

    checks = {
        "manifest_structurally_valid": accepted["science_target_fixed"],
        "external_submission_not_authorized": accepted["submission_authorized"] is False,
        "unauthorized_submission_manifest_rejected": rejected(submit),
        "missing_required_MHD_field_rejected": rejected(bad_field),
        "anchor_only_patch_request_rejected": rejected(anchor_only),
        "metric_derived_source_route_rejected": rejected(metric_leak),
        "actual_CCMC_run_remains_open": True,
    }

    status = "PASS" if all(checks.values()) else "FAIL"
    out = {
        "schema": SCHEMA,
        "status": status,
        "authority": "CANDIDATE_ONLY",
        "canon_allowed": False,
        "physical_production_claim": False,
        "submission_authorized": False,
        "checks": checks,
        "frontier": {
            "run_request_manifest": "READY",
            "external_submission": "NOT_AUTHORIZED",
            "actual_CCMC_run_id": "OPEN",
            "actual_W6_source_tensor": "OPEN",
            "RF_E26_production_promotion": "OPEN",
        },
    }
    print(json.dumps(out, indent=2, sort_keys=True))
    raise SystemExit(0 if status == "PASS" else 1)


if __name__ == "__main__":
    main()
