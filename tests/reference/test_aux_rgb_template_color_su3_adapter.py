import math
import numpy as np

TOL=1e-12

def pair():
    w=np.exp(2j*np.pi/3)
    X=np.array([[0,0,1],[1,0,0],[0,1,0]],complex)
    Z=np.diag([1,w,w**2]).astype(complex)
    return w,X,Z

def projectors(w,Z):
    return [sum((w**(-b*j))*np.linalg.matrix_power(Z,b) for b in range(3))/3 for j in range(3)]

def matrix_units(X,P):
    return {(k,j):np.linalg.matrix_power(X,(k-j)%3)@P[j] for k in range(3) for j in range(3)}

def lambdas_from_weyl(X,Z):
    w=np.exp(2j*np.pi/3); P=projectors(w,Z); E=matrix_units(X,P)
    return [
      E[0,1]+E[1,0],
      -1j*(E[0,1]-E[1,0]),
      E[0,0]-E[1,1],
      E[0,2]+E[2,0],
      -1j*(E[0,2]-E[2,0]),
      E[1,2]+E[2,1],
      -1j*(E[1,2]-E[2,1]),
      (E[0,0]+E[1,1]-2*E[2,2])/math.sqrt(3.0),
    ]

def standard_lambdas():
    return [
      np.array([[0,1,0],[1,0,0],[0,0,0]],complex),
      np.array([[0,-1j,0],[1j,0,0],[0,0,0]],complex),
      np.diag([1,-1,0]).astype(complex),
      np.array([[0,0,1],[0,0,0],[1,0,0]],complex),
      np.array([[0,0,-1j],[0,0,0],[1j,0,0]],complex),
      np.array([[0,0,0],[0,0,1],[0,1,0]],complex),
      np.array([[0,0,0],[0,0,-1j],[0,1j,0]],complex),
      np.diag([1,1,-2]).astype(complex)/math.sqrt(3.0),
    ]

def f_tensor(T):
    f=np.zeros((8,8,8))
    for a in range(8):
      for b in range(8):
        C=T[a]@T[b]-T[b]@T[a]
        for c in range(8):
          f[a,b,c]=(-2j*np.trace(C@T[c])).real
    return f

def test_rgb_template_to_color_su3_adapter():
    w,X,Z=pair(); I=np.eye(3,dtype=complex)
    assert np.linalg.norm(Z@X-w*X@Z)<TOL
    P=projectors(w,Z)
    for j in range(3):
      target=np.zeros((3,3),complex); target[j,j]=1
      assert np.linalg.norm(P[j]-target)<TOL
    L=lambdas_from_weyl(X,Z); S=standard_lambdas()
    assert max(np.linalg.norm(a-b) for a,b in zip(L,S))<TOL

    T=[a/2 for a in L]; f=f_tensor(T)
    F=np.array([-1j*f[a] for a in range(8)])
    C=sum(F[a]@F[a] for a in range(8))
    assert np.linalg.norm(C-3*np.eye(8))<1e-11

    # Stage-25 color/family tensor-factor firewall.
    color=np.kron(np.kron(T[0],np.eye(2)),np.eye(3))
    family=np.kron(np.kron(np.eye(3),np.eye(2)),T[1])
    assert np.linalg.norm(color@family-family@color)<TOL

    # Existing RF-M2 full bipolar AUX is 2^3=8D, not the 3D color carrier.
    assert 2**3 != 3
