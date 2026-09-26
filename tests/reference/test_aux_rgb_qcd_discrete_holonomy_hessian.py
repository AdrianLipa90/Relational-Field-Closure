import numpy as np

TOL=1e-12

def square_incidence():
    # Four oriented edges around one square: 0->1->2->3->0.
    return np.array([
        [-1., 1., 0., 0.],
        [ 0.,-1., 1., 0.],
        [ 0., 0.,-1., 1.],
        [ 1., 0., 0.,-1.],
    ])

def test_discrete_background_hessian_and_gauge_quotient():
    D=square_incidence()                 # links x sites
    B=np.ones((1,4),dtype=float)         # plaquette boundary acting on links
    assert np.linalg.norm(B@D)<TOL       # boundary of boundary = 0

    Cp=2.0
    xi=1.0

    # S_W^(2)=(Cp/4)||BA||^2 -> Hessian=(Cp/2) B^T B.
    Hphys=(Cp/2.0)*(B.T@B)
    assert np.linalg.matrix_rank(Hphys,tol=TOL)==1

    # Pure gauge link directions A=D theta are exact zero modes.
    assert np.linalg.norm(Hphys@D)<TOL

    # Gauge-fixing S_gf=(1/2xi)||D^T A||^2.
    Hgf=Hphys+(1.0/xi)*(D@D.T)
    assert np.linalg.matrix_rank(Hgf,tol=TOL)==4
    assert np.min(np.linalg.eigvalsh(Hgf))>0.0

    # FP/ghost operator is the site graph Laplacian. Its only zero mode
    # is the global gauge rotation on this connected plaquette.
    Lgh=D.T@D
    vals=np.linalg.eigvalsh(Lgh)
    assert np.sum(vals<TOL)==1
    assert np.allclose(vals[1:],[2.,2.,4.],atol=TOL)

    # Eight SU(3) color directions decouple at quadratic order.
    H8=np.kron(np.eye(8),Hgf)
    assert H8.shape==(32,32)
    assert np.linalg.matrix_rank(H8,tol=TOL)==32

    # Gauge-invariant physical Hessian remains transverse to gauge directions.
    for a in range(8):
        v=np.zeros(32)
        theta=np.array([0.3,-0.2,0.7,-0.8])
        v[4*a:4*a+4]=D@theta
        Hp8=np.kron(np.eye(8),Hphys)
        assert np.linalg.norm(Hp8@v)<TOL
