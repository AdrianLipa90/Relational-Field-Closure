import math
import pytest

from src.rfc.einstein_action_selection import (
    Admissibility,
    EinsteinActionSelectionError,
    coupling_closure_ratio,
    eh_action_prefactor_si,
    einstein_coupling_from_prefactor,
    einstein_coupling_si,
    lorentz_signature,
    selected_bulk_basis,
    source_bound_3plus1_ready,
)


def ready():
    return Admissibility(
        spacetime_dimension=4,
        lorentzian_metric=True,
        diffeomorphism_covariant=True,
        metric_local_bulk=True,
        second_order_metric_equations=True,
    )


def test_tir_idt_rank_composition_is_3_plus_1():
    assert source_bound_3plus1_ready(3, 1, True)
    assert lorentz_signature(3, 1) == (-1, 1, 1, 1)


def test_4d_lovelock_gate_selects_cosmological_and_ricci_bulk_basis():
    assert selected_bulk_basis(ready()) == ("cosmological_density", "ricci_scalar")


@pytest.mark.parametrize(
    "field,value",
    [
        ("spacetime_dimension", 5),
        ("lorentzian_metric", False),
        ("diffeomorphism_covariant", False),
        ("metric_local_bulk", False),
        ("second_order_metric_equations", False),
    ],
)
def test_action_selection_fails_closed_when_an_admissibility_parent_is_open(field, value):
    data = ready().__dict__.copy()
    data[field] = value
    with pytest.raises(EinsteinActionSelectionError):
        selected_bulk_basis(Admissibility(**data))


def test_rf_e3_prefactor_implies_einstein_coupling_exactly():
    G = 6.67430e-11
    c = 299792458.0
    A = eh_action_prefactor_si(G, c)
    k_from_A = einstein_coupling_from_prefactor(A)
    k_direct = einstein_coupling_si(G, c)
    assert k_from_A == pytest.approx(k_direct, rel=2e-15)
    assert coupling_closure_ratio(G, c) == pytest.approx(1.0, rel=2e-15)


def test_prefactor_identity_symbolic_numeric_controls():
    for G, c in [(1.0, 1.0), (2.3, 7.1), (6.67430e-11, 299792458.0)]:
        A = eh_action_prefactor_si(G, c)
        assert 2.0 * A * einstein_coupling_si(G, c) == pytest.approx(1.0, rel=2e-15)


@pytest.mark.parametrize("G,c", [(0.0,1.0),(-1.0,1.0),(1.0,0.0),(1.0,-1.0),(math.inf,1.0)])
def test_nonpositive_or_nonfinite_constants_fail_closed(G,c):
    with pytest.raises(EinsteinActionSelectionError):
        eh_action_prefactor_si(G,c)
