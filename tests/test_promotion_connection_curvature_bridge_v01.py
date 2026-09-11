import numpy as np
from rfc.promotion_connection_curvature_bridge_v01 import (
    connection_defect, curvature_defect, tangential_normal_split, exact_bridge, STATUS
)


def test_status_fail_closed():
    assert STATUS["promotion_state"] == "CANDIDATE_ONLY"
    assert STATUS["physical_binding"] == "OPEN"
    assert STATUS["canon_write_authority"] is False


def test_exact_intertwiner_zero_defects():
    P = np.vstack([np.eye(2), np.zeros((2,2))]).astype(complex)
    A_old = np.array([[0,1j],[-1j,0]], dtype=complex)
    A_new = np.block([[A_old, np.zeros((2,2))],[np.zeros((2,2)), np.zeros((2,2))]])
    assert np.allclose(connection_defect(P,A_old,A_new), 0.0)
    F_old = A_old @ A_old
    F_new = A_new @ A_new
    assert np.allclose(curvature_defect(P,F_old,F_new), 0.0)
    assert exact_bridge(P,A_old,A_new,F_old,F_new)["accepted"]


def test_tangential_normal_split_reconstructs_connection_defect():
    P = np.vstack([np.eye(2), np.zeros((2,2))]).astype(complex)
    A_old = np.zeros((2,2),dtype=complex)
    A_new = np.zeros((4,4),dtype=complex)
    dP = np.array([[0,0],[0,0],[1,0],[0,1]],dtype=complex)
    par,K = tangential_normal_split(P,A_old,A_new,dP)
    xi = connection_defect(P,A_old,A_new,dP)
    assert np.allclose(P @ par + K, xi)
    assert np.linalg.norm(K) > 0
