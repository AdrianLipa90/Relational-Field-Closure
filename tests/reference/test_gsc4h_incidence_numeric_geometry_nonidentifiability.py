import numpy as np
import pytest

from src.rfc.incidence_numeric_geometry_nonidentifiability import (
    certify_positive_translation_scaling_family,
    certify_same_incidence_distinct_numeric_cocycles,
    scale_translation_cocycle,
)
from src.rfc.rigid_overlap_cocycle_reconstruction import compose_edges, edge


def rz(theta):
    c, s = np.cos(theta), np.sin(theta)
    return np.array([[c, -s, 0.0], [s, c, 0.0], [0.0, 0.0, 1.0]])


def test_same_two_patch_incidence_admits_distinct_translation_cocycles():
    a = (edge("p", "q", np.eye(3), [1.0, 0.0, 0.0]),)
    b = (edge("p", "q", np.eye(3), [2.0, 0.0, 0.0]),)
    receipt = certify_same_incidence_distinct_numeric_cocycles(["p", "q"], a, b)
    assert receipt["status"] == "PASS"
    assert receipt["same_directed_incidence_edge_set"] is True
    assert receipt["distinct_numeric_cocycles"] is True
    assert receipt["inequivalent_mod_global_se3"] is True
    assert receipt["numeric_overlap_cocycle_remains_source_bound"] is True


def test_translation_scaling_preserves_consistent_triangle_cocycle():
    pq = edge("p", "q", rz(0.2), [1.0, 0.0, 0.0])
    qr = edge("q", "r", rz(-0.4), [0.0, 2.0, 0.0])
    pr = compose_edges(pq, qr)
    receipt = certify_positive_translation_scaling_family(
        ["p", "q", "r"], [pq, qr, pr], 1.7
    )
    assert receipt["status"] == "PASS"
    assert receipt["first_cocycle_certified"] is True
    assert receipt["second_cocycle_certified"] is True
    assert receipt["max_translation_difference"] > 0.0


def test_global_se3_quotient_does_not_remove_overlap_translation_difference():
    a = (edge("p", "q", np.eye(3), [1.0, 0.0, 0.0]),)
    b = (edge("p", "q", np.eye(3), [3.0, 0.0, 0.0]),)
    receipt = certify_same_incidence_distinct_numeric_cocycles(["p", "q"], a, b)
    assert receipt["inequivalent_mod_global_se3"] is True
    assert receipt["max_translation_difference"] == pytest.approx(2.0)


def test_same_incidence_can_also_carry_distinct_relative_rotation():
    a = (edge("p", "q", np.eye(3), [1.0, 0.0, 0.0]),)
    b = (edge("p", "q", rz(0.5), [1.0, 0.0, 0.0]),)
    receipt = certify_same_incidence_distinct_numeric_cocycles(["p", "q"], a, b)
    assert receipt["status"] == "PASS"
    assert receipt["max_rotation_difference"] > 0.0


def test_identical_numeric_cocycle_does_not_falsely_claim_nonidentifiability_witness():
    a = (edge("p", "q", np.eye(3), [1.0, 0.0, 0.0]),)
    receipt = certify_same_incidence_distinct_numeric_cocycles(["p", "q"], a, a)
    assert receipt["status"] == "FAIL"
    assert receipt["distinct_numeric_cocycles"] is False


def test_different_incidence_sets_are_rejected():
    a = (edge("p", "q", np.eye(3), [1.0, 0.0, 0.0]),)
    b = (edge("q", "r", np.eye(3), [1.0, 0.0, 0.0]),)
    with pytest.raises(ValueError, match="same directed incidence"):
        certify_same_incidence_distinct_numeric_cocycles(["p", "q", "r"], a, b)


def test_nonpositive_scaling_fails_closed():
    a = (edge("p", "q", np.eye(3), [1.0, 0.0, 0.0]),)
    with pytest.raises(ValueError):
        scale_translation_cocycle(a, 0.0)


def test_scaling_by_one_is_not_a_distinct_witness():
    a = (edge("p", "q", np.eye(3), [1.0, 0.0, 0.0]),)
    receipt = certify_positive_translation_scaling_family(["p", "q"], a, 1.0)
    assert receipt["status"] == "FAIL"
    assert receipt["distinct_numeric_cocycles"] is False
