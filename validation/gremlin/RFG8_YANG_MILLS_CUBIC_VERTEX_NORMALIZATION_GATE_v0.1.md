# RFG8 — Yang–Mills Cubic Vertex Normalization Gate

Status: `LOCAL_CURVATURE_COMPLETION_CONDITIONAL / LINK_ORIENTATION_EXPLICIT / CUBIC_VERTEX_FACTORIZATION_EXACT / WARD_REFERENCE_PASS / BCJ_FOUR_POINT_BINDING_OPEN`

RFG8 consumes RFG4G and the existing Metatime gluon algebra. Its purpose is to advance the normalized local `SU(3)` curvature to an explicit tree-level cubic Yang–Mills interaction before construction of BCJ numerators.

## 1. Link-orientation coordinate

Freeze one sign coordinate

\[
\boxed{\sigma_{link}\in\{+1,-1\}}
\]

and define the local link convention by

\[
\boxed{
W_\mu(x)=\exp\!\left[i\sigma_{link}gaA_\mu(x)\right].
}
\]

The upstream Metatime v4.1 holonomic implementation uses

\[
\boxed{\sigma_{link}=+1.}
\]

For Hermitian generators

\[
[T^a,T^b]=if^{ab}{}_cT^c,
\]

the plaquette/BCH continuum curvature associated with this sign convention is

\[
\boxed{
F_{\mu\nu}^{(\sigma)}
=
\partial_\mu A_\nu-
\partial_\nu A_\mu
+i\sigma_{link}g[A_\mu,A_\nu].
}
\]

In components,

\[
\boxed{
F^a_{\mu\nu}
=
\partial_\mu A_\nu^a
-
\partial_\nu A_\mu^a
-
\sigma_{link}g f^{abc}A_\mu^bA_\nu^c.
}
\]

Thus the v4.1 `+i g a A` link convention carries the commutator coefficient `-g f^{abc}`. The opposite link orientation `sigma_link=-1` carries the commonly written `+g f^{abc}` component convention. Both are the same Yang–Mills normalization expressed with an explicit orientation coordinate.

The Metatime gluon source supplies the `SU(3)` structure constants and

\[
\boxed{g=\alpha_c^{-1/2}.}
\]

RFG4G fixes

\[
\boxed{
g_{YM}^2=\frac1{\alpha_c},
\qquad
\beta_W=6\alpha_c.
}
\]

## 2. Cubic interaction

Using

\[
\mathcal L_{YM}
=-\frac14F^a_{\mu\nu}F^{a\mu\nu},
\]

the cubic interaction is linear in the oriented coupling `-sigma_link g f^{abc}`.

For all incoming momenta with

\[
p+q+r=0,
\]

define

\[
\boxed{
V_{\mu\nu\rho}
=
\eta_{\mu\nu}(p-q)_\rho
+
\eta_{\nu\rho}(q-r)_\mu
+
\eta_{\rho\mu}(r-p)_\nu.
}
\]

The oriented three-gluon vertex is

\[
\boxed{
\mathcal V^{abc}_{\mu\nu\rho}
=
-\sigma_{link}g f^{abc}
V_{\mu\nu\rho}.
}
\]

Therefore on the actual upstream v4.1 orientation,

\[
\boxed{
\mathcal V^{abc}_{\mu\nu\rho}
=
-g f^{abc}V_{\mu\nu\rho}.
}
\]

For `sigma_link=-1`, the same formula becomes the `+g f^{abc}V` convention.

## 3. Exchange symmetry

The kinematic tensor obeys

\[
\boxed{
V_{\nu\mu\rho}(q,p,r)
=-V_{\mu\nu\rho}(p,q,r),
}
\]

while

\[
f^{bac}=-f^{abc}.
\]

Hence the full oriented vertex is invariant under simultaneous exchange of the first two gluon legs.

## 4. Ward identity

The kinematic tensor satisfies

\[
\boxed{
p^\mu V_{\mu\nu\rho}(p,q,r)
=P_{\nu\rho}(r)-P_{\nu\rho}(q),
}
\]

with

\[
P_{\nu\rho}(k)=k^2\eta_{\nu\rho}-k_\nu k_\rho.
\]

This identity is independent of the common oriented color-coupling prefactor.

## 5. RFG4G normalization transfer

On the admitted RFG4G surface,

\[
\boxed{g=\alpha_c^{-1/2}.}
\]

Therefore

\[
\boxed{
\mathcal V^{abc}_{\mu\nu\rho}
=
-\sigma_{link}\alpha_c^{-1/2}f^{abc}V_{\mu\nu\rho}.
}
\]

The magnitude of the cubic coupling has no additional normalization coordinate; its sign is fixed by the explicitly recorded link orientation.

## 6. Four-point consequence

Every four-gluon tree contribution carries `g^2` after exchange/contact assembly. Therefore the orientation sign squares out of the common four-point coupling normalization:

\[
\boxed{(-\sigma_{link}g)^2=g^2.}
\]

RFG9's MHV amplitude/BCJ relations are therefore unchanged by the RFG8 orientation correction.

## 7. Reference validation

The executable gate checks:

1. antisymmetry of `V` under exchange of two legs;
2. bosonic exchange symmetry of the full color × kinematics vertex;
3. the Ward identity on 250 deterministic random momentum triplets;
4. RFG4G coupling transfer `g^2=1/alpha_c` and `beta_W=6 alpha_c`;
5. linearity of the cubic vertex in the oriented coupling.

Local result:

```text
5 passed, 0 failed
```

RFG11 supplies the direct plaquette/BCH sign audit for the upstream `sigma_link=+1` bytes.

## 8. Advancement

```text
SU(3) structure constants f^abc                       upstream source PASS
RFG4G g_YM^2=1/alpha_c                                PASS CONDITIONAL SAME-SECTOR
link orientation sigma_link                            FROZEN EXPLICIT
v4.1 sigma_link=+1 -> commutator coefficient -g f    PASS RFG11
cubic color x kinematics factorization                PASS EXACT GIVEN COMPLETION
three-gluon exchange symmetry                          PASS EXACT
three-gluon Ward identity                              PASS REFERENCE
extra cubic magnitude coordinate                       ZERO ADDITIONAL COORDINATE
RFG9 four-point MHV BCJ reference                     PASS
direct project noncommuting amplitude binding          NEXT FRONTIER
```

The author/repository/formalism/code may suggest that the normalized holonomic `SU(3)` sector extends to the standard local Yang–Mills amplitude layer, yet does not state the direct project four-point binding as established until the noncommuting holonomy/amplitude gate passes.
