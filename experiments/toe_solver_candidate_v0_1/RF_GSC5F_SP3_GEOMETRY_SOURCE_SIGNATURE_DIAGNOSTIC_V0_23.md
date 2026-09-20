# RF-GSC5F — SP3 Geometry-Implied Source Signature Diagnostic v0.23

Status: CANDIDATE_ONLY / GEOMETRY_DERIVED_DIAGNOSTIC_ONLY / NOT_W6_EVIDENCE / SOURCE_CLASS_TARGETING / CANON_ALLOWED_FALSE

Date: 2026-09-20

## 1. Purpose

V0.21 and v0.22 establish that RF-E26 still requires independent physical W6 source evidence and that no existing internal candidate currently supplies it.

The next useful question is not to manufacture

\[
T_{\mu\nu}:=\kappa_E^{-1}(G_{\mu\nu}+\Lambda g_{\mu\nu})
\]

and call it evidence.

The useful question is diagnostic:

\[
\boxed{
\text{What algebraic source class would the v0.17--v0.19 geometry require?}
}
\]

This candidate computes the Einstein tensor of the source-derived stationary Lorentz metric in the stereographic charts and classifies its orthonormal-frame algebraic structure.

The output is a search target for independent W6 acquisition, not a source receipt.

## 2. Metric used

On each stereographic chart the v0.19 coframe has the form

\[
E=
\begin{pmatrix}
N & 0\\
b & T
\end{pmatrix},
\]

with

\[
g=E^T\eta E,
\qquad
\eta=\operatorname{diag}(-1,1,1,1).
\]

Here:

- \(N\) is the v0.17 source-derived positive lapse;
- \(b^a\) is the v0.16 source-derived tangent matching field in the global quaternionic frame;
- \(T\) is the pullback of the global quaternionic spatial coframe into the selected stereographic chart.

The metric is stationary in the admitted mathematical extension.

## 3. Einstein tensor

The diagnostic uses the existing repository metric-jet and Einstein providers:

\[
g
\to
(g,\partial g,\partial^2g)
\to
G_{\mu\nu}.
\]

No Einstein field equation is used to construct \(G_{\mu\nu}\).

## 4. Orthonormal-frame representation

Let

\[
F=E^{-1}.
\]

For the covariant Einstein tensor,

\[
\boxed{
G_{\hat A\hat B}
=
F^T G F.
}
\]

The diagnostic extracts:

- energy-like component \(G_{\hat0\hat0}\);
- flux components \(G_{\hat0\hat i}\);
- spatial diagonal components;
- spatial off-diagonal components;
- isotropic pressure-like mean;
- spatial anisotropy.

## 5. Source-class residuals

The following geometric source signatures are tested only as algebraic diagnostics.

### Lambda-only

Fit

\[
G_{\hat A\hat B}
\approx
-\Lambda\eta_{\hat A\hat B}.
\]

### Comoving perfect-fluid form

Fit

\[
G_{\hat A\hat B}
\approx
\operatorname{diag}(\rho,p,p,p).
\]

The diagnostic reports flux and anisotropy residuals separately.

### Radiation-like ratio

When the perfect-fluid residual is small and \(\rho\neq0\), test

\[
w:=p/\rho
\]

against

\[
w=1/3.
\]

### Dust-like ratio

Test

\[
w=0.
\]

### Vacuum-like local residual

Report

\[
\|G\|_\infty.
\]

A small finite numerical value is not promoted to exact physical vacuum.

## 6. Sampling

The theorem-level atlas is global, but this v0.23 diagnostic is finite.

It evaluates a deterministic chart-safe sample of the source-derived \(S^3\) carrier in both north and south stereographic charts, including source-anchor and non-anchor directions.

Therefore the result is:

\[
\boxed{
\text{FINITE GEOMETRY-DERIVED SOURCE-SIGNATURE DIAGNOSTIC}.
}
\]

It is not a global source theorem.

## 7. Interpretation firewall

The diagnostic must not be used as:

- W6 physical source evidence;
- source-field provenance;
- proof that matter with the fitted equation of state exists;
- proof that a fitted \(\Lambda\) is physical;
- production RF-E26 promotion.

In particular:

\[
\boxed{
\text{geometry-implied source class}
\neq
\text{independently observed physical source}.
}
\]

## 8. Target outcome

The useful output is a ranked-by-residual description of the geometry's algebraic source requirement, for example:

- nearly Lambda-only;
- nearly perfect-fluid isotropic;
- radiation-like;
- dust-like;
- or irreducibly anisotropic/flux-carrying.

The result determines what kind of independent source packet would be worth acquiring next.
