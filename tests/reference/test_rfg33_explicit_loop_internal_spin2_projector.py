import numpy as np

# single-line tensor-product helicity basis: ++,+-,-+,--
P2=np.diag([1.,0.,0.,1.])
Q0=np.eye(4)-P2
# two-line cut basis induced by one-copy assignments A=(+,-), B=(-,+): AA,AB,BA,BB
PCUT=np.diag([1.,0.,0.,1.])
QCUT=np.eye(4)-PCUT

def ang(a,b): return a[0]*b[1]-a[1]*b[0]
def pt4(lams,neg):
 num=ang(lams[neg[0]],lams[neg[1]])**4;den=1+0j
 for i in range(4): den*=ang(lams[i],lams[(i+1)%4])
 return num/den

def make_external(rng):
 for _ in range(1000):
  lam=[rng.normal(size=2)+1j*rng.normal(size=2) for _ in range(4)]
  til=[rng.normal(size=2)+1j*rng.normal(size=2) for _ in range(2)]
  L=np.column_stack([lam[2],lam[3]])
  if abs(np.linalg.det(L))<0.2: continue
  M=sum(np.outer(lam[i],til[i]) for i in range(2));X=np.linalg.solve(L,-M);til += [X[0],X[1]]
  if min(abs(ang(lam[i],lam[j])) for i in range(4) for j in range(i+1,4))<0.05: continue
  return lam,til
 raise RuntimeError

def make_t_cut(lam,til,rng):
 q=np.outer(lam[0],til[0])+np.outer(lam[2],til[2])
 for _ in range(200):
  la=rng.normal(size=2)+1j*rng.normal(size=2);lb=rng.normal(size=2)+1j*rng.normal(size=2);L=np.column_stack([la,lb])
  if abs(np.linalg.det(L))<0.2: continue
  X=np.linalg.solve(L,q);ta,tb=X[0],X[1]
  left=[lam[0],lam[2],-la,-lb];right=[lam[1],lam[3],la,lb]
  if min(min(abs(ang(left[i],left[(i+1)%4])) for i in range(4)),min(abs(ang(right[i],right[(i+1)%4])) for i in range(4)))<0.03:continue
  return left,right
 raise RuntimeError
ASSIGN=((+1,-1),(-1,+1))
def one_copy(cut,a):
 left,right=cut;h1,h2=a
 lh=(-1,+1,-h1,-h2);rh=(-1,+1,h1,h2)
 nL=tuple(i for i,h in enumerate(lh) if h==-1);nR=tuple(i for i,h in enumerate(rh) if h==-1)
 return pt4(left,nL)*pt4(right,nR)

def state_vector(xA,xB): return np.array([xA*xA,xA*xB,xB*xA,xB*xB],complex)

def test_single_line_spin2_projector_is_hermitian_idempotent_rank_two():
 assert np.allclose(P2.conj().T,P2);assert np.allclose(P2@P2,P2)
 assert np.linalg.matrix_rank(P2)==2 and np.trace(P2)==2

def test_complement_is_orthogonal_and_complete():
 assert np.allclose(Q0@Q0,Q0);assert np.allclose(P2@Q0,0);assert np.allclose(P2+Q0,np.eye(4))
 assert np.linalg.matrix_rank(Q0)==2

def test_two_particle_projector_selects_matched_double_copy_assignments_only():
 e=np.eye(4)
 assert np.allclose(PCUT@e[0],e[0]);assert np.allclose(PCUT@e[3],e[3])
 assert np.allclose(PCUT@e[1],0);assert np.allclose(PCUT@e[2],0)

def test_projected_cut_equals_spin2_sector_on_generic_rfg32_kinematics():
 rng=np.random.default_rng(3301)
 for _ in range(100):
  lam,til=make_external(rng);cut=make_t_cut(lam,til,rng);xA=one_copy(cut,ASSIGN[0]);xB=one_copy(cut,ASSIGN[1]);v=state_vector(xA,xB)
  projected=np.sum(PCUT@v);expected=xA*xA+xB*xB
  assert abs(projected-expected)<2e-13*max(1.,abs(expected))

def test_projector_subtraction_is_exactly_the_rfg32_mixed_sector():
 rng=np.random.default_rng(3302)
 for _ in range(100):
  lam,til=make_external(rng);cut=make_t_cut(lam,til,rng);xA=one_copy(cut,ASSIGN[0]);xB=one_copy(cut,ASSIGN[1]);v=state_vector(xA,xB)
  raw=np.sum(v);proj=np.sum(PCUT@v);removed=np.sum(QCUT@v)
  scale=max(1.,abs(raw),abs(proj),abs(removed))
  assert abs(raw-proj-removed)<2e-13*scale
  assert abs(removed-2*xA*xB)<2e-13*scale

def test_projected_cut_is_copy_exchange_invariant_and_generic_raw_cut_is_changed():
 rng=np.random.default_rng(3303);witness=0
 X=np.array([[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]],float)
 assert np.allclose(X@PCUT@X,PCUT)
 for _ in range(80):
  lam,til=make_external(rng);cut=make_t_cut(lam,til,rng);xA=one_copy(cut,ASSIGN[0]);xB=one_copy(cut,ASSIGN[1]);v=state_vector(xA,xB)
  proj=np.sum(PCUT@v);projswap=np.sum(PCUT@(X@v));raw=np.sum(v)
  assert abs(proj-projswap)<2e-13*max(1.,abs(proj))
  if abs(raw-proj)>1e-8*max(1.,abs(raw),abs(proj)):witness+=1
 assert witness>=70
