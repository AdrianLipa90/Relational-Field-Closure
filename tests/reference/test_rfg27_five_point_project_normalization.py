import math
from functools import lru_cache
import numpy as np

ETA=np.diag([1.,-1.,-1.,-1.]).astype(complex)
ETA_A=2.0

def dot(a,b): return a@ETA@b
def br(a,b): return a[0]*b[1]-a[1]*b[0]
def sq(a,b): return a[0]*b[1]-a[1]*b[0]

def mat_to_vec(M):
    return np.array([(M[0,0]+M[1,1])/2,(M[0,1]+M[1,0])/2,(M[1,0]-M[0,1])/(2j),(M[0,0]-M[1,1])/2],complex)

def ep(lam,til,i,r): return mat_to_vec(np.sqrt(2)*np.outer(lam[r],til[i])/br(lam[r],lam[i]))
def em(lam,til,i,r): return -mat_to_vec(np.sqrt(2)*np.outer(lam[i],til[r])/sq(til[i],til[r]))

def bg_amplitude(ps,es,quartic_scale=1.0,binary_scale=math.sqrt(2.0)):
    n=len(ps)
    @lru_cache(None)
    def momentum(seq): return sum((ps[i] for i in seq),np.zeros(4,dtype=complex))
    @lru_cache(None)
    def current(seq):
        if len(seq)==1: return np.array(es[seq[0]],dtype=complex)
        return numerator(seq)/dot(momentum(seq),momentum(seq))
    @lru_cache(None)
    def numerator(seq):
        L=len(seq);out=np.zeros(4,dtype=complex)
        for k in range(1,L):
            X,Y=seq[:k],seq[k:];JX,JY=current(X),current(Y);kX,kY=momentum(X),momentum(Y);jj=dot(JX,JY)
            out+=binary_scale*(dot(kY,JX)*JY+0.5*kX*jj-dot(kX,JY)*JX-0.5*kY*jj)
        for i in range(1,L-1):
            for j in range(i+1,L):
                X,Y,Z=seq[:i],seq[i:j],seq[j:];JX,JY,JZ=current(X),current(Y),current(Z)
                out+=quartic_scale*(dot(JX,JZ)*JY-0.5*dot(JX,JY)*JZ-0.5*dot(JY,JZ)*JX)
        return out
    return dot(numerator(tuple(range(n-1))),es[n-1])

def raw_pt(order,lam,neg=(0,1)):
    num=br(lam[neg[0]],lam[neg[1]])**4;den=1+0j
    for k in range(len(order)): den*=br(lam[order[k]],lam[order[(k+1)%len(order)]])
    return num/den

def generate_n(n,rng):
    for _ in range(1000):
        lam=[rng.normal(size=2)+1j*rng.normal(size=2) for _ in range(n)]
        if abs(br(lam[-2],lam[-1]))<0.2: continue
        til=[rng.normal(size=2)+1j*rng.normal(size=2) for _ in range(n-2)]
        M=sum(np.outer(lam[i],til[i]) for i in range(n-2))
        X=np.linalg.solve(np.column_stack([lam[-2],lam[-1]]),-M);til += [X[0],X[1]]
        return lam,til
    raise RuntimeError("stable kinematics unavailable")

def helicity_es(lam,til):
    n=len(lam);out=[]
    for i in range(n):
        if i in (0,1):
            r=(i+2)%n
            if abs(sq(til[i],til[r]))<1e-8:r=(i+1)%n
            out.append(em(lam,til,i,r))
        else:
            r=0 if i!=0 else 1
            if abs(br(lam[r],lam[i]))<1e-8:r=(r+1)%n
            out.append(ep(lam,til,i,r))
    return out

def cubic_current(p,q,r,e1,e2): return dot(e1,e2)*(p-q)+e2*dot(e1,q-r)+e1*dot(e2,r-p)
def exchange(ps,es,k):
    p1,p2,p3,p4=ps;e1,e2,e3,e4=es
    if k=='s':q=p1+p2;jl=cubic_current(p1,p2,-q,e1,e2);jr=cubic_current(p3,p4,q,e3,e4)
    elif k=='t':q=p1+p3;jl=cubic_current(p1,p3,-q,e1,e3);jr=cubic_current(p2,p4,q,e2,e4)
    else:q=p1+p4;jl=cubic_current(p1,p4,-q,e1,e4);jr=cubic_current(p2,p3,q,e2,e3)
    return dot(jl,jr),dot(q,q)
def contact(es,k):
    e1,e2,e3,e4=es
    if k=='s':return dot(e1,e3)*dot(e2,e4)-dot(e1,e4)*dot(e2,e3)
    if k=='t':return dot(e1,e2)*dot(e3,e4)-dot(e1,e4)*dot(e2,e3)
    return dot(e1,e2)*dot(e3,e4)-dot(e1,e3)*dot(e2,e4)
def project_partial4(ps,es):
    n={};d={}
    for k in ('s','t','u'):
        x,D=exchange(ps,es,k);n[k]=x+D*contact(es,k);d[k]=D
    return n['s']/d['s']-n['u']/d['u']

def sij(lam,til,i,j): return br(lam[i],lam[j])*sq(til[j],til[i])
def c4_bg(lam,til): return -sij(lam,til,0,3)*raw_pt([0,1,2,3],lam)*raw_pt([0,2,1,3],lam)
def c5_bg(lam,til):
    s12=sij(lam,til,0,1);s13=sij(lam,til,0,2);s23=sij(lam,til,1,2)
    S=np.array([[s12*(s13+s23),s12*s13],[s12*s13,s13*(s12+s23)]],complex)
    AL=np.array([raw_pt([0,1,2,3,4],lam),raw_pt([0,2,1,3,4],lam)])
    AR=np.array([raw_pt([0,1,2,4,3],lam),raw_pt([0,2,1,4,3],lam)])
    return AL@S@AR

