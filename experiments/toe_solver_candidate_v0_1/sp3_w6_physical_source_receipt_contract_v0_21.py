from __future__ import annotations

import copy
import hashlib
import json
import math
from dataclasses import dataclass
from typing import Any, Mapping, Sequence

SCHEMA = "RF_GSC5D_SP3_W6_PHYSICAL_SOURCE_RECEIPT_CONTRACT_VALIDATION_V0_21"
PACKET_SCHEMA = "RF_GSC5D_SP3_W6_PHYSICAL_SOURCE_PACKET_V0_21"
PATCH_SCHEMA = "RF_GSC5D_SP3_W6_PATCH_RECEIPT_V0_21"

ATLAS_PATCHES = ("SP3_STEREO_N", "SP3_STEREO_S")
ATLAS_DOMAIN_ID = "SP3_STATIONARY_PRODUCT_DOMAIN_V0_18_V0_19"
RF_E24_LINEAGE = "RF-E24:EINSTEIN_OPERATOR"

FORBIDDEN_DERIVATIONS = {
    "T_FROM_G_ONLY",
    "T_FROM_METRIC_ONLY",
    "T_EQUALS_G_PLUS_LAMBDA_G_OVER_KAPPA",
    "GEOMETRIC_EFFECTIVE_STRESS_WITHOUT_INDEPENDENT_SOURCE",
    "SYNTHETIC_SOURCE_ONLY",
}


class W6ContractError(ValueError):
    pass


def _finite(value: Any, label: str) -> float:
    out = float(value)
    if not math.isfinite(out):
        raise W6ContractError(f"{label} must be finite")
    return out


def _nonempty(value: Any, label: str) -> str:
    out = str(value).strip()
    if not out:
        raise W6ContractError(f"{label} must be nonempty")
    return out


def _sha256_hex(value: Any, label: str) -> str:
    out = _nonempty(value, label)
    if len(out) != 64 or any(ch not in "0123456789abcdef" for ch in out.lower()):
        raise W6ContractError(f"{label} must be a sha256 hex digest")
    return out.lower()


def _validate_observation(obs: Mapping[str, Any], idx: int) -> None:
    prefix = f"source_observations[{idx}]"
    for key in (
        "observation_id",
        "observable_class",
        "coordinate_or_frame_binding",
        "units",
        "source_time_or_interval",
    ):
        _nonempty(obs.get(key), f"{prefix}.{key}")
    _sha256_hex(obs.get("immutable_digest"), f"{prefix}.immutable_digest")


def _validate_source_ref(ref: Mapping[str, Any], idx: int) -> None:
    prefix = f"immutable_source_refs[{idx}]"
    _nonempty(ref.get("ref"), f"{prefix}.ref")
    _sha256_hex(ref.get("digest"), f"{prefix}.digest")


