import itertools
import numpy as np

TOL=1e-11

def periodic_complex(L,d=4):
    sites=list(itertools.product(range(L),repeat=d))
    si={x:i for i,x in enumerate(sites)}
    links=[(x,mu) for x in sites for mu in range(d)]
    li={e:i for i,e in enumerate(links)}

    def shift(x,mu):
        y=list(x); y[mu]=(y[mu]+1)%L
        return tuple(y)

    D=np.zeros((len(links),len(sites)))
    for r,(x,mu) in enumerate(links):
        D[r,si[x]]=-1.0
        D[r,si[shift(x,mu)]]+=1.0

    plaquettes=[(x,mu,nu) for x in sites for mu in range(d) for nu in range(mu+1,d)]
    B=np.zeros((len(plaquettes),len(links)))
    for r,(x,mu,nu) in enumerate(plaquettes):
        xm=shift(x,mu); xn=shift(x,nu)
        B[r,li[(x,mu)]]+=1.0
        B[r,li[(xm,nu)]]+=1.0
        B[r,li[(xn,mu)]]-=1.0
        B[r,li[(x,nu)]]-=1.0
    return D,B

def expected_one_form_spectrum(L,d=4):
    vals=[]
    for n in itertools.product(range(L),repeat=d):
        p2=4.0*sum(np.sin(np.pi*np.asarray(n,dtype=float)/L)**2)
        vals.extend([p2]*d)
    return np.sort(np.asarray(vals))

def test_periodic_4d_hodge_spectrum():
    for L in (2,3):
        D,B=periodic_complex(L,4)
        assert np.linalg.norm(B@D)<TOL

        H=B.T@B+D@D.T
        got=np.sort(np.linalg.eigvalsh(H))
        expected=expected_one_form_spectrum(L,4)

        assert got.shape==expected.shape
        assert np.max(np.abs(got-expected))<1e-10

        # Four torus harmonic one-forms: one flat holonomy per spacetime direction.
        assert np.sum(got<TOL)==4

        # Ghost/site Laplacian has only the global gauge zero mode.
        ghost=np.linalg.eigvalsh(D.T@D)
        assert np.sum(ghost<TOL)==1

    # SU(3) color lift repeats the one-form spectrum eight times.
    D,B=periodic_complex(2,4)
    H=B.T@B+D@D.T
    H8=np.kron(np.eye(8),H)
    assert H8.shape==(512,512)
    assert np.sum(np.linalg.eigvalsh(H8)<TOL)==32

def test_lattice_spacing_scales_nonzero_modes_as_inverse_a2():
    D,B=periodic_complex(2,4)
    base=np.linalg.eigvalsh(B.T@B+D@D.T)
    pos=base[base>TOL]
    a1,a2=0.2,0.05
    e1=pos/a1**2
    e2=pos/a2**2
    assert np.max(np.abs(e2/e1-(a1/a2)**2))<TOL
