from __future__ import annotations
import json, hashlib
from pathlib import Path
import numpy as np

from production_lapse_packet_candidate import (
    ClockRatioEdge,LapseEventEmbedding,fit_affine_log_lapse,ProductionLapsePacketError
)
from production_spatial_coframe_packet_candidate import (
    RelationalEdgeSample,fit_affine_coframe,ProductionSpatialPacketError
)

ROOT=Path(__file__).resolve().parent


def adm_metric(N,h,b):
    N=float(N); h=np.asarray(h,float); b=np.asarray(b,float)
    if not np.isfinite(N) or N<=0 or h.shape!=(3,3) or b.shape!=(3,):
        raise ValueError('bad ADM input')
    if not np.allclose(h,h.T,atol=1e-12) or np.min(np.linalg.eigvalsh(h))<=0:
        raise ValueError('h must be SPD')
    bi=h@b; b2=float(b@bi)
    g=np.empty((4,4),float)
    g[0,0]=-N*N+b2; g[0,1:]=bi; g[1:,0]=bi; g[1:,1:]=h
    return g


def adm_inverse(N,h,b):
    hi=np.linalg.inv(h); b=np.asarray(b,float); N2=N*N
    gi=np.empty((4,4),float)
    gi[0,0]=-1/N2; gi[0,1:]=b/N2; gi[1:,0]=b/N2
    gi[1:,1:]=hi-np.outer(b,b)/N2
    return gi


