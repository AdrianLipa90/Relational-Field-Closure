"""RF-GSC4B sufficient RF-E25 route in flow-adapted product coordinates.

After the GSC3A product-trivialization parent supplies
    F: I x Sigma -> M,  F_* d/dt = X,
spatial coordinates pulled from the reference Sigma are constant along X.
Hence, in the induced chart, X = d/dt and the ADM matching shift and temporal
spatial drift are both zero.  This module specializes RF-GSC4A to that exact
coordinate gauge while keeping the product-trivialization parent explicit.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Sequence

from src.rfc.shared_spacetime_atlas import ADMPatch
from src.rfc.source_assembled_shared_spacetime_atlas import (
    SourceAssembledAtlasCertificate,
    SourceAssembledAtlasError,
    SpatialSourceOverlap,
    assemble_source_shared_spacetime_atlas,
)


class FlowAdaptedAtlasError(ValueError):
    """Raised when the GSC4B sufficient-route contract fails closed."""


ZERO3 = (0.0, 0.0, 0.0)


@dataclass(frozen=True)
class FlowAdaptedPatchSource:
    name: str
    lapse: float
    triad: Sequence[Sequence[float]]

    def as_adm_patch(self) -> ADMPatch:
        return ADMPatch(self.name, self.lapse, self.triad, ZERO3)


@dataclass(frozen=True)
class FlowAdaptedSpatialOverlap:
    source: str
    target: str
    spatial_jacobian: Sequence[Sequence[float]]
    spatial_rotation: Sequence[Sequence[float]]

    def as_source_overlap(self) -> SpatialSourceOverlap:
        return SpatialSourceOverlap(
            source=self.source,
            target=self.target,
            spatial_jacobian=self.spatial_jacobian,
            temporal_drift=ZERO3,
            spatial_rotation=self.spatial_rotation,
        )


@dataclass(frozen=True)
class FlowAdaptedAtlasCertificate:
    compatible: bool
    product_trivialization_parent: bool
    zero_shift_exact: bool
    zero_temporal_drift_exact: bool
    source_assembled: SourceAssembledAtlasCertificate
    theorem_status: str = "EXACT_FLOW_ADAPTED_ZERO_SHIFT_COORDINATE_THEOREM"
    production_input_status: str = "PRODUCT_TRIVIALIZATION_AND_SPATIAL_SOURCE_PACKET_OPEN"


def assemble_flow_adapted_shared_spacetime_atlas(
    patches: Sequence[FlowAdaptedPatchSource],
    overlaps: Sequence[FlowAdaptedSpatialOverlap],
    *,
    product_trivialization_certified: bool,
    triangles: Iterable[tuple[str, str, str]] = (),
    atol: float = 1.0e-10,
) -> FlowAdaptedAtlasCertificate:
    """Assemble the RF-E25 packet in the sufficient flow-adapted gauge.

    The boolean parent is an explicit dependency gate, not inferred from the
    finite patch packet.  Once it is admitted, the coordinate theorem fixes
    b=0 and v=0 in the transported spatial chart.  RF-GSC4A then performs the
    remaining lapse/coframe/spatial-cocycle checks and delegates to RF-E25.
    """
    if product_trivialization_certified is not True:
        raise FlowAdaptedAtlasError(
            "GSC4B requires an admitted GSC3A product-trivialization parent"
        )
    if not patches:
        raise FlowAdaptedAtlasError("at least one flow-adapted patch is required")

    adm_patches = [patch.as_adm_patch() for patch in patches]
    source_overlaps = [overlap.as_source_overlap() for overlap in overlaps]

    try:
        source_cert = assemble_source_shared_spacetime_atlas(
            adm_patches,
            source_overlaps,
            triangles=triangles,
            atol=atol,
        )
    except SourceAssembledAtlasError as exc:
        raise FlowAdaptedAtlasError(f"flow-adapted source assembly failed: {exc}") from exc

    return FlowAdaptedAtlasCertificate(
        compatible=True,
        product_trivialization_parent=True,
        zero_shift_exact=all(tuple(p.shift) == ZERO3 for p in adm_patches),
        zero_temporal_drift_exact=all(
            tuple(ov.temporal_drift) == ZERO3 for ov in source_overlaps
        ),
        source_assembled=source_cert,
    )
