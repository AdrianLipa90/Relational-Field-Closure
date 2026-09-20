from __future__ import annotations

import copy
import hashlib
import json
import math
from typing import Any, Mapping, Sequence

SCHEMA = "RF_GSC3F_SP3_PHYSICAL_PRODUCT_DOMAIN_BINDING_VALIDATION_V0_22"
PACKET_SCHEMA = "RF_GSC3F_SP3_PHYSICAL_PRODUCT_DOMAIN_BINDING_PACKET_V0_22"

DOMAIN = "SP3_STATIONARY_PRODUCT_DOMAIN_V0_18_V0_19"
PATCHES = ("SP3_STEREO_N", "SP3_STEREO_S")


class PhysicalDomainBindingError(ValueError):
    pass


def _text(value: Any, label: str) -> str:
    out = str(value).strip()
    if not out:
        raise PhysicalDomainBindingError(f"{label} must be nonempty")
    return out


def _finite(value: Any, label: str) -> float:
    out = float(value)
    if not math.isfinite(out):
        raise PhysicalDomainBindingError(f"{label} must be finite")
    return out


def _digest(value: Any, label: str) -> str:
    out = _text(value, label).lower()
    if len(out) != 64 or any(ch not in "0123456789abcdef" for ch in out):
        raise PhysicalDomainBindingError(f"{label} must be sha256 hex")
    return out


