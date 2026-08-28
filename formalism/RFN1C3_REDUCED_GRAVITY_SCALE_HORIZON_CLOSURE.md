# RF-N1C3 — Reduced Gravity Scale: Double-Copy ↔ Horizon Thermal Closure

Status: `EXACT_G_FREE_SCALE_REDUCTION / HORIZON_THERMAL_SCALE_EQUIVALENCE / THREE_ESTIMATOR_CLOSURE_DEFINED / PHYSICAL_HORIZON_INPUT_GATE_OPEN`

RF-N1C3 consumes RF-N1C2 and the existing RFG5 horizon/double-copy cross-check. It rewrites the RFG5 invariant directly in terms of the reduced gravity-scale coordinate `Mbar_G`, eliminating the Newton constant from the cross-route comparison.

## 1. Reduced gravity scale

RF-N1C2 defines

\[
\boxed{
\bar M_G
:=\frac{M_\star}{\Gamma_{DC}g_{YM}^2},
\qquad
G_{DC}=\frac{1}{8\pi\bar M_G^2}
}
\]

in natural units.

## 2. RFG5 invariant

RFG5 supplies the G-free double-copy/horizon relation

\[
\boxed{
\Gamma_{DC}^2g_{YM}^4M_H\kappa_H
=2\pi M_\star^2.
}
\]

Divide by `Gamma_DC^2 g_YM^4`. Then

\[
\boxed{
M_H\kappa_H
=2\pi\frac{M_\star^2}{\Gamma_{DC}^2g_{YM}^4}
=2\pi\bar M_G^2.
}
\]

Therefore

\[
\boxed{
\bar M_G^2
=\frac{M_H\kappa_H}{2\pi}.
}
\]

This is the reduced-gravity-scale horizon closure.

## 3. Hawking thermal form

RF-E1 gives

\[
\kappa_H=2\pi T_H
\]

in natural units. Hence

\[
\boxed{
\bar M_G^2=M_HT_H
}
\]

and therefore

\[
\boxed{
\bar M_G=\sqrt{M_HT_H}
}
\]

on the positive horizon sector.

The horizon route can therefore estimate the same reduced gravity scale without inserting a numerical value of `G`.

## 4. Wilson / local carrier forms

RFG3 and RF-N1C2 give

\[
\boxed{
\bar M_G
=\frac{\beta_WM_\star}{6\Gamma_{DC}}.
}
\]

On the local phase-carrier scale candidate

\[
M_\star=\frac12\omega_Q,
\]

this becomes

\[
\boxed{
\bar M_G^{local}
=\frac{\beta_W\omega_Q}{12\Gamma_{DC}}.
}
\]

Thus the three estimator coordinates are

\[
\boxed{
\bar M_G^{DC}
=\frac{M_\star}{\Gamma_{DC}g_{YM}^2},
}
\]

\[
\boxed{
\bar M_G^{H}
=\sqrt{\frac{M_H\kappa_H}{2\pi}},
}
\]

\[
\boxed{
\bar M_G^{T}
=\sqrt{M_HT_H}.
}
\]

On the local carrier candidate a fourth representation is

\[
\boxed{
\bar M_G^{local}
=\frac{\beta_W\omega_Q}{12\Gamma_{DC}}.
}
\]

## 5. Three-estimator closure

The physical cross-route gate is

\[
\boxed{
\bar M_G^{DC}
=\bar M_G^{H}
=\bar M_G^{T}.
}
\]

When the local carrier-scale candidate is included,

\[
\boxed{
\frac{\beta_W\omega_Q}{12\Gamma_{DC}}
=\sqrt{M_HT_H}.
}
\]

Equivalently,

\[
\boxed{
\beta_W^2\omega_Q^2
=144\Gamma_{DC}^2M_HT_H,
}
\]

which is exactly the RFG5 Hawking-temperature invariant.

RF-N1C3 therefore shows that the RFG5 relation is the equality of two independently typed estimators of one reduced gravity scale.

## 6. Universality use

RF-N1C2 requires source-independence of `Mbar_G` for universal `G`. RF-N1C3 supplies an independent horizon estimator for the same coordinate.

For any admitted source system `a` and horizon system `H`, define

\[
\boxed{
\delta_{DH}
=\frac{2|\bar M_G^{DC}-\bar M_G^H|}
{|\bar M_G^{DC}|+|\bar M_G^H|}
}
\]

and

\[
\boxed{
\delta_{HT}
=\frac{2|\bar M_G^H-\bar M_G^T|}
{|\bar M_G^H|+|\bar M_G^T|}.
}
\]

The second defect tests the Euclidean/Hawking conversion on the same horizon data; the first compares the gauge/double-copy scale with the horizon geometry/thermal scale.

## 7. Circularity firewall

The horizon estimator is used as an independent cross-check only when `M_H`, `kappa_H` or `T_H` carry provenance that is logically independent of the candidate double-copy value of `G`.

The reduced-scale algebra itself is exact. Physical cross-route promotion requires an explicit provenance graph for every estimator.

## 8. Advancement

```text
RFG5 G-free invariant                              PASS inherited
Mbar_G^2 = M_H kappa_H/(2 pi)                    PASS EXACT REDUCTION
Mbar_G^2 = M_H T_H                               PASS EXACT via RF-E1
DC estimator = horizon estimator                 ZERO-FIT TEST DEFINED
local carrier estimator = horizon estimator      CONDITIONAL TEST DEFINED
cross-system Mbar_G universality                  strengthened by independent estimator
physical horizon provenance                      OPEN evidence gate
```
