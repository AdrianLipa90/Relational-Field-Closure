import math

import pytest


def _finite_vector(values, name):
    out = tuple(float(value) for value in values)
    if not out or any(not math.isfinite(value) for value in out):
        raise ValueError(f"{name} must be a non-empty finite vector")
    return out


def _finite_nonzero(value, name):
    x = float(value)
    if not math.isfinite(x) or x == 0.0:
        raise ValueError(f"{name} must be finite and nonzero")
    return x


def scale_vector(scale, values):
    vector = _finite_vector(values, "current")
    factor = float(scale)
    if not math.isfinite(factor):
        raise ValueError("scale must be finite")
    return tuple(factor * value for value in vector)


def single_charge_em_current(j_rfc, q, hbar):
    h = _finite_nonzero(hbar, "hbar")
    charge = float(q)
    if not math.isfinite(charge):
        raise ValueError("q must be finite")
    return scale_vector(charge / h, j_rfc)


def charge_projected_current(component_currents, charges):
    currents = tuple(_finite_vector(values, "component current") for values in component_currents)
    qs = tuple(float(q) for q in charges)
    if not currents or len(currents) != len(qs):
        raise ValueError("component currents and charges must share non-empty support")
    if any(not math.isfinite(q) for q in qs):
        raise ValueError("charges must be finite")
    dimension = len(currents[0])
    if any(len(values) != dimension for values in currents):
        raise ValueError("component currents must have one common vector dimension")
    return tuple(
        sum(q * current[index] for q, current in zip(qs, currents))
        for index in range(dimension)
    )


def multiplet_em_current(component_currents, charges, hbar):
    h = _finite_nonzero(hbar, "hbar")
    return scale_vector(1.0 / h, charge_projected_current(component_currents, charges))


def total_carrier(component_currents):
    currents = tuple(_finite_vector(values, "component current") for values in component_currents)
    if not currents:
        raise ValueError("component currents must be non-empty")
    dimension = len(currents[0])
    if any(len(values) != dimension for values in currents):
        raise ValueError("component currents must have one common vector dimension")
    return tuple(sum(current[index] for current in currents) for index in range(dimension))


def l2(values):
    vector = _finite_vector(values, "vector")
    return math.sqrt(sum(value * value for value in vector))


def intertwiner_defect(j_em, j_rfc, q, hbar):
    observed = _finite_vector(j_em, "J_EM")
    predicted = single_charge_em_current(j_rfc, q, hbar)
    if len(observed) != len(predicted):
        raise ValueError("J_EM and RFC current must share vector dimension")
    residual = tuple(left - right for left, right in zip(observed, predicted))
    denominator = l2(observed) + l2(predicted)
    if denominator == 0.0:
        raise ValueError("use the neutral-sector gate for zero/zero current")
    return 2.0 * l2(residual) / denominator


def matmul2(left, right):
    return (
        (
            left[0][0] * right[0][0] + left[0][1] * right[1][0],
            left[0][0] * right[0][1] + left[0][1] * right[1][1],
        ),
        (
            left[1][0] * right[0][0] + left[1][1] * right[1][0],
            left[1][0] * right[0][1] + left[1][1] * right[1][1],
        ),
    )


def commutator2(left, right):
    lr = matmul2(left, right)
    rl = matmul2(right, left)
    return tuple(tuple(a - b for a, b in zip(row_lr, row_rl)) for row_lr, row_rl in zip(lr, rl))


def commutator_norm2(left, right):
    return math.sqrt(sum(value * value for row in commutator2(left, right) for value in row))


def test_single_charge_intertwiner_is_exact():
    j_rfc = (2.0, -1.0, 0.5, 4.0)
    q = 3.0
    hbar = 2.0
    j_em = (3.0, -1.5, 0.75, 6.0)
    assert single_charge_em_current(j_rfc, q, hbar) == j_em
    assert intertwiner_defect(j_em, j_rfc, q, hbar) == 0.0


def test_wrong_sign_fails_current_intertwiner():
    j_rfc = (1.0, 2.0, 3.0, 4.0)
    correct = single_charge_em_current(j_rfc, 2.0, 1.0)
    wrong = scale_vector(-1.0, correct)
    assert intertwiner_defect(wrong, j_rfc, 2.0, 1.0) > 1.9


