# RFG9 — Four-Gluon MHV BCJ Amplitude Gate

Status: `FOUR_POINT_MHV_REFERENCE_PASS / BCJ_AMPLITUDE_RELATION_PASS / MATCHED_JACOBI_NUMERATOR_WITNESS_PASS / DIRECT_HOLONOMIC_AMPLITUDE_BINDING_OPEN`

RFG9 consumes RFG8 and RFG6. Its purpose is to advance the normalized local Yang–Mills sector from the cubic color × kinematics vertex to an explicit four-gluon amplitude-level BCJ witness.

Scope is the tree-level four-gluon MHV sector. This supplies a controlled amplitude reference surface for the project-side holonomic binding.

## 1. RFG8 coupling normalization

RFG8 supplies

\[
\boxed{g^2=\frac1{\alpha_c}}
\]

on the admitted RFG4G same-sector surface, together with the normalized three-gluon vertex.

At four points, the tree amplitude therefore carries the expected overall factor `g^2`.

## 2. MHV color-ordered amplitude

For negative-helicity legs `1,2` and positive-helicity legs `3,4`, use the standard tree-level Parke–Taylor reference amplitude

\[
\boxed{
A(1^-,2^-,3^+,4^+)
=
i g^2
\frac{\langle12\rangle^4}
{\langle12\rangle\langle23\rangle\langle34\rangle\langle41\rangle}.
}
\]

For the ordering `(1,3,2,4)`,

\[
\boxed{
A(1^-,3^+,2^-,4^+)
=
i g^2
\frac{\langle12\rangle^4}
{\langle13\rangle\langle32\rangle\langle24\rangle\langle41\rangle}.
}
\]

The reference generator constructs rank-one massless momenta

\[
p_i=\lambda_i\tilde\lambda_i
\]

with exact numerical momentum conservation

\[
\sum_i p_i=0.
\]

## 3. Four-point BCJ amplitude relation

With

\[
s_{ij}=\langle ij\rangle[ji],
\]

the four-point MHV amplitudes obey

\[
\boxed{
s_{12}A(1,2,3,4)
=
s_{13}A(1,3,2,4).
}
\]

This is the four-point fundamental BCJ amplitude relation on the admitted reference sector.

## 4. Explicit matched-Jacobi numerator witness

Choose a four-point generalized-gauge representative

\[
\boxed{
n_t=0.}
\]

Define

\[
\boxed{
n_s=s_{12}A(1,2,3,4),}
\]

and

\[
\boxed{
n_u=-n_s.}
\]

Then the kinematic Jacobi relation is exact:

\[
\boxed{
n_s+n_t+n_u=0.}
\]

The second independent ordering is reconstructed as

\[
\boxed{
A(1,3,2,4)
=-\frac{n_u}{s_{13}}
=\frac{n_s}{s_{13}},
}
\]

which is equivalent to the BCJ amplitude relation above.

Thus RFG9 supplies an explicit four-point numerator witness satisfying the same Jacobi pattern as the color factors on this MHV reference surface.

## 5. Coupling scaling

Because

\[
A_4\propto g^2,
\]

the numerator witness scales as

\[
\boxed{n_i\propto g^2.}
\]

On RFG4G/RFG8,

\[
\boxed{n_i\propto\alpha_c^{-1}.}
\]

The BCJ relation itself is homogeneous in this common factor, so no additional amplitude-normalization coordinate is introduced at four points.

## 6. Reference validation

The executable gate generates deterministic random complex spinor-helicity kinematics satisfying momentum conservation and checks:

1. massless rank-one momentum matrices and total momentum conservation on 100 points;
2. the four-point BCJ amplitude relation on 250 points;
3. Mandelstam closure `s12+s13+s14=0` on 100 points;
4. explicit `n_s+n_t+n_u=0` numerator reconstruction and recovery of the second ordering on 200 points;
5. the RFG8 `g^2` scaling of both amplitudes and numerators.

Local result:

```text
5 passed, 0 failed
```

No gravity output is used to select the numerator representation or kinematics.

## 7. Project-side binding frontier

RFG9 establishes the amplitude-level BCJ reference surface. The next project gate binds the holonomic local transport data to the amplitude coordinates before double copy:

\[
\boxed{
W_{ij}
\rightarrow
A_\mu^a
\rightarrow
\mathcal V_3,\mathcal V_4
\rightarrow
A_4^{project}
\rightarrow
(n_s,n_t,n_u).
}
\]

The required comparison is

\[
\boxed{
\Delta_{amp}
=\|A_4^{project}-A_4^{YM}\|,
}
\]

with graph/order/helicity conventions frozen before the comparison.

## 8. Advancement

```text
RFG8 normalized cubic vertex                         inherited PASS
four-point massless momentum-conserving kinematics   PASS REFERENCE
four-point MHV BCJ amplitude relation                PASS REFERENCE
explicit n_s+n_t+n_u=0 witness                       PASS REFERENCE
second ordering reconstruction                       PASS REFERENCE
RFG8 g^2 normalization propagation                   PASS EXACT
project holonomy -> four-point amplitude bytes       NEXT BINDING FRONTIER
full-helicity / higher-point BCJ extension            OPEN LATER GATE
double-copy gravity amplitude with project numerators OPEN AFTER PROJECT BINDING
```

The author/repository/formalism/code may suggest the holonomic Yang–Mills sector can inherit the four-point BCJ representation after the same-field amplitude binding, yet does not state that project binding as established until the direct amplitude defect is evaluated.
