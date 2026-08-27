# Relational Field Closure
## From Spinorial Information Geometry to Gauge, Lorentzian Metric and Energy Transfer

**Working monograph v0.3 — 27 August 2026**  
**Status:** `EARLY_FORMALISM / EXACT_QGT_AND_SIGNATURE_RESULTS / PHYSICAL_FIELD_CLOSURE_OPEN`

## Abstract

Relational Field Closure (RFC) is a derivation-first program built from three pinned upstream theories: The Fundamental Theory of Informational Relations (TIR), Secret of a Half, and Informational Dynamics of Time (IDT). The program asks whether the structural content associated with Maxwell, Newton and Einstein can be obtained from a common relational geometry rather than inserted as independent premises.

The present stage identifies two exact geometric pivots. First, a spin-1/2 projective state generates a quantum geometric tensor whose real part is Fubini--Study metric data and whose imaginary part is Berry curvature data. Second, once a multi-state/polyhedral refinement supplies a positive rank-three spatial metric and IDT supplies one nonvanishing oriented temporal one-form, a single temporal reflection produces a Lorentzian metric with signature `(-,+,+,+)` and an associated null cone. The sign of Poincare curvature is kept logically separate from the sign of the temporal metric eigenvalue. A phase-energy bridge then connects temporal phase rate to physical energy transfer, including bound spectroscopy and the photoelectric threshold. Maxwell, Newton, dynamic Lambda0 and Einstein-Bianchi dynamics remain downstream falsifiable closures.

## 1. Pinned foundation

RFC uses three upstreams as frozen dependencies:

\[
\boxed{\mathrm{TIR}+\mathrm{Half}+\mathrm{IDT}\longrightarrow\mathrm{RFC}.}
\]

TIR supplies relational information geometry and phase structure. Secret of a Half supplies the spinorial double-cover and critical-half structure. IDT supplies internal temporal flow, transport and clock calibration. Target field equations are validation targets, not derivation premises.

## 2. Spin-1/2 projective geometry

A normalized spinor

\[
|\psi\rangle=
\begin{pmatrix}
\cos(\theta/2)\\
e^{i\varphi}\sin(\theta/2)
\end{pmatrix}
\]

defines a ray in

\[
\mathbb{CP}^1\simeq S^2.
\]

The spinor itself closes after `4pi`, while its projective ray closes after `2pi`. Thus the ratio

\[
\frac{2\pi}{4\pi}=\frac12
\]

is typed as a double-cover half-cycle.

## 3. Quantum geometric tensor: complex primitive, real metric and curvature

For a state map depending on relational coordinates, define the horizontal derivative

\[
D_\mu=(1-|\psi\rangle\langle\psi|)\partial_\mu
\]

and the quantum geometric tensor

\[
\boxed{Q_{\mu\nu}=\langle D_\mu\psi|D_\nu\psi\rangle.}
\]

Its Hermitian decomposition is

\[
\boxed{\Re Q=g^{FS},\qquad 2\Im Q=\Omega,}
\]

with convention fixed once. For the Bloch spinor,

\[
ds^2_{FS}=\frac14(d\theta^2+\sin^2\theta\,d\varphi^2),
\]

and in a standard Berry gauge

\[
\mathcal A=\frac{1-\cos\theta}{2}d\varphi,
\qquad
\mathcal F=d\mathcal A
=\frac12\sin\theta\,d\theta\wedge d\varphi.
\]

Thus one complex projective primitive naturally yields a real metric sector and a real curvature two-form sector.

## 4. Polyhedral invariants and why they are required

For projective vertices `[psi_a]`, coordinate- and representative-phase-independent quantities include

\[
d^{FS}_{ab}=\arccos|\langle\psi_a|\psi_b\rangle|,
\qquad
P_{ab}=|\langle\psi_a|\psi_b\rangle|^2,
\]

and oriented Bargmann products

\[
\Delta_{abc}=
\langle\psi_a|\psi_b\rangle
\langle\psi_b|\psi_c\rangle
\langle\psi_c|\psi_a\rangle.
\]