def test_charge_scale_perturbation_is_detected():
    j_rfc = (1.0, -2.0, 0.5, 3.0)
    j_em = single_charge_em_current(j_rfc, 5.0, 2.0)
    assert intertwiner_defect(j_em, j_rfc, 5.0, 2.0) == 0.0
    assert intertwiner_defect(j_em, j_rfc, 5.5, 2.0) > 0.09


def test_opposite_charge_reverses_maxwell_current():
    j_rfc = (0.5, 1.0, -1.5, 2.0)
    positive = single_charge_em_current(j_rfc, 1.0, 1.0)
    negative = single_charge_em_current(j_rfc, -1.0, 1.0)
    assert negative == scale_vector(-1.0, positive)


def test_neutral_sector_has_zero_em_current_with_finite_carrier():
    j_rfc = (3.0, -2.0, 1.0, 0.5)
    assert l2(j_rfc) > 0.0
    assert single_charge_em_current(j_rfc, 0.0, 1.0) == (0.0, 0.0, 0.0, 0.0)


def test_equal_charge_multiplet_reduces_to_total_carrier_scaling():
    components = ((1.0, 2.0, 0.0, 1.0), (3.0, -1.0, 2.0, 0.5))
    q = 4.0
    hbar = 2.0
    assert multiplet_em_current(components, (q, q), hbar) == single_charge_em_current(
        total_carrier(components), q, hbar
    )


def test_unequal_charge_multiplet_requires_charge_resolved_packet():
    components_a = ((1.0, 0.0, 0.0, 0.0), (0.0, 1.0, 0.0, 0.0))
    components_b = ((0.0, 1.0, 0.0, 0.0), (1.0, 0.0, 0.0, 0.0))
    charges = (1.0, -1.0)
    assert total_carrier(components_a) == total_carrier(components_b)
    assert multiplet_em_current(components_a, charges, 1.0) != multiplet_em_current(
        components_b, charges, 1.0
    )


def test_charge_compatible_mass_generator_has_zero_commutator():
    mass2 = ((2.0, 0.0), (0.0, 5.0))
    charge = ((1.0, 0.0), (0.0, -1.0))
    assert commutator_norm2(mass2, charge) == 0.0


def test_charge_mixing_mass_generator_is_rejected_by_commutator_gate():
    mass2 = ((2.0, 0.25), (0.25, 5.0))
    charge = ((1.0, 0.0), (0.0, -1.0))
    assert commutator_norm2(mass2, charge) > 0.0


def test_synchronized_gauge_shift_preserves_covariant_phase_carrier():
    q = 2.0
    hbar = 4.0
    dtheta = (1.0, -2.0, 0.5, 3.0)
    potential = (0.25, 1.5, -0.75, 0.0)
    d_lambda = (0.5, -0.25, 1.0, 2.0)
    # lambda=(q/hbar)Lambda, hence dLambda=(hbar/q)d_lambda.
    shifted_dtheta = tuple(value + shift for value, shift in zip(dtheta, d_lambda))
    shifted_potential = tuple(
        value - (hbar / q) * shift for value, shift in zip(potential, d_lambda)
    )
    before = tuple(dt + (q / hbar) * a for dt, a in zip(dtheta, potential))
    after = tuple(dt + (q / hbar) * a for dt, a in zip(shifted_dtheta, shifted_potential))
    assert after == pytest.approx(before, rel=0.0, abs=1e-15)


def test_fail_closed_on_bad_dimensions_and_zero_hbar():
    with pytest.raises(ValueError, match="finite and nonzero"):
        single_charge_em_current((1.0, 2.0), 1.0, 0.0)
    with pytest.raises(ValueError, match="common vector dimension"):
        multiplet_em_current(((1.0, 2.0), (1.0,)), (1.0, 2.0), 1.0)
    with pytest.raises(ValueError, match="share vector dimension"):
        intertwiner_defect((1.0,), (1.0, 2.0), 1.0, 1.0)
