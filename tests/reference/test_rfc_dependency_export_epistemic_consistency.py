import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def test_n1b2k_export_does_not_promote_reference_fixture_to_realized_physics():
    export = json.loads((ROOT / "DEPENDENCY_EXPORT.json").read_text(encoding="utf-8"))
    claim = next(
        row for row in export["claims"]
        if row["claim_id"] == "RFC.N1B2K.CURRENT_MEASURE"
    )

    assert "PHYSICAL_REALIZATION_INPUT_OPEN" in claim["status"]
    assert claim["status"] != "ACTIVE_PHYSICAL_REALIZATION"
    assert claim["source_path"] == "formalism/RF_F24_CURRENT_MEASURE_REALIZATION_RECEIPT.md"

    receipt = json.loads(
        (ROOT / "validation/RF_F24_CURRENT_MEASURE_REALIZATION_RECEIPT_V0_1.json")
        .read_text(encoding="utf-8")
    )
    assert receipt["status"] == "REFERENCE_SUITE_PASS"
    assert receipt["promotion_inputs"]
    assert all("realized-system" in item or "optional" in item for item in receipt["promotion_inputs"])


def test_f24_source_keeps_reference_and_realized_system_receipts_distinct():
    source = (
        ROOT / "formalism/RF_F24_CURRENT_MEASURE_REALIZATION_RECEIPT.md"
    ).read_text(encoding="utf-8")
    assert "PHYSICAL_REALIZATION_INPUT_OPEN" in source
    assert "reference zero-defect fixture" in source
    assert "realized-system receipt" in source
