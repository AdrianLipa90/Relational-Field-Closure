# Relational Field Closure

**Status:** EARLY_FORMALISM / QGT_GEOMETRY_ADMITTED / PHYSICAL_FIELD_BINDING_OPEN

Relational Field Closure (RFC) is a derivation-first research repository testing whether Maxwell, Newton and Einstein field structures can be obtained from three pinned upstream theories:

1. **The Fundamental Theory of Informational Relations (TIR)**
2. **Secret of a Half**
3. **Informational Dynamics of Time (IDT)**

The working geometric bridge is the spin-1/2 projective state space

\[
\mathbb{CP}^1 \simeq S^2_{\rm Bloch},
\]

with the quantum geometric tensor (QGT)

\[
Q_{\mu\nu}=\langle D_\mu\psi|D_\nu\psi\rangle.
\]

Its real part supplies Fubini--Study metric data and its imaginary part supplies Berry curvature data. RFC tests whether these two projections can be promoted, through explicit temporal, continuum and calibration gates, into physical metric and electromagnetic field structures.

The dynamic \(\Lambda_0\) program is retained as the candidate scalar closure in the Einstein sector. Its admissible scalar content and conservation law are to be re-derived rather than copied as premises.

## Current dependency graph

```text
TIR + Secret-of-a-Half + IDT
        |
        v
RF-00  pinned cross-reference contract
        |
        v
RF-01  spin-1/2 / CP1 quantum geometric tensor
        |
        v
RF-02  polyhedral geometric invariants and refinement
        |
        v
RF-03  Euler-Berry real/complex closure
       / \
      /   \
     v     v
RF-M0       RF-G0
Berry       IDT temporal orientation
one-form    + metric-signature gate
     |             |
     v             v
RF-M1         RF-N1 Newton weak-field gate
F=dA              |
     |             |
     +---- RF-P1 --+
          phase-energy / photoelectric bridge
                 |
                 v
        RF-L1 dynamic Lambda0 scalar closure
                 |
                 v
        RF-E1 Einstein-Bianchi closure
                 |
                 v
        RF-X1 unified limit + Resonant Chemistry interface
```

## Exact geometric core already available

For a normalized qubit/spinor

\[
|\psi\rangle=\begin{pmatrix}\cos(\theta/2)\\ e^{i\varphi}\sin(\theta/2)\end{pmatrix},
\]

the projective state lies on \(\mathbb{CP}^1\). With a fixed convention,

\[
\mathrm{Re}\,Q_{\mu\nu}=g^{\rm FS}_{\mu\nu},\qquad
2\,\mathrm{Im}\,Q_{\mu\nu}=\Omega_{\mu\nu},
\]

and the Berry connection and curvature are

\[
\mathcal A_\mu=-i\langle\psi|\partial_\mu\psi\rangle,
\qquad
\mathcal F=d\mathcal A.
\]

On the Bloch sphere one gauge gives

\[
\mathcal F=\frac12\sin\theta\,d\theta\wedge d\varphi.
\]

This exact factor \(1/2\) is cross-referenced to the spinorial \(2\pi/4\pi\) structure, without identifying distinct involutions or promoting a physical field equation prematurely.

## Repository layers

- `formalism/` — equations, type signatures and dependency gates
- `closure/maxwell/` — Berry/gauge curvature to Maxwell closure
- `closure/newton/` — weak-field limit and force-law closure
- `closure/einstein/` — Lorentzian metric, stress-energy and Bianchi closure
- `closure/lambda0/` — dynamic \(\Lambda_0\) scalar and conservation contract
- `crossrefs/` — pinned upstream references and source contracts
- `validation/` — exact identities, preregistration and GREMLIN candidate audits
- `monograph/` — derivation narrative tracking the admitted formalism

## Claim firewall

A target equation is never a derivation input. No result is promoted because it resembles Maxwell, Newton or Einstein. Exact projective/Berry/Fubini--Study identities are separated from the still-open physical bindings: Lorentzian signature, spacetime interpretation, Planck normalization, sourced Maxwell dynamics, Newtonian limit and Einstein--Bianchi closure.
