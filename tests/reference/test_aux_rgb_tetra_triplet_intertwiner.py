import numpy as np

TOL=2e-12

def test_tetrahedral_opposite_face_cycle_equals_aux_orbital_shift():
    v0=np.array([1.,1.,1.])
    v1=np.array([1.,-1.,-1.])
    v2=np.array([-1.,1.,-1.])
    v3=np.array([-1.,-1.,1.])
    P3=np.array([[0.,0.,1.],[1.,0.,0.],[0.,1.,0.]])
    assert np.max(np.abs(P3@v0-v0))<TOL
    assert np.max(np.abs(P3@v1-v2))<TOL
    assert np.max(np.abs(P3@v2-v3))<TOL
    assert np.max(np.abs(P3@v3-v1))<TOL
    assert np.max(np.abs(P3@P3@P3-np.eye(3)))<TOL
    assert abs(np.linalg.det(P3)-1.0)<TOL

def test_rotation_is_120_degrees_about_v0_axis():
    P3=np.array([[0.,0.,1.],[1.,0.,0.],[0.,1.,0.]])
    theta=np.arccos((np.trace(P3)-1.0)/2.0)
    assert abs(theta-2*np.pi/3)<TOL

def test_f3_character_basis_is_aux_rgb_clock_up_to_orientation():
    omega=np.exp(2j*np.pi/3)
    P3=np.array([[0,0,1],[1,0,0],[0,1,0]],complex)
    F3=np.array([[1,1,1],[1,omega,omega**2],[1,omega**2,omega]],complex)/np.sqrt(3)
    Zrgb=np.diag([1.,omega,omega**2]).astype(complex)
    D=F3.conj().T@P3@F3
    assert np.max(np.abs(D-Zrgb.conj().T))<TOL

def test_anchored_rgb_to_tetra_triplet_intertwiner():
    Xrgb=np.array([[0.,0.,1.],[1.,0.,0.],[0.,1.,0.]])
    Pcolor=Xrgb.copy()
    M=np.eye(3)
    assert np.max(np.abs(M@Xrgb-Pcolor@M))<TOL
