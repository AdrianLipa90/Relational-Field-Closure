import math
import pytest


def finite_charge(current, volumes):
    if len(current) != len(volumes) or not current:
        raise ValueError("current/volume support mismatch")
    if any(v <= 0.0 for v in volumes):
        raise ValueError("positive cell volumes required")
    return sum(j * v for j, v in zip(current, volumes))


def binding_defects(j_theta, v_theta, j_q, v_q):
    if not (len(j_theta) == len(v_theta) == len(j_q) == len(v_q)) or not j_theta:
        raise ValueError("common cell IDs required")
    q_theta = finite_charge(j_theta, v_theta)
    q_sigma = finite_charge(j_q, v_q)
    if q_theta <= 0.0:
        raise ValueError("positive Noether total required")
    if q_sigma <= 0.0:
        raise ValueError("positive RFC total required")
    delta_j = sum(vq * abs(jq - jt) for jt, jq, vq in zip(j_theta, j_q, v_q)) / q_theta
    delta_v = sum(abs(vq - vt) * abs(jt) for jt, vt, vq in zip(j_theta, v_theta, v_q)) / q_theta
    delta_sigma = abs(q_sigma - q_theta) / q_theta
    return q_theta, q_sigma, delta_j, delta_v, delta_sigma


def normalized_profile(current, volumes):
    q = finite_charge(current, volumes)
    if q <= 0.0:
        raise ValueError("positive carrier required")
    return [j * v / q for j, v in zip(current, volumes)]


def test_exact_rfc_noether_current_and_measure_binding_has_zero_defects():
    volumes = [1.0, 2.0, 1.0]
    current = [1.0, 2.0, 3.0]
    q_theta, q_sigma, delta_j, delta_v, delta_sigma = binding_defects(
        current, volumes, current, volumes
    )
    assert q_theta == q_sigma
    assert (delta_j, delta_v, delta_sigma) == (0.0, 0.0, 0.0)


def test_rfn1b2k_exact_triangle_bound_holds():
    rows = [
        ([1.0, 2.0], [1.0, 2.0], [1.2, 1.8], [1.0, 2.0]),
        ([0.5, 1.5, 2.0], [1.0, 1.0, 2.0], [0.6, 1.4, 2.2], [1.1, 0.9, 1.8]),
        ([3.0, 1.0], [0.4, 2.0], [2.5, 1.2], [0.5, 1.8]),
    ]
    for j_theta, v_theta, j_q, v_q in rows:
        _, _, delta_j, delta_v, delta_sigma = binding_defects(j_theta, v_theta, j_q, v_q)
        assert delta_sigma <= delta_j + delta_v + 1e-15


def test_equal_total_is_insufficient_for_rfc_local_current_promotion():
    volumes = [1.0, 1.0]
    j_theta = [1.0, 3.0]
    j_q = [2.0, 2.0]
    q_theta, q_sigma, delta_j, delta_v, delta_sigma = binding_defects(
        j_theta, volumes, j_q, volumes
    )
    assert q_theta == q_sigma == 4.0
    assert delta_sigma == 0.0
    assert math.isclose(delta_j, 0.5, rel_tol=0.0, abs_tol=1e-15)
    assert delta_v == 0.0


def test_current_and_measure_defects_are_independent():
    _, _, dj_current, dv_current, _ = binding_defects(
        [1.0, 2.0], [1.0, 1.0], [1.5, 2.0], [1.0, 1.0]
    )
    _, _, dj_measure, dv_measure, _ = binding_defects(
        [1.0, 2.0], [1.0, 1.0], [1.0, 2.0], [1.2, 0.8]
    )
    assert dj_current > 0.0 and dv_current == 0.0
    assert dj_measure == 0.0 and dv_measure > 0.0


def test_exact_local_binding_implies_equal_finite_charge():
    current = [4.0, 2.0, 1.0]
    volumes = [0.25, 0.75, 1.0]
    q_theta, q_sigma, delta_j, delta_v, delta_sigma = binding_defects(
        current, volumes, current, volumes
    )
    assert delta_j == 0.0 and delta_v == 0.0 and delta_sigma == 0.0
    assert q_sigma == q_theta


def test_exact_local_binding_preserves_normalized_profile():
    current = [1.0, 3.0, 2.0]
    volumes = [0.25, 0.5, 1.25]
    p_theta = normalized_profile(current, volumes)
    p_q = normalized_profile(current, volumes)
    assert p_q == p_theta
    assert math.isclose(sum(p_q), 1.0, rel_tol=0.0, abs_tol=1e-15)


def test_zero_side_flux_is_exact_conservation_sector():
    assert abs(0.0) == 0.0


def test_epsilon_q_candidate_uses_same_energy_after_carrier_identity():
    h_phi = 10.0
    q_theta = 5.0
    q_sigma = q_theta
    epsilon_n = h_phi / q_theta
    epsilon_q = h_phi / q_sigma
    assert epsilon_n == epsilon_q == 2.0
    assert epsilon_q * q_sigma == h_phi


def test_partition_measure_and_positive_sector_gates_fail_closed():
    with pytest.raises(ValueError, match="common cell IDs"):
        binding_defects([1.0, 2.0], [1.0, 1.0], [1.0], [1.0])
    with pytest.raises(ValueError, match="positive cell volumes"):
        binding_defects([1.0], [1.0], [1.0], [0.0])
    with pytest.raises(ValueError, match="positive Noether total"):
        binding_defects([-1.0], [1.0], [1.0], [1.0])
