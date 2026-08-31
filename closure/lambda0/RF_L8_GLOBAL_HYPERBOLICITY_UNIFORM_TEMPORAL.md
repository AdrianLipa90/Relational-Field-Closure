# RF-L8 — Global Hyperbolicity from a Completely Uniform Relational Clock

Status: `EXACT_ADM_CAUSAL_STEEPNESS_BOUND / EXTERNAL_GLOBAL_HYPERBOLICITY_CHARACTERIZATION / PROOF_CARRYING_CERTIFIER / PRODUCTION_WICK_COMPLETENESS_OPEN_INPUT`

Date: 2026-08-30

## 1. Purpose

RF-L7 closes the local normally-hyperbolic/Cauchy-data contract for the RFC scalar sector and leaves the global Cauchy-foliation premise open. RF-L8 supplies a noncircular global promotion route for that premise.

The route uses the IDT/RFC global clock and the ADM geometry already exported by RF-E8/RF-E25. It does not infer global hyperbolicity from local samples. Instead it proves an exact ADM steepness estimate and imports a standard global theorem only after two explicitly global witnesses are supplied:

1. a certified global finite upper bound on the relational lapse;
2. completeness of the associated Wick-rotated Riemannian metric.

## 2. Parent surfaces

Required RFC/IDT parents:

- IDT 05I regular smooth clock-extension witness;
- IDT 05G positive-lapse temporal foliation;
- RFC RF-E8 ADM metric/coframe carrier;
- RFC RF-E25 shared Lorentzian atlas/coframe cocycle;
- RFC RF-L7 local principal-hyperbolicity and Cauchy-data contract.

For full GR composition, production RF-E26/GSC-5 may be supplied as an additional downstream parent. The pure global-hyperbolicity theorem itself depends only on the global Lorentzian/clock geometry.

## 3. ADM clock geometry

Use the RFC ADM convention

\[
g=-N^2dt^2+h_{ij}(dx^i+b^i dt)(dx^j+b^j dt),
\qquad N>0.
\]

For a tangent vector

\[
v=a\,\partial_t+X^i\partial_i,
\qquad a=dt(v),
\]

define the shift-corrected spatial component

\[
Y^i=X^i+b^i a.
\]

Then

\[
\boxed{g(v,v)=-N^2a^2+h(Y,Y).}
\]

On the RF-E25 time orientation, every future-directed causal vector satisfies

\[
a=dt(v)>0,
\qquad
h(Y,Y)\le N^2a^2.
\]

The inverse ADM metric also gives

\[
\boxed{g^{-1}(dt,dt)=-\frac{1}{N^2}<0,}
\]

so the supplied global clock is temporal wherever the positive-lapse ADM carrier is regular.

## 4. Wick-rotated metric

Define the positive-definite ADM Wick metric

\[
\boxed{
W:=dt^2+h_{ij}(dx^i+b^i dt)(dx^j+b^j dt).
}
\]

For the same future-directed causal vector,

\[
W(v,v)=a^2+h(Y,Y).
\]

If one global finite lapse bound is certified,

\[
0<N(x)\le N_{\max}<\infty
\qquad \forall x\in M,
\]

then

\[
\begin{aligned}
W(v,v)
&=a^2+h(Y,Y)\\
&\le (1+N^2)a^2\\
&\le (1+N_{\max}^2)a^2.
\end{aligned}
\]

Set

\[
\boxed{
\varepsilon=(1+N_{\max}^2)^{-1/2}>0,
\qquad
H:=\varepsilon^2W.
}
\]

Therefore

\[
\|v\|_H
=\varepsilon\sqrt{W(v,v)}
\le a
=dt(v),
\]

hence

\[
\boxed{dt(v)\ge\|v\|_H}
\]

for every future-directed causal vector on the target domain.

This estimate is exact and shift-compatible because the shift enters only through the same `Y` in both the Lorentzian causal inequality and the Wick metric.

## 5. Completeness transfer

A constant positive rescaling preserves Riemannian completeness. Thus

\[
W\text{ complete}
\quad\Longrightarrow\quad
H=\varepsilon^2W\text{ complete}.
\]

RF-L8 does not infer completeness from finite point samples. The production gate therefore requires a source-owned analytic/topological completeness witness for `W`, or another independently proved complete Riemannian metric satisfying the same steepness inequality.

Status:

`PRODUCTION_WICK_COMPLETENESS_OPEN_INPUT`.

## 6. Imported global theorem

The external theorem ledger records the standard characterization used here:

> a spacetime is globally hyperbolic exactly when it admits a completely uniform/complete-metric steep temporal function; equivalently there exists a complete Riemannian metric `H` such that `d tau(v) >= ||v||_H` for all future-directed causal vectors.

