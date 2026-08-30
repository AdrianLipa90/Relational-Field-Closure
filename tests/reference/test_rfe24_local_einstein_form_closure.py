from pathlib import Path


def read(root: Path, rel: str) -> str:
    return (root / rel).read_text(encoding="utf-8")


def test_rfe24_local_einstein_form_dependency_contract():
    root = Path(__file__).resolve().parents[2]

    e21 = read(root, "closure/einstein/RF_E21_EINSTEIN_UNIQUENESS_SELECTION.md")
    e22 = read(root, "closure/einstein/RF_E22_TIR_CARTAN_LEVI_CIVITA_BINDING.md")
    e23 = read(root, "closure/einstein/RF_E23_CONSERVED_SOURCE_DIVERGENCE_FREE_SELECTION.md")
    e3 = read(root, "closure/einstein/RF_E3_DOUBLE_COPY_EINSTEIN_HILBERT_NORMALIZATION.md")
    e12 = read(root, "closure/einstein/RF_E12_ACTION_PROJECTED_ADM_SOURCE_CONSTRAINTS.md")
    e13 = read(root, "closure/einstein/RF_E13_CONSTRAINT_PROPAGATION_BIANCHI_LEDGER.md")
    e24 = read(root, "closure/einstein/RF_E24_LOCAL_EINSTEIN_FORM_CLOSURE.md")

    # RF-E21 owns the theorem selection rather than RF-E24 inventing a new tensor ansatz.
    assert r"A\,G_{\mu\nu}+B\,g_{\mu\nu}" in e21
    assert "Lovelock" in e21

    # Cross-repository geometry provenance is pinned and local/global status is split.
    assert "59b820e74c3b7be0e4cd81aa95ec0a23184e4f24" in e22
    assert "GLOBAL_REFINEMENT_EXISTENCE_OPEN" in e22
    assert "0ec6190f54a5bc64c5dfb89bdc77b48c6c144828" in e24

    # Divergence-free selection is made before identifying the Einstein tensor.
    assert r"\nabla^\mu\mathcal E_{\mu\nu}\equiv0" in e23
    assert "universal-source autonomy" in e23.lower()

    # RF-E3 owns the standard Newton/Einstein coupling transfer.
    assert r"\kappa_E=\frac{8\pi G}{c^4}" in e3

    # E24 must perform the nondegenerate coefficient quotient explicitly.
    assert r"\Lambda:=\frac BA" in e24
    assert r"\kappa_E:=\frac CA" in e24
    assert r"G_{\mu\nu}+\Lambda g_{\mu\nu}" in e24
    assert r"\frac{8\pi G}{c^4}T_{\mu\nu}" in e24

    # Publication firewall: local closure cannot silently become global completion.
    assert "GLOBAL_SMOOTH_REALIZATION_OPEN" in e24
    assert "PROJECT_ABSOLUTE_G_PROMOTION_OPEN" in e24
    assert "HKT_CROSSCHECK_OPEN" in e24

    # Existing ADM parents must still own constraints and propagation.
    assert r"\mathcal G_H=2\kappa_E\rho_n" in e12
    assert "homogeneous" in e13.lower()
    assert "constraint" in e13.lower()


def test_rfe24_does_not_use_eh_as_tensor_form_selection_premise():
    root = Path(__file__).resolve().parents[2]
    e24 = read(root, "closure/einstein/RF_E24_LOCAL_EINSTEIN_FORM_CLOSURE.md")

    prior = e24.split("## 6. Einstein-Hilbert action as downstream representative", 1)[0]
    assert "Lovelock" in prior
    assert "universal-source autonomy" in prior.lower()
    assert "Einstein-Hilbert action as the premise" in prior


def test_rfe24_status_is_local_and_conditional_on_declared_rules():
    root = Path(__file__).resolve().parents[2]
    e24 = read(root, "closure/einstein/RF_E24_LOCAL_EINSTEIN_FORM_CLOSURE.md")

    assert "LOCAL_EINSTEIN_FORM_CLOSURE_PASS_ON_DECLARED_SELECTION_RULES" in e24
    assert "PASS ON TIR LRR" in e24
    assert "PASS ON RFC UNIVERSAL-SOURCE AUTONOMY RULE" in e24
    assert "global smooth relational realization" in e24.lower()
