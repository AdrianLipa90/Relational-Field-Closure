import numpy as np

ETA_A=2.0

def br(a,b): return a[0]*b[1]-a[1]*b[0]
def sq(a,b): return a[0]*b[1]-a[1]*b[0]
def sij(lam,til,i,j): return br(lam[i],lam[j])*sq(til[j],til[i])

def pt(order,lam,neg=(0,2)):
    num=br(lam[neg[0]],lam[neg[1]])**4;den=1+0j
    for k in range(5): den*=br(lam[order[k]],lam[order[(k+1)%5]])
    return num/den

def make_base(rng):
    for _ in range(1000):
        vals=[rng.normal(size=2)+1j*rng.normal(size=2) for _ in range(8)]
        l1,chi,l3,l4,l5,t1,t2,t3=vals
        if min(abs(br(l1,chi)),abs(br(l1,l3)),abs(br(l4,l5)))<0.25: continue
        base=(l1,chi,l3,l4,l5,t1,t2,t3)
        try:
            b=basis(*family(1e-4,base))
            if min(abs(b[k]) for k in ('AL1','AR1'))<1e-8: continue
            return base
        except (np.linalg.LinAlgError,ZeroDivisionError,FloatingPointError):
            continue
    raise RuntimeError("stable factorization base unavailable")

def family(eps,base):
    l1,chi,l3,l4,l5,t1,t2,t3=base
    lam=[l1,l1+eps*chi,l3,l4,l5];til=[t1,t2,t3]
    M=sum(np.outer(lam[i],til[i]) for i in range(3))
    X=np.linalg.solve(np.column_stack([lam[3],lam[4]]),-M);til += [X[0],X[1]]
    return lam,til

def basis(lam,til):
    s12=sij(lam,til,0,1);s13=sij(lam,til,0,2);s23=sij(lam,til,1,2)
    AL1=pt([0,1,2,3,4],lam);AL2=pt([0,2,1,3,4],lam)
    AR1=pt([0,1,2,4,3],lam);AR2=pt([0,2,1,4,3],lam)
    S11=s12*(s13+s23);S12=s12*s13;S22=s13*(s12+s23)
    t11=S11*AL1*AR1;t12=S12*(AL1*AR2+AL2*AR1);t22=S22*AL2*AR2
    return dict(s12=s12,s13=s13,s23=s23,AL1=AL1,AL2=AL2,AR1=AR1,AR2=AR2,t11=t11,t12=t12,t22=t22,C=t11+t12+t22)

def test_factorization_family_is_exactly_massless_conserved_and_s12_linear():
    rng=np.random.default_rng(20260920);base=make_base(rng);ratios=[]
    for eps in (1e-2,1e-3,1e-4,1e-5):
        lam,til=family(eps,base);P=sum(np.outer(lam[i],til[i]) for i in range(5))
        assert np.linalg.norm(P)<2e-11
        for i in range(5): assert abs(np.linalg.det(np.outer(lam[i],til[i])))<2e-11
        ratios.append(basis(lam,til)['s12']/eps)
    assert max(abs(x-ratios[-1]) for x in ratios)<2e-10*max(1.0,abs(ratios[-1]))

def test_selected_yang_mills_basis_has_one_simple_pole_and_one_finite_entry():
    rng=np.random.default_rng(20260921);base=make_base(rng);resL=[];resR=[];finiteL=[];finiteR=[]
    for eps in (1e-3,1e-4,1e-5,1e-6):
        b=basis(*family(eps,base));resL.append(b['s12']*b['AL1']);resR.append(b['s12']*b['AR1']);finiteL.append(b['AL2']);finiteR.append(b['AR2'])
    assert abs(resL[-1])>1e-6 and abs(resR[-1])>1e-6
    assert abs(resL[-1]-resL[-2])<3e-4*max(1.0,abs(resL[-1]))
    assert abs(resR[-1]-resR[-2])<3e-4*max(1.0,abs(resR[-1]))
    assert max(abs(x) for x in finiteL)<10*max(1.0,abs(finiteL[-1]))
    assert max(abs(x) for x in finiteR)<10*max(1.0,abs(finiteR[-1]))

def test_klt_core_has_simple_not_double_s12_pole():
    rng=np.random.default_rng(20260922);base=make_base(rng);vals=[]
    for eps in (1e-3,1e-4,1e-5,1e-6):
        b=basis(*family(eps,base));vals.append((b['s12']*b['C'],b['s12']*b['s12']*b['C']))
    assert abs(vals[-1][0])>1e-6
    assert abs(vals[-1][0]-vals[-2][0])<4e-4*max(1.0,abs(vals[-1][0]))
    assert abs(vals[-1][1])<2e-5*max(1.0,abs(vals[-1][0]))

def test_klt_pole_residue_factorizes_into_left_right_yang_mills_residues():
    rng=np.random.default_rng(20260923)
    for _ in range(30):
        b=basis(*family(1e-7,make_base(rng)));actual=b['s12']*b['C'];pred=(b['s13']+b['s23'])*(b['s12']*b['AL1'])*(b['s12']*b['AR1'])
        assert abs(actual-pred)<3e-5*max(1.0,abs(actual),abs(pred))

def test_cross_and_finite_klt_terms_drop_out_of_the_residue():
    rng=np.random.default_rng(20260924);b=basis(*family(1e-7,make_base(rng)))
    lead=b['s12']*b['t11'];cross=b['s12']*b['t12'];finite=b['s12']*b['t22'];total=b['s12']*b['C']
    assert abs(total-lead)<3e-5*max(1.0,abs(total))
    assert abs(cross)<3e-5*max(1.0,abs(total))
    assert abs(finite)<3e-5*max(1.0,abs(total))

def test_project_and_physical_residue_normalization_follows_rfg27():
    rng=np.random.default_rng(20260925);b=basis(*family(1e-7,make_base(rng)));Rbg=b['s12']*b['C'];Rproject=ETA_A**2*Rbg
    assert abs(Rproject-4*Rbg)<1e-14*max(1.0,abs(Rproject))
    kg=0.67;P5=(kg/2)**3;Rphys=(-1j/4)*P5*Rproject
    assert abs(Rphys-(-1j)*P5*Rbg)<1e-14*max(1.0,abs(Rphys))
