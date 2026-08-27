# RF-L0 — Temporal Information Curvature Closure

Status: `EXACT_TIR_IDT_INTERFACE / LAMBDA0_COUPLING_CANDIDATE / ACTION_LEVEL_METRIC_VARIATION_OPEN`

Pinned upstreams for this gate:

- TIR `main`: `d21631fe7281b5dbbad70f3a4a5f5b4876cac9f7`
- IDT `main`: `647f1652edde59d9bfd7e075fb6ed5bf02aab2fc`
- Secret of a Half `main`: `206e49e306b246c4b0f4d182b0d32d5511739408`

## 1. Exact imported scalar

TIR supplies a positive physical relational area

\[
\mathcal A_{\rm rel}=\ell_R^2 a_{FS},
\qquad
[\mathcal A_{\rm rel}]=L^2,
\]

while IDT supplies the relative-information scalar and its temporal evolution. Define

\[
\mathcal J_\pi=(\ln2)\mathcal I_\pi
\]

and

\[
\boxed{
\Xi_I
:=\frac{\mathcal J_\pi}{\mathcal A_{\rm rel}}
=\frac{24\pi\kappa}{\mathcal A_{\rm rel}}\mathcal I_\pi.
}
\]

Then exactly

\[
\boxed{[\Xi_I]=L^{-2}.}
\]

The temporal rate is inherited from IDT:

\[
\boxed{
\frac{d\Xi_I}{d\tau_{\rm int}}
=\frac{1}{\mathcal A_{\rm rel}}
\frac{d\mathcal J_\pi}{d\tau_{\rm int}}
-\frac{\Xi_I}{\mathcal A_{\rm rel}}
\frac{d\mathcal A_{\rm rel}}{d\tau_{\rm int}}.
}
\]

## 2. Information contribution to the dynamic scalar sector

Introduce a dimensionless coupling `alpha_I` and define

\[
\boxed{
\Lambda_I:=\alpha_I\Xi_I.
}
\]

Therefore

\[
\boxed{[\Lambda_I]=L^{-2}.}
\]

The general scalar-basis candidate is

\[
\boxed{
\Lambda_0
=\Lambda_{\rm vac}
+\alpha_I\Xi_I
+\sum_r\alpha_r\mathcal S_r,
}
\]

where each admitted `S_r` has type `L^-2` and each `alpha_r` is dimensionless after the chosen field normalization.

The exact functional sensitivity of the information-area channel is

\[
\boxed{
\frac{\partial\Lambda_0}{\partial\Xi_I}=\alpha_I.
}
\]

For the minimal information-only truncation

\[
\Lambda_0=\Lambda_{\rm vac}+\alpha_I\Xi_I,
\]

one obtains

\[
\boxed{
\frac{d\Lambda_0}{d\tau_{\rm int}}
=\alpha_I\frac{d\Xi_I}{d\tau_{\rm int}}.
}
\]

Thus a nonzero `alpha_I` gives an exact temporal-information coupling in the minimal sector. In the multi-sector form,

\[
\frac{d\Lambda_0}{d\tau_{\rm int}}
=\alpha_I\frac{d\Xi_I}{d\tau_{\rm int}}
+\sum_r\alpha_r\frac{d\mathcal S_r}{d\tau_{\rm int}},
\]

so the total rate carries all admitted scalar channels and can include exact inter-sector cancellation.

## 3. Bianchi bookkeeping

For the phenomenological field-equation convention

\[
G_{\mu\nu}+\Lambda_0 g_{\mu\nu}
=\frac{8\pi G}{c^4}T^{\rm visible}_{\mu\nu},
\]

the contracted Bianchi identity gives

\[
\boxed{
\nabla_\mu T_{\rm visible}^{\mu\nu}
=\frac{c^4}{8\pi G}\nabla^\nu\Lambda_0.
}
\]

The information-area channel therefore contributes

\[
\boxed{
\nabla^\nu\Lambda_0
=\alpha_I\nabla^\nu\Xi_I
+\sum_r\alpha_r\nabla^\nu\mathcal S_r.
}
\]

This equation is a bookkeeping identity for the displayed convention. The action-level stress-energy partition is a separate closure gate.

## 4. Action-level metric-variation firewall

Consider the Einstein-Hilbert-type scalar action term

\[
S_{\Lambda}
=-\frac{c^3}{8\pi G}
\int d^4x\,\sqrt{-g}\,\Lambda_0.
\]

When `Lambda0` is independent of `g^{mu nu}` during metric variation, its contribution reduces to the familiar `Lambda0 g_{mu nu}` term.

When `Lambda0` contains metric-dependent invariants, the variation also carries the metric sensitivity of those invariants. For purely algebraic metric dependence,

\[
\boxed{
G_{\mu\nu}
+\Lambda_0 g_{\mu\nu}
-2\frac{\partial\Lambda_0}{\partial g^{\mu\nu}}
=\frac{8\pi G}{c^4}T_{\mu\nu}.
}
\]

For derivative-dependent functionals, the partial derivative is replaced by the corresponding functional Euler-Lagrange variation.

This gate is essential for `Xi_I` because RFC must decide whether the physical relational area used in `Xi_I` is an independent projective-area carrier or a functional of the emergent spacetime metric.

## 5. Temporal coupling criterion

RFC records the following typed criterion:

```text
TEMPORAL_INFORMATION_LAMBDA_COUPLING
  requires:
    alpha_I != 0
    Xi_I admitted from pinned TIR + IDT
  exact sensitivity:
    d Lambda0 / d Xi_I = alpha_I
```

For the minimal information sector, temporal variation of `Xi_I` and temporal variation of the information contribution `Lambda_I` are in one-to-one linear correspondence.

The author/formalism may suggest a stronger global inseparability of time and `Lambda0`, yet does not state that stronger claim as an established result until the remaining scalar sectors and action-level closure are fixed.

## 6. Promotion gates

RF-L0 advances only when the following are separately receipted:

1. TIR relational-area calibration/refinement;
2. IDT `Xi_I` temporal evolution;
3. empirical or derived `ell_R` normalization;
4. `alpha_I` determination or falsifiable bound;
5. action-level metric dependence of `A_rel`;
6. Bianchi/stress-energy partition;
7. Newton and Einstein limit tests.
