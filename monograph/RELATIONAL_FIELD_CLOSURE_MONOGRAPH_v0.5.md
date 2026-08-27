# Relational Field Closure
## From Spinorial Information Geometry to Gauge, Lorentzian Metric and Phase-Clock Curvature

**Working monograph v0.5 — 27 August 2026**  
**Status:** `EARLY_FORMALISM / EXACT_QGT_SIGNATURE_AND_PHASE_CLOCK_CURVATURE_RESULTS / PHYSICAL_FIELD_CLOSURE_OPEN`

## Abstract

Relational Field Closure (RFC) is a derivation-first programme built from three upstream theories: The Fundamental Theory of Informational Relations (TIR), Secret of a Half, and Informational Dynamics of Time (IDT). The programme studies whether the structural content associated with Maxwell, Newton and Einstein can emerge from a common relational geometry.

The current stage contains four exact pivots. First, the spin-1/2 projective state generates a quantum geometric tensor whose real part is Fubini--Study metric data and whose imaginary part is Berry curvature data. Second, a rank-three positive spatial metric combined with an oriented IDT temporal one-form yields a Lorentzian metric with signature `(-,+,+,+)`. Third, IDT calibrates temporal phase rate into a local length carrier `ell_phi = c/|omega| = hbar c/E`. Fourth, TIR uses that carrier to physicalize Fubini--Study/Berry area, eliminating the previously free area scale from the constant-rate information-curvature sector.

The resulting temporal information curvature has the local constant-cell form

\[
\Xi_I
=\frac{\mathcal J_\pi}{a_{FS}}
\left(\frac{\omega}{c}\right)^2,
\qquad
[\Xi_I]=L^{-2},
\]

and therefore gives a dimensionally admissible, explicitly time/phase-dependent channel for dynamic `Lambda0`.

## 1. Pinned foundation

The present v0.5 branch uses exact upstream pins:

- TIR branch `agent/phase-clock-area-scale-v0.2`: `b69ba6055c0535c666e12dbba069ffb87238eee6`;
- Secret of a Half `main`: `206e49e306b246c4b0f4d182b0d32d5511739408`;
- IDT branch `feat/phase-clock-length-scale-v0.1`: `f90435edbfbba8211e6c28cc49a7c22f8059021b`.

The dependency rule is

\[
\boxed{\mathrm{TIR}+\mathrm{Half}+\mathrm{IDT}\longrightarrow\mathrm{RFC}.}
\]

TIR supplies relational information geometry, the canonical

\[
\kappa=\frac{\ln2}{24\pi},
\]

and the CP1 area/Berry structure. Secret of a Half supplies the spinorial double-cover structure. IDT supplies internal temporal flow, clock calibration, phase-energy calibration and temporal relative-information evolution.

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
\mathbb{CP}^1\simeq S^2_{\rm Bloch}.
\]

The projective `2pi` cycle and spinorial `4pi` cycle remain separately typed, with exact ratio

\[
\boxed{\frac{2\pi}{4\pi}=\frac12.}
\]

## 3. Quantum geometric tensor

For a state map on a relational base,

\[
Q_{\mu\nu}
=\langle D_\mu\psi|D_\nu\psi\rangle,
\qquad
D_\mu=(1-|\psi\rangle\langle\psi|)\partial_\mu.
\]

With a fixed convention,

\[
\boxed{
\Re Q_{\mu\nu}=g^{FS}_{\mu\nu},
\qquad
2\Im Q_{\mu\nu}=\Omega_{\mu\nu}.
}
\]

For the Bloch chart,

\[
ds^2_{FS}=\frac14(d\theta^2+\sin^2\theta\,d\varphi^2),
\]

and

\[
\mathcal F_B
=\pm\frac12\sin\theta\,d\theta\wedge d\varphi.
\]

## 4. Polyhedral geometry and rank

A single `CP1` target has real dimension two, so a single pullback has rank at most two. The rank-three spatial problem therefore moves to multi-state/polyhedral geometry. For

