# RGB-Moire QCD background gauge-vector Hessian v0.11

Status: YM_SECOND_VARIATION_OPERATOR_CLOSED / BACKGROUND_SPECTRUM_CONJUGACY_PASS / SELECTED_CONSTANT_NONCOMMUTING_BACKGROUND_UNSTABLE / REAL_LOGDET_RG_SURFACE_REJECTED

Date: 2026-09-26

## Purpose

v0.9 and v0.10 supply background-dependent adjoint/FP and quark determinants.

The remaining one-loop ingredient is the gauge-vector quadratic operator.

RFG4G already admits the continuum Yang-Mills action and RFG8/RFG13 contain its cubic/quartic interaction structure, so the background-field second variation introduces no new gauge algebra.

## Background-field second variation

In Feynman background gauge the quadratic Yang-Mills operator has the standard form

\[
\boxed{
(\Delta_1)_{\mu\nu}
=
-\bar D^2\,\delta_{\mu\nu}
-2\,\operatorname{ad}(\bar F_{\mu\nu})
}
\]

up to the declared Hermitian-generator/sign convention.

The first term is supplied by the background covariant adjoint Laplacian already constructed in v0.9.

For a Hermitian curvature carrier \(H_F\), define the real adjoint commutator matrix by

\[
[H_F,T_b]
=
i\,M_{ab}T_a.
\]

Then

\[
M^T=-M.
\]

Because \(F_{\nu\mu}=-F_{\mu\nu}\), the Lorentz-color curvature blocks combine into a real symmetric full vector Hessian.

## RFG11-type noncommuting witness

Use

\[
\bar U_x=e^{i\theta T_1},
\qquad
\bar U_y=e^{i\theta T_2},
\]

with the other directions trivial.

The plaquette

\[
P_{xy}
=
\bar U_x\bar U_y
\bar U_x^\dagger\bar U_y^\dagger
\]

is nontrivial. Its principal Lie-algebra logarithm supplies the finite background-curvature carrier used by the spectral witness.

## Conjugacy test

Under global color conjugation

\[
\bar U_\mu\mapsto G\bar U_\mu G^\dagger,
\]

the complete vector operator is related by similarity.

The executable test verifies equality of its full spectrum to numerical precision.

## Critical result: instability of this simple background

For the \(2^4\) witness with \(\theta=0.20\), the vector operator has

\[
\boxed{6\ \text{negative modes}}
\]

and four near-zero modes.

Therefore this simple constant noncommuting \(T_1/T_2\) background is rejected as a stable surface for a naive real logarithmic determinant.

This is not a failure of the RGB-Moire SU(3) algebra. It is a property of the selected background/expansion surface.

A determinant treatment on such a background requires either analytic continuation/instability handling or a different background suitable for extracting the ultraviolet local coefficient.

## Consequence for the RG strategy

The three one-loop sectors are now structurally present:

\[
\frac12\log\det\Delta_1,
\qquad
-\log\det\Delta_{\rm FP},
\qquad
-n_f\log\det D_q.
\]

However the current noncommuting constant background is not promoted to the RG extraction surface.

The safer next step is to extract the ultraviolet local \(F^2\) coefficient by a heat-kernel/background-field method or to construct a controlled lattice background family with an explicit stability prescription.

Reference:
\`tests/reference/test_aux_rgb_qcd_background_vector_hessian.py\`.