def validate_packet(packet: Mapping[str, Any]) -> dict[str, Any]:
    if packet.get("schema") != PACKET_SCHEMA:
        raise PhysicalDomainBindingError("schema mismatch")

    rid = _text(packet.get("physical_realization_id"), "physical_realization_id")
    clock_id = _text(packet.get("clock_id"), "clock_id")
    if _text(packet.get("candidate_domain_id"), "candidate_domain_id") != DOMAIN:
        raise PhysicalDomainBindingError("candidate domain mismatch")
    _text(packet.get("production_spatial_realization_id"), "production_spatial_realization_id")
    _text(packet.get("production_event_complex_id"), "production_event_complex_id")

    refs = packet.get("source_receipt_refs")
    if not isinstance(refs, Sequence) or isinstance(refs, (str, bytes)) or len(refs) < 4:
        raise PhysicalDomainBindingError("source_receipt_refs must contain at least four bound source receipts")
    roles = set()
    for i, ref in enumerate(refs):
        if not isinstance(ref, Mapping):
            raise PhysicalDomainBindingError("source receipt ref must be an object")
        role = _text(ref.get("role"), f"source_receipt_refs[{i}].role")
        roles.add(role)
        _text(ref.get("receipt_id"), f"source_receipt_refs[{i}].receipt_id")
        _digest(ref.get("digest"), f"source_receipt_refs[{i}].digest")
        if _text(ref.get("physical_realization_id"), f"source_receipt_refs[{i}].physical_realization_id") != rid:
            raise PhysicalDomainBindingError("source receipt realization mismatch")
    required_roles = {"IDT_CLOCK", "TIR_SPATIAL", "RFC_ATLAS", "W6_SOURCE"}
    if not required_roles.issubset(roles):
        raise PhysicalDomainBindingError("required source receipt roles missing")

    spatial = packet.get("spatial_carrier_binding")
    if not isinstance(spatial, Mapping):
        raise PhysicalDomainBindingError("spatial_carrier_binding must be an object")
    for key in ("source_spatial_domain_id", "map_kind", "map_receipt_id"):
        _text(spatial.get(key), f"spatial_carrier_binding.{key}")
    if _text(
        spatial.get("target_candidate_spatial_domain_id"),
        "spatial_carrier_binding.target_candidate_spatial_domain_id",
    ) != DOMAIN:
        raise PhysicalDomainBindingError("spatial target domain mismatch")
    _digest(
        spatial.get("implementation_or_payload_digest"),
        "spatial_carrier_binding.implementation_or_payload_digest",
    )
    for key in (
        "orientation_preserving",
        "rank_three_everywhere_on_declared_domain",
        "injective_on_declared_domain",
        "surjective_onto_declared_target_domain",
        "coverage_certified",
        "source_owned",
    ):
        if spatial.get(key) is not True:
            raise PhysicalDomainBindingError(f"spatial carrier binding requires {key}=true")
    if spatial.get("binding_scope") != "FULL_DECLARED_SPATIAL_DOMAIN":
        raise PhysicalDomainBindingError("finite anchor-only spatial binding is insufficient")

    placement = packet.get("event_placement_binding")
    if not isinstance(placement, Mapping):
        raise PhysicalDomainBindingError("event_placement_binding must be an object")
    offset = _finite(placement.get("common_clock_offset"), "event_placement_binding.common_clock_offset")
    tol = abs(_finite(placement.get("temporal_tolerance"), "event_placement_binding.temporal_tolerance"))
    if placement.get("event_set_coverage_exact") is not True:
        raise PhysicalDomainBindingError("event set coverage must be exact")
    if placement.get("spatial_binding_resolves_through_Phi_Sigma") is not True:
        raise PhysicalDomainBindingError("event spatial binding must resolve through spatial carrier map")
    if placement.get("no_event_outside_candidate_domain") is not True:
        raise PhysicalDomainBindingError("event placement leaves candidate domain")
    if placement.get("source_owned") is not True:
        raise PhysicalDomainBindingError("event placement must be source-owned")
    events = placement.get("events")
    if not isinstance(events, Sequence) or isinstance(events, (str, bytes)) or not events:
        raise PhysicalDomainBindingError("placed event set must be nonempty")
    event_ids = set()
    for i, event in enumerate(events):
        if not isinstance(event, Mapping):
            raise PhysicalDomainBindingError("event placement record must be an object")
        eid = _text(event.get("event_id"), f"events[{i}].event_id")
        if eid in event_ids:
            raise PhysicalDomainBindingError("duplicate event_id")
        event_ids.add(eid)
        clock_value = _finite(event.get("clock_value"), f"events[{i}].clock_value")
        candidate_time = _finite(event.get("candidate_time_value"), f"events[{i}].candidate_time_value")
        if abs((candidate_time - clock_value) - offset) > tol:
            raise PhysicalDomainBindingError("event clock offset mismatch")
        _text(event.get("spatial_source_anchor_id"), f"events[{i}].spatial_source_anchor_id")
        _text(event.get("candidate_spatial_coordinate_or_ref"), f"events[{i}].candidate_spatial_coordinate_or_ref")
        patches = event.get("atlas_patch_ids")
        if not isinstance(patches, Sequence) or isinstance(patches, (str, bytes)) or not patches:
            raise PhysicalDomainBindingError("event must resolve to at least one atlas patch")
        if not set(patches).issubset(set(PATCHES)):
            raise PhysicalDomainBindingError("event references foreign atlas patch")
        _digest(event.get("placement_digest"), f"events[{i}].placement_digest")

    atlas = packet.get("atlas_domain_binding")
    if not isinstance(atlas, Mapping):
        raise PhysicalDomainBindingError("atlas_domain_binding must be an object")
    if _text(atlas.get("physical_realization_id"), "atlas_domain_binding.physical_realization_id") != rid:
        raise PhysicalDomainBindingError("atlas realization mismatch")
    if _text(atlas.get("candidate_domain_id"), "atlas_domain_binding.candidate_domain_id") != DOMAIN:
        raise PhysicalDomainBindingError("atlas candidate domain mismatch")
    patch_ids = atlas.get("atlas_patch_ids")
    if not isinstance(patch_ids, Sequence) or set(patch_ids) != set(PATCHES):
        raise PhysicalDomainBindingError("atlas patch set mismatch")
    for key in ("spatial_binding_receipt_id", "event_placement_receipt_id", "coverage_receipt_id"):
        _text(atlas.get(key), f"atlas_domain_binding.{key}")
    if atlas.get("full_bound_domain_coverage_certified") is not True:
        raise PhysicalDomainBindingError("atlas does not certify full physically bound domain coverage")

    w6 = packet.get("w6_domain_binding")
    if not isinstance(w6, Mapping):
        raise PhysicalDomainBindingError("w6_domain_binding must be an object")
    if _text(w6.get("physical_realization_id"), "w6_domain_binding.physical_realization_id") != rid:
        raise PhysicalDomainBindingError("W6 realization mismatch")
    if _text(w6.get("candidate_domain_id"), "w6_domain_binding.candidate_domain_id") != DOMAIN:
        raise PhysicalDomainBindingError("W6 domain mismatch")
    if _text(w6.get("clock_id"), "w6_domain_binding.clock_id") != clock_id:
        raise PhysicalDomainBindingError("W6 clock mismatch")
    w6_patches = w6.get("atlas_patch_ids")
    if not isinstance(w6_patches, Sequence) or set(w6_patches) != set(PATCHES):
        raise PhysicalDomainBindingError("W6 patch set mismatch")
    for key in ("source_frame_id", "RF_E25_frame_id", "frame_transform_kind"):
        _text(w6.get(key), f"w6_domain_binding.{key}")
    _digest(
        w6.get("frame_transform_payload_or_callable_digest"),
        "w6_domain_binding.frame_transform_payload_or_callable_digest",
    )
    if w6.get("transform_invertible") is not True:
        raise PhysicalDomainBindingError("W6 frame transform must be invertible")
    if w6.get("tensor_pushforward_pullback_certified") is not True:
        raise PhysicalDomainBindingError("W6 tensor frame transformation must be certified")
    if w6.get("source_field_coverage_full_bound_domain") is not True:
        raise PhysicalDomainBindingError("W6 source tensor does not cover the full physically bound domain")

    authority = packet.get("authority")
    if authority not in {"CANDIDATE_ONLY", "PRODUCTION_SOURCE_AUTHORITY"}:
        raise PhysicalDomainBindingError("unknown authority")
    if packet.get("canon_allowed") not in {True, False}:
        raise PhysicalDomainBindingError("canon_allowed must be boolean")
    if packet.get("physical_production_claim") not in {True, False}:
        raise PhysicalDomainBindingError("physical_production_claim must be boolean")

    production_admissible = bool(
        authority == "PRODUCTION_SOURCE_AUTHORITY"
        and packet.get("physical_production_claim") is True
    )

    return {
        "structurally_complete": True,
        "same_realization_bound": True,
        "same_clock_bound": True,
        "full_spatial_domain_binding": True,
        "event_placement_exact": True,
        "atlas_domain_bound": True,
        "w6_source_domain_and_frame_bound": True,
        "production_authority_present": authority == "PRODUCTION_SOURCE_AUTHORITY",
        "physical_product_realization_admissible_by_contract": production_admissible,
    }


