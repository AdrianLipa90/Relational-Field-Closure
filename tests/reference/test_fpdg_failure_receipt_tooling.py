from types import SimpleNamespace

from tools.run_reference_suite_with_fpdg_receipt import FpdgFailurePlugin, load_bindings


def test_conserved_carrier_failure_maps_to_exact_fpdg_source_claim():
    plugin = FpdgFailurePlugin(load_bindings())
    path = "tests/reference/test_rfn1b2_conserved_source_carrier.py"
    report = SimpleNamespace(
        failed=True,
        nodeid=f"{path}::test_internal_continuity_flux_conserves_total_carrier",
        when="call",
        location=(path, 30, "test_internal_continuity_flux_conserves_total_carrier"),
        longrepr=None,
    )

    plugin.pytest_runtest_logreport(report)

    assert len(plugin.failures) == 1
    failure = plugin.failures[0]
    assert failure["claim_id"] == "RFC.SOURCE.CONSERVED_CARRIER"
    assert failure["source_locator"]["path"] == path
    assert failure["source_locator"]["line_start"] == 31
    assert failure["source_locator"]["test_id"].endswith(
        "::test_internal_continuity_flux_conserves_total_carrier"
    )
    assert "claim-source:formalism/DEPENDENCY_GRAPH.md" in failure["evidence_refs"]


def test_rfe20_failure_maps_to_exact_fpdg_claim_and_test_coordinate():
    plugin = FpdgFailurePlugin(load_bindings())
    path = "tests/reference/test_rfe20_tetra_clock_mass_scale_closure.py"
    report = SimpleNamespace(
        failed=True,
        nodeid=f"{path}::test_mass_scale",
        when="call",
        location=(path, 40, "test_mass_scale"),
        longrepr=None,
    )

    plugin.pytest_runtest_logreport(report)

    assert len(plugin.failures) == 1
    failure = plugin.failures[0]
    assert failure["claim_id"] == "RFC.E20.TETRA_CLOCK_MASS_SCALE"
    assert failure["source_locator"]["path"] == path
    assert failure["source_locator"]["line_start"] == 41
    assert failure["source_locator"]["test_id"].endswith("::test_mass_scale")
    assert "validation-receipt:validation/RF_E20_TETRA_CLOCK_MASS_SCALE_CLOSURE_V0_1.json" in failure["evidence_refs"]


def test_collection_failure_is_recorded_instead_of_being_silent():
    plugin = FpdgFailurePlugin(load_bindings())
    path = "tests/reference/test_rfe14_adm_directional_relative_entropy.py"
    report = SimpleNamespace(
        failed=True,
        nodeid=path,
        location=(path, 4, "<module>"),
        longrepr="import failed",
    )

    plugin.pytest_collectreport(report)

    assert len(plugin.failures) == 1
    failure = plugin.failures[0]
    assert failure["claim_id"] == "RFC.E14.DIRECTIONAL_RELATIVE_ENTROPY"
    assert failure["source_locator"]["line_start"] == 5
    assert "pytest-phase:collection" in failure["evidence_refs"]
