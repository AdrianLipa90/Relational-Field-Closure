from __future__ import annotations
import importlib.util, json, math
from pathlib import Path
import numpy as np
M=Path(__file__).with_name('igs_sp3_observational_e2e_v0_11.py')
spec=importlib.util.spec_from_file_location('m',M); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)

def exact_jet(fit, point):
    x=np.asarray(point,float); y=x[1:4]
    a=np.asarray(fit['coef_logN'],float); C=np.asarray(fit['coef_shift'],float)
    ln=a[0]+a[1:]@y; N=math.exp(float(ln)); b=C[0]+C[1:].T@y
    g=m.adm_metric(N,np.eye(3),b); dg=np.zeros((4,4,4)); ddg=np.zeros((4,4,4,4))
    for k in range(3):
        mu=k+1; ak=a[k+1]; Bk=C[k+1]
        dg[mu,0,0]=-2*N*N*ak+2*float(b@Bk)
        for i in range(3): dg[mu,0,i+1]=Bk[i]; dg[mu,i+1,0]=Bk[i]
        for l in range(3):
            nu=l+1; al=a[l+1]; Bl=C[l+1]
            ddg[mu,nu,0,0]=-4*N*N*ak*al+2*float(Bk@Bl)
    return g,dg,ddg

def Gup_exact(fit, point):
    g,dg,ddg=exact_jet(fit,point); R,Ric,G,Gamma=m.curvature(g,dg,ddg); gi=np.linalg.inv(g); return gi@G@gi,Gamma,G,R

def bianchi_exact_metric(fit, h):
    x=np.zeros(4); Gup,Gamma,Gcov,R=Gup_exact(fit,x); deriv=np.zeros((4,4,4))
    for mu in range(4):
        xp=x.copy(); xm=x.copy(); xp[mu]+=h; xm[mu]-=h
        gp=Gup_exact(fit,xp)[0]; gm=Gup_exact(fit,xm)[0]; deriv[mu]=(gp-gm)/(2*h)
    div=np.zeros(4)
    for nu in range(4):
        val=sum(deriv[mu,mu,nu] for mu in range(4))
        val+=sum(Gamma[mu,mu,lam]*Gup[lam,nu] for mu in range(4) for lam in range(4))
        val+=sum(Gamma[nu,mu,lam]*Gup[mu,lam] for mu in range(4) for lam in range(4))
        div[nu]=val
    return float(np.max(np.abs(div))), div, float(np.max(np.abs(Gcov))), R

def run():
    out=m.run(); _,fit=m.fit_fields(); hs=[1e-2,3e-3,1e-3,3e-4,1e-4,3e-5]; sweep=[]
    for h in hs:
        b,v,g,R=bianchi_exact_metric(fit,h); sweep.append({'h':h,'bianchi':b,'Gmax':g,'R':R})
    vals=np.array([x['bianchi'] for x in sweep]); stable=float(np.min(vals))<1e-12 and float(np.median(vals))<1e-10
    checks={'base_observational_e2e_pass': out['status']=='PASS','full_A5_vertex_link_certificate': out['spatial']['manifold_certified'] is True,'single_source_realization': out['checks']['same_physical_realization'] is True,'precision_clock_exact_inverse_cycles': out['checks']['clock_inverse_cocycle_exact'] is True,'matching_failclosed_relation_residual': out['matching']['max_matching_residual']<1e-15,'analytic_metric_bianchi_convergence': bool(stable),'no_physical_truth_promotion': out['physical_production_claim'] is False and out['canon_allowed'] is False}
    status='PASS' if all(checks.values()) else 'FAIL'
    r={'schema':'QHTRI_TOE_IGS_SP3_OBSERVATIONAL_VALIDATION_V0_11','status':status,'checks':checks,'bianchi_sweep':sweep,'source_extract_sha256':out['source_extract_sha256'],'physical_realization_id':out['physical_realization_id'],'evidence_class':out['evidence_class'],'authority':'CANDIDATE_ONLY','canon_allowed':False}
    r['receipt_sha256']=m.sha(r); return r
if __name__=='__main__':
    r=run(); print(json.dumps(r,indent=2,sort_keys=True)); raise SystemExit(0 if r['status']=='PASS' else 1)
