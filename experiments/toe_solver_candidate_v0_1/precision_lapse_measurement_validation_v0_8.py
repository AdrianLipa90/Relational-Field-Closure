from __future__ import annotations
import json, math
from decimal import Decimal, getcontext, localcontext
from pathlib import Path
from precision_lapse_measurement_candidate_v0_8 import (
    PrecisionClockError, log_ratio_from_fractional_offset,
    fractional_offset_from_log_ratio, reconstruct_log_clock_potential,
    weighted_slope_through_origin, stable_receipt_sha,
)

SOURCE = {
    'doi':'10.5281/zenodo.8184043',
    'record_url':'https://zenodo.org/records/8184043',
    'file':'Fig3.csv',
    'fig3_md5':'257eab6f29cf3480c536cac73ed3998a',
    'evidence_class':'EXTERNAL_PROCESS_DATA_REFERENCE',
    'physical_production_claim':False,
}
X=['0.25','0.5','0.75','1.0']
Y_1E19=['-2.943597600750136','-6.43016785640077','-8.427872488195288','-11.955018632210269']
S_1E19=['0.6867700606639362','0.5087085144387439','0.660633464684558','1.1305939800725837']
EXPECTED_SLOPE='-11.931497812058647330178150456210840554320038300818627288826189506893919006324977'
EXPECTED_SIGMA='0.56167907568042397202224492309163135908706507721062290379612341792725309068448916'


def delta(v): return Decimal(v)*Decimal('1e-19')

def run():
    checks=[]
    def record(name, ok, detail):
        checks.append({'name':name,'status':'PASS' if ok else 'FAIL','detail':detail})

    collapsed=[]
    for v in Y_1E19:
        d=float(Decimal(v)*Decimal('1e-19'))
        collapsed.append((1.0+d)==1.0)
    record('legacy_float64_collapses_all_four_real_data_offsets', all(collapsed), {'collapsed':collapsed})

    max_round=Decimal(0)
    for v in Y_1E19:
        d=delta(v)
        l=log_ratio_from_fractional_offset(str(d),precision=80)
        back=fractional_offset_from_log_ratio(str(l),precision=80)
        max_round=max(max_round,abs(back-d))
    record('decimal_log_ratio_roundtrip_real_data', max_round==0, {'max_abs_error':str(max_round)})

    edges=[]
    for i,v in enumerate(Y_1E19,1):
        l=log_ratio_from_fractional_offset(str(delta(v)),precision=80)
        edges.append((f'h{i}','h0',str(l)))
    cert=reconstruct_log_clock_potential(edges,reference='h0',tolerance_log='1e-40',precision=80)
    record('real_data_star_reconstruction_exact_at_80_digits', Decimal(cert.max_log_residual)==0, {'max_log_residual':cert.max_log_residual,'edge_count':cert.edge_count})

    fit=weighted_slope_through_origin(X,Y_1E19,S_1E19,precision=80)
    record('weighted_fig3b_slope_reproduced', fit.slope==EXPECTED_SLOPE and fit.sigma_slope==EXPECTED_SIGMA, {'slope':fit.slope,'sigma':fit.sigma_slope,'chi2':fit.chi2,'dof':fit.dof})

    l1=log_ratio_from_fractional_offset(str(delta(Y_1E19[0])),precision=80)
    l2=log_ratio_from_fractional_offset(str(delta(Y_1E19[1])),precision=80)
    direct=(l2-l1)+Decimal('1e-22')
    bad=[('h1','h0',str(l1)),('h2','h0',str(l2)),('h2','h1',str(direct))]
    detected=False; reason=''
    try:
        reconstruct_log_clock_potential(bad,reference='h0',tolerance_log='1e-30',precision=80)
    except PrecisionClockError as exc:
        detected=True; reason=str(exc)
    record('injected_1e-22_cycle_defect_detected', detected, {'reason':reason})

    getcontext().prec=28
    d=delta(Y_1E19[0])
    with localcontext() as ctx:
        ctx.prec=80
        l=(Decimal(1)+d).ln()
    broken=-l
    legacy_loss=broken+l
    fixed=l.copy_negate()+l
    record('decimal_unary_negation_context_regression_fixed', legacy_loss!=0 and fixed==0, {'legacy_loss':str(legacy_loss),'fixed_loss':str(fixed)})

    passed=sum(c['status']=='PASS' for c in checks)
    receipt={
        'schema':'QHTRI_TOE_PRECISION_LAPSE_REALDATA_VALIDATION_V0_8',
        'status':'PASS' if passed==len(checks) else 'FAIL',
        'authority':'CANDIDATE_ONLY','canon_allowed':False,
        'source':SOURCE,'checks':checks,'passed':passed,'failed':len(checks)-passed,
        'precision_digits':80,
        'firewall':'Real external process data are used as a precision benchmark only. This receipt is not an IDT production capture and makes no physical-production claim.'
    }
    receipt['receipt_sha256']=stable_receipt_sha(receipt)
    return receipt

if __name__=='__main__':
    r=run(); print(json.dumps(r,indent=2,sort_keys=True)); raise SystemExit(0 if r['status']=='PASS' else 1)
