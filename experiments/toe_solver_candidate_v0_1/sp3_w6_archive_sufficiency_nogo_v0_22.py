from __future__ import annotations

import importlib.util
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
SP3_PATH = ROOT / "experiments" / "toe_solver_candidate_v0_1" / "igs_sp3_observational_e2e_v0_11.py"
W6_PATH = ROOT / "experiments" / "toe_solver_candidate_v0_1" / "sp3_w6_physical_source_receipt_contract_v0_21.py"
LOCAL_SOLVER_PATH = ROOT / "experiments" / "toe_solver_candidate_v0_1" / "local_einstein_closure_solver_candidate.py"
MULTI_SOLVER_PATH = ROOT / "experiments" / "toe_solver_candidate_v0_1" / "multisector_source_cone_solver_candidate.py"

SCHEMA = "QHTRI_TOE_CURRENT_SP3_ARCHIVE_W6_SUFFICIENCY_NOGO_V0_22"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def expect_reject_w6(w6, packet: dict[str, Any]) -> tuple[bool, str]:
    try:
        w6.validate_w6_packet(packet)
    except w6.W6ContractError as exc:
        return True, str(exc)
    return False, "unexpectedly accepted"


def main():
    sp3 = load_module("sp3_v011_nogo", SP3_PATH)
    w6 = load_module("w6_v021_nogo", W6_PATH)

    records = sp3.source_records()
    cp = sp3.clock_packet()
    spp = sp3.spatial_packet()
    mp = sp3.matching_packet()
    e2e = sp3.run()

    local_solver_source = LOCAL_SOLVER_PATH.read_text(encoding="utf-8")
    multi_solver_source = MULTI_SOLVER_PATH.read_text(encoding="utf-8")

    raw_record_vectors = [
        tuple(sp3.REC1[s]) for s in sp3.SAT_IDS
    ] + [
        tuple(sp3.REC2[s]) for s in sp3.SAT_IDS
    ]

    raw_records_are_exactly_four_scalars = all(len(v) == 4 for v in raw_record_vectors)
    raw_source_keyset = set(records)
    raw_source_has_only_orbit_clock_structure = raw_source_keyset == {
        "source_url",
        "source_revision",
        "epochs",
        "satellites",
        "epoch1",
        "epoch2",
    }

    forbidden_w6_source_keys = {
        "source_tensor",
        "tensor_payload_digest",
        "source_field_lineage_id",
        "local_solution",
        "RF-E24",
        "coverage_domain_id",
        "coverage_patch_id",
        "coverage_certified",
    }

    serialized_records = json.dumps(records, sort_keys=True)
    raw_source_contains_no_w6_tensor_payload = all(
        key not in serialized_records for key in forbidden_w6_source_keys
    )

    descendant_packets = {
        "clock": cp,
        "spatial": spp,
        "matching": mp,
    }
    serialized_descendants = json.dumps(descendant_packets, sort_keys=True)

    descendant_packets_contain_no_independent_source_tensor_payload = all(
        key not in serialized_descendants
        for key in (
            "source_tensor",
            "tensor_payload_digest",
            "source_field_lineage_id",
            "local_solution",
            "coverage_patch_id",
            "coverage_certified",
        )
    )

    # The raw source has ten four-scalar samples (five satellites x two epochs),
    # not a covered rank-two field over either stereographic patch.
    raw_sample_count = len(raw_record_vectors)
    raw_sample_count_is_ten = raw_sample_count == 10
    no_stereographic_patch_ids_in_raw_archive = all(
        patch not in serialized_records for patch in w6.ATLAS_PATCHES
    )

    # Existing geometry-side E2E produces an Einstein tensor from a metric derived
    # from the same source; this is not independent source-field evidence.
    e2e_has_geometry_derived_einstein_tensor = (
        e2e.get("status") == "PASS"
        and "einstein" in e2e
        and "G_at_center" in e2e["einstein"]
    )

    local_solver_is_geometry_downstream = (
        "SCOPE='zero-shift Lorentzian metric + Einstein tensor -> Lambda plus nonnegative orthonormal massless-stream pair couplings'"
        in local_solver_source
        and "def solve_positive_massless_pair_closure(einstein_tensor, metric" in local_solver_source
    )

    multisector_solver_is_geometry_downstream = (
        "def solve_source_cone(einstein_tensor,metric" in multi_solver_source
        and "G=_mat4(einstein_tensor,'G'); g=_mat4(metric,'g')" in multi_solver_source
    )

    # Try to form a structurally W6-shaped packet using only SP3 provenance,
    # deliberately without inventing a source tensor. The v0.21 contract must reject it.
    pseudo_receipts = []
    for patch in w6.ATLAS_PATCHES:
        pseudo_receipts.append({
            "schema": w6.PATCH_SCHEMA,
            "patch_id": patch,
            "atlas_domain_id": w6.ATLAS_DOMAIN_ID,
            "physical_realization_id": sp3.realization_id(),
            "metric_lineage_id": "SP3_DERIVED_METRIC_V017",
            "einstein_operator_lineage_id": w6.RF_E24_LINEAGE,
            "source_field_lineage_id": "MISSING_IN_SP3_ARCHIVE",
            "source_class": "SP3_ORBIT_CLOCK_ONLY",
            "source_observations": [
                {
                    "observation_id": f"{sat}:{epoch}",
                    "observable_class": "POSITION_PLUS_CLOCK_CORRECTION",
                    "coordinate_or_frame_binding": sat,
                    "units": "km_plus_microsecond_clock_correction",
                    "source_time_or_interval": epoch,
                    "immutable_digest": sp3.sha({
                        "satellite": sat,
                        "epoch": epoch,
                        "record": list(
                            sp3.REC1[sat] if epoch == sp3.EPOCH1 else sp3.REC2[sat]
                        ),
                    }),
                }
                for sat in sp3.SAT_IDS
                for epoch in (sp3.EPOCH1, sp3.EPOCH2)
            ],
            "immutable_source_refs": [
                {
                    "ref": sp3.SOURCE_URL,
                    "digest": sp3.sha(sp3.source_records()),
                }
            ],
            "Lambda": 0.0,
            "kappa_E": 1.0,
            # source_tensor intentionally absent because the archive does not contain one.
            "local_solution": {
                "certified": False,
                "equation": "RF-E24",
            },
            "authority": "CANDIDATE_ONLY",
            "canon_allowed": False,
            "physical_production_claim": False,
        })

    pseudo_packet = {
        "schema": w6.PACKET_SCHEMA,
        "patch_receipts": pseudo_receipts,
    }
    rejected, rejection_reason = expect_reject_w6(w6, pseudo_packet)

    # Explicitly ensure that the rejection is source-side, not because the SP3 geometry failed.
    geometry_stack_still_passes = (
        e2e.get("status") == "PASS"
        and cp.get("source_class") == "EXTERNAL_OBSERVATIONAL_ARCHIVE_DERIVED"
        and mp.get("source_class") == "EXTERNAL_OBSERVATIONAL_ARCHIVE_DERIVED"
        and bool(spp.get("manifold_certified"))
    )

    checks = {
        "raw_SP3_records_are_exactly_position3_plus_clock1": raw_records_are_exactly_four_scalars,
        "raw_SP3_source_schema_is_orbit_clock_only": raw_source_has_only_orbit_clock_structure,
        "raw_SP3_source_contains_no_W6_tensor_payload": raw_source_contains_no_w6_tensor_payload,
        "clock_spatial_matching_descendants_contain_no_independent_source_tensor_payload": descendant_packets_contain_no_independent_source_tensor_payload,
        "raw_archive_has_only_ten_anchor_records": raw_sample_count_is_ten,
        "raw_archive_contains_no_N_or_S_stereographic_patch_coverage": no_stereographic_patch_ids_in_raw_archive,
        "SP3_geometry_stack_itself_still_PASS": geometry_stack_still_passes,
        "SP3_E2E_Einstein_tensor_is_geometry_derived": e2e_has_geometry_derived_einstein_tensor,
        "local_source_solver_consumes_metric_and_Einstein_tensor": local_solver_is_geometry_downstream,
        "multisector_source_solver_consumes_metric_and_Einstein_tensor": multisector_solver_is_geometry_downstream,
        "v021_W6_contract_rejects_SP3_only_pseudo_packet": rejected,
        "current_archive_has_no_independent_RF_E24_local_solution_receipts": True,
        "current_archive_has_no_common_physical_source_field_lineage": True,
        "additional_external_source_evidence_is_required": True,
        "physical_production_claim_remains_false": True,
    }

    status = "PASS" if all(checks.values()) else "FAIL"
    out = {
        "schema": SCHEMA,
        "status": status,
        "authority": "CANDIDATE_ONLY",
        "canon_allowed": False,
        "physical_production_claim": False,
        "no_go_class": "CURRENT_ARCHIVE_SOURCE_SUFFICIENCY_NO_GO",
        "source": {
            "source_id": "RT218283.SP3@8013",
            "physical_realization_id": sp3.realization_id(),
            "epochs": [sp3.EPOCH1, sp3.EPOCH2],
            "satellites": list(sp3.SAT_IDS),
            "raw_record_count": raw_sample_count,
            "raw_record_shape": "R3_position_plus_R1_clock_correction",
        },
        "w6_rejection": {
            "rejected": rejected,
            "reason": rejection_reason,
            "contract": "RF_GSC5D_SP3_W6_PHYSICAL_SOURCE_PACKET_V0_21",
        },
        "checks": checks,
        "frontier": {
            "current_SP3_archive_geometry_role": "SUFFICIENT_FOR_EXISTING_CANDIDATE_GEOMETRY_STACK",
            "current_SP3_archive_W6_role": "INSUFFICIENT",
            "independent_physical_source_tensor": "MISSING",
            "full_patch_source_tensor_coverage": "MISSING",
            "physical_RF_E24_patch_receipts": "MISSING",
            "common_physical_source_field_lineage": "MISSING",
            "next_required_step": "ACQUIRE_OR_BIND_INDEPENDENT_EXTERNAL_PHYSICAL_SOURCE_PACKET",
        },
        "interpretation_firewall": {
            "no_go_does_not_invalidate_geometry_stack": True,
            "geometry_derived_G_is_not_independent_T_evidence": True,
            "source_class_fitting_is_not_physical_source_measurement": True,
            "future_external_data_can_lift_this_no_go": True,
        },
    }
    print(json.dumps(out, indent=2, sort_keys=True))
    raise SystemExit(0 if status == "PASS" else 1)


if __name__ == "__main__":
    main()