def digest(label: str) -> str:
    return hashlib.sha256(label.encode("utf-8")).hexdigest()


def fixture() -> dict[str, Any]:
    rid = "FIXTURE_REALIZATION_NOT_EVIDENCE"
    clock = "FIXTURE_CLOCK_NOT_EVIDENCE"
    refs = [
        {
            "role": role,
            "receipt_id": f"fixture:{role}",
            "digest": digest(f"fixture:{role}"),
            "physical_realization_id": rid,
        }
        for role in ("IDT_CLOCK", "TIR_SPATIAL", "RFC_ATLAS", "W6_SOURCE")
    ]
    return {
        "schema": PACKET_SCHEMA,
        "physical_realization_id": rid,
        "clock_id": clock,
        "candidate_domain_id": DOMAIN,
        "production_spatial_realization_id": "FIXTURE_SPATIAL_NOT_EVIDENCE",
        "production_event_complex_id": "FIXTURE_EVENTS_NOT_EVIDENCE",
        "source_receipt_refs": refs,
        "spatial_carrier_binding": {
            "source_spatial_domain_id": "FIXTURE_SOURCE_SPATIAL_DOMAIN",
            "target_candidate_spatial_domain_id": DOMAIN,
            "map_kind": "TEST_DIFFEO_FIXTURE",
            "map_receipt_id": "fixture-spatial-map",
            "implementation_or_payload_digest": digest("fixture-spatial-map"),
            "orientation_preserving": True,
            "rank_three_everywhere_on_declared_domain": True,
            "injective_on_declared_domain": True,
            "surjective_onto_declared_target_domain": True,
            "coverage_certified": True,
            "source_owned": True,
            "binding_scope": "FULL_DECLARED_SPATIAL_DOMAIN",
        },
        "event_placement_binding": {
            "common_clock_offset": 5.0,
            "temporal_tolerance": 1e-12,
            "event_set_coverage_exact": True,
            "spatial_binding_resolves_through_Phi_Sigma": True,
            "no_event_outside_candidate_domain": True,
            "source_owned": True,
            "events": [
                {
                    "event_id": "E0",
                    "clock_value": 10.0,
                    "candidate_time_value": 15.0,
                    "spatial_source_anchor_id": "V0",
                    "candidate_spatial_coordinate_or_ref": "SP3_STEREO_N:x0",
                    "atlas_patch_ids": ["SP3_STEREO_N"],
                    "placement_digest": digest("E0-placement"),
                },
                {
                    "event_id": "E1",
                    "clock_value": 12.0,
                    "candidate_time_value": 17.0,
                    "spatial_source_anchor_id": "V1",
                    "candidate_spatial_coordinate_or_ref": "SP3_STEREO_S:x1",
                    "atlas_patch_ids": ["SP3_STEREO_S"],
                    "placement_digest": digest("E1-placement"),
                },
            ],
        },
        "atlas_domain_binding": {
            "physical_realization_id": rid,
            "candidate_domain_id": DOMAIN,
            "atlas_patch_ids": list(PATCHES),
            "spatial_binding_receipt_id": "fixture-spatial-map",
            "event_placement_receipt_id": "fixture-event-placement",
            "coverage_receipt_id": "fixture-atlas-coverage",
            "full_bound_domain_coverage_certified": True,
        },
        "w6_domain_binding": {
            "physical_realization_id": rid,
            "candidate_domain_id": DOMAIN,
            "clock_id": clock,
            "atlas_patch_ids": list(PATCHES),
            "source_frame_id": "FIXTURE_SOURCE_FRAME",
            "RF_E25_frame_id": "FIXTURE_RF_E25_FRAME",
            "frame_transform_kind": "TEST_LINEAR_ISOMORPHISM",
            "frame_transform_payload_or_callable_digest": digest("fixture-frame-transform"),
            "transform_invertible": True,
            "tensor_pushforward_pullback_certified": True,
            "source_field_coverage_full_bound_domain": True,
        },
        "authority": "CANDIDATE_ONLY",
        "canon_allowed": False,
        "physical_production_claim": False,
    }