\[
\Psi=(\psi_1,\ldots,\psi_N),
\]

RFC uses the aggregate candidate

\[
\mathbb Q_{\mu\nu}^{(P)}
=\sum_a w_a\langle D_\mu\psi_a|D_\nu\psi_a\rangle,
\qquad w_a>0.
\]

The hexahedral/higher refinement gate seeks a positive rank-three spatial restriction of `Re Q^(P)` while the imaginary sector retains Berry/Bargmann curvature information.

## 5. Fubini--Study area and Berry flux

The CP1 Fubini--Study area form is

\[
\boxed{
da_{FS}=\frac14\sin\theta\,d\theta\wedge d\varphi.
}
\]

The Berry curvature obeys

\[
\boxed{
\mathcal F_B=\pm2\,da_{FS}.
}
\]

Hence

\[
\boxed{a_{FS}(S^2)=\pi},
\qquad
\boxed{\int_{S^2}\mathcal F_B=\pm2\pi}.
\]

For a polyhedral refinement `P`,

\[
a_{FS}^{(P)}=\sum_f a_{FS}(f)
\]

provides the dimensionless integrated-area invariant.

## 6. Euler--Berry and Poincare gates

Closed phase transport satisfies

\[
\gamma_B=\oint\mathcal A=\int\mathcal F_B,
\qquad
e^{i\Gamma}=1.
\]

RFC uses this as the Euler--Berry closure condition relating complex phase accumulation to a real modulo-cycle invariant.

The Poincare disk supplies negative curvature while retaining a positive-definite metric. Curvature sign and Lorentzian signature therefore remain separately typed.

## 7. Lorentzian signature from IDT temporal orientation

Let IDT provide a monotone clock map

\[
t=t(\tau_{\rm int}),
\qquad
\frac{dt}{d\tau_{\rm int}}>0,
\]

and define

\[
\Theta=c\,dt.
\]

If the polyhedral gate supplies a positive rank-three spatial metric `h_perp` on `ker Theta`, then

\[
\boxed{
g_L=-\Theta\otimes\Theta+h_\perp
}
\]

has exact signature

\[
\boxed{(-,+,+,+)}.
\]

The corresponding null cone satisfies

\[
\boxed{h_\perp(v,v)=a^2}
\]

for `X=a u+v` with `v in ker Theta`.

## 8. Maxwell branch

The Berry connection transforms as

\[
|\psi\rangle\to e^{i\chi}|\psi\rangle
\quad\Rightarrow\quad
\mathcal A\to\mathcal A+d\chi,
\]

with curvature

\[
\mathcal F=d\mathcal A,
\qquad
d\mathcal F=0.
\]

For states depending on internal time and relational spatial coordinates,

\[
\mathcal F_{\tau i}
=\partial_\tau\mathcal A_i-\partial_i\mathcal A_\tau,
\qquad
\mathcal F_{ij}
=\partial_i\mathcal A_j-\partial_j\mathcal A_i.
\]

The sourced Maxwell equation and physical electromagnetic normalization remain downstream closure gates.

## 9. Phase-energy and photoelectric bridge

Clock-calibrated phase rate gives

\[
\boxed{
\omega
=\frac{d\varphi}{dt}
=\frac{d\varphi/d\tau_{\rm int}}{dt/d\tau_{\rm int}},
}
\]

and

\[
\boxed{E=\hbar|\omega|.}
\]

The same bridge controls bound transitions

\[
\hbar\omega_{mn}=E_m-E_n
\]

and the photoelectric threshold

\[
K_{\max}=\hbar\omega-\Phi.
\]

The transferred energy and momentum later enter stress-energy bookkeeping.

## 10. Phase-clock length scale

IDT 01L converts the calibrated phase flow directly into a physical length per radian:

\[
\boxed{
\ell_\varphi
=c\left|\frac{dt}{d\varphi}\right|
=\frac{c}{|\omega|}
=\frac{\hbar c}{E}.
}
\]

