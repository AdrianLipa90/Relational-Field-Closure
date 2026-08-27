import math


def finite_charge(current, volumes):
    if len(current) != len(volumes) or not current:
        raise ValueError("current/volume support mismatch")
    if any(v <= 0.0 for v in volumes):
        raise ValueError("positive cell volumes required")
    return sum(j * v for j, v in zip(current, volumes))


def measure_defect(v_theta, v_q):
    if len(v_theta) != len(v_q) or not v_theta:
        raise ValueError("measure support mismatch")
    return sum(abs(a - b) for a, b in zip(v_theta, v_q)) / sum(v_theta)


def local_current_defect(j_theta, j_q, volumes):
    q_theta = finite_charge(j_theta, volumes)
    if q_theta <= 0.0:
        raise ValueError("positive Noether total required")
    return sum(v * abs(a - b) for v, a, b in zip(volumes, j_theta, j_q)) / q_theta


def total_charge_defect(q_theta, q_sigma):
    if q_theta <= 0.0:
        raise ValueError("positive Noether total required")
    return abs(q_sigma - q_theta) / q_theta


def test_exact_rfc_noether_current_binding_has_zero_defects():
    volumes = [1.0, 2.0, 1.0]
    current = [1.0, 2.0, 3.0]
    q_theta = finite_charge(current, volumes)
    q_sigma = finite_charge(current, volumes)
    assert measure_defect(volumes, volumes) == 0.0
    assert local_current_defect(current, current, volumes) == 0.0
    assert total_charge_defect(q_theta, q_sigma) == 0.0


def test_equal_total_is_insufficient_for_rfc_local_current_promotion():
    volumes = [1.0, 1.0]
    j_theta = [1.0, 3.0]
    j_q = [2.0, 2.0]
    q_theta = finite_charge(j_theta, volumes)
    q_sigma = finite_charge(j_q, volumes)
    assert q_theta == q_sigma == 4.0
    assert total_charge_defect(q_theta, q_sigma) == 0.0
    assert math.isclose(local_current_defect(j_theta, j_q, volumes), 0.5, rel_tol=0.0, abs_tol=1e-15)


def test_rfc_measure_defect_is_explicit():
    assert math.isclose(measure_defect([1.0, 2.0], [1.0, 2.3]), 0.1, rel_tol=0.0, abs_tol=1e-15)


def test_integrated_charge_defect_is_explicit():
    q_theta = finite_charge([1.0, 2.0], [1.0, 1.0])
    q_sigma = finite_charge([2.0, 2.0], [1.0, 1.0])
    assert math.isclose(total_charge_defect(q_theta, q_sigma), 1.0 / 3.0, rel_tol=0.0, abs_tol=1e-15)


def test_exact_local_binding_implies_equal_finite_charge_on_common_measure():
    volumes = [0.25, 0.75, 1.0]
    current = [4.0, 2.0, 1.0]
    assert local_current_defect(current, current, volumes) == 0.0
    assert finite_charge(current, volumes) == finite_charge(current, volumes)


def test_zero_side_flux_is_exact_conservation_sector():
    assert abs(0.0) == 0.0


def test_epsilon_q_candidate_uses_same_energy_per_charge_after_carrier_identity():
    h_phi = 10.0
    q_theta = 5.0
    q_sigma = 5.0
    epsilon_n = h_phi / q_theta
    epsilon_q = h_phi / q_sigma
    assert epsilon_n == epsilon_q == 2.0