def validate_patch_receipt(receipt: Mapping[str, Any]) -> dict[str, Any]:
    if receipt.get("schema") != PATCH_SCHEMA:
        raise W6ContractError("unexpected patch receipt schema")

    patch_id = _nonempty(receipt.get("patch_id"), "patch_id")
    if patch_id not in ATLAS_PATCHES:
        raise W6ContractError("patch_id is not in the admitted atlas patch set")

    if _nonempty(receipt.get("atlas_domain_id"), "atlas_domain_id") != ATLAS_DOMAIN_ID:
        raise W6ContractError("atlas_domain_id mismatch")

    physical_realization_id = _nonempty(
        receipt.get("physical_realization_id"), "physical_realization_id"
    )
    metric_lineage_id = _nonempty(receipt.get("metric_lineage_id"), "metric_lineage_id")
    operator_lineage = _nonempty(
        receipt.get("einstein_operator_lineage_id"), "einstein_operator_lineage_id"
    )
    if operator_lineage != RF_E24_LINEAGE:
        raise W6ContractError("Einstein operator lineage must be RF-E24")

    source_lineage = _nonempty(
        receipt.get("source_field_lineage_id"), "source_field_lineage_id"
    )
    source_class = _nonempty(receipt.get("source_class"), "source_class")

    observations = receipt.get("source_observations")
    if not isinstance(observations, Sequence) or isinstance(observations, (str, bytes)) or not observations:
        raise W6ContractError("source_observations must be a nonempty sequence")
    for idx, obs in enumerate(observations):
        if not isinstance(obs, Mapping):
            raise W6ContractError("source observation must be an object")
        _validate_observation(obs, idx)

    refs = receipt.get("immutable_source_refs")
    if not isinstance(refs, Sequence) or isinstance(refs, (str, bytes)) or not refs:
        raise W6ContractError("immutable_source_refs must be a nonempty sequence")
    for idx, ref in enumerate(refs):
        if not isinstance(ref, Mapping):
            raise W6ContractError("immutable source ref must be an object")
        _validate_source_ref(ref, idx)

    lam = _finite(receipt.get("Lambda"), "Lambda")
    kappa = _finite(receipt.get("kappa_E"), "kappa_E")
    if kappa <= 0.0:
        raise W6ContractError("kappa_E must be strictly positive")

    source_tensor = receipt.get("source_tensor")
    if not isinstance(source_tensor, Mapping):
        raise W6ContractError("source_tensor must be an object")
    if int(source_tensor.get("tensor_rank", -1)) != 2:
        raise W6ContractError("source tensor rank must be 2")
    if source_tensor.get("symmetry") != "symmetric":
        raise W6ContractError("source tensor must be symmetric")
    if source_tensor.get("covariance") != "covariant_2":
        raise W6ContractError("source tensor must be covariant rank two")
    _nonempty(source_tensor.get("units"), "source_tensor.units")
    _nonempty(source_tensor.get("representation_kind"), "source_tensor.representation_kind")
    tensor_digest = _sha256_hex(
        source_tensor.get("tensor_payload_digest"), "source_tensor.tensor_payload_digest"
    )
    _nonempty(
        source_tensor.get("construction_receipt_id"),
        "source_tensor.construction_receipt_id",
    )
    coverage_domain_id = _nonempty(
        source_tensor.get("coverage_domain_id"), "source_tensor.coverage_domain_id"
    )
    coverage_patch_id = _nonempty(
        source_tensor.get("coverage_patch_id"), "source_tensor.coverage_patch_id"
    )
    if coverage_domain_id != ATLAS_DOMAIN_ID:
        raise W6ContractError("source tensor coverage domain does not match atlas domain")
    if coverage_patch_id != patch_id:
        raise W6ContractError("source tensor coverage patch does not match patch receipt")
    if source_tensor.get("coverage_certified") is not True:
        raise W6ContractError("source tensor full-patch coverage must be certified")
    derivation = _nonempty(
        source_tensor.get("derivation_class"), "source_tensor.derivation_class"
    )
    if derivation in FORBIDDEN_DERIVATIONS:
        raise W6ContractError("source tensor derivation class is forbidden for physical W6")
    if source_tensor.get("independent_of_target_metric_construction") is not True:
        raise W6ContractError("source tensor independence firewall is not satisfied")

    if source_tensor.get("representation_kind") == "VACUUM_ZERO":
        vacuum = source_tensor.get("vacuum_domain_provenance")
        if not isinstance(vacuum, Mapping):
            raise W6ContractError("vacuum source requires independent vacuum-domain provenance")
        _nonempty(vacuum.get("domain_receipt_id"), "vacuum_domain_provenance.domain_receipt_id")
        _sha256_hex(vacuum.get("digest"), "vacuum_domain_provenance.digest")

    solution = receipt.get("local_solution")
    if not isinstance(solution, Mapping):
        raise W6ContractError("local_solution must be an object")
    if solution.get("certified") is not True:
        raise W6ContractError("local RF-E24 solution must be certified")
    if solution.get("equation") != "RF-E24":
        raise W6ContractError("local solution equation must be RF-E24")
    residual = abs(_finite(solution.get("residual_norm"), "local_solution.residual_norm"))
    tolerance = _finite(
        solution.get("residual_tolerance"), "local_solution.residual_tolerance"
    )
    if tolerance < 0.0 or residual > tolerance:
        raise W6ContractError("local Einstein residual exceeds declared tolerance")
    _nonempty(
        solution.get("residual_units_or_normalization"),
        "local_solution.residual_units_or_normalization",
    )
    _sha256_hex(
        solution.get("metric_representation_digest"),
        "local_solution.metric_representation_digest",
    )
    _sha256_hex(
        solution.get("einstein_tensor_representation_digest"),
        "local_solution.einstein_tensor_representation_digest",
    )
    solution_source_digest = _sha256_hex(
        solution.get("source_tensor_payload_digest"),
        "local_solution.source_tensor_payload_digest",
    )
    if solution_source_digest != tensor_digest:
        raise W6ContractError("source tensor digest mismatch between evidence and local solution")
    solution_coverage_domain = _nonempty(
        solution.get("source_tensor_coverage_domain_id"),
        "local_solution.source_tensor_coverage_domain_id",
    )
    solution_coverage_patch = _nonempty(
        solution.get("source_tensor_coverage_patch_id"),
        "local_solution.source_tensor_coverage_patch_id",
    )
    if solution_coverage_domain != coverage_domain_id:
        raise W6ContractError("local solution source coverage domain mismatch")
    if solution_coverage_patch != coverage_patch_id:
        raise W6ContractError("local solution source coverage patch mismatch")
    _nonempty(
        solution.get("validation_receipt_id"), "local_solution.validation_receipt_id"
    )
    _nonempty(
        solution.get("validation_head_or_artifact_digest"),
        "local_solution.validation_head_or_artifact_digest",
    )

    if receipt.get("authority") not in {"CANDIDATE_ONLY", "PRODUCTION_SOURCE_AUTHORITY"}:
        raise W6ContractError("unknown receipt authority")
    if receipt.get("canon_allowed") not in {True, False}:
        raise W6ContractError("canon_allowed must be boolean")
    if receipt.get("physical_production_claim") not in {True, False}:
        raise W6ContractError("physical_production_claim must be boolean")

    return {
        "patch_id": patch_id,
        "physical_realization_id": physical_realization_id,
        "metric_lineage_id": metric_lineage_id,
        "source_field_lineage_id": source_lineage,
        "source_class": source_class,
        "Lambda": lam,
        "kappa_E": kappa,
        "tensor_digest": tensor_digest,
        "authority": receipt.get("authority"),
        "physical_production_claim": bool(receipt.get("physical_production_claim")),
    }


