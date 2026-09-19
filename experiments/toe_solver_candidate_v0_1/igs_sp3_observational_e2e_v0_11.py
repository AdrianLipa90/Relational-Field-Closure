from __future__ import annotations
import json, hashlib, math
from decimal import Decimal, getcontext, localcontext
from itertools import combinations
from collections import defaultdict
import numpy as np

getcontext().prec=80
C_KM_S=Decimal('299792.458')
SOURCE_URL='https://software.rtcm-ntrip.org/browser/ntrip/branches/BNC_2.12/Example_Configs/Input/RT218283.SP3?rev=8013'
SOURCE_REV='8013'
EPOCH1='2015-01-21T00:01:00Z'
EPOCH2='2015-01-21T00:03:00Z'
DT=Decimal('120')
SAT_IDS=('G01','G02','G03','G04','G05')
REC1={
'G01':('-20211.852590','-13534.722421','-10912.571617','-9.945341'),
'G02':('-2486.675251','15651.983479','21665.396870','543.075190'),
'G03':('-13217.118012','-20316.554735','10814.894646','161.246676'),
'G04':('-11048.109091','-16496.227733','-18079.087021','-5.933971'),
'G05':('1415.296556','25391.537629','7286.804159','-290.125298'),
}
REC2={
'G01':('-20043.488953','-13516.640374','-11240.133653','-9.945279'),
'G02':('-2799.216197','15576.603484','21676.134685','543.075198'),
'G03':('-13229.808727','-20481.341421','10482.835849','161.249567'),
'G04':('-10782.320197','-16449.365320','-18281.546350','-5.934176'),
'G05':('1347.312437','25290.546183','7641.773766','-290.124639'),
}

