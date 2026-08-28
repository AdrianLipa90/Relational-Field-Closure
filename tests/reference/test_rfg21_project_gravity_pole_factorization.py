import math
import numpy as np

ETA=np.diag([1.0,-1.0,-1.0,-1.0])

def dot(a,b): return a @ ETA @ b

def cubic_current(p,q,r,e1,e2):
    return dot(e1,e2)*(p-q)+e2*dot(e1,q-r)+e1*dot(e2,r-p)

def channel_data(ps,es,kind):
    p1,p2,p3,p4=ps; e1,e2,e3,e4=es
    if kind=="s":
        k=p1+p2; jl=cubic_current(p1,p2,-k,e1,e2); jr=cubic_current(p3,p4,k,e3,e4)
    elif kind=="t":
        k=p1+p3; jl=cubic_current(p1,p3,-k,e1,e3); jr=cubic_current(p2,p4,k,e2,e4)
    else:
        k=p1+p4; jl=cubic_current(p1,p4,-k,e1,e4); jr=cubic_current(p2,p3,k,e2,e3)
    return jl,jr,dot(jl,jr),dot(k,k)

def contact_kinematic(es,kind):
    e1,e2,e3,e4=es
    if kind=="s": return dot(e1,e3)*dot(e2,e4)-dot(e1,e4)*dot(e2,e3)
    if kind=="t": return dot(e1,e2)*dot(e3,e4)-dot(e1,e4)*dot(e2,e3)
    return dot(e1,e2)*dot(e3,e4)-dot(e1,e3)*dot(e2,e4)

def project_data(ps,es):
    n={}; d={}; x={}; k={}; currents={}
    for kind in ("s","t","u"):
        jl,jr,xx,dd=channel_data(ps,es,kind); kk=contact_kinematic(es,kind)
        currents[kind]=(jl,jr); x[kind]=xx; d[kind]=dd; k[kind]=kk; n[kind]=xx+dd*kk
    return n,d,x,k,currents

def gravity_core(ps,ea,eb):
    na,d,_,_,_=project_data(ps,ea); nb,_,_,_,_=project_data(ps,eb)
    return sum(na[k]*nb[k]/d[k] for k in ("s","t","u"))

def kinematics(theta,energy=1.0):
    s,c=math.sin(theta),math.cos(theta)
    ps=[
        np.array([energy,0,0,energy]),
        np.array([energy,0,0,-energy]),
        np.array([-energy,-energy*s,0,-energy*c]),
        np.array([-energy,energy*s,0,energy*c]),
    ]
    ey=np.array([0.0,0.0,1.0,0.0]); e12=np.array([0.0,1.0,0.0,0.0]); e34=np.array([0.0,c,0.0,-s])
    return ps,ey,e12,e34

def polarizations(theta,weights):
    ps,ey,e12,e34=kinematics(theta)
    es=[]
    for w,b in zip(weights,[e12,e12,e34,e34]):
        es.append((ey+w*b)/math.sqrt(1.0+w*w))
    return ps,es

WA=[0.3,-0.4,0.5,-0.2]
WB=[-0.2,0.1,0.4,-0.3]

def test_forward_t_channel_is_massless_pole_coordinate():
    vals=[]
    for theta in (0.2,0.1,0.05,0.025):
        ps,es=polarizations(theta,WA); _,d,_,_,_=project_data(ps,es)
        vals.append(abs(d["t"]))
        assert abs(d["s"]-4.0)<1e-13
        assert abs(d["u"])>3.9
    for a,b in zip(vals,vals[1:]):
        assert 0.23 < b/a < 0.27

def test_quartic_contact_drops_out_of_t_channel_numerator_at_pole():
    for weights in (WA,WB):
        defects=[]
        for theta in (0.2,0.1,0.05,0.025,0.0125):
            ps,es=polarizations(theta,weights)
            n,d,x,k,_=project_data(ps,es)
            assert abs((n["t"]-x["t"])-d["t"]*k["t"])<1e-13
            defects.append(abs(n["t"]-x["t"]))
        for a,b in zip(defects,defects[1:]):
            assert b < 0.30*a
        assert defects[-1] < 0.006*defects[0]

def test_t_times_gravity_core_converges_to_cubic_residue():
    errors=[]
    for theta in (0.2,0.1,0.05,0.025,0.0125):
        ps,ea=polarizations(theta,WA); _,eb=polarizations(theta,WB)
        na,d,xa,_,_=project_data(ps,ea); nb,_,xb,_,_=project_data(ps,eb)
        residue=d["t"]*gravity_core(ps,ea,eb)
        target=xa["t"]*xb["t"]
        errors.append(abs(residue-target)/max(1.0,abs(target)))
    for a,b in zip(errors,errors[1:]):
        assert b < 0.27*a
    assert errors[-1] < 1e-5

def test_non_t_channels_vanish_after_multiplication_by_t():
    vals=[]
    for theta in (0.2,0.1,0.05,0.025):
        ps,ea=polarizations(theta,WA); _,eb=polarizations(theta,WB)
        na,d,_,_,_=project_data(ps,ea); nb,_,_,_,_=project_data(ps,eb)
        other=d["t"]*(na["s"]*nb["s"]/d["s"]+na["u"]*nb["u"]/d["u"])
        vals.append(abs(other))
    for a,b in zip(vals,vals[1:]):
        assert b < 0.30*a

def test_cubic_double_copy_residue_factorizes_as_rank2_current_contraction():
    for theta in (0.4,0.2,0.1,0.05):
        ps,ea=polarizations(theta,WA); _,eb=polarizations(theta,WB)
        _,_,xa,_,ca=project_data(ps,ea); _,_,xb,_,cb=project_data(ps,eb)
        jla,jra=ca["t"]; jlb,jrb=cb["t"]
        HL=np.outer(jla,jlb); HR=np.outer(jra,jrb)
        contracted=np.einsum("mn,ma,nb,ab->",HL,ETA,ETA,HR)
        target=xa["t"]*xb["t"]
        assert abs(contracted-target)<2e-13*max(1.0,abs(target))

def test_finite_contact_redistribution_does_not_change_pole_residue_limit():
    theta=5e-4
    ps,ea=polarizations(theta,WA); _,eb=polarizations(theta,WB)
    na,d,xa,ka,_=project_data(ps,ea); nb,_,xb,kb,_=project_data(ps,eb)
    base=d["t"]*gravity_core(ps,ea,eb)
    target=xa["t"]*xb["t"]
    assert abs(base-target)/max(1.0,abs(target))<1e-7
    assert abs(d["t"]*ka["t"])<6e-8 and abs(d["t"]*kb["t"])<6e-8
