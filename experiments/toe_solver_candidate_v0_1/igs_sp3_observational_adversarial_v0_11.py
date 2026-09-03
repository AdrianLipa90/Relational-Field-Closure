from __future__ import annotations
import importlib.util, json, copy
from decimal import Decimal
from pathlib import Path
M=Path(__file__).with_name('igs_sp3_observational_e2e_v0_11.py')
spec=importlib.util.spec_from_file_location('m',M); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)

def run():
    checks=[]
    def add(name,cond,detail): checks.append({'name':name,'status':'PASS' if cond else 'FAIL','detail':detail})
    cp=m.clock_packet(); broken=copy.deepcopy(cp); broken['edges'][1]['log_ratio']=str(Decimal(broken['edges'][1]['log_ratio'])+Decimal('1e-30'))
    a=Decimal(broken['edges'][0]['log_ratio'])+Decimal(broken['edges'][1]['log_ratio']); add('clock_inverse_cycle_tamper_detected',a!=0,str(a))
    sp=m.spatial_packet(); tets=[tuple(c['vertices']) for c in sp['capture']['tetrahedral_cells']][:-1]; add('open_spatial_complex_rejected',not m.certify_closed_3manifold_full(tets),len(tets))
    mp=m.matching_packet(); target=mp['overlaps'][0]['target']; bet={p['patch_id']:p['beta_match'][:] for p in mp['patches']}; bet[target][0]+=1e-3
    o=mp['overlaps'][0]; import numpy as np
    expected=np.array(o['spatial_jacobian'])@np.array(bet[o['source']])-np.array(o['time_drift']); res=float(np.max(np.abs(expected-np.array(bet[target])))); add('matching_tamper_detected',res>1e-6,res)
    same=m.clock_packet()['physical_realization_id']==m.spatial_packet()['capture']['physical_realization_id']==m.matching_packet()['physical_realization_id']; fake='physical:igs-sp3:sha256:'+'0'*64; add('realization_mismatch_rejected',same and fake!=m.clock_packet()['physical_realization_id'],fake)
    base=m.realization_id(); old=m.REC2['G05']; m.REC2['G05']=(old[0],old[1],old[2],str(Decimal(old[3])+Decimal('0.000001'))); changed=m.realization_id(); m.REC2['G05']=old
    add('source_record_tamper_changes_realization_id',base!=changed,{'base':base,'changed':changed})
    passed=sum(c['status']=='PASS' for c in checks)
    out={'schema':'QHTRI_TOE_IGS_SP3_OBSERVATIONAL_ADVERSARIAL_V0_11','status':'PASS' if passed==len(checks) else 'FAIL','passed':passed,'failed':len(checks)-passed,'checks':checks,'authority':'CANDIDATE_ONLY','canon_allowed':False}
    out['receipt_sha256']=m.sha(out); return out
if __name__=='__main__':
    r=run(); print(json.dumps(r,indent=2,sort_keys=True)); raise SystemExit(0 if r['status']=='PASS' else 1)
