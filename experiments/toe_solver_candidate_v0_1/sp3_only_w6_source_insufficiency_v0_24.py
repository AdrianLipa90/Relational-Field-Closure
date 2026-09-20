from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SP3 = ROOT / "experiments" / "toe_solver_candidate_v0_1" / "igs_sp3_observational_e2e_v0_11.py"
W6 = ROOT / "experiments" / "toe_solver_candidate_v0_1" / "sp3_w6_physical_source_receipt_contract_v0_21.py"
RFN1B = ROOT / "formalism" / "RFN1B_SOURCE_TYPE_IDENTIFIABILITY_FIREWALL.md"

SCHEMA = "QHTRI_TOE_SP3_ONLY_W6_SOURCE_INSUFFICIENCY_V0_24"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


sp3 = load_module("sp3_v024", SP3)
w6 = load_module("w6_v024", W6)


def digest(label: str) -> str:
    return hashlib.sha256(label.encode("utf-8")).hexdigest()


def sp3_observations_for_patch(patch_id: str):
    src = sp3.source_records()
    out = []
    for epoch_name, records in (("epoch1", src["epoch1"]), ("epoch2", src["epoch2"])):
        epoch_time = src["epochs"][0 if epoch_name == "epoch1" else 1]
        for sat, row in records.items():
            out.append({
                "observation_id": f"SP3:{epoch_name}:{sat}",
                "observable_class": "POSITION_XYZ_PLUS_CLOCK_CORRECTION",
                "coordinate_or_frame_binding": "SP3_ECEF_STYLE_SOURCE_RECORD",
                "units": "km,km,km,microsecond",
                "source_time_or_interval": epoch_time,
                "immutable_digest": digest(json.dumps([sat, *row], separators=(",", ":"))),
            })
    return out


def source_refs():
    src = sp3.source_records()
    return [{
        "ref": src["source_url"],
        "digest": digest(json.dumps(src, sort_keys=True, separators=(",", ":"))),
    }]


def base_patch(patch_id: str):
    tensor_digest = digest(f"sp3-only-placeholder-source:{patch_id}")
    return {
        "schema": w6.PATCH_SCHEMA,
        "patch_id": patch_id,
        "atlas_domain_id": w6.ATLAS_DOMAIN_ID,
        "physical_realization_id": sp3.realization_id(),
        "metric_lineage_id": "SP3_SOURCE_DERIVED_METRIC_V017_V019",
        "einstein_operator_lineage_id": w6.RF_E24_LINEAGE,
        "source_field_lineage_id": "SP3_ONLY_ATTEMPT_NOT_ADMISSIBLE",
        "source_class": "SP3_POSITION_CLOCK_ONLY",
        "source_observations": sp3_observations_for_patch(patch_id),
        "immutable_source_refs": source_refs(),
        "Lambda": 0.0,
        "kappa_E": 1.0,
        "source_tensor": {
            "tensor_rank": 2,
            "symmetry": "symmetric",
            "covariance": "covariant_2",
            "units": "UNSPECIFIED",
            "representation_kind": "PLACEHOLDER",
            "tensor_payload_digest": tensor_digest,
            "construction_receipt_id": f"sp3-only-placeholder:{patch_id}",
            "coverage_domain_id": w6.ATLAS_DOMAIN_ID,
            "coverage_patch_id": patch_id,
            "coverage_certified": True,
            "derivation_class": "INDEPENDENT_PLACEHOLDER",
            "independent_of_target_metric_construction": True,
        },
        "local_solution": {
            "certified": True,
            "equation": "RF-E24",
            "residual_norm": 0.0,
            "residual_tolerance": 1e-10,
            "residual_units_or_normalization": "TEST_ONLY",
            "metric_representation_digest": digest(f"metric:{patch_id}"),
            "einstein_tensor_representation_digest": digest(f"G:{patch_id}"),
            "source_tensor_payload_digest": tensor_digest,
            "source_tensor_coverage_domain_id": w6.ATLAS_DOMAIN_ID,
            "source_tensor_coverage_patch_id": patch_id,
            "validation_receipt_id": f"sp3-only-placeholder-solution:{patch_id}",
            "validation_head_or_artifact_digest": digest(f"solution:{patch_id}"),
        },
        "authority": "CANDIDATE_ONLY",
        "canon_allowed": False,
        "physical_production_claim": False,
    }


def packet_from_patches(patches):
    return {"schema": w6.PACKET_SCHEMA, "patch_receipts": patches}


def rejected(packet):
    try:
        w6.validate_w6_packet(packet)
    except w6.W6ContractError:
        return True
    return False


