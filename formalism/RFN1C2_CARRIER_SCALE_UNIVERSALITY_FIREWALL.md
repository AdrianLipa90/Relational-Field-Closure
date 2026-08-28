# RF-N1C2 — Double-Copy Carrier-Scale Universality Firewall

Status: `EXACT_UNIVERSALITY_REPARAMETERIZATION / REDUCED_GRAVITY_SCALE_IDENTIFIED / LOCAL_CARRIER_SCALE_PROMOTION_GATED / ZERO_FIT_CROSS_SYSTEM_TEST_DEFINED`

RF-N1C2 consumes RFG2/RFG3, RF-N1C and RF-N1C1. Its role is to isolate the exact source-independent combination required for a universal Newton coupling.

## 1. General double-copy coupling

RFG2 gives, in natural units,

\[
\boxed{
G_{DC}
=\frac{\Gamma_{DC}^2g_{YM}^4}{8\pi M_\star^2}.
}
\]

Define the reduced gravity-scale coordinate

\[
\boxed{
\bar M_G
:=\frac{M_\star}{\Gamma_{DC}g_{YM}^2}.
}
\]

Then exactly

\[
\boxed{
G_{DC}=\frac{1}{8\pi\bar M_G^2}.
}
\]

Thus all double-copy normalization freedom relevant to the Newton coupling collapses to one positive dimensionful coordinate `Mbar_G`.

## 2. Wilson form

RFG3 supplies

\[
g_{YM}^2=\frac6{\beta_W}.
\]

Therefore

\[
\boxed{
\bar M_G
=\frac{\beta_WM_\star}{6\Gamma_{DC}}.
}
\]

On the RF-N1C local carrier-scale candidate

\[
M_\star=\epsilon_Q=\frac12\omega_Q,
\]

this becomes

\[
\boxed{
\bar M_G^{local}
=\frac{\beta_W\omega_Q}{12\Gamma_{DC}}.
}
\]

and hence

\[
\boxed{
G_{DC}
=\frac{18\Gamma_{DC}^2}{\pi\beta_W^2\omega_Q^2}.
}
\]

## 3. Universality theorem

For any two independently admitted weak-field systems `a,b`,

\[
G_a=G_b
\]

is equivalent to

\[
\boxed{
\bar M_{G,a}=\bar M_{G,b}
}
\]

on the positive scale sector.

Equivalently,

\[
\boxed{
\frac{G_a}{G_b}
=\left(\frac{\bar M_{G,b}}{\bar M_{G,a}}\right)^2.
}
\]

For the local carrier-scale candidate this becomes

\[
\boxed{
\frac{G_a}{G_b}
=\left(
\frac{\beta_{W,b}\omega_{Q,b}/\Gamma_{DC,b}}
{\beta_{W,a}\omega_{Q,a}/\Gamma_{DC,a}}
\right)^{-2}.
}
\]

Therefore a universal Newton coupling requires

\[
\boxed{
\frac{\beta_W\omega_Q}{\Gamma_{DC}}
=\text{source-independent constant}
}
\]

on every system admitted to the same gravity sector.

## 4. Fixed gauge-normalization corollary

If `beta_W` and `Gamma_DC` are universal constants across two source sectors, then

\[
\boxed{
\frac{G_a}{G_b}
=\left(\frac{\omega_{Q,b}}{\omega_{Q,a}}\right)^{-2}.
}
\]

Hence different phase rates give different `G_DC` values on the direct local binding `M_star=omega_Q/2` unless another admitted mechanism changes the relevant normalization coordinates.

This is a falsification coordinate for the local scale binding, not a fitted correction rule.

## 5. Source-law cancellation remains distinct

RF-N1C1 gives

\[
\mathcal S_R^{DC}
=\frac{72\Gamma_{DC}^2}{\beta_W^2}A^2
\]

on the phase-source specialization. Therefore local source curvature can remain invariant under a phase-rate rescaling even while `G_DC` changes, because the phase mass density transforms reciprocally.

The two questions are therefore separately audited:

```text
local source-law closure      -> G_DC rho_theta product
universal gravity coupling    -> Mbar_G source-independence
```

## 6. General-scale alternative coordinate

Keeping `M_star` independent of the local phase-energy coordinate gives

\[
\boxed{
G_{DC}=\frac{1}{8\pi\bar M_G^2}
}
\]

with `Mbar_G` tested directly across systems.

For the phase-source sector, equating `G_N=G_DC` before imposing `M_star=omega_Q/2` gives

\[
\boxed{
\mathcal S_R
=\frac{\Gamma_{DC}^2g_{YM}^4}{4M_\star^2}\,\omega_Qj_\vartheta.
}
\]

Using `j_theta=2A^2 omega_Q`,

\[
\boxed{
\mathcal S_R
=\frac{\Gamma_{DC}^2g_{YM}^4}{2M_\star^2}A^2\omega_Q^2.
}
\]

The local-scale surface `M_star=omega_Q/2` is one exact specialization of this more general relation.

## 7. Cross-system executable defects

Define

\[
\boxed{
\delta_{M_G}^{ab}
=\frac{2|\bar M_{G,a}-\bar M_{G,b}|}
{|\bar M_{G,a}|+|\bar M_{G,b}|}
}
\]

and

\[
\boxed{
\delta_G^{ab}
=\frac{2|G_a-G_b|}{|G_a|+|G_b|}.
}
\]

On the positive sector,

\[
\delta_{M_G}^{ab}=0
\quad\Longleftrightarrow\quad
\delta_G^{ab}=0.
\]

A logarithmic universality coordinate is

\[
\boxed{
U_{ab}:=\ln\frac{G_a}{G_b}
=-2\ln\frac{\bar M_{G,a}}{\bar M_{G,b}}.
}
\]

These quantities are evaluated only after `beta_W`, `Gamma_DC`, `M_star` or their local replacements are frozen independently for each system.

## 8. Promotion boundary

The reduced-scale identity is exact algebra. Physical promotion of a universal `G` requires cross-system evidence that one and the same `Mbar_G` is obtained from independently frozen source sectors.

For the local phase-rate candidate, the decisive test is whether

\[
\frac{\beta_W\omega_Q}{\Gamma_{DC}}
\]

remains invariant across the admitted matter/source family. A failure localizes the rejected coordinate to the local `M_star=epsilon_Q` binding or to another independently testable normalization input.

## 9. Advancement

```text
Mbar_G = M_star/(Gamma_DC g_YM^2)              PASS EXACT DEFINITION
G_DC = 1/(8 pi Mbar_G^2)                       PASS EXACT
Wilson Mbar_G = beta_W M_star/(6 Gamma_DC)     PASS EXACT
local Mstar=omega_Q/2 specialization           CONDITIONAL CANDIDATE
local Mbar_G = beta_W omega_Q/(12 Gamma_DC)    PASS EXACT on candidate surface
G universality <-> Mbar_G universality         PASS EXACT
fixed beta_W,Gamma + varying omega             FAILS universal-G test
cross-system zero-fit universality test         DEFINED
physical universal-G promotion                  OPEN evidence gate
```
