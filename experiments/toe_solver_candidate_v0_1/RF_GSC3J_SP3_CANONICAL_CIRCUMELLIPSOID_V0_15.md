# RF-GSC3J — SP3 Canonical Circumellipsoid Smooth Carrier v0.15

Status: CANDIDATE_ONLY / EXACT_SOURCE_QUADRATIC_FORM / SMOOTH_3D_ELLIPSOID_THROUGH_ALL_SOURCE_POINTS / SMOOTH_AFFINE_COEFFICIENT_FIELD / TANGENT_SOLDERING_OPEN / CANON_ALLOWED_FALSE

Date: 2026-09-19

## 1. Purpose

V0.13 establishes five external-archive midpoint events in a \(3+1\) affine carrier.
V0.14 establishes the unique affine matching-field coefficient map

\[
B:\mathbb R^4\to\mathbb R^3
\]

through the five source-derived \(\beta_i\).

The remaining mathematical seam is the PL/simplicial boundary versus the smooth spatial leaf required downstream by RF-GSC3A.

This candidate constructs one parameter-free smooth carrier directly from the same five source points.

## 2. Dimensionally homogeneous source coordinates

For this affine carrier construction only, convert the SP3 midpoint clock-correction coordinate from microseconds to a length coordinate by

\[
u^0=c\,\delta t_{\rm clock}.
\]

This is a unit conversion, not an identification of the SP3 clock correction with the TIR event trace scale.

Define homogeneous source points

\[
y_i=
(x_i,y_i,z_i,u_i^0)\in\mathbb R^4.
\]

Let

\[
g=\frac15\sum_{i=1}^{5}y_i,
\qquad
z_i=y_i-g.
\]

Because the five source points are affinely independent, the four-dimensional centered span is full.

## 3. Exact source quadratic form

Define

\[
S=\sum_{i=1}^{5} z_i z_i^\top.
\]

Then \(S\) is symmetric positive definite.

Define

\[
\boxed{
Q=\frac54 S^{-1}.
}
\]

For the frozen SP3 source, exact rational arithmetic gives

\[
\boxed{
z_i^\top Qz_i=1
}
\]

for every \(i\), and

\[
\boxed{
z_i^\top Qz_j=-\frac14
}
\]

for every \(i\neq j\).

Therefore the five source points form a regular 4-simplex with respect to the source-derived inner product

\[
\langle a,b\rangle_Q=a^\top Qb.
\]

No fit parameter or smoothing scale is introduced.

## 4. Smooth circumellipsoid

Define the level set

\[
\boxed{
\mathcal E_Q
=
\left\{
y\in\mathbb R^4:
(y-g)^\top Q(y-g)=1
\right\}.
}
\]

Since \(Q\) is positive definite, \(\mathcal E_Q\) is a smooth compact three-dimensional ellipsoid, hence diffeomorphic to \(S^3\).

Every source midpoint lies on it exactly:

\[
y_i\in\mathcal E_Q.
\]

Thus the same five source points determine both:

1. the combinatorial boundary of their affine 4-simplex;
2. a smooth \(S^3\)-like carrier through all five points.

The second construction does not require choosing a smoothing parameter.

## 5. Smooth matching-field coefficient restriction

V0.14 supplies the unique affine map

\[
B:\mathbb R^4\to\mathbb R^3
\]

with

\[
B(y_i)=\beta_i.
\]

Because \(B\) is affine and \(\mathcal E_Q\) is smooth,

\[
\boxed{
B|_{\mathcal E_Q}:\mathcal E_Q\to\mathbb R^3
}
\]

is a globally smooth coefficient field and still satisfies

\[
B(y_i)=\beta_i
\]

at all five source anchors.

Therefore the PL-to-smooth problem for the coefficient field has a parameter-free source-derived candidate realization.

## 6. Relation to the simplicial boundary

The affine 4-simplex

\[
\Delta^4=\operatorname{conv}\{y_i\}
\]

and the ellipsoid \(\mathcal E_Q\) share the same source center \(g\) and the same five source vertices as radial directions.

The simplicial boundary remains the exact A5 combinatorial source surface.

The ellipsoid is a smooth source-derived carrier associated to that same affine simplex.

This candidate does not claim that the straight tetrahedral facets themselves are smooth patches of the ellipsoid.

## 7. Remaining tangent soldering gate

RF-GSC3A ultimately requires a smooth spatial vector field, not merely a smooth \(\mathbb R^3\)-valued coefficient function.

The present candidate closes

\[
\text{source values}
\to
\text{unique affine coefficient field}
\to
\text{smooth source-derived coefficient field on }\mathcal E_Q.
\]

It does not yet close the map

\[
\boxed{
\mathbb R^3\text{ coefficients}
\longrightarrow
T\mathcal E_Q
}
\]

with the exact physical coframe/patch identity required by RF-GSC3A/RF-E25.

That tangent-frame soldering is the next gate.

## 8. Evidence boundary

Current classification:

source affine independence: EXACT
source quadratic form Q: EXACT
five source points Q-unit: EXACT
pairwise Q-inner product -1/4: EXACT
smooth ellipsoid through all five points: EXACT
ellipsoid diffeomorphic to S3: STANDARD
unique affine beta field: EXACT PARENT V0.14
smooth beta coefficient restriction to ellipsoid: EXACT
physical tangent-frame soldering: OPEN
global physical spatial-carrier identification: OPEN
physical production claim: FALSE
canon allowed: FALSE
