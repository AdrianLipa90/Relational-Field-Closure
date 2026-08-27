# Relational Field Closure
## From Spinorial Information Geometry to Gauge, Metric and Energy Transfer

**Working monograph v0.2 — 27 August 2026**  
**Status:** EARLY_FORMALISM / EXACT_PROJECTIVE_GEOMETRY / PHYSICAL_CLOSURE_OPEN

## Abstract

Relational Field Closure (RFC) studies whether familiar field structures can arise from a common relational geometry built from TIR, Secret of a Half and Informational Dynamics of Time. The present stage identifies a precise mathematical primitive: the quantum geometric tensor of a spin-1/2 projective state. Its real part is Fubini--Study metric data and its imaginary part is Berry curvature data. The same construction supports coordinate-independent polyhedral invariants, discrete holonomy and a refinement path toward continuum fields. IDT supplies the separate temporal orientation and clock-calibration problem needed before any Lorentzian spacetime identification. A phase-energy gate then connects temporal phase rate to physical energy transfer, including bound spectroscopy and the photoelectric threshold. The Maxwell, Newton, dynamic \(\Lambda_0\) and Einstein closures remain downstream falsifiable targets.

## 1. Three pinned upstreams

RFC is not a replacement for its sources. It is a closure repository with frozen cross-references:

\[
\mathrm{TIR}+\mathrm{Half}+\mathrm{IDT}\longrightarrow\mathrm{RFC}.
\]

TIR supplies relational information geometry and phase structures; Secret of a Half supplies the spinorial/double-cover critical-half structure; IDT supplies internal temporal flow, transport and clock calibration. The target field equations are used only for validation.

## 2. Spin-1/2 and the Bloch sphere

A normalized two-component state

\[
|\psi\rangle=\begin{pmatrix}\cos(\theta/2)\\e^{i\varphi}\sin(\theta/2)\end{pmatrix}
\]

defines a ray on

\[
\mathbb{CP}^1\simeq S^2.
\]

The spinor representative and the projective point have different closure properties. A \(2\pi\) rotation changes the sign of the spinor while a \(4\pi\) rotation restores it. This is the exact geometric setting in which the recurring half-cycle

\[
\frac{2\pi}{4\pi}=\frac12
\]

is typed.

## 3. One complex tensor, two real geometries

The horizontal quantum geometric tensor is

\[
Q_{\mu\nu}=\langle D_\mu\psi|D_\nu\psi\rangle,
\qquad
D_\mu=(1-|\psi\rangle\langle\psi|)\partial_\mu.
\]

Its Hermitian decomposition yields

\[
\mathrm{Re}\,Q=g^{FS},
\qquad
2\,\mathrm{Im}\,Q=\Omega,
\]

with convention fixed once. Thus the complex projective state naturally generates a real metric and a real curvature two-form. For the Bloch spinor,

\[
ds^2_{FS}=\frac14(d\theta^2+\sin^2\theta\,d\varphi^2),
\]

while one Berry gauge gives

\[
\mathcal A=\frac{1-\cos\theta}{2}d\varphi,
\qquad
\mathcal F=\frac12\sin\theta\,d\theta\wedge d\varphi.
\]

The coefficient \(1/2\) therefore appears in the map from oriented Bloch-sphere area to Berry phase, independently of any later field interpretation.

## 4. Polyhedra as discrete curvature cells

For projective vertices \([\psi_a]\), the quantities

\[
d^{FS}_{ab}=\arccos|\langle\psi_a|\psi_b\rangle|,
\qquad
P_{ab}=|\langle\psi_a|\psi_b\rangle|^2
\]

are coordinate- and phase-representative-independent. Oriented triples carry the Bargmann invariant

\[
\Delta_{abc}=\langle\psi_a|\psi_b\rangle
\langle\psi_b|\psi_c\rangle
\langle\psi_c|\psi_a\rangle,
\]

whose argument is geometric phase. A polyhedral face therefore has an integrated Berry holonomy. Tetrahedral, hexahedral and higher cells become discretizations of metric and curvature rather than merely preferred pictures. The research target is the subset of invariants that survives arbitrary refinement.

For an oriented closed covering of the Bloch sphere,

\[
\sum_f\Omega_f=4\pi,
\qquad
\sum_f\gamma_f=2\pi\pmod{2\pi},
\]

