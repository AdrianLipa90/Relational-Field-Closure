from __future__ import annotations

import json
from igs_sp3_observational_e2e_v0_12 import run


def main():
    out = run()
    checks = {
        "base_e2e_pass_after_retyping": out.get("status") == "PASS",
        "observational_id_prefix": str(out.get("physical_realization_id", "")).startswith("observational:igs-sp3:sha256:"),
        "candidate_only": out.get("authority") == "CANDIDATE_ONLY" and out.get("canon_allowed") is False,
        "no_physical_production_claim": out.get("physical_production_claim") is False,
        "source_typing_check": out.get("checks", {}).get("observational_spatial_source_nonproduction") is True,
        "production_receipt_absent": out.get("checks", {}).get("observational_spatial_has_no_production_receipt") is True,
        "production_admission_false": out.get("checks", {}).get("observational_spatial_production_admission_false") is True,
        "numerical_geometry_unchanged": out.get("claim_boundary_correction", {}).get("numerical_geometry_changed") is False,
    }
    result = {
        "schema": "QHTRI_TOE_IGS_SP3_OBSERVATIONAL_VALIDATION_V0_12",
        "status": "PASS" if all(checks.values()) else "FAIL",
        "authority": "CANDIDATE_ONLY",
        "canon_allowed": False,
        "physical_production_claim": False,
        "checks": checks,
        "passed": sum(bool(x) for x in checks.values()),
        "failed": sum(not bool(x) for x in checks.values()),
        "v012_receipt_sha256": out.get("receipt_sha256"),
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
