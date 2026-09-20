from __future__ import annotations

import copy
import json
from typing import Any, Mapping, Sequence

SCHEMA = "RF_GSC5E_SP3_W6_MHD_SOURCE_ACQUISITION_VALIDATION_V0_22"
PATCHES = {"SP3_STEREO_N", "SP3_STEREO_S"}

PRIMARY_ALLOWED = {"SWMF_BATSRUS", "OPEN_GGCM"}
AUXILIARY_ONLY = {
    "IGS_SP3_CLOCK",
    "IERS_FRAME_TIME",
    "EGM2008",
    "PREM",
    "NRLMSIS",
    "IRI",
}

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


class AcquisitionError(ValueError):
    pass


def _nonempty(value: Any, label: str) -> str:
    out = str(value).strip()
    if not out:
        raise AcquisitionError(f"{label} must be nonempty")
    return out


def validate_manifest(manifest: Mapping[str, Any]) -> dict[str, Any]:
    if manifest.get("schema") != "RF_GSC5E_W6_MHD_ACQUISITION_MANIFEST_V0_22":
        raise AcquisitionError("unexpected acquisition manifest schema")

    model = _nonempty(manifest.get("primary_model"), "primary_model")
    if model in AUXILIARY_ONLY:
        raise AcquisitionError("auxiliary source class cannot be the W6 primary source")
    if model not in PRIMARY_ALLOWED:
        raise AcquisitionError("unsupported primary MHD source class")

    interval = manifest.get("time_interval")
    if not isinstance(interval, Mapping):
        raise AcquisitionError("time_interval must be an object")
    start = _nonempty(interval.get("start"), "time_interval.start")
    end = _nonempty(interval.get("end"), "time_interval.end")
    if start > "2015-01-21T00:01:00Z" or end < "2015-01-21T00:03:00Z":
        raise AcquisitionError("source run does not cover both frozen SP3 epochs")

    fields = set(manifest.get("available_fields") or [])
    missing = REQUIRED_FIELDS - fields
    if missing:
        raise AcquisitionError(f"missing required MHD fields: {sorted(missing)}")

    eos = manifest.get("closure_metadata")
    if not isinstance(eos, Mapping):
        raise AcquisitionError("closure_metadata must be an object")
    _nonempty(eos.get("equation_of_state"), "closure_metadata.equation_of_state")
    _nonempty(eos.get("density_convention"), "closure_metadata.density_convention")
    _nonempty(eos.get("pressure_convention"), "closure_metadata.pressure_convention")

    coverage = set(manifest.get("covered_patch_ids") or [])
    if coverage != PATCHES:
        raise AcquisitionError("MHD source coverage must match both atlas patches exactly")

    transform = manifest.get("coordinate_transform")
    if not isinstance(transform, Mapping):
        raise AcquisitionError("coordinate_transform must be an object")
    for key in (
        "source_frame",
        "target_model_frame",
        "transform_library",
        "transform_version",
        "auxiliary_input_digest",
    ):
        _nonempty(transform.get(key), f"coordinate_transform.{key}")

    lineage = manifest.get("driver_lineage")
    if not isinstance(lineage, Sequence) or isinstance(lineage, (str, bytes)) or not lineage:
        raise AcquisitionError("driver_lineage must be nonempty")
    for idx, item in enumerate(lineage):
        if not isinstance(item, Mapping):
            raise AcquisitionError("driver_lineage item must be an object")
        _nonempty(item.get("observation_id"), f"driver_lineage[{idx}].observation_id")
        _nonempty(item.get("digest"), f"driver_lineage[{idx}].digest")

    interpolation = manifest.get("interpolation_receipt")
    if not isinstance(interpolation, Mapping):
        raise AcquisitionError("interpolation_receipt must be an object")
    for key in (
        "spatial_method",
        "temporal_method",
        "source_grid_digest",
        "implementation_digest",
    ):
        _nonempty(interpolation.get(key), f"interpolation_receipt.{key}")

    if manifest.get("target_metric_used_to_construct_source") is not False:
        raise AcquisitionError("target metric must not be used to construct the W6 source")

    authority = manifest.get("authority")
    if authority != "CANDIDATE_ONLY":
        raise AcquisitionError("v0.22 acquisition manifest is candidate-only")

    return {
        "primary_model_allowed": True,
        "epoch_coverage_complete": True,
        "required_MHD_fields_complete": True,
        "closure_metadata_complete": True,
        "full_two_patch_coverage": True,
        "coordinate_transform_receipt_complete": True,
        "driver_lineage_present": True,
        "interpolation_receipt_present": True,
        "independent_of_target_metric": True,
        "production_admission": False,
    }


