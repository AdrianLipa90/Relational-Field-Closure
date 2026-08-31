import numpy as np
import pytest

from src.rfc.rigid_overlap_cocycle_reconstruction import (
    compose_edges,
    edge,
    inverse_edge,
    reconstruct_from_cocycle,
)


def rz(theta):
    c, s = np.cos(theta), np.sin(theta)
    return np.array([[c, -s, 0.0], [s, c, 0.0], [0.0, 0.0, 1.0]])


def test_inverse_edge_formula():
    e = edge("p", "q", rz(0.4), [1.0, -2.0, 0.5])
    inv = inverse_edge(e)
    assert inv.rotation == pytest.approx(e.rotation.T)
    assert inv.translation == pytest.approx(-(e.rotation.T @ e.translation))


def test_composition_formula():
    pq = edge("p", "q", rz(0.2), [1.0, 0.0, 0.0])
    qr = edge("q", "r", rz(-0.3), [0.0, 2.0, 0.0])
    pr = compose_edges(pq, qr)
    assert pr.rotation == pytest.approx(qr.rotation @ pq.rotation)
    assert pr.translation == pytest.approx(qr.rotation @ pq.translation + qr.translation)


def test_two_patch_tree_reconstructs_relative_geometry():
    pq = edge("p", "q", rz(0.5), [1.0, 2.0, 3.0])
    receipt = reconstruct_from_cocycle(["p", "q"], [pq], root="p")
    assert receipt["status"] == "PASS"
    assert receipt["minimal_tree_edge_count"] == 1
    assert receipt["minimal_continuous_relative_dof"] == 6
    assert receipt["charts"]["p"].anchor == pytest.approx(np.zeros(3))
    assert receipt["charts"]["p"].frame == pytest.approx(np.eye(3))


def test_three_patch_tree_has_exact_6n_minus_6_count():
    pq = edge("p", "q", rz(0.2), [1.0, 0.0, 0.0])
    qr = edge("q", "r", rz(-0.4), [0.0, 2.0, 0.0])
    receipt = reconstruct_from_cocycle(["p", "q", "r"], [pq, qr])
    assert receipt["minimal_tree_edge_count"] == 2
    assert receipt["minimal_continuous_relative_dof"] == 12
    assert receipt["relative_rigid_geometry_reconstructed"] is True
    assert receipt["production_geometry_promoted"] is False


def test_consistent_triangle_closes_holonomy():
    pq = edge("p", "q", rz(0.2), [1.0, 0.0, 0.0])
    qr = edge("q", "r", rz(-0.4), [0.0, 2.0, 0.0])
    pr = compose_edges(pq, qr)
    receipt = reconstruct_from_cocycle(["p", "q", "r"], [pq, qr, pr])
    assert receipt["status"] == "PASS"
    assert receipt["max_path_rotation_defect"] == pytest.approx(0.0, abs=1e-12)
    assert receipt["max_path_translation_defect"] == pytest.approx(0.0, abs=1e-12)


def test_translation_holonomy_mismatch_fails_closed():
    pq = edge("p", "q", np.eye(3), [1.0, 0.0, 0.0])
    qr = edge("q", "r", np.eye(3), [0.0, 1.0, 0.0])
    bad_pr = edge("p", "r", np.eye(3), [1.0, 1.1, 0.0])
    with pytest.raises(ValueError, match="holonomy closure"):
        reconstruct_from_cocycle(["p", "q", "r"], [pq, qr, bad_pr])


def test_rotation_holonomy_mismatch_fails_closed():
    pq = edge("p", "q", rz(0.2), [1.0, 0.0, 0.0])
    qr = edge("q", "r", rz(0.3), [0.0, 1.0, 0.0])
    bad_pr = edge("p", "r", rz(0.8), [0.0, 0.0, 0.0])
    with pytest.raises(ValueError, match="holonomy closure"):
        reconstruct_from_cocycle(["p", "q", "r"], [pq, qr, bad_pr])


def test_disconnected_graph_fails_closed():
    pq = edge("p", "q", np.eye(3), [1.0, 0.0, 0.0])
    with pytest.raises(ValueError, match="disconnected"):
        reconstruct_from_cocycle(["p", "q", "r"], [pq])


def test_duplicate_directed_edge_fails_closed():
    pq1 = edge("p", "q", np.eye(3), [1.0, 0.0, 0.0])
    pq2 = edge("p", "q", np.eye(3), [1.0, 0.0, 0.0])
    with pytest.raises(ValueError, match="duplicate directed edge"):
        reconstruct_from_cocycle(["p", "q"], [pq1, pq2])


def test_reflection_rotation_fails_closed():
    with pytest.raises(ValueError):
        edge("p", "q", np.diag([1.0, 1.0, -1.0]), [0.0, 0.0, 0.0])
