# RGB-Moire QCD typed quark determinant gate v0.10

Status: STANDARD_WILSON_DIRAC_REGULATOR_IMPORTED / EXACT_LOCAL_COLOR_GAUGE_COVARIANCE / BACKGROUND_SENSITIVE_QUARK_DETERMINANT / PHYSICAL_QUARK_RENORMALIZATION_OPEN

Date: 2026-09-26

## Purpose

v0.9 constructed the background-dependent adjoint/Faddeev-Popov determinant on the admitted SU(3) color holonomy.

This gate adds a regulated quark determinant acting on the already typed fundamental color carrier

\[
\mathbb C^4_{\rm spin}\otimes\mathbb C^3_C.
\]

The Wilson-Dirac discretization is used only as a standard regulator/witness. It is not claimed as a new project-derived fermion law.

## Wilson-Dirac witness

On a four-dimensional periodic lattice define

\[
D_W(x,y)
=
(m+4r)\delta_{xy}
-\frac12\sum_\mu
\left[
(r-\gamma_\mu)U_\mu(x)\delta_{x+\hat\mu,y}
+
(r+\gamma_\mu)U_\mu^\dagger(x-\hat\mu)\delta_{x-\hat\mu,y}
\right].
\]

The color links \(U_\mu(x)\) are exactly the same SU(3) holonomy type used by the RGB-Moire/RFG color lane.

The executable witness uses a dimensionless structural mass \(m=0.4\) only to keep the finite matrix nonsingular. It is not a quark-mass prediction.

## Local gauge covariance

For an arbitrary site-dependent color frame

\[
G(x)\in SU(3)_C,
\]

links transform as

\[
U_\mu(x)
\mapsto
G(x)U_\mu(x)G^\dagger(x+\hat\mu),
\]

and quark spinors as

\[
\psi(x)\mapsto
(I_4\otimes G(x))\psi(x).
\]

The Wilson-Dirac matrix therefore obeys

\[
\boxed{
D_W[U^G]
=
\mathcal G\,D_W[U]\,\mathcal G^\dagger.
}
\]

Consequently

\[
\boxed{
\det D_W[U^G]=\det D_W[U].
}
\]

The executable test verifies the matrix covariance under independent random local SU(3) transformations on all sites.

## Background sensitivity

For the same noncommuting background used in v0.9,

\[
U_x=e^{i\theta T_1},
\qquad
U_y=e^{i\theta T_2},
\]

the regulated quark log-determinant differs from the trivial-background value.

Thus the matter sector now supplies a genuine background-dependent functional contribution

\[
\boxed{
\Gamma_q^{(1)}[\bar U]
=
-n_f\log\det D_W[\bar U].
}
\]

This object is locally gauge invariant by construction.

## Claim boundary

The project now has two background-dependent one-loop ingredients:

\[
-\log\det{}'\Delta_{\rm adj}[\bar U]
\]

and

\[
-n_f\log\det D_W[\bar U].
\]

The missing dominant piece is the gauge-vector Hessian determinant

\[
\frac12\log\det{}'\Delta_1[\bar U].
\]

Only after all three are defined on the same regulator/background family may the combined \(F^2\log a\) coefficient be extracted and compared with the universal QCD target.

Reference:
\`tests/reference/test_aux_rgb_qcd_wilson_dirac_determinant.py\`.
