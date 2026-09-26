# RGB-Moire QCD 4D periodic holonomy spectrum v0.8

Status: EXACT_4D_CHAIN_COMPLEX / EXACT_HODGE_SPECTRUM / EXACT_SCALE_CARRIER / BACKGROUND_F2_LOG_OPEN

Date: 2026-09-26

## Purpose

v0.7 constructed the graph-native Wilson Hessian and gauge quotient on one plaquette. A single plaquette has no meaningful momentum/scale spectrum.

This gate extends the same construction to a periodic four-dimensional hypercubic lattice.

## Discrete complex

For an \(L^4\) periodic lattice define

\[
D:C^0\to C^1
\]

as the site-to-link incidence operator and

\[
B:C^1\to C^2
\]

as the plaquette curl.

Exactly,

\[
\boxed{BD=0}.
\]

In Feynman-type graph gauge with the v0.7 normalization \(C_p=2,\xi=1\), the one-form Hodge operator is

\[
\boxed{
\Delta_1
=
B^\dagger B+DD^\dagger.
}
\]

The ghost/site operator is

\[
\boxed{
\Delta_0=D^\dagger D.
}
\]

## Exact periodic spectrum

For lattice momentum

\[
n_\mu\in\{0,\ldots,L-1\},
\]

define

\[
\boxed{
\hat p^2(n)
=
4\sum_{\mu=1}^4
\sin^2\left(\frac{\pi n_\mu}{L}\right).
}
\]

The one-form Hodge spectrum is exactly the scalar lattice-Laplacian spectrum repeated once for each of the four spacetime link directions:

\[
\operatorname{spec}(\Delta_1)
=
\{\hat p^2(n)\}_{n}^{\times 4}.
\]

The executable gate verifies this independently for \(L=2\) and \(L=3\).

## Harmonic holonomies

On the four-torus, \(\Delta_1\) has exactly four harmonic zero modes.

They are the four constant flat-link/toron directions and are not local gauge artifacts.

Thus the SU(3) quadratic lift has

\[
\boxed{4\times8=32}
\]

harmonic color-holonomy zero modes before a global-sector prescription is chosen.

The ghost Laplacian has exactly one zero mode per color copy, corresponding to the global gauge rotation.

## Physical scale

Restoring lattice spacing \(a\),

\[
\lambda_n(a)
=
\frac{\hat p^2(n)}{a^2}.
\]

Therefore the fluctuation engine now has an explicit scale carrier. Under \(a\to a'\), every nonzero free eigenvalue scales as

\[
\lambda_n(a')/\lambda_n(a)
=
(a/a')^2.
\]

## Why this is still not the QCD beta function

The trivial-background determinant sees the free Hodge spectrum but has no nonzero background field strength \(F_{\mu\nu}\).

Consequently it cannot determine the coefficient of

\[
F^2\log\mu
\]

that controls coupling renormalization.

The next gate must replace the trivial background by an admitted nontrivial background holonomy/curvature and compute the background-dependent determinant difference

\[
\Delta\Gamma[\bar W]
=
\Gamma[\bar W]-\Gamma[I].
\]

Only the \(F^2\log a\) or \(F^2\log\mu\) coefficient of that difference can enter the v0.6 beta-function transfer.

## Advancement

The project-side route is now

\[
W_{ij}
\to
(B,D)
\to
\Delta_1,\Delta_0
\to
\hat p^2/a^2
\to
\text{background-dependent determinant next}.
\]

Reference:
\`tests/reference/test_aux_rgb_qcd_4d_periodic_holonomy_spectrum.py\`.
