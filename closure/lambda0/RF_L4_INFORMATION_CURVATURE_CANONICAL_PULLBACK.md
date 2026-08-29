# RF-L4 — Information-Curvature Canonical Pullback Gate

Status: `EXACT_SQRT_COORDINATE_PULLBACK / BASELINE_SHIFT_EXACT / QUADRATIC_POTENTIAL_CONSEQUENCE / KINETIC_JACOBIAN_EXACT / IDT_KINETIC_METRIC_MATCH_OPEN`

RF-L4 consumes RF-L3 together with the IDT 01K information-curvature scalar

\[
\Xi_I=\frac{\mathcal J_\pi}{\mathcal A_{\rm rel}},
\qquad [\Xi_I]=L^{-2}.
\]

The gate resolves the scalar-coordinate interface between the RF-L2 canonical action coordinate and the RF-L3 information-curvature potential by introducing an explicit baseline and field-coordinate Jacobian.

## 1. Baseline-resolved information curvature

Let an admitted reference state carry a constant information-curvature value

\[
\Xi_\star,
\qquad [\Xi_\star]=L^{-2}.
\]

On an admitted branch with

\[
\boxed{\bar\Xi_I:=\Xi_I-\Xi_\star\ge0,}
\]

define the baseline-resolved dynamic coordinate `bar(Xi)_I`.

RF-L3 gives

\[
\Lambda_0=\Lambda_{ref}+\alpha_I\Xi_I.
\]

Define

\[
\boxed{\Lambda_\star:=\Lambda_{ref}+\alpha_I\Xi_\star.}
\]

Then exactly

\[
\boxed{\Lambda_0=\Lambda_\star+\alpha_I\bar\Xi_I.}
\]

Thus the constant information-curvature background is absorbed into the constant Einstein-side reference coordinate while the dynamical displacement remains explicit.

## 2. Canonical-dimension square-root coordinate

In four-dimensional natural units, a canonical real scalar entering

\[
-\frac12\nabla_\mu\phi\nabla^\mu\phi
\]

has field dimension

\[
[\phi]=L^{-1}.
\]

Since `[bar(Xi)_I]=L^-2`, introduce

\[
\boxed{\phi_I:=\beta_I\sqrt{\bar\Xi_I},}
\qquad
\beta_I>0,
\qquad
[\beta_I]=1.
\]

Therefore

\[
\boxed{[\phi_I]=L^{-1}}
\]

and the inverse map is

\[
\boxed{\bar\Xi_I=\frac{\phi_I^2}{\beta_I^2}.}
\]

`beta_I` is the dimensionless field-coordinate normalization carried explicitly by this gate.

## 3. RF-L3 potential becomes quadratic

Substituting the inverse map into the RF-L3 displacement gives

\[
\boxed{
\Lambda_0
=\Lambda_\star
+\frac{\alpha_I}{\beta_I^2}\phi_I^2.
}
\]

RF-L2 requires

\[
\Lambda_0=\Lambda_\star+\kappa_EU_I(\phi_I).
\]

Hence

\[
\boxed{
U_I(\phi_I)
=\frac{\alpha_I}{\kappa_E\beta_I^2}\phi_I^2.
}
\]

Writing the canonical quadratic form as

\[
U_I(\phi_I)=\frac12m_I^2\phi_I^2,
\]

gives the exact parameter relation

\[
\boxed{
m_I^2
=\frac{2\alpha_I}{\kappa_E\beta_I^2}
}
\]

and equivalently

\[
\boxed{
\alpha_I
=\frac12\kappa_E\beta_I^2m_I^2.
}
\]

RF-L4 therefore converts the RF-L3 coupling-calibration coordinate into an equivalent mass/field-normalization calibration coordinate.

## 4. Kinetic Jacobian in the information-curvature chart

For `bar(Xi)_I>0`,

\[
\nabla_\mu\phi_I
=\frac{\beta_I}{2\sqrt{\bar\Xi_I}}\nabla_\mu\Xi_I.
\]

Therefore the canonical kinetic term pulls back exactly to

\[
-\frac12(\nabla\phi_I)^2
=-\frac12Z_I(\Xi_I)(\nabla\Xi_I)^2,
\]

with

\[
\boxed{
Z_I(\Xi_I)
=\frac{\beta_I^2}{4(\Xi_I-\Xi_\star)}.
}
\]

This is the field-space metric coefficient induced by the RF-L4 square-root coordinate on the positive dynamic branch.

At `Xi_I=Xi_star`, the regular coordinate is `phi_I=0`; the `Xi_I` chart reaches its boundary there.

## 5. Scalar equation and local stability

The RF-L2 scalar equation becomes

\[
\boxed{
(\Box-m_I^2)\phi_I=0
}
\]

for the RF-L4 quadratic information-curvature sector.

The RF-L2 local stability condition is

\[
m_I^2\ge0.
\]

Using the exact RF-L4 relation,

\[
\boxed{
\frac{\alpha_I}{\kappa_E}\ge0
}
\]

