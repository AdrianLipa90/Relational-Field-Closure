from __future__ import annotations

import json
from pathlib import Path

from igs_sp3_observational_e2e_v0_12 import run

ROOT = Path(__file__).resolve().parents[2]
V11_ACCEPTANCE = ROOT / "validation" / "toe_solver_candidate_v0_1" / "FINAL_CANDIDATE_ACCEPTANCE_V0_11.json"


def main():
    old = json.loads(V11_ACCEPTANCE.read_text())
    current = run()
    checks = {
        "v011_acceptance_preserved": old.get("status") == "PASS" and old.get("candidate_release_ready") is True,
        "zero_missing_software_operators_preserved": old.get("missing_software_operators") == 0,
        "zero_missing_source_wiring_operators_preserved": old.get("missing_source_wiring_operators") == 0,
        "v012_observational_retyped_pass": current.get("status") == "PASS",
        "observational_source_nonproduction": current.get("checks", {}).get("observational_spatial_source_nonproduction") is True,
        "observational_production_receipt_absent": current.get("checks", {}).get("observational_spatial_has_no_production_receipt") is True,
        "no_physical_production_claim": current.get("physical_production_claim") is False,
        "canon_forbidden": current.get("canon_allowed") is False,
        "main_merge_still_requires_explicit_order": old.get("merge_to_main_requires_explicit_user_order") is True,
    }
    result = {
        "schema": "QHTRI_TOE_FINAL_CANDIDATE_GATE_V0_12",
        "status": "PASS" if all(checks.values()) else "FAIL",
        "verdict": "PASS_REPOSITORY_IMPLEMENTATION_COMPLETE_CLAIM_BOUNDARY_CLEAN" if all(checks.values()) else "FAIL_FINAL_CANDIDATE_GATE_V0_12",
        "authority": "CANDIDATE_ONLY",
        "canon_allowed": False,
        "physical_production_claim": False,
        "repository_implementation_complete": all(checks.values()),
        "external_physical_production_evidence": "OPEN_SEPARATE_EVIDENCE_GATE",
        "checks": checks,
        "passed": sum(bool(x) for x in checks.values()),
        "failed": sum(not bool(x) for x in checks.values()),
        "v011_acceptance_receipt_sha256": old.get("receipt_sha256"),
        "v012_observational_receipt_sha256": current.get("receipt_sha256"),
        "merge_to_main_requires_explicit_user_order": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
