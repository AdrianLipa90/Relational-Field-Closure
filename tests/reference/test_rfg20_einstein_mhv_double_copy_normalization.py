import math
import numpy as np

ETA=np.diag([1.,-1.,-1.,-1.]).astype(complex)

def dot(a,b): return a@ETA@b

def br(a,b): return a[0]*b[1]-a[1]*b[0]

def mat_to_vec(M):
    return np.array([(M[0,0]+M[1,1])/2,(M[0,1]+M[1,0])/2,(M[1,0]-M[0,1])/(2j),(M[0,0]-M[1,1])/2],complex)

def make_point(rng):
    while True:
        lam=[rng.normal(size=2)+1j*rng.normal(size=2) for _ in range(4)]
        M=np.column_stack([lam[2],lam[3]])
        if abs(np.linalg.det(M))<.2: continue
        til=[rng.normal(size=2)+1j*rng.normal(size=2) for _ in range(2)]
        t3=np.empty(2,complex);t4=np.empty(2,complex)
        for d in range(2):
            rhs=-(lam[0]*til[0][d]+lam[1]*til[1][d])
            sol=np.linalg.solve(M,rhs);t3[d],t4[d]=sol
        til += [t3,t4]
        if min(abs(br(lam[i],lam[j])) for i,j in [(0,1),(1,2),(2,3),(3,0),(0,2),(0,3)])<.05: continue
        return lam,til

def ep(lam,til,i,r): return mat_to_vec(np.sqrt(2)*np.outer(lam[r],til[i])/br(lam[r],lam[i]))
def em(lam,til,i,r): return -mat_to_vec(np.sqrt(2)*np.outer(lam[i],til[r])/br(til[i],til[r]))

def cubic_current(p,q,r,e1,e2):
    return dot(e1,e2)*(p-q)+e2*dot(e1,q-r)+e1*dot(e2,r-p)

def exchange(ps,es,k):
    p1,p2,p3,p4=ps;e1,e2,e3,e4=es
    if k=='s':
        q=p1+p2;jl=cubic_current(p1,p2,-q,e1,e2);jr=cubic_current(p3,p4,q,e3,e4)
    elif k=='t':
        q=p1+p3;jl=cubic_current(p1,p3,-q,e1,e3);jr=cubic_current(p2,p4,q,e2,e4)
    else:
        q=p1+p4;jl=cubic_current(p1,p4,-q,e1,e4);jr=cubic_current(p2,p3,q,e2,e3)
    return dot(jl,jr),dot(q,q)

def contact(es,k):
    e1,e2,e3,e4=es
    if k=='s': return dot(e1,e3)*dot(e2,e4)-dot(e1,e4)*dot(e2,e3)
    if k=='t': return dot(e1,e2)*dot(e3,e4)-dot(e1,e4)*dot(e2,e3)
    return dot(e1,e2)*dot(e3,e4)-dot(e1,e3)*dot(e2,e4)

def nums(ps,es):
    n={};d={}
    for k in ('s','t','u'):
        x,D=exchange(ps,es,k);n[k]=x+D*contact(es,k);d[k]=D
    return n,d

def pt(lam):
    prod=br(lam[0],lam[1])*br(lam[1],lam[2])*br(lam[2],lam[3])*br(lam[3],lam[0])
    return 1j*br(lam[0],lam[1])**4/prod

def test_project_partial_is_minus_2i_times_parke_taylor():
    rng=np.random.default_rng(20260828)
    for _ in range(100):
        la,ti=make_point(rng);ps=[mat_to_vec(np.outer(la[i],ti[i])) for i in range(4)]
        es=[em(la,ti,0,2),em(la,ti,1,3),ep(la,ti,2,0),ep(la,ti,3,1)]
        n,d=nums(ps,es)
        Apart=n['s']/d['s']-n['u']/d['u']
        assert abs(Apart-(-2j)*pt(la)) < 5e-10*max(1,abs(Apart),abs(pt(la)))

def real_kin(theta):
    s,c=math.sin(theta),math.cos(theta)
    return [np.array([1,0,0,1],complex),np.array([1,0,0,-1],complex),np.array([-1,-s,0,-c],complex),np.array([-1,s,0,c],complex)]

def hel_frame(p):
    spatial=np.real(p[1:]).astype(float);nh=spatial/np.linalg.norm(spatial)
    ref=np.array([0.,1.,0.])
    if abs(ref@nh)>.9: ref=np.array([1.,0.,0.])
    u=ref-nh*(ref@nh);u/=np.linalg.norm(u);v=np.cross(nh,u);v/=np.linalg.norm(v)
    return {1:np.r_[0,(u+1j*v)/np.sqrt(2)].astype(complex),-1:np.r_[0,(u-1j*v)/np.sqrt(2)].astype(complex)}

def project_core(theta):
    ps=real_kin(theta)
    phys=(-1,-1,1,1); es=[]
    for i,(p,h) in enumerate(zip(ps,phys)):
        hin=h if i<2 else -h
        es.append(hel_frame(p)[hin])
    n,d=nums(ps,es)
    return sum(n[k]*n[k]/d[k] for k in ('s','t','u')),d

def test_project_mhv_core_is_minus_four_s3_over_tu():
    for th in np.linspace(.35,2.55,31):
        core,d=project_core(float(th)); s,t,u=d['s'],d['t'],d['u']
        ref=-4*s**3/(t*u)
        assert abs(core-ref)<2e-11*max(1,abs(core),abs(ref))

def test_kappa_over_4_transfer_reproduces_einstein_mhv_normalization():
    kg=0.37; kE=kg*kg/4
    for th in (.5,1.1,1.8,2.3):
        core,d=project_core(th);s,t,u=d['s'],d['t'],d['u']
        project=(-1j)*(kg/4)**2*core
        einstein=1j*kE*s**3/(t*u)
        assert abs(project-einstein)<2e-12*max(1,abs(project),abs(einstein))

def test_old_kappa_over_2_transfer_has_exact_minus_four_mismatch():
    kg=.41
    core,d=project_core(1.17);s,t,u=d['s'],d['t'],d['u'];kE=kg*kg/4
    old=1j*(kg/2)**2*core
    target=1j*kE*s**3/(t*u)
    assert abs(old/target+4)<2e-13

def test_project_prefactor_in_kappaE_units_is_minus_i_kappaE_over_4():
    kg=.7;kE=kg*kg/4
    assert abs((-1j)*(kg/4)**2 - (-1j)*kE/4)<1e-15

def test_physical_kappaE_relation_is_unchanged():
    kg=.9;G=kg*kg/(32*math.pi)
    assert math.isclose(kg*kg/4,8*math.pi*G,rel_tol=1e-15)
