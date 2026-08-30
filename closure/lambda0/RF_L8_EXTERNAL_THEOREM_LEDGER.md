# RF-L8 External Theorem Ledger

Status: `EXTERNAL_GLOBAL_CAUSALITY_THEOREMS_TYPED / NO_INTERNAL_PROMOTION_BY_CITATION`

## E1 — Completely uniform / complete-metric steep temporal characterization

Primary references:

1. Patrick Bernard, Stefan Suhr, *Lyapounov Functions of closed Cone Fields: from Conley Theory to Time Functions*, arXiv:1512.08410, published in Communications in Mathematical Physics (2018). Theorem 3 gives the global-hyperbolicity / smooth steep Lyapounov-function equivalence for nondegenerate closed cone fields, including Lorentzian spacetimes.
2. Patrick Bernard, Stefan Suhr, *Cauchy and uniform temporal functions of globally hyperbolic cone fields*, Proceedings of the American Mathematical Society 148 (2020), 4951-4966, DOI 10.1090/proc/15106.

Modern crosscheck used for terminology:

Annegret Burtscher, Leonardo García-Heveling, *Global Hyperbolicity through the Eyes of the Null Distance*, Communications in Mathematical Physics (2024). The paper defines a completely uniform temporal function by the existence of a complete Riemannian metric `h` satisfying

\[
d\tau(v)\ge \|v\|_h
\]

for all causal vectors and records the Bernard-Suhr/Minguzzi equivalence with global hyperbolicity.

Imported result used by RF-L8:

```text
complete Riemannian metric H
+ smooth temporal tau
+ d tau(v) >= ||v||_H for every future causal vector v
------------------------------------------------------------
=> global hyperbolicity
```

RFC-side obligations before application:

```text
global Lorentzian carrier              -> RF-E25 / production GSC-4
smooth regular temporal clock t         -> IDT 05I + 05G / production GSC-3
future time orientation                 -> RF-E25
positive lapse                          -> IDT 05C / RF-E8 / RF-E25
global finite lapse upper bound         -> OPEN production witness
ADM Wick metric W                       -> RF-L8 exact definition
W complete                              -> OPEN production analytic/topological witness
steepness inequality                    -> RF-L8 exact ADM estimate
```

The citation provides theorem authority only after those RFC/IDT-side premises are independently certified. It does not promote the open global bound or completeness premises.

## E2 — Smooth Cauchy temporal splitting

Reference:

Antonio N. Bernal, Miguel Sánchez, *Smoothness of time functions and the metric splitting of globally hyperbolic spacetimes*, Communications in Mathematical Physics 257 (2005), 43-50, DOI 10.1007/s00220-005-1346-1, arXiv:gr-qc/0401112.

Imported result used as a consistency crosscheck:

- a smooth globally hyperbolic spacetime admits a smooth time function whose level sets are spacelike Cauchy hypersurfaces and a smooth product splitting;
- stable causality admits smoothing to a temporal function with timelike gradient.

RF-L8 uses E1 for the forward promotion from the proof-carrying steepness/completeness witness to global hyperbolicity. E2 records the corresponding smooth Cauchy-foliation/splitting structure after that promotion.

## E3 — RF-L7 normally hyperbolic Cauchy theorem

RF-L7 separately imports:

C. Bär, N. Ginoux, F. Pfäffle, *Wave Equations on Lorentzian Manifolds and Quantization*, arXiv:0806.1036.

Once RF-L8 promotes the global Cauchy geometry and the remaining regularity/data premises are supplied, RF-L7 may invoke its normally-hyperbolic global Cauchy theorem. RF-L8 does not itself promote PDE regularity, support or nonlinear stability.
