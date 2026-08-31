# RF-GSC3A — Proper-Clock Flow-Coverage Route

Status: `EXACT_PROPER_CLOCK_IMPLIES_INTERVAL_COMPLETE_FLOW / GLOBAL_CLOCK_PROPERNESS_OPEN_ANALYTIC_INPUT / GSC3A_PRODUCT_TRIVIALIZATION_HANDOFF`

Date: 2026-08-31

## 1. Purpose

RF-GSC3A derives the product trivialization

\[
M\cong I\times\Sigma_{t_0}
\]

from a global clock-transverse matching field

\[
X,
\qquad dt(X)=1,
\]

once the `X` flow covers every required finite displacement inside the admitted clock interval `I`.

This addendum gives a sharper sufficient route for that coverage premise.

## 2. Proper global clock

Let

\[
\boxed{t:M\to I\subset\mathbb R}
\]

be the admitted smooth regular clock. Assume `t` is proper: for every compact subset

\[
K\subset I,
\]

the preimage

\[
\boxed{t^{-1}(K)}
\]

is compact in `M`.

Let `X` be the global smooth matching field certified by RF-GSC3A with

\[
\boxed{dt(X)=1.}
\]

## 3. Finite-displacement continuation theorem

Let `m in M` and choose any target clock value `tau in I`. Along the maximal integral curve of `X`,

\[
\frac{d}{ds}t(\Phi_s(m))=1,
\]

so

\[
\boxed{t(\Phi_s(m))=t(m)+s.}
\]

The target is reached at the finite flow parameter

\[
\boxed{s_*=\tau-t(m).}
\]

Every intermediate clock value lies inside the compact interval

\[
K=
[\min(t(m),\tau),\max(t(m),\tau)]
\subset I.
\]

Therefore the corresponding trajectory segment lies in

\[
\boxed{t^{-1}(K)}.
\]

Properness makes this subset compact. The standard continuation theorem for smooth ordinary differential equations extends an integral curve through each finite parameter interval while its image remains in a compact subset of the manifold.

Hence the flow reaches `s_*`.

Since `m` and `tau` were arbitrary,

\[
\boxed{
t\text{ proper}+dt(X)=1
\Longrightarrow
X\text{ is interval-complete over }I.
}
\]

The statement applies in both clock directions because `s_*` may have either sign.

## 4. Product-trivialization consequence

Choose one reference value

\[
t_0\in I
\]

and its leaf

\[
\Sigma_{t_0}=t^{-1}(t_0).
\]

The proper-clock theorem supplies the flow-coverage premise of RF-GSC3A. Therefore

\[
\boxed{
F(\tau,p)=\Phi_{\tau-t_0}(p)
}
\]

is defined for every

\[
(\tau,p)\in I\times\Sigma_{t_0}
\]

and RF-GSC3A gives

\[
\boxed{F:I\times\Sigma_{t_0}\overset{\sim}{\longrightarrow}M.}
\]

Thus the production closure has two sufficient routes:

```text
ROUTE A
GLOBAL_INTERVAL_COMPLETE_FLOW_COVERAGE
 -> RF-GSC3A product trivialization

ROUTE B
GLOBAL_CLOCK_PROPERNESS
 + dt(X)=1
 -> interval-complete flow
 -> RF-GSC3A product trivialization
```

## 5. Relation to TIR A5

TIR A5 supplies the production target type for the reference spatial leaf: a connected closed smooth three-manifold realization after its actual relational-complex incidence certificate passes.

For the finite closed simplicial carrier used by A5, the certified spatial realization is compact. This is the spatial fiber-side compactness entering the intended global realization. Route B retains global clock properness as the separate spacetime-wide analytic/topological coordinate.

## 6. Production gate

The theorem status is

`EXACT_PROPER_CLOCK_IMPLIES_INTERVAL_COMPLETE_FLOW`.

The production input status is

`GLOBAL_CLOCK_PROPERNESS_OPEN_ANALYTIC_INPUT`.

A production properness receipt promotes the RF-GSC3A flow-coverage coordinate through Route B. Physical event placement and the downstream RF-E25 Lorentz/coframe realization retain their independently typed production gates.

## 7. Claim ledger

| Claim | Status |
|---|---|
| `dt(X)=1` gives `t(Phi_s(m))=t(m)+s` | `EXACT` |
| properness makes each finite clock slab preimage compact | `DEFINITIONAL` |
| compact-slab confinement gives finite-time ODE continuation | `STANDARD ODE CONTINUATION THEOREM` |
| proper clock implies interval-complete matching flow | `EXACT CONDITIONAL THEOREM` |
| interval-complete matching flow gives `M ≅ I x Sigma_t0` | `RF-GSC3A EXACT CONDITIONAL THEOREM` |
| production global-clock properness | `OPEN ANALYTIC INPUT` |
