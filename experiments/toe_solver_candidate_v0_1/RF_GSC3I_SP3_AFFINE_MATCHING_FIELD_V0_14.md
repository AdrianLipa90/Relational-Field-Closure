# RF-GSC3I — SP3 Affine Matching-Field Extension v0.14

Status: CANDIDATE_ONLY / UNIQUE_AFFINE_SOURCE_INTERPOLANT / EXACT_FACET_OVERLAP_COMPATIBILITY / SUBLUMINAL_CONVEX_BOUND / SMOOTH_PHYSICAL_TANGENT_BINDING_OPEN / CANON_ALLOWED_FALSE

Date: 2026-09-19

## 1. Purpose

The v0.13 source constructor establishes five observed midpoint events in a common \(3+1\) affine carrier and five source-derived spatial tangent values

\[
\beta_i
=
\frac{\mathbf x_i^{(2)}-\mathbf x_i^{(1)}}{\Delta t},
\qquad i=1,\ldots,5.
\]

The same five midpoint events are affinely independent and therefore determine one nondegenerate affine 4-simplex.

This candidate asks whether the five observed tangent values determine one global matching-field coefficient function on that data-defined simplex rather than five unrelated patch values.

## 2. Unique affine interpolant

Let the five midpoint events be

\[
y_i\in\mathbb R^4,
\qquad i=1,\ldots,5,
\]

and define the augmented affine-coordinate matrix

\[
A=
\begin{pmatrix}
1 & y_1^0 & y_1^1 & y_1^2 & y_1^3\\
1 & y_2^0 & y_2^1 & y_2^2 & y_2^3\\
1 & y_3^0 & y_3^1 & y_3^2 & y_3^3\\
1 & y_4^0 & y_4^1 & y_4^2 & y_4^3\\
1 & y_5^0 & y_5^1 & y_5^2 & y_5^3
\end{pmatrix}.
\]

Affine independence implies

\[
\det A\neq0.
\]

For each spatial component \(a=1,2,3\), there is therefore a unique coefficient vector

\[
q^{(a)}
=
(q_0^{(a)},q_1^{(a)},q_2^{(a)},q_3^{(a)},q_4^{(a)})
\]

such that

\[
\boxed{
B^a(y)
=
q_0^{(a)}
+
\sum_{\mu=0}^{3}
q_{\mu+1}^{(a)}y^\mu
}
\]

and

\[
\boxed{
B(y_i)=\beta_i
}
\]

for all five observed source events.

Thus the five source-derived tangent values determine one unique affine vector-valued interpolant

\[
\boxed{
B:\mathbb R^4\to\mathbb R^3.
}
\]

## 3. Restriction to the data-defined 4-simplex

Let

\[
\Delta^4
=
\operatorname{conv}\{y_1,\ldots,y_5\}.
\]

Every point \(y\in\Delta^4\) has barycentric coordinates

\[
\lambda_i\ge0,
\qquad
\sum_i\lambda_i=1,
\qquad
y=\sum_i\lambda_i y_i.
\]

Because \(B\) is affine,

\[
\boxed{
B(y)
=
\sum_i\lambda_i\beta_i.
}
\]

Therefore the field on the entire simplex is determined by the source vertex values with no additional interpolation parameter.

## 4. Exact boundary-facet compatibility

The spatial packet uses the five tetrahedral facets of

\[
\partial\Delta^4.
\]

On one facet, the omitted barycentric coordinate is zero. Therefore the restricted field is

\[
B_F(y)
=
\sum_{i\in F}\lambda_i\beta_i.
\]

If two facets \(F,G\) overlap on a triangular face, then both restrictions reduce to

\[
\boxed{
B_{F\cap G}(y)
=
\sum_{i\in F\cap G}\lambda_i\beta_i.
}
\]

Hence

\[
\boxed{
B_F|_{F\cap G}
=
B_G|_{F\cap G}
}
\]

exactly on every pairwise facet overlap.

This is stronger than checking one finite handoff residual: the entire affine coefficient field agrees on every simplicial overlap.

## 5. Relation to the current TIR/RFC matching packet

The v0.13 matching packet records the five vertex values \(\beta_i\).

RF-GSC3I adds the deterministic interpolation theorem

\[
\boxed{
\{\beta_i\}_{i=1}^{5}
+
\{y_i\}_{i=1}^{5}
\Longrightarrow
B(y)
}
\]

with no additional field-value input.

The existing RF-E8 shift remains

\[
\boxed{
b(y)
=
\frac{B(y)}{c}.
}
\]

At the observed vertices this equals the already-validated source packet.

## 6. Convex subluminal bound

For every point of the simplex,

\[
B(y)
=
\sum_i\lambda_i\beta_i.
\]

The Euclidean norm is convex, so

\[
|B(y)|
\le
\sum_i\lambda_i|\beta_i|
\le
\max_i|\beta_i|.
\]

The source vertex speeds satisfy

\[
\max_i\frac{|\beta_i|}{c}
\ll1.
\]

Therefore

\[
\boxed{
\frac{|B(y)|}{c}<1
}
\]

everywhere on the entire simplex.

Consequently the v0.13 TIR Hermitian half-displacement construction

\[
X(y)
=
\frac{\ell}{2}
\left(
I+\frac{B(y)}{c}\cdot\boldsymbol\sigma
\right)
\]

stays strictly inside the positive Hermitian cone for every convex interpolation point.

## 7. What this closes

At candidate level, this removes another arbitrary choice:

old interpretation:

\[
\text{five source values}
\to
\text{chosen patchwise matching values}.
\]

v0.14 interpretation:

\[
\boxed{
\text{five source values}
+
\text{data-defined affine simplex}
\to
\text{unique global affine coefficient field}.
}
\]

No separate interpolation kernel is required.

## 8. What remains open

The boundary of an affine 4-simplex is a simplicial 3-manifold. RF-GSC3A downstream uses a smooth spatial leaf and a smooth clock-transverse vector field.

The present candidate establishes an exact affine field on the ambient simplex and an exact continuous piecewise-affine restriction to the simplicial boundary.

It does not yet establish a unique source-owned smooth tangent-field realization after the A5 smoothing step.

Therefore the remaining gate is

\[
\boxed{
\text{source-defined PL/affine matching field}
\longrightarrow
\text{smooth physical matching vector field on the admitted A5 leaf}.
}
\]

Existence of smooth approximations is standard; unique physical/source selection is a separate requirement and is not claimed here.

## 9. Evidence boundary

Current classification:

external source vertex positions: PRESENT
external source tangent values: PRESENT
affine independence: EXACT
unique affine interpolant: EXACT
facet-overlap equality: EXACT
whole-simplex subluminal bound: EXACT
RF-E8 shift extension: EXACT
continuous PL boundary field: EXACT
unique smooth physical tangent realization: OPEN
global physical spatial-carrier binding: OPEN
physical production claim: FALSE
canon allowed: FALSE
