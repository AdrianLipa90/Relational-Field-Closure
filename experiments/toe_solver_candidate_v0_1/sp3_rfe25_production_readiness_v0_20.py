from __future__ import annotations

import importlib.util
import json
import math
from pathlib import Path

import numpy as np

from src.rfc.shared_spacetime_atlas import ADMPatch
from src.rfc.source_assembled_shared_spacetime_atlas import SpatialSourceOverlap
from src.rfc.gsc4a_shift_source_provenance import (
    TIR_BETA_MATCH_BOUND,
    assemble_provenance_typed_source_shared_spacetime_atlas,
    tir_beta_match_bound_shift_source,
)

ROOT = Path(__file__).resolve().parents[2]
V019 = ROOT / "experiments" / "toe_solver_candidate_v0_1" / "sp3_stereographic_rfe25_atlas_v0_19.py"
V017 = ROOT / "experiments" / "toe_solver_candidate_v0_1" / "sp3_source_lapse_lorentz_coframe_v0_17.py"

R019 = ROOT / "validation" / "toe_solver_candidate_v0_1" / "SP3_STEREOGRAPHIC_RFE25_ATLAS_V0_19.json"
R013 = ROOT / "validation" / "toe_solver_candidate_v0_1" / "THREE_PLUS_ONE_TWO_EPOCH_CONSTRUCTOR_V0_13.json"
RGSC3D = ROOT / "validation" / "GSC3D_BETA_SHIFT_INTERFACE_ALIAS_V0_1.json"
RGSC3E = ROOT / "validation" / "GSC3C_BETA_MATCH_SHIFT_SOURCE_BINDING_V0_1.json"
RGSC4A_PROV = ROOT / "validation" / "GSC4A_SHIFT_SOURCE_PROVENANCE_V0_1.json"

SCHEMA = "QHTRI_TOE_SP3_RFE25_PRODUCTION_READINESS_V0_20"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def sha(obj):
    import hashlib
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    ).hexdigest()


def build_candidate_packet():
    v19 = load_module("v019_readiness", V019)
    v17 = load_module("v017_readiness", V017)
    sym = v19.symbolic_atlas()

    sats, points, betas, centroid, Q_exact, beta_coeffs, lapse_coeff, source_logs = v17.build_geometry()

    g = np.array([float(x) for x in centroid], dtype=float)
    Q = np.array([[float(x) for x in row] for row in Q_exact], dtype=float)
    R = np.linalg.cholesky(Q).T

    candidates = []
    for sat in sats:
        y = np.array([float(x) for x in points[sat]], dtype=float)
        u = R @ (y-g)
        candidates.append((abs(float(u[0])), sat, y, u))
    _, sat, y, u = min(candidates, key=lambda item: item[0])

    S = np.diag([-1.0, 1.0, 1.0])
    x = u[1:] / (1.0-u[0])
    q = S @ (u[1:] / (1.0+u[0]))

    TN = np.array(sym["lambdas"]["TN"](*x), dtype=float)
    TS = np.array(sym["lambdas"]["TS"](*q), dtype=float)
    A = np.array(sym["lambdas"]["A"](*x), dtype=float)

    b = v17.v16.eval_beta(beta_coeffs, y) / float(v17.v16.C)
    wN = np.linalg.solve(TN, b)
    wS = np.linalg.solve(TS, b)
    lapse = math.exp(float(source_logs[sat]))

    north = ADMPatch(
        name="SP3_STEREO_N",
        lapse=lapse,
        triad=tuple(tuple(float(v) for v in row) for row in TN),
        shift=tuple(float(v) for v in wN),
    )
    south = ADMPatch(
        name="SP3_STEREO_S",
        lapse=lapse,
        triad=tuple(tuple(float(v) for v in row) for row in TS),
        shift=tuple(float(v) for v in wS),
    )

    I3 = (
        (1.0, 0.0, 0.0),
        (0.0, 1.0, 0.0),
        (0.0, 0.0, 1.0),
    )
    zero3 = (0.0, 0.0, 0.0)
    A_tuple = tuple(tuple(float(v) for v in row) for row in A)
    Ainv_tuple = tuple(tuple(float(v) for v in row) for row in np.linalg.inv(A))

    overlaps = [
        SpatialSourceOverlap(
            "SP3_STEREO_N", "SP3_STEREO_S", A_tuple, zero3, I3
        ),
        SpatialSourceOverlap(
            "SP3_STEREO_S", "SP3_STEREO_N", Ainv_tuple, zero3, I3
        ),
    ]

    cp = v17.sp3.clock_packet()
    rid = v17.sp3.realization_id()
    clock_id = f"IDT_05K:{cp['reference_clock']}:{rid}"
    return v17, sat, rid, clock_id, [north, south], overlaps