RF-L8 supplies the RFC-side temporal and steepness algebra. The external theorem is invoked only when completeness and the global lapse-bound witnesses are independently supplied.

Therefore the production implication is

\[
\boxed{
\begin{gathered}
\text{global RF-E25 Lorentzian carrier}
+\text{global regular IDT clock }t\\
+\;0<N\le N_{\max}<\infty\\
+\;W\text{ complete}
\\[2mm]
\Longrightarrow\quad
(M,g)\text{ globally hyperbolic}.
\end{gathered}}
\]

The same theorem line promotes the clock level sets to the Cauchy-foliation class required by RF-L7.

## 7. Separation of geometry and GR composition

RF-L8 returns two logically distinct promotion bits.

### 7.1 Pure causal geometry

`global_hyperbolicity=true` requires:

- global Lorentzian carrier supplied;
- global regular temporal clock supplied;
- certified global finite lapse upper bound supplied;
- Wick-completeness witness supplied.

### 7.2 Full GR Cauchy carrier

`global_gr_cauchy_carrier=true` additionally requires the production global Einstein carrier from RF-E26/GSC-5.

Thus the global causality theorem is not made circularly dependent on Einstein's equation, while the final FPDG GR composition can require both GSC-5 and GSC-6.

## 8. GSC-6 mapping

```text
GSC-3 production global regular clock
 + GSC-4 production shared Lorentzian atlas
 + GLOBAL_LAPSE_UPPER_BOUND witness
 + COMPLETE_ADM_WICK_METRIC witness
 -> RF-L8 completely-uniform-clock certifier
 -> GSC-6 GLOBAL_HYPERBOLICITY / CAUCHY_FOLIATION
```

For the full GR carrier:

```text
GSC-5 production global Einstein carrier
 + GSC-6 production global hyperbolicity
 -> GLOBAL_GR_CAUCHY_CARRIER
```

Reference controls validate the exact bound and the fail-closed promotion logic. Reference data do not replace the global production witnesses.

## 9. Falsification / fail-closed rules

RF-L8 fails or withholds promotion when any of the following occurs:

1. the lapse is non-positive or non-finite;
2. a claimed global lapse upper bound is non-positive/non-finite;
3. a checked lapse exceeds the declared bound;
4. a tested future-causal vector has `dt(v)<=0` on the selected time orientation;
5. a vector declared causal violates `h(Y,Y)<=N^2 dt(v)^2`;
6. the derived Wick steepness inequality is violated;
7. global Lorentzian carrier is absent;
8. global regular clock is absent;
9. global lapse-bound certification is absent;
10. Wick-metric completeness certification is absent.

Failure of item 10 leaves the local/pointwise steepness theorem intact but keeps global hyperbolicity open.

## 10. Claim ledger

| Statement | Status |
|---|---|
| `g(v,v)=-N^2 a^2+h(Y,Y)` | `EXACT ADM IDENTITY` |
| `g^{-1}(dt,dt)=-1/N^2` | `EXACT ADM IDENTITY` |
| causal `h(Y,Y)<=N^2 a^2` | `EXACT` |
| `W(v,v)<= (1+Nmax^2)a^2` | `EXACT UNDER GLOBAL LAPSE BOUND` |
| `epsilon=(1+Nmax^2)^(-1/2)` steepness scale | `EXACT` |
| `dt(v)>=||v||_H` for future causal `v` | `EXACT UNDER DECLARED BOUND` |
| completeness preserved by positive constant rescaling | `STANDARD RIEMANNIAN RESULT` |
| completely uniform temporal function iff global hyperbolicity | `EXTERNAL THEOREM` |
| RF-L8 executable algebra/promotion certifier | `PASS TARGET` |
| production global lapse bound | `OPEN_INPUT` |
| production Wick-metric completeness | `OPEN_INPUT` |
| production global hyperbolicity | `CONDITIONAL_ON_GLOBAL_WITNESSES` |
| coupled nonlinear global stability | `OPEN_SEPARATE` |

## 11. Validation authority

Reference implementation:

`src/rfc/global_hyperbolicity_uniform_temporal.py`

Reference tests:

`tests/reference/test_rfl8_global_hyperbolicity_uniform_temporal.py`

External theorem ledger:

`closure/lambda0/RF_L8_EXTERNAL_THEOREM_LEDGER.md`

Static receipt:

`validation/RFL8_GLOBAL_HYPERBOLICITY_UNIFORM_TEMPORAL_V0_1.json`

Target verdict:

`PASS_RF_L8_UNIFORM_TEMPORAL_GLOBAL_HYPERBOLICITY_CERTIFIER_WITH_COMPLETENESS_INPUT_OPEN`.