def main():
    rng=np.random.default_rng(20260902)
    checks={}

    coeff_true=np.array([0.0,0.08,-0.05,0.03,0.02])
    coords={
      'r':np.array([0.,0.,0.,0.]), 'a':np.array([1.,0.,0.,0.]),
      'b':np.array([0.,1.,0.,0.]), 'c':np.array([0.,0.,1.,0.]),
      'd':np.array([0.,0.,0.,1.]), 'e':np.array([1.,1.,1.,1.]),
    }
    rates={k:float(np.exp(np.r_[1.0,x]@coeff_true)) for k,x in coords.items()}
    edges=[ClockRatioEdge(k,'r',rates[k]/rates['r']) for k in coords if k!='r']
    edges.append(ClockRatioEdge('e','a',rates['e']/rates['a']))
    embeddings=[LapseEventEmbedding(k,tuple(x)) for k,x in coords.items()]
    lapse=fit_affine_log_lapse(edges=edges,embeddings=embeddings,reference='r',
        provenance_id='SYNTHETIC_CONTROL_LOG_LAPSE',domain_coverage_witness_supplied=True,
        fit_tolerance=1e-11)
    probe=np.array([0.3,-0.2,0.4,0.1])
    expected=float(np.exp(np.r_[1.0,probe]@coeff_true))
    lapse_err=abs(lapse.lapse(probe)-expected)
    checks['lapse_reconstruction']={'pass':lapse_err<1e-12,'max_error':lapse_err,
        'graph_residual':lapse.graph_residual,'fit_residual':lapse.fit_residual,'rank':lapse.design_rank}

    try:
        bad=list(edges)+[ClockRatioEdge('b','a',2.0*rates['b']/rates['a'])]
        fit_affine_log_lapse(edges=bad,embeddings=embeddings,reference='r',provenance_id='BAD')
        bad_cycle=False
    except ProductionLapsePacketError:
        bad_cycle=True
    checks['lapse_inconsistent_cycle_fail_closed']={'pass':bad_cycle}

    try:
        fit_affine_log_lapse(edges=edges[:3],embeddings=embeddings[:4],reference='r',provenance_id='UNDER')
        under=False
    except ProductionLapsePacketError:
        under=True
    checks['lapse_underdetermined_fail_closed']={'pass':under}

    coeff=np.zeros((3,3,5),float)
    coeff[:,:,0]=np.array([[1.20,0.05,0.02],[0.01,1.10,-0.03],[0.00,0.04,0.95]])
    coeff[:,:,1]=np.array([[.02,0,0],[0,.01,0],[0,0,-.01]])
    coeff[:,:,2]=np.array([[0,.015,0],[.005,0,0],[0,0,.008]])
    coeff[:,:,3]=np.array([[0,0,.01],[0,-.007,0],[.004,0,0]])
    coeff[:,:,4]=np.array([[.006,0,0],[0,.005,.002],[0,0,.004]])
    samples=[]
    for _ in range(80):
        x=rng.uniform(-0.4,0.4,size=4)
        dx=rng.normal(size=3); dx/=np.linalg.norm(dx)
        phi=np.r_[1.0,x]; e=np.einsum('aik,k->ai',coeff,phi); E=e@dx
        samples.append(RelationalEdgeSample(tuple(x),tuple(dx),tuple(E)))
    spatial=fit_affine_coframe(samples=samples,provenance_id='SYNTHETIC_CONTROL_TIR_SOLDER',
        overlap_cocycle_witness_supplied=True,domain_coverage_witness_supplied=True,
        fit_tolerance=1e-11)
    probe2=np.array([0.1,-0.15,0.22,0.07])
    e_true=np.einsum('aik,k->ai',coeff,np.r_[1.0,probe2])
    e_err=float(np.max(np.abs(spatial.coframe(probe2)-e_true)))
    h_true=e_true.T@e_true
    h_err=float(np.max(np.abs(spatial.spatial_metric(probe2)-h_true)))
    checks['coframe_reconstruction']={'pass':max(e_err,h_err)<1e-11,'coframe_error':e_err,'metric_error':h_err,
        'fit_residual':spatial.fit_residual,'rank':spatial.design_rank,'min_abs_det':spatial.min_abs_det_coframe,
        'min_metric_eigenvalue':spatial.min_metric_eigenvalue}

    try:
        bad_samples=[]
        for k in range(30):
            x=np.array([k/30,0,0,0.]); dx=np.array([1.,0,0]); E=np.array([1.,0,0])
            bad_samples.append(RelationalEdgeSample(tuple(x),tuple(dx),tuple(E)))
        fit_affine_coframe(samples=bad_samples,provenance_id='BAD_RANK')
        bad_rank=False
    except ProductionSpatialPacketError:
        bad_rank=True
    checks['coframe_rank_fail_closed']={'pass':bad_rank}

    bshift=np.array([0.04,-0.02,0.01])
    max_inverse=0.0; max_metric=0.0; max_det_factor=0.0
    for _ in range(20):
        x=rng.uniform(-0.3,0.3,size=4)
        N=lapse.lapse(x); h=spatial.spatial_metric(x)
        g=adm_metric(N,h,bshift); gi=adm_inverse(N,h,bshift)
        max_inverse=max(max_inverse,float(np.max(np.abs(g@gi-np.eye(4)))))
        N0=float(np.exp(np.r_[1.0,x]@coeff_true))
        e0=np.einsum('aik,k->ai',coeff,np.r_[1.0,x]); h0=e0.T@e0
        g0=adm_metric(N0,h0,bshift)
        max_metric=max(max_metric,float(np.max(np.abs(g-g0))))
        max_det_factor=max(max_det_factor,abs(float(np.linalg.det(g))+N*N*float(np.linalg.det(h))))
    checks['source_packet_to_rf_e8']={'pass':max(max_inverse,max_metric,max_det_factor)<1e-10,
        'inverse_identity_error':max_inverse,'metric_reconstruction_error':max_metric,
        'det_factorization_error':max_det_factor,
        'production_ready_synthetic_control': bool(lapse.production_ready and spatial.production_ready)}

    status='PASS' if all(v['pass'] for v in checks.values()) else 'FAIL'
    receipt={
      'schema':'QHTRI_TOE_PRODUCTION_METRIC_PACKET_CANDIDATE_V0_3','status':status,
      'authority':'CANDIDATE_ONLY','evidence_scope':'SYNTHETIC_WITNESS_RECONSTRUCTION_AND_FAIL_CLOSED_CONTROLS',
      'source_contracts':{
        'IDT':'positive clock-ratio graph + event embeddings -> local affine log-lapse witness',
        'TIR':'relational edge-generator samples -> local affine coframe witness -> h=e^T e',
        'RFC':'RF-E8 ADM block metric assembly'},
      'firewalls':{
        'finite_event_graph_proves_global_smooth_lapse':False,
        'local_affine_coframe_fit_proves_global_continuum_existence':False,
        'phase_magnitude_aliases_idt_lapse':False,'36d_state_aliases_4d_metric':False},
      'open_production_inputs':[
        'SOURCE_OWNED_CLOCK_RATIO_AND_EVENT_EMBEDDING_PACKET',
        'SOURCE_OWNED_GLOBAL_CLOCK_DOMAIN_COVERAGE_WITNESS',
        'SOURCE_OWNED_RELATIONAL_EDGE_REFINEMENT_PACKET',
        'SOURCE_OWNED_SPATIAL_OVERLAP_COCYCLE_AND_GLOBAL_REFINEMENT_WITNESS',
        'SHIFT_WITNESS_OR_CERTIFIED_FLOW_ADAPTED_ROUTE'],
      'checks':checks}
    out=ROOT/'production_metric_packet_receipt_v0_3.json'
    out.write_text(json.dumps(receipt,indent=2,sort_keys=True)+'\n')
    print(json.dumps(receipt,indent=2,sort_keys=True))
    print('sha256',hashlib.sha256(out.read_bytes()).hexdigest())
    if status!='PASS': raise SystemExit(1)

if __name__=='__main__': main()
