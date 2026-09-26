import math
import numpy as np

TOL = 1e-12

def rgb_weyl_pair():
    omega = np.exp(2j * np.pi / 3)
    X = np.array([[0,0,1],[1,0,0],[0,1,0]], dtype=complex)
    Z = np.diag([1.0, omega, omega**2]).astype(complex)
    return omega, X, Z

def realvec(A):
    return np.concatenate([A.real.reshape(-1), A.imag.reshape(-1)])

def gell_mann():
    return [
        np.array([[0,1,0],[1,0,0],[0,0,0]], complex),
        np.array([[0,-1j,0],[1j,0,0],[0,0,0]], complex),
        np.diag([1,-1,0]).astype(complex),
        np.array([[0,0,1],[0,0,0],[1,0,0]], complex),
        np.array([[0,0,-1j],[0,0,0],[1j,0,0]], complex),
        np.array([[0,0,0],[0,0,1],[0,1,0]], complex),
        np.array([[0,0,0],[0,0,-1j],[0,1j,0]], complex),
        np.diag([1,1,-2]).astype(complex) / math.sqrt(3.0),
    ]

def weyl_hermitian_sector(X, Z):
    out = []
    for a in range(3):
        for b in range(3):
            if (a,b) == (0,0):
                continue
            W = np.linalg.matrix_power(X,a) @ np.linalg.matrix_power(Z,b)
            for H in ((W+W.conj().T)/2.0, (W-W.conj().T)/(2.0j)):
                H = H - np.trace(H)*np.eye(3)/3.0
                if np.linalg.norm(H) > TOL:
                    out.append(H)
    return out

def test_aux_rgb_moire_weyl_su3_bridge():
    omega, X, Z = rgb_weyl_pair()
    I = np.eye(3, dtype=complex)

    assert abs(1 + omega + omega**2) < TOL
    assert np.linalg.norm(X@X@X-I) < TOL
    assert np.linalg.norm(Z@Z@Z-I) < TOL
    assert np.linalg.norm(Z@X-omega*X@Z) < TOL
    assert np.linalg.norm(X@Z-Z@X) > 1.0

    ops = [np.linalg.matrix_power(X,a) @ np.linalg.matrix_power(Z,b)
           for a in range(3) for b in range(3)]
    assert np.linalg.matrix_rank(np.stack([A.reshape(-1) for A in ops],axis=1), tol=TOL) == 9

    H = weyl_hermitian_sector(X,Z)
    Wspan = np.stack([realvec(A) for A in H],axis=1)
    Gspan = np.stack([realvec(A) for A in gell_mann()],axis=1)
    assert np.linalg.matrix_rank(Wspan,tol=TOL) == 8
    assert np.linalg.matrix_rank(Gspan,tol=TOL) == 8
    assert np.linalg.matrix_rank(np.concatenate([Wspan,Gspan],axis=1),tol=TOL) == 8

    for A in [I,Z,Z@Z]:
        for B in [I,Z,Z@Z]:
            assert np.linalg.norm(A@B-B@A) < TOL
