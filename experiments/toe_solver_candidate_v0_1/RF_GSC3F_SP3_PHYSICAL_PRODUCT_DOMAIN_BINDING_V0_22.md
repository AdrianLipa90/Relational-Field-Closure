# RF-GSC3F — SP3 Physical Product-Domain Binding Contract v0.22

Status: CANDIDATE_ONLY / FAIL_CLOSED_PHYSICAL_PRODUCT_REALIZATION_SCHEMA / EVENT_PLACEMENT_AND_SPATIAL_DOMAIN_BINDING / NO_IDENTIFIER_ONLY_PROMOTION / CANON_ALLOWED_FALSE

Date: 2026-09-20

## 1. Purpose

V0.18--v0.21 construct and validate a candidate carrier

\[
M_{\rm cand}
=
\mathbb R\times\mathcal E_Q
\]

with global clock, Lorentz metric, Cauchy foliation, two-chart RF-E25 atlas, and explicit W6 source-receipt requirements.

For production use, RF-GSC3 still requires a source-owned physical identification of the admitted TIR x IDT realization with the product carrier.

A common realization identifier is necessary but not sufficient.

This contract defines the minimum evidence needed to state that the physical source domain, event placements, production spatial carrier, RF-E25 atlas and W6 source tensor all refer to one and the same spacetime realization.

## 2. Fixed candidate domain

The candidate domain is

\[
\boxed{
D_{\rm cand}
=
\texttt{SP3\_STATIONARY\_PRODUCT\_DOMAIN\_V0\_18\_V0\_19}.
}
\]

Its spatial fibre is the v0.15 ellipsoid

\[
\mathcal E_Q\simeq S^3
\]

with v0.19 patches

\[
P_{\rm atlas}
=
\{
\mathrm{SP3\_STEREO\_N},
\mathrm{SP3\_STEREO\_S}
\}.
\]

## 3. Required physical product-binding packet

The aggregate packet must contain:

    schema
    physical_realization_id
    clock_id
    candidate_domain_id
    production_spatial_realization_id
    production_event_complex_id
    source_receipt_refs

    spatial_carrier_binding
    event_placement_binding
    atlas_domain_binding
    w6_domain_binding

    authority
    canon_allowed
    physical_production_claim

A string equality of identifiers does not by itself satisfy any of the four binding blocks.

## 4. Spatial carrier binding

Production use requires an explicit map

\[
\boxed{
\Phi_\Sigma:
|\Sigma_{\rm prod}|
\longrightarrow
\mathcal E_Q
}
\]

or an equivalent source-owned coordinate transformation.

The receipt must state:

    source_spatial_domain_id
    target_candidate_spatial_domain_id
    map_kind
    map_receipt_id
    implementation_or_payload_digest
    orientation_preserving
    rank_three_everywhere_on_declared_domain
    injective_on_declared_domain
    surjective_onto_declared_target_domain
    coverage_certified
    source_owned

For a production identification of the full candidate carrier, coverage must be certified on the full declared spatial target domain, not only at the five source anchors.

A finite anchor list without an independently certified extension does not establish the product realization.

## 5. Event placement binding

Let the production event set be E and let the production clock be

\[
t_E:E\to I.
\]

The packet must provide one source-owned placement

\[
\boxed{
\iota:E\to I\times\mathcal E_Q
}
\]

with

\[
\boxed{
\operatorname{pr}_I\circ\iota=t_E+C
}
\]

for one finite common additive constant C.

Each placed event record must contain:

    event_id
    clock_value
    candidate_time_value
    spatial_source_anchor_id
    candidate_spatial_coordinate_or_ref
    atlas_patch_ids
    placement_digest

The aggregate placement receipt must certify:

    event_set_coverage_exact
    one_common_clock_offset
    temporal_residual_within_tolerance
    spatial_binding_resolves_through_Phi_Sigma
    no_event_outside_candidate_domain
    source_owned

If a downstream sector requires injectivity, the receipt must also certify injective placement.

## 6. Atlas-domain binding

The RF-E25 atlas must cover the image of the physically bound domain.

The packet must certify:

\[
\boxed{
\Phi_\Sigma(|\Sigma_{\rm prod}|)
=
\mathcal E_Q
}
\]

for a full-domain promotion, or explicitly declare a smaller physical target domain.

For the current full-domain route, the patch cover must remain exactly

\[
\{
\mathrm{SP3\_STEREO\_N},
\mathrm{SP3\_STEREO\_S}
\}.
\]

The atlas-domain receipt must bind:

    physical_realization_id
    candidate_domain_id
    atlas_patch_ids
    spatial_binding_receipt_id
    event_placement_receipt_id
    coverage_receipt_id

## 7. W6 source-domain binding

A W6 source packet is admissible only if its source tensor coverage domain is the same physically bound domain.

The following must match the physical product packet:

    physical_realization_id
    candidate_domain_id
    atlas patch ids
    clock id or declared clock/frame transform
    physical frame binding
    source-field coverage domain

Thus an independently measured or modelled source tensor on an unrelated coordinate domain cannot close RF-E26 merely because its lineage id is nonempty.

## 8. Same-realization condition

The following identifiers must resolve to one source-owned realization:

\[
\boxed{
R_{\rm IDT}
=
R_{\rm TIR}
=
R_{\rm RFC}
=
R_{\rm atlas}
=
R_{\rm W6}.
}
\]

Identifier equality is only a necessary first test.

The packet additionally requires cryptographic references to the source receipts establishing each equality relation.

## 9. Physical frame condition

The source tensor and RF-E25 metric need not originate in the same coordinate chart, but the transformation between their frames must be supplied and certified.

For every W6 patch:

    source_frame_id
    RF_E25_frame_id
    frame_transform_kind
    frame_transform_payload_or_callable_digest
    transform_invertible
    tensor_pushforward_pullback_certified

A bare declaration that two frames are equivalent is insufficient.

## 10. Fail-closed rules

The contract rejects:

1. identifier equality without spatial-domain binding;
2. five anchor correspondences without full-domain extension/coverage;
3. event placements with different clock offsets;
4. event placements outside the bound spatial domain;
5. an RF-E25 atlas whose patches do not cover the physically bound domain;
6. W6 source tensors on an unrelated domain;
7. source-frame / metric-frame equality asserted without a transform or shared frame receipt;
8. mixed physical realization ids;
9. mixed clock ids without a certified clock transform;
10. candidate or synthetic fixtures presented as production source authority.

## 11. Corrected RF-E26 production frontier

V0.20 remains correct as a dependency reduction inside the declared candidate domain:

\[
\text{W7 coverage}
\to
\text{derived from complete W6 patch coverage}.
\]

For production, however, the complete frontier is

\[
\boxed{
\text{physical product-realization/event-placement binding}
+
\text{W6 independent physical source receipts}.
}
\]

Only after both are supplied on one realization can the RF-E25/RF-E26 production route be evaluated.

## 12. Evidence boundary

This contract does not supply a physical product realization.

It explicitly records that the current source-derived ellipsoid and stationary extension are candidate mathematical carriers.

The frozen SP3 anchor set supplies useful external-source constraints, but five anchors do not by themselves prove that the full ellipsoid is the physical spatial domain.

The remaining task is therefore external/source-owned domain binding, not additional local differential geometry.
