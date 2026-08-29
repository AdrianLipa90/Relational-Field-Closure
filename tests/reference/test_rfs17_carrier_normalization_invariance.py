import math

import pytest

from src.rfc.carrier_normalization_invariance import (
    CarrierNormalizationError,
    carrier_normalization_state,
    energy_density_invariance_defect,
    rescale_carrier_normalization,
)


def test_carrier_rescaling_changes_current_units_but_not_energy_density():
    base = carrier_normalization_state(
        (2.0, 3.0, 5.0),
        (0.5, 1.5, 4.0),
        carrier_quantum=2.0,
        energy_per_occupied_carrier=7.0,
    )
    scaled = rescale_carrier_normalization(base, 11.0)

    assert scaled.carrier_quantum == 11.0 * base.carrier_quantum
    assert scaled.total_charge == 11.0 * base.total_charge
    assert all(
        math.isclose(b, 11.0 * a, rel_tol=0.0, abs_tol=1e-14)
        for a, b in zip(base.current_densities, scaled.current_densities, strict=True)
    )
    assert math.isclose(scaled.energy_per_charge, base.energy_per_charge / 11.0, rel_tol=1e-15)
    assert scaled.energy_density_cells == base.energy_density_cells
    assert scaled.normalized_profile == base.normalized_profile
    assert energy_density_invariance_defect(base, scaled) == 0.0


def test_energy_density_is_occupation_density_times_energy_per_occupied_carrier():
    occupations = (4.0, 6.0)
    volumes = (2.0, 3.0)
    epsilon_occ = 9.5
    state = carrier_normalization_state(
        occupations,
        volumes,
        carrier_quantum=13.0,
        energy_per_occupied_carrier=epsilon_occ,
    )
    expected = tuple(n * epsilon_occ / v for n, v in zip(occupations, volumes, strict=True))
    assert all(
        math.isclose(a, b, rel_tol=1e-15)
        for a, b in zip(state.energy_density_cells, expected, strict=True)
    )


def test_profile_is_independent_of_carrier_quantum():
    args = ((1.0, 4.0, 5.0), (0.1, 3.0, 20.0))
    a = carrier_normalization_state(*args, carrier_quantum=1.0, energy_per_occupied_carrier=2.0)
    b = carrier_normalization_state(*args, carrier_quantum=1000.0, energy_per_occupied_carrier=2.0)
    assert a.normalized_profile == b.normalized_profile
    assert all(math.isclose(x, y, rel_tol=1e-15) for x, y in zip(a.energy_density_cells, b.energy_density_cells, strict=True))


def test_composed_rescalings_multiply():
    state = carrier_normalization_state((1.0, 2.0), (1.0, 1.0), carrier_quantum=3.0, energy_per_occupied_carrier=4.0)
    seq = rescale_carrier_normalization(rescale_carrier_normalization(state, 2.0), 5.0)
    direct = rescale_carrier_normalization(state, 10.0)
    assert seq == direct


def test_fail_closed_inputs():
    bad_calls = (
        lambda: carrier_normalization_state((), (), carrier_quantum=1.0, energy_per_occupied_carrier=1.0),
        lambda: carrier_normalization_state((1.0,), (0.0,), carrier_quantum=1.0, energy_per_occupied_carrier=1.0),
        lambda: carrier_normalization_state((-1.0,), (1.0,), carrier_quantum=1.0, energy_per_occupied_carrier=1.0),
        lambda: carrier_normalization_state((0.0,), (1.0,), carrier_quantum=1.0, energy_per_occupied_carrier=1.0),
        lambda: carrier_normalization_state((1.0,), (1.0,), carrier_quantum=0.0, energy_per_occupied_carrier=1.0),
    )
    for call in bad_calls:
        with pytest.raises(CarrierNormalizationError):
            call()

    good = carrier_normalization_state((1.0,), (1.0,), carrier_quantum=1.0, energy_per_occupied_carrier=1.0)
    with pytest.raises(CarrierNormalizationError):
        rescale_carrier_normalization(good, 0.0)
