from __future__ import annotations
import itertools, json, hashlib, math
from pathlib import Path
import numpy as np

from production_lapse_packet_candidate import ClockRatioEdge, LapseEventEmbedding, fit_affine_log_lapse
from production_spatial_coframe_packet_candidate import RelationalEdgeSample, fit_affine_coframe

ROOT=Path(__file__).resolve().parent


def rz(a):
    c,s=math.cos(a),math.sin(a)
    return np.array([[c,-s,0.],[s,c,0.],[0.,0.,1.]])

def ry(a):
    c,s=math.cos(a),math.sin(a)
    return np.array([[c,0.,s],[0.,1.,0.],[-s,0.,c]])

def patch_coords(X,Q,r0):
    X=np.asarray(X,float); return np.r_[X[0], Q.T@(X[1:]-r0)]

def transition(p,q):
    Qp,rp=p; Qq,rq=q
    A=Qq.T@Qp
    trans=Qq.T@(rp-rq)
    return A,trans

def adm_metric(N,h):
    g=np.zeros((4,4),float); g[0,0]=-float(N)**2; g[1:,1:]=h; return g

def tetra_boundary_complex():
    vertices=tuple('abcde')
    return vertices,tuple(tuple(v for v in vertices if v!=missing) for missing in vertices)

def triangle_incidence(facets):
    counts={}
    for tet in facets:
        for tri in itertools.combinations(sorted(tet),3): counts[tri]=counts.get(tri,0)+1
    return counts


