import math
import numpy as np

TOL=1e-11

def weyl_color_generators():
    w=np.exp(2j*np.pi/3)
    X=np.array([[0,0,1],[1,0,0],[0,1,0]],complex)
    Z=np.diag([1,w,w**2]).astype(complex)
    P=[sum((w**(-b*j))*np.linalg.matrix_power(Z,b) for b in range(3))/3 for j in range(3)]
    E={(k,j):np.linalg.matrix_power(X,(k-j)%3)@P[j] for k in range(3) for j in range(3)}
    L=[
      E[0,1]+E[1,0],
      -1j*(E[0,1]-E[1,0]),
      E[0,0]-E[1,1],
      E[0,2]+E[2,0],
      -1j*(E[0,2]-E[2,0]),
      E[1,2]+E[2,1],
      -1j*(E[1,2]-E[2,1]),
      (E[0,0]+E[1,1]-2*E[2,2])/math.sqrt(3.0),
    ]
    return [a/2 for a in L]

def exp_su3(T,coeff):
    H=sum(float(c)*T[a] for a,c in enumerate(coeff))
    vals,vecs=np.linalg.eigh(H)
    return vecs@np.diag(np.exp(1j*vals))@vecs.conj().T

def test_color_quark_link_covariance():
    rng=np.random.default_rng(260926)
    T=weyl_color_generators()
    max_inv=max_cov=max_adj=max_comm=0.0
    for _ in range(200):
        W=exp_su3(T,rng.normal(size=8))
        Gi=exp_su3(T,rng.normal(size=8))
        Gj=exp_su3(T,rng.normal(size=8))
        qi=rng.normal(size=3)+1j*rng.normal(size=3)
        qj=rng.normal(size=3)+1j*rng.normal(size=3)
        qi/=np.linalg.norm(qi); qj/=np.linalg.norm(qj)

        Wp=Gi@W@Gj.conj().T
        qip=Gi@qi; qjp=Gj@qj

        inv=qi.conj()@W@qj
        invp=qip.conj()@Wp@qjp
        max_inv=max(max_inv,abs(inv-invp))
        max_cov=max(max_cov,np.linalg.norm(Wp@qjp-Gi@(W@qj)))

        J=np.array([(qi.conj()@Ta@qi).real for Ta in T])
        Jp=np.array([(qip.conj()@Ta@qip).real for Ta in T])
        R=np.array([[2*np.trace(T[a]@Gi@T[b]@Gi.conj().T).real
                     for b in range(8)] for a in range(8)])
        max_adj=max(max_adj,np.linalg.norm(Jp-R@J))

        color=np.kron(np.kron(W,np.eye(2)),np.eye(3))
        family=np.kron(np.kron(np.eye(3),np.eye(2)),exp_su3(T,rng.normal(size=8)))
        max_comm=max(max_comm,np.linalg.norm(color@family-family@color))

    assert max_inv<TOL
    assert max_cov<TOL
    assert max_adj<TOL
    assert max_comm<TOL
    CF=sum(t@t for t in T)
    assert np.linalg.norm(CF-(4.0/3.0)*np.eye(3))<TOL
