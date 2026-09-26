# RGB-Moire QCD background-holonomy renormalization gate v0.6

Status: EXACT_EFFECTIVE_ACTION_TO_BETA_TRANSFER / STANDARD_BACKGROUND_FIELD_TARGET_IMPORTED / PROJECT_LOOP_DETERMINANT_OPEN

Date: 2026-09-26

## Why this gate exists

The current branch has already closed the typed color representation, full SU(3) structure tensor, adjoint and fundamental Casimirs, quark-triplet link covariance, and compatibility with the existing RFG4G/RFG8-RFG15 pure-gauge tree-level sector.

A beta function cannot follow from tree-level holonomy alone. Renormalization requires a quantum fluctuation measure or an equivalent nonperturbative step-scaling construction.

Repository audit found no current RFC implementation of BRST/Faddeev-Popov, Z_g/Z_A/Z_q, a gauge-field functional measure, Wilson-action ensemble, gradient flow, Creutz-ratio step scaling, or another quantum renormalization engine.

## Preserve the holonomy as the primary object

Use the existing color link as the background carrier,

\[
\bar W_\mu(x)\in SU(3)_C.
\]

A perturbative background split may be written

\[
W_\mu(x)
=
\bar W_\mu(x)
\exp\!\left[iag\,\xi_\mu^a(x)T_a\right].
\]

The project ontology remains the holonomy/link geometry. Gauge fixing is introduced only to quotient redundant fluctuation directions in the quantum calculation.

## Standard background-field target architecture

A conventional Euclidean one-loop comparison surface has the schematic form

\[
\Gamma[\bar W]
=
S[\bar W]
+\frac12\log\det\Delta_{\rm gauge}
-\log\det\Delta_{\rm gh}
-n_f\log\det\Delta_{\rm q}
+\cdots.
\]

This determinant formula is an imported QFT target, not yet a project derivation.

The background-field Ward identity gives

\[
\boxed{Z_g Z_B^{1/2}=1}.
\]

Therefore the running coupling can be extracted from the renormalization of the background two-point sector alone once the quantum determinant/Hessian is actually derived.

## Exact transfer from an F-squared logarithm to beta(g)

Use the convention

\[
\Gamma_{\rm eff}
\supset
\frac{1}{4g^2(\mu)}
\int d^4x\,F^a_{\mu\nu}F^{a\mu\nu}.
\]

If the project calculation produces

\[
\frac{d}{d\ln\mu}\frac1{g^2}
=
\frac{b_0}{8\pi^2},
\]

then identically

\[
\boxed{
\beta(g)
=
\mu\frac{dg}{d\mu}
=
-\frac{b_0}{16\pi^2}g^3.
}
\]

Equivalently the coefficient multiplying
\(F^2\ln\mu\)
inside the effective action above is

\[
\boxed{\mathcal C_{\log}=\frac{b_0}{32\pi^2}}.
\]

This convention-transfer statement is exact.

## Target coefficient from the already-derived group data

The branch has

\[
C_A=3,\qquad C_F=\frac43,\qquad T_F=\frac12.
\]

The standard one-loop target is

\[
b_0
=
\frac{11}{3}C_A-\frac{4}{3}T_Fn_f
=
11-\frac23n_f.
\]

For \(n_f=6\),

\[
b_0=7.
\]

The project has not yet derived this logarithmic coefficient from its own fluctuation operator. Matching it is the next falsification gate.

## Minimal project-derived closure contract

Promotion from tree-level Yang-Mills to project-derived one-loop QCD requires all of:

1. a background-link split built from the existing RFG holonomy;
2. an explicit quadratic fluctuation Hessian from the same admitted action;
3. a defined quantum measure/regulator;
4. removal of gauge redundancy by BRST/Faddeev-Popov or a demonstrably equivalent gauge-invariant construction;
5. quark fluctuation determinant on the typed \(\mathbf3_C\) carrier;
6. extraction of the logarithmic \(F^2\) coefficient;
7. reproduction of \(b_0=11-\frac23n_f\) without inserting that coefficient as an input;
8. regulator/gauge-parameter independence of the admitted universal coefficient.

Two-loop promotion additionally requires the corresponding interaction/measure corrections and reproduction of

\[
b_1=102-\frac{38}{3}n_f.
\]

## Current verdict

The exact algebraic transfer

\[
F^2\log\mu
\rightarrow
\frac{d}{d\log\mu}(1/g^2)
\rightarrow
\beta(g)
\]

is closed.

The project-specific production of the logarithmic coefficient from RGB-Moire/RFG dynamics is OPEN.

Reference:
\`tests/reference/test_aux_rgb_qcd_background_holonomy_rg_transfer.py\`.
