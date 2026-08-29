import math

import pytest

from src.rfc.common_projective_cell_area_binding import (
    CommonProjectiveCellAreaError,
    admitted_common_area,
    area_defect,
    area_defect_from_ratio,
    area_ratio,
    constant_cell_area,
    nonuniform_cell_area,
    same_source_ledger,
)


def test_constant_cell_area_matches_idt_01k_formula():
    a_fs = math.pi
    omega = 2.5
    c = 3.0
    assert constant_cell_area(a_fs, omega, c) == pytest.approx(
        c * c * a_fs / (omega * omega)
    )


def test_area_ratio_separates_projective_and_clock_mismatch():
    a_r, a_c = 1.2, 0.8
    omega_r, r_0 = 2.0, 3.0
    expected = (a_r / a_c) * (r_0 / omega_r) ** 2
    assert area_ratio(a_r, a_c, omega_r, r_0) == pytest.approx(expected)


def test_same_cell_same_carriers_force_exact_common_area():
    area = admitted_common_area(
        radial_cell_id="P17",
        clock_cell_id="P17",
        radial_area_carrier_id="FS:P17",
        clock_area_carrier_id="FS:P17",
        radial_clock_carrier_id="CLOCK:P17",
        clock_clock_carrier_id="CLOCK:P17",
        a_fs_radial=math.pi / 3.0,
        a_fs_clock=math.pi / 3.0,
        omega_radial=1.75,
        r_0=1.75,
        c=2.0,
    )
    expected = constant_cell_area(math.pi / 3.0, 1.75, 2.0)
    assert area == pytest.approx(expected)
    assert area_ratio(math.pi / 3.0, math.pi / 3.0, 1.75, 1.75) == pytest.approx(1.0)
    assert area_defect(area, expected) == pytest.approx(0.0)
    assert area_defect_from_ratio(1.0) == pytest.approx(0.0)


def test_numerical_area_crossing_without_source_identity_is_not_admitted():
    assert not same_source_ledger(
        "P1",
        "P2",
        "FS:shared-value-only-A",
        "FS:shared-value-only-B",
        "CLOCK:A",
        "CLOCK:B",
    )
    with pytest.raises(CommonProjectiveCellAreaError):
        admitted_common_area(
            "P1",
            "P2",
            "FS:A",
            "FS:B",
            "CLOCK:A",
            "CLOCK:B",
            1.0,
            1.0,
            2.0,
            2.0,
        )


def test_same_ids_with_inconsistent_projective_area_fail_closed():
    with pytest.raises(CommonProjectiveCellAreaError):
        admitted_common_area(
            "P",
            "P",
            "FS:P",
            "FS:P",
            "CLOCK:P",
            "CLOCK:P",
            1.0,
            1.1,
            2.0,
            2.0,
        )


def test_same_ids_with_inconsistent_phase_rate_fail_closed():
    with pytest.raises(CommonProjectiveCellAreaError):
        admitted_common_area(
            "P",
            "P",
            "FS:P",
            "FS:P",
            "CLOCK:P",
            "CLOCK:P",
            1.0,
            1.0,
            2.0,
            2.1,
        )


def test_nonuniform_same_domain_and_integrand_give_same_area():
    weights = (0.2, 0.3, 0.5)
    rates = (1.0, 1.5, 2.0)
    area_r = nonuniform_cell_area(weights, rates, c=3.0)
    area_c = nonuniform_cell_area(weights, rates, c=3.0)
    assert area_r == pytest.approx(area_c)
    assert area_defect(area_r, area_c) == pytest.approx(0.0)


def test_nonuniform_rate_difference_is_detected():
    weights = (0.5, 0.5)
    area_r = nonuniform_cell_area(weights, (1.0, 2.0))
    area_c = nonuniform_cell_area(weights, (1.0, 3.0))
    assert area_r != pytest.approx(area_c)
    assert area_defect(area_r, area_c) > 0.0


@pytest.mark.parametrize("bad", [0.0, -1.0, math.inf, math.nan])
def test_positive_domains_fail_closed(bad):
    with pytest.raises(CommonProjectiveCellAreaError):
        constant_cell_area(1.0, bad)
    with pytest.raises(CommonProjectiveCellAreaError):
        constant_cell_area(bad, 1.0)


def test_invalid_nonuniform_quadrature_fails_closed():
    with pytest.raises(CommonProjectiveCellAreaError):
        nonuniform_cell_area((0.5,), (1.0, 2.0))
    with pytest.raises(CommonProjectiveCellAreaError):
        nonuniform_cell_area((-0.2, 1.2), (1.0, 1.0))
