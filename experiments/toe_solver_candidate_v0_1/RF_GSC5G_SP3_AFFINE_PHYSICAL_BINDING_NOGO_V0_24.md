# RF-GSC5G — SP3 Affine Physical-Spacetime Binding No-Go v0.24

Status: CANDIDATE_ONLY / FEATURE_R4_NEQ_PHYSICAL_SPACETIME_R4 / AFFINE_BINDING_REFUTED / NONLINEAR_OR_FIBERED_PHYSICAL_BINDING_REQUIRED / CANON_ALLOWED_FALSE

Date: 2026-09-20

## 1. Purpose

V0.13 proves that the five midpoint records

\[
y_i
=
(x_i,y_i,z_i,\chi_i)
\]

are affinely independent in a four-dimensional feature space.

Here \(\chi_i\) is the dimensionally homogenized SP3 clock-correction feature.

That result is exact.

This note asks a different question:

\[
\boxed{
\text{Can those same five feature-space midpoint records be identified with five physical spacetime midpoint events by one invertible affine map?}
}
\]

The answer is no.

## 2. Feature-space midpoint set

For the two source epochs

\[
t_1=2015\text{-}01\text{-}21T00{:}01{:}00Z,
\qquad
t_2=2015\text{-}01\text{-}21T00{:}03{:}00Z,
\]

the common coordinate midpoint epoch is

\[
\boxed{
t_m=2015\text{-}01\text{-}21T00{:}02{:}00Z.
}
\]

For each satellite \(i\), v0.13 forms the feature midpoint

\[
y_i
=
\frac12
\left(
y_i^{(1)}+y_i^{(2)}
\right)
\in\mathbb R^4_{\rm feature}.
\]

The five \(y_i\) have affine rank four.

Equivalently, choosing one base point \(y_1\),

\[
\det
\left[
y_2-y_1,\,
y_3-y_1,\,
y_4-y_1,\,
y_5-y_1
\right]
\neq0.
\]

## 3. Physical midpoint event set

The corresponding physical coordinate-time midpoint events are

\[
e_i
=
(c t_m,\mathbf p_i)
\in\mathbb R^{1,3}_{\rm phys},
\]

where \(\mathbf p_i\) is the spatial midpoint position of satellite \(i\).

All five share the same coordinate time:

\[
e_i^0=c t_m.
\]

Therefore every difference

\[
e_i-e_1
\]

has zero temporal component.

Hence all four difference vectors lie in the three-dimensional spatial hyperplane

\[
\{v^0=0\}.
\]

Therefore

\[
\boxed{
\operatorname{affrank}\{e_1,\ldots,e_5\}\le3.
}
\]

## 4. Affine-rank invariance

Let

\[
F(x)=Ax+b
\]

be an invertible affine map with

\[
A\in GL(4,\mathbb R).
\]

Then affine independence is preserved:

\[
\operatorname{affrank}F(S)
=
\operatorname{affrank}S.
\]

Since the feature midpoint set has affine rank four while the physical same-epoch event set has affine rank at most three,

\[
\boxed{
\operatorname{affrank}\{y_i\}=4
\neq
\operatorname{affrank}\{e_i\}\le3,
}
\]

there is no invertible affine map satisfying

\[
F(y_i)=e_i
\]

for all five anchors.

## 5. Main no-go

Therefore the four-dimensional feature carrier used in v0.13--v0.17 is not related to the physical same-epoch spacetime event coordinates by one invertible affine relabeling.

In particular:

\[
\boxed{
\text{clock-correction feature}
\neq
\text{physical coordinate time}
}
\]

at the level of affine event coordinates.

This strengthens the earlier raw-clock/event-time firewall.

## 6. What remains valid

The following earlier results remain valid in their declared scope:

- the two-epoch transform is lossless in the four-observable feature representation;
- the five feature midpoints define a nondegenerate affine 4-simplex;
- the source-derived \(Q\)-ellipsoid is a valid relational carrier;
- the Herm(2) half-difference construction uses the physical source epoch separation \(c\Delta t\), not the raw clock-correction coordinate;
- the local causal 3+1 theorem remains an exact theorem on the admitted Hermitian event carrier.

The no-go only blocks the shortcut

\[
\mathbb R^4_{\rm feature}
\overset{\rm affine}{=}
\mathbb R^{1,3}_{\rm physical}.
\]

## 7. Consequence for the carrier interpretation

The fourth SP3 feature is better typed as an additional relational / clock-state coordinate attached to the observed spatial event.

Thus the source-derived \(S^3\)-like carrier should not be treated automatically as an ordinary physical spatial slice embedded by its first three ambient coordinates.

A physical realization requires an explicit binding map.

Two admissible structural possibilities remain open:

### 7.1 Nonlinear spacetime binding

A nonlinear smooth map

\[
\Psi:
I\times\mathcal E_Q
\to
\Omega_{\rm phys}
\]

may satisfy the physical anchor constraints even though no invertible affine map can.

### 7.2 Fibered interpretation

The carrier may be represented as a base physical spacetime / spatial domain together with a clock-state or relational fiber.

Schematically,

\[
\mathcal C
\to
\mathcal X_{\rm phys},
\]

where the SP3 clock-correction feature belongs to the fiber rather than to the base physical-time coordinate.

The present result does not choose between these possibilities.

## 8. Implication for W6 external-source binding

An external physical source model supplies fields in a physical coordinate domain.

Because the feature carrier is not affinely identical to physical spacetime, W6 cannot use a source tensor by merely equating feature coordinates with external spacetime coordinates.

The external tensor must be transported through a separately certified physical binding:

\[
\boxed{
T^{\rm carrier}
=
\Psi^*T^{\rm phys}
}
\]

or through an equivalent bundle/fiber construction.

## 9. Evidence boundary

Exact:

- feature midpoint affine rank = 4;
- physical common-epoch midpoint affine rank <= 3;
- invertible affine maps preserve affine rank;
- invertible affine physical-spacetime identification is impossible.

Open:

- nonlinear physical binding;
- fibered clock-state interpretation;
- frame-transform and tensor pullback;
- full W6 physical source packet.

## 10. Frontier

The physical binding problem is now narrowed to

\[
\boxed{
\text{relational feature carrier}
\longrightarrow
\text{nonlinear or fibered physical realization}
\longrightarrow
\text{independent source pullback}.
}
\]

No further affine identification of the raw feature tuple with physical spacetime is admissible.