def main():
    rng=np.random.default_rng(4042026)
    angles=[(0.0,0.0),(0.4,-0.2),(-0.35,0.25),(0.7,0.15),(-0.55,-0.3)]
    anchors=[np.array(v,float) for v in [(0,0,0),(0.3,0.1,-0.1),(-0.2,0.25,0.05),(0.1,-0.3,0.2),(-0.25,-0.15,-0.2)]]
    patches={name:(rz(a)@ry(b),anchors[i]) for i,(name,(a,b)) in enumerate(zip('abcde',angles))}

    logN_global=np.array([0.0,0.06,0.025,-0.035,0.02])
    event_global={
      'r':np.array([0.,0.,0.,0.]), 'e1':np.array([1.,0.,0.,0.]),
      'e2':np.array([0.,1.,0.,0.]), 'e3':np.array([0.,0.,1.,0.]),
      'e4':np.array([0.,0.,0.,1.]), 'e5':np.array([1.,.4,-.2,.3]),
      'e6':np.array([.3,-.5,.35,-.25]),
    }
    abs_rates={k:float(np.exp(np.r_[1.,X]@logN_global)) for k,X in event_global.items()}
    edges=[ClockRatioEdge(k,'r',abs_rates[k]/abs_rates['r']) for k in event_global if k!='r']
    edges += [ClockRatioEdge('e5','e2',abs_rates['e5']/abs_rates['e2']),ClockRatioEdge('e6','e3',abs_rates['e6']/abs_rates['e3'])]
    lapse_models={}
    for name,(Q,r0) in patches.items():
        embs=[LapseEventEmbedding(k,tuple(patch_coords(X,Q,r0))) for k,X in event_global.items()]
        lapse_models[name]=fit_affine_log_lapse(edges=edges,embeddings=embs,reference='r',
            provenance_id=f'REFERENCE_CONTROL_IDT_PATCH_{name}',domain_coverage_witness_supplied=True,fit_tolerance=2e-11)

    C=np.zeros((3,3,5),float)
    C[:,:,0]=np.array([[1.15,.04,.01],[.02,1.05,-.025],[.00,.03,.92]])
    C[:,:,1]=np.array([[.008,0,0],[0,.006,0],[0,0,-.004]])
    C[:,:,2]=np.array([[.01,.004,0],[0,.003,0],[.002,0,.005]])
    C[:,:,3]=np.array([[0,.006,.002],[.003,-.004,0],[0,.002,.003]])
    C[:,:,4]=np.array([[.004,0,.005],[0,.004,.002],[.003,0,.002]])
    def e_global(X): return np.einsum('aik,k->ai',C,np.r_[1.,np.asarray(X,float)])

    spatial_models={}
    for name,(Q,r0) in patches.items():
        samples=[]
        for _ in range(120):
            X=rng.uniform([-0.3,-0.45,-0.45,-0.45],[0.8,0.45,0.45,0.45])
            xp=patch_coords(X,Q,r0)
            dxp=rng.normal(size=3); dxp/=np.linalg.norm(dxp)
            E=e_global(X)@(Q@dxp)
            samples.append(RelationalEdgeSample(tuple(xp),tuple(dxp),tuple(E)))
        spatial_models[name]=fit_affine_coframe(samples=samples,provenance_id=f'REFERENCE_CONTROL_TIR_PATCH_{name}',
            overlap_cocycle_witness_supplied=True,domain_coverage_witness_supplied=True,fit_tolerance=3e-11)

    max_lapse_overlap=0.0; max_coframe_overlap=0.0; max_metric_overlap=0.0; max_adm_overlap=0.0
    for p,q in itertools.combinations(patches,2):
        A,trans=transition(patches[p],patches[q])
        J=np.zeros((4,4),float); J[0,0]=1.; J[1:,1:]=A
        for _ in range(12):
            X=rng.uniform([-0.2,-0.3,-0.3,-0.3],[0.6,0.3,0.3,0.3])
            xp=patch_coords(X,*patches[p]); xq=patch_coords(X,*patches[q])
            mapped=np.r_[xp[0], A@xp[1:]+trans]
            if np.max(np.abs(mapped-xq))>1e-12: raise RuntimeError('transition construction error')
            Np=lapse_models[p].lapse(xp); Nq=lapse_models[q].lapse(xq)
            max_lapse_overlap=max(max_lapse_overlap,abs(Np-Nq))
            ep=spatial_models[p].coframe(xp); eq=spatial_models[q].coframe(xq)
            max_coframe_overlap=max(max_coframe_overlap,float(np.max(np.abs(eq@A-ep))))
            hp=ep.T@ep; hq=eq.T@eq
            max_metric_overlap=max(max_metric_overlap,float(np.max(np.abs(A.T@hq@A-hp))))
            gp=adm_metric(Np,hp); gq=adm_metric(Nq,hq)
            max_adm_overlap=max(max_adm_overlap,float(np.max(np.abs(J.T@gq@J-gp))))

    vertices,facets=tetra_boundary_complex(); tri_counts=triangle_incidence(facets)
    topology_ok=(len(vertices)==5 and len(facets)==5 and len(tri_counts)==10 and set(tri_counts.values())=={2})
    bad_counts=triangle_incidence(facets[:-1]); bad_topology_rejected=any(v!=2 for v in bad_counts.values()) or len(bad_counts)!=10

    Xtest=np.array([.2,.1,-.15,.05]); p,q='a','b'; A,_=transition(patches[p],patches[q])
    xp=patch_coords(Xtest,*patches[p]); xq=patch_coords(Xtest,*patches[q])
    tampered_lapse_res=abs(lapse_models[p].lapse(xp)-1.01*lapse_models[q].lapse(xq))
    tampered_coframe_res=float(np.max(np.abs((1.01*spatial_models[q].coframe(xq))@A-spatial_models[p].coframe(xp))))

    checks={
      'five_patch_reference_topology':{'pass':topology_ok,'vertices':len(vertices),'tetrahedra':len(facets),'triangles':len(tri_counts),'triangle_incidence_values':sorted(set(tri_counts.values()))},
      'bad_topology_fail_control':{'pass':bad_topology_rejected},
      'global_lapse_scalar_gluing':{'pass':max_lapse_overlap<1e-11,'max_residual':max_lapse_overlap},
      'global_coframe_solder_gluing':{'pass':max_coframe_overlap<1e-11,'max_residual':max_coframe_overlap},
      'global_spatial_metric_covariance':{'pass':max_metric_overlap<2e-11,'max_residual':max_metric_overlap},
      'global_rf_e8_metric_covariance_zero_shift_reference':{'pass':max_adm_overlap<2e-11,'max_residual':max_adm_overlap},
      'tampered_lapse_overlap_detected':{'pass':tampered_lapse_res>1e-4,'residual':tampered_lapse_res},
      'tampered_coframe_overlap_detected':{'pass':tampered_coframe_res>1e-4,'residual':tampered_coframe_res},
      'flow_adapted_shift_reference_witness':{'pass':True,'shift':[0.,0.,0.],'scope':'REFERENCE_CONTROL_DECLARED_FLOW_ADAPTED'}
    }
    status='PASS' if all(v['pass'] for v in checks.values()) else 'FAIL'
    receipt={
      'schema':'QHTRI_TOE_GLOBAL_REFERENCE_PACKET_INTEGRATION_V0_4','status':status,'authority':'CANDIDATE_ONLY',
      'evidence_scope':'REFERENCE_CONTROL_GLOBAL_MULTI_PATCH_INTEGRATION','reference_source_class':'REFERENCE_CONTROL',
      'patch_count':len(patches),'topology':'BOUNDARY_OF_4_SIMPLEX_REFERENCE_S3_COMPLEX','checks':checks,
      'firewalls':{
        'reference_control_counts_as_production_source':False,
        'declared_reference_domain_coverage_proves_physical_global_coverage':False,
        'flow_adapted_reference_shift_promotes_production_shift':False,
        'global_reference_pass_promotes_canon':False},
      'production_delta_after_pass':[
        'PRODUCTION_IDT_EVENT_CLOCK_RATIO_AND_SMOOTH_DOMAIN_CAPTURE',
        'PRODUCTION_TIR_GLOBAL_RELATIONAL_COMPLEX_AND_EDGE_REFINEMENT_CAPTURE',
        'PRODUCTION_SHIFT_OR_GLOBAL_FLOW_WITNESS']}
    out=ROOT/'global_reference_packet_integration_receipt_v0_4.json'; out.write_text(json.dumps(receipt,indent=2,sort_keys=True)+'\n')
    print(json.dumps(receipt,indent=2,sort_keys=True)); print('sha256',hashlib.sha256(out.read_bytes()).hexdigest())
    if status!='PASS': raise SystemExit(1)

if __name__=='__main__': main()
