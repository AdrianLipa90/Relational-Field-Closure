# Relational Field Closure

**Status:** `EARLY_FORMALISM / EXACT_QGT_AND_LORENTZ_SIGNATURE_RESULTS / PHYSICAL_CLOSURE_OPEN`

Relational Field Closure (RFC) is a derivation-first research repository testing whether Maxwell, Newton and Einstein field structures can be obtained from three pinned upstream theories:

1. **The Fundamental Theory of Informational Relations (TIR)**
2. **Secret of a Half**
3. **Informational Dynamics of Time (IDT)**

The repository also carries dynamic `Lambda0` as the candidate scalar closure entering the Einstein sector.

## Current exact structural results

### Quantum geometric tensor

For a projective state,

\[
Q_{\mu\nu}=\langle D_\mu\psi|D_\nu\psi\rangle,
\qquad
\Re Q=g^{FS},
\qquad
2\Im Q=\Omega.
\]

### Single-Bloch rank firewall

A pullback from a single `CP1` has rank at most two. A nondegenerate 3+1 geometry therefore requires a multi-state/polyhedral configuration or a higher-dimensional projective state space.

### RF-G0 Lorentzian signature theorem

Given a nonvanishing IDT temporal one-form `Theta` on a four-dimensional base and a positive-definite rank-three spatial metric `h_perp` on `ker(Theta)`, define

\[
\boxed{g_L=-\Theta\otimes\Theta+h_\perp.}
\]

Then

\[
\boxed{\operatorname{signature}(g_L)=(-,+,+,+).}
\]

The associated null cone satisfies

\[
g_L(a u+v,a u+v)=0
\iff
h_\perp(v,v)=a^2.
\]

The signature result is exact. The physical binding of `h_perp` to the hexahedral/higher invariant hierarchy and of `Theta` to the current IDT clock object remains open.

## Curvature/sign separation

The Poincare metric is positive definite even though its curvature is negative. RFC therefore treats Poincare as a curvature/refinement gate and IDT temporal orientation as the Lorentzian signature gate.

## Phase-energy bridge

The current bridge from phase to transferred energy is

\[
E=\hbar\omega
=\hbar\frac{d\varphi/d\tau}{dt/d\tau}.
\]

This controls both bound spectroscopy and the photoelectric threshold and later feeds stress-energy bookkeeping.

## Repository layers

- `formalism/` — equations, theorems and dependency gates
- `closure/maxwell/` — Maxwell derivation and tests
- `closure/newton/` — Newtonian limit derivation and tests
- `closure/einstein/` — Einstein/Bianchi closure and tests
- `closure/lambda0/` — dynamic `Lambda0` derivation and conservation contract
- `crossrefs/` — pinned upstream references
- `validation/` — symbolic/numerical receipts and bounded GREMLIN audits
- `monograph/` — derivation narrative

## Immediate frontier

1. derive a rank-three positive spatial metric from the polyhedral/hexahedral refinement hierarchy;
2. bind the IDT temporal one-form and clock normalization;
3. derive lapse/shift dynamics;
4. derive the Newton weak-field limit;
5. close Maxwell sourced dynamics;
6. derive dynamic `Lambda0` and Einstein-Bianchi closure.

## Claim firewall

Target equations remain validation targets. No known field equation may be inserted upstream and then counted as derived.