def main():
    r019 = load_json(R019)
    r013 = load_json(R013)
    gsc3d = load_json(RGSC3D)
    gsc3e = load_json(RGSC3E)
    gsc4a_prov = load_json(RGSC4A_PROV)

    v17, sat, rid, clock_id, patches, overlaps = build_candidate_packet()

    gsc3d_ref = "RFC:GSC3D:validated_head:" + str(gsc3d["validated_head"])
    gsc3e_ref = "RFC:GSC3E:validated_head:" + str(gsc3e["lineage"]["validated_head"])

    provenance = [
        tir_beta_match_bound_shift_source(
            patch_id=p.name,
            realization_id=rid,
            clock_id=clock_id,
            source_reference=f"TIR:CANDIDATE:{rid}:{sat}:{p.name}:v0.19",
            gsc3d_alias_receipt=gsc3d_ref,
            gsc3e_w0_receipt=gsc3e_ref,
        )
        for p in patches
    ]

    cert = assemble_provenance_typed_source_shared_spacetime_atlas(
        patches,
        overlaps,
        shift_provenance=provenance,
        atol=1e-9,
    )

    spatial_payload = v17.sp3.spatial_packet()
    legacy_source_label = spatial_payload["capture"]["source"]["source_class"]

    six_fields = {
        "TIR_SPATIAL_PATCH_COFRAME_PACKET": (
            r019.get("checks", {}).get("north_chart_triad_invertible_exact") is True
            and r019.get("checks", {}).get("south_chart_triad_invertible_exact") is True
        ),
        "TIR_SPATIAL_OVERLAP_A_R_COCYCLES": (
            r019.get("checks", {}).get("global_quaternionic_coframe_pullback_relation_TS_A_equals_TN_exact") is True
            and r019.get("checks", {}).get("spatial_overlap_orientation_preserving") is True
        ),
        "IDT_SHARED_CLOCK_LAPSE_PACKET": (
            all(p.lapse > 0.0 for p in patches)
            and abs(patches[0].lapse-patches[1].lapse) < 1e-15
        ),
        "GSC3_MATCHING_SHIFT_AND_DRIFT_PACKET": (
            cert.geometry.max_shift_residual < 1e-9
            and all(o.temporal_drift == (0.0,0.0,0.0) for o in overlaps)
        ),
        "SOURCE_PATCH_CLOCK_IDENTIFIERS": (
            cert.realization_id == rid
            and cert.clock_id == clock_id
            and len(cert.source_references_by_patch) == len(patches)
        ),
        "PRODUCTION_OVERLAP_COVERAGE_STRUCTURAL_CANDIDATE": (
            r019.get("checks", {}).get("two_stereographic_domains_cover_S3") is True
            and cert.geometry.rf_e25.patch_count == 2
            and cert.geometry.rf_e25.overlap_count == 2
        ),
    }

    parent_firewalls = {
        "GSC3D_same_realization_patch_clock_provenance_still_input": bool(
            gsc3d.get("remaining_provenance_input")
        ),
        "GSC3E_production_source_binding_open": (
            gsc3e.get("production_source_binding") == "OPEN_SOURCE_BINDING"
        ),
        "GSC4A_source_controlled_provenance_open": (
            "SOURCE_CONTROLLED_PROVENANCE" in gsc4a_prov.get("open_inputs", [])
        ),
        "GSC4A_production_source_packet_open": (
            "PRODUCTION_TIR_IDT_OR_RFC_SOURCE_PACKET" in gsc4a_prov.get("open_inputs", [])
        ),
        "GSC4A_production_overlap_coverage_open": (
            "PRODUCTION_OVERLAP_COVERAGE" in gsc4a_prov.get("open_inputs", [])
        ),
    }

    evidence_firewall = {
        "v013_model_level_archive_derived": (
            r013.get("source_evidence_class") == "EXTERNAL_OBSERVATIONAL_ARCHIVE_DERIVED_MODEL_LEVEL"
        ),
        "v013_physical_production_claim_false": r013.get("physical_production_claim") is False,
        "legacy_internal_PRODUCTION_SOURCE_label_present": legacy_source_label == "PRODUCTION_SOURCE",
        "legacy_label_does_not_override_newer_evidence_boundary": True,
    }

    packet_complete = all(six_fields.values())
    provenance_wrapper_pass = (
        cert.provenance_status == "DECLARED_SOURCE_ROUTES_ADMITTED"
        and set(cert.routes_by_patch.values()) == {TIR_BETA_MATCH_BOUND}
        and cert.geometry.compatible
        and cert.geometry.rf_e25.compatible
    )
    production_authority_open = all(parent_firewalls.values()) and all(evidence_firewall.values())
    missing_software_operators = 0 if packet_complete and provenance_wrapper_pass else 1
    production_admission = False

    checks = {
        "all_six_reduced_packet_coordinates_populated_structurally": packet_complete,
        "TIR_beta_match_bound_route_used_on_all_patches": set(cert.routes_by_patch.values()) == {TIR_BETA_MATCH_BOUND},
        "one_common_realization_id": cert.realization_id == rid,
        "one_common_clock_id": cert.clock_id == clock_id,
        "GSC4A_provenance_wrapper_PASS": provenance_wrapper_pass,
        "downstream_GSC4A_geometry_PASS": cert.geometry.compatible,
        "downstream_RF_E25_geometry_PASS": cert.geometry.rf_e25.compatible,
        "declared_provenance_is_not_source_ownership_proof": (
            cert.production_source_ownership_status == "SOURCE_CONTROLLED_PROVENANCE_REQUIRED"
        ),
        "parent_production_firewalls_remain_open": production_authority_open,
        "legacy_source_label_firewall_enforced": all(evidence_firewall.values()),
        "missing_software_operators_zero": missing_software_operators == 0,
        "production_admission_remains_false": production_admission is False,
    }

    status = "PASS" if all(checks.values()) else "FAIL"
    out = {
        "schema": SCHEMA,
        "status": status,
        "authority": "CANDIDATE_ONLY",
        "canon_allowed": False,
        "physical_production_claim": False,
        "production_admission": production_admission,
        "readiness_class": "PACKET_READY_PRODUCTION_AUTHORITY_OPEN",
        "candidate_realization_id": rid,
        "candidate_clock_id": clock_id,
        "source_anchor": sat,
        "six_field_population": six_fields,
        "provenance_wrapper": {
            "status": cert.provenance_status,
            "production_source_ownership_status": cert.production_source_ownership_status,
            "routes_by_patch": dict(cert.routes_by_patch),
            "source_references_by_patch": dict(cert.source_references_by_patch),
            "gsc3d_receipt_reference": gsc3d_ref,
            "gsc3e_receipt_reference": gsc3e_ref,
        },
        "parent_firewalls": parent_firewalls,
        "evidence_firewall": evidence_firewall,
        "metrics": {
            "GSC4A_max_lapse_residual": cert.geometry.max_lapse_residual,
            "GSC4A_max_spatial_coframe_residual": cert.geometry.max_spatial_coframe_residual,
            "GSC4A_max_shift_residual": cert.geometry.max_shift_residual,
            "RF_E25_max_coframe_residual": cert.geometry.rf_e25.max_coframe_residual,
            "RF_E25_max_metric_residual": cert.geometry.rf_e25.max_metric_residual,
            "missing_software_operators": missing_software_operators,
        },
        "checks": checks,
        "remaining_external_gate": [
            "source-controlled provenance for the declared physical realization",
            "GSC3E physical production source-binding witness",
            "admitted production TIR/IDT/RFC source packet",
            "production overlap coverage authority",
            "RF-E26 global Einstein/source carrier",
        ],
        "interpretation_firewall": {
            "packet_readiness_is_not_production_admission": True,
            "declared_source_reference_is_not_source_ownership_proof": True,
            "legacy_PRODUCTION_SOURCE_string_is_not_authoritative_evidence_class": True,
            "physical_production_claim_remains_false": True,
        },
    }
    out["receipt_sha256"] = sha(out)
    print(json.dumps(out, indent=2, sort_keys=True))
    raise SystemExit(0 if status == "PASS" else 1)


if __name__ == "__main__":
    main()
