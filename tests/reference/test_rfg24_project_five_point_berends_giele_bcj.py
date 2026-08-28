import math
from functools import lru_cache
import numpy as np

ALPHA_C=0.47483961905223004
G_YM=ALPHA_C**-0.5
ETA=np.diag([1.0,-1.0,-1.0,-1.0])

def dot(a,b): return a@ETA@b

def generate_2to3(rng,energy=1.0):
    for _ in range(100):
        v3=rng.normal(size=3); v4=rng.normal(size=3)
        if np.linalg.norm(v3)<1e-5 or np.linalg.norm(v4)<1e-5: continue
        v5=-(v3+v4)
        if np.linalg.norm(v5)<1e-5: continue
        scale=2.0*energy/(np.linalg.norm(v3)+np.linalg.norm(v4)+np.linalg.norm(v5))
        vs=[scale*v3,scale*v4,scale*v5]
        ps=[np.array([-energy,0.0,0.0,-energy]),np.array([-energy,0.0,0.0,energy])]
        ps += [np.r_[np.linalg.norm(v),v] for v in vs]
        if min(abs(dot(ps[i]+ps[j],ps[i]+ps[j])) for i in range(5) for j in range(i+1,5))>1e-5:
            return ps
    raise RuntimeError

def transverse_basis(p):
    n=p[1:]/np.linalg.norm(p[1:]); ref=np.array([1.0,0.0,0.0])
    if abs(np.dot(n,ref))>0.9: ref=np.array([0.0,1.0,0.0])
    e1=np.cross(n,ref); e1/=np.linalg.norm(e1); e2=np.cross(n,e1); e2/=np.linalg.norm(e2)
    return np.r_[0.0,e1],np.r_[0.0,e2]

def polarizations(ps,rng):
    out=[]
    for p in ps:
        e1,e2=transverse_basis(p); a,b=rng.normal(size=2)
        out.append((a*e1+b*e2)/math.sqrt(a*a+b*b))
    return out

def bg_amplitude(ps,es,quartic_scale=1.0,binary_scale=math.sqrt(2.0)):
    n=len(ps)
    @lru_cache(None)
    def momentum(seq): return sum((ps[i] for i in seq),np.zeros(4))
    @lru_cache(None)
    def current(seq):
        if len(seq)==1: return es[seq[0]].astype(float)
        return numerator(seq)/dot(momentum(seq),momentum(seq))
    @lru_cache(None)
    def numerator(seq):
        L=len(seq); out=np.zeros(4)
        for k in range(1,L):
            X,Y=seq[:k],seq[k:]; JX,JY=current(X),current(Y); kX,kY=momentum(X),momentum(Y); jj=dot(JX,JY)
            out += binary_scale*(dot(kY,JX)*JY+0.5*kX*jj-dot(kX,JY)*JX-0.5*kY*jj)
        for i in range(1,L-1):
            for j in range(i+1,L):
                X,Y,Z=seq[:i],seq[i:j],seq[j:]; JX,JY,JZ=current(X),current(Y),current(Z)
                out += quartic_scale*(dot(JX,JZ)*JY-0.5*dot(JX,JY)*JZ-0.5*dot(JY,JZ)*JX)
        return out
    return dot(numerator(tuple(range(n-1))),es[n-1])

def ordered_amplitude(ps,es,order,**kw): return bg_amplitude([ps[i] for i in order],[es[i] for i in order],**kw)
def sij(ps,i,j): return 2.0*dot(ps[i],ps[j])

def test_project_five_point_states_are_massless_conserved_and_transverse():
    rng=np.random.default_rng(20260902)
    for _ in range(120):
        ps=generate_2to3(rng); es=polarizations(ps,rng)
        assert np.linalg.norm(sum(ps))<2e-13
        for p,e in zip(ps,es): assert abs(dot(p,p))<2e-13 and abs(dot(p,e))<2e-13

def test_project_five_point_all_leg_ward_identities():
    rng=np.random.default_rng(20260903)
    for _ in range(180):
        ps=generate_2to3(rng); es=polarizations(ps,rng); scale=max(1.0,abs(bg_amplitude(ps,es)))
        for leg in range(5):
            replaced=[e.copy() for e in es]; replaced[leg]=ps[leg].copy()
            assert abs(bg_amplitude(ps,replaced))<3e-11*scale

def test_project_five_point_fundamental_bcj_relation():
    rng=np.random.default_rng(20260904)
    for _ in range(220):
        ps=generate_2to3(rng); es=polarizations(ps,rng)
        a1=ordered_amplitude(ps,es,[0,1,2,3,4]); a2=ordered_amplitude(ps,es,[0,2,1,3,4]); a3=ordered_amplitude(ps,es,[0,2,3,1,4])
        terms=[sij(ps,0,1)*a1,(sij(ps,0,1)+sij(ps,1,2))*a2,(sij(ps,0,1)+sij(ps,1,2)+sij(ps,1,3))*a3]
        assert abs(sum(terms))<4e-11*max(1.0,*map(abs,terms))

def test_project_five_point_reflection_and_photon_decoupling():
    rng=np.random.default_rng(20260905)
    for _ in range(150):
        ps=generate_2to3(rng); es=polarizations(ps,rng)
        a=ordered_amplitude(ps,es,[0,1,2,3,4]); ar=ordered_amplitude(ps,es,[4,3,2,1,0])
        assert abs(a+ar)<3e-11*max(1.0,abs(a),abs(ar))
        dec=sum(ordered_amplitude(ps,es,o) for o in ([0,1,2,3,4],[1,0,2,3,4],[1,2,0,3,4],[1,2,3,0,4]))
        assert abs(dec)<4e-11*max(1.0,abs(a))

def test_quartic_normalization_is_required_for_five_point_ward_closure():
    rng=np.random.default_rng(20260906); witnessed=False
    for _ in range(30):
        ps=generate_2to3(rng); es=polarizations(ps,rng); good=[]; bad=[]
        for leg in range(5):
            replaced=[e.copy() for e in es]; replaced[leg]=ps[leg].copy()
            good.append(abs(bg_amplitude(ps,replaced,quartic_scale=1.0))); bad.append(abs(bg_amplitude(ps,replaced,quartic_scale=0.0)))
        assert max(good)<3e-10
        if max(bad)>1e-3: witnessed=True
    assert witnessed

def test_project_five_point_coupling_power_is_g_cubed():
    rng=np.random.default_rng(20260907); ps=generate_2to3(rng); es=polarizations(ps,rng)
    stripped=bg_amplitude(ps,es); physical=G_YM**3*stripped
    assert math.isclose(G_YM**2,1.0/ALPHA_C,rel_tol=1e-15)
    assert abs(physical-G_YM**3*stripped)<1e-14*max(1.0,abs(physical))