Their phases encode integrated Berry geometry. Tetrahedral, hexahedral and higher configurations are therefore treated as discrete metric-curvature cells.

A crucial rank theorem prevents a shortcut. If a four-dimensional base maps into a single Bloch sphere,

\[
\psi:M^4\to\mathbb{CP}^1,
\]

then

\[
\operatorname{rank}(\psi^*g_{FS})\le2,
\]

because `CP1` is only two-real-dimensional. A single Bloch sphere cannot therefore provide a nondegenerate 3+1 metric by itself.

RFC consequently uses a multi-state/polyhedral configuration

\[
\Psi=(\psi_1,\ldots,\psi_N)
\]

with aggregate tensor

\[
\boxed{
\mathbb Q^{(P)}_{\mu\nu}
=\sum_a w_a
\langle D_\mu\psi_a|D_\nu\psi_a\rangle.
}
\]

The open RF-02 task is to identify which hexahedral/higher refinement invariant yields a positive rank-three spatial sector and survives refinement toward a continuum description.

## 5. Euler--Berry real closure

For a closed loop,

\[
\gamma_B=\oint\mathcal A=\int\mathcal F.
\]

Projective phase closure is represented by

\[
e^{i\Gamma}=1,
\]

so the accumulated complex phase is represented by a real modulo-`2pi` geometric invariant. On an oriented full covering of the Bloch sphere,

\[
\int_{S^2}\mathcal F=2\pi,
\]

while the sphere area is `4pi`, exposing the geometric half factor directly.

## 6. RF-G0: Lorentzian signature from IDT temporal orientation

The complex-to-real QGT decomposition by itself gives positive projective metric data. A Lorentzian sign requires a distinct structure: one oriented temporal direction.

Let the admitted IDT internal time be `tau` and let empirical clock calibration be monotone:

\[
t=t(\tau),\qquad \frac{dt}{d\tau}>0.
\]

Define the length-valued temporal one-form

\[
\boxed{
\Theta=c\,dt
=c\frac{dt}{d\tau}d\tau.
}
\]

On a four-dimensional relational base, the kernel

\[
\mathcal K=\ker\Theta
\]

is three-dimensional. Assume the admitted polyhedral/refinement sector supplies a positive metric `h_perp` on this kernel:

\[
h_\perp(v,v)>0
\qquad
(0\ne v\in\mathcal K).
\]

Introduce the positive companion metric

\[
h_+=\Theta\otimes\Theta+h_\perp.
\]

The temporal reflection is

\[
\boxed{g_L=h_+-2\Theta\otimes\Theta
=-\Theta\otimes\Theta+h_\perp.}
\]

For

\[
X=a u+v,
\qquad
v\in\mathcal K,
\qquad
\Theta(u)=1,
\]

we have exactly

\[
\boxed{g_L(X,X)=-a^2+h_\perp(v,v).}
\]

Therefore the metric has one negative and three positive directions:

\[
\boxed{\operatorname{signature}(g_L)=(-,+,+,+).}
\]

This result is coordinate-independent by Sylvester's law of inertia.

The null cone follows from the same identity:

\[
\boxed{g_L(X,X)=0
\iff h_\perp(v,v)=a^2.}
\]

Thus the causal cone is generated once a positive spatial metric and one oriented temporal covector are both admitted.

## 7. The exact role of the Poincare gate

The Poincare disk has negative Gaussian curvature but a positive-definite metric:

\[
ds_P^2=\frac{4(dx^2+dy^2)}{(1-r^2)^2}.
\]

Hence

\[
\boxed{\text{curvature sign}\ne\text{metric signature}.}
\]

RFC now types the roles sharply:

- Bloch/Fubini--Study/Berry geometry supplies projective metric and curvature invariants;
- Poincare-type continuation may determine the curvature class of spatial slices or refinement limits;
- IDT temporal orientation supplies the single reflected direction that creates Lorentzian signature.

