# RGB-Moire QCD perturbative-running invariant gate v0.4

Status: PROJECT_GROUP_INVARIANTS_EXACT / STANDARD_QFT_BETA_FORMULA_IMPORTED / ASYMPTOTIC_FREEDOM_GROUP_FACTOR_PASS / PHYSICAL_SCALE_RUNNING_OPEN

Date: 2026-09-26

## Scope

v0.2 reconstructs the color SU(3) generator algebra from the typed RGB-Moire phase template.
v0.3 couples that same color algebra covariantly to the quark triplet.

The next falsification gate compares the resulting group invariants with the universal perturbative QCD beta-function structure.

## Project-derived invariants

From the reconstructed fundamental generators \(T_a=\lambda_a/2\),

\[
\operatorname{Tr}(T_aT_b)=T_F\delta_{ab},
\qquad
T_F=\frac12,
\]

\[
\sum_aT_aT_a=C_FI_3,
\qquad
C_F=\frac43,
\]

and from the reconstructed adjoint eight,

\[
C_A=3.
\]

These values are derived from the RGB-Moire color representation, not fitted to running-coupling data.

## Standard QFT comparison surface

Import the standard massless gauge-theory perturbative coefficients

\[
\beta_0
=\frac{11}{3}C_A-\frac{4}{3}T_Fn_f,
\]

\[
\beta_1
=\frac{34}{3}C_A^2
-4C_FT_Fn_f
-\frac{20}{3}C_AT_Fn_f.
\]

Substituting the project-derived SU(3) invariants gives

\[
\boxed{\beta_0=11-\frac23n_f},
\qquad
\boxed{\beta_1=102-\frac{38}{3}n_f}.
\]

For the standard six-flavour comparison surface,

\[
\boxed{\beta_0(6)=7},
\qquad
\boxed{\beta_1(6)=26}.
\]

The one-loop coefficient remains positive for every integer \(n_f\le16\), so the corresponding perturbative gauge theory is asymptotically free on that matter-content range.

## Claim boundary

This gate does not derive the beta-function formulas from TIR/RFC dynamics. They are standard QFT input used as an external structural falsification target.

What is project-derived here is the group data

\[
(C_A,C_F,T_F)=\left(3,\frac43,\frac12\right).
\]

Therefore any future project-specific renormalization flow proposed as physical QCD must reproduce the scheme-independent perturbative coefficients on the matching matter-content surface before promotion.

RFG4/RFG4G's \(\alpha_c\) provenance remains separately gated. No value of \(\Lambda_{QCD}\), \(\alpha_s(M_Z)\), threshold scale, or renormalization scheme is predicted here.

## Strong falsifier

A proposed RGB-Moire/QCD physical running law fails the perturbative-QCD binding if, after matching conventions and active flavour content, it cannot reproduce the universal \(\beta_0\) coefficient and the standard two-loop \(\beta_1\) coefficient.

Reference:
`tests/reference/test_aux_rgb_qcd_running_invariants.py`.
