# RF-L4A — Shannon–Fisher Local Canonical Normalization

Status: `SHANNON_HESSIAN_EXACT / LOCAL_FISHER_RADIAL_REDUCTION_PASS / BETA_I_SQRT2_LOCAL_PASS / AREA_VARIATION_QUADRATIC_INVARIANCE_PASS / GLOBAL_INFORMATION_GEODESIC_EXTENSION_OPEN`

RF-L4A consumes RF-L4 together with the IDT 01C Shannon relative-information scalar and the 01K inverse-area curvature export. Its purpose is to fix the RF-L4 dimensionless field normalization `beta_I` in the local stationary-reference sector from the intrinsic quadratic geometry of relative information.

## 1. Natural-log Shannon information near the stationary reference

IDT 01C defines the bit-valued relative information

\[
\mathcal I_\pi[p]=D_{KL}^{(2)}(p\|\pi).
\]

IDT 01K uses the natural-log scalar

\[
\boxed{
\mathcal J_\pi[p]
=(\ln2)\mathcal I_\pi[p]
=\sum_a p_a\ln\frac{p_a}{\pi_a}.
}
\]

Let

\[
p_a=\pi_a+\delta p_a,
\qquad
\sum_a\delta p_a=0,
\qquad
\pi_a>0.
\]

At the stationary reference `p=pi`,

\[
\mathcal J_\pi[\pi]=0.
\]

The first variation on the simplex tangent space vanishes because

\[
\delta\mathcal J_\pi
=\sum_a\delta p_a=0.
\]

The Hessian is

\[
\boxed{
H_{ab}^{F}(\pi)
=\left.\frac{\partial^2\mathcal J_\pi}{\partial p_a\partial p_b}\right|_{p=\pi}
=\frac{\delta_{ab}}{\pi_a}.
}
\]

This is the local Fisher information metric on the probability-simplex tangent space.

## 2. Exact quadratic expansion coefficient

Taylor expansion around the stationary reference gives

\[
\boxed{
\mathcal J_\pi[\pi+\delta p]
=\frac12\sum_a\frac{(\delta p_a)^2}{\pi_a}
+O(\|\delta p\|^3).
}
\]

Define the local Fisher radial norm

\[
\boxed{
s_F^2
:=\sum_a\frac{(\delta p_a)^2}{\pi_a}.
}
\]

Then

\[
\boxed{
\mathcal J_\pi
=\frac12s_F^2+O(\|\delta p\|^3).
}
\]

The factor `1/2` is fixed by the exact Hessian of the admitted Shannon-relative-information scalar.

## 3. Division by the relational area

IDT 01K defines

\[
\Xi_I=\frac{\mathcal J_\pi}{\mathcal A_{rel}}.
\]

Let the stationary-reference area be

\[
\mathcal A_\star>0
\]

and allow a smooth local variation

\[
\mathcal A_{rel}
=\mathcal A_\star+O(\|\delta p\|).
\]

Since `J_pi=O(||delta p||^2)`, the area variation contributes first at cubic order. Therefore

\[
\boxed{
\Xi_I
=\frac{s_F^2}{2\mathcal A_\star}
+O(\|\delta p\|^3).
}
\]

Thus the quadratic canonical normalization depends on the stationary-reference area `A_star`, while smooth first-order area motion leaves the quadratic coefficient unchanged.

## 4. Fisher radial scalar coordinate

Define the inverse-length local Fisher radial field

\[
\boxed{
\phi_F
:=\frac{s_F}{\sqrt{\mathcal A_\star}}.
}
\]

Then

\[
[\phi_F]=L^{-1}
\]

and

\[
\boxed{
\Xi_I
=\frac12\phi_F^2
+O(\|\delta p\|^3).
}
\]

RF-L4 uses, in the zero-baseline stationary-reference sector,

\[
\phi_I=\beta_I\sqrt{\Xi_I}.
\]

Matching the leading Fisher radial coordinate gives

\[
\boxed{\beta_I=\sqrt2.}
\]

Therefore the RF-L4 canonical field is locally

\[
\boxed{
\phi_I
=\sqrt{2\Xi_I}
=\phi_F+O(\|\delta p\|^2).
}
\]

This fixes the RF-L4 field normalization in the local Shannon–Fisher sector.

## 5. RF-L4 kinetic coefficient after Fisher normalization

RF-L4 derived

