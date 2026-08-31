"""RF-GSC4A shift-source provenance admission for source-assembled RF-E25 atlases.

The exact GSC4A geometry accepts an ADM shift b as a typed geometric field.  This
module separates two admissible source routes before production-facing assembly:

1. RFC_INDEPENDENT_SHIFT: b is supplied as an RFC-owned shift source;
2. TIR_BETA_MATCH_BOUND: b represents the TIR beta_match carrier after the
   GSC3D shared-one-form alias and GSC3E W=0 realization binding have both been
   certified on the declared realization.

The provenance record is an admission input.  Repository/source ownership remains
controlled by the source records that issue the referenced receipts.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Mapping, Sequence

from src.rfc.shared_spacetime_atlas import ADMPatch
from src.rfc.source_assembled_shared_spacetime_atlas import (
    SourceAssembledAtlasCertificate,
    SourceAssembledAtlasError,
    SpatialSourceOverlap,
    assemble_source_shared_spacetime_atlas,
)

RFC_INDEPENDENT_SHIFT = "RFC_INDEPENDENT_SHIFT"
TIR_BETA_MATCH_BOUND = "TIR_BETA_MATCH_BOUND"


class ShiftSourceProvenanceError(SourceAssembledAtlasError):
    """Raised when the shift-source admission packet is incomplete or inconsistent."""


@dataclass(frozen=True)
class ShiftSourceProvenance:
    patch_id: str
    route: str
    source_owner: str
    realization_id: str
    clock_id: str
    source_reference: str
    gsc3d_alias_receipt: str | None = None
    gsc3e_w0_receipt: str | None = None


@dataclass(frozen=True)
class ProvenanceTypedAtlasCertificate:
    geometry: SourceAssembledAtlasCertificate
    realization_id: str
    clock_id: str
    routes_by_patch: Mapping[str, str]
    source_references_by_patch: Mapping[str, str]
    provenance_status: str = "DECLARED_SOURCE_ROUTES_ADMITTED"
    production_source_ownership_status: str = "SOURCE_CONTROLLED_PROVENANCE_REQUIRED"


def _text(value: str, label: str) -> str:
    out = str(value).strip()
    if not out:
        raise ShiftSourceProvenanceError(f"{label} must be nonempty")
    return out


def rfc_independent_shift_source(
    *, patch_id: str, realization_id: str, clock_id: str, source_reference: str
) -> ShiftSourceProvenance:
    return ShiftSourceProvenance(
        patch_id=_text(patch_id, "patch_id"),
        route=RFC_INDEPENDENT_SHIFT,
        source_owner="RFC",
        realization_id=_text(realization_id, "realization_id"),
        clock_id=_text(clock_id, "clock_id"),
        source_reference=_text(source_reference, "source_reference"),
    )


def tir_beta_match_bound_shift_source(
    *,
    patch_id: str,
    realization_id: str,
    clock_id: str,
    source_reference: str,
    gsc3d_alias_receipt: str,
    gsc3e_w0_receipt: str,
) -> ShiftSourceProvenance:
    return ShiftSourceProvenance(
        patch_id=_text(patch_id, "patch_id"),
        route=TIR_BETA_MATCH_BOUND,
        source_owner="TIR",
        realization_id=_text(realization_id, "realization_id"),
        clock_id=_text(clock_id, "clock_id"),
        source_reference=_text(source_reference, "source_reference"),
        gsc3d_alias_receipt=_text(gsc3d_alias_receipt, "gsc3d_alias_receipt"),
        gsc3e_w0_receipt=_text(gsc3e_w0_receipt, "gsc3e_w0_receipt"),
    )


def _validate_record(record: ShiftSourceProvenance) -> None:
    _text(record.patch_id, "patch_id")
    _text(record.realization_id, "realization_id")
    _text(record.clock_id, "clock_id")
    _text(record.source_reference, "source_reference")

    if record.route == RFC_INDEPENDENT_SHIFT:
        if record.source_owner != "RFC":
            raise ShiftSourceProvenanceError("RFC_INDEPENDENT_SHIFT requires source_owner=RFC")
        return

    if record.route == TIR_BETA_MATCH_BOUND:
        if record.source_owner != "TIR":
            raise ShiftSourceProvenanceError("TIR_BETA_MATCH_BOUND requires source_owner=TIR")
        _text(record.gsc3d_alias_receipt or "", "gsc3d_alias_receipt")
        _text(record.gsc3e_w0_receipt or "", "gsc3e_w0_receipt")
        return

    raise ShiftSourceProvenanceError(f"unsupported shift-source route: {record.route}")


def certify_shift_source_provenance(
    patches: Sequence[ADMPatch],
    provenance: Sequence[ShiftSourceProvenance],
) -> tuple[str, str, dict[str, ShiftSourceProvenance]]:
    if not patches:
        raise ShiftSourceProvenanceError("at least one ADM patch is required")

    patch_ids = [patch.name for patch in patches]
    if len(set(patch_ids)) != len(patch_ids):
        raise ShiftSourceProvenanceError("patch IDs must be unique")

    by_patch: dict[str, ShiftSourceProvenance] = {}
    for record in provenance:
        _validate_record(record)
        if record.patch_id in by_patch:
            raise ShiftSourceProvenanceError(f"duplicate provenance patch_id: {record.patch_id}")
        by_patch[record.patch_id] = record

    if set(by_patch) != set(patch_ids):
        missing = sorted(set(patch_ids) - set(by_patch))
        extra = sorted(set(by_patch) - set(patch_ids))
        raise ShiftSourceProvenanceError(
            f"provenance patch coverage mismatch; missing={missing}, extra={extra}"
        )

    realization_ids = {record.realization_id for record in by_patch.values()}
    clock_ids = {record.clock_id for record in by_patch.values()}
    if len(realization_ids) != 1:
        raise ShiftSourceProvenanceError("all shift sources must name one common realization_id")
    if len(clock_ids) != 1:
        raise ShiftSourceProvenanceError("all shift sources must name one common clock_id")

    return next(iter(realization_ids)), next(iter(clock_ids)), by_patch


def assemble_provenance_typed_source_shared_spacetime_atlas(
    patches: Sequence[ADMPatch],
    source_overlaps: Sequence[SpatialSourceOverlap],
    *,
    shift_provenance: Sequence[ShiftSourceProvenance],
    triangles: Iterable[tuple[str, str, str]] = (),
    atol: float = 1.0e-10,
) -> ProvenanceTypedAtlasCertificate:
    """Admit shift provenance and then execute the exact GSC4A/RF-E25 geometry."""
    realization_id, clock_id, by_patch = certify_shift_source_provenance(
        patches, shift_provenance
    )
    geometry = assemble_source_shared_spacetime_atlas(
        patches,
        source_overlaps,
        triangles=triangles,
        atol=atol,
    )
    return ProvenanceTypedAtlasCertificate(
        geometry=geometry,
        realization_id=realization_id,
        clock_id=clock_id,
        routes_by_patch={pid: record.route for pid, record in by_patch.items()},
        source_references_by_patch={
            pid: record.source_reference for pid, record in by_patch.items()
        },
    )
