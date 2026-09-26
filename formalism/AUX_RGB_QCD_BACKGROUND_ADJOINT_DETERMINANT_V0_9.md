# RGB-Moire QCD background adjoint determinant gate v0.9

Status: EXACT_BACKGROUND_COVARIANT_ADJOINT_LAPLACIAN / BACKGROUND_SENSITIVE_FP_SPECTRUM / GLOBAL_COLOR_CONJUGACY_INVARIANT / FULL_VECTOR_AND_QUARK_DETERMINANTS_OPEN

Date: 2026-09-26

## Purpose

v0.8 supplied a four-dimensional scale-dependent free Hodge spectrum. Running requires a nontrivial background.

This gate introduces a noncommuting constant SU(3) holonomy background and constructs the first background-dependent determinant sector: the adjoint/Faddeev-Popov Laplacian.

## Background

Use the already admitted color generators \(T_a=\lambda_a/2\) and define constant links

\[
\bar U_x=e^{i\theta T_1},
\qquad
\bar U_y=e^{i\theta T_2},
\qquad
\bar U_z=\bar U_t=I.
\]

Because \(T_1\) and \(T_2\) do not commute,

\[
\bar U_x\bar U_y\bar U_x^\dagger\bar U_y^\dagger\neq I.
\]

Thus the background carries nonzero plaquette curvature.

## Adjoint transport

For \(U\in SU(3)\), define its adjoint representation by

\[
\boxed{
R(U)_{ab}
=
2\,\operatorname{Tr}
\left(
T_aUT_bU^\dagger
\right).
}
\]

With the project normalization
\(\operatorname{Tr}(T_aT_b)=\tfrac12\delta_{ab}\),
\(R(U)\) is real orthogonal.

The covariant forward transport of an adjoint site field is

\[
(\mathcal T_\mu\phi)(x)
=
R(\bar U_\mu)\phi(x+\hat\mu).
\]

## Background ghost/adjoint Laplacian

On the periodic lattice define

\[
\boxed{
\Delta_{\rm adj}[\bar U]
=
\sum_\mu
\left(
2I-\mathcal T_\mu-\mathcal T_\mu^\dagger
\right).
}
\]

For the trivial background this reduces to eight copies of the scalar lattice Laplacian and therefore has eight global adjoint zero modes.

For the noncommuting \(T_1/T_2\) background, only the common stabilizer/centralizer direction remains covariantly constant in the executable witness.

The pseudodeterminant

\[
\det{}'\Delta_{\rm adj}[\bar U]
\]

therefore changes nontrivially relative to the trivial background.

This is the first project-side background-sensitive determinant object in the QCD lane.

## Gauge-basis invariance

Under a global color-frame conjugation

\[
\bar U_\mu\mapsto
G\bar U_\mu G^\dagger,
\]

the adjoint Laplacian undergoes an orthogonal similarity transformation.

Hence

\[
\boxed{
\operatorname{spec}
\Delta_{\rm adj}[G\bar U G^\dagger]
=
\operatorname{spec}
\Delta_{\rm adj}[\bar U].
}
\]

The executable test verifies this to floating-point precision.

## Interpretation

This gate gives the graph-native Faddeev-Popov/adjoint determinant its first nontrivial curvature dependence.

It does not yet produce the QCD beta coefficient because the one-loop effective action also needs the gauge-vector Hessian in the same background and the quark determinant.

The target combination remains schematically

\[
\Gamma^{(1)}[\bar U]
=
\frac12\log\det{}'\Delta_1[\bar U]
-\log\det{}'\Delta_{\rm adj}[\bar U]
-n_f\log\det\Delta_q[\bar U].
\]

The next high-value gate is therefore the background-covariant vector Hessian, including its curvature/spin term.

Reference:
\`tests/reference/test_aux_rgb_qcd_background_adjoint_determinant.py\`.
