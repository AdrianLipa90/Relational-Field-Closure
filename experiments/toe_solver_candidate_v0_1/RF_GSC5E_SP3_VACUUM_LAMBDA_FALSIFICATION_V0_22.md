# RF-GSC5E — SP3 Vacuum + Lambda Falsification v0.22

Status: CANDIDATE_ONLY / SOURCE_CLASS_FALSIFICATION_DIAGNOSTIC / NO_SOURCE_PROMOTION / CANON_ALLOWED_FALSE

Date: 2026-09-20

## 1. Purpose

The current RF-E26 frontier requires independent W6 source evidence.

Before acquiring a general nonzero source tensor, one simple physical source class can be falsified directly against the source-derived candidate metric:

\[
\boxed{
T_{\mu\nu}=0
}
\]

with one common cosmological constant

\[
\Lambda.
\]

The vacuum-plus-Lambda equation is

\[
\boxed{
G_{\mu\nu}+\Lambda g_{\mu\nu}=0.
}
\]

This candidate tests whether one common Lambda can satisfy that equation on the five frozen SP3 source anchors for the v0.17/v0.19 metric.

It does not assume that the source-derived carrier is production physical spacetime.

## 2. Metric under test

Use the north stereographic chart of v0.19.

For chart coordinate \(x\in\mathbb R^3\),

\[
u_N(x)
=
\left(
\frac{|x|^2-1}{|x|^2+1},
\frac{2x}{|x|^2+1}
\right)
\in S^3.
\]

Map back to the source-derived ellipsoid through

\[
y=g+R^{-1}u_N(x).
\]

At y:

- v0.17 gives the positive lapse \(N(y)\);
- v0.14 gives the affine matching coefficients \(b^a(y)\);
- v0.16/v0.19 give the stereographic spatial coframe \(T_N(x)\).

The chart-coordinate shift is

\[
w_N=T_N^{-1}b.
\]

The ADM coframe therefore determines the coordinate metric

\[
g_{\mu\nu}(x).
\]

## 3. Curvature provider

The test consumes the existing candidate providers:

- metric callable to centered metric jet;
- metric jet to Ricci and Einstein tensor.

No Einstein tensor is inserted by hand.

The metric is stationary, so the time coordinate is retained in the 4D jet even though the metric coefficients are time independent.

## 4. Source anchors

Each frozen SP3 midpoint source event lies on the v0.15 ellipsoid.

Every source anchor away from the north stereographic pole has a finite north-chart coordinate and is evaluated directly.

The test uses all five frozen source anchors unless a pole exclusion is triggered, in which case the chart failure is explicit rather than silently dropping the point.

## 5. Common-Lambda fit

At each anchor i obtain

\[
g_i,\qquad G_i.
\]

A vacuum-plus-Lambda solution requires

\[
G_i=-\Lambda g_i
\]

for the same scalar Lambda at every anchor.

The unique least-squares common scalar is

\[
\boxed{
\Lambda_\star
=
-
\frac{
\sum_i \langle G_i,g_i\rangle_F
}{
\sum_i \langle g_i,g_i\rangle_F
}.
}
\]

The residual matrices are

\[
R_i
=
G_i+\Lambda_\star g_i.
\]

The diagnostic reports absolute and scale-normalized residuals.

## 6. Numerical stability

Curvature is estimated on a deterministic finite-difference sweep in stereographic coordinates.

The classification is accepted only if:

1. every metric remains finite and Lorentzian;
2. the fitted common Lambda and normalized residual are stable across the selected central sweep scales;
3. no source anchor is silently excluded.

The sweep is evidence about numerical stability only.

## 7. Interpretation

Possible outcomes:

VACUUM_PLUS_LAMBDA_COMPATIBLE_NUMERIC

means the candidate metric is numerically consistent, within the declared tolerance, with the simple vacuum-plus-Lambda source class on all five frozen anchors.

VACUUM_PLUS_LAMBDA_REJECTED_ON_CANDIDATE_METRIC

means one common Lambda does not remove the Einstein tensor on the tested source-derived metric.

INCONCLUSIVE_NUMERICAL_STABILITY

means the finite-difference sweep is not stable enough to classify the source class.

No outcome supplies production W6 evidence by itself.

Even a compatible vacuum route would still require independent provenance that the physical domain represented by the atlas is actually vacuum.

## 8. Firewalls

This diagnostic does not:

- define \(T\) from \(G\);
- promote a vacuum source;
- infer physical vacuum solely from the source metric;
- promote RF-E26;
- treat small curvature as proof of physical GR correctness.

Its role is source-class falsification only.
