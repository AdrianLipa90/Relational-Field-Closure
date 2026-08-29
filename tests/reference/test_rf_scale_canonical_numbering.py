from pathlib import Path


SCALE_DIR = Path("closure/scale")
VALIDATION_DIR = Path("validation")
TEST_DIR = Path("tests/reference")


CANONICAL = {
    18: (
        "RF_S18_RELATIONAL_GENERATOR_DUST_STRESS_ENERGY.md",
        "RF_S18_RELATIONAL_GENERATOR_DUST_STRESS_ENERGY_V0_1.json",
        "test_rfs18_relational_generator_dust_stress_energy.py",
    ),
    19: (
        "RF_S19_FOURCURRENT_DUST_TENSOR_CLOSURE.md",
        "RF_S19_FOURCURRENT_DUST_TENSOR_CLOSURE_V0_1.json",
        "test_rfs19_fourcurrent_dust_tensor_closure.py",
    ),
    20: (
        "RF_S20_NOETHER_PROFILE_SOURCE_RECONSTRUCTION.md",
        "RF_S20_NOETHER_PROFILE_SOURCE_RECONSTRUCTION_V0_1.json",
        "test_rfs20_noether_profile_source_reconstruction.py",
    ),
    21: (
        "RF_S21_IDT_NOETHER_PROFILE_BINDING.md",
        "RF_S21_IDT_NOETHER_PROFILE_BINDING_V0_1.json",
        "test_rfs21_idt_noether_profile_binding.py",
    ),
    22: (
        "RF_S22_NOETHER_HAMILTONIAN_SOURCE_CLOSURE.md",
        "RF_S22_NOETHER_HAMILTONIAN_SOURCE_CLOSURE_V0_1.json",
        "test_rfs22_noether_hamiltonian_source_closure.py",
    ),
}


def test_rf_s18_through_s22_have_one_canonical_document_each():
    for gate, (doc_name, _, _) in CANONICAL.items():
        matches = sorted(SCALE_DIR.glob(f"RF_S{gate}_*.md"))
        assert [path.name for path in matches] == [doc_name]
        first_line = matches[0].read_text(encoding="utf-8").splitlines()[0]
        assert first_line.startswith(f"# RF-S{gate} ")


def test_rf_s18_through_s22_validation_and_test_paths_match_canonical_ids():
    for _, (_, validation_name, test_name) in CANONICAL.items():
        assert (VALIDATION_DIR / validation_name).is_file()
        assert (TEST_DIR / test_name).is_file()


def test_legacy_parallel_numbering_paths_are_absent():
    legacy_paths = (
        SCALE_DIR / "RF_S18_NOETHER_PROFILE_SOURCE_RECONSTRUCTION.md",
        SCALE_DIR / "RF_S19_IDT_NOETHER_PROFILE_BINDING.md",
        SCALE_DIR / "RF_S20_NOETHER_HAMILTONIAN_SOURCE_CLOSURE.md",
        VALIDATION_DIR / "RF_S18_NOETHER_PROFILE_SOURCE_RECONSTRUCTION_V0_1.json",
        VALIDATION_DIR / "RF_S19_IDT_NOETHER_PROFILE_BINDING_V0_1.json",
        VALIDATION_DIR / "RF_S20_NOETHER_HAMILTONIAN_SOURCE_CLOSURE_V0_1.json",
        TEST_DIR / "test_rfs18_noether_profile_source_reconstruction.py",
        TEST_DIR / "test_rfs19_idt_noether_profile_binding.py",
        TEST_DIR / "test_rfs20_noether_hamiltonian_source_closure.py",
    )
    assert all(not path.exists() for path in legacy_paths)
