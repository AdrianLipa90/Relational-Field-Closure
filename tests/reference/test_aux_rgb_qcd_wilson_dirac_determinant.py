import itertools, math
import numpy as np

TOL=1e-10

def euclidean_gammas():
    s1=np.array([[0,1],[1,0]],complex)
    s2=np.array([[0,-1j],[1j,0]],complex)
    s3=np.array([[1,0],[0,-1]],complex)
    z=np.zeros((2,2),complex); I=np.eye(2)
    out=[np.block([[z,-1j*s],[1j*s,z]]) for s in (s1,s2,s3)]
    out.append(np.block([[z,I],[I,z]]))
    return out

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

GAMMA=euclidean_gammas()
T=generators()

def exp_generator(H,theta=1.0):
    vals,vecs=np.linalg.eigh(H)
    return vecs@np.diag(np.exp(1j*theta*vals))@vecs.conj().T

def lattice(L):
    sites=list(itertools.product(range(L),repeat=4))
    si={x:i for i,x in enumerate(sites)}
    def shift(x,mu,sgn=1):
        y=list(x); y[mu]=(y[mu]+sgn)%L
        return tuple(y)
    return sites,si,shift

def wilson_dirac(L,links,m=0.4,r=1.0):
    sites,si,shift=lattice(L)
    I4=np.eye(4)
    n=12*len(sites)
    D=np.zeros((n,n),complex)
    for x in sites:
        ix=12*si[x]
        D[ix:ix+12,ix:ix+12]+=(m+4.0*r)*np.eye(12)
        for mu in range(4):
            xp=shift(x,mu,+1); xm=shift(x,mu,-1)
            jp=12*si[xp]; jm=12*si[xm]
            Uf=links[(x,mu)]
            Ub=links[(xm,mu)].conj().T
            D[ix:ix+12,jp:jp+12]+=-0.5*np.kron(r*I4-GAMMA[mu],Uf)
            D[ix:ix+12,jm:jm+12]+=-0.5*np.kron(r*I4+GAMMA[mu],Ub)
    return D

def test_wilson_dirac_background_and_local_gauge_covariance():
    for mu in range(4):
        assert np.linalg.norm(GAMMA[mu]-GAMMA[mu].conj().T)<TOL
        for nu in range(4):
            target=2.0*np.eye(4) if mu==nu else np.zeros((4,4))
            assert np.linalg.norm(GAMMA[mu]@GAMMA[nu]+GAMMA[nu]@GAMMA[mu]-target)<TOL

    L=2
    sites,si,shift=lattice(L)
    I3=np.eye(3,dtype=complex)
    theta=0.37
    Uconst=[exp_generator(T[0],theta),exp_generator(T[1],theta),I3,I3]
    links={(x,mu):Uconst[mu] for x in sites for mu in range(4)}
    trivial={(x,mu):I3 for x in sites for mu in range(4)}

    Db=wilson_dirac(L,links)
    D0=wilson_dirac(L,trivial)

    signb,logb=np.linalg.slogdet(Db)
    sign0,log0=np.linalg.slogdet(D0)
    assert abs(logb-log0)>1e-3

    rng=np.random.default_rng(260926)
    local_G={}
    for x in sites:
        H=sum(float(c)*T[a] for a,c in enumerate(rng.normal(scale=0.2,size=8)))
        local_G[x]=exp_generator(H)

    transformed={}
    for x in sites:
        for mu in range(4):
            transformed[(x,mu)]=local_G[x]@links[(x,mu)]@local_G[shift(x,mu)].conj().T

    D2=wilson_dirac(L,transformed)
    BIG=np.zeros_like(Db)
    for x in sites:
        i=12*si[x]
        BIG[i:i+12,i:i+12]=np.kron(np.eye(4),local_G[x])

    assert np.linalg.norm(D2-BIG@Db@BIG.conj().T)<1e-10
    assert abs(np.linalg.slogdet(D2)[1]-logb)<1e-10
