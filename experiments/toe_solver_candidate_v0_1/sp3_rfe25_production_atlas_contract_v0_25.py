from __future__ import annotations

import copy
import hashlib
import json
import math
from pathlib import Path
from typing import Any, Mapping, Sequence

ROOT = Path(__file__).resolve().parents[2]
R019 = ROOT / "validation" / "toe_solver_candidate_v0_1" / "SP3_STEREOGRAPHIC_RFE25_ATLAS_V0_19.json"

SCHEMA = "QHTRI_TOE_SP3_RF_E25_PRODUCTION_ATLAS_CONTRACT_VALIDATION_V0_25"
PACKET_SCHEMA = "RF_GSC4D_SP3_RF_E25_PRODUCTION_ATLAS_PACKET_V0_25"
PATCHES = ("SP3_STEREO_N", "SP3_STEREO_S")
OVERLAPS = (("SP3_STEREO_N","SP3_STEREO_S"),("SP3_STEREO_S","SP3_STEREO_N"))
DOMAIN = "SP3_STATIONARY_PRODUCT_DOMAIN_V0_18_V0_19"

class AtlasContractError(ValueError):
    pass

def digest(label: str) -> str:
    return hashlib.sha256(label.encode("utf-8")).hexdigest()

def nonempty(v: Any, label: str) -> str:
    s=str(v).strip()
    if not s:
        raise AtlasContractError(f"{label} must be nonempty")
    return s

def sha(v: Any, label: str) -> str:
    s=nonempty(v,label).lower()
    if len(s)!=64 or any(c not in "0123456789abcdef" for c in s):
        raise AtlasContractError(f"{label} must be sha256")
    return s

def validate_temporal_coverage(tc: Mapping[str,Any]) -> dict[str,Any]:
    kind=nonempty(tc.get("kind"),"temporal_coverage.kind")
    coverage_id=nonempty(tc.get("coverage_id"),"temporal_coverage.coverage_id")
    if kind=="OBSERVED_PHYSICAL_WINDOW":
        nonempty(tc.get("start"),"temporal_coverage.start")
        nonempty(tc.get("end"),"temporal_coverage.end")
        return {"coverage_id":coverage_id,"kind":kind,"production_temporal_ok":True}
    if kind=="INDEPENDENTLY_VALIDATED_PHYSICAL_MODEL_EXTENSION":
        nonempty(tc.get("model_extension_receipt_id"),"temporal_coverage.model_extension_receipt_id")
        sha(tc.get("model_extension_digest"),"temporal_coverage.model_extension_digest")
        nonempty(tc.get("validation_domain"),"temporal_coverage.validation_domain")
        obs=tc.get("validation_observations")
        if not isinstance(obs,Sequence) or isinstance(obs,(str,bytes)) or not obs:
            raise AtlasContractError("model extension requires validation observations")
        if tc.get("independent_validation") is not True:
            raise AtlasContractError("model extension requires independent validation")
        return {"coverage_id":coverage_id,"kind":kind,"production_temporal_ok":True}
    if kind=="SOURCE_DERIVED_STATIONARY_MATHEMATICAL_EXTENSION":
        return {"coverage_id":coverage_id,"kind":kind,"production_temporal_ok":False}
    raise AtlasContractError("unknown temporal coverage kind")

