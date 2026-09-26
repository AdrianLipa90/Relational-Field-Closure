# RGB-Moire QCD local heat-kernel one-loop coefficient v0.12

Status: PURE_GAUGE_ONE_LOOP_LOCAL_COEFFICIENT_CLOSED_UNDER_STANDARD_SPECTRAL_QUANTIZATION / DIRAC_MATTER_TERM_CONDITIONAL / PHYSICAL_GS_BOUNDARY_AND_SCALE_OPEN

Date: 2026-09-26

## Purpose

The v0.11 constant noncommuting background has negative vector modes, so it is not admitted as a naive real-logdet vacuum surface.

The universal one-loop beta coefficient, however, is controlled by the local ultraviolet \(F^2\) coefficient of the fluctuation operators. It can be extracted from the local heat-kernel coefficient without assuming global stability of the chosen background.

## Mathematical input

For a flat-space Laplace-type operator

\[
P=-(\nabla^2+E),
\]

the local \(F^2\) part of the four-dimensional Seeley-DeWitt coefficient is

\[
\boxed{
a_4(P)\big|_{F^2}
=
\frac{1}{(4\pi)^2}
\int
\operatorname{tr}
\left[
\frac1{12}\Omega_{\mu\nu}\Omega_{\mu\nu}
+
\frac12E^2
\right].
}
\]

This is a standard spectral theorem used as the quantization/regulator rule.

## Gauge-vector contribution

v0.11 supplies the background-field operator

\[
(\Delta_1)_{\alpha\beta}
=
-\bar D^2\delta_{\alpha\beta}
-2\,\operatorname{ad}(\bar F_{\alpha\beta}).
\]

For this operator,

\[
\operatorname{tr}\Omega^2
=
4\,\operatorname{tr}_{ad}\mathcal F^2,
\]

and

\[
\operatorname{tr}E^2
=
-4\,\operatorname{tr}_{ad}\mathcal F^2
\]

in the anti-Hermitian curvature convention.

Hence the vector \(a_4\) bracket is

\[
\frac13-2=-\frac53
\]

times \(\operatorname{tr}_{ad}\mathcal F^2\).

The bosonic determinant carries the factor \(+\frac12\), giving

\[
-\frac56\operatorname{tr}_{ad}\mathcal F^2.
\]

## Ghost contribution

v0.9 supplies the adjoint scalar/FP operator

\[
\Delta_{\rm FP}=-\bar D^2.
\]

Its local bracket is

\[
+\frac1{12}\operatorname{tr}_{ad}\mathcal F^2.
\]

The complex Grassmann determinant enters with a minus sign, yielding

\[
-\frac1{12}\operatorname{tr}_{ad}\mathcal F^2.
\]

Therefore gauge plus ghost gives

\[
\boxed{
-\frac{11}{12}
\operatorname{tr}_{ad}\mathcal F^2.
}
\]

With anti-Hermitian curvature,

\[
\operatorname{tr}_{ad}\mathcal F^2
=
-C_A F^a_{\mu\nu}F^{a\mu\nu}.
\]

Thus the one-loop effective-action divergence is proportional to

\[
+\frac{11}{12}C_A F^2.
\]

Comparing with

\[
\Gamma\supset
\frac{1}{4g^2}F^2
\]

multiplies the effective \(F^2\) coefficient by four and gives

\[
\boxed{
b_0^{\rm gauge}
=
\frac{11}{3}C_A.
}
\]

For the RGB-Moire-derived \(C_A=3\),

\[
\boxed{b_0^{\rm gauge}=11.}
\]

This pure-gauge coefficient follows from the already admitted Yang-Mills background operator, FP quotient, project-derived adjoint invariant, and the standard heat-kernel theorem.

## Dirac matter term

For a standard minimally coupled Dirac operator in representation \(R\), the corresponding spectral coefficient contributes

\[
\boxed{
b_0^{\rm Dirac}
=
-\frac43T_R n_f.
}
\]

The branch has already derived

\[
T_F=\frac12
\]

for the fundamental color triplet, and v0.10 demonstrates a gauge-covariant regulated quark determinant.

However the project-specific continuum Dirac kinetic action is not promoted here beyond the existing gauge-covariant derivative skeleton. Therefore the matter term is typed

\[
\text{CONDITIONAL_ON_STANDARD_DIRAC_KINETIC_TERM}.
\]

Under that condition,

\[
\boxed{
b_0
=
\frac{11}{3}C_A
-\frac43T_Fn_f
=
11-\frac23n_f.
}
\]

For \(n_f=6\),

\[
\boxed{b_0=7}.
\]

## Beta function

Using the exact v0.6 transfer,

\[
\boxed{
\beta(g)
=
-\frac{b_0}{16\pi^2}g^3+O(g^5).
}
\]

The one-loop coefficient is independent of the numerical value chosen for the bare coupling.

## What is and is not closed

Closed under the declared standard spectral quantization rule:

- pure-gauge local one-loop coefficient \(11C_A/3\);
- for the derived SU(3) adjoint, \(b_0^{gauge}=11\).

Conditional:

- the \(-4T_Fn_f/3\) matter contribution, pending project-level promotion of the continuum Dirac kinetic term.

Still open:

1. physical/source selection of the boundary value \(g_s(\mu_0)\) or \(\alpha_c\);
2. project-native continuum Dirac-action promotion;
3. two-loop coefficient from the full interaction/measure ledger;
4. threshold matching;
5. \(\Lambda_{QCD}\);
6. nonperturbative confinement and hadronization.

Reference:
\`tests/reference/test_aux_rgb_qcd_heat_kernel_b0.py\`.
