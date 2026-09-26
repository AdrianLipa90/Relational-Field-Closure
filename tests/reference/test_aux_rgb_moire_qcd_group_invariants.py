import math
import numpy as np

TOL=2e-12

def hs(A,B): return float(np.real(np.trace(A.conj().T@B)))

def weyl_generators():
    omega=np.exp(2j*np.pi/3)
    X=np.array([[0,0,1],[1,0,0],[0,1,0]],complex)
    Z=np.diag([1,omega,omega**2]).astype(complex)
    labels=[(0,1,'+'),(0,1,'-'),(1,0,'+'),(1,0,'-'),(1,1,'+'),(1,1,'-'),(1,2,'+'),(1,2,'-')]
    raw=[]
    for a,b,s in labels:
        W=np.linalg.matrix_power(X,a)@np.linalg.matrix_power(Z,b)
        H=(W+W.conj().T)/2 if s=='+' else (W-W.conj().T)/(2j)
        H-=np.trace(H)*np.eye(3)/3
        raw.append(H)
    Q=[]
    for H in raw:
        V=H.copy()
        for U in Q: V-=hs(U,V)*U
        V/=math.sqrt(hs(V,V)); Q.append(V)
    return omega,[U/math.sqrt(2) for U in Q]

def structure_constants(T):
    f=np.zeros((8,8,8))
    for a in range(8):
        for b in range(8):
            C=T[a]@T[b]-T[b]@T[a]
            for c in range(8):
                f[a,b,c]=float(np.real(-2j*np.trace(C@T[c])))
    return f

def test_fundamental_index_TF_is_one_half():
    _,T=weyl_generators()
    gram=np.array([[np.trace(A@B) for B in T] for A in T])
    assert np.max(np.abs(gram-0.5*np.eye(8)))<TOL

def test_fundamental_casimir_CF_is_four_thirds():
    _,T=weyl_generators()
    C=sum(A@A for A in T)
    assert np.max(np.abs(C-(4/3)*np.eye(3)))<TOL

def test_adjoint_casimir_CA_is_three():
    _,T=weyl_generators(); f=structure_constants(T)
    C=np.einsum('acd,bcd->ab',f,f)
    assert np.max(np.abs(C-3*np.eye(8)))<TOL

def test_one_loop_qcd_group_factor_is_standard():
    CA,TF=3.0,0.5
    for nf in range(0,17):
        b0=(11*CA-4*TF*nf)/(12*math.pi)
        expected=(33-2*nf)/(12*math.pi)
        assert abs(b0-expected)<TOL
        assert b0>0
    assert (33-2*17)/(12*math.pi)<0

def test_z3_center_is_invisible_in_adjoint_but_not_fundamental():
    omega,T=weyl_generators(); I=np.eye(3,dtype=complex)
    q=np.array([1.,2.,3.],dtype=complex)
    for k in (0,1,2):
        z=(omega**k)*I
        for A in T:
            assert np.max(np.abs(z@A@z.conj().T-A))<TOL
        if k:
            assert np.linalg.norm(z@q-q)>1e-3
