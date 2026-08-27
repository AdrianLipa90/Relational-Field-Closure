# Relational Field Closure
## From Spinorial Information Geometry to Gauge, Lorentzian Metric and Temporal Information Curvature

**Working monograph v0.4 — 27 August 2026**  
**Status:** `EARLY_FORMALISM / EXACT_QGT_SIGNATURE_AND_INFORMATION_CURVATURE_RESULTS / PHYSICAL_FIELD_CLOSURE_OPEN`

## Abstract

Relational Field Closure (RFC) is a derivation-first programme built from three pinned upstream theories: The Fundamental Theory of Informational Relations (TIR), Secret of a Half, and Informational Dynamics of Time (IDT). The programme studies whether the structural content associated with Maxwell, Newton and Einstein can emerge from a common relational geometry.

The current stage contains three exact pivots. First, the spin-1/2 projective state generates a quantum geometric tensor whose real part is Fubini--Study metric data and whose imaginary part is Berry curvature data. Second, a rank-three positive spatial metric combined with an oriented IDT temporal one-form yields a Lorentzian metric with signature `(-,+,+,+)`. Third, TIR relational-area calibration and IDT Shannon-relative-information evolution combine into an inverse-area information scalar `Xi_I` with dimension `L^-2`, providing a dimensionally admissible temporal-information channel for the dynamic `Lambda0` sector.

Maxwell sourced dynamics, the Newton weak-field limit, the physical normalization of relational area, the information coupling coefficient and the full Einstein--Bianchi action closure remain the active derivation frontier.

## 1. Pinned foundation

RFC uses frozen upstream commits:

- TIR: `d21631fe7281b5dbbad70f3a4a5f5b4876cac9f7`;
- Secret of a Half: `206e49e306b246c4b0f4d182b0d32d5511739408`;
- IDT: `647f1652edde59d9bfd7e075fb6ed5bf02aab2fc`.

The dependency rule is

\[
\boxed{\mathrm{TIR}+\mathrm{Half}+\mathrm{IDT}\longrightarrow\mathrm{RFC}.}
\]

TIR supplies relational information geometry, the canonical

\[
\kappa=\frac{\ln2}{24\pi},
\]

and the CP1 area/Berry calibration interface. Secret of a Half supplies the spinorial double-cover structure. IDT supplies internal temporal flow, clock calibration and the temporal evolution of relative information.

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

The spinor closes after `4pi`, while the associated projective orientation carries the familiar `2pi` cycle. The typed half-cycle is therefore