def validate_w6_packet(packet: Mapping[str, Any]) -> dict[str, Any]:
    if packet.get("schema") != PACKET_SCHEMA:
        raise W6ContractError("unexpected W6 aggregate schema")
    receipts = packet.get("patch_receipts")
    if not isinstance(receipts, Sequence) or isinstance(receipts, (str, bytes)):
        raise W6ContractError("patch_receipts must be a sequence")

    normalized = [validate_patch_receipt(r) for r in receipts]
    ids = [r["patch_id"] for r in normalized]
    if len(ids) != len(set(ids)):
        raise W6ContractError("duplicate patch receipt")
    if set(ids) != set(ATLAS_PATCHES):
        raise W6ContractError("W6 patch receipt set must equal the atlas patch set exactly")

    for key in (
        "physical_realization_id",
        "source_field_lineage_id",
        "Lambda",
        "kappa_E",
    ):
        values = {r[key] for r in normalized}
        if len(values) != 1:
            raise W6ContractError(f"cross-patch {key} mismatch")

    operator = {_nonempty(r.get("einstein_operator_lineage_id"), "einstein_operator_lineage_id") for r in receipts}
    if operator != {RF_E24_LINEAGE}:
        raise W6ContractError("cross-patch Einstein operator lineage mismatch")

    production_authority = all(
        r["authority"] == "PRODUCTION_SOURCE_AUTHORITY" for r in normalized
    )
    production_claims = all(r["physical_production_claim"] for r in normalized)

    return {
        "schema_complete": True,
        "exact_atlas_patch_set_match": True,
        "common_physical_realization": True,
        "common_source_lineage": True,
        "common_constants": True,
        "all_patch_receipts_certified": True,
        "all_source_provenance_independent": True,
        "W6_structurally_complete": True,
        "production_authority_present": production_authority,
        "physical_production_claims_present": production_claims,
        "W6_production_admissible_by_contract": bool(
            production_authority and production_claims
        ),
    }


