# RF-N1C1 — Phase-Source Specialization of the Newton ↔ Double-Copy ↔ Einstein Bridge

Status: `EXACT_PHASE_SOURCE_REDUCTION / RATE_CANCELLATION_IN_SOURCE_LAW / NEWTON_EINSTEIN_MATCH_PASS_CONDITIONAL / UNIVERSAL_G_GATE_EXPOSED`

RF-N1C1 consumes RF-N1B2O and RF-N1C. It specializes the generic carrier coordinate `j_Q` to the admitted gauge-covariant phase Noether density `j_theta` and exposes the resulting cancellation structure.

## 1. Phase-source inputs

RF-N1B2O gives, on the positive phase-kinetic matter sector,

\[
\boxed{
j_\vartheta=2A^2\omega_Q,
\qquad
\rho_\vartheta=\frac{\omega_Q}{2c^2}j_\vartheta
=\frac{A^2\omega_Q^2}{c^2},
}
\]

with

\[
\omega_Q=D_{\hat\tau}\chi.
\]

In natural units,

\[
\boxed{\rho_\vartheta=A^2\omega_Q^2.}
\]

## 2. Double-copy coupling

RF-N1C gives

\[
\boxed{
G_{DC}=\frac{18\Gamma_{DC}^2}{\pi\beta_W^2\omega_Q^2}
}
\]

on the independently gated local carrier-scale candidate `M_star=omega_Q/2`.

The RF-N1C source law is

\[
\mathcal S_R^{DC}
=\frac{36\Gamma_{DC}^2}{\beta_W^2\omega_Q}j_\vartheta.
\]

Substituting `j_theta=2 A^2 omega_Q` gives the exact reduction

\[
\boxed{
\mathcal S_R^{DC}
=\frac{72\Gamma_{DC}^2}{\beta_W^2}A^2.
}
\]

The local normal phase rate cancels from the curvature-source expression.

## 3. Newton-product cancellation

Although `G_DC` scales as `omega_Q^-2`, the phase mass density scales as `omega_Q^2`:

\[
G_{DC}\propto\omega_Q^{-2},
\qquad
\rho_\vartheta\propto\omega_Q^2.
\]

Their product is therefore

\[
\boxed{
G_{DC}\rho_\vartheta
=\frac{18\Gamma_{DC}^2}{\pi\beta_W^2}A^2,
}
\]

and the Newton source law gives

\[
\boxed{
4\pi G_{DC}\rho_\vartheta
=\frac{72\Gamma_{DC}^2}{\beta_W^2}A^2
=\mathcal S_R^{DC}.
}
\]

Thus the phase-rate dependence cancels exactly in the physical source product on this sector.

## 4. Einstein consistency

RF-N1C supplies

\[
\kappa_E^{DC}=8\pi G_{DC}.
\]

The weak-field Einstein source is

\[
\mathcal S_R=\frac12\kappa_E\rho_\vartheta.
\]

Therefore

\[
\boxed{
\frac12\kappa_E^{DC}\rho_\vartheta
=4\pi G_{DC}\rho_\vartheta
=\mathcal S_R^{DC}.
}
\]

The Newton and Einstein source normalizations remain identical after the RF-N1B2O phase-source specialization.

## 5. Phase-rate rescaling theorem

For fixed `A`, `beta_W` and `Gamma_DC`, let

\[
\omega_Q\mapsto\lambda\omega_Q,
\qquad \lambda>0.
\]

Then

\[
\boxed{
\rho_\vartheta\mapsto\lambda^2\rho_\vartheta,
\qquad
G_{DC}\mapsto\lambda^{-2}G_{DC},
\qquad
\mathcal S_R^{DC}\mapsto\mathcal S_R^{DC}.
}
\]

This exact reciprocal scaling is the phase-source coupling holonomy.

## 6. Universality consequence

The cancellation above protects the local source law, while a universal Newton constant additionally requires the double-copy coupling coordinate itself to remain source-independent. That condition is isolated in RF-N1C2.

The candidate local scale binding

\[
M_\star=\omega_Q/2
\]

therefore reaches promotion only together with an independently verified universality mechanism for the combination entering `G_DC`.

## 7. Advancement

```text
j_theta = 2 A^2 omega_Q                      PASS via RF-N1B2O
rho_theta = A^2 omega_Q^2 / c^2             PASS conditional phase sector
G_DC proportional to omega_Q^-2             inherited RF-N1C candidate surface
S_R^DC = 72 Gamma_DC^2 A^2 / beta_W^2       PASS EXACT REDUCTION
4 pi G_DC rho_theta = S_R^DC                 PASS EXACT
(1/2) kappa_E^DC rho_theta = S_R^DC          PASS EXACT
phase-rate rescaling source holonomy         PASS EXACT
universal G across source/species sectors    RF-N1C2 firewall
```
