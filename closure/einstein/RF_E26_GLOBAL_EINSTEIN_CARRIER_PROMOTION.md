# RF-E26 — Global Einstein Carrier Promotion from a Certified Shared Atlas

Status: `LOCAL_TO_GLOBAL_TENSOR_GLUE_THEOREM / GLOBAL_EINSTEIN_CARRIER_CERTIFIER / PRODUCTION_DOMAIN_COVERAGE_OPEN_INPUT / GLOBAL_HYPERBOLICITY_SEPARATE_RF_L7_GATE`

Date: 2026-08-30

## 1. Purpose

RF-E24 establishes the Einstein field-equation form on every admitted local continuum patch,

\[
G_{\mu\nu}+\Lambda g_{\mu\nu}=\kappa_E T_{\mu\nu},
\qquad
\kappa_E=\frac{8\pi G}{c^4},
\]

under its declared TIR/RFC selection rules. RF-E25 independently certifies that supplied ADM patches and overlaps define one time-oriented Lorentzian atlas when the coframe, metric, orientation, shared clock and cocycle gates pass.

RF-E26 owns the remaining local-to-global equation question:

> if the local tensors on an RF-E25-certified atlas are compatible on overlaps and the supplied patches cover the target domain, does the RF-E24 equation define one global tensor equation on that domain?

The answer is an exact conditional gluing theorem. The production existence of the required atlas and coverage witness remains an explicit input.

## 2. Parent locks

RFC main baseline for this gate:

`5bb01438a44a68b0d747a3d1f9114aa648bd7395`.

Required parent surfaces:

- `closure/einstein/RF_E24_LOCAL_EINSTEIN_FORM_CLOSURE.md`;
- `closure/einstein/RF_E25_SHARED_SPACETIME_ATLAS_COCYCLE.md`;
- `src/rfc/shared_spacetime_atlas.py`;
- `closure/lambda0/RF_L7_CAUCHY_HYPERBOLICITY_WELLPOSEDNESS.md`.

RF-E24 owns the local tensor form. RF-E25 owns the shared Lorentzian atlas. RF-L7 owns the stronger Cauchy/global-hyperbolicity gate.

## 3. Patchwise Einstein residual

On each supplied patch `p`, define the covariant rank-two residual

\[
\boxed{
\mathcal R^{(p)}_{\mu\nu}
:=G^{(p)}_{\mu\nu}
+\Lambda g^{(p)}_{\mu\nu}
-\kappa_E T^{(p)}_{\mu\nu}.
}
\]

RF-E26 requires one common finite scalar `Lambda` and one common positive finite scalar `kappa_E` across the patch system.

The local RF-E24 equation is exactly the statement

\[
\boxed{\mathcal R^{(p)}=0}
\]

on every represented patch.

## 4. Tensor overlap law

Use the RF-E25 coordinate convention

\[
dx_q=J_{q\leftarrow p}\,dx_p.
\]

For a covariant rank-two tensor `X`, the local representatives obey

\[
\boxed{
X_p=J_{q\leftarrow p}^{T}X_qJ_{q\leftarrow p}.
}
\]

RF-E26 checks this independently for

\[
X\in\{g,G,T\}.
\]

Because `Lambda` and `kappa_E` are common scalars, linearity gives

\[
\begin{aligned}
J^T\mathcal R_qJ
&=J^TG_qJ+\Lambda J^Tg_qJ-\kappa_EJ^TT_qJ\\
&=G_p+\Lambda g_p-\kappa_ET_p\\
&=\mathcal R_p.
\end{aligned}
\]

Hence the residual itself is a compatible covariant two-tensor on every certified overlap.

## 5. Local-to-global gluing theorem

Let `M` be the target domain and let `{U_p}` be a supplied cover of `M`. Assume:

1. RF-E25 has certified the supplied shared spacetime atlas;
2. the supplied patch family covers the target domain;
3. `g_p`, `G_p` and `T_p` satisfy the covariant overlap law on every declared overlap;
4. the overlap incidence is connected on the represented domain;
5. one common `Lambda` and one common `kappa_E` are used on all patches;
6. every patch satisfies `R_p=0`.

