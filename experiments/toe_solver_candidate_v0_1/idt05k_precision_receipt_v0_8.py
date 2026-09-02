from __future__ import annotations
from dataclasses import dataclass
from decimal import Decimal, InvalidOperation
import re

HEX64=re.compile(r'^[0-9a-f]{64}$')
ALLOWED_EVIDENCE_CLASSES={'PRODUCTION_SOURCE','REFERENCE_CONTROL','CANDIDATE_SOURCE','EXTERNAL_PROCESS_DATA_REFERENCE'}

class IDT05KPrecisionReceiptError(ValueError): pass

def _id(v,label):
    if not isinstance(v,str) or not v.strip(): raise IDT05KPrecisionReceiptError(f'{label} must be non-empty string')
    return v.strip()

def _sha(v,label):
    out=_id(v,label)
    if HEX64.fullmatch(out) is None: raise IDT05KPrecisionReceiptError(f'{label} must be 64 lowercase hex')
    return out

def _dec(v,label):
    try: out=Decimal(str(v))
    except (InvalidOperation,ValueError,TypeError) as exc: raise IDT05KPrecisionReceiptError(f'{label} must parse as Decimal') from exc
    if not out.is_finite(): raise IDT05KPrecisionReceiptError(f'{label} must be finite')
    return out

@dataclass(frozen=True)
class IDT05KPrecisionLapseReceiptV08:
    schema: str
    source_schema: str
    input_valid: bool
    integrity_valid: bool
    cocycle_valid: bool
    patch_coverage_valid: bool
    production_input: bool
    promotion_review_eligible: bool
    canon_allowed: bool
    dataset_id: str
    realization_id: str
    clock_id: str
    reference_patch_id: str
    dataset_sha256: str
    encoding: str
    precision_digits: int
    tolerance_log: str
    max_log_residual: str
    patch_count: int
    edge_count: int
    source_evidence_class: str
    source_reference: str
    source_digest: str

    def validate(self):
        if self.schema!='IDT_GLOBAL_LAPSE_PRECISION_CAPTURE_V0_8': raise IDT05KPrecisionReceiptError('precision receipt schema mismatch')
        if self.source_schema!='IDT_GLOBAL_LAPSE_PRODUCTION_CAPTURE_V0_1': raise IDT05KPrecisionReceiptError('source_schema mismatch')
        if self.encoding!='DECIMAL_LOG_N': raise IDT05KPrecisionReceiptError('encoding must equal DECIMAL_LOG_N')
        for name in ('input_valid','integrity_valid','cocycle_valid','patch_coverage_valid'):
            if not getattr(self,name): raise IDT05KPrecisionReceiptError(f'{name} must be true')
        if self.canon_allowed: raise IDT05KPrecisionReceiptError('precision capture must not self-authorize canon')
        if self.promotion_review_eligible != self.production_input: raise IDT05KPrecisionReceiptError('promotion_review_eligible must track production_input')
        for name in ('dataset_id','realization_id','clock_id','reference_patch_id','source_reference'):
            _id(getattr(self,name),name)
        _sha(self.dataset_sha256,'dataset_sha256'); _sha(self.source_digest,'source_digest')
        if not isinstance(self.precision_digits,int) or self.precision_digits < 28: raise IDT05KPrecisionReceiptError('precision_digits must be integer >= 28')
        tol=_dec(self.tolerance_log,'tolerance_log'); res=_dec(self.max_log_residual,'max_log_residual')
        if tol<=0 or res<0: raise IDT05KPrecisionReceiptError('tolerance_log must be positive and residual non-negative')
        if res>tol: raise IDT05KPrecisionReceiptError('max_log_residual exceeds tolerance_log')
        if self.patch_count<=0 or self.edge_count<=0: raise IDT05KPrecisionReceiptError('patch_count and edge_count must be positive')
        if self.source_evidence_class not in ALLOWED_EVIDENCE_CLASSES: raise IDT05KPrecisionReceiptError('unsupported source_evidence_class')
        if self.production_input and self.source_evidence_class!='PRODUCTION_SOURCE':
            raise IDT05KPrecisionReceiptError('production_input requires source_evidence_class=PRODUCTION_SOURCE')
        return True
