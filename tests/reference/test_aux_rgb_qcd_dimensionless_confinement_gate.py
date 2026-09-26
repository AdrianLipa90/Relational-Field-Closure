import itertools, math
import numpy as np

TOL=1e-9

def haar_su3(rng):
    z=rng.normal(size=(3,3))+1j*rng.normal(size=(3,3))
    q,r=np.linalg.qr(z)
    phases=np.diag(r)/np.abs(np.diag(r))
    q=q@np.diag(np.conj(phases))
    q=q*np.exp(-1j*np.angle(np.linalg.det(q))/3.0)
    return q

def sites(L):
    return list(itertools.product(range(L),repeat=4))

def shift(x,mu,s,L):
    y=list(x); y[mu]=(y[mu]+s)%L
    return tuple(y)

def plaquette(U,x,mu,nu,L):
    return (U[(x,mu)]
            @U[(shift(x,mu,1,L),nu)]
            @U[(shift(x,nu,1,L),mu)].conj().T
            @U[(x,nu)].conj().T)

def wilson_action(U,L,beta):
    s=0.0
    for x in sites(L):
        for mu in range(4):
            for nu in range(mu+1,4):
                s += 1.0-np.trace(plaquette(U,x,mu,nu,L)).real/3.0
    return beta*s

def polyakov(U,L,time_mu=3):
    vals=[]
    for sp in itertools.product(range(L),repeat=3):
        x=(sp[0],sp[1],sp[2],0)
        M=np.eye(3,dtype=complex)
        for _ in range(L):
            M=M@U[(x,time_mu)]
            x=shift(x,time_mu,1,L)
        vals.append(np.trace(M)/3.0)
    return sum(vals)/len(vals)

def center_transform(U,L,z,time_mu=3,t_slice=0):
    V={k:v.copy() for k,v in U.items()}
    for x in sites(L):
        if x[time_mu]==t_slice:
            V[(x,time_mu)]=z*V[(x,time_mu)]
    return V

def euclidean_gammas():
    s1=np.array([[0,1],[1,0]],complex)
    s2=np.array([[0,-1j],[1j,0]],complex)
    s3=np.array([[1,0],[0,-1]],complex)
    z=np.zeros((2,2),complex)
    I=np.eye(2)
    return [np.block([[z,-1j*s],[1j*s,z]]) for s in (s1,s2,s3)] + [np.block([[z,I],[I,z]])]

GAMMA=euclidean_gammas()

def wilson_dirac(U,L,m=0.4,r=1.0,time_mu=3):
    ss=sites(L); si={x:i for i,x in enumerate(ss)}
    D=np.zeros((12*len(ss),12*len(ss)),complex)
    I4=np.eye(4)
    for x in ss:
        ix=12*si[x]
        D[ix:ix+12,ix:ix+12]+=(m+4*r)*np.eye(12)
        for mu in range(4):
            xp=shift(x,mu,1,L); xm=shift(x,mu,-1,L)
            jp=12*si[xp]; jm=12*si[xm]
            sf=-1.0 if (mu==time_mu and x[mu]==L-1) else 1.0
            sb=-1.0 if (mu==time_mu and x[mu]==0) else 1.0
            D[ix:ix+12,jp:jp+12]+=-0.5*sf*np.kron(r*I4-GAMMA[mu],U[(x,mu)])
            D[ix:ix+12,jm:jm+12]+=-0.5*sb*np.kron(r*I4+GAMMA[mu],U[(xm,mu)].conj().T)
    return D

def creutz(W,R,T):
    return -math.log(W(R,T)*W(R+1,T+1)/(W(R+1,T)*W(R,T+1)))

def test_creutz_cancels_perimeter_and_constant_terms():
    sigma,mu,c=0.73,0.21,0.17
    W=lambda R,T: math.exp(-sigma*R*T-mu*(R+T)-c)
    assert abs(creutz(W,2,3)-sigma)<1e-14

    W_perimeter=lambda R,T: math.exp(-mu*(R+T)-c)
    assert abs(creutz(W_perimeter,2,3))<1e-14

def test_pure_yang_mills_center_and_full_qcd_firewall():
    rng=np.random.default_rng(260926)
    L=2; beta=2.84903771431338
    U={(x,mu):haar_su3(rng) for x in sites(L) for mu in range(4)}
    omega=np.exp(2j*np.pi/3)
    V=center_transform(U,L,omega)

    assert abs(wilson_action(U,L,beta)-wilson_action(V,L,beta))<1e-10

    P=polyakov(U,L); P2=polyakov(V,L)
    assert abs(P2-omega*P)<1e-10

    # A fundamental anti-periodic Wilson-Dirac determinant explicitly breaks
    # the pure-gauge Z3 center transformation.
    logdet0=np.linalg.slogdet(wilson_dirac(U,L))[1]
    logdet1=np.linalg.slogdet(wilson_dirac(V,L))[1]
    assert abs(logdet1-logdet0)>1e-6

def test_su3_leading_strong_coupling_dimensionless_area_law_coordinate():
    beta=2.84903771431338
    u=beta/18.0
    sigma_a2=-math.log(u)
    assert 0.0<u<1.0
    assert abs(u-0.15827987301741)<1e-15
    assert abs(sigma_a2-1.8433904647307773)<1e-15