Compatible local tensor representatives glue to global tensors `g`, `G` and `T` on the represented atlas. The compatible residual representatives glue to one global covariant tensor

\[
\mathcal R=G+\Lambda g-\kappa_ET.
\]

Since `R|_{U_p}=0` on every member of a cover,

\[
\boxed{\mathcal R=0\text{ on }M.}
\]

Therefore

\[
\boxed{
G_{\mu\nu}+\Lambda g_{\mu\nu}=\kappa_ET_{\mu\nu}
}
\]

holds globally on the supplied, covered, RF-E25-certified spacetime domain.

This promotion is a tensor-gluing result. It does not depend on a global Cauchy theorem.

## 6. Executable certificate

The reference certifier consumes:

- a finite set of patchwise `g`, `G`, `T`, `Lambda`, `kappa_E` data;
- overlap Jacobians `J_{q<-p}`;
- the RF-E25 parent-certificate flag;
- an explicit target-domain coverage flag.

It fails closed on:

1. non-finite or non-symmetric tensor input;
2. degenerate patch metric;
3. non-positive/non-finite `kappa_E`;
4. patchwise mismatch of `Lambda` or `kappa_E`;
5. nonzero local Einstein residual;
6. singular overlap Jacobian;
7. failure of metric, Einstein-tensor or stress-tensor pullback covariance;
8. failure of residual pullback covariance;
9. disconnected multi-patch atlas;
10. global promotion requested without both RF-E25 certification and domain coverage.

The final item is represented fail-closed in the returned promotion bit: local/overlap checks may pass while `global_einstein_carrier=false` until both upstream production witnesses are supplied.

## 7. GSC-5 mapping

The FPDG mapping is

```text
GSC-1 production spatial realization
 + GSC-2 production event complex
 + GSC-3 production regular clock witness
 + GSC-4 production RF-E25 shared spacetime atlas
 -> RF-E26 local-to-global tensor glue
 -> GSC-5 global carrier carrying RF-E24
```

RF-E26 therefore provides the missing certifier definition for `GSC-5`.

Production promotion still requires the actual upstream realization and domain-coverage witnesses. A reference PASS does not substitute synthetic/reference patch data for production geometry.

## 8. Separation from RF-L7

RF-L7 proves local principal hyperbolicity and specifies the additional conditions required for a global Cauchy evolution. RF-E26 does not require or promote those stronger causal conditions.

The two coordinates are therefore typed separately:

```text
GSC-5 global Einstein carrier on supplied covered atlas     RF-E26
GSC-6 global hyperbolicity / Cauchy foliation               RF-L7 downstream gate
```

A spacetime may satisfy the global tensor equation on a covered atlas while a global Cauchy-foliation claim remains open.

## 9. Claim ledger

| Statement | Status |
|---|---|
| local Einstein-form equation | `PARENT RF-E24 PASS` |
| shared Lorentzian atlas certifier | `PARENT RF-E25 PASS` |
| covariant pullback law for rank-two tensors | `STANDARD TENSOR IDENTITY` |
| residual pullback covariance from common constants | `EXACT LINEAR ALGEBRA` |
| compatible local tensors glue on a supplied atlas | `STANDARD LOCAL-TO-GLOBAL TENSOR GLUING` |
| zero local residual on a cover implies zero global residual | `EXACT LOCALITY` |
| executable RF-E26 reference certifier | `PASS TARGET` |
| production RF-E25 atlas | `OPEN_INPUT` |
| production target-domain coverage witness | `OPEN_INPUT` |
| global Cauchy foliation / global hyperbolicity | `OPEN_SEPARATE_RF_L7_GATE` |
| coupled nonlinear global stability | `OPEN` |

## 10. Validation authority

Reference implementation:

`src/rfc/global_einstein_carrier.py`

Reference tests:

`tests/reference/test_rfe26_global_einstein_carrier.py`

Static receipt:

`validation/RFE26_GLOBAL_EINSTEIN_CARRIER_PROMOTION_V0_1.json`

Target verdict:

`PASS_RFE26_GLOBAL_EINSTEIN_CARRIER_CERTIFIER_WITH_PRODUCTION_INPUT_OPEN`.