providing a discrete form of the sphere-to-Berry half factor.

## 5. Euler--Berry closure and the Poincare gate

A closed Berry loop satisfies

\[
\gamma_B=\oint\mathcal A=\int\mathcal F,
\]

and projective closure is expressed by

\[
e^{i\Gamma}=1.
\]

This is the Euler--Berry closure condition that converts an accumulated complex phase into a real modulo-\(2\pi\) geometric invariant.

The Fubini--Study sphere has positive curvature. The Poincare disk has negative curvature. RFC therefore treats their denominator/sign relation as a candidate continuation problem, not an identification. The central metric task is to determine whether IDT temporal orientation plus an explicit continuation can yield a Lorentzian metric and causal cone while preserving the appropriate projective/holonomy invariants.

## 6. Maxwell branch

The Berry connection already has the local gauge law

\[
|\psi\rangle\to e^{i\chi}|\psi\rangle
\quad\Rightarrow\quad
\mathcal A\to\mathcal A+d\chi,
\]

and curvature

\[
\mathcal F=d\mathcal A,
\qquad
d\mathcal F=0.
\]

If the state depends on internal time and relational spatial coordinates,

\[
|\psi\rangle=|\psi(\tau,q^i)\rangle,
\]

then

\[
\mathcal F_{\tau i}=\partial_\tau\mathcal A_i-\partial_i\mathcal A_\tau,
\qquad
\mathcal F_{ij}=\partial_i\mathcal A_j-\partial_j\mathcal A_i.
\]

This reproduces the tensor type required for electric-like and magnetic-like components. The physical electromagnetic normalization and sourced Maxwell equation remain open gates.

## 7. Einstein's photoelectric bridge as energy transfer

The phase sector becomes physically measurable through frequency. For clock time \(t\),

\[
\omega=\frac{d\varphi}{dt},
\qquad
E=\hbar\omega.
\]

With IDT internal time \(\tau\),

\[
E=\hbar\frac{d\varphi/d\tau}{dt/d\tau}.
\]

The same relation controls bound spectroscopy,

\[
\hbar\omega_{mn}=E_m-E_n,
\]

and the photoelectric threshold,

\[
K_{\max}=\hbar\omega-\Phi.
\]

This is the RFC bridge from field phase to matter energy transfer. Once energy and momentum are transferred, they contribute to the total stress-energy bookkeeping that later enters the Einstein closure. The bridge joins electromagnetic phase dynamics and gravitational sourcing through energy transfer; it is not itself a derivation of the Einstein field equations.

## 8. Dynamic Lambda0 and Einstein closure target

RFC retains the source-program target

\[
G_{\mu\nu}+\Lambda_0g_{\mu\nu}
=\frac{8\pi G}{c^4}T^{\rm total}_{\mu\nu},
\]

but re-derives the admissible scalar basis of \(\Lambda_0\). Candidate scalar inputs include information/time invariants, matter kinetic/potential invariants and the electromagnetic scalar \(F_{\mu\nu}F^{\mu\nu}\). Every term must have net dimension \(L^{-2}\).

The Bianchi identity forces a conservation/transfer contract. In the displayed bookkeeping convention,

\[
\nabla_\mu T_{\rm total}^{\mu\nu}
=\frac{c^4}{8\pi G}\nabla^\nu\Lambda_0.
\]

A complete action-level closure must decide whether this is represented as exchange with an explicit \(\Lambda_0\) stress-energy sector or by an equivalent covariant formulation.

## 9. What must be derived next

The immediate sequence is now sharp:

\[
\boxed{
\mathbb{CP}^1
\to Q_{\mu\nu}
\to \{g^{FS},\Omega\}
\to \text{polyhedral/refinement invariants}
\to \text{Euler--Berry closure}
}
\]

followed by two physical branches:

\[
\boxed{\Omega\to\mathcal A\to\mathcal F\to\text{Maxwell gates}}
\]

and

\[
\boxed{g^{FS}+\text{IDT temporal orientation}\to g^{Lor}\to\text{Newton gate}}.
\]

The phase-energy bridge then supplies a common matter-transfer layer, after which dynamic \(\Lambda_0\) and Einstein--Bianchi closure can be tested. Resonant Chemistry becomes the first high-resolution empirical interface because its spectra expose \(\hbar\omega=\Delta E\) across chemically distinct state geometries.