def validate_patch(p: Mapping[str,Any], realization: str, metric_lineage: str, coverage_id: str):
    patch_id=nonempty(p.get("patch_id"),"patch_id")
    if patch_id not in PATCHES:
        raise AtlasContractError("foreign patch id")
    if nonempty(p.get("physical_realization_id"),"physical_realization_id") != realization:
        raise AtlasContractError("patch physical realization mismatch")
    if nonempty(p.get("metric_lineage_id"),"metric_lineage_id") != metric_lineage:
        raise AtlasContractError("patch metric lineage mismatch")
    if nonempty(p.get("coverage_domain_id"),"coverage_domain_id") != DOMAIN:
        raise AtlasContractError("patch coverage domain mismatch")
    if nonempty(p.get("coverage_patch_id"),"coverage_patch_id") != patch_id:
        raise AtlasContractError("patch coverage patch mismatch")
    if p.get("spatial_coverage_certified") is not True:
        raise AtlasContractError("full patch spatial coverage required")
    if nonempty(p.get("temporal_coverage_id"),"temporal_coverage_id") != coverage_id:
        raise AtlasContractError("patch temporal coverage id mismatch")
    for key in ("lapse_provider_digest","triad_provider_digest","shift_provider_digest"):
        sha(p.get(key),key)
    nonempty(p.get("field_construction_receipt_id"),"field_construction_receipt_id")
    refs=p.get("immutable_source_refs")
    if not isinstance(refs,Sequence) or isinstance(refs,(str,bytes)) or not refs:
        raise AtlasContractError("immutable source refs required")
    for i,ref in enumerate(refs):
        if not isinstance(ref,Mapping):
            raise AtlasContractError("immutable source ref must be object")
        nonempty(ref.get("ref"),f"immutable_source_refs[{i}].ref")
        sha(ref.get("digest"),f"immutable_source_refs[{i}].digest")
    for key in ("positive_lapse_certified","invertible_triad_certified","Lorentz_signature_certified"):
        if p.get(key) is not True:
            raise AtlasContractError(f"{key} must be true")
    return patch_id

def validate_overlap(o: Mapping[str,Any], realization: str, metric_lineage: str):
    source=nonempty(o.get("source_patch_id"),"source_patch_id")
    target=nonempty(o.get("target_patch_id"),"target_patch_id")
    if (source,target) not in OVERLAPS:
        raise AtlasContractError("unexpected overlap direction")
    if nonempty(o.get("physical_realization_id"),"physical_realization_id") != realization:
        raise AtlasContractError("overlap realization mismatch")
    if nonempty(o.get("metric_lineage_id"),"metric_lineage_id") != metric_lineage:
        raise AtlasContractError("overlap metric lineage mismatch")
    nonempty(o.get("overlap_domain_id"),"overlap_domain_id")
    if o.get("full_overlap_coverage_certified") is not True:
        raise AtlasContractError("full overlap coverage required")
    for key in ("coordinate_jacobian_provider_digest","Lorentz_transition_provider_digest","validation_digest"):
        sha(o.get(key),key)
    nonempty(o.get("validation_receipt_id"),"validation_receipt_id")
    for key in ("orientation_preserving_certified","proper_orthochronous_certified","coframe_overlap_certified","metric_overlap_certified"):
        if o.get(key) is not True:
            raise AtlasContractError(f"{key} must be true")
    return (source,target)

def validate_packet(packet: Mapping[str,Any]) -> dict[str,Any]:
    if packet.get("schema")!=PACKET_SCHEMA:
        raise AtlasContractError("unexpected packet schema")
    realization=nonempty(packet.get("physical_realization_id"),"physical_realization_id")
    metric_lineage=nonempty(packet.get("metric_lineage_id"),"metric_lineage_id")
    if nonempty(packet.get("atlas_domain_id"),"atlas_domain_id") != DOMAIN:
        raise AtlasContractError("atlas domain mismatch")
    nonempty(packet.get("source_bundle_receipt_id"),"source_bundle_receipt_id")
    sha(packet.get("source_bundle_receipt_digest"),"source_bundle_receipt_digest")
    tc=validate_temporal_coverage(packet.get("temporal_coverage",{}))
    patches=packet.get("patch_field_receipts")
    if not isinstance(patches,Sequence) or isinstance(patches,(str,bytes)):
        raise AtlasContractError("patch_field_receipts must be sequence")
    patch_ids=[validate_patch(p,realization,metric_lineage,tc["coverage_id"]) for p in patches]
    if len(patch_ids)!=len(set(patch_ids)) or set(patch_ids)!=set(PATCHES):
        raise AtlasContractError("patch set must equal admitted two-chart atlas exactly")
    overlaps=packet.get("overlap_receipts")
    if not isinstance(overlaps,Sequence) or isinstance(overlaps,(str,bytes)):
        raise AtlasContractError("overlap_receipts must be sequence")
    dirs=[validate_overlap(o,realization,metric_lineage) for o in overlaps]
    if len(dirs)!=len(set(dirs)) or set(dirs)!=set(OVERLAPS):
        raise AtlasContractError("both directed full overlaps are required")
    authority=nonempty(packet.get("authority"),"authority")
    if authority not in {"CANDIDATE_ONLY","PRODUCTION_SOURCE_AUTHORITY"}:
        raise AtlasContractError("unknown authority")
    if packet.get("physical_production_claim") not in {True,False}:
        raise AtlasContractError("physical_production_claim must be boolean")
    production=(
        authority=="PRODUCTION_SOURCE_AUTHORITY"
        and packet.get("physical_production_claim") is True
        and tc["production_temporal_ok"]
    )
    return {
        "exact_patch_set":True,
        "both_directed_overlaps":True,
        "full_spatial_coverage":True,
        "temporal_coverage_kind":tc["kind"],
        "production_temporal_coverage_ok":tc["production_temporal_ok"],
        "production_authority_present":authority=="PRODUCTION_SOURCE_AUTHORITY",
        "RF_E25_production_admissible_by_contract":bool(production),
    }

