# RF-GSC5F — SP3 Round-S3 Perfect-Fluid Source Shape v0.23

Status: CANDIDATE_ONLY / EXACT_SOURCE_SHAPE_THEOREM / NO_SOURCE_EVIDENCE / NO_W6_PROMOTION / CANON_ALLOWED_FALSE

Date: 2026-09-20

## 1. Purpose

V0.22 tests and rejects the simple vacuum-plus-one-Lambda source class on the source-derived candidate metric.

The round baseline of the v0.15/v0.16 carrier is

\[
M=\mathbb R\times S^3_a
\]

with finite spatial curvature radius \(a>0\).

This note derives the exact isotropic perfect-fluid source shape required by the Einstein equation on that baseline.

It does not claim that such a source is physically present.

## 2. Einstein tensor of the round product baseline

For

\[
ds^2=-dt^2+a^2 d\Omega_3^2,
\]

the orthonormal-frame Einstein tensor is

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

The scalar curvature is

\[
\boxed{
R=\frac{6}{a^2}.
}
\]

## 3. Perfect-fluid ansatz

Let the source have orthonormal-frame covariant form

\[
\boxed{
T_{\hat A\hat B}
=
\operatorname{diag}(\rho,p,p,p).
}
\]

The Einstein equation is

\[
G_{\hat A\hat B}
+
\Lambda\eta_{\hat A\hat B}
=
\kappa_E T_{\hat A\hat B},
\]

with

\[
\eta=\operatorname{diag}(-1,1,1,1).
\]

The temporal component gives

\[
\boxed{
\rho
=
\frac{3/a^2-\Lambda}{\kappa_E}.
}
\]

Each spatial component gives

\[
\boxed{
p
=
\frac{-1/a^2+\Lambda}{\kappa_E}.
}
\]

Thus, once \(a,\Lambda,\kappa_E\) are fixed, the isotropic source shape is unique.

## 4. Vacuum no-go recovered

Vacuum requires

\[
\rho=0,
\qquad
p=0.
\]

The first equation gives

\[
\Lambda=\frac{3}{a^2},
\]

while the second gives

\[
\Lambda=\frac{1}{a^2}.
\]

For finite \(a>0\), these are incompatible.

Therefore v0.22's vacuum-plus-Lambda no-go is recovered exactly.

## 5. Equation-of-state family

Define

\[
x:=\Lambda a^2.
\]

For \(\rho\neq0\),

\[
\boxed{
w
=
\frac{p}{\rho}
=
\frac{x-1}{3-x}.
}
\]

Important exact special cases are:

\[
\Lambda=0
\quad\Longrightarrow\quad
w=-\frac13;
\]

\[
\Lambda=\frac1{a^2}
\quad\Longrightarrow\quad
p=0,
\qquad
\rho=\frac{2}{\kappa_E a^2};
\]

\[
\Lambda=\frac{3}{2a^2}
\quad\Longrightarrow\quad
w=\frac13,
\]

with

\[
\rho=\frac{3}{2\kappa_Ea^2},
\qquad
p=\frac{1}{2\kappa_Ea^2}.
\]

The last case is the trace-free member of the family.

## 6. Trace-free split

The perfect-fluid trace is

\[
T
=
-\rho+3p
=
\frac{-6/a^2+4\Lambda}{\kappa_E}.
\]

Hence

\[
T=0
\]

iff

\[
\boxed{
\Lambda=\frac{3}{2a^2}
=
\frac{R}{4}.
}
\]

This is exactly the Lambda selected by orthonormal-frame least squares when one removes the metric-proportional trace part of the Einstein tensor.

The remaining source-shaped residual then has the radiation-like ratio

\[
\boxed{
p=\frac{\rho}{3}.
}
\]

This is a decomposition identity, not evidence that the physical source is radiation.

## 7. Useful invariant combinations

For positive \(\kappa_E\),

\[
\boxed{
\rho+p
=
\frac{2}{\kappa_E a^2}
>0
}
\]

independently of Lambda.

Also,

\[
\boxed{
\rho+3p
=
\frac{2\Lambda}{\kappa_E}.
}
\]

Therefore the curvature radius fixes one source combination independently of the cosmological split.

## 8. Energy-condition windows

Assuming \(\kappa_E>0\):

\[
\rho\ge0
\quad\Longleftrightarrow\quad
\Lambda a^2\le3.
\]

The dominant-energy inequality

\[
\rho\ge|p|
\]

holds for

\[
\boxed{
\Lambda a^2\le2.
}
\]

These are admissibility windows for an independently measured source. They are not source detections.

## 9. Relation to W6

V0.21 requires an independently sourced tensor packet.

The present theorem may be used only as a source-shape prediction to compare with such a packet.

A future W6 source can support this route only if its independently reconstructed local orthonormal components agree, within declared uncertainties and normalization, with the required \((\rho,p,p,p)\) family.

The theorem cannot itself populate source_observations, immutable_source_refs, or source_tensor_payload_digest.

## 10. Evidence boundary

Exact:

- round-product Einstein tensor;
- unique perfect-fluid decomposition for fixed \(a,\Lambda,\kappa_E\);
- vacuum no-go;
- equation-of-state family;
- trace-free member at \(\Lambda=R/4\);
- invariant \(\rho+p\);
- energy-condition windows.

Not established:

- physical value of \(a\);
- physical value of Lambda on this carrier;
- existence of a perfect fluid;
- matter/radiation identity;
- W6 source provenance;
- RF-E26 production promotion.

This result narrows the source class to be tested. It does not supply the source.
