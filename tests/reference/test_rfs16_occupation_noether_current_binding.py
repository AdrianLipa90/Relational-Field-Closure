import math

import pytest

from src.rfc.occupation_noether_current_binding import (
    OccupationNoetherBindingError,
    carrier_energy_per_charge,
    generator_density_from_current,
    occupation_current_binding_diagnostic,
    occupation_current_ledger,
    occupations_from_current,
)
from src.rfc.relational_generator_source_density import KAPPA_INFO


def test_cellwise_occupation_maps_exactly_to_current_density_and_total_charge():
    occupations = (2.0, 3.0, 5.0)
    volumes = (0.5, 2.0, 4.0)
    q0 = 7.0
    out = occupation_current_ledger(occupations, volumes, carrier_quantum=q0)

    assert out.predicted_current_densities == (28.0, 10.5, 8.75)
    assert out.total_occupation == 10.0
    assert out.total_charge == 70.0
    assert math.isclose(
        sum(v * j for v, j in zip(volumes, out.predicted_current_densities, strict=True)),
        out.total_charge,
        rel_tol=0.0,
        abs_tol=1e-14,
    )


def test_normalized_charge_profile_equals_normalized_occupation_profile_independent_of_volume():
    occupations = (1.0, 2.0, 7.0)
    volumes = (1e-6, 3.0, 900.0)
    out = occupation_current_ledger(occupations, volumes, carrier_quantum=2.5)

    assert all(
        math.isclose(a, b, rel_tol=0.0, abs_tol=1e-15)
        for a, b in zip(out.occupation_profile, out.charge_profile, strict=True)
    )
    assert math.isclose(sum(out.charge_profile), 1.0, rel_tol=0.0, abs_tol=1e-15)


def test_current_to_occupation_roundtrip_is_exact():
    occupations = (4.0, 9.0, 16.0, 25.0)
    volumes = (0.25, 0.5, 1.5, 4.0)
    q0 = 3.5
    ledger = occupation_current_ledger(occupations, volumes, carrier_quantum=q0)
    recovered = occupations_from_current(
        ledger.predicted_current_densities,
        volumes,
        carrier_quantum=q0,
    )
    assert all(
        math.isclose(a, b, rel_tol=0.0, abs_tol=1e-14)
        for a, b in zip(occupations, recovered, strict=True)
    )


def test_exact_predicted_current_has_zero_local_and_total_defect():
    occupations = (1.0, 3.0, 6.0)
    volumes = (0.4, 0.8, 1.2)
    predicted = occupation_current_ledger(occupations, volumes, carrier_quantum=2.0)
    diag = occupation_current_binding_diagnostic(
        occupations,
        volumes,
        predicted.predicted_current_densities,
        carrier_quantum=2.0,
    )
    assert diag.local_current_defect == 0.0
    assert diag.total_charge_defect == 0.0
    assert diag.bound_margin == 0.0
    assert diag.observed_profile == predicted.charge_profile


def test_equal_total_charge_does_not_imply_local_current_binding():
    occupations = (1.0, 3.0)
    volumes = (1.0, 1.0)
    # q0=1 predicts j=(1,3); observed j=(2,2) has same total charge.
    diag = occupation_current_binding_diagnostic(
        occupations,
        volumes,
        (2.0, 2.0),
        carrier_quantum=1.0,
    )
    assert diag.total_charge_defect == 0.0
    assert math.isclose(diag.local_current_defect, 0.5, rel_tol=0.0, abs_tol=1e-15)
    assert diag.bound_margin == 0.0


def test_total_charge_defect_is_bounded_by_local_current_defect():
    diag = occupation_current_binding_diagnostic(
        (2.0, 5.0, 7.0),
        (0.5, 1.0, 2.0),
        (3.0, 4.0, 5.0),
        carrier_quantum=1.25,
    )
    assert diag.total_charge_defect <= diag.local_current_defect + 1e-15
    assert diag.bound_margin <= 1e-15


def test_generator_rewrites_exactly_from_occupation_density_to_current_density():
    B = 2.75e-34
    omega = 6.0e10
    occupation = 13.0
    volume = 2.25e-3
    q0 = 4.0
    phi = 0.41

    current = q0 * occupation / volume
    direct = (B * omega * occupation / volume) * (phi + KAPPA_INFO)
    from_current = generator_density_from_current(
        B,
        omega,
        current,
        phi,
        carrier_quantum=q0,
    )
    epsilon_q = carrier_energy_per_charge(
        B,
        omega,
        phi,
        carrier_quantum=q0,
    )

    assert math.isclose(from_current, direct, rel_tol=1e-15)
    assert math.isclose(from_current, epsilon_q * current, rel_tol=1e-15)


def test_fail_closed_invalid_inputs():
    bad_calls = (
        lambda: occupation_current_ledger((), (1.0,)),
        lambda: occupation_current_ledger((1.0,), (0.0,)),
        lambda: occupation_current_ledger((-1.0,), (1.0,)),
        lambda: occupation_current_ledger((0.0,), (1.0,)),
        lambda: occupation_current_ledger((1.0,), (1.0,), carrier_quantum=0.0),
        lambda: occupations_from_current((-1.0,), (1.0,)),
        lambda: occupation_current_binding_diagnostic((1.0,), (1.0,), (1.0, 2.0)),
        lambda: generator_density_from_current(1.0, 1.0, -1.0, 0.0),
    )
    for call in bad_calls:
        with pytest.raises(OccupationNoetherBindingError):
            call()
