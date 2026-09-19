# RF-GSC5F — SP3 Dust + Lambda Effective Source-Class Diagnostic v0.23

Status: CANDIDATE_ONLY / EFFECTIVE_SOURCE_CLASS_DIAGNOSTIC / NO_PHYSICAL_SOURCE_PROMOTION / CANON_ALLOWED_FALSE

Date: 2026-09-20

## 1. Purpose

V0.22 tests the simple vacuum-plus-Lambda class.

The source-derived carrier is approximately a static product with compact \(S^3\)-like spatial slices. The corresponding Einstein tensor may instead have the orthonormal-frame form

\[
G_{\hat a\hat b}
\approx
\operatorname{diag}(3,-1,-1,-1).
\]

This candidate tests the next minimal source class:

\[
T_{\hat a\hat b}
=
\operatorname{diag}(\rho,0,0,0),
\]

with one common cosmological constant Lambda and one common normalized density coordinate

\[
A:=\kappa_E\rho.
\]

The field equation becomes

\[
G_{\hat a\hat b}
+
\Lambda\eta_{\hat a\hat b}
=
A\,\delta_{\hat a0}\delta_{\hat b0}.
\]

Equivalently,

\[
G_{\hat0\hat0}=A+\Lambda,
\qquad
G_{\hati\hat i}=-\Lambda,
\]

with off-diagonal components zero.

## 2. Metric and curvature

The metric and Einstein tensor are exactly the same source-derived candidate objects used by v0.22.

No source tensor is inserted into the curvature calculation.

At each frozen SP3 source anchor:

1. compute the north-chart metric;
2. compute \(G_{\mu\nu}\) through the existing metric-jet / Einstein provider;
3. transform \(G_{\mu\nu}\) into the global quaternionic orthonormal frame.

## 3. Common parameter fit

For all five anchors and one finite-difference scale, define

\[
\Lambda_\star
=
-
\operatorname{mean}_{i,a=1,2,3}
G^{(i)}_{\hat a\hat a}.
\]

Then define

\[
A_\star
=
\operatorname{mean}_{i}
G^{(i)}_{\hat0\hat0}
-
\Lambda_\star.
\]

These are one common pair of parameters for the whole frozen source set.

The model tensor is

\[
G_{\rm model}
=
\operatorname{diag}
(
A_\star+\Lambda_\star,
-\Lambda_\star,
-\Lambda_\star,
-\Lambda_\star
).
\]

## 4. Diagnostics

The candidate reports:

- common Lambda_star;
- common kappa-rho coordinate A_star;
- normalized full-tensor residual;
- maximum off-diagonal component;
- maximum spatial anisotropy;
- parameter stability across an h-sweep.

A compatible result means only that the required geometric source class is numerically dust-like plus Lambda.

It does not establish that a physical dust source occupies the candidate atlas.

## 5. Expected exact static-S3 reference

For the ideal unit-radius static product

\[
\mathbb R\times S^3,
\]

one has

\[
R=6
\]

and

\[
G_{\hat a\hat b}
=
\operatorname{diag}(3,-1,-1,-1).
\]

The dust-plus-Lambda decomposition with zero pressure is then

\[
\boxed{
\Lambda=1,
\qquad
\kappa_E\rho=2.
}
\]

This reference is a diagnostic target, not an imposed fit value.

## 6. Firewalls

This candidate does not:

- claim that the physical source is dust;
- create W6 evidence;
- derive a physical matter tensor and promote it;
- identify the normalized Lambda with the observed cosmological constant;
- assign SI units to the normalized carrier without an additional scale binding.

Any eventual W6 receipt must still satisfy the independent-source contract of v0.21.