def fixture_patch(patch_id: str, realization: str, metric_lineage: str, coverage_id: str):
    return {
        "patch_id":patch_id,
        "physical_realization_id":realization,
        "metric_lineage_id":metric_lineage,
        "coverage_domain_id":DOMAIN,
        "coverage_patch_id":patch_id,
        "spatial_coverage_certified":True,
        "temporal_coverage_id":coverage_id,
        "lapse_provider_digest":digest("lapse:"+patch_id),
        "triad_provider_digest":digest("triad:"+patch_id),
        "shift_provider_digest":digest("shift:"+patch_id),
        "field_construction_receipt_id":"fixture-field:"+patch_id,
        "immutable_source_refs":[{"ref":"fixture://"+patch_id,"digest":digest("ref:"+patch_id)}],
        "positive_lapse_certified":True,
        "invertible_triad_certified":True,
        "Lorentz_signature_certified":True,
    }

def fixture_overlap(a: str,b: str,realization: str,metric_lineage: str):
    return {
        "source_patch_id":a,"target_patch_id":b,
        "physical_realization_id":realization,
        "metric_lineage_id":metric_lineage,
        "overlap_domain_id":"fixture-overlap:"+a+":"+b,
        "full_overlap_coverage_certified":True,
        "coordinate_jacobian_provider_digest":digest("J:"+a+":"+b),
        "Lorentz_transition_provider_digest":digest("L:"+a+":"+b),
        "orientation_preserving_certified":True,
        "proper_orthochronous_certified":True,
        "coframe_overlap_certified":True,
        "metric_overlap_certified":True,
        "validation_receipt_id":"fixture-overlap-validation:"+a+":"+b,
        "validation_digest":digest("validation:"+a+":"+b),
    }

def fixture_packet():
    realization="FIXTURE_REALIZATION_NOT_EVIDENCE"
    lineage="FIXTURE_METRIC_LINEAGE_NOT_EVIDENCE"
    coverage_id="FIXTURE_OBSERVED_WINDOW"
    return {
        "schema":PACKET_SCHEMA,
        "physical_realization_id":realization,
        "metric_lineage_id":lineage,
        "atlas_domain_id":DOMAIN,
        "source_bundle_receipt_id":"fixture-source-bundle",
        "source_bundle_receipt_digest":digest("fixture-source-bundle"),
        "temporal_coverage":{
            "kind":"OBSERVED_PHYSICAL_WINDOW",
            "coverage_id":coverage_id,
            "start":"fixture-start","end":"fixture-end",
        },
        "patch_field_receipts":[fixture_patch(p,realization,lineage,coverage_id) for p in PATCHES],
        "overlap_receipts":[fixture_overlap(a,b,realization,lineage) for a,b in OVERLAPS],
        "authority":"CANDIDATE_ONLY",
        "canon_allowed":False,
        "physical_production_claim":False,
    }

def rejected(packet):
    try:
        validate_packet(packet)
    except AtlasContractError:
        return True
    return False

