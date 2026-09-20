# RF-GSC3G — SP3 ECEF-to-Candidate Affine Binding No-Go v0.23

Status: CANDIDATE_ONLY / GLOBAL_SPATIAL_AFFINE_BINDING_FAIL / FIVE_SOURCE_ANCHORS / NONLINEAR_OR_FULL_3PLUS1_BINDING_REQUIRED / CANON_ALLOWED_FALSE

Date: 2026-09-20

## 1. Purpose

V0.22 makes the production-domain problem explicit: a source-owned physical product realization must bind the physical spatial domain to the candidate carrier

\[
\mathcal E_Q\simeq S^3.
\]

The first possible shortcut is a single affine map from the observed physical ECEF midpoint coordinates

\[
\mathbf X_s\in\mathbb R^3
\]

to one stereographic chart of the candidate carrier

\[
x_s\in\mathbb R^3.
\]

This note tests and rejects that shortcut on the five frozen SP3 source anchors.

## 2. Source coordinates

For each satellite \(s\in\{G01,\ldots,G05\}\), define the physical spatial midpoint

\[
\boxed{
\mathbf X_s
=
\frac12
\left(
\mathbf X_s^{(1)}
+
\mathbf X_s^{(2)}
\right)
}
\]

from the two archived ECEF positions.

These are source-owned three-dimensional physical coordinates.

## 3. Candidate chart coordinates

The v0.15 carrier uses the four-component homogeneous midpoint

\[
y_s
=
\left(
\mathbf X_s,
c\,\delta t_{{\rm clock},s}
\right)
\in\mathbb R^4.
\]

From the exact source quadratic form \(Q\), use the positive-diagonal Cholesky convention

\[
Q=R^TR,
\]

and define

\[
u_s=R(y_s-g)\in S^3.
\]

For the north stereographic chart,

\[
\boxed{
x_s
=
\frac{\mathbf u_s}{1-u_{0,s}}.
}
\]

All five frozen source points lie away from the excluded north pole, so all five chart coordinates are finite.

## 4. Affine binding hypothesis

Assume there exists one affine physical spatial binding

\[
\boxed{
F(\mathbf X)
=
a+M\mathbf X,
\qquad
a\in\mathbb R^3,\quad
M\in\mathbb R^{3\times3},
}
\]

such that

\[
F(\mathbf X_s)=x_s
\]

for all five source anchors.

Writing

\[
A=
\begin{pmatrix}
1&X^1_{G01}&X^2_{G01}&X^3_{G01}\\
\vdots&\vdots&\vdots&\vdots\\
1&X^1_{G05}&X^2_{G05}&X^3_{G05}
\end{pmatrix},
\]

the hypothesis is equivalent to requiring each output coordinate vector

\[
(x^j_{G01},\ldots,x^j_{G05})^T
\]

to lie in the column space of \(A\).

## 5. Overdetermined fifth-anchor test

The five ECEF midpoints have affine rank three, so any four affinely independent anchors determine one affine map \(F\).

Use the first four anchors to determine \(F\) uniquely.

The fifth anchor then provides an independent test.

The candidate is rejected if

\[
\boxed{
F(\mathbf X_{G05})\ne x_{G05}.
}
\]

This test is invariant under how the affine coefficients are parameterized.

## 6. Least-squares global no-go witness

Independently, solve the overdetermined five-point least-squares problem

\[
\min_{a,M}
\sum_s
\left\|
a+M\mathbf X_s-x_s
\right\|^2.
\]

If the minimum residual is nonzero beyond numerical tolerance, no exact affine map exists through all five anchors.

The validator records both:

1. the fifth-anchor residual from the four-point exact fit;
2. the all-five least-squares residual.

## 7. Result target

The current source gives a fifth-anchor residual norm of order unity in chart coordinates, while numerical roundoff is of order machine precision.

Therefore the affine mismatch is many orders of magnitude above numerical noise.

The target classification is

\[
\boxed{
\text{GLOBAL ECEF-TO-CANDIDATE AFFINE SPATIAL BINDING}
=
\text{FAIL}.
}
\]

## 8. Interpretation

This does not refute the candidate carrier.

It refutes only the shortcut

\[
\text{physical ECEF } \mathbb R^3
\longrightarrow
\text{candidate chart } \mathbb R^3
\]

by one global affine map constrained solely by the five spatial midpoint anchors.

The result is consistent with the construction history: the candidate carrier is derived from the full four-component source points

\[
(\mathbf X,c\,\delta t_{\rm clock}),
\]

not from ECEF position alone.

Therefore a physically admissible product binding, if it exists, must use at least one of:

- a nonlinear spatial map;
- a piecewise atlas-level map with certified overlap compatibility;
- the full \(3+1\) source coordinate;
- a different independently justified physical spatial carrier binding.

## 9. Production consequence

V0.22 must not accept a spatial binding receipt whose only evidence is:

- the five ECEF midpoint anchors;
- one global affine interpolation;
- no independent full-domain extension.

That route is now explicitly falsified on the frozen source.

## 10. Evidence boundary

Exact source input:

- five archived ECEF midpoint positions;
- five v0.15/v0.19 candidate chart anchors.

Numerical theorem witness:

- affine rank of the ECEF design matrix;
- unique four-anchor affine fit;
- fifth-anchor residual;
- full five-anchor least-squares residual.

Not proved:

- absence of a nonlinear physical binding;
- absence of a full \(3+1\) physical binding;
- global physical identity of the candidate carrier.

The no-go narrows the binding search without promoting the carrier.