for positive `beta_I^2`. In the admitted positive-`G` Einstein sector, `kappa_E>0`, so the stable quadratic branch corresponds to

\[
\boxed{\alpha_I\ge0.}
\]

The marginal surface `alpha_I=0` gives `m_I^2=0`.

## 6. Bianchi transfer in the canonical coordinate

RF-L3 gives

\[
\nabla_\nu\Lambda_0
=\alpha_I\nabla_\nu\Xi_I.
\]

Since

\[
\Xi_I=\Xi_\star+\frac{\phi_I^2}{\beta_I^2},
\]

one has

\[
\boxed{
\nabla_\nu\Lambda_0
=\frac{2\alpha_I}{\beta_I^2}\phi_I\nabla_\nu\phi_I
=\kappa_E m_I^2\phi_I\nabla_\nu\phi_I.
}
\]

Therefore the RF-L2 transfer remains

\[
\boxed{
\kappa_E\nabla^\mu T^{displayed}_{\mu\nu}
=\kappa_Em_I^2\phi_I\nabla_\nu\phi_I.
}
\]

The information-curvature and canonical-scalar charts carry the same transfer covector.

## 7. Direct IDT 01K specialization

For the IDT constant-rate cell sector,

\[
\Xi_I
=\frac{\mathcal J_\pi}{a_{FS}}
\left(\frac{\omega}{c}\right)^2.
\]

On the zero-baseline specialization `Xi_star=0`, RF-L4 gives

\[
\boxed{
\phi_I
=\beta_I
\sqrt{\frac{\mathcal J_\pi}{a_{FS}}}
\frac{|\omega|}{c}.
}
\]

For the full CP1/Bloch sphere, IDT 01K gives

\[
\Xi_I
=24\kappa\,\mathcal I_\pi
\left(\frac{\omega}{c}\right)^2,
\qquad
\kappa=\frac{\ln2}{24\pi}.
\]

Hence

\[
\boxed{
\phi_I^{(S^2)}
=\beta_I\sqrt{24\kappa\,\mathcal I_\pi}\,
\frac{|\omega|}{c}.
}
\]

This is an explicit Shannon-information × phase-clock representation of the RF-L4 scalar coordinate in the admitted IDT constant-rate full-sphere sector.

## 8. Shannon–Onsager kinetic-metric comparison target

IDT 01D supplies the positive tangent-space Shannon–Onsager response metric on the probability simplex. RF-L4 supplies the one-dimensional information-curvature metric required by the canonical scalar chart:

\[
\boxed{
Z_I^{RFC}(\Xi_I)
=\frac{\beta_I^2}{4(\Xi_I-\Xi_\star)}.
}
\]

The next promotion gate is the explicit reduction of the IDT 01D tangent metric along the admitted 01K information-curvature trajectory and comparison with `Z_I^RFC`.

The comparison target is

\[
\boxed{
Z_I^{IDT}(\Xi_I)
\stackrel{gate}{=}
Z_I^{RFC}(\Xi_I).
}
\]

A successful metric match fixes the physical field-coordinate normalization `beta_I` from the upstream information dynamics and upgrades the pullback from dimensional/coordinate closure to kinetic closure.

## 9. Executable reference gates

RF-L4 tests verify:

1. baseline shift `Xi_I -> bar(Xi)_I` and `Lambda_ref -> Lambda_star` roundtrip;
2. square-root coordinate and inverse map;
3. canonical field dimension represented by the inverse-length coordinate;
4. exact quadratic potential reconstruction;
5. exact `m_I^2 <-> alpha_I` relation;
6. kinetic Jacobian `Z_I=beta_I^2/[4(Xi_I-Xi_star)]`;
7. Bianchi-transfer equality in both coordinate charts;
8. full-Bloch-sphere IDT specialization with canonical `kappa=ln(2)/(24pi)`;
9. negative dynamic curvature and invalid normalization fail closed;
10. the baseline boundary is represented through the regular `phi_I=0` chart.

## 10. Advancement

```text
RF-L3 information-curvature potential                 ADMITTED
constant Xi_star background -> Lambda_star             PASS EXACT
barXi_I = Xi_I - Xi_star                               PASS EXACT
phi_I = beta_I sqrt(barXi_I)                           PASS EXACT ON ADMITTED BRANCH
canonical L^-1 scalar dimension                        PASS IN 4D NATURAL UNITS
U_I(phi_I) quadratic                                   PASS EXACT
m_I^2 = 2 alpha_I/(kappa_E beta_I^2)                  PASS EXACT
kinetic Jacobian in Xi chart                           PASS EXACT
Bianchi transfer coordinate equivalence                PASS EXACT
IDT 01K constant-cell/full-sphere scalar export        PASS EXACT GIVEN 01K
IDT 01D -> RF-L4 kinetic metric equality               OPEN
physical beta_I normalization                          OPEN
alpha_I / m_I physical calibration                     OPEN
```
