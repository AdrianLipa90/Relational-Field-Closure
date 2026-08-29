from types import SimpleNamespace

from tools.run_reference_suite_with_fpdg_receipt import FpdgFailurePlugin, load_bindings


def _synthetic_failure(path, test_name, line_zero_based):
    return SimpleNamespace(
        failed=True,
        nodeid=f"{path}::{test_name}",
        when="call",
        location=(path, line_zero_based, test_name),
        longrepr=None,
    )


def _assert_exact_mapping(path, test_name, expected_claim):
    plugin = FpdgFailurePlugin(load_bindings())
    plugin.pytest_runtest_logreport(_synthetic_failure(path, test_name, 10))
    assert len(plugin.failures) == 1
    failure = plugin.failures[0]
    assert failure["claim_id"] == expected_claim
    assert failure["source_locator"]["path"] == path
    assert failure["source_locator"]["line_start"] == 11
    assert failure["source_locator"]["test_id"].endswith(f"::{test_name}")
    assert "claim-source:formalism/DEPENDENCY_GRAPH.md" in failure["evidence_refs"]


def test_conserved_carrier_failure_maps_to_exact_fpdg_source_claim():
    plugin = FpdgFailurePlugin(load_bindings())
    path = "tests/reference/test_rfn1b2_conserved_source_carrier.py"
    report = _synthetic_failure(
        path,
        "test_internal_continuity_flux_conserves_total_carrier",
        30,
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


def test_early_source_chain_failures_map_to_exact_fpdg_claims():
    cases = (
        (
            "tests/reference/test_rfn1b2k_noether_rfc_conserved_current_binding.py",
            "test_exact_rfc_noether_current_and_measure_binding_has_zero_defects",
            "RFC.N1B2K.CURRENT_MEASURE",
        ),
        (
            "tests/reference/test_rfn1b2o_phase_energy_current_source_binding.py",
            "test_local_energy_current_factorization",
            "RFC.N1B2O.MATTER_SOURCE_FACTORIZATION",
        ),
        (
            "tests/reference/test_rfn1b2p_charge_projected_em_current_intertwiner.py",
            "test_single_charge_intertwiner_is_exact",
            "RFC.N1B2P.MAXWELL_INTERTWINER",
        ),
    )
    for path, test_name, expected_claim in cases:
        _assert_exact_mapping(path, test_name, expected_claim)


def test_matter_action_chain_failures_map_to_exact_fpdg_claims():
    cases = (
        (
            "tests/reference/test_rfe4_phase_kinetic_stress_energy_firewall.py",
            "test_phase_only_active_einstein_source_is_four_times_energy_density",
            "RFC.E4.PHASE_STRESS_ENERGY",
        ),
        (
            "tests/reference/test_rfe5_onshell_scalar_carrier_energy.py",
            "test_phase_kinetic_and_total_energy_per_noether_charge_differ_by_two",
            "RFC.E5.CARRIER_ENERGY",
        ),
        (
            "tests/reference/test_rfe6_lorentzian_matter_action_source_bookkeeping.py",
            "test_matter_variation_has_minus_charge_current_over_hbar",
            "RFC.E6.LORENTZIAN_ACTION",
        ),
        (
            "tests/reference/test_rfe7_total_scalar_stress_energy_composition.py",
            "test_full_scalar_tensor_recomposes_from_three_exact_parts",
            "RFC.E7.SCALAR_T_DECOMPOSITION",
        ),
    )
    for path, test_name, expected_claim in cases:
        _assert_exact_mapping(path, test_name, expected_claim)


def test_rfe20_failure_maps_to_exact_fpdg_claim_and_test_coordinate():
    plugin = FpdgFailurePlugin(load_bindings())
    path = "tests/reference/test_rfe20_tetra_clock_mass_scale_closure.py"
    report = _synthetic_failure(path, "test_mass_scale", 40)

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
