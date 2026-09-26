import itertools, math
import numpy as np

TOL=1e-10

def generators():
    L=[
      np.array([[0,1,0],[1,0,0],[0,0,0]],complex),
      np.array([[0,-1j,0],[1j,0,0],[0,0,0]],complex),
      np.diag([1,-1,0]).astype(complex),
      np.array([[0,0,1],[0,0,0],[1,0,0]],complex),
      np.array([[0,0,-1j],[0,0,0],[1j,0,0]],complex),
      np.array([[0,0,0],[0,0,1],[0,1,0]],complex),
      np.array([[0,0,0],[0,0,-1j],[0,1j,0]],complex),
      np.diag([1,1,-2]).astype(complex)/math.sqrt(3.0),
    ]
    return [x/2.0 for x in L]

T=generators()

def exp_generator(H,theta):
    vals,vecs=np.linalg.eigh(H)
    return vecs@np.diag(np.exp(1j*theta*vals))@vecs.conj().T

def adjoint(U):
    return np.array([
        [2.0*np.trace(T[a]@U@T[b]@U.conj().T).real for b in range(8)]
        for a in range(8)
    ])

def covariant_site_laplacian(L,links):
    sites=list(itertools.product(range(L),repeat=4))
    si={x:i for i,x in enumerate(sites)}
    n=8*len(sites)
    Delta=np.zeros((n,n),float)
    I=np.eye(n)

    def shift(x,mu):
        y=list(x); y[mu]=(y[mu]+1)%L
        return tuple(y)

    for mu,U in enumerate(links):
        R=adjoint(U)
        assert np.linalg.norm(R.T@R-np.eye(8))<TOL
        S=np.zeros((n,n),float)
        for x in sites:
            xp=shift(x,mu)
            i,j=8*si[x],8*si[xp]
            S[i:i+8,j:j+8]=R
        Delta += 2.0*I-S-S.T
    return Delta

def log_pdet(A):
    vals=np.linalg.eigvalsh(A)
    pos=vals[vals>TOL]
    return float(np.log(pos).sum()), int(np.sum(vals<=TOL))

def test_background_adjoint_ghost_spectrum():
    I3=np.eye(3,dtype=complex)
    theta=0.37
    Ux=exp_generator(T[0],theta)
    Uy=exp_generator(T[1],theta)
    bg=[Ux,Uy,I3,I3]

    trivial=covariant_site_laplacian(2,[I3]*4)
    back=covariant_site_laplacian(2,bg)

    lp0,z0=log_pdet(trivial)
    lpb,zb=log_pdet(back)

    # Trivial background has eight global adjoint zero modes.
    assert z0==8

    # Noncommuting T1/T2 holonomies leave only the common centralizer direction.
    assert zb==1

    # The FP/adjoint determinant is genuinely background sensitive.
    assert abs(lpb-lp0)>1.0

    P=Ux@Uy@Ux.conj().T@Uy.conj().T
    defect=3.0-np.trace(P).real
    assert defect>1e-6
    assert np.linalg.norm(P.conj().T@P-I3)<TOL
    assert abs(np.linalg.det(P)-1.0)<TOL

    # Global color-basis conjugation leaves the spectrum invariant.
    G=exp_generator(T[3]+0.3*T[7],0.51)
    conjugated=[G@U@G.conj().T for U in bg]
    back2=covariant_site_laplacian(2,conjugated)
    assert np.max(np.abs(
        np.linalg.eigvalsh(back)-np.linalg.eigvalsh(back2)
    ))<1e-10
