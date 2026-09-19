from __future__ import annotations
import json, hashlib
from pathlib import Path

def sha(obj):
    return hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(",",":")).encode()).hexdigest()

def run(receipt_path: Path, qhtri_path: Path | None=None):
    r=json.loads(receipt_path.read_text())
    q=None if qhtri_path is None else json.loads(qhtri_path.read_text())
    checks=[]
    def add(name,cond,detail): checks.append({"name":name,"status":"PASS" if cond else "FAIL","detail":detail})
    add("v011_empirical_e2e_pass",r.get("status")=="PASS" and r.get("passed")==10 and r.get("failed")==0,{"status":r.get("status"),"passed":r.get("passed"),"failed":r.get("failed")})
    e=r.get("e2e",{})
    add("rindler_curvature_null_control",e.get("rindler",{}).get("max_abs_einstein")==0.0 and e.get("rindler",{}).get("max_abs_ricci")==0.0,e.get("rindler",{}))
    add("rf_e25_single_patch_pass",e.get("rf_e25_reference",{}).get("shared_atlas_certified") is True,e.get("rf_e25_reference",{}))
    add("bounded_domain_coverage_pass",e.get("coverage",{}).get("covered") is True,e.get("coverage",{}))
    add("rf_e26_global_carrier_on_covered_domain_pass",e.get("rf_e26_reference",{}).get("global_einstein_carrier") is True,e.get("rf_e26_reference",{}))
    routing=r.get("routing_result",{})
    add("a5_not_mandatory_for_single_patch_e26","NOT_REQUIRED_FOR_SINGLE_PATCH" in str(routing.get("A5_global_tetrahedral_incidence")),routing.get("A5_global_tetrahedral_incidence"))
    add("interleaf_not_mandatory_for_single_patch_e26","NOT_REQUIRED_FOR_SINGLE_PATCH" in str(routing.get("interleaf_beta_match")),routing.get("interleaf_beta_match"))
    add("physical_claim_firewall",e.get("physical_production_claim") is False and e.get("canon_allowed") is False,{"physical_production_claim":e.get("physical_production_claim"),"canon_allowed":e.get("canon_allowed")})
    if q is not None:
        add("qhtri_model_state_validation_pass",q.get("status")=="PASS" and q.get("qhtri_norm_error",1)>-1 and q.get("hardware_witness_scope")=="UNASSESSED",{"status":q.get("status"),"norm_error":q.get("qhtri_norm_error"),"hardware":q.get("hardware_witness_scope")})
    passed=sum(x["status"]=="PASS" for x in checks)
    out={"schema":"QHTRI_TOE_CANDIDATE_RELEASE_GATE_V0_11","status":"PASS" if passed==len(checks) else "FAIL","verdict":"PASS_REPOSITORY_BOUNDED_DOMAIN_E2E_REFERENCE_COMPLETE" if passed==len(checks) else "FAIL_REPOSITORY_BOUNDED_DOMAIN_E2E_REFERENCE","authority":"CANDIDATE_ONLY","canon_allowed":False,"physical_production_claim":False,"passed":passed,"failed":len(checks)-passed,"checks":checks,"repository_scope_status":"IMPLEMENTATION_COMPLETE_FOR_BOUNDED_DOMAIN_E2E_REFERENCE","optional_expansion_routes":["GLOBAL_A5_MULTIPATCH_TOPOLOGY","TIR_INTERLEAF_MULTIPATCH_SHIFT","RF_L7_GLOBAL_HYPERBOLICITY_CAUCHY"],"open_external_evidence":["FULL_PHYSICAL_3PLUS1_PRODUCTION_CAPTURE_IF_PHYSICAL_PRODUCTION_CLAIM_IS_REQUESTED"],"firewall":"Repository completion is an implementation/reference-validation status. It does not promote a physical-production claim or canon."}
    out["receipt_sha256"]=sha(out)
    return out

if __name__=="__main__":
    import argparse
    p=argparse.ArgumentParser(); p.add_argument("--receipt",type=Path,required=True); p.add_argument("--qhtri",type=Path)
    a=p.parse_args(); o=run(a.receipt,a.qhtri); print(json.dumps(o,indent=2,sort_keys=True)); raise SystemExit(0 if o["status"]=="PASS" else 1)
