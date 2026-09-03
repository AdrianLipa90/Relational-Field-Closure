from __future__ import annotations
import copy, json
from decimal import Decimal
from empirical_rindler_bounded_e2e_v0_11 import *

def run():
    checks=[]
    def check(name, ok, detail):
        checks.append({"name":name,"status":"PASS" if ok else "FAIL","detail":detail})
    gamma=empirical_gamma_per_m()
    gsig=empirical_gamma_sigma_per_m()
    check("empirical_gradient_nonzero_and_finite", gamma!=0 and gsig>0, {"gamma_per_m":str(gamma),"sigma":str(gsig)})
    n1=legacy_endpoint_lapse_float64(0.01)
    check("legacy_float64_lapse_collapses_over_1cm", n1==1.0, {"float64_N_at_1cm":repr(n1),"decimal_delta_at_1cm":str(gamma*Decimal("0.01"))})
    g,dg,ddg=rindler_analytic_jet(0.0)
    analytic_dg=dg[3][0][0]
    analytic_ddg=ddg[3][3][0][0]
    check("precision_safe_analytic_jet_retains_signal", analytic_dg!=0.0 and analytic_ddg!=0.0,{"dg_z_g00":analytic_dg,"ddg_zz_g00":analytic_ddg})
    scalar,ricci,G=curvature_at_point(g,dg,ddg)
    gmax=max(abs(v) for row in G for v in row)
    rmax=max(abs(v) for row in ricci for v in row)
    check("empirically_calibrated_rindler_is_flat", gmax<1e-45 and rmax<1e-45 and abs(scalar)<1e-45,{"Gmax":gmax,"RicciMax":rmax,"R":scalar})
    bad=copy.deepcopy(ddg)
    bad[3][3][0][0] *= 1.01
    _,_,Gb=curvature_at_point(g,dg,bad)
    gbmax=max(abs(v) for row in Gb for v in row)
    check("one_percent_second_derivative_defect_detected", gbmax>1e-37, {"Gmax_bad":gbmax})
    rec=run_e2e()
    check("rf_e25_single_patch_shared_atlas_reference_pass",rec["rf_e25_reference"]["shared_atlas_certified"] and rec["rf_e25_reference"]["patch_count"]==1 and rec["rf_e25_reference"]["overlap_count"]==0,rec["rf_e25_reference"])
    check("explicit_bounded_domain_coverage_pass", rec["coverage"]["covered"], rec["coverage"])
    check("rf_e26_single_patch_bounded_domain_global_carrier_pass",rec["rf_e26_reference"]["global_einstein_carrier"] and rec["rf_e26_reference"]["max_local_residual"]<1e-28,rec["rf_e26_reference"])
    d=reference_domain()
    bad_domain=BoundedDomain(d.domain_id,d.x0_min_m,d.x0_max_m,d.x_min_m,d.x_max_m,d.y_min_m,d.y_max_m,d.z_min_m,d.z_max_m+0.001)
    check("coverage_extension_beyond_patch_rejected", not domain_contains(d,bad_domain), {"patch_zmax":d.z_max_m,"target_zmax":bad_domain.z_max_m})
    check("claim_firewall_remains_nonproduction",rec["evidence_class"]=="EXTERNAL_EMPIRICAL_RINDLER_CALIBRATED_REFERENCE" and rec["physical_production_claim"] is False and rec["canon_allowed"] is False,{"evidence_class":rec["evidence_class"],"physical_production_claim":rec["physical_production_claim"],"canon_allowed":rec["canon_allowed"]})
    passed=sum(x["status"]=="PASS" for x in checks)
    out={"schema":"QHTRI_TOE_EMPIRICAL_RINDLER_BOUNDED_E2E_VALIDATION_V0_11","status":"PASS" if passed==len(checks) else "FAIL","authority":"CANDIDATE_ONLY","canon_allowed":False,"physical_production_claim":False,"passed":passed,"failed":len(checks)-passed,"checks":checks,"e2e":rec,"routing_result":{"A5_global_tetrahedral_incidence":"OPTIONAL_GLOBAL_MULTIPATCH_ROUTE_NOT_REQUIRED_FOR_SINGLE_PATCH_RF_E25_RF_E26","interleaf_beta_match":"OPTIONAL_MULTIPATCH_ROUTE_NOT_REQUIRED_FOR_SINGLE_PATCH_RF_E25_RF_E26","bounded_domain_e26":"EXECUTABLE_REFERENCE_ROUTE"}}
    out["receipt_sha256"]=stable_sha(out)
    return out

if __name__=="__main__":
    r=run(); print(json.dumps(r,indent=2,sort_keys=True)); raise SystemExit(0 if r["status"]=="PASS" else 1)
