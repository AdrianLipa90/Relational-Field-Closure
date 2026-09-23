import math

import pytest

from src.rfc.chemistry_loop_phase_interface import (
    fixed_carrier_phase_energy_response,
    loop_phase_displacement,
    loop_phase_from_two_paths,
)
from src.rfc.foundational_phase_source_formalism import FoundationalPhaseSourceError


def test_loop_phase_is_same_endpoint_gauge_invariant():
    c1 = 1.7
    c2 = -0.4
    endpoint_gauge_shift = 3.25
    base = loop_phase_from_two_paths(c1, c2)
    transformed = loop_phase_from_two_paths(
        c1 - endpoint_gauge_shift,
        c2 - endpoint_gauge_shift,
    )
    assert transformed == pytest.approx(base, abs=1e-15)


def test_inter_realization_loop_displacement_is_gauge_invariant():
    base = loop_phase_displacement(1.2, -0.3, 1.8, -0.1)
    reference_shift = 4.0
    perturbed_shift = -2.5
    transformed = loop_phase_displacement(
        1.2 - reference_shift,
        -0.3 - reference_shift,
        1.8 - perturbed_shift,
        -0.1 - perturbed_shift,
    )
    assert transformed.reference_loop_phase == pytest.approx(
        base.reference_loop_phase, abs=1e-15
    )
    assert transformed.perturbed_loop_phase == pytest.approx(
        base.perturbed_loop_phase, abs=1e-15
    )
    assert transformed.lifted_delta == pytest.approx(base.lifted_delta, abs=1e-15)
    assert transformed.projective_delta == pytest.approx(
        base.projective_delta, abs=1e-15
    )


def test_lift_retains_winding_while_projective_delta_closes():
    state = loop_phase_displacement(0.0, 0.0, 2.0 * math.pi, 0.0)
    assert state.lifted_delta == pytest.approx(2.0 * math.pi, abs=1e-15)
    assert state.projective_delta == pytest.approx(0.0, abs=1e-14)


def test_fixed_carrier_phase_energy_response_has_expected_scale():
    B = 2.0e-34
    omega = 5.0e9
    delta = 0.25
    expected = B * omega * delta
    assert fixed_carrier_phase_energy_response(B, omega, delta) == pytest.approx(
        expected, rel=1e-15
    )


@pytest.mark.parametrize(
    "args",
    [
        (float("nan"), 1.0, 1.0),
        (1.0, float("inf"), 1.0),
        (1.0, 1.0, float("nan")),
    ],
)
def test_energy_response_fails_closed_on_nonfinite_inputs(args):
    with pytest.raises(FoundationalPhaseSourceError):
        fixed_carrier_phase_energy_response(*args)
