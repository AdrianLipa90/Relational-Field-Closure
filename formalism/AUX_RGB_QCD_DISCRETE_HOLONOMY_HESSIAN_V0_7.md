# RGB-Moire QCD discrete holonomy Hessian and gauge quotient v0.7

Status: EXACT_GRAPH_HODGE_GATE / EXACT_QUADRATIC_WILSON_HESSIAN / EXACT_GAUGE_NULLSPACE / EXACT_FP_GRAPH_LAPLACIAN / CONTINUUM_LOOP_LOG_OPEN

Date: 2026-09-26

## Objective

v0.6 identified the missing quantum-fluctuation layer between the existing holonomic Yang-Mills action and a project-derived beta function.

This gate constructs the first project-side quadratic fluctuation operator directly from the holonomy graph.

No continuum loop coefficient is claimed.

## One-plaquette chain complex

Take one oriented square plaquette with four sites and four oriented links.

Let

\[
D:C^0\to C^1
\]

be the site-to-link incidence/coboundary operator and

\[
B:C^1\to C^2
\]

the oriented plaquette curl.

For the closed square,

\[
\boxed{BD=0}.
\]

This is the exact graph statement that a pure gauge link field has zero plaquette curvature.

## Quadratic Wilson action

For one color direction, the small-link expansion of the admitted Wilson defect has the quadratic form

\[
S_W^{(2)}
=
\frac{C_p}{4}\|BA\|^2.
\]

Therefore its Hessian is

\[
\boxed{
H_{\rm phys}
=
\frac{C_p}{2}B^\dagger B.
}
\]

For every site phase \(\theta\),

\[
A_{\rm gauge}=D\theta
\]

obeys

\[
H_{\rm phys}D\theta=0
\]

because \(BD=0\).

Thus the gauge nullspace is produced by the same graph topology as the holonomy itself; it is not inserted by hand.

## Gauge quotient

Use the quadratic gauge-fixing functional

\[
S_{\rm gf}
=
\frac{1}{2\xi}\|D^\dagger A\|^2.
\]

The gauge-fixed Hessian is

\[
\boxed{
H_\xi
=
\frac{C_p}{2}B^\dagger B
+
\frac1\xi DD^\dagger.
}
\]

On the connected one-plaquette complex this is full rank on link space.

The corresponding Faddeev-Popov operator is

\[
\boxed{
\Delta_{\rm FP}=D^\dagger D.
}
\]

This is simply the site graph Laplacian. Its single zero mode is the global gauge rotation; the nonzero spectrum for the square is

\[
\{2,2,4\}.
\]

In this graph formulation the ghost determinant is therefore the Jacobian associated with quotienting gauge-redundant directions. No separate ontological carrier is required.

## SU(3) lift

At quadratic order around the identity, the eight Lie-algebra color directions decouple:

\[
\boxed{
H_\xi^{SU(3)}
=
I_8\otimes H_\xi.
}
\]

For the one-plaquette witness this gives a \(32\times32\) full-rank gauge-fixed link Hessian, while the ungauge-fixed physical Hessian annihilates every color copy of the pure-gauge subspace.

Non-Abelian structure constants enter the cubic and higher fluctuation vertices already represented downstream by RFG8-RFG15.

## What this closes

The project now has an explicit graph-native route

\[
W_{ij}
\to
(B,D)
\to
H_{\rm phys}
\to
H_\xi
\to
\Delta_{\rm FP}.
\]

This supplies the quadratic operator and gauge-redundancy quotient required by the v0.6 background-holonomy renormalization architecture.

## What remains open

A one-plaquette finite Hessian has no continuum momentum integral and cannot produce logarithmic running.

The next gate requires a lattice/continuum family large enough to define:

1. momentum modes or a scale-dependent spectrum;
2. the determinant ratio over nonzero modes;
3. quark Dirac determinant on the typed color triplet;
4. regulator/continuum limit;
5. extraction of the \(F^2\log\mu\) coefficient.

Only that coefficient may be compared with \(b_0=11-\frac23n_f\).

Reference:
\`tests/reference/test_aux_rgb_qcd_discrete_holonomy_hessian.py\`.