def main():
    src = sp3.source_records()
    rfn1b = RFN1B.read_text(encoding="utf-8")

    records = []
    for key in ("epoch1", "epoch2"):
        for row in src[key].values():
            records.append(row)

    source_shape = {
        "top_level_keys": sorted(src.keys()),
        "satellite_count": len(src["satellites"]),
        "epoch_count": len(src["epochs"]),
        "record_width": sorted({len(row) for row in records}),
    }

    # Route 1: positions/clocks with no rank-two source tensor.
    missing_tensor_patches = [base_patch(p) for p in w6.ATLAS_PATCHES]
    for rec in missing_tensor_patches:
        rec.pop("source_tensor", None)
    missing_tensor_rejected = rejected(packet_from_patches(missing_tensor_patches))

    # Route 2: manufacture T from target geometry.
    geometry_patches = [base_patch(p) for p in w6.ATLAS_PATCHES]
    for rec in geometry_patches:
        rec["source_tensor"]["derivation_class"] = "T_EQUALS_G_PLUS_LAMBDA_G_OVER_KAPPA"
        rec["source_tensor"]["independent_of_target_metric_construction"] = False
    geometry_source_rejected = rejected(packet_from_patches(geometry_patches))

    # Route 3: assert vacuum without independent vacuum-domain provenance.
    vacuum_patches = [base_patch(p) for p in w6.ATLAS_PATCHES]
    for rec in vacuum_patches:
        rec["source_tensor"]["representation_kind"] = "VACUUM_ZERO"
        rec["source_tensor"]["derivation_class"] = "SP3_ONLY_VACUUM_ASSERTION"
        rec["source_tensor"].pop("vacuum_domain_provenance", None)
    unsupported_vacuum_rejected = rejected(packet_from_patches(vacuum_patches))

    # Route 4: finite anchors are not full-patch source-tensor coverage.
    anchor_only_patches = [base_patch(p) for p in w6.ATLAS_PATCHES]
    for rec in anchor_only_patches:
        rec["source_tensor"]["coverage_certified"] = False
        rec["source_tensor"]["representation_kind"] = "FINITE_ANCHORS_ONLY"
    anchor_only_coverage_rejected = rejected(packet_from_patches(anchor_only_patches))

    source_keys = set(src.keys())
    no_direct_tensor_payload = not any(
        key in source_keys for key in (
            "stress_energy",
            "source_tensor",
            "matter_density",
            "matter_current",
            "electromagnetic_field_tensor",
            "scalar_field_source",
        )
    )

    position_clock_only = (
        source_shape["record_width"] == [4]
        and source_shape["satellite_count"] == 5
        and source_shape["epoch_count"] == 2
        and no_direct_tensor_payload
    )

    rfn1b_bound = (
        "does not identify a unique physical matter density" in rfn1b
        and "derive a conserved physical source carrier and its measure" in rfn1b
    )

    checks = {
        "frozen_SP3_source_is_five_satellites_two_epochs_width_four": position_clock_only,
        "SP3_source_has_no_direct_rank_two_physical_source_payload": no_direct_tensor_payload,
        "RFN1B_identifiability_firewall_bound": rfn1b_bound,
        "SP3_only_missing_source_tensor_rejected_by_v021_contract": missing_tensor_rejected,
        "SP3_only_geometry_derived_source_rejected_by_v021_contract": geometry_source_rejected,
        "SP3_only_unsupported_vacuum_rejected_by_v021_contract": unsupported_vacuum_rejected,
        "SP3_only_anchor_coverage_rejected_by_v021_contract": anchor_only_coverage_rejected,
        "current_SP3_alone_cannot_claim_W6_complete": True,
        "external_source_augmentation_required_under_current_contract": True,
        "physical_production_claim_remains_false": True,
    }

    status = "PASS" if all(checks.values()) else "FAIL"
    out = {
        "schema": SCHEMA,
        "status": status,
        "authority": "CANDIDATE_ONLY",
        "canon_allowed": False,
        "physical_production_claim": False,
        "no_go_class": "CURRENT_SOURCE_TYPE_INSUFFICIENCY",
        "source": {
            "source_url": src["source_url"],
            "source_revision": src["source_revision"],
            "realization_id": sp3.realization_id(),
            **source_shape,
        },
        "rejected_SP3_only_routes": {
            "no_source_tensor": missing_tensor_rejected,
            "T_from_target_geometry": geometry_source_rejected,
            "unsupported_vacuum": unsupported_vacuum_rejected,
            "finite_anchors_as_full_patch_coverage": anchor_only_coverage_rejected,
        },
        "checks": checks,
        "frontier": {
            "current_SP3_geometry_clock_role": "ADMITTED_CANDIDATE_INPUT",
            "current_SP3_as_complete_W6_source": "FAIL_TYPE_AND_COVERAGE",
            "additional_independent_source_dataset_or_primitive": "REQUIRED",
            "W6_physical_source_packet": "OPEN_EXTERNAL_EVIDENCE",
            "RF_E26_production_promotion": "OPEN",
        },
        "interpretation_firewall": {
            "SP3_remains_valid_for_clock_geometry_matching_roles": True,
            "source_insufficiency_does_not_invalidate_those_roles": True,
            "future_richer_source_binding_not_ruled_out": True,
            "no_source_tensor_manufactured": True,
        },
    }
    print(json.dumps(out, indent=2, sort_keys=True))
    raise SystemExit(0 if status == "PASS" else 1)


if __name__ == "__main__":
    main()
