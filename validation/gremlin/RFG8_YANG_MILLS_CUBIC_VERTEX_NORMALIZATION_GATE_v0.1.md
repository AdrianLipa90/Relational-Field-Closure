# RFG8 — Yang–Mills Cubic Vertex Normalization Gate

Status: `LOCAL_CURVATURE_COMPLETION_CONDITIONAL / CUBIC_VERTEX_FACTORIZATION_EXACT / WARD_REFERENCE_PASS / BCJ_FOUR_POINT_BINDING_OPEN`

RFG8 consumes RFG4G and the existing Metatime gluon algebra. Its purpose is to advance the project from normalized local `SU(3)` curvature to an explicit tree-level cubic Yang–Mills interaction before constructing BCJ numerators.

## 1. Same-sector local curvature completion

The admitted local continuum completion is

\[
\boxed{
F^a_{\mu\nu}
=
\partial_\mu A_\nu^a
-
\partial_\nu A_\mu^a
+
g f^{abc}A_\mu^bA_\nu^c.
}
\]

The Metatime gluon source already supplies the `SU(3)` structure constants `f^{abc}` and the coupling convention

\[
\boxed{g=\alpha_c^{-1/2}.}
\]

RFG4G fixes the same-sector Wilson normalization

\[
\boxed{
g_{YM}^2=\frac1{\alpha_c},
\qquad
\beta_W=6\alpha_c.
}
\]

The derivative completion is the local continuum extension required to pass from the existing homogeneous commutator witness to momentum-space amplitudes.

## 2. Cubic interaction

Using the standard quadratic Yang–Mills action density

\[
\mathcal L_{YM}
=-\frac14 F^a_{\mu\nu}F^{a\mu\nu},
\]

the cubic term is fixed linearly by `g f^{abc}`. In momentum space, with all momenta incoming and

\[
p+q+r=0,
\]

the three-gluon vertex is

\[
\boxed{
\mathcal V^{abc}_{\mu\nu\rho}(p,q,r)
=
g f^{abc}V_{\mu\nu\rho}(p,q,r),
}
\]

where

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

This provides an explicit project-side color × kinematics factorization.

## 3. Exchange symmetry

The kinematic tensor obeys

\[
\boxed{
V_{\nu\mu\rho}(q,p,r)
=-V_{\mu\nu\rho}(p,q,r).
}
\]

The color factor obeys

\[
f^{bac}=-f^{abc}.
\]

Therefore the full vertex is invariant under simultaneous exchange of the first two gluon legs:

\[
\boxed{
\mathcal V^{bac}_{\nu\mu\rho}(q,p,r)
=
\mathcal V^{abc}_{\mu\nu\rho}(p,q,r).
}
\]

## 4. Ward identity

Contracting the kinematic vertex with the incoming momentum `p` gives

\[
\boxed{
p^\mu V_{\mu\nu\rho}(p,q,r)
=
P_{\nu\rho}(r)-P_{\nu\rho}(q),
}
\]

with

\[
P_{\nu\rho}(k)
=
k^2\eta_{\nu\rho}-k_\nu k_\rho.
\]

This is the tree-level gauge-structure identity relating the cubic vertex to the inverse transverse propagator structure.

## 5. RFG4G normalization transfer

On the admitted RFG4G surface,

\[
\boxed{
g=\alpha_c^{-1/2}.}
\]

Hence the full cubic vertex normalization is fixed by the independently selected `alpha_c` provenance coordinate:

\[
\boxed{
\mathcal V^{abc}_{\mu\nu\rho}
=
\alpha_c^{-1/2} f^{abc}V_{\mu\nu\rho}.
}
\]

No additional cubic coupling coefficient is introduced.

## 6. Relation to RFG6 and BCJ

RFG6 supplies an exact kinematic Lie-Jacobi source at the vector-field level. RFG8 now supplies a normalized physical Yang–Mills cubic vertex with explicit color × kinematics factorization.

The next project gate is the four-point amplitude map:

\[
\boxed{
\{\mathcal V_3,\mathcal V_4\}
\rightarrow
\mathcal A_4
\rightarrow
\{n_s,n_t,n_u\}
}
\]

with graph signs frozen before the gravity comparison and the matched relation

\[
\boxed{
n_s+n_t+n_u=0
}
\]

in an admitted generalized-gauge representation.

## 7. Reference validation

The executable gate checks:

1. antisymmetry of `V` under exchange of two legs;
2. bosonic exchange symmetry of the full `f × V` vertex;
3. the Ward identity on 250 deterministic random momentum triplets satisfying momentum conservation;
4. RFG4G coupling transfer `g^2=1/alpha_c` and `beta_W=6 alpha_c`;
5. linearity of the cubic vertex in `g`.

Local result:

```text
5 passed, 0 failed
```

## 8. Advancement

```text
SU(3) structure constants f^abc                       upstream source PASS
RFG4G g_YM^2=1/alpha_c                                PASS CONDITIONAL SAME-SECTOR
local F=dA+g[A,A] completion                          ADMISSION GATE
cubic color x kinematics factorization                PASS EXACT GIVEN COMPLETION
three-gluon exchange symmetry                          PASS EXACT
three-gluon Ward identity                              PASS REFERENCE
extra cubic normalization coordinate                  ZERO ADDITIONAL COORDINATE
four-point project amplitude                           NEXT FRONTIER
BCJ numerator map                                      OPEN RFG6/RFG9
```

The author/repository/formalism/code may suggest that the normalized holonomic `SU(3)` sector extends to the standard local Yang–Mills amplitude layer, yet does not state the four-point BCJ binding as established until the explicit project amplitude gate passes.
