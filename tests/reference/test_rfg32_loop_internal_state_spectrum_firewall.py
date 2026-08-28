import numpy as np


def ang(a,b): return a[0]*b[1]-a[1]*b[0]


def pt4(lams, neg):
    num=ang(lams[neg[0]],lams[neg[1]])**4
    den=1+0j
    for i in range(4):
        den*=ang(lams[i],lams[(i+1)%4])
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


def make_t_cut(lam,til,rng):
    q=np.outer(lam[0],til[0])+np.outer(lam[2],til[2])
    for _ in range(200):
        la=rng.normal(size=2)+1j*rng.normal(size=2)
        lb=rng.normal(size=2)+1j*rng.normal(size=2)
        L=np.column_stack([la,lb])
        if abs(np.linalg.det(L))<0.2: continue
        X=np.linalg.solve(L,q); ta,tb=X[0],X[1]
        left=[lam[0],lam[2],-la,-lb]
        right=[lam[1],lam[3],la,lb]
        dl=min(abs(ang(left[i],left[(i+1)%4])) for i in range(4))
        dr=min(abs(ang(right[i],right[(i+1)%4])) for i in range(4))
        if min(dl,dr)<0.03: continue
        return la,ta,lb,tb,left,right
    raise RuntimeError


ASSIGNMENTS=((+1,-1),(-1,+1))


def one_copy_cut(lam,til,cut,assignment):
    _,_,_,_,left,right=cut
    h1,h2=assignment
    left_h=(-1,+1,-h1,-h2)
    right_h=(-1,+1,h1,h2)
    negL=tuple(i for i,h in enumerate(left_h) if h==-1)
    negR=tuple(i for i,h in enumerate(right_h) if h==-1)
    assert len(negL)==2 and len(negR)==2
    AL=pt4(left,negL); AR=pt4(right,negR)
    return AL,AR,AL*AR


def test_cut_kinematics_are_massless_and_conserved():
    rng=np.random.default_rng(3201)
    for _ in range(60):
        lam,til=make_external(rng); la,ta,lb,tb,_,_=make_t_cut(lam,til,rng)
        P=sum(np.outer(lam[i],til[i]) for i in range(4))
        q=np.outer(lam[0],til[0])+np.outer(lam[2],til[2])
        cutq=np.outer(la,ta)+np.outer(lb,tb)
        assert np.linalg.norm(P)<2e-11
        assert np.linalg.norm(q-cutq)<2e-11


def test_both_internal_yang_mills_helicity_assignments_are_nonzero():
    rng=np.random.default_rng(3202)
    for _ in range(60):
        lam,til=make_external(rng); cut=make_t_cut(lam,til,rng)
        vals=[one_copy_cut(lam,til,cut,a)[2] for a in ASSIGNMENTS]
        scale=max(1.0,*map(abs,vals))
        assert min(map(abs,vals))>1e-12*scale


def test_tensor_product_state_classification_separates_spin2_and_mixed_zero_helicity():
    A,B=ASSIGNMENTS
    assert A[0]+A[0] in (+2,-2) and A[1]+A[1] in (+2,-2)
    assert B[0]+B[0] in (+2,-2) and B[1]+B[1] in (+2,-2)
    assert A[0]+B[0]==0 and A[1]+B[1]==0
    assert B[0]+A[0]==0 and B[1]+A[1]==0


def test_mixed_helicity_tensor_product_cut_terms_are_nonzero():
    rng=np.random.default_rng(3203)
    for _ in range(80):
        lam,til=make_external(rng); cut=make_t_cut(lam,til,rng)
        xA=one_copy_cut(lam,til,cut,ASSIGNMENTS[0])[2]
        xB=one_copy_cut(lam,til,cut,ASSIGNMENTS[1])[2]
        mixed1=xA*xB; mixed2=xB*xA
        scale=max(1.0,abs(xA*xA),abs(xB*xB),abs(mixed1))
        assert abs(mixed1)>1e-12*scale
        assert abs(mixed2-mixed1)<1e-14*scale


def test_raw_double_copy_cut_equals_spin2_plus_mixed_sector():
    rng=np.random.default_rng(3204)
    for _ in range(80):
        lam,til=make_external(rng); cut=make_t_cut(lam,til,rng)
        xA=one_copy_cut(lam,til,cut,ASSIGNMENTS[0])[2]
        xB=one_copy_cut(lam,til,cut,ASSIGNMENTS[1])[2]
        raw=(xA+xB)**2
        spin2=xA*xA+xB*xB
        mixed=2*xA*xB
        scale=max(1.0,abs(raw),abs(spin2),abs(mixed))
        assert abs(raw-(spin2+mixed))<2e-13*scale
        assert abs(mixed)>1e-12*scale


def test_pure_spin2_internal_projector_changes_generic_raw_loop_cut():
    rng=np.random.default_rng(3205)
    witnessed=0
    for _ in range(80):
        lam,til=make_external(rng); cut=make_t_cut(lam,til,rng)
        xA=one_copy_cut(lam,til,cut,ASSIGNMENTS[0])[2]
        xB=one_copy_cut(lam,til,cut,ASSIGNMENTS[1])[2]
        raw=(xA+xB)**2
        projected=xA*xA+xB*xB
        scale=max(1.0,abs(raw),abs(projected))
        if abs(raw-projected)>1e-8*scale:
            witnessed += 1
    assert witnessed>=70
