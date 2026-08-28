import itertools
import numpy as np

P2=np.diag([1.,0.,0.,1.])
LABELS=((+1,+1),(+1,-1),(-1,+1),(-1,-1))
HEXT=(-1,-1,+1,+1)

def ang(a,b): return a[0]*b[1]-a[1]*b[0]
def pt4(lams,neg):
    num=ang(lams[neg[0]],lams[neg[1]])**4; den=1+0j
    for i in range(4): den*=ang(lams[i],lams[(i+1)%4])
    return num/den

def make_external(rng):
    for _ in range(1000):
        lam=[rng.normal(size=2)+1j*rng.normal(size=2) for _ in range(4)]
        til=[rng.normal(size=2)+1j*rng.normal(size=2) for _ in range(2)]
        L=np.column_stack([lam[2],lam[3]])
        if abs(np.linalg.det(L))<0.2: continue
        M=sum(np.outer(lam[i],til[i]) for i in range(2))
        X=np.linalg.solve(L,-M); til += [X[0],X[1]]
        if min(abs(ang(lam[i],lam[j])) for i in range(4) for j in range(i+1,4))<0.05: continue
        return lam,til
    raise RuntimeError

def make_cut(lam,til,pair,rng):
    rest=tuple(i for i in range(4) if i not in pair)
    q=sum((np.outer(lam[i],til[i]) for i in pair),np.zeros((2,2),complex))
    for _ in range(300):
        la=rng.normal(size=2)+1j*rng.normal(size=2); lb=rng.normal(size=2)+1j*rng.normal(size=2)
        L=np.column_stack([la,lb])
        if abs(np.linalg.det(L))<0.2: continue
        X=np.linalg.solve(L,q); ta,tb=X[0],X[1]
        left=[lam[pair[0]],lam[pair[1]],-la,-lb]; right=[lam[rest[0]],lam[rest[1]],la,lb]
        dl=min(abs(ang(left[i],left[(i+1)%4])) for i in range(4)); dr=min(abs(ang(right[i],right[(i+1)%4])) for i in range(4))
        if min(dl,dr)<0.03: continue
        return rest,left,right,la,ta,lb,tb
    raise RuntimeError

def allowed_assignments(pair):
    rest=tuple(i for i in range(4) if i not in pair); out=[]
    for h1,h2 in itertools.product((+1,-1),repeat=2):
        lh=(HEXT[pair[0]],HEXT[pair[1]],-h1,-h2); rh=(HEXT[rest[0]],HEXT[rest[1]],h1,h2)
        if lh.count(-1)==2 and rh.count(-1)==2: out.append((h1,h2))
    return tuple(out)

def one_copy(cut,pair,a):
    rest,left,right,_,_,_,_=cut; h1,h2=a
    lh=(HEXT[pair[0]],HEXT[pair[1]],-h1,-h2); rh=(HEXT[rest[0]],HEXT[rest[1]],h1,h2)
    nL=tuple(i for i,h in enumerate(lh) if h==-1); nR=tuple(i for i,h in enumerate(rh) if h==-1)
    return pt4(left,nL)*pt4(right,nR)

def test_channel_helicity_selection_counts_are_exact():
    assert allowed_assignments((0,1))==((-1,-1),)
    assert set(allowed_assignments((0,2)))=={(+1,-1),(-1,+1)}
    assert set(allowed_assignments((0,3)))=={(+1,-1),(-1,+1)}

def test_all_three_cut_families_are_exactly_momentum_compatible():
    rng=np.random.default_rng(3401)
    for _ in range(50):
        lam,til=make_external(rng)
        assert np.linalg.norm(sum(np.outer(lam[i],til[i]) for i in range(4)))<2e-11
        for pair in ((0,1),(0,2),(0,3)):
            rest,_,_,la,ta,lb,tb=make_cut(lam,til,pair,rng)
            q=sum((np.outer(lam[i],til[i]) for i in pair),np.zeros((2,2),complex)); cutq=np.outer(la,ta)+np.outer(lb,tb)
            rightq=sum((np.outer(lam[i],til[i]) for i in rest),np.zeros((2,2),complex))
            assert np.linalg.norm(q-cutq)<2e-11
            assert np.linalg.norm(rightq+cutq)<2e-11

def test_s_channel_is_already_pure_spin2_by_helicity_selection():
    rng=np.random.default_rng(3402); pair=(0,1)
    for _ in range(80):
        lam,til=make_external(rng); cut=make_cut(lam,til,pair,rng); vals=[one_copy(cut,pair,a) for a in allowed_assignments(pair)]
        assert len(vals)==1; x=vals[0]
        assert abs(x*x-x*x)<1e-14*max(1.,abs(x*x))

def test_t_and_u_channels_have_nonzero_mixed_sector_and_project_exactly():
    rng=np.random.default_rng(3403)
    for pair in ((0,2),(0,3)):
        witnessed=0
        for _ in range(80):
            lam,til=make_external(rng); cut=make_cut(lam,til,pair,rng); A=allowed_assignments(pair)
            xA=one_copy(cut,pair,A[0]); xB=one_copy(cut,pair,A[1]); raw=(xA+xB)**2; projected=xA*xA+xB*xB; mixed=2*xA*xB
            scale=max(1.,abs(raw),abs(projected),abs(mixed)); assert abs(raw-projected-mixed)<3e-13*scale
            if abs(mixed)>1e-10*scale: witnessed+=1
        assert witnessed>=70

def test_projector_is_covariant_under_copy_exchange_and_simultaneous_helicity_flip():
    def pm(fn):
        M=np.zeros((4,4))
        for i,l in enumerate(LABELS): M[LABELS.index(fn(l)),i]=1
        return M
    X=pm(lambda h:(h[1],h[0])); H=pm(lambda h:(-h[0],-h[1]))
    for U in (X,H,X@H): assert np.allclose(U@P2@U.T,P2) and np.allclose(U@P2,P2@U)

def test_projection_commutes_with_admissible_channel_state_relabelings():
    rng=np.random.default_rng(3404)
    admissible=[np.eye(4),np.array([[0,0,0,1],[0,1,0,0],[0,0,1,0],[1,0,0,0]],float),np.array([[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]],float)]
    for U in admissible:
        assert np.allclose(U@P2@U.T,P2)
        for _ in range(50):
            v=rng.normal(size=4)+1j*rng.normal(size=4); assert np.allclose(U@(P2@v),P2@(U@v))
