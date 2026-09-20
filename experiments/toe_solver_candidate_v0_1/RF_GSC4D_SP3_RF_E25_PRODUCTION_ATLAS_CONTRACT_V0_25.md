# RF-GSC4D — SP3 RF-E25 Production Atlas Admission Contract v0.25

Status: CANDIDATE_ONLY / FAIL_CLOSED_PRODUCTION_ATLAS_SCHEMA / FULL_PATCH_AND_TIME_COVERAGE_REQUIRED / MODEL_EXTENSION_NEQ_OBSERVATION / CANON_ALLOWED_FALSE

Date: 2026-09-20

## 1. Purpose

V0.19 closes the mathematical two-chart atlas seam and passes the executable GSC4A/RF-E25 data-structure compatibility test.

It explicitly does not promote a production physical atlas.

This contract defines the additional evidence required for

\[
\boxed{
\text{RF-E25 production metric-atlas admission}.
}
\]

It is the metric-side counterpart of the v0.21 W6 source receipt contract.

## 2. Required patch set

The admitted candidate atlas uses exactly

\[
\boxed{
P_{\rm atlas}
=
\{
\mathrm{SP3\_STEREO\_N},
\mathrm{SP3\_STEREO\_S}
\}.
}
\]

A production packet must cover both patches completely and certify both overlap directions.

## 3. Aggregate packet

Minimum aggregate fields:

    schema = RF_GSC4D_SP3_RF_E25_PRODUCTION_ATLAS_PACKET_V0_25
    physical_realization_id
    metric_lineage_id
    atlas_domain_id
    source_bundle_receipt_id
    source_bundle_receipt_digest
    temporal_coverage
    patch_field_receipts
    overlap_receipts
    authority
    canon_allowed
    physical_production_claim

The physical realization and metric lineage must be common across every patch and overlap receipt.

## 4. Patch field receipt

Each patch must provide full field representations for:

    lapse N
    spatial triad/coframe
    shift/matching field

Minimum fields:

    patch_id
    coverage_domain_id
    coverage_patch_id
    spatial_coverage_certified
    temporal_coverage_id
    lapse_provider_digest
    triad_provider_digest
    shift_provider_digest
    field_construction_receipt_id
    immutable_source_refs
    positive_lapse_certified
    invertible_triad_certified
    Lorentz_signature_certified

A finite set of source anchors is not full-patch coverage.

## 5. Temporal coverage firewall

The frozen SP3 source directly observes only a finite two-epoch window.

A production atlas packet must declare one of:

    OBSERVED_PHYSICAL_WINDOW
    INDEPENDENTLY_VALIDATED_PHYSICAL_MODEL_EXTENSION

The class

    SOURCE_DERIVED_STATIONARY_MATHEMATICAL_EXTENSION

is acceptable for candidate mathematics but is not, by itself, production physical coverage outside the observed window.

If a model extension is used for production admission, it must carry:

    model_extension_receipt_id
    model_extension_digest
    validation_domain
    validation_observations
    independent_validation = true

No silent promotion of stationarity is allowed.

## 6. Full-overlap receipt

For each directed overlap N->S and S->N, require:

    source_patch_id
    target_patch_id
    overlap_domain_id
    full_overlap_coverage_certified
    coordinate_jacobian_provider_digest
    Lorentz_transition_provider_digest
    orientation_preserving_certified
    proper_orthochronous_certified
    coframe_overlap_certified
    metric_overlap_certified
    validation_receipt_id
    validation_digest

A single overlap anchor is executable compatibility evidence, not full-overlap production certification.

The analytic v0.19 theorem may serve as a mathematical parent, but the production receipt must bind that theorem to the admitted production field providers and domain.

## 7. Source bundle binding

The metric atlas must identify the same physical realization as the admitted spatial/matching source bundle.

The packet must include immutable provenance linking:

- the source spatial capture;
- the matching-field capture;
- the lapse/clock capture;
- the production atlas field providers.

A candidate source-derived field may be reused only if its source lineage and coverage are explicitly admitted.

## 8. Production authority

A packet may set

    physical_production_claim = true

only when:

1. authority is PRODUCTION_SOURCE_AUTHORITY;
2. both patch fields have full spatial coverage;
3. admitted temporal coverage is complete for the declared target domain;
4. both directed overlaps have full-overlap certification;
5. all provider digests are immutable and bound;
6. the physical realization and metric lineage are common;
7. the stationary/model extension firewall passes.

Candidate-only fixtures must never gain production admission.

## 9. Current v0.19 status

V0.19 establishes:

- exact two-chart mathematical coverage;
- exact orientation-preserving transition;
- exact coframe pullback relation;
- pointwise source-anchor compatibility with the real GSC4A/RF-E25 implementation.

It does not yet establish:

- full physical temporal coverage;
- production authority;
- physical validity of stationary continuation outside the frozen source window;
- production field-provider provenance over both complete patches.

Therefore

\[
\boxed{
\text{RF-E25 production atlas admission remains OPEN}.
}
\]

## 10. Relationship to RF-E26

On the corrected v0.20 frontier, RF-E26 production requires both:

\[
\boxed{
\text{A: RF-E25 production metric-atlas admission}
}
\]

and

\[
\boxed{
\text{B: W6 independent physical source receipts}.
}
\]

W7 target-domain coverage is then derived from the exact atlas/solution patch-set match.

## 11. Evidence boundary

This contract is infrastructure.

It does not promote the source-derived stationary carrier, does not extend observations beyond their source window, does not close RF-E25 production, and does not close RF-E26.

It makes the metric-side production evidence request explicit and machine-checkable.
