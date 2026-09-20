# RF-GSC5E — SP3 Vacuum + Lambda Falsification v0.22

Status: CANDIDATE_ONLY / SOURCE_CLASS_FALSIFICATION_DIAGNOSTIC / ORTHONORMAL_FRAME_PRIMARY / EXACT_ROUND_S3_NO_GO / NO_SOURCE_PROMOTION / CANON_ALLOWED_FALSE

Date: 2026-09-20

## 1. Purpose

The remaining RF-E26 frontier requires independent W6 source evidence.

Before acquiring a general nonzero source tensor, test the simplest source class

\[
T_{\mu\nu}=0
\]

with one common cosmological constant \(\Lambda\):

\[
\boxed{
G_{\mu\nu}+\Lambda g_{\mu\nu}=0.
}
\]

The test is performed on all five frozen SP3 source anchors for the v0.17/v0.19 source-derived candidate metric.

It is a falsification diagnostic only. It does not promote vacuum, a physical source, or RF-E26.

## 2. Metric and curvature under test

Use the north stereographic chart of v0.19,

\[
u_N(x)
=
\left(
\frac{|x|^2-1}{|x|^2+1},
\frac{2x}{|x|^2+1}
\right),
\]

then

\[
y=g+R^{-1}u_N(x).
\]

At each y, the existing candidate chain supplies:

- lapse \(N(y)\);
- quaternionic stereographic coframe \(T_N(x)\);
- matching coefficients \(b^a(y)\);
- coordinate shift \(w_N=T_N^{-1}b\);
- the Lorentz metric from the ADM coframe.

Curvature is calculated by the existing

    metric callable -> centered metric jet -> Ricci / Einstein tensor

providers. No Einstein tensor is inserted by hand.

## 3. Primary source-class test in an orthonormal frame

The coordinate coframe is

\[
E^A{}_\mu.
\]

For a covariant Einstein tensor \(G_{\mu\nu}\), define orthonormal-frame components

\[
\boxed{
G_{\hat A\hat B}
=
(E^{-1})^\mu{}_{\hat A}
(E^{-1})^\nu{}_{\hat B}
G_{\mu\nu}.
}
\]

In this frame,

\[
g_{\hat A\hat B}=\eta_{\hat A\hat B}
=
\operatorname{diag}(-1,1,1,1).
\]

Therefore the vacuum-plus-Lambda condition is

\[
\boxed{
G_{\hat A\hat B}
+
\Lambda\eta_{\hat A\hat B}
=
0.
}
\]

The primary common scalar fit across all five anchors is

\[
\boxed{
\Lambda_\star
=
-
\frac{
\sum_i
\langle G_{\hat A\hat B}^{(i)},\eta\rangle_F
}{
5\,\langle\eta,\eta\rangle_F
}.
}
\]

This removes chart-dependent weighting from the source-class decision.

The previous coordinate-basis Frobenius fit is retained only as a secondary diagnostic.

## 4. Exact round-S3 no-go

The v0.15/v0.16 spatial carrier is the round \(S^3\) geometry in its source-derived Q metric.

For the exact product baseline

\[
\mathbb R\times S^3_a
\]

with finite radius a, the orthonormal Einstein tensor is

\[
\boxed{
G_{\hat A\hat B}
=
\operatorname{diag}
\left(
\frac{3}{a^2},
-\frac{1}{a^2},
-\frac{1}{a^2},
-\frac{1}{a^2}
\right).
}
\]

Vacuum plus one constant Lambda requires simultaneously

\[
\Lambda=\frac{3}{a^2}
\]

from the temporal component and

\[
\Lambda=\frac{1}{a^2}
\]

from the spatial components.

Their difference is

\[
\boxed{
\frac{2}{a^2}>0
}
\]

for every finite positive a.

Therefore

\[
\boxed{
\mathbb R\times S^3_a
\text{ cannot satisfy vacuum + one constant }\Lambda
}
\]

for finite a.

This is an exact mathematical source-class no-go for the round baseline. It is not physical source evidence.

## 5. Numerical source-derived deformation test

The actual v0.17 metric contains the source-derived lapse and matching field.

At each frozen anchor and each finite-difference scale h, the validator computes:

- \(R\);
- \(G_{\hat A\hat B}\);
- the common orthonormal-frame \(\Lambda_\star\);
- the normalized vacuum-plus-Lambda residual;
- deviation from the round-S3 pattern
  \[
  \operatorname{diag}(3,-1,-1,-1)
  \]
  in the normalized carrier.

The h-sweep is

\[
3\times10^{-3},\;
10^{-3},\;
3\times10^{-4},\;
10^{-4}.
\]

A robust rejection requires a normalized residual above the declared rejection floor at every h and stable \(\Lambda_\star\).

## 6. Interpretation classes

VACUUM_PLUS_LAMBDA_COMPATIBLE_NUMERIC

means the candidate metric is numerically compatible with the simple source class on the tested anchors.

VACUUM_PLUS_LAMBDA_REJECTED_ON_CANDIDATE_METRIC

means one common Lambda does not remove the Einstein tensor on the tested source-derived metric.

INCONCLUSIVE_NUMERICAL_STABILITY

means the h-sweep is not stable enough to classify the source class.

## 7. Evidence boundary

This diagnostic does not:

- define \(T_{\mu\nu}\) from \(G_{\mu\nu}\);
- identify the required nonzero source;
- prove that the candidate carrier is physical spacetime;
- promote vacuum;
- promote RF-E26;
- use the numerical source-class rejection as production W6 evidence.

A rejection only says that if this candidate metric is retained, the W6 source cannot be the simple \(T=0\) plus one constant Lambda class on the tested carrier.