def digest(label: str) -> str:
    return hashlib.sha256(label.encode("utf-8")).hexdigest()


def fixture_patch(patch_id: str) -> dict[str, Any]:
    tensor_digest = digest(f"fixture-source-tensor:{patch_id}")
    return {
        "schema": PATCH_SCHEMA,
        "patch_id": patch_id,
        "atlas_domain_id": ATLAS_DOMAIN_ID,
        "physical_realization_id": "FIXTURE_REALIZATION_NOT_EVIDENCE",
        "metric_lineage_id": "FIXTURE_METRIC_LINEAGE_NOT_EVIDENCE",
        "einstein_operator_lineage_id": RF_E24_LINEAGE,
        "source_field_lineage_id": "FIXTURE_COMMON_SOURCE_NOT_EVIDENCE",
        "source_class": "TEST_FIXTURE_ONLY",
        "source_observations": [
            {
                "observation_id": f"fixture-observation:{patch_id}",
                "observable_class": "TEST_ONLY",
                "coordinate_or_frame_binding": patch_id,
                "units": "TEST_ONLY",
                "source_time_or_interval": "TEST_ONLY",
                "immutable_digest": digest(f"fixture-observation:{patch_id}"),
            }
        ],
        "immutable_source_refs": [
            {
                "ref": f"fixture://{patch_id}",
                "digest": digest(f"fixture-ref:{patch_id}"),
            }
        ],
        "Lambda": 0.0,
        "kappa_E": 1.0,
        "source_tensor": {
            "tensor_rank": 2,
            "symmetry": "symmetric",
            "covariance": "covariant_2",
            "units": "TEST_ONLY",
            "representation_kind": "INDEPENDENT_TEST_PACKET",
            "tensor_payload_digest": tensor_digest,
            "construction_receipt_id": f"fixture-source-construction:{patch_id}",
            "coverage_domain_id": ATLAS_DOMAIN_ID,
            "coverage_patch_id": patch_id,
            "coverage_certified": True,
            "derivation_class": "INDEPENDENT_TEST_FIXTURE",
            "independent_of_target_metric_construction": True,
        },
        "local_solution": {
            "certified": True,
            "equation": "RF-E24",
            "residual_norm": 0.0,
            "residual_tolerance": 1e-10,
            "residual_units_or_normalization": "TEST_ONLY",
            "metric_representation_digest": digest(f"fixture-metric:{patch_id}"),
            "einstein_tensor_representation_digest": digest(f"fixture-G:{patch_id}"),
            "source_tensor_payload_digest": tensor_digest,
            "source_tensor_coverage_domain_id": ATLAS_DOMAIN_ID,
            "source_tensor_coverage_patch_id": patch_id,
            "validation_receipt_id": f"fixture-local-solution:{patch_id}",
            "validation_head_or_artifact_digest": digest(
                f"fixture-local-validation:{patch_id}"
            ),
        },
        "authority": "CANDIDATE_ONLY",
        "canon_allowed": False,
        "physical_production_claim": False,
    }


def expect_reject(packet: Mapping[str, Any]) -> bool:
    try:
        validate_w6_packet(packet)
    except W6ContractError:
        return True
    return False


