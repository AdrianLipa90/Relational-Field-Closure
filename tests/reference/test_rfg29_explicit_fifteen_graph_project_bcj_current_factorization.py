import math
from functools import lru_cache
from itertools import permutations
import numpy as np

ETA_A=2.0
ETA=np.diag([1.,-1.,-1.,-1.])
ETAC=ETA.astype(complex)
PERMS=list(permutations([1,2,3]))
GRAPHS=[
 ((1,2),0,(3,4)), ((1,3),0,(2,4)), ((1,4),0,(2,3)),
 ((0,2),1,(3,4)), ((0,3),1,(2,4)), ((0,4),1,(2,3)),
 ((0,1),2,(3,4)), ((0,3),2,(1,4)), ((0,4),2,(1,3)),
 ((0,1),3,(2,4)), ((0,2),3,(1,4)), ((0,4),3,(1,2)),
 ((0,1),4,(2,3)), ((0,2),4,(1,3)), ((0,3),4,(1,2)),
]
B=np.array([
 [-1,0,1,0,0,0], [0,-1,0,0,1,0], [0,0,0,1,0,-1],
 [0,0,1,0,0,0], [0,0,0,0,1,0], [-1,1,0,1,0,-1],
 [1,0,0,0,0,0], [0,0,0,0,0,1], [0,1,-1,1,-1,0],
 [0,1,0,0,0,0], [0,0,0,1,0,0], [1,0,-1,0,-1,1],
 [-1,1,0,0,0,0], [0,0,-1,1,0,0], [0,0,0,0,-1,1],
],dtype=float)
JACOBI=[
 ((0,3,6),(1,-1,1)), ((0,11,14),(1,1,-1)),
 ((1,4,9),(1,-1,1)), ((1,8,13),(1,1,-1)),
 ((2,5,12),(1,-1,1)), ((2,7,10),(1,1,-1)),
 ((3,10,13),(1,-1,1)), ((4,7,14),(1,-1,1)),
 ((5,8,11),(1,-1,1)), ((6,9,12),(1,-1,1)),
]

LAM=[
 np.array([[0,1,0],[1,0,0],[0,0,0]],complex),
 np.array([[0,-1j,0],[1j,0,0],[0,0,0]],complex),
 np.array([[1,0,0],[0,-1,0],[0,0,0]],complex),
 np.array([[0,0,1],[0,0,0],[1,0,0]],complex),
 np.array([[0,0,-1j],[0,0,0],[1j,0,0]],complex),
 np.array([[0,0,0],[0,0,1],[0,1,0]],complex),
 np.array([[0,0,0],[0,0,-1j],[0,1j,0]],complex),
 np.array([[1,0,0],[0,1,0],[0,0,-2]],complex)/math.sqrt(3),
]
T=[x/2 for x in LAM]
FABC=np.zeros((8,8,8))
for a in range(8):
 for b in range(8):
  comm=T[a]@T[b]-T[b]@T[a]
  for c in range(8): FABC[a,b,c]=(-2j*np.trace(T[c]@comm)).real

def dot(a,b): return a@ETA@b
def dotc(a,b): return a@ETAC@b

def graph_color(cols,g):
 (a,b),e,(c,d)=g
 return np.einsum('x,xy,y->',FABC[cols[a],cols[b],:],FABC[:,cols[e],:],FABC[:,cols[c],cols[d]])
def ddm_color(cols,sig):
 s1,s2,s3=sig
 return np.einsum('x,xy,y->',FABC[cols[0],cols[s1],:],FABC[:,cols[s2],:],FABC[:,cols[s3],cols[4]])

def generate_2to3(rng,energy=1.0):
 for _ in range(100):
  v3=rng.normal(size=3);v4=rng.normal(size=3)
  if np.linalg.norm(v3)<1e-5 or np.linalg.norm(v4)<1e-5: continue
  v5=-(v3+v4)
  if np.linalg.norm(v5)<1e-5: continue
  scale=2*energy/(np.linalg.norm(v3)+np.linalg.norm(v4)+np.linalg.norm(v5))
  vs=[scale*v3,scale*v4,scale*v5]
  ps=[np.array([-energy,0.,0.,-energy]),np.array([-energy,0.,0.,energy])]
  ps += [np.r_[np.linalg.norm(v),v] for v in vs]
  if min(abs(dot(ps[i]+ps[j],ps[i]+ps[j])) for i in range(5) for j in range(i+1,5))>1e-5:return ps
 raise RuntimeError