\[
\frac{2\pi}{4\pi}=\frac12.
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

Thus one Hermitian tensor yields two real geometric objects: a metric sector and a curvature two-form sector.

For the Bloch chart,

\[
ds^2_{FS}=\frac14(d\theta^2+\sin^2\theta\,d\varphi^2),
\]

and one Berry orientation convention gives

\[
\mathcal F_B
=\frac12\sin\theta\,d\theta\wedge d\varphi.
\]

## 4. Polyhedral geometry and rank

A single `CP1` target has real dimension two, so a single pullback satisfies

\[
\operatorname{rank}(\psi^*g_{FS})\le2.
\]

The rank-three spatial problem therefore moves to multi-state/polyhedral geometry. For

\[
\Psi=(\psi_1,\ldots,\psi_N),
\]

RFC uses the aggregate candidate

\[
\mathbb Q_{\mu\nu}^{(P)}
=\sum_a w_a\langle D_\mu\psi_a|D_\nu\psi_a\rangle,
\qquad w_a>0.
\]

Its real part must produce a positive rank-three spatial restriction in the hexahedral/higher refinement gate. Its imaginary part carries integrated Berry/Bargmann curvature data.

## 5. Fubini--Study area and Berry flux

The CP1 Fubini--Study area form is

\[
\boxed{
da_{FS}=\frac14\sin\theta\,d\theta\wedge d\varphi.
}
\]

The Berry curvature is related by

\[
\boxed{
\mathcal F_B=\pm2\,da_{FS}.
}
\]

Consequently,

\[
\boxed{a_{FS}(S^2)=\pi},
\qquad
\boxed{\int_{S^2}\mathcal F_B=\pm2\pi}.
\]

This gives a discrete-to-continuum bridge: polyhedral face areas and Berry holonomies can be refined while preserving integrated invariants.

## 6. Euler--Berry and Poincare gates

Closed phase transport satisfies

\[
\gamma_B=\oint\mathcal A=\int\mathcal F_B,
\qquad
e^{i\Gamma}=1.
\]

RFC uses this as the Euler--Berry closure condition relating complex phase accumulation to a real modulo-cycle invariant.

The Poincare disk supplies negative curvature while retaining a positive-definite metric. RFC therefore keeps curvature sign and Lorentzian signature as separate geometric questions.

## 7. Lorentzian signature from IDT temporal orientation

Let IDT provide an oriented time variable and a monotone clock map

\[
t=t(\tau_{\rm int}),
\qquad
\frac{dt}{d\tau_{\rm int}}>0.
\]

Define the temporal one-form

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

For `X=a u+v`, `v in ker Theta`,

\[
g_L(X,X)=-a^2+h_\perp(v,v),
\]

so the null cone is

\[
\boxed{h_\perp(v,v)=a^2.}
\]

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

The physical electromagnetic normalization and the sourced Maxwell equation remain downstream closure gates.

## 9. Phase-energy and photoelectric bridge

Clock-calibrated phase rate gives

\[
\boxed{
E=\hbar\omega
=\hbar\frac{d\varphi/d\tau_{\rm int}}{dt/d\tau_{\rm int}}.
}
\]

The same bridge covers bound transitions

\[
\hbar\omega_{mn}=E_m-E_n
\]

and the photoelectric threshold

\[
K_{\max}=\hbar\omega-\Phi.
\]

The transferred energy and momentum later enter the total stress-energy bookkeeping.

## 10. Temporal information curvature

IDT uses the Shannon-relative-information scalar

\[
\mathcal I_\pi
=D_{\rm KL}^{(2)}(p\|\pi),
\]

and its natural-log form

\[
\mathcal J_\pi=(\ln2)\mathcal I_\pi.
\]

TIR supplies the physical relational-area interface

\[
\boxed{
\mathcal A_{\rm rel}=\ell_R^2a_{FS},
\qquad
[\mathcal A_{\rm rel}]=L^2.
}
\]

The combined scalar is

\[
\boxed{
\Xi_I
=\frac{\mathcal J_\pi}{\mathcal A_{\rm rel}}
=\frac{24\pi\kappa\mathcal I_\pi}{\mathcal A_{\rm rel}},
\qquad
[\Xi_I]=L^{-2}.
}
\]

Its internal-time evolution is exact:

\[
\boxed{
\frac{d\Xi_I}{d\tau_{\rm int}}
=\frac{1}{\mathcal A_{\rm rel}}
\frac{d\mathcal J_\pi}{d\tau_{\rm int}}
-\frac{\Xi_I}{\mathcal A_{\rm rel}}
\frac{d\mathcal A_{\rm rel}}{d\tau_{\rm int}}.
}
\]

This equation makes explicit that the inverse-area information scalar changes through both information redistribution and relational-area evolution.

## 11. Dynamic Lambda0 information channel

RFC defines

\[
\boxed{\Lambda_I=\alpha_I\Xi_I},
\]

with dimensionless `alpha_I`, and the multi-sector candidate

\[
\boxed{
\Lambda_0
=\Lambda_{\rm vac}
+\alpha_I\Xi_I
+\sum_r\alpha_r\mathcal S_r.
}
\]

The exact sensitivity is

\[
\boxed{
\frac{\partial\Lambda_0}{\partial\Xi_I}=\alpha_I.
}
\]

In the minimal information sector,

\[
\boxed{
\frac{d\Lambda_0}{d\tau_{\rm int}}
=\alpha_I\frac{d\Xi_I}{d\tau_{\rm int}}.
}
\]

This is the current precise meaning of the temporal-information coupling to `Lambda0`.

## 12. Bianchi and action-level closure

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

The action-level gate is sharper. For

\[
S_\Lambda
=-\frac{c^3}{8\pi G}
\int\sqrt{-g}\,\Lambda_0\,d^4x,
\]

an algebraic metric dependence of `Lambda0` produces

\[
\boxed{
G_{\mu\nu}
+\Lambda_0g_{\mu\nu}
-2\frac{\partial\Lambda_0}{\partial g^{\mu\nu}}
=\frac{8\pi G}{c^4}T_{\mu\nu}.
}
\]

This distinction is central because `A_rel` may remain an independent projective-area carrier or may become a functional of the emergent spacetime metric. RFC treats that choice as an explicit derivation gate.

## 13. Current frontier

The next sequence is

\[
\boxed{
\text{hexahedral rank-3 spatial metric}
\rightarrow
\text{physical }\ell_R
\rightarrow
\text{IDT temporal binding}
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