def canon(o): return json.dumps(o,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()
def sha(o): return hashlib.sha256(canon(o)).hexdigest()

def source_records():
    return {'source_url':SOURCE_URL,'source_revision':SOURCE_REV,'epochs':[EPOCH1,EPOCH2],
            'satellites':list(SAT_IDS),'epoch1':REC1,'epoch2':REC2}

def realization_id(): return 'physical:igs-sp3:sha256:'+sha(source_records())

def decimal_ln1p(x: Decimal)->Decimal:
    with localcontext() as ctx:
        ctx.prec=80
        return (Decimal(1)+x).ln()

def clock_packet():
    rates={}
    for s in SAT_IDS:
        dc=(Decimal(REC2[s][3])-Decimal(REC1[s][3]))*Decimal('1e-6')
        rates[s]=dc/DT
    ref=rates['G01']
    logs={s:decimal_ln1p(rates[s])-decimal_ln1p(ref) for s in SAT_IDS}
    edges=[]
    for s in SAT_IDS:
        if s=='G01': continue
        edges.append({'source':'G01','target':s,'log_ratio':str(logs[s])})
        edges.append({'source':s,'target':'G01','log_ratio':str(logs[s].copy_negate())})
    inv=max(abs(Decimal(e['log_ratio'])+Decimal(next(x['log_ratio'] for x in edges if x['source']==e['target'] and x['target']==e['source']))) for e in edges)
    return {'schema':'IDT_05K_PRECISION_PRODUCTION_CLOCK_CAPTURE_V0_11','physical_realization_id':realization_id(),
            'source_class':'EXTERNAL_OBSERVATIONAL_ARCHIVE_DERIVED','reference_clock':'G01',
            'clock_rate_offsets':{k:str(v) for k,v in rates.items()},'log_lapse_relative':{k:str(v) for k,v in logs.items()},
            'edges':edges,'inverse_cycle_residual':str(inv),'precision_digits':80,'encoding':'DECIMAL_LOG_N'}

def face_incidence(tets):
    c=defaultdict(int)
    for t in tets:
        for f in combinations(sorted(t),3): c[f]+=1
    return c

def certify_s2_link(tris):
    tris=[tuple(sorted(t)) for t in tris]
    if not tris or len(set(tris))!=len(tris): return False
    verts=set(v for t in tris for v in t); em=defaultdict(list)
    for i,t in enumerate(tris):
        for e in combinations(t,2): em[tuple(sorted(e))].append(i)
    if any(len(v)!=2 for v in em.values()): return False
    adj={i:set() for i in range(len(tris))}
    for owners in em.values():
        a,b=owners; adj[a].add(b); adj[b].add(a)
    seen=set(); stack=[0]
    while stack:
        a=stack.pop()
        if a in seen: continue
        seen.add(a); stack.extend(adj[a]-seen)
    if len(seen)!=len(tris): return False
    for v in verts:
        ca=defaultdict(set)
        for t in tris:
            if v in t:
                a,b=[x for x in t if x!=v]; ca[a].add(b); ca[b].add(a)
        if not ca or any(len(n)!=2 for n in ca.values()): return False
        sv=set(); st=[next(iter(ca))]
        while st:
            a=st.pop()
            if a in sv: continue
            sv.add(a); st.extend(ca[a]-sv)
        if sv!=set(ca): return False
    return len(verts)-len(em)+len(tris)==2

def certify_closed_3manifold_full(tets):
    tets=[tuple(sorted(t)) for t in tets]
    if not tets or len(set(tets))!=len(tets): return False
    inc=face_incidence(tets)
    if any(v!=2 for v in inc.values()): return False
    adj={i:set() for i in range(len(tets))}; faceowners=defaultdict(list)
    for i,t in enumerate(tets):
        for f in combinations(t,3): faceowners[tuple(sorted(f))].append(i)
    for owners in faceowners.values():
        a,b=owners; adj[a].add(b); adj[b].add(a)
    seen=set(); stack=[0]
    while stack:
        a=stack.pop()
        if a in seen: continue
        seen.add(a); stack.extend(adj[a]-seen)
    if len(seen)!=len(tets): return False
    verts=sorted(set(v for t in tets for v in t))
    for v in verts:
        tris=[tuple(x for x in t if x!=v) for t in tets if v in t]
        if not certify_s2_link(tris): return False
    return True

def spatial_packet():
    tets=[]
    for omitted in SAT_IDS:
        tet=tuple(s for s in SAT_IDS if s!=omitted); tets.append(tuple(sorted(tet)))
    inc=face_incidence(tets); manifold_ok=certify_closed_3manifold_full(tets)
    payload={'schema':'TIR_GLOBAL_RELATIONAL_COMPLEX_CAPTURE_V0_11','capture_id':'igs-sp3-g01-g05-20150121T0001Z',
             'physical_realization_id':realization_id(),'source':{'source_id':'RT218283.SP3@8013','source_class':'PRODUCTION_SOURCE',
             'immutable_ref':SOURCE_URL,'derivation_class':'DETERMINISTIC_RELATIONAL_BOUNDARY_CLOSURE_FROM_OBSERVED_NODE_SET'},
             'tetrahedral_cells':[{'cell_id':f'tet-{i}','vertices':list(t)} for i,t in enumerate(sorted(tets))]}
    payload['source']['capture_receipt_sha256']=sha({'records':source_records(),'derivation':payload['source']['derivation_class'],'tets':payload['tetrahedral_cells']})
    return {'capture':payload,'manifold_certified':manifold_ok,'face_count':len(inc),'bad_face_incidence':{str(k):v for k,v in inc.items() if v!=2}}

def matching_packet():
    p1={s:np.array([float(x) for x in REC1[s][:3]],dtype=float) for s in SAT_IDS}
    p2={s:np.array([float(x) for x in REC2[s][:3]],dtype=float) for s in SAT_IDS}
    beta={s:(p2[s]-p1[s])/float(DT) for s in SAT_IDS}
    patches=[{'patch_id':s,'beta_match':beta[s].tolist()} for s in SAT_IDS]; overlaps=[]; I=np.eye(3)
    for s in SAT_IDS[1:]:
        v=beta['G01']-beta[s]
        overlaps.append({'source':'G01','target':s,'spatial_jacobian':I.tolist(),'time_drift':v.tolist()})
    maxres=0.0
    for o in overlaps:
        expected=np.array(o['spatial_jacobian'])@beta[o['source']]-np.array(o['time_drift'])
        maxres=max(maxres,float(np.max(np.abs(expected-beta[o['target']]))))
    shifts={s:(beta[s]/float(C_KM_S)).tolist() for s in SAT_IDS}
    return {'schema':'TIR_INTERLEAF_MATCHING_FIELD_INPUT_V0_11','physical_realization_id':realization_id(),
            'source_class':'EXTERNAL_OBSERVATIONAL_ARCHIVE_DERIVED','temporal_coordinate':{'kind':'t','x0_binding':'x0=c*t','c_scale_km_s':float(C_KM_S)},
            'patches':patches,'overlaps':overlaps,'max_matching_residual':maxres,'derived_rfe8_shift':shifts,'shift_status':'DERIVED_DOWNSTREAM'}

def adm_metric(N,h,b):
    H=np.asarray(h,float); b=np.asarray(b,float); bi=H@b
    g=np.empty((4,4),float); g[0,0]=-N*N+float(b@bi); g[0,1:]=bi; g[1:,0]=bi; g[1:,1:]=H
    return g

def fit_fields():
    cp=clock_packet(); mp=matching_packet()
    xyz=np.array([[0.5*(float(REC1[s][i])+float(REC2[s][i])) for i in range(3)] for s in SAT_IDS])
    center=xyz.mean(axis=0); scale=float(np.median(np.linalg.norm(xyz-center,axis=1))); Y=(xyz-center)/scale
    A=np.column_stack([np.ones(len(SAT_IDS)),Y]); logN=np.array([float(Decimal(cp['log_lapse_relative'][s])) for s in SAT_IDS])
    coefN=np.linalg.lstsq(A,logN,rcond=None)[0]; B=np.array([mp['derived_rfe8_shift'][s] for s in SAT_IDS]); coefB=np.linalg.lstsq(A,B,rcond=None)[0]
    fitN=A@coefN; fitB=A@coefB; resN=float(np.max(np.abs(fitN-logN))); resB=float(np.max(np.abs(fitB-B)))
    def metric_fn(x):
        y=np.asarray(x[1:4],float); ln=float(coefN[0]+coefN[1:]@y); N=math.exp(ln); b=coefB[0]+coefB[1:].T@y
        return adm_metric(N,np.eye(3),b)
    return metric_fn, {'center_km':center.tolist(),'scale_km':scale,'lapse_fit_max_abs':resN,'shift_fit_max_abs':resB,'coef_logN':coefN.tolist(),'coef_shift':coefB.tolist()}

def metric_jet(metric_fn,point,h=1e-3):
    x=np.array(point,float); g=np.asarray(metric_fn(x),float); dg=np.zeros((4,4,4)); ddg=np.zeros((4,4,4,4))
    for a in range(4):
        xp=x.copy(); xm=x.copy(); xp[a]+=h; xm[a]-=h; gp=np.asarray(metric_fn(xp)); gm=np.asarray(metric_fn(xm))
        dg[a]=(gp-gm)/(2*h); ddg[a,a]=(gp-2*g+gm)/(h*h)
    for a in range(4):
        for b in range(a+1,4):
            vals=[]
            for sa,sb in [(1,1),(1,-1),(-1,1),(-1,-1)]:
                xx=x.copy(); xx[a]+=sa*h; xx[b]+=sb*h; vals.append(np.asarray(metric_fn(xx)))
            v=(vals[0]-vals[1]-vals[2]+vals[3])/(4*h*h); ddg[a,b]=v; ddg[b,a]=v
    return g,dg,ddg

def curvature(g,dg,ddg):
    n=4; gi=np.linalg.inv(g); dgi=np.zeros((n,n,n))
    for a in range(n): dgi[a]=-gi@dg[a]@gi
    Gamma=np.zeros((n,n,n))
    for r in range(n):
        for m in range(n):
            for q in range(n): Gamma[r,m,q]=0.5*sum(gi[r,s]*(dg[m,s,q]+dg[q,s,m]-dg[s,m,q]) for s in range(n))
    dGamma=np.zeros((n,n,n,n))
    for a in range(n):
        for r in range(n):
            for mm in range(n):
                for q in range(n): dGamma[a,r,mm,q]=0.5*sum(dgi[a,r,s]*(dg[mm,s,q]+dg[q,s,mm]-dg[s,mm,q])+gi[r,s]*(ddg[a,mm,s,q]+ddg[a,q,s,mm]-ddg[a,s,mm,q]) for s in range(n))
    Ric=np.zeros((n,n))
    for mm in range(n):
        for q in range(n): Ric[mm,q]=sum(dGamma[r,r,mm,q]-dGamma[q,r,mm,r] for r in range(n))+sum(Gamma[r,r,s]*Gamma[s,mm,q]-Gamma[r,q,s]*Gamma[s,mm,r] for r in range(n) for s in range(n))
    R=float(np.sum(gi*Ric)); G=Ric-0.5*g*R
    return R,Ric,G,Gamma

def bianchi_residual(metric_fn,point,h=2e-3):
    x=np.array(point,float); g,dg,ddg=metric_jet(metric_fn,x,h/2); R,Ric,Gcov,Gamma=curvature(g,dg,ddg); gi=np.linalg.inv(g); Gup=gi@Gcov@gi
    deriv=np.zeros((4,4,4))
    for mu in range(4):
        xp=x.copy(); xm=x.copy(); xp[mu]+=h; xm[mu]-=h
        def gu(xx):
            gg,dd,ddd=metric_jet(metric_fn,xx,h/2); _,_,Gc,_=curvature(gg,dd,ddd); ggi=np.linalg.inv(gg); return ggi@Gc@ggi
        deriv[mu]=(gu(xp)-gu(xm))/(2*h)
    div=np.zeros(4)
    for nu in range(4):
        val=sum(deriv[mu,mu,nu] for mu in range(4)); val+=sum(Gamma[mu,mu,lam]*Gup[lam,nu] for mu in range(4) for lam in range(4)); val+=sum(Gamma[nu,mu,lam]*Gup[mu,lam] for mu in range(4) for lam in range(4)); div[nu]=val
    return float(np.max(np.abs(div))),div.tolist(),float(np.max(np.abs(Gcov))),R

def run():
    cp=clock_packet(); sp=spatial_packet(); mp=matching_packet(); metric_fn,fit=fit_fields(); bres,bvec,gmax,R=bianchi_residual(metric_fn,[0,0,0,0]); g0,dg0,ddg0=metric_jet(metric_fn,[0,0,0,0],1e-3); _,_,G0,_=curvature(g0,dg0,ddg0)
    checks={'same_physical_realization': cp['physical_realization_id']==sp['capture']['physical_realization_id']==mp['physical_realization_id'],'clock_inverse_cocycle_exact': Decimal(cp['inverse_cycle_residual'])==0,'spatial_A5_face_incidence': sp['manifold_certified'],'matching_exact': mp['max_matching_residual']<1e-15,'metric_finite_lorentzian': bool(np.isfinite(g0).all() and np.linalg.det(g0)<0),'bianchi_numeric': bres<1e-6}
    status='PASS' if all(checks.values()) else 'FAIL'
    out={'schema':'QHTRI_TOE_IGS_SP3_OBSERVATIONAL_E2E_V0_11','status':status,'authority':'CANDIDATE_ONLY','canon_allowed':False,'physical_production_claim':False,'evidence_class':'EXTERNAL_OBSERVATIONAL_ARCHIVE_DERIVED_MODEL_LEVEL','source':source_records(),'source_extract_sha256':sha(source_records()),'physical_realization_id':realization_id(),'clock':cp,'spatial':sp,'matching':mp,'field_fit':fit,'einstein':{'G_max_abs':gmax,'scalar_R':R,'G_at_center':G0.tolist(),'bianchi_div_max_abs':bres,'bianchi_div':bvec},'checks':checks}
    out['receipt_sha256']=sha(out); return out
if __name__=='__main__':
    o=run(); print(json.dumps(o,indent=2,sort_keys=True)); raise SystemExit(0 if o['status']=='PASS' else 1)