def transverse_basis(p):
 n=p[1:]/np.linalg.norm(p[1:]);ref=np.array([1.,0.,0.])
 if abs(np.dot(n,ref))>0.9:ref=np.array([0.,1.,0.])
 e1=np.cross(n,ref);e1/=np.linalg.norm(e1);e2=np.cross(n,e1);e2/=np.linalg.norm(e2)
 return np.r_[0.,e1],np.r_[0.,e2]
def polarizations(ps,rng):
 out=[]
 for p in ps:
  e1,e2=transverse_basis(p);a,b=rng.normal(size=2);out.append((a*e1+b*e2)/math.sqrt(a*a+b*b))
 return out

def bg_amplitude(ps,es,cdot=dot,binary_scale=math.sqrt(2.0),quartic_scale=1.0):
 n=len(ps);dtype=complex if np.iscomplexobj(ps[0]) or np.iscomplexobj(es[0]) else float
 @lru_cache(None)
 def momentum(seq): return sum((ps[i] for i in seq),np.zeros(4,dtype=dtype))
 @lru_cache(None)
 def current(seq):
  if len(seq)==1:return np.array(es[seq[0]],dtype=dtype)
  return numerator(seq)/cdot(momentum(seq),momentum(seq))
 @lru_cache(None)
 def numerator(seq):
  L=len(seq);out=np.zeros(4,dtype=dtype)
  for k in range(1,L):
   X,Y=seq[:k],seq[k:];JX,JY=current(X),current(Y);kX,kY=momentum(X),momentum(Y);jj=cdot(JX,JY)
   out+=binary_scale*(cdot(kY,JX)*JY+0.5*kX*jj-cdot(kX,JY)*JX-0.5*kY*jj)
  for i in range(1,L-1):
   for j in range(i+1,L):
    X,Y,Z=seq[:i],seq[i:j],seq[j:];JX,JY,JZ=current(X),current(Y),current(Z)
    out+=quartic_scale*(cdot(JX,JZ)*JY-0.5*cdot(JX,JY)*JZ-0.5*cdot(JY,JZ)*JX)
  return out
 return cdot(numerator(tuple(range(n-1))),es[n-1])

def ordered_bg(ps,es,order,cdot=dot):return bg_amplitude([ps[i] for i in order],[es[i] for i in order],cdot=cdot)
def graph_den(ps,g,cdot=dot):
 (a,b),_,(c,d)=g
 return cdot(ps[a]+ps[b],ps[a]+ps[b])*cdot(ps[c]+ps[d],ps[c]+ps[d])

def canonical_numerators(ps,es,cdot=dot):
 A=ETA_A*np.array([ordered_bg(ps,es,[0,*sig,4],cdot=cdot) for sig in PERMS])
 D=np.array([graph_den(ps,g,cdot=cdot) for g in GRAPHS])
 F=B.T@np.diag(1/D)@B
 m=np.linalg.pinv(F,rcond=1e-11)@A
 n=B@m
 return A,D,F,m,n

def br(a,b):return a[0]*b[1]-a[1]*b[0]
def sq(a,b):return a[0]*b[1]-a[1]*b[0]
def mat_to_vec(M):return np.array([(M[0,0]+M[1,1])/2,(M[0,1]+M[1,0])/2,(M[1,0]-M[0,1])/(2j),(M[0,0]-M[1,1])/2],complex)
def ep(lam,til,i,r):return mat_to_vec(np.sqrt(2)*np.outer(lam[r],til[i])/br(lam[r],lam[i]))
def em(lam,til,i,r):return -mat_to_vec(np.sqrt(2)*np.outer(lam[i],til[r])/sq(til[i],til[r]))
def helicity_es(lam,til,neg=(0,2)):
 out=[];n=len(lam)
 for i in range(n):
  cand=[j for j in range(n) if j!=i]
  if i in neg:
   r=max(cand,key=lambda j:abs(sq(til[i],til[j])));out.append(em(lam,til,i,r))
  else:
   r=max(cand,key=lambda j:abs(br(lam[j],lam[i])));out.append(ep(lam,til,i,r))
 return out

def make_base(rng):
 for _ in range(1000):
  vals=[rng.normal(size=2)+1j*rng.normal(size=2) for _ in range(8)]
  l1,chi,l3,l4,l5,t1,t2,t3=vals
  if min(abs(br(l1,chi)),abs(br(l1,l3)),abs(br(l4,l5)))<0.25:continue
  return vals
 raise RuntimeError

def family(eps,base):
 l1,chi,l3,l4,l5,t1,t2,t3=base;lam=[l1,l1+eps*chi,l3,l4,l5];til=[t1,t2,t3]
 M=sum(np.outer(lam[i],til[i]) for i in range(3));X=np.linalg.solve(np.column_stack([lam[3],lam[4]]),-M);til += [X[0],X[1]]
 return lam,til
