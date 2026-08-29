import math

import pytest


def current_flow_from_adm_components(j0, ji, lapse, shift):
    vals = (j0, ji, lapse, shift)
    if not all(math.isfinite(v) for v in vals):
        raise ValueError("finite current/ADM state required")
    if lapse <= 0.0 or j0 <= 0.0:
        raise ValueError("future current and positive lapse required")
    q = lapse * j0
    j_spatial = ji + shift * j0
    beta = j_spatial / q
    if abs(beta) >= 1.0:
        raise ValueError("current is not future timelike on this 1+1 sector")
    gamma = 1.0 / math.sqrt(1.0 - beta * beta)
    proper_density = q / gamma
    w = ji / j0
    return {
        "q": q,
        "j": j_spatial,
        "beta": beta,
        "gamma": gamma,
        "proper_density": proper_density,
        "w": w,
    }


def build_current_from_flow(q, beta, lapse, shift):
    vals = (q, beta, lapse, shift)
    if not all(math.isfinite(v) for v in vals):
        raise ValueError("finite flow state required")
    if q <= 0.0 or lapse <= 0.0 or abs(beta) >= 1.0:
        raise ValueError("future timelike flow required")
    j0 = q / lapse
    ji = q * beta - shift * j0
    return j0, ji


def phi(x):
    if not math.isfinite(x) or x <= 0.0:
        raise ValueError("positive finite carrier required")
    return x - 1.0 - math.log(x)


def directional_phi(beta, s):
    if s not in (-1, 1):
        raise ValueError("orientation must be +/-1")
    if not math.isfinite(beta) or abs(beta) >= 1.0:
        raise ValueError("sub-luminal beta required")
    return phi(1.0 / (1.0 - s * beta))


def test_current_decomposition_recovers_seeded_physical_velocity():
    q = 3.2
    beta = 0.37
    lapse = 1.4
    shift = -0.18
    j0, ji = build_current_from_flow(q, beta, lapse, shift)
    state = current_flow_from_adm_components(j0, ji, lapse, shift)
    assert state["q"] == pytest.approx(q)
    assert state["j"] == pytest.approx(q * beta)
    assert state["beta"] == pytest.approx(beta)


def test_coordinate_rate_matches_rfe18_relation_w_equals_n_beta_minus_b():
    q = 2.1
    beta = -0.28
    lapse = 1.3
    shift = 0.17
    j0, ji = build_current_from_flow(q, beta, lapse, shift)
    state = current_flow_from_adm_components(j0, ji, lapse, shift)
    assert state["w"] == pytest.approx(lapse * beta - shift)
    assert (state["w"] + shift) / lapse == pytest.approx(beta)


def test_current_norm_and_proper_density_are_consistent():
    q = 4.0
    beta = 0.6
    lapse = 1.0
    shift = 0.0
    j0, ji = build_current_from_flow(q, beta, lapse, shift)
    state = current_flow_from_adm_components(j0, ji, lapse, shift)
    current_norm = -(state["q"] ** 2) + state["j"] ** 2
    assert current_norm < 0.0
    assert state["proper_density"] == pytest.approx(math.sqrt(-current_norm))
    assert state["gamma"] * state["proper_density"] == pytest.approx(q)


def test_positive_current_rescaling_leaves_beta_invariant():
    q = 1.7
    beta = -0.42
    lapse = 1.1
    shift = 0.09
    j0, ji = build_current_from_flow(q, beta, lapse, shift)
    base = current_flow_from_adm_components(j0, ji, lapse, shift)
    scale = 5.3
    scaled = current_flow_from_adm_components(scale * j0, scale * ji, lapse, shift)
    assert scaled["beta"] == pytest.approx(base["beta"])
    assert scaled["q"] == pytest.approx(scale * base["q"])
    assert scaled["j"] == pytest.approx(scale * base["j"])
    assert scaled["proper_density"] == pytest.approx(scale * base["proper_density"])


def test_material_adapted_chart_has_shift_equals_n_beta():
    q = 2.6
    beta = 0.33
    lapse = 1.25
    shift = lapse * beta
    j0, ji = build_current_from_flow(q, beta, lapse, shift)
    state = current_flow_from_adm_components(j0, ji, lapse, shift)
    assert state["w"] == pytest.approx(0.0, abs=1.0e-15)
    assert shift == pytest.approx(lapse * state["beta"])


def test_directional_information_branch_is_now_current_sourced():
    q = 2.9
    beta = 0.21
    lapse = 1.2
    shift = -0.07
    j0, ji = build_current_from_flow(q, beta, lapse, shift)
    state = current_flow_from_adm_components(j0, ji, lapse, shift)
    expected_plus = math.log(1.0 - beta) + beta / (1.0 - beta)
    expected_minus = math.log(1.0 + beta) - beta / (1.0 + beta)
    assert directional_phi(state["beta"], 1) == pytest.approx(expected_plus)
    assert directional_phi(state["beta"], -1) == pytest.approx(expected_minus)


def test_current_sourced_branch_preserves_parity_conjugacy():
    beta = 0.26
    assert directional_phi(beta, 1) == pytest.approx(directional_phi(-beta, -1))
    assert directional_phi(beta, -1) == pytest.approx(directional_phi(-beta, 1))


def test_null_current_boundary_fails_timelike_gate():
    # q=1, |j|=1 is null, so the material four-velocity normalization is unavailable.
    with pytest.raises(ValueError):
        current_flow_from_adm_components(1.0, 1.0, 1.0, 0.0)


def test_spacelike_current_fails_timelike_gate():
    with pytest.raises(ValueError):
        current_flow_from_adm_components(1.0, 1.2, 1.0, 0.0)


@pytest.mark.parametrize(
    "j0,ji,lapse,shift",
    [
        (0.0, 0.0, 1.0, 0.0),
        (-1.0, 0.0, 1.0, 0.0),
        (1.0, 0.0, 0.0, 0.0),
        (math.nan, 0.0, 1.0, 0.0),
        (1.0, math.inf, 1.0, 0.0),
    ],
)
def test_invalid_current_or_adm_state_fails_closed(j0, ji, lapse, shift):
    with pytest.raises(ValueError):
        current_flow_from_adm_components(j0, ji, lapse, shift)