\[
Z_I^{RFC}(\Xi_I)
=\frac{\beta_I^2}{4\Xi_I}
\]

in the zero-baseline positive chart. With `beta_I^2=2`,

\[
\boxed{
Z_I^{RFC}(\Xi_I)
=\frac{1}{2\Xi_I}.
}
\]

Equivalently,

\[
\boxed{
d\phi_I^2
=\frac{d\Xi_I^2}{2\Xi_I}.
}
\]

This is the radial information-curvature metric required by the locally Fisher-normalized canonical scalar chart.

## 6. Quadratic potential and mass relation

RF-L4 gives

\[
U_I(\phi_I)
=\frac{\alpha_I}{\kappa_E\beta_I^2}\phi_I^2.
\]

With `beta_I^2=2`,

\[
\boxed{
U_I(\phi_I)
=\frac{\alpha_I}{2\kappa_E}\phi_I^2.
}
\]

Comparing with

\[
U_I=\frac12m_I^2\phi_I^2
\]

gives

\[
\boxed{
m_I^2=\frac{\alpha_I}{\kappa_E}}
\]

and

\[
\boxed{
\alpha_I=\kappa_Em_I^2.
}
\]

Thus the local Fisher normalization removes `beta_I` from the remaining coupling calibration problem.

## 7. Bianchi transfer after Fisher normalization

The exact RF-L3 transfer is

\[
\nabla_\nu\Lambda_0
=\alpha_I\nabla_\nu\Xi_I.
\]

With

\[
\Xi_I=\frac12\phi_I^2
\]

in the RF-L4A canonical coordinate convention,

\[
\boxed{
\nabla_\nu\Lambda_0
=\alpha_I\phi_I\nabla_\nu\phi_I
=\kappa_E m_I^2\phi_I\nabla_\nu\phi_I.
}
\]

The same local normalization therefore closes the potential, mass and transfer coefficients with one scalar parameter `m_I` or equivalently `alpha_I`.

## 8. Full-Bloch-sphere IDT specialization

IDT 01K gives

\[
\Xi_I^{(S^2)}
=24\kappa\mathcal I_\pi
\left(\frac{\omega}{c}\right)^2,
\qquad
\kappa=\frac{\ln2}{24\pi}.
\]

Using `beta_I=sqrt(2)`,

\[
\boxed{
\phi_I^{(S^2)}
=\sqrt{48\kappa\mathcal I_\pi}\,
\frac{|\omega|}{c}.
}
\]

This is the locally Fisher-normalized Shannon-information × phase-clock scalar coordinate for the admitted constant-rate full-sphere sector.

## 9. Relation to the IDT 01D Onsager operator

RF-L4A fixes the local scalar-coordinate normalization from the Hessian geometry of `J_pi`. IDT 01D independently supplies the dynamical Onsager response operator

\[
G_\pi^{(2)}(p).
\]

The next dynamical closure gate is to project the 01D response along a Fisher-radial / admitted 01K trajectory and compare its relaxation operator with the RF-L2/RF-L4A Lorentzian scalar dynamics.

This separates two already typed structures:

```text
local information geometry / field normalization      beta_I = sqrt(2)  PASS LOCAL
Onsager response / temporal relaxation                IDT 01D            ADMITTED
Lorentzian scalar propagation                         RF-L2              ADMITTED
response-to-propagation dynamical bridge              OPEN
alpha_I <-> m_I physical scale                        OPEN
```

## 10. Evidence status

```text
Hessian of J_pi at p=pi                               PASS EXACT
Fisher tangent metric diag(1/pi_a)                    PASS EXACT
J_pi = (1/2) s_F^2 + O(delta p^3)                    PASS LOCAL EXPANSION
Xi_I = s_F^2/(2 A_star) + O(delta p^3)                PASS LOCAL EXPANSION
smooth first-order A_rel variation                     QUADRATIC COEFFICIENT PRESERVED
beta_I = sqrt(2)                                      PASS LOCAL FISHER MATCH
Z_I^RFC = 1/(2 Xi_I)                                  PASS GIVEN RF-L4
m_I^2 = alpha_I/kappa_E                               PASS GIVEN RF-L4
full-sphere phi_I coefficient                          PASS GIVEN IDT 01K
global finite-distance KL/Fisher extension             OPEN
Onsager-to-Lorentzian dynamical bridge                 OPEN
alpha_I / m_I physical calibration                     OPEN
```
