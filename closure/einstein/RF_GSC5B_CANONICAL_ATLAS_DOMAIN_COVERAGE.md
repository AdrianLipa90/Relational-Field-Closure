# RF-GSC5B — Canonical Atlas Domain-Coverage Reduction

Status: `EXACT_COVER_COMPOSITION_THEOREM / EXECUTABLE_PATCH_COMPLETENESS_CERTIFIER / W7_DERIVED_ON_CANONICAL_ATLAS_DOMAIN_ROUTE / BROADER_TARGET_DOMAIN_COVERAGE_OPEN`

Date: 2026-08-31

## 1. Purpose

RF-GSC5A reduces the RF-E26 production packet to a smooth RF-E25 metric atlas, patchwise RF-E24 local-solution receipts with common constants/source lineage, connected incidence, and a target-domain coverage receipt.

On the canonical GSC1 -> GSC4C -> GSC3 product route, the target-domain coverage coordinate can be reduced further.

## 2. Canonical spatial cover

Let the admitted finite TIR A5 complex have vertex set `V`. RF-GSC4C supplies the exact open-star cover

\[
\boxed{\Sigma=\bigcup_{v\in V}\operatorname{st}^{\circ}(v).}
\]

For an admitted global product

\[
\boxed{M=I\times\Sigma,}
\]

define spacetime patches

\[
\boxed{U_v=I\times\operatorname{st}^{\circ}(v).}
\]

Then distributivity of the Cartesian product over unions gives

\[
\bigcup_{v\in V}U_v
=I\times\bigcup_{v\in V}\operatorname{st}^{\circ}(v)
=I\times\Sigma
=M.
\]

Thus the GSC4C cover, extended along the global GSC3 product clock, certifies coverage of the production atlas domain.

## 3. Patchwise local-solution completeness

Let `P_atlas` be the finite patch-id set of the production RF-E25/GSC4 atlas and let `P_sol` be the patch-id set carrying certified RF-E24 local-solution receipts.

On the reduced route require

\[
\boxed{P_{\rm sol}=P_{\rm atlas}.}
\]

This equality is stronger than a count comparison: it checks that every atlas patch has a local solution and that no foreign patch id is silently substituted.

Combined with the canonical atlas coverage theorem, the complete patch-index receipt gives local RF-E24 solution coverage of the entire atlas domain.

## 4. Target-domain identity

The reduction applies when the RF-E26 target domain is declared to be the production atlas domain:

\[
\boxed{D_{\rm target}=D_{\rm atlas}=M.}
\]

Therefore

```text
GSC1/A5 finite production carrier
 + GSC4C canonical vertex-star spatial cover
 + global GSC3 product M = I x Sigma
 -> canonical spacetime atlas cover of M

 + W6 RF-E24 local-solution receipts on every atlas patch id
 + target_domain_id = atlas_domain_id
 -> RF-E26/GSC5 target-domain coverage derived
```

No separate W7 coverage receipt is required on this sufficient route.

## 5. Firewalls

The reduction is fail-closed under each of the following controls:

1. one atlas patch lacks an RF-E24 local-solution receipt;
2. the solution receipt set contains patch ids outside the admitted atlas set;
3. the requested target domain differs from the production atlas domain;
4. the canonical atlas coverage parent has not been certified.

A broader target domain retains an explicit coverage coordinate. Reference fixtures do not promote production coverage.

Connectedness remains a distinct property of the atlas incidence and is not inferred from patch-index equality alone.

## 6. Executable certifier

Implementation:

`src/rfc/canonical_atlas_domain_coverage.py`

Reference tests:

`tests/reference/test_gsc5b_canonical_atlas_domain_coverage.py`

The certifier compares exact patch-id sets and target/atlas domain ids and returns `domain_coverage_derived=true` only when the canonical atlas coverage parent is certified and all identities close.

## 7. Relation to GSC5A / RF-E26

RF-GSC5A already derives Einstein/stress/residual overlap covariance from metric naturality and local equations. RF-GSC5B supplies a sufficient route for its remaining domain-coverage parent.

The combined production route becomes

```text
production RF-E25/GSC4 canonical atlas
 + patchwise RF-E24 local solutions on the full atlas patch-id set
 + common Lambda/kappa_E/source lineage
 -> GSC5A natural tensor globalization
 + GSC5B derived atlas-domain coverage
 -> RF-E26 global Einstein carrier on the declared atlas domain
```

## 8. Live GREMLIN × Terminal36D × PhaseNav audit

A fresh candidate audit ran through the active NOEMA surface:

- source event: `gremlin:whisper:sha256:2bca7d1afe8affe0d20ab7bef6b53a59f47618831468b7d084d1659831732936`;
- fused event: `gremlin:whisper:sha256:ca04fde040d3174a259fad50c88a6fda86aa59def3dcf68e45bce09e5b8d6ab9`;
- Terminal36D receipt: `edf6f20d2057f4ac73704d524f229f8f0d3f5b09660283741a48c273bd008c2b`;
- PhaseNav trace: `b062e4b14f2db315efcc9389bb726567ab28c93a07fe97167e5dde1f9fe1fc0d`;
- shape: `[9,36]`;
- authority: `CANDIDATE_ONLY`.

Runtime audit is dependency/falsification evidence only.

## 9. Claim ledger

| Statement | Status |
|---|---|
| GSC4C vertex-star patches cover the finite A5 spatial carrier | `EXACT PARENT` |
| `I x star(v)` patches cover the global product `I x Sigma` | `EXACT` |
| exact patch-id equality certifies one RF-E24 solution receipt per atlas patch | `EXACT FINITE SET THEOREM` |
| target=atlas domain + canonical cover + patch completeness derives W7 | `EXACT SUFFICIENT ROUTE` |
| broader/different target-domain coverage | `OPEN SEPARATE INPUT` |
| production W6 local-solution receipts | `OPEN PRODUCTION PARENT` |
| production canonical atlas/product parents | `OPEN PRODUCTION PARENTS` |

Target verdict:

`PASS_RFC_GSC5B_CANONICAL_ATLAS_DOMAIN_COVERAGE_REDUCTION_WITH_PRODUCTION_PARENTS_OPEN`.
