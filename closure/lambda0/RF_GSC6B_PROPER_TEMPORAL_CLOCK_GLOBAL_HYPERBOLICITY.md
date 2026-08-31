# RF-GSC6B — Proper Temporal Clock Global-Hyperbolicity Route

Status: `EXACT_PROPER_CLOCK_TO_COMPLETE_WICK_THEOREM / EXACT_STEEP_REPARAMETRIZATION_EXISTENCE / PRODUCT_COMPACT_FIBER_COROLLARY / PRODUCTION_PROPER_CLOCK_BINDING_OPEN`

Date: 2026-08-31

## 1. Purpose

RF-L8 supplies a completely-uniform temporal route based on a global lapse bound and completeness of the ADM Wick metric. RF-GSC6A supplies an adaptive-metric route based on completeness of `H_N`.

RF-GSC6B isolates a third sufficient route in which the global input is the properness of the temporal clock itself.

Assume a smooth global temporal function

\[
\boxed{t:M\to\mathbb R}
\]

on the production RF-E25 Lorentzian carrier and the ADM Wick metric

\[
\boxed{W=dt^2+h_{ij}(dx^i+b^i dt)(dx^j+b^j dt)}.
\]

## 2. Wick distance controls temporal distance

For every tangent vector `v`,

\[
W(v,v)=dt(v)^2+h(Y,Y)\ge dt(v)^2.
\]

Hence along every piecewise smooth curve,

\[
|\Delta t|\le L_W,
\]

and therefore for the Riemannian distance

\[
\boxed{|t(x)-t(y)|\le d_W(x,y)}.
\]

Thus `t` is 1-Lipschitz with respect to the Wick distance.

## 3. Proper clock implies completeness of W

Let `(x_n)` be a `d_W`-Cauchy sequence. The Lipschitz inequality makes `(t(x_n))` Cauchy in `R`, hence bounded. For sufficiently large `n`, all `x_n` lie in one slab

\[
t^{-1}([a,b]).
\]

If `t` is proper, the preimage of `[a,b]` is compact. Therefore `(x_n)` has a convergent subsequence in the manifold topology. The topology induced by the smooth Riemannian metric `W` is the manifold topology, so the subsequence converges in `d_W`. Since the full sequence is Cauchy, it converges to the same limit.

Therefore

\[
\boxed{t\text{ proper}\quad\Longrightarrow\quad (M,W)\text{ complete}.}
\]

## 4. Slice-wise lapse control and smooth majorant

Let `N:M->(0,infinity)` be the smooth finite ADM lapse. Properness implies every compact time slab is compact. Consequently `N` is bounded on every compact slab.

For each `s in R`, the level set `Sigma_s=t^{-1}(s)` is compact and

\[
F(s):=\sup_{x\in\Sigma_s}\sqrt{1+N(x)^2}
\]

is finite. The function `F` is locally bounded because compact intervals have compact preimages.

A locally bounded positive function on `R` admits a smooth positive majorant. Choose

\[
\boxed{m(s)>F(s),\qquad m(s)\ge1.}
\]

Define

\[
\boxed{\tau(s)=\int_0^s m(u)\,du.}
\]

Because `m>=1`, `tau:R->R` is strictly increasing and unbounded at both ends.

For every future-directed causal vector,

\[
\begin{aligned}
d(\tau\circ t)(v)
&=m(t)dt(v)\\
&\ge\sqrt{1+N^2}\,dt(v)\\
&\ge\sqrt{W(v,v)}\\
&=\|v\|_W.
\end{aligned}
\]

Thus `tau o t` is steep with respect to the complete Riemannian metric `W`.

By the external completely-uniform temporal characterization already typed by RF-L8,

\[
\boxed{t\text{ proper temporal}\quad\Longrightarrow\quad(M,g)\text{ globally hyperbolic}.}
\]

## 5. Compact-fiber product corollary

Suppose GSC3 supplies a global product trivialization

\[
\boxed{M\cong\mathbb R\times\Sigma}
\]

with the global clock equal to the projection onto `R`.

If the production GSC1/A5 spatial carrier `Sigma` is compact, then for every compact interval `[a,b]`,

\[
t^{-1}([a,b])\cong[a,b]\times\Sigma
\]

is compact. Hence the product clock is proper.

Therefore the composition

```text
compact production GSC1 spatial carrier
 + global GSC3 product trivialization over R
 + production RF-E25 Lorentzian/ADM carrier
 -> proper global temporal clock
 -> RF-GSC6B
 -> global hyperbolicity / Cauchy foliation
```

is a sufficient GSC6 route.

A finite closed tetrahedral realization accepted by the production A5/GSC1 contract is compact as a finite simplicial realization; the physical product-trivialization and common clock bindings remain separately certified by the GSC3/GSC4 surfaces.

## 6. Separation from other GSC6 routes

Three sufficient routes are now typed:

1. **RF-L8 constant-scale route:** global `N_max` + complete `W`;
2. **RF-GSC6A adaptive route:** complete `H_N=(1+N^2)^(-1)W`;
3. **RF-GSC6B proper-clock route:** proper global temporal clock `t:M->R`.

They are logical alternatives. None is promoted by finite samples.

## 7. Executable certifier

Implementation:

`src/rfc/proper_temporal_clock_global_hyperbolicity.py`

Reference tests:

`tests/reference/test_gsc6b_proper_temporal_clock.py`

The executable surface preserves properness as an explicit global input and records the exact implications:

- `W >= dt^2`;
- proper clock -> complete `W`;
- proper clock + smooth finite lapse -> smooth slice-wise lapse majorant;
- steep temporal reparametrization;
- pure global-hyperbolicity eligibility;
- separate GR Cauchy composition bit.

## 8. Live GREMLIN × Terminal36D × PhaseNav audit

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

- source event: `gremlin:whisper:sha256:3e5cbe6a1c76235d55e69bdf3645a5d08cc5c711b6c7009701429e9d0cdac7ff`;
- fused event: `gremlin:whisper:sha256:e3e2a656a30161a0f0bea1214730f9c94203cd60c0aeab434f4dbebbf0842105`;
- Terminal36D receipt: `4454a297affd9381a03f2ef8addf407ad5e2b6d9e91aa738259de1c9bbf66135`;
- PhaseNav trace: `157b3e09de67cf7d48f1a13644b7a322d6d4935658bbacc0a81b2128708462a0`;
- shape: `[13,36]`.

Runtime audit remains separate from hosted theorem validation.

## 9. Claim ledger

| Statement | Status |
|---|---|
| `W(v,v)>=dt(v)^2` | `EXACT` |
| `|t(x)-t(y)|<=d_W(x,y)` | `EXACT` |
| proper `t:M->R` implies complete `W` | `EXACT` |
| properness gives compact clock levels/slabs | `EXACT BY DEFINITION` |
| smooth finite lapse admits smooth time-only majorant on proper clock | `EXACT EXISTENCE` |
| reparametrized clock is steep relative to complete `W` | `EXACT` |
| proper temporal clock implies global hyperbolicity on the admitted carrier | `EXACT CONDITIONAL ON RF-L8 EXTERNAL THEOREM` |
| compact `Sigma` + global `R x Sigma` product implies proper projection clock | `EXACT` |
| production proper-clock/product realization | `OPEN GLOBAL INPUT` |
| nonlinear global stability | `OPEN SEPARATE` |

Target verdict:

`PASS_RFC_GSC6B_PROPER_CLOCK_GLOBAL_HYPERBOLICITY_WITH_PRODUCTION_PROPERNESS_BINDING_OPEN`.