def reject(packet: Mapping[str, Any]) -> bool:
    try:
        validate_packet(packet)
    except PhysicalDomainBindingError:
        return True
    return False


def main():
    good = fixture()
    good_result = validate_packet(good)

    id_only = copy.deepcopy(good)
    id_only["spatial_carrier_binding"]["coverage_certified"] = False

    anchors_only = copy.deepcopy(good)
    anchors_only["spatial_carrier_binding"]["binding_scope"] = "FIVE_SOURCE_ANCHORS_ONLY"

    bad_offset = copy.deepcopy(good)
    bad_offset["event_placement_binding"]["events"][1]["candidate_time_value"] = 18.0

    foreign_w6 = copy.deepcopy(good)
    foreign_w6["w6_domain_binding"]["candidate_domain_id"] = "UNRELATED_DOMAIN"

    no_transform = copy.deepcopy(good)
    no_transform["w6_domain_binding"]["frame_transform_payload_or_callable_digest"] = ""

    mixed_realization = copy.deepcopy(good)
    mixed_realization["source_receipt_refs"][2]["physical_realization_id"] = "OTHER_REALIZATION"

    production_spoof = copy.deepcopy(good)
    production_spoof["physical_production_claim"] = True
    production_spoof_result = validate_packet(production_spoof)

    checks = {
        "structurally_complete_fixture_passes_schema": good_result["structurally_complete"],
        "candidate_fixture_does_not_gain_physical_product_admission": not good_result[
            "physical_product_realization_admissible_by_contract"
        ],
        "identifier_only_without_domain_coverage_rejected": reject(id_only),
        "five_anchor_only_binding_rejected": reject(anchors_only),
        "inconsistent_event_clock_offset_rejected": reject(bad_offset),
        "W6_source_on_foreign_domain_rejected": reject(foreign_w6),
        "missing_source_to_RF_E25_frame_transform_rejected": reject(no_transform),
        "mixed_realization_receipts_rejected": reject(mixed_realization),
        "candidate_authority_cannot_self_promote_physical_product_claim": not production_spoof_result[
            "physical_product_realization_admissible_by_contract"
        ],
        "contract_does_not_supply_real_physical_product_binding": True,
    }

    status = "PASS" if all(checks.values()) else "FAIL"
    out = {
        "schema": SCHEMA,
        "status": status,
        "authority": "CANDIDATE_ONLY",
        "canon_allowed": False,
        "physical_production_claim": False,
        "contract_class": "FAIL_CLOSED_PHYSICAL_PRODUCT_REALIZATION_SCHEMA",
        "candidate_domain_id": DOMAIN,
        "required_patch_ids": list(PATCHES),
        "checks": checks,
        "frontier": {
            "physical_product_realization_event_placement_binding": "OPEN_EXTERNAL_SOURCE_EVIDENCE",
            "W6_physical_source_receipts": "OPEN_EXTERNAL_SOURCE_EVIDENCE",
            "RF_E26_production_promotion": "OPEN",
        },
        "corrected_production_frontier": [
            "PHYSICAL_PRODUCT_REALIZATION_EVENT_PLACEMENT_BINDING",
            "W6_INDEPENDENT_PHYSICAL_SOURCE_RECEIPTS",
        ],
        "interpretation_firewall": {
            "same_identifier_is_not_same_physical_domain_proof": True,
            "finite_source_anchors_are_not_full_domain_binding": True,
            "candidate_carrier_is_not_self_promoted_to_physical_spacetime": True,
        },
    }
    print(json.dumps(out, indent=2, sort_keys=True))
    raise SystemExit(0 if status == "PASS" else 1)


if __name__ == "__main__":
    main()
