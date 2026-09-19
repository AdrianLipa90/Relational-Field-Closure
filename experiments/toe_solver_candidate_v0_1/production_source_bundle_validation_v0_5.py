from __future__ import annotations
import hashlib, json, sys
from pathlib import Path

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
from production_source_bundle_v0_5 import *

H='a'*64
I=((1.,0.,0.),(0.,1.,0.),(0.,0.,1.))

def prov(cls='REFERENCE_CONTROL',rid=None,seed='a'):
    return SourceProvenance('fixture-'+seed,cls,'fixture://'+seed,(seed*64)[:64] if cls=='PRODUCTION_SOURCE' else None,rid)

def clock_capture(p):
    return ClockCapture(p,(
        ClockActivityEdge('a','r',3.0,2.0),
        ClockActivityEdge('b','a',4.5,3.0),
        ClockActivityEdge('b','r',4.5,2.0),
    ),'r',H,H,True)

def spatial_capture(p):
    return SpatialCapture(p,H,H,True,True,True,True)

def shift_capture(p,wrong=False):
    bp=(2.,-1.,4.); v=(.5,-1.,2.); bq=(2.5, -2.,6.) if wrong else (1.5,0.,2.)
    return ShiftCapture(p,(ShiftPatch('p',bp),ShiftPatch('q',bq)),(ShiftTransition('p','q',I,v),),(),True,True,True)

def expect_error(name,fn,needle):
    try: fn()
    except Exception as e:
        return {'name':name,'pass':needle in str(e),'error':str(e)}
    return {'name':name,'pass':False,'error':'NO_ERROR'}

def main():
    checks=[]
    rp=prov()
    ref=certify_production_bundle(ProductionSourceBundle(clock_capture(rp),spatial_capture(rp),shift_capture(rp)))
    checks.append({'name':'reference_control_never_promotes_production','pass':not ref.production_admitted and set(ref.blockers)=={'CLOCK_SOURCE_WITNESS','SPATIAL_SOURCE_WITNESS','SHIFT_FLOW_SOURCE_WITNESS','SAME_PHYSICAL_REALIZATION_BINDING'},'blockers':list(ref.blockers),'clock_cycle_residual':ref.clock.max_cycle_residual,'shift_overlap_residual':ref.shift.max_shift_overlap_residual})

    cp=prov('PRODUCTION_SOURCE','realization-A','b')
    sp=prov('PRODUCTION_SOURCE','realization-A','c')
    xp=prov('PRODUCTION_SOURCE','realization-B','d')
    mismatch=certify_production_bundle(ProductionSourceBundle(clock_capture(cp),spatial_capture(sp),shift_capture(xp)))
    checks.append({'name':'same_physical_realization_firewall','pass':not mismatch.production_admitted and mismatch.blockers==('SAME_PHYSICAL_REALIZATION_BINDING',),'blockers':list(mismatch.blockers),'individual_ready':[mismatch.clock.production_ready,mismatch.spatial.production_ready,mismatch.shift.production_ready]})

    checks.append(expect_error('clock_nonpositive_activity_fail_closed',lambda: certify_clock_capture(ClockCapture(rp,(ClockActivityEdge('a','r',0.,2.),),'r',H,H,True)),'strictly positive'))
    badcycle=ClockCapture(rp,(ClockActivityEdge('a','r',2.,1.),ClockActivityEdge('b','a',2.,1.),ClockActivityEdge('b','r',3.,1.)),'r',H,H,True)
    checks.append(expect_error('clock_cycle_mismatch_fail_closed',lambda: certify_clock_capture(badcycle),'cycle closure'))
    checks.append(expect_error('shift_wrong_sign_fail_closed',lambda: certify_shift_capture(shift_capture(rp,wrong=True)),'overlap law'))
    badp=SourceProvenance('x','PRODUCTION_SOURCE','immutable','not-a-hash','R')
    checks.append(expect_error('malformed_production_receipt_fail_closed',lambda: badp.validate(),'64-hex'))

    status='PASS' if all(c['pass'] for c in checks) else 'FAIL'
    out={'schema':'QHTRI_TOE_PRODUCTION_SOURCE_BUNDLE_VALIDATION_V0_5','status':status,'authority':'CANDIDATE_ONLY','canon_allowed':False,'physical_production_claim':False,'checks':checks,'summary':{'pass':sum(c['pass'] for c in checks),'fail':sum(not c['pass'] for c in checks)},'interpretation_firewall':'PRODUCTION-shaped fixtures validate gate logic only; they are not physical production evidence.'}
    enc=json.dumps(out,sort_keys=True,indent=2)
    (HERE/'production_source_bundle_receipt_v0_5.json').write_text(enc+'\n')
    print(enc)
    return 0 if status=='PASS' else 1

if __name__=='__main__': raise SystemExit(main())
