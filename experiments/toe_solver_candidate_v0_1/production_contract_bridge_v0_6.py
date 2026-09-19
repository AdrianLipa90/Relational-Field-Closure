from __future__ import annotations

from dataclasses import dataclass, asdict
import hashlib
import json
import math
import re

HEX64 = re.compile(r'^[0-9a-f]{64}$')

class ProductionContractBridgeError(ValueError):
    pass


def _id(value: str | None, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ProductionContractBridgeError(f'{label} must be a non-empty string')
    return value.strip()


def _sha(value: str | None, label: str) -> str:
    out=_id(value,label)
    if HEX64.fullmatch(out) is None:
        raise ProductionContractBridgeError(f'{label} must be 64 lowercase hex')
    return out


def _finite_nonnegative(value: float, label: str) -> float:
    out=float(value)
    if not math.isfinite(out) or out < 0.0:
        raise ProductionContractBridgeError(f'{label} must be finite and non-negative')
    return out


@dataclass(frozen=True)
class IDT05KLapseReceipt:
    schema: str
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
    max_relative_residual: float
    patch_count: int
    edge_count: int

    def validate(self) -> None:
        if self.schema != 'IDT_GLOBAL_LAPSE_PRODUCTION_CAPTURE_V0_1':
            raise ProductionContractBridgeError('IDT 05K schema mismatch')
        for name in ('input_valid','integrity_valid','cocycle_valid','patch_coverage_valid'):
            if not getattr(self,name):
                raise ProductionContractBridgeError(f'IDT 05K {name} must be true')
        if self.canon_allowed:
            raise ProductionContractBridgeError('IDT 05K capture must not self-authorize canon')
        if self.promotion_review_eligible != self.production_input:
            raise ProductionContractBridgeError('IDT 05K promotion_review_eligible must track production_input')
        for name in ('dataset_id','realization_id','clock_id','reference_patch_id'):
            _id(getattr(self,name), f'IDT 05K {name}')
        _sha(self.dataset_sha256,'IDT 05K dataset_sha256')
        _finite_nonnegative(self.max_relative_residual,'IDT 05K max_relative_residual')
        if self.patch_count <= 0 or self.edge_count <= 0:
            raise ProductionContractBridgeError('IDT 05K patch_count and edge_count must be positive')


@dataclass(frozen=True)
class TIRGSC1SpatialReceipt:
    schema: str
    capture_schema: str
    production_source_admitted: bool
    capture_sha256: str
    capture_receipt_sha256: str | None
    incidence_sha256: str
    manifold_certified: bool
    input_valid: bool
    integrity_valid: bool
    edge_refinement_certificate_sha256: str
    edge_refinement_ready: bool
    overlap_cocycle_witness_supplied: bool
    domain_coverage_witness_supplied: bool
    realization_id: str

    def validate(self) -> None:
        if self.schema != 'TIR_GSC1_PRODUCTION_SPATIAL_RECEIPT_BRIDGE_V0_6':
            raise ProductionContractBridgeError('TIR bridge schema mismatch')
        if self.capture_schema != 'TIR_GLOBAL_RELATIONAL_COMPLEX_CAPTURE_V0_1':
            raise ProductionContractBridgeError('TIR GSC1 capture schema mismatch')
        for name in ('capture_sha256','incidence_sha256','edge_refinement_certificate_sha256'):
            _sha(getattr(self,name),f'TIR {name}')
        if self.production_source_admitted:
            _sha(self.capture_receipt_sha256,'TIR capture_receipt_sha256')
        for name in ('manifold_certified','input_valid','integrity_valid','edge_refinement_ready','overlap_cocycle_witness_supplied','domain_coverage_witness_supplied'):
            if not getattr(self,name):
                raise ProductionContractBridgeError(f'TIR {name} must be true for production bridge')
        _id(self.realization_id,'TIR realization_id')


@dataclass(frozen=True)
class RFCGSC3CShiftReceipt:
    status: str
    realization_id: str
    clock_id: str
    overlap_covariance_pass: bool
    source_binding_exact: bool
    max_beta_overlap_defect: float
    max_shift_overlap_defect: float
    max_homogeneous_w_defect: float
    max_source_binding_defect: float
    production_status: str
    global_flow_coverage_witness_supplied: bool
    global_clock_properness_witness_supplied: bool
    physical_event_placement_witness_supplied: bool
    receipt_sha256: str

    def validate(self) -> None:
        _id(self.realization_id,'RFC realization_id')
        _id(self.clock_id,'RFC clock_id')
        _sha(self.receipt_sha256,'RFC receipt_sha256')
        if not self.overlap_covariance_pass:
            raise ProductionContractBridgeError('RFC overlap covariance must pass')
        for name in ('max_beta_overlap_defect','max_shift_overlap_defect','max_homogeneous_w_defect','max_source_binding_defect'):
            _finite_nonnegative(getattr(self,name),f'RFC {name}')
        if self.source_binding_exact:
            if self.production_status != 'SOURCE_BINDING_CERTIFIED_ON_SUPPLIED_REALIZATION':
                raise ProductionContractBridgeError('RFC exact binding requires certified production_status')
            if not self.status.startswith('PASS_GSC3C_BETA_MATCH_RFC_SHIFT_SOURCE_BINDING'):
                raise ProductionContractBridgeError('RFC exact binding status mismatch')
        else:
            raise ProductionContractBridgeError('RFC production bridge requires source_binding_exact')
        for name in ('global_flow_coverage_witness_supplied','global_clock_properness_witness_supplied','physical_event_placement_witness_supplied'):
            if not getattr(self,name):
                raise ProductionContractBridgeError(f'RFC {name} must be true for production bridge')


@dataclass(frozen=True)
class ProductionContractBundleV06:
    idt_lapse: IDT05KLapseReceipt
    tir_spatial: TIRGSC1SpatialReceipt
    rfc_shift: RFCGSC3CShiftReceipt


@dataclass(frozen=True)
class ProductionContractBundleCertificateV06:
    idt_provider_contract_valid: bool
    tir_provider_contract_valid: bool
    rfc_provider_contract_valid: bool
    same_physical_realization: bool
    same_clock_identity: bool
    all_source_receipts_production_ready: bool
    promotion_review_eligible: bool
    canon_allowed: bool
    blockers: tuple[str,...]


def certify_production_contract_bundle(bundle: ProductionContractBundleV06) -> ProductionContractBundleCertificateV06:
    bundle.idt_lapse.validate()
    bundle.tir_spatial.validate()
    bundle.rfc_shift.validate()

    same_realization = (
        bundle.idt_lapse.realization_id == bundle.tir_spatial.realization_id == bundle.rfc_shift.realization_id
    )
    same_clock = bundle.idt_lapse.clock_id == bundle.rfc_shift.clock_id
    blockers=[]
    if not bundle.idt_lapse.production_input:
        blockers.append('IDT_05K_PRODUCTION_CAPTURE_DATASET')
    if not bundle.tir_spatial.production_source_admitted:
        blockers.append('TIR_GSC1_PRODUCTION_SOURCE_CAPTURE')
    if not same_realization:
        blockers.append('SAME_PHYSICAL_REALIZATION_BINDING')
    if not same_clock:
        blockers.append('SAME_CLOCK_ID_BINDING')
    all_ready = not blockers
    return ProductionContractBundleCertificateV06(
        idt_provider_contract_valid=True,
        tir_provider_contract_valid=True,
        rfc_provider_contract_valid=True,
        same_physical_realization=same_realization,
        same_clock_identity=same_clock,
        all_source_receipts_production_ready=all_ready,
        promotion_review_eligible=all_ready,
        canon_allowed=False,
        blockers=tuple(blockers),
    )


def certificate_json(cert: ProductionContractBundleCertificateV06) -> str:
    return json.dumps(asdict(cert),sort_keys=True,separators=(',',':'))


def certificate_sha256(cert: ProductionContractBundleCertificateV06) -> str:
    return hashlib.sha256(certificate_json(cert).encode()).hexdigest()
