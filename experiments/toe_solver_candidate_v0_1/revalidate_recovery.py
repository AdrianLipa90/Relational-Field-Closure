from __future__ import annotations
import json, math, hashlib, time, sys
from pathlib import Path
import numpy as np
D=Path(__file__).parent
sys.path.insert(0,str(D))
import adm_metric_field_provider_candidate as adm
import metric_jet_provider_candidate as jet
import gmn_einstein_provider_candidate as ein
import rfn0_rf02h_metric_provider_candidate as rfn
import qhtri_neutrino_total_stress_binding_candidate as neu
import gsc3a_gsc4b_shift_route_candidate as shift
import local_einstein_closure_solver_candidate as loc
import multisector_source_cone_solver_candidate as multi

checks={}; metrics={}
checks['imports']=True
rng=np.random.default_rng(12345); mi=mc=md=0.0
for _ in range(100):
    A=rng.normal(size=(3,3)); H=A.T@A+0.2*np.eye(3); N=float(np.exp(rng.normal(scale=.4))); b=rng.normal(scale=.3,size=3)
    g=adm.adm_metric(N,H,b); gi=adm.adm_inverse(N,H,b); e=np.linalg.cholesky(H).T
    mi=max(mi,float(np.max(np.abs(g@gi-np.eye(4)))))
    mc=max(mc,float(np.max(np.abs(g-adm.coframe_metric(N,e,b)))))
    md=max(md,abs(float(np.linalg.det(g))+N*N*float(np.linalg.det(H))))