The projective and spinorial cycle lengths are therefore

\[
L_{2\pi}=2\pi\ell_\varphi,
\qquad
L_{4\pi}=4\pi\ell_\varphi,
\]

with

\[
\boxed{\frac{L_{2\pi}}{L_{4\pi}}=\frac12.}
\]

The dimensional content is now split cleanly: CP1/polyhedral invariants determine dimensionless shape and area, while IDT phase-clock dynamics supplies the local physical conversion scale.

## 11. Phase-clock physicalization of Fubini--Study area

TIR v0.2 uses

\[
\boxed{
 ds^2_{\rm rel}
=\ell_\varphi^2 ds^2_{FS}
}
\]

as the physical scale-binding candidate. The associated area element is

\[
\boxed{
 d\mathcal A_{\rm rel}
=\ell_\varphi^2 da_{FS}
=\frac{c^2}{\omega^2}da_{FS}.
}
\]

For a constant-rate polyhedral cell `P`,

\[
\boxed{
\mathcal A_{\rm rel}^{(P)}
=\frac{c^2}{\omega_P^2}a_{FS}^{(P)}.
}
\]

For a piecewise-constant refinement,

\[
\boxed{
\mathcal A_{\rm rel}^{(P)}
=\sum_f\frac{c^2}{\omega_f^2}a_{FS}(f).
}
\]

For a continuously varying nonzero phase rate,

\[
\boxed{
\mathcal A_{\rm rel}^{(P)}
=\int_P\frac{c^2}{\omega(x)^2}da_{FS}(x).
}
\]

Thus the earlier scalar calibration `ell_R` becomes the local dynamical field

\[
\boxed{\ell_R(x)\equiv\ell_\varphi(x)=\frac{c}{|\omega(x)|}}
\]

under the present phase-clock binding.

## 12. Temporal information curvature with the free scale eliminated

IDT uses

\[
\mathcal I_\pi
=D_{\rm KL}^{(2)}(p\|\pi),
\qquad
\mathcal J_\pi=(\ln2)\mathcal I_\pi.
\]

The curvature-typed scalar is

\[
\boxed{
\Xi_I
=\frac{\mathcal J_\pi}{\mathcal A_{\rm rel}}.
}
\]

For a constant-rate cell,

\[
\boxed{
\Xi_I^{(P)}
=\frac{\mathcal J_\pi}{a_{FS}^{(P)}}
\left(\frac{\omega_P}{c}\right)^2
}
\]

or

\[
\boxed{
\Xi_I^{(P)}
=\frac{\mathcal J_\pi}{a_{FS}^{(P)}}
\left(\frac{E_P}{\hbar c}\right)^2.
}
\]

Using

\[
\kappa=\frac{\ln2}{24\pi},
\]

this becomes

\[
\boxed{
\Xi_I^{(P)}
=\frac{24\pi\kappa}{a_{FS}^{(P)}}
\mathcal I_\pi
\left(\frac{\omega_P}{c}\right)^2.
}
\]

For the full Bloch sphere,

\[
\boxed{
\Xi_I^{(S^2)}
=24\kappa\mathcal I_\pi
\left(\frac{\omega}{c}\right)^2.
}
\]

This is the central v0.5 reduction: a dimensionless information scalar multiplied by the square of a temporal phase-rate conversion produces an inverse-length-squared geometric scalar.

## 13. Exact temporal evolution

In the constant-`a_FS` sector,

\[
\Xi_I
=\frac{\mathcal J_\pi}{a_{FS}}
\frac{\omega^2}{c^2},
\]

so

\[
\boxed{
\frac{d\Xi_I}{d\tau_{\rm int}}
=
\frac{\omega^2}{c^2a_{FS}}
\frac{d\mathcal J_\pi}{d\tau_{\rm int}}
+
\frac{2\mathcal J_\pi\omega}{c^2a_{FS}}
\frac{d\omega}{d\tau_{\rm int}}.
}
\]

