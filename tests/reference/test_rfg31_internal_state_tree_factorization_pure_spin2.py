import importlib.util
from pathlib import Path
import numpy as np
HERE=Path(__file__).resolve().parent

def load(name,file):
    spec=importlib.util.spec_from_file_location(name,HERE/file);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
r29=load("r29","test_rfg29_explicit_fifteen_graph_project_bcj_current_factorization.py")
r30=load("r30","test_rfg30_explicit_fifteen_graph_double_copy_klt_equivalence.py")

ALLOWED=[(0,2),(1,2),(2,3),(0,3),(1,3)]

def tensor_trace(u,v): return r29.dotc(u,v)
def antisym_norm(u,v):
    A=np.outer(u,v);return np.linalg.norm(0.5*(A-A.T))

def test_matching_helicity_internal_currents_are_transverse_null_and_nonzero_on_supported_branch():
    rng=np.random.default_rng(20261011)
    for _ in range(12):
        lam,til=r29.family(0.,r29.make_base(rng));ps=r29.ps_from_spin(lam,til);P=ps[0]+ps[1]
        for neg in ALLOWED:
            es=r29.helicity_es(lam,til,neg=neg);R,N,J=r29.factor_current_residue(ps,es);scale=max(1.,np.linalg.norm(N),np.linalg.norm(J))
            assert abs(R)>1e-8
            assert abs(r29.dotc(P,N))<3e-10*scale and abs(r29.dotc(P,J))<3e-10*scale
            assert abs(r29.dotc(N,N))<3e-9*scale**2 and abs(r29.dotc(J,J))<3e-9*scale**2

def test_matched_copy_internal_three_point_tensor_is_symmetric_traceless_and_selects_spin2_residue():
    rng=np.random.default_rng(20261012)
    for k in range(20):
        lam,til=r29.family(0.,r29.make_base(rng));ps=r29.ps_from_spin(lam,til);es=r29.helicity_es(lam,til,neg=ALLOWED[k%len(ALLOWED)])
        RL,N,JL=r29.factor_current_residue(ps,es);orderR=[0,1,2,4,3];RR,NR,JR=r29.factor_current_residue([ps[i] for i in orderR],[es[i] for i in orderR])
        assert np.linalg.norm(N-NR)<2e-10*max(1.,np.linalg.norm(N))
        T3=np.outer(N,NR);assert np.linalg.norm(T3-T3.T)<2e-10*max(1.,np.linalg.norm(T3))
        tr3=r29.dotc(N,NR);tr4=r29.dotc(JL,JR);full=r29.dotc(N,JL)*r29.dotc(NR,JR)
        scalar=.5*tr3*tr4
        anti=.5*(r29.dotc(N,JL)*r29.dotc(NR,JR)-r29.dotc(N,JR)*r29.dotc(NR,JL))
        spin2=full-scalar-anti
        assert abs(tr3)<3e-9*max(1.,np.linalg.norm(N)*np.linalg.norm(NR))
        assert abs(scalar)<3e-9*max(1.,abs(full));assert abs(anti)<3e-9*max(1.,abs(full))
        assert abs(spin2-full)<4e-9*max(1.,abs(full));assert abs(full-RL*RR)<3e-10*max(1.,abs(full),abs(RL*RR))

def test_channel_gauge_shifts_along_null_momentum_preserve_tracelessness_and_residue():
    rng=np.random.default_rng(20261013)
    for _ in range(25):
        lam,til=r29.family(0.,r29.make_base(rng));ps=r29.ps_from_spin(lam,til);P=ps[0]+ps[1];es=r29.helicity_es(lam,til,neg=ALLOWED[_%len(ALLOWED)]);R,N,J=r29.factor_current_residue(ps,es)
        a=rng.normal()+1j*rng.normal();b=rng.normal()+1j*rng.normal();Ns=N+a*P;Js=J+b*P
        assert abs(r29.dotc(Ns,Ns)-r29.dotc(N,N))<2e-9*max(1.,abs(r29.dotc(N,N)))
        assert abs(r29.dotc(Js,Js)-r29.dotc(J,J))<2e-9*max(1.,abs(r29.dotc(J,J)))
        assert abs(r29.dotc(Ns,Js)-R)<2e-9*max(1.,abs(R))

def test_mixed_copy_control_activates_trace_or_antisymmetric_tensor_coordinates():
    rng=np.random.default_rng(20261014);witness=False
    for _ in range(20):
        lam,til=r29.family(0.,r29.make_base(rng));ps=r29.ps_from_spin(lam,til)
        eL=r29.helicity_es(lam,til,neg=(0,2));eR=r29.helicity_es(lam,til,neg=(2,3));_,NL,JL=r29.factor_current_residue(ps,eL);_,NR,JR=r29.factor_current_residue(ps,eR)
        measure=max(abs(tensor_trace(NL,NR)),abs(tensor_trace(JL,JR)),antisym_norm(NL,NR),antisym_norm(JL,JR))
        if measure>1e-4:witness=True
    assert witness

def test_holomorphic_factorization_branch_suppresses_the_two_negative_pair_and_supports_matching_spin2_channels():
    rng=np.random.default_rng(20261015)
    for _ in range(15):
        lam,til=r29.family(0.,r29.make_base(rng));ps=r29.ps_from_spin(lam,til)
        Rwrong,_,_=r29.factor_current_residue(ps,r29.helicity_es(lam,til,neg=(0,1)))
        Rgood,_,_=r29.factor_current_residue(ps,r29.helicity_es(lam,til,neg=(0,2)))
        assert abs(Rwrong)<2e-10*max(1.,abs(Rgood));assert abs(Rgood)>1e-8

def test_rfg30_graph_residue_equals_pure_spin2_current_product_on_matched_copy_branch():
    rng=np.random.default_rng(20261016)
    for _ in range(10):
        base=r29.make_base(rng);lam0,til0=r29.family(0.,base);ps0=r29.ps_from_spin(lam0,til0);es0=r29.helicity_es(lam0,til0,neg=(0,2));RL,N,JL=r29.factor_current_residue(ps0,es0);orderR=[0,1,2,4,3];RR,NR,JR=r29.factor_current_residue([ps0[i] for i in orderR],[es0[i] for i in orderR]);s13=r29.dotc(ps0[0]+ps0[2],ps0[0]+ps0[2]);s23=r29.dotc(ps0[1]+ps0[2],ps0[1]+ps0[2]);Rspin2=(s13+s23)*RL*RR
        lam,til=r29.family(1e-6,base);ps=r29.ps_from_spin(lam,til);es=r29.helicity_es(lam,til,neg=(0,2));s12=r29.dotc(ps[0]+ps[1],ps[0]+ps[1]);Cg=r30.graph_core(ps,es,es,r29.dotc)[0]
        assert abs(s12*Cg+4*Rspin2)<3e-4*max(1.,abs(4*Rspin2))
        mbar=.91;P5=1/mbar**3;Mres=(1j/4)*P5*(s12*Cg);target=-1j*P5*Rspin2
        assert abs(Mres-target)<3e-4*max(1.,abs(target))
