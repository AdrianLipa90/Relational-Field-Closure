import math

import pytest

from src.rfc.chemistry_carrier_scale_identifiability import (
    CarrierScaleIdentifiabilityError,
    carrier_scale_state,
    dot,
    log_source_jacobian,
    log_source_null_directions,
    observable_rank,
    parameter_identifiable,
    rescale_source_equivalent,
)


def test_two_parameter_rescaling_preserves_source_density_exactly():
    base = carrier_scale_state(
        B_action=2.5,
        occupation=7.0,
        volume=11.0,
        omega=13.0,
        phase_factor=0.4,
    )
    for a, b in ((2.0, 3.0), (0.25, 4.0), (7.0, 0.2)):
        moved = rescale_source_equivalent(
            base,
            action_scale=a,
            occupation_scale=b,
        )
        assert moved.source_density == pytest.approx(
            base.source_density,
            rel=1e-15,
        )
        assert moved.carrier_energy == pytest.approx(
            a * base.carrier_energy,
            rel=1e-15,
        )
        assert moved.occupation_density == pytest.approx(
            base.occupation_density / a,
            rel=1e-15,
        )


def test_log_source_jacobian_has_two_independent_null_directions():
    jac = log_source_jacobian()
    dirs = log_source_null_directions()
    assert len(dirs) == 2
    for direction in dirs:
        assert dot(jac, direction) == pytest.approx(0.0, abs=1e-15)

    # The two listed directions are not collinear.
    cross = (
        dirs[0][1] * dirs[1][2] - dirs[0][2] * dirs[1][1],
        dirs[0][2] * dirs[1][0] - dirs[0][0] * dirs[1][2],
        dirs[0][0] * dirs[1][1] - dirs[0][1] * dirs[1][0],
    )
    assert math.sqrt(sum(x*x for x in cross)) > 0.0


def test_source_density_does_not_identify_carrier_energy():
    base = carrier_scale_state(1.0, 5.0, 7.0, 3.0, 0.2)
    moved = rescale_source_equivalent(
        base,
        action_scale=4.0,
        occupation_scale=1.0,
    )
    assert moved.source_density == pytest.approx(base.source_density)
    assert moved.carrier_energy != pytest.approx(base.carrier_energy)


@pytest.mark.parametrize(
    "args",
    [
        (0.0, 1.0, 1.0, 1.0, 1.0),
        (1.0, -1.0, 1.0, 1.0, 1.0),
        (1.0, 1.0, 0.0, 1.0, 1.0),
        (1.0, 1.0, 1.0, float("nan"), 1.0),
    ],
)
def test_fail_closed_inputs(args):
    with pytest.raises(CarrierScaleIdentifiabilityError):
        carrier_scale_state(*args)


def test_rho_epsilon_and_n_are_rank_redundant():
    assert observable_rank(("rho", "epsilon", "n")) == 2


def test_minimal_routes_identify_B():
    assert parameter_identifiable(("epsilon",), "B")
    assert parameter_identifiable(("rho", "n"), "B")
    assert not parameter_identifiable(("rho",), "B")


def test_full_parameter_identification_requires_absolute_N_or_V_scale():
    assert observable_rank(("rho", "epsilon", "N")) == 3
    assert observable_rank(("rho", "epsilon", "V")) == 3
    assert observable_rank(("rho", "n", "N")) == 3
    assert observable_rank(("rho", "n", "V")) == 3

    assert observable_rank(("rho", "epsilon", "n")) == 2
    assert not parameter_identifiable(("rho", "epsilon", "n"), "N")
    assert not parameter_identifiable(("rho", "epsilon", "n"), "V")