checks['adm_100_random']=mi<1e-12 and mc<1e-12 and md<1e-10
metrics.update(adm_max_inverse=mi,adm_max_coframe=mc,adm_max_det=md)
rf=adm.make_metric_fn(lambda x:1+.17*x[1],lambda x:np.eye(3),lambda x:np.zeros(3)); g,dg,ddg=jet.metric_jet_4d(rf,[0,.2,0,0],h=2e-4); _,_,G=ein.curvature_at_point(g,dg,ddg); rindler=max(abs(v) for row in G for v in row)
H0=.07; ds=adm.make_metric_fn(lambda x:1.,lambda x:np.eye(3)*np.exp(2*H0*x[0]),lambda x:np.zeros(3)); g,dg,ddg=jet.metric_jet_4d(ds,[.3,0,0,0],h=2e-4); _,_,G=ein.curvature_at_point(g,dg,ddg); G=np.array(G); g=np.array(g); target=np.zeros((4,4)); target[0,0]=3*H0*H0; target[1:,1:]=-3*H0*H0*g[1:,1:]; dserr=float(np.max(np.abs(G-target)))
checks['rindler_flat']=rindler<1e-6; checks['de_sitter']=dserr<1e-6; metrics.update(rindler_Gmax=rindler,de_sitter_error=dserr)
checks['rfn_lapse']=abs(rfn.relational_lapse(2,1)-2)<1e-15
T=np.array(neu.integrated_massless_stress([(1,0,0),(-1,0,0)],[.5,.5])); eta=np.diag([-1.,1.,1.,1.]); tr=float(np.sum(np.linalg.inv(eta)*T)); checks['neutrino_trace']=abs(tr)<1e-12; metrics['neutrino_trace']=tr
I=((1.,0.,0.),(0.,1.,0.),(0.,0.,1.)); r0=shift.matching_residual(I,(0,0,0),(0,0,0),(0,0,0)); A=((1.,.2,0.),(0.,1.,0.),(0.,0.,1.)); bp=(.3,-.2,.1); v=(.05,-.02,.03); bq=shift.expected_target_shift(A,bp,v); r1=shift.matching_residual(A,bp,v,bq); bad=shift.matching_residual(A,bp,v,(bq[0]+.1,bq[1],bq[2])); checks['shift_route']=r0==0 and r1<1e-15 and bad>.09; metrics.update(shift_valid=r1,shift_bad=bad)
rad=adm.make_metric_fn(lambda x:1.,lambda x:(np.eye(3)*x[0]).tolist(),lambda x:(0,0,0)); gR,dgR,ddgR=jet.metric_jet_4d(rad,(2.,0,0,0),h=1e-4); RR,_,GR=ein.curvature_at_point(gR,dgR,ddgR); sr=loc.solve_positive_massless_pair_closure(GR,gR,tolerance=1e-8)
Hs=(.05,.08,.11)
def hA(x): return np.diag([math.exp(2*H*x[0]) for H in Hs]).tolist()
ani=adm.make_metric_fn(lambda x:1.,hA,lambda x:(0,0,0)); gA,dgA,ddgA=jet.metric_jet_4d(ani,(.3,0,0,0),h=3e-4); RA,_,GA=ein.curvature_at_point(gA,dgA,ddgA); sa=loc.solve_positive_massless_pair_closure(GA,gA,tolerance=1e-8); ua=loc.solve_unconstrained_diagnostic(GA,gA)
checks['radiation_closure']=sr.success and sr.max_abs_residual<1e-12
checks['anisotropic_reject']=not sa.success and ua['requires_negative_stream_coupling'] and ua['max_abs_residual']<1e-12
metrics.update(radiation_residual=sr.max_abs_residual, anisotropic_massless_residual=sa.max_abs_residual, anisotropic_unconstrained_residual=ua['max_abs_residual'])
ss=multi.solve_source_cone(GA,gA,include_scalar=True,tolerance=1e-8); sall=multi.solve_source_cone(GA,gA,include_scalar=True,include_maxwell=True,include_dust=True,tolerance=1e-8)
scalarB=multi.scalar_amplitude_gradient_bases(eta)[1]; syn=-.03*eta+.17*scalarB; syns=multi.solve_source_cone(syn,eta,include_scalar=True,tolerance=1e-10)
checks['multisector_control']=syns.success and abs(syns.Lambda-.03)<1e-12 and abs(syns.scalar_amp[1]-.17)<1e-12
checks['multisector_anisotropic_reject']=not sall.success and ss.max_abs_residual<sa.max_abs_residual
metrics.update(multisector_scalar_residual=ss.max_abs_residual,multisector_all_residual=sall.max_abs_residual,synthetic_scalar_residual=syns.max_abs_residual,residual_reduction=1-ss.max_abs_residual/sa.max_abs_residual)
ledger=json.loads((D/'conceptnav_closure_ledger_v0_2.json').read_text()); expected=ledger['key_solver_results']
checks['ledger_radiation_match']=abs(metrics['radiation_residual']-expected['radiation_FLRW_massless_closure_max_residual'])<1e-14
checks['ledger_anisotropic_match']=abs(metrics['anisotropic_massless_residual']-expected['anisotropic_BianchiI_massless_only_residual'])<1e-9
checks['ledger_multisector_match']=abs(metrics['multisector_scalar_residual']-expected['anisotropic_BianchiI_massless_plus_RF_E7_scalar_residual'])<1e-9
status='PASS' if all(checks.values()) else 'FAIL'
out={'schema':'QHTRI_TOE_RECOVERY_REVALIDATION_V1','status':status,'authority':'CANDIDATE_ONLY','canon_allowed':False,'recovery_mode':'EXACT_COMMAND_HISTORY_RECOVERY_PLUS_FRESH_REVALIDATION','checks':checks,'metrics':metrics,'archived_ledger_sha256':ledger['ledger_sha256'],'source_main_commit':'85bbb1d0754605be2720b6bd258b486b0a072345','created_unix_ns':time.time_ns()}
raw=json.dumps(out,sort_keys=True,separators=(',',':')).encode(); out['receipt_sha256']=hashlib.sha256(raw).hexdigest(); (D/'recovery_revalidation_v1.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(json.dumps(out,indent=2,sort_keys=True))
raise SystemExit(0 if status=='PASS' else 1)
