# RF-GSC6C — Compact-Fiber Open-Interval Proper-Clock Closure

Status: `EXACT_OPEN_INTERVAL_REPARAMETRIZATION / EXACT_COMPACT_FIBER_PROPER_CLOCK_THEOREM / GSC6B_INPUT_REDUCTION / PRODUCTION_PARENT_BINDINGS_OPEN`

Date: 2026-08-31

## 1. Purpose

RF-GSC6B proves a sufficient global-hyperbolicity route from a proper temporal function `t:M->R`. RF-GSC3A supplies a global product trivialization from a regular scalar clock and an interval-complete matching flow. RF-GSC6C composes those two gates with the compactness already carried by a finite production GSC1/A5 spatial realization.

The target dependency reduction is

```text
production finite closed GSC1/A5 spatial carrier Sigma
+ production GSC3A global product trivialization M ~= I x Sigma
+ production RF-E25 Lorentzian/ADM carrier
-> orientation-preserving clock reparametrization tau:M->R
-> tau proper
-> RF-GSC6B
-> global hyperbolicity / Cauchy foliation
```

## 2. The product clock has open interval image

Let

\[
F:I\times\Sigma\overset{\sim}{\longrightarrow}M
\]

be the GSC3A product trivialization with

\[
t\circ F=\operatorname{pr}_I,
\qquad dt\neq0.
\]

The regular scalar clock is a submersion. A submersion is an open map. Since the product trivialization is onto and `I=t(M)` is an interval, the clock image is an open interval

\[
\boxed{I\subset\mathbb R\text{ open}.}
\]

The four interval types are `R`, `(a,infinity)`, `(-infinity,b)`, and `(a,b)`.

## 3. Every open interval admits an increasing diffeomorphism to R

Choose an orientation-preserving smooth diffeomorphism

\[
\boxed{\psi:I\to\mathbb R}
\]

for example

\[
\psi(t)=t\quad(I=\mathbb R),
\]

\[
\psi(t)=\ln(t-a)\quad(I=(a,\infty)),
\]

\[
\psi(t)=-\ln(b-t)\quad(I=(-\infty,b)),
\]

and

\[
\psi(t)=\ln\frac{t-a}{b-t}\quad(I=(a,b)).
\]

In every case

\[
\boxed{\psi'(t)>0.}
\]

Define

\[
\boxed{\tau=\psi\circ t:M\to\mathbb R.}
\]

Then

\[
\boxed{d\tau=\psi'(t)dt,}
\]

so the temporal orientation of the regular clock is preserved.

## 4. Compact spatial fiber implies proper reparametrized clock

Let the production GSC1/A5 spatial carrier `Sigma` be compact. For a finite closed tetrahedral realization this compactness is inherited from finite simplicial realization.

For every compact `K subset R`,

\[
\psi^{-1}(K)\subset I
\]

is compact because `psi^{-1}` is continuous. Under the product trivialization,

\[
F^{-1}(\tau^{-1}(K))
=\psi^{-1}(K)\times\Sigma.
\]

The product of two compact spaces is compact. Therefore

\[
\boxed{\tau^{-1}(K)\text{ is compact for every compact }K\subset\mathbb R.}
\]

Hence

\[
\boxed{\tau:M\to\mathbb R\text{ is proper}.}
\]

## 5. Composition with RF-GSC6B

RF-GSC6B then supplies

\[
\tau\text{ proper temporal}
\Longrightarrow
(M,W)\text{ complete}
\Longrightarrow
\text{steep temporal reparametrization}
\Longrightarrow
\text{global hyperbolicity}
\]

on the admitted production RF-E25 Lorentzian/ADM carrier with smooth finite positive lapse.

Thus the compact-fiber product route removes a separately supplied proper-clock witness from the GSC6 production frontier. The production burden is carried by already typed upstream parents:

1. production finite closed GSC1/A5 compact spatial realization;
2. production GSC3A interval-complete product trivialization and common clock binding;
3. production RF-E25 Lorentzian/ADM carrier;
4. RF-E26/GSC5 only for the stronger global GR Cauchy carrier composition.

## 6. Executable surface

Implementation:

`src/rfc/compact_fiber_open_interval_proper_clock.py`

Reference tests:

`tests/reference/test_gsc6c_compact_fiber_open_interval_proper_clock.py`

The implementation explicitly covers all four open-interval types and checks positive derivative of the chosen reparametrization. The route certifier keeps the product, regular-clock, compact-fiber, RF-E25 carrier, lapse, and RF-E26/GSC5 parent bits separately typed.

## 7. Live GREMLIN × Terminal36D × PhaseNav audit

The reduction was independently routed through the active NOEMA surface

```text
/dev/shm/ciel_noema
 -> GREMLIN
 -> Terminal36D
 -> PhaseNav 36D
 -> GREMLIN_PHASE36D_FUSED
```

with `CANDIDATE_ONLY` authority.

Fresh audit:

- source event: `gremlin:whisper:sha256:28d14e4b42d0c9b860eeab8c7f5dd40b3d2377fd6fa3124fa8f7ff1060c754b7`;
- fused event: `gremlin:whisper:sha256:a00e284674c715c30ff40bef2e1c41df6e2a033cfc8247592aa836521bdd6962`;
- Terminal36D receipt: `83b828f66599427b4968c14757d9f50a5e982aedf007c1668756a5f09285bc26`;
- PhaseNav trace: `bed9ad75952a708af37e3dcf2e1aa85e35b0bdec7479e73de6f565be7ee3267f`;
- shape: `[10,36]`.

Runtime evidence remains an audit layer; deterministic hosted validation is the theorem execution surface.

## 8. Claim ledger

| Statement | Status |
|---|---|
| regular onto GSC3A product clock has open interval image | `EXACT` |
| every open interval admits an orientation-preserving diffeomorphism to R | `EXACT` |
| positive reparametrization preserves temporal orientation | `EXACT` |
| compact Sigma + product clock gives proper R-valued reparametrized clock | `EXACT` |
| separate GSC6 properness witness on this route | `DERIVED FROM UPSTREAM PRODUCTION PARENTS` |
| global hyperbolicity after RF-GSC6B composition | `EXACT CONDITIONAL ON RF-L8 EXTERNAL THEOREM AND PRODUCTION PARENTS` |
| production GSC1 compact carrier | `OPEN SOURCE INPUT` |
| production GSC3A product realization/common clock | `OPEN SOURCE INPUT` |
| production RF-E25 Lorentzian/ADM carrier | `OPEN SOURCE INPUT` |
| global GR Cauchy carrier | `REQUIRES PRODUCTION GSC5 / RF-E26` |

Target verdict:

`PASS_RFC_GSC6C_COMPACT_FIBER_PRODUCT_ROUTE_WITH_SEPARATE_PROPERNESS_INPUT_REMOVED`.
