# RF-01 — Spin-1/2 Quantum Geometric Tensor as Relational Field Primitive

**Status:** EXACT_STATE_SPACE_GEOMETRY / PHYSICAL_FIELD_BINDING_OPEN

## 1. Projective state

Start with a normalized two-component spinor

\[
|\psi(x)\rangle\in\mathbb C^2,\qquad \langle\psi|\psi\rangle=1,
\]

with the physical ray

\[
[\psi]\in\mathbb{CP}^1\simeq S^2_{\rm Bloch}.
\]

A local Bloch chart is

\[
|\psi\rangle=
\begin{pmatrix}
\cos(\theta/2)\\
e^{i\varphi}\sin(\theta/2)
\end{pmatrix},
\qquad
z=e^{i\varphi}\tan(\theta/2).
\]

The spinorial double cover remains typed separately from the projective ray:

\[
|\psi\rangle\xrightarrow{2\pi}-|\psi\rangle,
\qquad
|\psi\rangle\xrightarrow{4\pi}|\psi\rangle.
\]

## 2. Quantum geometric tensor

Define the horizontal derivative

\[
D_\mu=(1-|\psi\rangle\langle\psi|)\partial_\mu
\]

and

\[
\boxed{Q_{\mu\nu}=\langle D_\mu\psi|D_\nu\psi\rangle.}
\]

With convention fixed once for the repository,

\[
\boxed{\mathrm{Re}\,Q_{\mu\nu}=g^{\rm FS}_{\mu\nu}},
\qquad
\boxed{2\,\mathrm{Im}\,Q_{\mu\nu}=\Omega_{\mu\nu}}.
\]

Thus one Hermitian object produces two real geometric structures: a metric tensor on projective state space and a symplectic/Berry curvature two-form.

For a qubit,

\[
ds^2_{\rm FS}=\frac14\left(d\theta^2+\sin^2\theta\,d\varphi^2\right)
\]

under the common radius-1/2 normalization.

## 3. Berry connection

Define

\[
\mathcal A_\mu=-i\langle\psi|\partial_\mu\psi\rangle,
\qquad
\mathcal F=d\mathcal A.
\]

In one standard gauge,

\[
\mathcal A=\frac{1-\cos\theta}{2}\,d\varphi,
\qquad
\mathcal F=\frac12\sin\theta\,d\theta\wedge d\varphi.
\]

The integrated flux over the Bloch sphere has magnitude \(2\pi\), corresponding to first Chern number magnitude one after division by \(2\pi\).

## 4. Time and space type signature

RFC does not insert an external spacetime one-form at RF-01. Instead the state is allowed to depend on an IDT clock variable and relational spatial coordinates,

\[
|\psi\rangle=|\psi(\tau,q^1,q^2,q^3)\rangle.
\]

Then the Berry one-form decomposes algebraically as

\[
\mathcal A=\mathcal A_\tau\,d\tau+\mathcal A_i\,dq^i,
\]

and its curvature contains

\[
\mathcal F_{\tau i}=\partial_\tau\mathcal A_i-\partial_i\mathcal A_\tau,
\qquad
\mathcal F_{ij}=\partial_i\mathcal A_j-\partial_j\mathcal A_i.
\]

This is the admitted type-level origin of temporal and spatial curvature components. Physical identification with electromagnetic \(F_{0i}\) and \(F_{ij}\) belongs to the later Maxwell binding gates.

## 5. Open gate

The Fubini--Study metric is positive definite. A physical Lorentzian metric therefore requires an additional derivation from IDT temporal orientation and/or an explicit curvature-sign/signature continuation. No Lorentzian signature is assumed at RF-01.