def ps_from_spin(lam,til):return [mat_to_vec(np.outer(lam[i],til[i])) for i in range(len(lam))]

def factor_current_residue(ps,es):
 def momentum(seq):return sum((ps[i] for i in seq),np.zeros(4,complex))
 def haspair(seq):return 0 in seq and 1 in seq
 def bbr(JX,JY,kX,kY):
  jj=dotc(JX,JY);return math.sqrt(2)*(dotc(kY,JX)*JY+0.5*kX*jj-dotc(kX,JY)*JX-0.5*kY*jj)
 def tbr(JX,JY,JZ):return dotc(JX,JZ)*JY-0.5*dotc(JX,JY)*JZ-0.5*dotc(JY,JZ)*JX
 @lru_cache(None)
 def fincur(seq):
  if len(seq)==1:return np.array(es[seq[0]],complex)
  return finnum(seq)/dotc(momentum(seq),momentum(seq))
 @lru_cache(None)
 def finnum(seq):
  out=np.zeros(4,complex);L=len(seq)
  for k in range(1,L):
   X,Y=seq[:k],seq[k:];out+=bbr(fincur(X),fincur(Y),momentum(X),momentum(Y))
  for i in range(1,L-1):
   for j in range(i+1,L):
    X,Y,Z=seq[:i],seq[i:j],seq[j:];out+=tbr(fincur(X),fincur(Y),fincur(Z))
  return out
 seed=bbr(es[0],es[1],ps[0],ps[1])
 def residue_with_seed(seedx):
  @lru_cache(None)
  def rc(seq):
   if tuple(seq)==(0,1):return seedx
   return rn(seq)/dotc(momentum(seq),momentum(seq))
  @lru_cache(None)
  def rn(seq):
   out=np.zeros(4,complex);L=len(seq)
   for k in range(1,L):
    X,Y=seq[:k],seq[k:]
    if haspair(X):out+=bbr(rc(X),fincur(Y),momentum(X),momentum(Y))
    if haspair(Y):out+=bbr(fincur(X),rc(Y),momentum(X),momentum(Y))
   for i in range(1,L-1):
    for j in range(i+1,L):
     X,Y,Z=seq[:i],seq[i:j],seq[j:]
     if haspair(X):out+=tbr(rc(X),fincur(Y),fincur(Z))
     if haspair(Y):out+=tbr(fincur(X),rc(Y),fincur(Z))
     if haspair(Z):out+=tbr(fincur(X),fincur(Y),rc(Z))
   return out
  return dotc(rn((0,1,2,3)),es[4])
 R=residue_with_seed(seed)
 vals=np.array([residue_with_seed(np.eye(4,dtype=complex)[mu]) for mu in range(4)])
 K=ETAC@vals
 return R,seed,K

def klt_bg_core(ps,es):
 s12=dotc(ps[0]+ps[1],ps[0]+ps[1]);s13=dotc(ps[0]+ps[2],ps[0]+ps[2]);s23=dotc(ps[1]+ps[2],ps[1]+ps[2])
 S=np.array([[s12*(s13+s23),s12*s13],[s12*s13,s13*(s12+s23)]],complex)
 AL=np.array([ordered_bg(ps,es,[0,1,2,3,4],dotc),ordered_bg(ps,es,[0,2,1,3,4],dotc)])
 AR=np.array([ordered_bg(ps,es,[0,1,2,4,3],dotc),ordered_bg(ps,es,[0,2,1,4,3],dotc)])
 return AL@S@AR

def test_color_graphs_have_six_ddm_coordinates_and_nine_independent_jacobi_relations():
 assert np.linalg.matrix_rank(B)==6
 R=[]
 for inds,sgn in JACOBI:
  row=np.zeros(15)
  for i,s in zip(inds,sgn):row[i]=s
  R.append(row)
 assert np.linalg.matrix_rank(np.array(R))==9
 rng=np.random.default_rng(20260929)
 for _ in range(400):
  cols=tuple(int(x) for x in rng.integers(0,8,size=5));C=np.array([ddm_color(cols,s) for s in PERMS])
  for g,brow in zip(GRAPHS,B): assert abs(graph_color(cols,g)-brow@C)<3e-13