This removes the need to identify negative Poincare curvature with the negative time eigenvalue.

## 8. Maxwell branch from Berry connection

The Berry connection obeys the gauge transformation

\[
|\psi\rangle\to e^{i\chi}|\psi\rangle
\quad\Longrightarrow\quad
\mathcal A\to\mathcal A+d\chi.
\]

Its curvature

\[
\mathcal F=d\mathcal A
\]

satisfies

\[
d\mathcal F=0
\]

identically. If the state depends on internal time and relational spatial coordinates,

\[
|\psi\rangle=|\psi(\tau,q^i)\rangle,
\]

then

\[
\mathcal F_{\tau i}
=\partial_\tau\mathcal A_i-\partial_i\mathcal A_\tau,
\qquad
\mathcal F_{ij}
=\partial_i\mathcal A_j-\partial_j\mathcal A_i.
\]

This supplies the correct antisymmetric tensor type and homogeneous closure. Physical electromagnetic normalization and the sourced Maxwell equation remain open.

## 9. Einstein's photoelectric bridge: phase becomes transferred energy

For physical clock time,

\[
\omega=\frac{d\varphi}{dt},
\qquad
E=\hbar\omega.
\]

Using IDT internal time,

\[
\boxed{
E=\hbar\frac{d\varphi/d\tau}{dt/d\tau}.
}
\]

The same map controls bound transitions,

\[
\hbar\omega_{mn}=E_m-E_n,
\]

and photoelectric release,

\[
K_{\max}=\hbar\omega-\Phi.
\]

RFC uses this as the bridge

\[
\boxed{
\text{phase}\to\text{frequency}\to\text{energy transfer}\to T_{\mu\nu}.
}
\]

The bridge connects electromagnetic phase dynamics to later gravitational sourcing through energy transfer. It is not itself the Einstein field equation.

## 10. Dynamic Lambda0 and Einstein-Bianchi target

RFC keeps the dynamic scalar closure target

\[
\boxed{
G_{\mu\nu}+\Lambda_0 g_{\mu\nu}
=\frac{8\pi G}{c^4}T^{\rm total}_{\mu\nu}.
}
\]

The admissible basis of `Lambda0` must be re-derived from RFC invariants rather than copied as an assumption. Candidate scalar inputs include information/time invariants, matter kinetic/potential invariants and the electromagnetic scalar

\[
F_{\mu\nu}F^{\mu\nu}.
\]

Every contribution must have net dimension `L^-2`.

The Bianchi identity imposes the bookkeeping relation

\[
\nabla_\mu T_{\rm total}^{\mu\nu}
=\frac{c^4}{8\pi G}\nabla^\nu\Lambda_0
\]

in the displayed convention. The final action-level closure must determine whether this exchange is represented by an explicit `Lambda0` stress-energy sector or an equivalent covariant formulation.

## 11. Frontier after RF-G0

The new dependency chain is

\[
\boxed{
\mathbb{CP}^1
\to Q
\to \{g^{FS},\Omega\}
\to \text{polyhedral configuration}
\to h_\perp
}
\]

and

\[
\boxed{
\mathrm{IDT}\to\Theta
\quad\Longrightarrow\quad
(h_\perp,\Theta)\to g_L.
}
\]

From there the program bifurcates:

\[
\Omega\to\mathcal A\to\mathcal F\to\text{Maxwell closure},
\]

\[
g_L\to\text{clock-rate/lapse dynamics}\to\text{Newton weak field}\to\text{Einstein curvature dynamics}.
\]

The immediate unresolved problem is no longer the sign of the Lorentzian metric. The exact sign theorem is closed conditionally. The bottleneck is now physical binding:

1. obtain a rank-three positive spatial metric from the hexahedral/higher invariant hierarchy;
2. bind `Theta` to the current canonical IDT temporal pace/clock object with units and provenance;
3. derive lapse/shift dynamics rather than assuming ADM form;
4. recover the Newtonian potential from weak clock-rate variation;
5. derive Einstein-Bianchi dynamics from an admitted action.
