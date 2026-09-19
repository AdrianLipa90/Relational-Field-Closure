# RF-GSC5D — SP3 W6 Physical Source Receipt Contract v0.21

Status: CANDIDATE_ONLY / FAIL_CLOSED_EXTERNAL_SOURCE_RECEIPT_SCHEMA / TWO_PATCH_RF_E24_COMPLETENESS_CONTRACT / NO_GEOMETRY_DERIVED_SOURCE_PROMOTION / CANON_ALLOWED_FALSE

Date: 2026-09-20

## 1. Purpose

V0.20 reduces the remaining RF-E26 production frontier on the source-derived two-chart carrier to

\[
\boxed{
\text{W6 patchwise RF-E24 physical local-solution receipts}
+
\text{one common physical source-field lineage}.
}
\]

This note defines the minimum fail-closed receipt required to satisfy that parent. It does not supply the source data. It defines the acceptance boundary for future source acquisition.

## 2. Required atlas patch set

The v0.19 atlas patch set is fixed:

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

A complete W6 packet must contain exactly one local-solution receipt for each patch and no foreign patch IDs.

## 3. Patch receipt

Each patch receipt must contain the following fields:

    schema
    patch_id
    atlas_domain_id
    physical_realization_id
    metric_lineage_id
    einstein_operator_lineage_id
    source_field_lineage_id
    source_class
    source_observations
    immutable_source_refs
    Lambda
    kappa_E
    source_tensor
    local_solution
    authority
    canon_allowed
    physical_production_claim

## 4. Source provenance

source_observations must be nonempty.

Each source observation must contain:

    observation_id
    observable_class
    coordinate_or_frame_binding
    units
    source_time_or_interval
    immutable_digest

immutable_source_refs must contain at least one immutable external or source-owned reference with a cryptographic digest.

A receipt that only names a source lineage without source-owned observations is insufficient.

## 5. Independence firewall

The source tensor must declare its derivation class.

Forbidden production derivation classes include:

    T_FROM_G_ONLY
    T_FROM_METRIC_ONLY
    T_EQUALS_G_PLUS_LAMBDA_G_OVER_KAPPA
    GEOMETRIC_EFFECTIVE_STRESS_WITHOUT_INDEPENDENT_SOURCE
    SYNTHETIC_SOURCE_ONLY

The receipt must state

\[
\boxed{
\texttt{independent\_of\_target\_metric\_construction=true}.
}
\]

This does not mean the source tensor is independent of coordinates or of metric coupling in its physical field equations. It means the evidence establishing the source field cannot be produced solely by algebraically rearranging the target Einstein equation being tested.

## 6. Source tensor representation

The receipt must identify a source-owned tensor representation on the patch.

Minimum fields:

    tensor_rank = 2
    symmetry = symmetric
    covariance = covariant_2
    units
    representation_kind
    tensor_payload_digest
    construction_receipt_id
    independent_of_target_metric_construction = true

The payload may be a finite tensor field sample packet with declared interpolation/coverage; coefficients of an independently calibrated physical source model; a source-field callable with immutable implementation/data digest; or a certified zero-source/vacuum packet if the physical source domain is independently established as vacuum.

A bare assertion T=0 is not enough. A vacuum packet must itself carry independent domain/source provenance.

## 7. Common constants

Both patch receipts must carry one common finite

\[
\Lambda
\]

and one common positive finite

\[
\kappa_E.
\]

For SI-normalized GR,

\[
\kappa_E=\frac{8\pi G}{c^4}.
\]

The receipt must identify the normalization source or convention.

## 8. Local RF-E24 solution certificate

Each patch must certify

\[
\boxed{
G_{\mu\nu}
+
\Lambda g_{\mu\nu}
-
\kappa_E T_{\mu\nu}
=
0
}
\]

within a declared tolerance and representation scope.

Minimum local-solution fields:

    certified = true
    equation = RF-E24
    residual_norm
    residual_tolerance
    residual_units_or_normalization
    metric_representation_digest
    einstein_tensor_representation_digest
    source_tensor_payload_digest
    validation_receipt_id
    validation_head_or_artifact_digest

The source tensor digest in the local-solution certificate must equal the independent source-tensor digest in the same patch receipt.

## 9. Cross-patch lineage

The north and south receipts must share:

    physical_realization_id
    atlas_domain_id
    source_field_lineage_id
    einstein_operator_lineage_id
    Lambda
    kappa_E

Their source observation subsets may differ if chart coverage differs, but they must resolve to the same source-field lineage.

## 10. Atlas and solution completeness

The aggregate W6 packet must satisfy

\[
\boxed{
P_{\rm sol}=P_{\rm atlas}.
}
\]

For the current carrier:

\[
\boxed{
P_{\rm sol}
=
\{
\mathrm{SP3\_STEREO\_N},
\mathrm{SP3\_STEREO\_S}
\}.
}
\]

No count-only substitution is accepted. Patch IDs must match exactly.

## 11. Aggregate W6 certificate

A complete aggregate certificate records:

    schema = RF_GSC5D_SP3_W6_PHYSICAL_SOURCE_PACKET_V0_21
    patch_ids
    physical_realization_id
    atlas_domain_id
    source_field_lineage_id
    einstein_operator_lineage_id
    Lambda
    kappa_E
    all_patch_receipts_certified
    all_source_provenance_independent
    all_source_tensor_digests_bound
    all_local_residuals_within_tolerance
    exact_atlas_patch_set_match
    common_source_lineage
    common_constants
    W6_complete
    physical_production_claim

W6_complete=true is permitted only when every condition above passes.

## 12. Relationship to v0.20

Once a valid W6 packet satisfies this contract:

1. GSC5B derives target-domain coverage on the v0.19 two-chart atlas;
2. GSC5A derives G, T, and residual overlap covariance;
3. RF-E26 has the required reduced parents for global carrier promotion, subject to the production authority boundary.

Thus future work no longer needs to invent another atlas or another global-causality theorem. It needs source-owned physical evidence.

## 13. Fail-closed examples

The contract rejects:

1. only one patch receipt;
2. a foreign patch receipt;
3. different source lineage IDs across the two patches;
4. different Lambda or kappa_E;
5. missing immutable source evidence;
6. local_solution_certified=false;
7. residual above tolerance;
8. source tensor digest mismatch between source packet and local solution;
9. geometry-only derivation of T;
10. a claimed vacuum source without independent vacuum-domain provenance.

## 14. Evidence boundary

This contract is infrastructure.

It does not assert that the frozen SP3 source supplies T; assert that the source-derived metric is a production physical spacetime metric; create a physical matter source from curvature; or promote RF-E26.

It makes the remaining evidence request explicit and machine-checkable.
