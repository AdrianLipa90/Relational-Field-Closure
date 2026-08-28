import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CONTRACT = ROOT / "validation" / "gremlin" / "RFG4B_ALPHA_C_EXTRACTION_REPLAY_CONTRACT_v0.1.json"


def load_contract():
    return json.loads(CONTRACT.read_text(encoding="utf-8"))


def test_historical_reported_interval_contains_analytic_legacy_crosscheck():
    c = load_contract()
    mean = c["historical_report"]["alpha_c_mean"]
    half = c["historical_report"]["alpha_c_reported_half_width"]
    candidate = c["analytic_crosscheck"]["alpha_c_legacy_reconstruction"]
    assert mean - half <= candidate <= mean + half


def test_legacy_reconstruction_rounds_to_archived_six_decimal_coordinate():
    c = load_contract()
    candidate = c["analytic_crosscheck"]["alpha_c_legacy_reconstruction"]
    assert round(candidate, 6) == c["historical_report"]["alpha_c_mean"]


def test_paper_adaptive_eta_is_positive_and_bounded_by_point_zero_one():
    numerator = 0.01
    for grad_norm in [0.0, 0.1, 1.0, 10.0, 100.0]:
        eta = numerator / (1.0 + grad_norm)
        assert 0.0 < eta <= numerator


def test_paper_update_and_archived_generic_optimizer_are_separately_typed():
    c = load_contract()
    assert c["paper_method"]["alpha_update_sign"] == 1
    assert c["optimiser_ancestry"]["update_sign"] == -1
    assert c["paper_method"]["eta_rule"] != c["optimiser_ancestry"]["objective"]


def test_same_positive_gradient_moves_paper_coordinate_and_generic_descent_in_opposite_directions():
    theta = 0.4
    grad = 0.1
    eta = 0.005
    paper_next = theta + eta * grad
    generic_next = theta - 0.05 * grad
    assert paper_next > theta
    assert generic_next < theta


def test_typed_1024_counts_have_zero_identity_authority():
    c = load_contract()
    fw = c["typed_count_firewall"]
    assert fw["simulation_run_count"] == 1024
    assert fw["batch17_time_series_sample_count"] == 1024
    assert fw["identity_authority"] is False


def test_replay_gate_requires_nonempty_driver_coordinate_set():
    c = load_contract()
    required = c["required_driver_coordinates"]
    assert len(required) >= 30
    assert len(required) == len(set(required))
    for key in [
        "psi_initialization",
        "random_seed_schedule",
        "alpha_c_initialization",
        "fourth_order_stencil",
        "symplectic_update_map",
        "adaptive_timestep_law",
        "peak_detector",
        "ensemble_uncertainty_estimator",
    ]:
        assert key in required


def test_promotion_sequence_ends_only_after_ensemble_statistics_reproduction():
    c = load_contract()
    seq = c["promotion_sequence"]
    assert seq[-2] == "ENSEMBLE_STATISTICS_REPRODUCED"
    assert seq[-1] == "EXTRACTION_REPLAY_PASS"


def test_analytic_residual_is_far_below_reported_historical_half_width():
    c = load_contract()
    mean = c["historical_report"]["alpha_c_mean"]
    half = c["historical_report"]["alpha_c_reported_half_width"]
    candidate = c["analytic_crosscheck"]["alpha_c_legacy_reconstruction"]
    residual = abs(candidate - mean)
    assert residual < half / 100.0
    assert math.isclose(residual, 2.619417855509899e-08, rel_tol=5e-7, abs_tol=1e-15)
