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

def exp_generator(H,theta=1.0):
    vals,vecs=np.linalg.eigh(H)
    return vecs@np.diag(np.exp(1j*theta*vals))@vecs.conj().T

def adjoint(U):
    return np.array([
        [2.0*np.trace(T[a]@U@T[b]@U.conj().T).real for b in range(8)]
        for a in range(8)
    ])

def principal_log_hermitian(U):
    vals,vecs=np.linalg.eig(U)
    H=vecs@np.diag(np.angle(vals))@np.linalg.inv(vecs)
    H=0.5*(H+H.conj().T)
    return H-np.trace(H)*np.eye(3)/3.0

def ad_matrix(H):
    M=np.zeros((8,8),float)
    for b in range(8):
        C=H@T[b]-T[b]@H
        for a in range(8):
            M[a,b]=(-2j*np.trace(T[a]@C)).real
    return M

def covariant_laplacian(L,links):
    sites=list(itertools.product(range(L),repeat=4))
    si={x:i for i,x in enumerate(sites)}
    N=len(sites); n=8*N
    out=np.zeros((n,n),float); I=np.eye(n)
    def shift(x,mu):
        y=list(x); y[mu]=(y[mu]+1)%L
        return tuple(y)
    for mu,U in enumerate(links):
        R=adjoint(U)
        S=np.zeros((n,n),float)
        for x in sites:
            i=8*si[x]; j=8*si[shift(x,mu)]
            S[i:i+8,j:j+8]=R
        out += 2.0*I-S-S.T
    return out,N

def vector_operator(L,links):
    Lap,N=covariant_laplacian(L,links)
    P=links[0]@links[1]@links[0].conj().T@links[1].conj().T
    Fxy=principal_log_hermitian(P)
    M=ad_matrix(Fxy)
    assert np.linalg.norm(M+M.T)<TOL

    block=8*N
    Delta=np.kron(np.eye(4),Lap)
    C=-2.0*np.kron(np.eye(N),M)
    Delta[0:block,block:2*block]+=C
    Delta[block:2*block,0:block]+=C.T
    return Delta,P

def test_background_vector_hessian_and_instability_witness():
    I3=np.eye(3,dtype=complex)
    theta=0.20
    bg=[exp_generator(T[0],theta),exp_generator(T[1],theta),I3,I3]

    Delta,P=vector_operator(2,bg)
    assert np.linalg.norm(Delta-Delta.T)<TOL
    assert 3.0-np.trace(P).real>1e-7

    vals=np.linalg.eigvalsh(Delta)
    assert np.sum(vals<-1e-9)==6
    assert np.sum(np.abs(vals)<1e-9)==4

    # The selected constant noncommuting background is therefore not
    # admitted as a stable real-logdet RG extraction surface.
    assert np.min(vals)<0.0

    G=exp_generator(T[3]+0.3*T[7],0.51)
    bg2=[G@U@G.conj().T for U in bg]
    Delta2,_=vector_operator(2,bg2)
    assert np.max(np.abs(np.linalg.eigvalsh(Delta)-np.linalg.eigvalsh(Delta2)))<1e-10
