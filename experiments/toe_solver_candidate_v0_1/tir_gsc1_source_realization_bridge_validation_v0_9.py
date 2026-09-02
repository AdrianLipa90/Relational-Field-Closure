from __future__ import annotations
import copy,json
from tir_gsc1_source_realization_bridge_v0_9 import *

SOURCE_DIGEST='1'*64
LOCATOR='snapshot://tir-spatial-realization-R1/source.json'
PHASE_RID='pncs:realization36:sha256:'+'2'*64
PHYSICAL_RID='physical:tir-spatial:R1'

def binding(source_digest=SOURCE_DIGEST, locator=LOCATOR, canon=False):
    return {
      'schema':'PNCS_EXACT_36D_BINDING_V0_18','realization_id':PHASE_RID,
      'content_id':'pncs:file:sha256:'+'3'*64,'basis_id':'TIR_GSC1_SOURCE_CAPTURE_V0_9','derivation_id':'SOURCE_OWNED_SPATIAL_CAPTURE',
      'phase36_sha256':'4'*64,'source_digest_sha256':source_digest,'source_locator':locator,
      'epistemic_operator':'CHYBA','canon_allowed':canon}

def registry(bindings=None):
    bs=list(bindings or [binding()])
    ids=['pncs:binding36:sha256:'+sha256(b) for b in bs]
    payload={'schema':PNCS_RECEIPT_SCHEMA,'binding_ids':sorted(ids),'bindings':bs,'semantic_equivalence_from_vectors':False}
    return {**payload,'receipt_sha256':sha256(payload)}

def capture(source_class='PRODUCTION_SOURCE', receipt=None, physical=PHYSICAL_RID, digest=SOURCE_DIGEST, locator=LOCATOR):
    rec=registry()['receipt_sha256'] if receipt is None else receipt
    source={'source_id':'TIR_SPATIAL_R1','source_class':source_class,'immutable_ref':locator,'source_digest_sha256':digest,'physical_realization_id':physical}
    if source_class=='PRODUCTION_SOURCE': source['capture_receipt_sha256']=rec
    cells=[]
    vertices=['0','1','2','3','4']
    for omit in range(5): cells.append({'cell_id':f'tet-{omit}','vertices':[v for i,v in enumerate(vertices) if i!=omit]})
    return {'schema':CAPTURE_SCHEMA,'capture_id':'tir-gsc1-R1','source':source,'tetrahedral_cells':cells}

def run():
    checks=[]
    def ck(name,fn,expect_error=None):
        try:
            out=fn()
            ok=expect_error is None
            detail=certificate_receipt(out) if hasattr(out,'capture_sha256') else out
        except Exception as e:
            ok=expect_error is not None and expect_error in str(e); detail=str(e)
        checks.append({'name':name,'status':'PASS' if ok else 'FAIL','detail':detail})
    reg=registry()
    ck('production_source_provenance_bridge_pass',lambda:certify_source_realization_bridge(capture(receipt=reg['receipt_sha256']),reg))
    ck('digest_mismatch_fails',lambda:certify_source_realization_bridge(capture(digest='9'*64,receipt=reg['receipt_sha256']),reg),'no PNCS binding matches')
    ck('locator_mismatch_fails',lambda:certify_source_realization_bridge(capture(locator='snapshot://other',receipt=reg['receipt_sha256']),reg),'no PNCS binding matches')
    ck('receipt_mismatch_fails',lambda:certify_source_realization_bridge(capture(receipt='a'*64),reg),'capture receipt does not match')
    badreg=registry(); badreg['bindings'][0]['canon_allowed']=True
    ck('mutated_pncs_receipt_fails_integrity',lambda:certify_source_realization_bridge(capture(receipt=badreg['receipt_sha256']),badreg),'receipt_sha256 mismatch')
    ck('phase_id_cannot_be_used_as_physical_id',lambda:certify_source_realization_bridge(capture(physical=PHASE_RID,receipt=reg['receipt_sha256']),reg),'must remain distinct')
    ref=registry()
    ck('reference_control_never_production_ready',lambda:certify_source_realization_bridge(capture(source_class='REFERENCE_CONTROL'),ref))
    dup=capture(receipt=reg['receipt_sha256']); dup['tetrahedral_cells'][1]['vertices']=dup['tetrahedral_cells'][0]['vertices']
    ck('duplicate_tetrahedron_fails',lambda:certify_source_realization_bridge(dup,reg),'duplicate tetrahedral facet')
    passed=sum(c['status']=='PASS' for c in checks)
    out={'schema':'QHTRI_TOE_TIR_GSC1_SOURCE_REALIZATION_BRIDGE_VALIDATION_V0_9','status':'PASS' if passed==len(checks) else 'FAIL','authority':'CANDIDATE_ONLY','canon_allowed':False,'physical_production_claim':False,'passed':passed,'failed':len(checks)-passed,'checks':checks,'frontier':'ACTUAL_SOURCE_OWNED_GLOBAL_TETRAHEDRAL_INCIDENCE_STILL_OPEN','tir_a5_reference_alignment':'CONTROL_CAPTURE_IS_BOUNDARY_OF_4_SIMPLEX_FIVE_TETRAHEDRA'}
    out['receipt_sha256']=sha256(out); return out
if __name__=='__main__':
    r=run();print(json.dumps(r,indent=2,sort_keys=True));raise SystemExit(0 if r['status']=='PASS' else 1)