def main():
    r19=json.loads(R019.read_text(encoding="utf-8"))
    good=fixture_packet()
    good_result=validate_packet(good)

    anchor_only=copy.deepcopy(good)
    anchor_only["patch_field_receipts"][0]["spatial_coverage_certified"]=False

    one_overlap=copy.deepcopy(good)
    one_overlap["overlap_receipts"]=one_overlap["overlap_receipts"][:1]

    stationary=copy.deepcopy(good)
    stationary["temporal_coverage"]={
        "kind":"SOURCE_DERIVED_STATIONARY_MATHEMATICAL_EXTENSION",
        "coverage_id":"STATIONARY_MODEL_ONLY",
    }
    for p in stationary["patch_field_receipts"]:
        p["temporal_coverage_id"]="STATIONARY_MODEL_ONLY"
    stationary_result=validate_packet(stationary)

    invalid_model=copy.deepcopy(good)
    invalid_model["temporal_coverage"]={
        "kind":"INDEPENDENTLY_VALIDATED_PHYSICAL_MODEL_EXTENSION",
        "coverage_id":"MODEL_EXTENSION",
        "model_extension_receipt_id":"fixture-model",
        "model_extension_digest":digest("fixture-model"),
        "validation_domain":DOMAIN,
        "validation_observations":[],
        "independent_validation":False,
    }
    for p in invalid_model["patch_field_receipts"]:
        p["temporal_coverage_id"]="MODEL_EXTENSION"

    mismatch=copy.deepcopy(good)
    mismatch["patch_field_receipts"][1]["physical_realization_id"]="DIFFERENT_REALIZATION"

    spoof=copy.deepcopy(good)
    spoof["physical_production_claim"]=True
    spoof_result=validate_packet(spoof)

    checks={
        "parent_v019_PASS":r19.get("status")=="PASS",
        "parent_v019_RF_E25_production_input_still_open":r19.get("checks",{}).get("RF_E25_production_input_still_open") is True,
        "candidate_fixture_structurally_complete":good_result["exact_patch_set"] and good_result["both_directed_overlaps"],
        "candidate_fixture_does_not_gain_production_admission":not good_result["RF_E25_production_admissible_by_contract"],
        "anchor_only_spatial_coverage_rejected":rejected(anchor_only),
        "single_overlap_sample_rejected":rejected(one_overlap),
        "stationary_mathematical_extension_not_production_temporal_coverage":not stationary_result["RF_E25_production_admissible_by_contract"],
        "unvalidated_model_extension_rejected":rejected(invalid_model),
        "physical_realization_mismatch_rejected":rejected(mismatch),
        "candidate_authority_cannot_spoof_production_claim":not spoof_result["RF_E25_production_admissible_by_contract"],
        "actual_RF_E25_production_packet_remains_open":True,
        "physical_production_claim_remains_false":True,
    }
    status="PASS" if all(checks.values()) else "FAIL"
    out={
        "schema":SCHEMA,
        "status":status,
        "authority":"CANDIDATE_ONLY",
        "canon_allowed":False,
        "physical_production_claim":False,
        "contract_class":"FAIL_CLOSED_RF_E25_PRODUCTION_ATLAS_SCHEMA",
        "required_patch_ids":list(PATCHES),
        "required_overlap_directions":[list(x) for x in OVERLAPS],
        "atlas_domain_id":DOMAIN,
        "fixture_result":good_result,
        "checks":checks,
        "frontier":{
            "RF_E25_mathematical_atlas":"CLOSED_PARENT_V019",
            "RF_E25_executable_compatibility":"PASS_PARENT_V019",
            "RF_E25_production_metric_atlas_packet":"OPEN_EXTERNAL_OR_INDEPENDENTLY_VALIDATED_MODEL_EVIDENCE",
            "W6_physical_source_packet":"OPEN_SEPARATE_AXIS",
            "RF_E26_production_promotion":"OPEN",
        },
        "interpretation_firewall":{
            "finite_anchor_compatibility_is_not_full_patch_production_coverage":True,
            "stationary_mathematical_extension_is_not_physical_time_coverage":True,
            "candidate_authority_cannot_promote_production":True,
        },
    }
    print(json.dumps(out,indent=2,sort_keys=True))
    raise SystemExit(0 if status=="PASS" else 1)

if __name__=="__main__":
    main()
