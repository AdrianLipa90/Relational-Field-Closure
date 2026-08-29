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


def _assert_exact_mapping(path, test_name, expected_claim, expected_source="formalism/DEPENDENCY_GRAPH.md"):
    plugin = FpdgFailurePlugin(load_bindings())
    plugin.pytest_runtest_logreport(_synthetic_failure(path, test_name, 10))
    assert len(plugin.failures) == 1
    failure = plugin.failures[0]
    assert failure["claim_id"] == expected_claim
    assert failure["source_locator"]["path"] == path
    assert failure["source_locator"]["line_start"] == 11
    assert failure["source_locator"]["test_id"].endswith(f"::{test_name}")
    assert f"claim-source:{expected_source}" in failure["evidence_refs"]


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


def test_scalar_total_matter_uses_exact_per_test_override():
    _assert_exact_mapping(
        "tests/reference/test_rfe7_total_scalar_stress_energy_composition.py",
        "test_einstein_source_ledger_is_exact_tensor_sum",
        "RFC.MATTER.SCALAR_TMN",
        "closure/einstein/RF_E7_TOTAL_SCALAR_STRESS_ENERGY_COMPOSITION.md",
    )


def test_lambda_chain_failures_map_to_exact_fpdg_claims():
    cases = (
        (
            "tests/reference/test_rfl1_oriented_holonomy_identities.py",
            "test_half_angle_partition_closes_energy",
            "RFC.L1.LAMBDA_TARGET",
            "formalism/RFL1_RELATIONAL_LAMBDA_ORIENTED_HOLONOMY.md",
        ),
        (
            "tests/reference/test_rfl2_dynamic_lambda0_action_stability.py",
            "test_action_split_maps_potential_to_dynamic_lambda_coordinate",
            "RFC.L2.LAMBDA_ACTION_STABILITY",
            "closure/lambda0/RF_L2_DYNAMIC_LAMBDA0_ACTION_REALIZABILITY_STABILITY.md",
        ),
        (
            "tests/reference/test_rfl3_information_scalar_potential_reconstruction.py",
            "test_exact_information_scalar_potential_roundtrip",
            "RFC.L3.INFORMATION_SCALAR_POTENTIAL",
            "closure/lambda0/RF_L3_INFORMATION_SCALAR_POTENTIAL_RECONSTRUCTION.md",
        ),
        (
            "tests/reference/test_rfl4_information_curvature_canonical_pullback.py",
            "test_square_root_coordinate_roundtrip",
            "RFC.L4.INFORMATION_CURVATURE_PULLBACK",
            "closure/lambda0/RF_L4_INFORMATION_CURVATURE_CANONICAL_PULLBACK.md",
        ),
        (
            "tests/reference/test_rfl4a_shannon_fisher_local_normalization.py",
            "test_beta_sqrt2_matches_local_fisher_radial_coordinate",
            "RFC.L4A.SHANNON_FISHER_NORMALIZATION",
            "closure/lambda0/RF_L4A_SHANNON_FISHER_LOCAL_NORMALIZATION.md",
        ),
        (
            "tests/reference/test_rfl5_shannon_onsager_klein_gordon_bridge.py",
            "test_uniform_onsager_stiffness_roundtrip_exact_normalization",
            "RFC.L5.TEMPORAL_WAVE_KG_BRIDGE",
            "closure/lambda0/RF_L5_SHANNON_ONSAGER_TEMPORAL_WAVE_KLEIN_GORDON_BRIDGE.md",
        ),
        (
            "tests/reference/test_rfl5a_premetric_dimensional_calibration_firewall.py",
            "test_lightcone_ratio_is_exact",
            "RFC.L5A.PREMETRIC_CALIBRATION",
            "closure/lambda0/RF_L5A_PREMETRIC_DIMENSIONAL_CALIBRATION_FIREWALL.md",
        ),
    )
    for path, test_name, expected_claim, expected_source in cases:
        _assert_exact_mapping(path, test_name, expected_claim, expected_source)


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
