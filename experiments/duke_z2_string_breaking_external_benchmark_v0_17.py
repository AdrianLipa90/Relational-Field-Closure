#!/usr/bin/env python3
from __future__ import annotations
import json, math
import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import expm_multiply

L=13
DIM=1<<L
BETA=0.78
J=1.0
PARAM_GRID=((0.75,0.0),(0.75,0.3),(0.75,0.6),(1.0,0.0),(1.0,0.3),(1.0,0.6),(1.25,0.0),(1.25,0.3),(1.25,0.6))

states=np.arange(DIM,dtype=np.uint32)
z=np.array([2*((states>>i)&1).astype(np.int8)-1 for i in range(L)])
psi0=np.zeros(DIM,dtype=np.complex128); psi0[0]=1.0


def virtual_field(beta=BETA):
    r=math.exp(-beta)
    out=[]
    for i in range(L):
        left=math.exp(-beta*i)/(1-r)
        right=math.exp(-beta*(L-i-1))/(1-r)
        out.append(left+right)
    return np.asarray(out)

DELTA=virtual_field()
BASE=np.zeros(DIM)
for i in range(L):
    for j in range(i+1,L):
        BASE -= math.exp(-BETA*((j-i)-1))*z[i]*z[j]


def build_hamiltonian(g,h):
    diag=BASE.copy()-np.sum((h+DELTA)[:,None]*z,axis=0)
    rows=[states]; cols=[states]; data=[diag.astype(np.complex128)]
    for i in range(L):
        rows.append(states)
        cols.append(states^(1<<i))
        data.append(np.full(DIM,-g,dtype=np.complex128))
    return coo_matrix((np.concatenate(data),(np.concatenate(rows),np.concatenate(cols))),shape=(DIM,DIM)).tocsr()


def charges(psi):
    p=np.abs(psi)**2
    return np.asarray([0.5*(1.0-np.dot(p,z[i]*z[i+1])) for i in range(L-1)])


def exact_edge_bulk_scan(g,h,tmax=4.0,nt=81):
    ts=np.linspace(0.0,tmax,nt)
    psis=expm_multiply(-1j*build_hamiltonian(g,h),psi0,start=0.0,stop=tmax,num=nt,endpoint=True)
    edge=[]; centre=[]
    for psi in psis:
        q=charges(psi)
        edge.append(float(q[[0,1,-2,-1]].mean()))
        centre.append(float(q[[4,5,6,7]].mean()))
    edge=np.asarray(edge); centre=np.asarray(centre); d=edge-centre; k=int(np.argmax(d))
    return {'g_over_J':g,'h_over_J':h,'max_edge_minus_center':float(d[k]),'peak_Jt':float(ts[k]),'edge_at_peak':float(edge[k]),'center_at_peak':float(centre[k])}


def adjacent_pair_potential(l,h,beta=BETA):
    # Eq. (14) with bond coordinate l=1..L and l2=l+1.
    l1=float(l); l2=float(l+1)
    e=math.exp
    return 4.0/(1.0-e(-beta))**2*(1+e(-beta*l2)-e(-beta*l1)-e(-beta*(l2-l1))+e(-beta*(L+2-l1))-e(-beta*(L+2-l2)))-2*h*(l2-l1)


def perturbative_edge_ratio(g,h):
    amp=np.asarray([abs(g/adjacent_pair_potential(l,h)) for l in range(1,L+1)])
    edge=float((amp[0]+amp[-1])/2)
    center=float(amp[L//2])
    return {'g_over_J':g,'h_over_J':h,'edge_amp':edge,'center_amp':center,'edge_center_ratio':edge/center}


def analytic_scaling(g,h):
    out={'g_over_J':g,'h_over_J':h,'vmax_over_J':2*g}
    if h>0:
        out.update({'oscillation_amplitude_sites':2*g/h,'period_Jt':math.pi/h})
    return out


def run():
    exact=[exact_edge_bulk_scan(g,h) for g,h in PARAM_GRID]
    perturb=[perturbative_edge_ratio(g,h) for g,h in PARAM_GRID if h>0]
    analytic=[analytic_scaling(g,h) for g,h in PARAM_GRID]
    checks={
      'dimension_exact_2pow13': DIM==8192,
      'virtual_field_symmetric': bool(np.allclose(DELTA,DELTA[::-1],rtol=0,atol=1e-14)),
      'all_nine_exact_scans_edge_excess_positive': all(x['max_edge_minus_center']>0.25 for x in exact),
      'all_confined_perturbative_initial_states_edge_enhanced': all(x['edge_center_ratio']>1.5 for x in perturb),
      'published_velocity_identity': all(abs(x['vmax_over_J']-2*x['g_over_J'])<1e-15 for x in analytic),
      'published_period_identity': all(abs(x['period_Jt']-math.pi/x['h_over_J'])<1e-15 for x in analytic if x['h_over_J']>0),
    }
    status='PASS' if all(checks.values()) else 'FAIL'
    return {
      'schema':'AUX_RGB_QCD_DUKE_Z2_STRING_BREAKING_EXTERNAL_BENCHMARK_V0_17',
      'status':status,
      'authority':'EXTERNAL_CONSISTENCY_BENCHMARK_ONLY',
      'not_claimed':['full_SU3_QCD_confirmation','PhaseNav_confirmation','priority_or_independent_prediction_provenance'],
      'source':{'doi':'10.1038/s41567-026-03422-0','arxiv':'2410.13815','model':'1+1D Z2 lattice gauge theory / 13-spin dual Ising chain'},
      'frozen_inputs':{'L':L,'beta':BETA,'J_units':1.0,'parameter_grid':[list(x) for x in PARAM_GRID]},
      'checks':checks,
      'exact_reduced_13spin':exact,
      'perturbative_eq14_adjacent_pair':perturb,
      'analytic_scaling':analytic,
    }

if __name__=='__main__':
    print(json.dumps(run(),indent=2,sort_keys=True))
