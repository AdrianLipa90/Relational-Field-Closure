# RF-GSC6A — Adaptive Wick Steepness Route

Status: `EXACT_POINTWISE_ADAPTIVE_STEEPNESS_THEOREM / ALTERNATIVE_GLOBAL_HYPERBOLICITY_ROUTE / PRODUCTION_ADAPTIVE_METRIC_COMPLETENESS_OPEN_INPUT`

Date: 2026-08-31

## 1. Purpose

RF-L8 proves a sufficient completely-uniform temporal route by combining a global lapse upper bound with completeness of the ADM Wick metric. RF-GSC6A gives a second sufficient route in which the lapse is absorbed pointwise into the Riemannian comparison metric.

The RF-L8 ADM carrier is

\[
g=-N^2dt^2+h_{ij}(dx^i+b^i dt)(dx^j+b^j dt),
\qquad N>0,
\]

and

\[
W=dt^2+h_{ij}(dx^i+b^i dt)(dx^j+b^j dt).
\]

For

\[
v=a\partial_t+X,
\qquad Y=X+ba,
\]

future causality gives

\[
\boxed{h(Y,Y)\le N^2a^2},
\qquad a=dt(v)>0.
\]

## 2. Adaptive comparison metric

Define

\[
\boxed{H_N:=\frac{1}{1+N^2}\,W}.
\]

Since `N` is smooth, finite and positive on the admitted ADM carrier, `H_N` is a smooth positive-definite Riemannian metric.

For every future-directed causal vector,

\[
\begin{aligned}
H_N(v,v)
&=\frac{a^2+h(Y,Y)}{1+N^2}\\
&\le\frac{a^2+N^2a^2}{1+N^2}\\
&=a^2.
\end{aligned}
\]

Therefore

\[
\boxed{dt(v)\ge\|v\|_{H_N}}
\]

pointwise for every future-directed causal vector.

The estimate is exact and retains arbitrary shift because the same shift-corrected `Y` appears in the Lorentzian causal inequality and in `W`.

## 3. Global theorem input reduction

The completely-uniform temporal characterization used by RF-L8 requires one complete Riemannian metric with respect to which the temporal function is steep.

On the RF-GSC6A route, the required metric is already `H_N`. Hence the sufficient production contract becomes

```text
global RF-E25 Lorentzian carrier
 + global regular IDT clock t
 + COMPLETE(H_N)
 -> completely uniform temporal clock
 -> global hyperbolicity / Cauchy foliation
```

where

\[
H_N=(1+N^2)^{-1}W.
\]

This route directly types the remaining global witness as

`PRODUCTION_ADAPTIVE_WICK_METRIC_COMPLETENESS`.

The original RF-L8 route using a global `N_max` and completeness of `W` remains a parallel sufficient route.

## 4. Completeness firewall

Pointwise positivity and the steepness inequality determine the local algebra of `H_N`. Global completeness is a separate global property of the supplied Riemannian carrier.

The executable certifier therefore carries no finite-sample promotion rule for completeness. Production promotion requires a source-owned analytic/topological completeness receipt for `H_N`, or another complete Riemannian metric satisfying the same steepness inequality.

## 5. GR composition

Pure causal geometry requires:

- production global Lorentzian carrier;
- production global regular temporal clock;
- production completeness witness for `H_N`.

The full GR Cauchy carrier additionally requires the production GSC-5/RF-E26 global Einstein carrier.

Nonlinear global stability remains separately typed.

## 6. Executable certifier

Implementation:

`src/rfc/adaptive_wick_steepness.py`

Reference tests:

`tests/reference/test_gsc6a_adaptive_wick_steepness.py`

The certifier checks the exact pointwise inequality and keeps the global completeness bit as an explicit input.

## 7. Live GREMLIN × Terminal36D × PhaseNav audit

The candidate was routed through the active NOEMA surface

```text
/dev/shm/ciel_noema
 -> GREMLIN
 -> Terminal36D
 -> PhaseNav 36D
 -> GREMLIN_PHASE36D_FUSED
```

with `CANDIDATE_ONLY` authority.

Fresh audit:

- source event: `gremlin:whisper:sha256:f5a4c3a286b4fe50382224645445bf76a09ae9c352bd5d392d2eb62f4aaa0fde`;
- fused event: `gremlin:whisper:sha256:09dae18902b51816e5c0f1df8e2a3f7dcc33ce617dc151f9326490d890c0a660`;
- Terminal36D receipt: `7a3fcf3f46b3a39ea65c67839aa0d06c7c5ca081b04794da1af20447a237f719`;
- PhaseNav trace: `3f351ac0923b2d741c2a67ab7c213e86d7ab41e9a5aa038d68f57bc4ca8e6fb3`;
- shape: `[10,36]`.

Runtime evidence remains audit-only.

## 8. Claim ledger

| Statement | Status |
|---|---|
| `H_N=(1+N^2)^(-1)W` is positive definite for finite positive `N` | `EXACT` |
| future causal vectors satisfy `H_N(v,v)<=dt(v)^2` | `EXACT` |
| `dt(v)>=||v||_{H_N}` | `EXACT` |
| one global finite lapse upper bound is required on this route | `ELIMINATED AS INDEPENDENT INPUT` |
| completeness of unscaled `W` is required on this route | `ELIMINATED AS INDEPENDENT INPUT` |
| production completeness of `H_N` | `OPEN GLOBAL INPUT` |
| global hyperbolicity | `CONDITIONAL ON GLOBAL CARRIER + CLOCK + COMPLETE H_N` |
| global GR Cauchy carrier | `CONDITIONAL ON GSC-5 + GSC-6A` |

Target verdict:

`PASS_RFC_GSC6A_ADAPTIVE_STEEPNESS_WITH_ADAPTIVE_METRIC_COMPLETENESS_OPEN`.