def soft_plus(lam,til,s=4,x=0,y=1):
    total=0j
    for a in range(4):
        total+=sq(til[s],til[a])/br(lam[s],lam[a])*br(lam[x],lam[a])*br(lam[y],lam[a])/(br(lam[x],lam[s])*br(lam[y],lam[s]))
    return total

def conserved_soft_family(eps,lam0,t12,t5raw):
    lam=[x.copy() for x in lam0];til=[None]*5
    lam[4]=math.sqrt(eps)*lam0[4];til[0],til[1]=t12[0].copy(),t12[1].copy();til[4]=math.sqrt(eps)*t5raw
    M=np.outer(lam[0],til[0])+np.outer(lam[1],til[1])+np.outer(lam[4],til[4])
    X=np.linalg.solve(np.column_stack([lam[2],lam[3]]),-M);til[2],til[3]=X[0],X[1]
    return lam,til

def test_bg_four_point_is_standard_color_order_normalization():
    rng=np.random.default_rng(20260910)
    for _ in range(80):
        lam,til=generate_n(4,rng);ps=[mat_to_vec(np.outer(lam[i],til[i])) for i in range(4)];es=helicity_es(lam,til)
        bg=bg_amplitude(ps,es);ref=raw_pt([0,1,2,3],lam)
        assert abs(bg-ref)<2e-10*max(1.0,abs(ref))

def test_rfg15_project_partial_is_exactly_twice_bg_basis():
    rng=np.random.default_rng(20260911)
    for _ in range(80):
        lam,til=generate_n(4,rng);ps=[mat_to_vec(np.outer(lam[i],til[i])) for i in range(4)];es=helicity_es(lam,til)
        bg=bg_amplitude(ps,es);project=project_partial4(ps,es)
        assert abs(project-ETA_A*bg)<2e-10*max(1.0,abs(project))

def test_bg_five_point_is_standard_color_order_normalization():
    rng=np.random.default_rng(20260912)
    for _ in range(80):
        lam,til=generate_n(5,rng);ps=[mat_to_vec(np.outer(lam[i],til[i])) for i in range(5)];es=helicity_es(lam,til)
        bg=bg_amplitude(ps,es);ref=raw_pt([0,1,2,3,4],lam)
        assert abs(bg-ref)<5e-9*max(1.0,abs(ref))

def test_project_klt_map_is_quadratic_in_eta_A():
    rng=np.random.default_rng(20260913)
    for _ in range(80):
        lam,til=generate_n(5,rng);core_bg=c5_bg(lam,til);core_project=ETA_A**2*core_bg
        assert abs(core_project-4.0*core_bg)<1e-14*max(1.0,abs(core_project))

def test_five_to_four_gravity_core_soft_factorization_fixes_same_project_zeta():
    rng=np.random.default_rng(20260914);lam0=[rng.normal(size=2)+1j*rng.normal(size=2) for _ in range(5)]
    while abs(br(lam0[2],lam0[3]))<0.3 or min(abs(br(lam0[3],lam0[4])),abs(br(lam0[4],lam0[0])))<0.3:lam0=[rng.normal(size=2)+1j*rng.normal(size=2) for _ in range(5)]
    t12=[rng.normal(size=2)+1j*rng.normal(size=2) for _ in range(2)];t5raw=rng.normal(size=2)+1j*rng.normal(size=2)
    lam,til=conserved_soft_family(1e-6,lam0,t12,t5raw);S=soft_plus(lam,til);C4p=4*c4_bg(lam[:4],til[:4]);C5p=4*c5_bg(lam,til)
    assert abs(C5p/(S*C4p)-1.0)<2e-5
    kg=0.73;P4=(kg/2)**2;P5=(kg/2)**3;M4=(-1j/4)*P4*C4p;M5=(-1j/4)*P5*C5p
    assert abs(M5/((kg/2)*S*M4)-1.0)<2e-5

def test_old_plus_i_bg_prefactor_has_soft_phase_defect_and_project_prefactor_is_minus_i_over_4():
    rng=np.random.default_rng(20260915);lam0=[rng.normal(size=2)+1j*rng.normal(size=2) for _ in range(5)]
    while abs(br(lam0[2],lam0[3]))<0.3 or min(abs(br(lam0[3],lam0[4])),abs(br(lam0[4],lam0[0])))<0.3:lam0=[rng.normal(size=2)+1j*rng.normal(size=2) for _ in range(5)]
    t12=[rng.normal(size=2)+1j*rng.normal(size=2) for _ in range(2)];t5raw=rng.normal(size=2)+1j*rng.normal(size=2)
    lam,til=conserved_soft_family(1e-6,lam0,t12,t5raw);S=soft_plus(lam,til);C4p=4*c4_bg(lam[:4],til[:4]);C5bg=c5_bg(lam,til);C5p=4*C5bg
    kg=0.61;P4=(kg/2)**2;P5=(kg/2)**3;M4=(-1j/4)*P4*C4p;target=(kg/2)*S*M4
    good=(-1j/4)*P5*C5p;old=1j*P5*C5bg
    assert abs(good/target-1.0)<2e-5
    assert abs(old/target+1.0)<2e-5
    mbar=2/kg
    assert abs((-1j/4)*P5-(-1j)/(4*mbar**3))<1e-15