def base_fixture():
    return {
        "schema": "RF_GSC5E_W6_MHD_ACQUISITION_MANIFEST_V0_22",
        "primary_model": "SWMF_BATSRUS",
        "time_interval": {
            "start": "2015-01-20T23:55:00Z",
            "end": "2015-01-21T00:10:00Z",
        },
        "available_fields": sorted(REQUIRED_FIELDS | {"current_density_x", "current_density_y", "current_density_z"}),
        "closure_metadata": {
            "equation_of_state": "MODEL_DECLARED",
            "density_convention": "MODEL_DECLARED",
            "pressure_convention": "MODEL_DECLARED",
        },
        "covered_patch_ids": sorted(PATCHES),
        "coordinate_transform": {
            "source_frame": "SP3_SOURCE_FRAME",
            "target_model_frame": "GSM",
            "transform_library": "DECLARED_EXTERNAL_TRANSFORM",
            "transform_version": "FIXTURE",
            "auxiliary_input_digest": "fixture-digest",
        },
        "driver_lineage": [
            {
                "observation_id": "solar-wind-driver-fixture",
                "digest": "fixture-driver-digest",
            }
        ],
        "interpolation_receipt": {
            "spatial_method": "DECLARED",
            "temporal_method": "DECLARED",
            "source_grid_digest": "fixture-grid-digest",
            "implementation_digest": "fixture-impl-digest",
        },
        "target_metric_used_to_construct_source": False,
        "authority": "CANDIDATE_ONLY",
    }


def rejected(manifest):
    try:
        validate_manifest(manifest)
    except AcquisitionError:
        return True
    return False


def main():
    good = base_fixture()
    accepted = validate_manifest(good)

    bad_primary = copy.deepcopy(good)
    bad_primary["primary_model"] = "EGM2008"

    missing_field = copy.deepcopy(good)
    missing_field["available_fields"].remove("pressure")

    anchor_only = copy.deepcopy(good)
    anchor_only["covered_patch_ids"] = ["SP3_STEREO_N"]

    no_driver = copy.deepcopy(good)
    no_driver["driver_lineage"] = []

    metric_leak = copy.deepcopy(good)
    metric_leak["target_metric_used_to_construct_source"] = True

    checks = {
        "independent_MHD_fixture_structurally_accepted": accepted["primary_model_allowed"],
        "auxiliary_gravity_model_rejected_as_primary_W6_source": rejected(bad_primary),
        "missing_MHD_field_rejected": rejected(missing_field),
        "incomplete_patch_coverage_rejected": rejected(anchor_only),
        "missing_external_driver_lineage_rejected": rejected(no_driver),
        "target_metric_source_leakage_rejected": rejected(metric_leak),
        "manifest_PASS_is_not_external_W6_evidence_PASS": True,
        "actual_external_MHD_run_remains_open": True,
    }

    status = "PASS" if all(checks.values()) else "FAIL"
    out = {
        "schema": SCHEMA,
        "status": status,
        "authority": "CANDIDATE_ONLY",
        "canon_allowed": False,
        "physical_production_claim": False,
        "acquisition_class": "EXTERNAL_W6_SOURCE_ROUTE_INFRASTRUCTURE",
        "primary_source_candidates": ["SWMF_BATSRUS", "OPEN_GGCM"],
        "auxiliary_only_source_classes": sorted(AUXILIARY_ONLY),
        "required_MHD_fields": sorted(REQUIRED_FIELDS),
        "checks": checks,
        "frontier": {
            "acquisition_route": "DEFINED_AND_EXECUTABLE",
            "actual_external_MHD_run": "OPEN",
            "actual_W6_source_tensor": "OPEN",
            "RF_E24_patch_receipts": "OPEN",
            "RF_E26_production_promotion": "OPEN",
        },
    }
    print(json.dumps(out, indent=2, sort_keys=True))
    raise SystemExit(0 if status == "PASS" else 1)


if __name__ == "__main__":
    main()