def main():
    good_fixture = {
        "schema": PACKET_SCHEMA,
        "patch_receipts": [fixture_patch(p) for p in ATLAS_PATCHES],
    }
    accepted_fixture = validate_w6_packet(good_fixture)

    missing = copy.deepcopy(good_fixture)
    missing["patch_receipts"] = missing["patch_receipts"][:1]

    forbidden = copy.deepcopy(good_fixture)
    forbidden["patch_receipts"][0]["source_tensor"][
        "derivation_class"
    ] = "T_EQUALS_G_PLUS_LAMBDA_G_OVER_KAPPA"

    lineage = copy.deepcopy(good_fixture)
    lineage["patch_receipts"][1]["source_field_lineage_id"] = "DIFFERENT_SOURCE"

    digest_mismatch = copy.deepcopy(good_fixture)
    digest_mismatch["patch_receipts"][0]["local_solution"][
        "source_tensor_payload_digest"
    ] = digest("wrong-source-digest")

    no_refs = copy.deepcopy(good_fixture)
    no_refs["patch_receipts"][0]["immutable_source_refs"] = []

    high_residual = copy.deepcopy(good_fixture)
    high_residual["patch_receipts"][0]["local_solution"]["residual_norm"] = 1e-3

    bad_coverage = copy.deepcopy(good_fixture)
    bad_coverage["patch_receipts"][0]["source_tensor"]["coverage_patch_id"] = "ANCHORS_ONLY_NOT_PATCH"

    vacuum_no_provenance = copy.deepcopy(good_fixture)
    vacuum_no_provenance["patch_receipts"][0]["source_tensor"][
        "representation_kind"
    ] = "VACUUM_ZERO"

    production_spoof = copy.deepcopy(good_fixture)
    for rec in production_spoof["patch_receipts"]:
        rec["physical_production_claim"] = True
        rec["authority"] = "CANDIDATE_ONLY"
    production_spoof_result = validate_w6_packet(production_spoof)

    checks = {
        "complete_two_patch_test_fixture_satisfies_schema": accepted_fixture[
            "W6_structurally_complete"
        ],
        "test_fixture_does_not_gain_production_admission": not accepted_fixture[
            "W6_production_admissible_by_contract"
        ],
        "missing_patch_rejected": expect_reject(missing),
        "geometry_derived_source_rejected": expect_reject(forbidden),
        "cross_patch_source_lineage_mismatch_rejected": expect_reject(lineage),
        "source_tensor_digest_mismatch_rejected": expect_reject(digest_mismatch),
        "missing_immutable_source_reference_rejected": expect_reject(no_refs),
        "residual_above_tolerance_rejected": expect_reject(high_residual),
        "incomplete_or_wrong_source_patch_coverage_rejected": expect_reject(bad_coverage),
        "vacuum_without_independent_domain_provenance_rejected": expect_reject(
            vacuum_no_provenance
        ),
        "candidate_authority_cannot_promote_physical_production_claim": not production_spoof_result[
            "W6_production_admissible_by_contract"
        ],
        "contract_does_not_supply_real_W6_evidence": True,
    }

    status = "PASS" if all(checks.values()) else "FAIL"
    out = {
        "schema": SCHEMA,
        "status": status,
        "authority": "CANDIDATE_ONLY",
        "canon_allowed": False,
        "physical_production_claim": False,
        "contract_class": "FAIL_CLOSED_SOURCE_EVIDENCE_SCHEMA",
        "required_patch_ids": list(ATLAS_PATCHES),
        "atlas_domain_id": ATLAS_DOMAIN_ID,
        "forbidden_source_derivations": sorted(FORBIDDEN_DERIVATIONS),
        "fixture_result": accepted_fixture,
        "checks": checks,
        "frontier": {
            "W6_receipt_schema": "DEFINED_AND_EXECUTABLE",
            "actual_physical_W6_source_packet": "OPEN_EXTERNAL_EVIDENCE",
            "RF_E26_production_promotion": "OPEN",
        },
        "interpretation_firewall": {
            "test_fixture_is_not_physical_source_evidence": True,
            "schema_PASS_is_not_W6_evidence_PASS": True,
            "geometry_only_effective_stress_is_rejected": True,
        },
    }
    print(json.dumps(out, indent=2, sort_keys=True))
    raise SystemExit(0 if status == "PASS" else 1)


if __name__ == "__main__":
    main()
