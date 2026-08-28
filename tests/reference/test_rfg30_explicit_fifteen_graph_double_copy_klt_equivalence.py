import importlib.util
from pathlib import Path
import numpy as np

HERE=Path(__file__).resolve().parent
P29=HERE/"test_rfg29_explicit_fifteen_graph_project_bcj_current_factorization.py"
spec=importlib.util.spec_from_file_location("r29",P29)
r29=importlib.util.module_from_spec(spec); spec.loader.exec_module(r29)


def klt_bg(ps,eL,eR,cdot=r29.dot):
    s12=2*cdot(ps[0],ps[1]); s13=2*cdot(ps[0],ps[2]); s23=2*cdot(ps[1],ps[2])
    S=np.array([[s12*(s13+s23),s12*s13],[s12*s13,s13*(s12+s23)]],complex if np.iscomplexobj(ps[0]) else float)
    L=np.array([r29.ordered_bg(ps,eL,[0,1,2,3,4],cdot),r29.ordered_bg(ps,eL,[0,2,1,3,4],cdot)])
    R=np.array([r29.ordered_bg(ps,eR,[0,1,2,4,3],cdot),r29.ordered_bg(ps,eR,[0,2,1,4,3],cdot)])
    return L@S@R


def graph_core(ps,eL,eR,cdot=r29.dot):
    _,D,FL,mL,nL=r29.canonical_numerators(ps,eL,cdot=cdot)
    _,D2,FR,mR,nR=r29.canonical_numerators(ps,eR,cdot=cdot)
    assert np.max(abs(D-D2))<1e-12*max(1.,np.max(abs(D)))
    return np.sum(nL*nR/D),FL,mL,mR


def test_fifteen_graph_double_copy_equals_minus_project_klt_core():
    rng=np.random.default_rng(20261005)
    for _ in range(120):
        ps=r29.generate_2to3(rng);eL=r29.polarizations(ps,rng);eR=r29.polarizations(ps,rng)
        cg,_,_,_=graph_core(ps,eL,eR);ck=4.0*klt_bg(ps,eL,eR)
        assert abs(cg+ck)<8e-10*max(1.,abs(cg),abs(ck))


def test_graph_double_copy_is_invariant_under_null_space_generalized_gauge_shifts():
    rng=np.random.default_rng(20261006)
    for _ in range(60):
        ps=r29.generate_2to3(rng);eL=r29.polarizations(ps,rng);eR=r29.polarizations(ps,rng)
        AL,D,F,mL,nL=r29.canonical_numerators(ps,eL);AR,D2,F2,mR,nR=r29.canonical_numerators(ps,eR)
        _,_,vh=np.linalg.svd(F);N=vh[2:].T
        dL=N@rng.normal(size=4);dR=N@rng.normal(size=4)
        nLs=r29.B@(mL+dL);nRs=r29.B@(mR+dR)
        c0=np.sum(nL*nR/D);cs=np.sum(nLs*nRs/D)
        assert np.linalg.norm(F@dL)<2e-10 and np.linalg.norm(F@dR)<2e-10
        assert abs(cs-c0)<5e-10*max(1.,abs(c0),abs(cs))


def test_fifteen_graph_gravity_ward_identity_holds_in_either_copy():
    rng=np.random.default_rng(20261007)
    for _ in range(35):
        ps=r29.generate_2to3(rng);eL=r29.polarizations(ps,rng);eR=r29.polarizations(ps,rng)
        base=graph_core(ps,eL,eR)[0];scale=max(1.,abs(base))
        for leg in range(5):
            x=[e.copy() for e in eL];x[leg]=ps[leg].copy();assert abs(graph_core(ps,x,eR)[0])<3e-9*scale
            y=[e.copy() for e in eR];y[leg]=ps[leg].copy();assert abs(graph_core(ps,eL,y)[0])<3e-9*scale


def test_fifteen_graph_double_copy_is_copy_exchange_symmetric():
    rng=np.random.default_rng(20261008)
    for _ in range(80):
        ps=r29.generate_2to3(rng);eL=r29.polarizations(ps,rng);eR=r29.polarizations(ps,rng)
        a=graph_core(ps,eL,eR)[0];b=graph_core(ps,eR,eL)[0]
        assert abs(a-b)<3e-10*max(1.,abs(a),abs(b))


def test_s12_graph_double_copy_residue_matches_minus_four_rfg28_bg_residue():
    rng=np.random.default_rng(20261009)
    for _ in range(10):
        base=r29.make_base(rng);lam0,til0=r29.family(0.,base);ps0=r29.ps_from_spin(lam0,til0);eL0=r29.helicity_es(lam0,til0);eR0=r29.helicity_es(lam0,til0)
        RL,_,_=r29.factor_current_residue(ps0,eL0);orderR=[0,1,2,4,3];RR,_,_=r29.factor_current_residue([ps0[i] for i in orderR],[eR0[i] for i in orderR])
        s13=r29.dotc(ps0[0]+ps0[2],ps0[0]+ps0[2]);s23=r29.dotc(ps0[1]+ps0[2],ps0[1]+ps0[2]);Rbg=(s13+s23)*RL*RR
        lam,til=r29.family(1e-6,base);ps=r29.ps_from_spin(lam,til);eL=r29.helicity_es(lam,til);eR=r29.helicity_es(lam,til);s12=r29.dotc(ps[0]+ps[1],ps[0]+ps[1]);cg=graph_core(ps,eL,eR,r29.dotc)[0]
        assert abs(s12*cg+4*Rbg)<3e-4*max(1.,abs(4*Rbg))


def test_graph_form_physical_prefactor_matches_rfg27_klt_form_and_reduced_scale():
    rng=np.random.default_rng(20261010)
    for _ in range(40):
        ps=r29.generate_2to3(rng);eL=r29.polarizations(ps,rng);eR=r29.polarizations(ps,rng);cg=graph_core(ps,eL,eR)[0];ck=4*klt_bg(ps,eL,eR)
        mbar=float(rng.uniform(.7,4.0));kg=2/mbar;P5=(kg/2)**3
        Mg=(1j/4)*P5*cg;Mk=(-1j/4)*P5*ck
        assert abs(Mg-Mk)<8e-10*max(1.,abs(Mg),abs(Mk))
        assert abs(P5-1/mbar**3)<2e-15
