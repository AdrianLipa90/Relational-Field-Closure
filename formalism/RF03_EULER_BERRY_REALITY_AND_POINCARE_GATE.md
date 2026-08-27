# RF-03 — Euler–Berry Reality Map and Poincare Continuation Gate

**Status:** EULER_BERRY_CLOSURE_EXACT / POINCARE_TO_LORENTZ_BINDING_OPEN

## 1. Complex-to-real geometric split

The state amplitude is complex, but the QGT produces real observables by Hermitian decomposition:

\[
Q_{\mu\nu}
\longmapsto
\left(
\mathrm{Re}\,Q_{\mu\nu},
2\,\mathrm{Im}\,Q_{\mu\nu}
\right)
=
\left(g^{\rm FS}_{\mu\nu},\Omega_{\mu\nu}\right).
\]

The passage is therefore not a deletion of the imaginary sector. Metric and curvature are complementary real projections of one complex projective geometry.

## 2. Euler–Berry closure

For a closed loop \(C\),

\[
\gamma_B[C]=\oint_C\mathcal A=\int_S\mathcal F
\]

and the transported state acquires

\[
|\psi\rangle\mapsto e^{i\Gamma}|\psi\rangle.
\]

Projective Euler closure requires

\[
\boxed{e^{i\Gamma}=1\iff \Gamma\in2\pi\mathbb Z.}
\]

The spinorial representative retains the separate \(2\pi\) sign reversal / \(4\pi\) full-state closure inherited from the double cover.

## 3. Fubini--Study and Poincare geometries

In a stereographic complex chart the qubit Fubini--Study metric has positive curvature and a denominator of the form

\[
(1+|z|^2)^2,
\]

whereas the Poincare disk metric on \(|w|<1\) has negative curvature and denominator

\[
(1-|w|^2)^2.
\]

RFC therefore records the sign change as a structural clue, not an isometry:

\[
\boxed{\mathbb{CP}^1_{\rm FS}\not\cong \mathbb D_{\rm Poincare}\ \text{as Riemannian metric spaces}.}
\]

The research gate is to determine whether an admitted analytic continuation, Wick-type continuation, projective duality, or IDT temporal orientation can convert the positive projective metric sector into a Lorentzian physical metric while preserving the relevant Berry/Euler invariants.

Any such map must explicitly pass:

1. dimensional typing,
2. signature audit,
3. curvature-sign audit,
4. preservation or controlled transformation of holonomy,
5. recovery of a physical causal cone,
6. Newton weak-field limit downstream.