def test_canonical_fifteen_graph_numerators_reconstruct_all_six_project_ddm_amplitudes():
 rng=np.random.default_rng(20260930)
 for _ in range(70):
  ps=generate_2to3(rng);es=polarizations(ps,rng);A,D,F,m,n=canonical_numerators(ps,es)
  sv=np.linalg.svd(F,compute_uv=False);assert sv[1]>1e-5 and sv[2]<2e-11*sv[0]
  rec=F@m;assert np.max(abs(rec-A))<3e-10*max(1.,np.max(abs(A)))
  for inds,sgn in JACOBI:assert abs(sum(s*n[i] for i,s in zip(inds,sgn)))<3e-11*max(1.,np.max(abs(n)))

def test_fifteen_graph_color_dressed_sum_equals_ddm_project_sum_and_pseudoinverse_fixes_canonical_gauge():
 rng=np.random.default_rng(20261001)
 for _ in range(40):
  ps=generate_2to3(rng);es=polarizations(ps,rng);A,D,F,m,n=canonical_numerators(ps,es)
  projector=np.linalg.pinv(F,rcond=1e-11)@F
  assert np.linalg.norm((np.eye(6)-projector)@m)<2e-10*max(1.,np.linalg.norm(m))
  for _ in range(4):
   cols=tuple(int(x) for x in rng.integers(0,8,size=5));lhs=sum(ddm_color(cols,s)*A[j] for j,s in enumerate(PERMS));rhs=sum(graph_color(cols,g)*n[i]/D[i] for i,g in enumerate(GRAPHS))
   assert abs(lhs-rhs)<5e-10*max(1.,abs(lhs),abs(rhs))

def test_s12_project_residue_is_carried_by_two_planar_cubic_graphs_and_matches_current_recursion():
 rng=np.random.default_rng(20261002)
 for _ in range(12):
  base=make_base(rng);lam0,til0=family(0.,base);ps0=ps_from_spin(lam0,til0);es0=helicity_es(lam0,til0);Rbg,seed,K=factor_current_residue(ps0,es0);Rproj=ETA_A*Rbg
  lam,til=family(1e-6,base);ps=ps_from_spin(lam,til);es=helicity_es(lam,til);A,D,F,m,n=canonical_numerators(ps,es,cdot=dotc);s12=dotc(ps[0]+ps[1],ps[0]+ps[1])
  s45=dotc(ps[3]+ps[4],ps[3]+ps[4]);s34=dotc(ps[2]+ps[3],ps[2]+ps[3]);Rgraph=n[6]/s45-n[12]/s34
  assert abs(s12*A[0]-Rproj)<2e-4*max(1.,abs(Rproj))
  assert abs(Rgraph-Rproj)<2e-4*max(1.,abs(Rproj))
  assert abs(Rproj-ETA_A*dotc(seed,K))<2e-11*max(1.,abs(Rproj))

def test_three_point_times_four_point_current_factor_is_transverse_on_exact_factorization_surface():
 rng=np.random.default_rng(20261003)
 for _ in range(20):
  lam,til=family(0.,make_base(rng));ps=ps_from_spin(lam,til);es=helicity_es(lam,til);R,seed,K=factor_current_residue(ps,es);P=ps[0]+ps[1]
  assert abs(R-dotc(seed,K))<2e-11*max(1.,abs(R))
  assert abs(dotc(P,seed))<2e-10*max(1.,np.linalg.norm(P)*np.linalg.norm(seed))
  assert abs(dotc(P,K))<2e-10*max(1.,np.linalg.norm(P)*np.linalg.norm(K))

def test_rfg28_rank_one_klt_residue_equals_product_of_two_project_current_residues():
 rng=np.random.default_rng(20261004)
 for _ in range(10):
  base=make_base(rng);lam0,til0=family(0.,base);ps0=ps_from_spin(lam0,til0);es0=helicity_es(lam0,til0)
  RL,_,_=factor_current_residue(ps0,es0);orderR=[0,1,2,4,3];RR,_,_=factor_current_residue([ps0[i] for i in orderR],[es0[i] for i in orderR]);s13=dotc(ps0[0]+ps0[2],ps0[0]+ps0[2]);s23=dotc(ps0[1]+ps0[2],ps0[1]+ps0[2]);pred=(s13+s23)*RL*RR
  lam,til=family(1e-6,base);ps=ps_from_spin(lam,til);es=helicity_es(lam,til);s12=dotc(ps[0]+ps[1],ps[0]+ps[1]);actual=s12*klt_bg_core(ps,es)
  assert abs(actual-pred)<2e-5*max(1.,abs(actual),abs(pred))
  kg=.71;P5=(kg/2)**3;Rphys=(-1j)*P5*pred;Rproject_core=ETA_A**2*pred
  assert abs(Rphys-(-1j/4)*P5*Rproject_core)<2e-13*max(1.,abs(Rphys))
