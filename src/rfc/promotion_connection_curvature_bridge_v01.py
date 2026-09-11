from __future__ import annotations
import numpy as np

STATUS = {
    "promotion_state": "CANDIDATE_ONLY",
    "physical_binding": "OPEN",
    "canon_write_authority": False,
    "epistemic": "CHYBA",
}


def connection_defect(P, A_old, A_new, dP=None):
    P = np.asarray(P, dtype=complex)
    dP = np.zeros_like(P) if dP is None else np.asarray(dP, dtype=complex)
    return dP + np.asarray(A_new, dtype=complex) @ P - P @ np.asarray(A_old, dtype=complex)


def curvature_defect(P, F_old, F_new):
    P = np.asarray(P, dtype=complex)
    return np.asarray(F_new, dtype=complex) @ P - P @ np.asarray(F_old, dtype=complex)


def tangential_normal_split(P, A_old, A_new, dP=None):
    P = np.asarray(P, dtype=complex)
    dP = np.zeros_like(P) if dP is None else np.asarray(dP, dtype=complex)
    Pi = P @ P.conj().T
    Q = np.eye(P.shape[0], dtype=complex) - Pi
    transport = dP + np.asarray(A_new, dtype=complex) @ P
    xi_parallel = P.conj().T @ transport - np.asarray(A_old, dtype=complex)
    K = Q @ transport
    return xi_parallel, K


def exact_bridge(P, A_old, A_new, F_old=None, F_new=None, dP=None, atol=1e-10):
    xi = connection_defect(P, A_old, A_new, dP=dP)
    out = {"connection": bool(np.allclose(xi, 0.0, atol=atol))}
    if F_old is not None and F_new is not None:
        df = curvature_defect(P, F_old, F_new)
        out["curvature"] = bool(np.allclose(df, 0.0, atol=atol))
    out["accepted"] = all(out.values())
    return out