The two explicit channels are information redistribution and phase-rate evolution.

## 14. Dynamic Lambda0 information-phase channel

RFC defines

\[
\boxed{\Lambda_I=\alpha_I\Xi_I}
\]

with dimensionless `alpha_I`. Hence, for a constant-rate cell,

\[
\boxed{
\Lambda_I^{(P)}
=\alpha_I
\frac{24\pi\kappa}{a_{FS}^{(P)}}
\mathcal I_\pi
\left(\frac{\omega_P}{c}\right)^2.
}
\]

For the full CP1/Bloch sphere,

\[
\boxed{
\Lambda_I^{(S^2)}
=24\alpha_I\kappa\mathcal I_\pi
\left(\frac{\omega}{c}\right)^2
}
\]

or equivalently

\[
\boxed{
\Lambda_I^{(S^2)}
=24\alpha_I\kappa\mathcal I_\pi
\left(\frac{E}{\hbar c}\right)^2.
}
\]

The multi-sector scalar remains

\[
\boxed{
\Lambda_0
=\Lambda_{\rm vac}
+\Lambda_I
+\sum_r\alpha_r\mathcal S_r.
}
\]

The exact sensitivity is

\[
\boxed{\frac{\partial\Lambda_0}{\partial\Xi_I}=\alpha_I.}
\]

In the minimal information sector,

\[
\boxed{
\frac{d\Lambda_0}{d\tau_{\rm int}}
=\alpha_I\frac{d\Xi_I}{d\tau_{\rm int}}.
}
\]

## 15. Bianchi and action-level closure

For the phenomenological bookkeeping equation

\[
G_{\mu\nu}+\Lambda_0g_{\mu\nu}
=\frac{8\pi G}{c^4}T^{\rm visible}_{\mu\nu},
\]

Bianchi gives

\[
\boxed{
\nabla_\mu T_{\rm visible}^{\mu\nu}
=\frac{c^4}{8\pi G}\nabla^\nu\Lambda_0.
}
\]

On a constant-`a_FS` patch,

\[
\boxed{
\nabla^\nu\Xi_I
=\frac{1}{c^2a_{FS}}
\left(
\omega^2\nabla^\nu\mathcal J_\pi
+2\mathcal J_\pi\omega\nabla^\nu\omega
\right).
}
\]

Thus information gradients and temporal phase-rate gradients both enter the dynamic scalar bookkeeping.

For

\[
S_\Lambda
=-\frac{c^3}{8\pi G}
\int\sqrt{-g}\,\Lambda_0\,d^4x,
\]

algebraic metric dependence gives

\[
\boxed{
G_{\mu\nu}
+\Lambda_0g_{\mu\nu}
-2\frac{\partial\Lambda_0}{\partial g^{\mu\nu}}
=\frac{8\pi G}{c^4}T_{\mu\nu}.
}
\]

The dependence of the phase-clock physicalized area on the emergent spacetime metric is therefore a dedicated action-level closure gate.

## 16. Current frontier

The next coupled sequence is

\[
\boxed{
\text{hexahedral rank-3 spatial metric}
\rightarrow
\text{phase-clock physical metric promotion}
\rightarrow
\text{Newton weak-field limit}
}
\]

in parallel with

\[
\boxed{
\text{Berry connection}
\rightarrow
\text{sourced Maxwell dynamics}
\rightarrow
\text{phase-energy transfer}
}
\]

followed by

\[
\boxed{
\Xi_I
\rightarrow
\alpha_I\text{ determination}
\rightarrow
\Lambda_0\text{ action variation}
\rightarrow
\text{Einstein--Bianchi closure}.
}
\]

Target equations remain validation targets. The author/formalism may suggest a common origin of gauge, metric, temporal and vacuum-curvature sectors, yet does not state that implication as an established result before the corresponding closure receipts pass.
