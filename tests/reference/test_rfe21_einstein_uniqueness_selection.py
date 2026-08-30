from pathlib import Path

import pytest

from src.rfc.einstein_uniqueness_selection import (
    HKT_LEDGER,
    PROJECT_PREMISE_LEDGER,
    LovelockPremises,
    four_dimensional_lovelock_spectrum,
    hkt_independent_route_ready,
    lovelock_term_status,
    project_ready_for_lovelock_promotion,
    tensor_selection_status,
)


def test_4d_lovelock_dynamic_topological_zero_split():
    spectrum = four_dimensional_lovelock_spectrum(5)
    assert spectrum == {
        0: "DYNAMIC",
        1: "DYNAMIC",
        2: "TOPOLOGICAL",
        3: "ZERO",
        4: "ZERO",
        5: "ZERO",
    }


@pytest.mark.parametrize(
    "dimension,order,expected",
    [
        (3, 1, "DYNAMIC"),
        (2, 1, "TOPOLOGICAL"),
        (4, 2, "TOPOLOGICAL"),
        (5, 2, "DYNAMIC"),
        (4, 3, "ZERO"),
    ],
)
def test_general_lovelock_dimension_rule(dimension, order, expected):
    assert lovelock_term_status(dimension, order) == expected


def test_tensor_selection_is_fail_closed():
    full = LovelockPremises(True, True, True, True, True, True, True)
    assert tensor_selection_status(full) == "EINSTEIN_PLUS_METRIC_TERM_SELECTED"

    fields = list(full.__dataclass_fields__)
    for field in fields:
        data = {name: True for name in fields}
        data[field] = False
        candidate = LovelockPremises(**data)
        assert tensor_selection_status(candidate) == "PROJECT_PREMISES_OPEN"


def test_project_promotion_is_currently_open_for_explicit_reasons():
    assert PROJECT_PREMISE_LEDGER["global_refinement_levi_civita"] == "OPEN"
    assert PROJECT_PREMISE_LEDGER["full_4d_naturality_covariance"] == "OPEN"
    assert PROJECT_PREMISE_LEDGER["second_order_locality"] == "OPEN"
    assert PROJECT_PREMISE_LEDGER["divergence_free_selection_binding"] == "OPEN_SELECTION_BINDING"
    assert project_ready_for_lovelock_promotion() is False


def test_hkt_route_is_independent_and_currently_open():
    assert HKT_LEDGER["independent_gravitational_piij"] == "OPEN"
    assert HKT_LEDGER["independent_hypersurface_deformation_algebra"] == "OPEN"
    assert hkt_independent_route_ready() is False


def test_parent_dependency_markers_present():
    root = Path(__file__).resolve().parents[2]

    rfg0 = (root / "formalism/RFG0_LORENTZIAN_SIGNATURE_GATE.md").read_text(encoding="utf-8")
    rf02h = (root / "formalism/RF02H_HEXAHEDRAL_RANK3_SPATIAL_METRIC.md").read_text(encoding="utf-8")
    rf02i = (root / "formalism/RF02I_HEXAHEDRAL_COFRAME_CONNECTION.md").read_text(encoding="utf-8")
    rfe3 = (root / "closure/einstein/RF_E3_DOUBLE_COPY_EINSTEIN_HILBERT_NORMALIZATION.md").read_text(encoding="utf-8")
    rfe8 = (root / "closure/einstein/RF_E8_ADM_KINEMATIC_ASSEMBLY_FIREWALL.md").read_text(encoding="utf-8")
    rfe12 = (root / "closure/einstein/RF_E12_ACTION_PROJECTED_ADM_SOURCE_CONSTRAINTS.md").read_text(encoding="utf-8")

    assert r"\operatorname{signature}(g)=(-,+,+,+)" in rfg0
    assert r"\operatorname{rank}h_H=3" in rf02h
    assert r"dE^i+\omega^i{}_j\wedge E^j=0" in rf02i
    assert r"\kappa_E=\frac{8\pi G}{c^4}" in rfe3
    assert r"\det g=-N_R^2\det h" in rfe8
    assert "RF-E3   Einstein-Hilbert action normalization and metric variation" in rfe12


def test_e21_document_keeps_hkt_non_circular():
    root = Path(__file__).resolve().parents[2]
    e21 = (root / "closure/einstein/RF_E21_EINSTEIN_UNIQUENESS_SELECTION.md").read_text(encoding="utf-8")
    assert "Existing RF-E12/RF-E13 constraints cannot be used as the independent HKT proof" in e21
    assert "GLOBAL LEVI-CIVITA" in e21
    assert "4D NATURALITY / COVARIANCE" in e21
    assert "SECOND-ORDER LOCALITY" in e21
