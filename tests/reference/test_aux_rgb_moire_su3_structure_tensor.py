import math
import numpy as np

TOL = 2e-12

def rgb_weyl_pair():
    omega = np.exp(2j * np.pi / 3)
    X = np.array([[0,0,1],[1,0,0],[0,1,0]], dtype=complex)
    Z = np.diag([1.0, omega, omega**2]).astype(complex)
    return omega, X, Z

def hs(A, B):
    return float(np.real(np.trace(A.conj().T @ B)))

def weyl_su3_basis():
    _, X, Z = rgb_weyl_pair()
    labels = [(0,1,'+'),(0,1,'-'),(1,0,'+'),(1,0,'-'),
              (1,1,'+'),(1,1,'-'),(1,2,'+'),(1,2,'-')]
    raw = []
    for a,b,sign in labels:
        W = np.linalg.matrix_power(X,a) @ np.linalg.matrix_power(Z,b)
        H = (W + W.conj().T)/2 if sign == '+' else (W - W.conj().T)/(2j)
        H = H - np.trace(H)*np.eye(3)/3
        raw.append(H)
    ortho = []
    for H in raw:
        V = H.copy()
        for Q in ortho:
            V -= hs(Q,V)*Q
        V /= math.sqrt(hs(V,V))
        ortho.append(V)
    return labels, [H/math.sqrt(2) for H in ortho]

def gell_mann_basis():
    lam = [
        np.array([[0,1,0],[1,0,0],[0,0,0]], complex),
        np.array([[0,-1j,0],[1j,0,0],[0,0,0]], complex),
        np.diag([1,-1,0]).astype(complex),
        np.array([[0,0,1],[0,0,0],[1,0,0]], complex),
        np.array([[0,0,-1j],[0,0,0],[1j,0,0]], complex),
        np.array([[0,0,0],[0,0,1],[0,1,0]], complex),
        np.array([[0,0,0],[0,0,-1j],[0,1j,0]], complex),
        np.diag([1,1,-2]).astype(complex)/math.sqrt(3),
    ]
    return [L/2 for L in lam]

def structure_constants(B):
    f = np.zeros((8,8,8))
    for a in range(8):
        for b in range(8):
            comm = B[a]@B[b] - B[b]@B[a]
            for c in range(8):
                f[a,b,c] = float(np.real(-2j*np.trace(comm@B[c])))
    return f

def intertwiner(E, G):
    return np.array([[2*hs(EA,Ga) for Ga in G] for EA in E])

def test_weyl_relation_and_standard_normalization():
    omega,X,Z = rgb_weyl_pair()
    _,E = weyl_su3_basis()
    assert np.max(np.abs(Z@X - omega*X@Z)) < TOL
    gram = np.array([[hs(A,B) for B in E] for A in E])
    assert np.max(np.abs(gram - 0.5*np.eye(8))) < TOL

def test_weyl_gell_mann_intertwiner_is_orthogonal():
    _,E = weyl_su3_basis(); G = gell_mann_basis()
    O = intertwiner(E,G)
    assert np.max(np.abs(O@O.T - np.eye(8))) < TOL
    assert np.max(np.abs(O.T@O - np.eye(8))) < TOL

def test_full_structure_tensor_matches_under_intertwiner():
    _,E = weyl_su3_basis(); G = gell_mann_basis(); O = intertwiner(E,G)
    fE = structure_constants(E); fG = structure_constants(G)
    transported = np.einsum('Aa,Bb,Cc,abc->ABC', O,O,O,fG)
    assert np.max(np.abs(fE-transported)) < TOL

def test_adjoint_eight_representation_intertwines():
    _,E = weyl_su3_basis(); G = gell_mann_basis(); O = intertwiner(E,G)
    fE = structure_constants(E); fG = structure_constants(G)
    adE = np.array([fE[a] for a in range(8)])
    adG = np.array([fG[a] for a in range(8)])
    pred = np.array([sum(O[A,a]*(O@adG[a]@O.T) for a in range(8)) for A in range(8)])
    assert np.max(np.abs(adE-pred)) < TOL

def test_adjoint_casimir_is_su3_value_three():
    _,E = weyl_su3_basis(); fE = structure_constants(E)
    adE = np.array([fE[a] for a in range(8)])
    C_A = sum(A@A.T for A in adE)
    assert np.max(np.abs(C_A - 3.0*np.eye(8))) < TOL
