# RF-GSC5A — Natural Einstein Globalization Input Reduction

Status: `EXACT_NATURAL_TENSOR_GLOBALIZATION / EXACT_SOURCE_GLUE_DERIVATION_ON_PATCHWISE_SOLUTIONS / GSC5_INPUT_REDUCTION / PRODUCTION_SMOOTH_ATLAS_AND_SOLUTION_RECEIPTS_OPEN`

Date: 2026-08-31

## 1. Purpose

RF-E26 certifies a global Einstein carrier by checking overlap covariance independently for the local representatives of

\[
g_{\mu\nu},\qquad G_{\mu\nu},\qquad T_{\mu\nu},\qquad \mathcal R_{\mu\nu}.
\]

RF-GSC5A isolates the smaller sufficient production contract available once the RF-E24 Einstein operator and the RF-E25 shared metric atlas are already typed.

The reduced route consumes:

1. a smooth RF-E25 shared metric atlas;
2. patchwise RF-E24 solution receipts;
3. one common finite `Lambda`;
4. one common positive finite `kappa_E`;
5. one common physical source-field lineage identifier;
6. connected overlap incidence.

From these inputs, the overlap laws for `G`, `T`, and the Einstein residual are derived.

## 2. Metric atlas parent

Let patches `U_p,U_q` belong to one smooth RF-E25 atlas. On an overlap use

\[
dx_q=J_{q\leftarrow p}\,dx_p.
\]

The global metric parent supplies

\[
\boxed{g_p=J^Tg_qJ.}
\]

The smooth realization is taken in the regularity class required by the Levi-Civita curvature construction, so the Einstein tensor is defined patchwise from the same global metric.

## 3. Naturality of the Einstein tensor

For a smooth coordinate change, the Levi-Civita connection, curvature, Ricci tensor and scalar curvature are natural constructions from `g`. Therefore the Einstein tensor

\[
\boxed{G[g]=\operatorname{Ric}[g]-\frac12R[g]g}
\]

is a covariant rank-two natural tensor.

Hence metric compatibility on the shared atlas gives

\[
\boxed{G_p=J^TG_qJ.}
\]

This overlap identity is a derived output of the shared smooth metric atlas plus the RF-E24 operator identification.

## 4. Source overlap law from the local equation

Assume patchwise RF-E24 solution receipts certify

\[
\boxed{G_p+\Lambda g_p=\kappa_E T_p}
\]

and

\[
\boxed{G_q+\Lambda g_q=\kappa_E T_q}
\]

with the same constants `Lambda` and `kappa_E`, where

\[
\kappa_E>0.
\]

Pull the `q` equation back to the `p` coordinates:

\[
J^TG_qJ+\Lambda J^Tg_qJ
=\kappa_EJ^TT_qJ.
\]

Using the derived metric and Einstein-tensor overlap laws,

\[
G_p+\Lambda g_p
=\kappa_EJ^TT_qJ.
\]

Compare with the patch-`p` solution equation:

\[
G_p+\Lambda g_p=\kappa_ET_p.
\]

Since `kappa_E` is common and strictly positive,

\[
\boxed{T_p=J^TT_qJ.}
\]

Thus source-tensor overlap covariance follows from the shared metric atlas, Einstein-tensor naturality, common coupling constants and patchwise solution certification.

The common source-lineage identifier preserves physical provenance across the derived tensor gluing.

## 5. Residual globalization

Define

\[
\mathcal R_p:=G_p+\Lambda g_p-\kappa_ET_p.
\]

Every patchwise solution receipt gives

\[
\boxed{\mathcal R_p=0.}
\]

The three tensor overlap laws immediately give

\[
\boxed{\mathcal R_p=J^T\mathcal R_qJ.}
\]

Hence the residual overlap witness is also derived on this route.

For a supplied connected cover of the target domain,

\[
\mathcal R|_{U_p}=0\quad\forall p
\]

implies

\[
\boxed{\mathcal R=0}
\]

on the represented covered domain.

## 6. Reduced production contract

The RF-E26 explicit production packet can be reduced on this sufficient route from

```text
metric representatives g_p
Einstein representatives G_p
source representatives T_p
residual representatives R_p
overlap checks for g, G, T, R
common Lambda and kappa_E
RF-E25 atlas certification
domain coverage
```

to

```text
smooth RF-E25 shared metric atlas
patchwise RF-E24 local-solution receipts
common Lambda
common positive kappa_E
common physical source-field lineage id
connected overlap incidence
domain coverage
```

with deterministic derived overlap outputs

\[
G_p=J^TG_qJ,
\]

\[
T_p=J^TT_qJ,
\]

\[
\mathcal R_p=J^T\mathcal R_qJ=0.
\]

## 7. Typed boundaries

RF-GSC5A keeps the following source roles explicit:

- the shared metric atlas and its smoothness/regularity are geometry-owned inputs;
- each patchwise RF-E24 solution receipt remains a physical solution witness;
- the physical source lineage remains source-owned provenance;
- `Lambda` and `kappa_E` are common scalar coordinates;
- target-domain coverage remains a separate GSC5 coverage coordinate;
- GSC6 causal/Cauchy structure remains a separate global coordinate.

## 8. Executable certifier

Implementation:

`src/rfc/natural_einstein_globalization.py`

Reference tests:

`tests/reference/test_gsc5a_natural_einstein_globalization.py`

The certifier checks the reduced contract at the dependency/type level:

- smooth shared-atlas parent receipt;
- common Einstein-operator lineage;
- patchwise local-solution receipts;
- common finite `Lambda`;
- common positive finite `kappa_E`;
- common physical source-field lineage;
- known connected overlap incidence;
- explicit target-domain coverage for global promotion.

The output records `G`, `T`, and residual overlap covariance as derived coordinates rather than independent production witnesses.

## 9. Claim ledger

| Statement | Status |
|---|---|
| Einstein tensor is natural under smooth coordinate changes | `STANDARD EXACT DIFFERENTIAL GEOMETRY` |
| global smooth metric atlas induces compatible local `G[g]` representatives | `EXACT` |
| patchwise Einstein solutions with common constants induce `T` overlap covariance | `EXACT ALGEBRA` |
| residual overlap covariance is derived | `EXACT` |
| explicit `G` overlap packet on this route | `DERIVED COORDINATE` |
| explicit `T` overlap packet on this route | `DERIVED COORDINATE` |
| explicit residual overlap packet on this route | `DERIVED COORDINATE` |
| production smooth shared atlas | `OPEN SOURCE INPUT` |
| production patchwise RF-E24 solution receipts | `OPEN SOURCE INPUT` |
| production source-lineage provenance | `OPEN SOURCE INPUT` |
| target-domain coverage | `OPEN GSC5 COORDINATE` |

## 10. Result

On the admitted smooth shared-atlas route,

\[
\boxed{
\text{metric atlas}
+\text{patchwise RF-E24 solutions}
+\text{common }(\Lambda,\kappa_E)
\Longrightarrow
\text{global compatible }G,T,\mathcal R
}
\]

with source provenance and target-domain coverage retained as explicit production coordinates.
