import math

import pytest

from src.rfc.generator_source_placement import (
    GeneratorSourcePlacementError,
    einstein_residual_after_lambda_move,
    frobenius_norm4,
    lambda_shift_from_vacuum_energy,
    perfect_fluid_rest_tensor,
    source_placement_diagnostic,
    vacuum_stress_tensor,
)


def test_vacuum_equation_of_state_is_exactly_lambda_absorbable():
    rho = 7.25
    diag = source_placement_diagnostic(rho, -rho)
    assert diag.vacuum_absorbable
    assert diag.vacuum_residual == 0.0
    assert diag.vacuum_defect == 0.0
    assert diag.equation_of_state_w == -1.0
    assert perfect_fluid_rest_tensor(rho, -rho) == vacuum_stress_tensor(rho)


def test_dust_source_is_not_lambda_absorbable():
    rho = 7.25
    diag = source_placement_diagnostic(rho, 0.0)
    assert not diag.vacuum_absorbable
    assert diag.equation_of_state_w == 0.0
    assert math.isclose(diag.vacuum_defect, 2.0, rel_tol=0.0, abs_tol=1e-15)


def test_lambda_move_residual_vanishes_only_on_vacuum_surface():
    kappa_E = 2.1e-43
    rho = 9.0e12

    vacuum_residual = einstein_residual_after_lambda_move(rho, -rho, kappa_E)
    dust_residual = einstein_residual_after_lambda_move(rho, 0.0, kappa_E)
    radiation_residual = einstein_residual_after_lambda_move(rho, rho / 3.0, kappa_E)

    assert frobenius_norm4(vacuum_residual) == 0.0
    assert frobenius_norm4(dust_residual) > 0.0
    assert frobenius_norm4(radiation_residual) > frobenius_norm4(dust_residual)


def test_lambda_shift_is_kappa_E_times_energy_density():
    rho = 3.0e8
    kappa_E = 4.5e-44
    assert math.isclose(
        lambda_shift_from_vacuum_energy(rho, kappa_E),
        kappa_E * rho,
        rel_tol=0.0,
        abs_tol=1e-30,
    )


def test_zero_source_is_typed_without_division_by_zero():
    diag = source_placement_diagnostic(0.0, 0.0)
    assert diag.equation_of_state_w is None
    assert diag.vacuum_defect == 0.0
    assert diag.vacuum_absorbable


def test_fail_closed_inputs():
    bad_calls = (
        lambda: source_placement_diagnostic(float("nan"), 0.0),
        lambda: source_placement_diagnostic(1.0, float("inf")),
        lambda: source_placement_diagnostic(1.0, 0.0, tolerance=-1.0),
        lambda: lambda_shift_from_vacuum_energy(1.0, 0.0),
        lambda: einstein_residual_after_lambda_move(1.0, -1.0, -2.0),
    )
    for call in bad_calls:
        with pytest.raises(GeneratorSourcePlacementError):
            call()
