# Relational Field Closure
## From Spinorial Information Geometry to Gauge, Hexahedral 3-Space, Lorentzian Metric and Phase-Clock Curvature

**Working monograph v0.6 — 27 August 2026**  
**Status:** `EARLY_FORMALISM / EXACT_QGT_HEXAHEDRAL_RANK3_LORENTZ_AND_PHASE_CLOCK_CURVATURE_RESULTS / DYNAMICAL_FIELD_CLOSURE_OPEN`

## Abstract

Relational Field Closure (RFC) is a derivation-first programme built from three upstream theories: The Fundamental Theory of Informational Relations (TIR), Secret of a Half, and Informational Dynamics of Time (IDT). Its central question is whether the structures associated with Maxwell, Newton and Einstein can arise as consequences of a common relational geometry while the known target laws remain outside the premise set.

The current stage contains five exact structural pivots. First, a spin-1/2 projective state defines a quantum geometric tensor whose real part is Fubini--Study metric data and whose imaginary part is Berry curvature data. Second, a regular hexahedral cell can be represented on the Bloch sphere by its six oriented face-normal rays. Their weighted projective orbit has exact second moment `I3/3` and aggregate Fubini--Study metric `I3/6`, giving a positive rank-three local spatial metric. Third, combining that local spatial metric with an oriented IDT temporal one-form gives Lorentzian signature `(-,+,+,+)`. Fourth, IDT converts calibrated phase rate into the local physical length carrier `ell_phi=c/|omega|=hbar c/E`, which physicalizes the projective metric and area. Fifth, the same phase-clock scale converts Shannon-relative information per projective area into an inverse-length-squared scalar `Xi_I`, giving an explicitly temporal information-curvature channel for dynamic `Lambda0`.

The principal open problems are now dynamical rather than purely dimensional: gluing the local hexahedral coframes, deriving their connection and curvature, deriving lapse/clock-rate dynamics, obtaining the Newton weak-field source equation, closing sourced Maxwell dynamics, fixing the `Lambda0` information coupling and completing action-level Einstein--Bianchi closure.

## 1. Pinned foundation and derivation firewall

The present v0.6 branch uses the stacked upstream state

- TIR `agent/hexahedral-bloch-frame-v0.1`: `a2e7003599b13a7b38c0860ecfdcf1c012780c92`;
- Secret of a Half `main`: `206e49e306b246c4b0f4d182b0d32d5511739408`;
- IDT `feat/phase-clock-length-scale-v0.1`: `f90435edbfbba8211e6c28cc49a7c22f8059021b`.

The dependency direction is

\[
\boxed{\mathrm{TIR}+\mathrm{Half}+\mathrm{IDT}\longrightarrow\mathrm{RFC}.}
\]

Known field equations are validation targets. They are not derivation inputs. Every promoted statement therefore carries one of the separate statuses: exact mathematical identity, exact conditional theorem, structural binding candidate, dynamical closure candidate, limit pass, or empirical pass.

TIR fixes

\[
\boxed{\kappa=\frac{\ln2}{24\pi}}.
\]

IDT supplies internal temporal flow, clock calibration, phase evolution and Shannon-relative-information evolution. Secret of a Half supplies the spinorial double-cover/critical-half interface without being used circularly to prove unrelated dynamical claims.

## 2. Spin-1/2 projective geometry

A normalized spinor

\[
|\psi\rangle=
\begin{pmatrix}
\cos(\theta/2)\\
e^{i\varphi}\sin(\theta/2)
\end{pmatrix}
\]

defines a projective ray in

\[
\boxed{\mathbb{CP}^1\simeq S^2_{\rm Bloch}.}
\]

The projective `2pi` cycle and spinorial `4pi` cycle remain separately typed:

\[
\boxed{\frac{2\pi}{4\pi}=\frac12.}
\]

This ratio is retained as a spinorial/projective structural relation; it is not by itself a field equation.

## 3. Quantum geometric tensor

For a projective state map,

\[
Q_{\mu\nu}
=\langle D_\mu\psi|D_\nu\psi\rangle,
\qquad
D_\mu=(1-|\psi\rangle\langle\psi|)\partial_\mu.
\]

With the declared convention,

\[
\boxed{
\Re Q_{\mu\nu}=g^{FS}_{\mu\nu},
\qquad
2\Im Q_{\mu\nu}=\Omega_{\mu\nu}.
}
\]

Thus a single Hermitian geometric tensor yields two real geometric sectors: metric data and curvature two-form data.

For the Bloch chart,

\[
\boxed{
ds^2_{FS}=\frac14(d\theta^2+\sin^2\theta\,d\varphi^2)
}
\]

and the spin-1/2 Berry curvature is

\[
\boxed{
\mathcal F_B=\pm\frac12\sin\theta\,d\theta\wedge d\varphi.
}
\]

## 4. Single-ray rank firewall

Because `CP1` has real dimension two, a single map

\[
\psi:M^4\to\mathbb{CP}^1
\]

satisfies

\[
\boxed{\operatorname{rank}(\psi^*g_{FS})\le2.}
\]

A rank-three spatial metric therefore cannot be obtained from one Bloch ray alone. RFC consequently moves the spatial problem to a multi-ray/polyhedral configuration.

This rank firewall is important: the emergence of three local spatial directions must come from relational structure among several projective states, not from relabeling the two coordinates of one Bloch sphere.

## 5. Hexahedral dual Bloch frame

A regular hexahedron has six oriented faces. Represent their outward normals by

\[
\boxed{
\mathcal H^\star
=\{\pm\mathbf e_1,\pm\mathbf e_2,\pm\mathbf e_3\}
\subset S^2_{\rm Bloch}.
}
\]

The associated pure-state density matrices are

\[
\boxed{
\rho_{i,\pm}=\frac12(I\pm\sigma_i).
}
\]

The six Bloch points form the octahedral dual of the hexahedron. The combinatorial data are

\[
(V,E,F)_{\rm hex}=(8,12,6),
\qquad
(V,E,F)_{\rm dual}=(6,12,8),
\]

so both carry

\[
\boxed{\chi=V-E+F=2.}
\]

The six Bloch states are therefore typed as oriented hexahedral face normals, not as the eight cube vertices.

## 6. Exact pair fingerprint

For pure qubit rays with Bloch vectors `n_a,n_b`,

\[
\boxed{
P_{ab}=|\langle\psi_a|\psi_b\rangle|^2
=\frac{1+\mathbf n_a\cdot\mathbf n_b}{2}
}
\]

and

\[
\boxed{
d_{FS}(a,b)=\frac12\arccos(\mathbf n_a\cdot\mathbf n_b).
}
\]

For the regular hexahedral dual frame:

\[
\boxed{
P(n,-n)=0,
\qquad
d_{FS}(n,-n)=\frac\pi2,
}
\]

while distinct orthogonal face normals satisfy

\[
\boxed{
P(e_i,e_j)=\frac12,
\qquad
d_{FS}(e_i,e_j)=\frac\pi4
\quad(i\ne j).
}
\]

This gives a coordinate-independent pairwise fingerprint of the regular dual frame.

## 7. Exact rank-three aggregate Fubini--Study metric

Assign equal weights

\[
w_a=\frac16.
\]

Define the Bloch second moment

\[
M_H=\sum_aw_a\,n_an_a^{\mathsf T}.
\]

For the six antipodal axis normals,

\[
\boxed{M_H=\frac13I_3.}
\]

Let `xi,eta in R3` generate infinitesimal rigid rotations of the six-ray configuration. Each Bloch vector changes by

\[
\delta_\xi n=\xi\times n.
\]

The aggregate Fubini--Study orbit bilinear form is

\[
\boxed{
h_H(\xi,\eta)
=\frac14\sum_aw_a
(\xi\times n_a)\cdot(\eta\times n_a).
}
\]

Using

\[
(\xi\times n)\cdot(\eta\times n)
=\xi\cdot\eta-(\xi\cdot n)(\eta\cdot n),
\]

gives the general relation

\[
\boxed{h_P=\frac14(I_3-M_P)}
\]

and for the regular hexahedral dual frame

\[
\boxed{h_H=\frac16I_3.}
\]

Therefore

\[
\boxed{
\operatorname{rank}h_H=3,
\qquad
\operatorname{Spec}(h_H)=\left\{\frac16,\frac16,\frac16\right\}
}
\]

and

\[
\boxed{
\det h_H=\frac1{216}>0,
\qquad
\operatorname{cond}(h_H)=1.
}
\]

This is an exact local theorem for the declared multi-ray orbit geometry. It satisfies the positive rank-three prerequisite required later by RF-G0.

For any normalized weighted unit-vector configuration `tr M_P=1`, so

\[
\operatorname{tr}h_P=\frac12.
\]

At fixed trace, the determinant is maximal when the three positive eigenvalues are equal; hence

\[
\boxed{\det h_P\le\left(\frac16\right)^3}
\]

with equality for isotropic second moment `M_P=I3/3`, including the regular hexahedral dual frame.

## 8. Berry, Euler and Chern invariants of the hexahedral dual

The six dual vertices tessellate the Bloch sphere into eight spherical octants, one for each original hexahedral vertex.

Each octant has solid angle

\[
\boxed{\Omega_{\rm oct}=\frac\pi2.}
\]

Since the qubit Fubini--Study area is one quarter of Bloch solid angle,

\[
\boxed{a_{FS,\rm oct}=\frac\pi8.}
\]

The corresponding oriented Berry/Pancharatnam triangular phase has magnitude

\[
\boxed{|\gamma_{B,\rm oct}|=\frac\pi4.}
\]

For the ordered rays `(+x,+y,+z)`, the Bargmann product

\[
\Delta_{xyz}
=\langle +x|+y\rangle
\langle +y|+z\rangle
\langle +z|+x\rangle
\]

has

\[
\boxed{\arg\Delta_{xyz}=+\frac\pi4}
\]

in the stated orientation convention.

Summing all eight oriented octants gives

\[
\boxed{
\sum_f\Omega_f=4\pi,
\qquad
\sum_fa_{FS}(f)=\pi
}
\]

and

\[
\boxed{
\int_{S^2}\mathcal F_B=\pm2\pi,
\qquad
c_1=\frac1{2\pi}\int_{S^2}\mathcal F_B=\pm1.
}
\]

The Euler characteristic, total FS area, total Berry flux and Chern number therefore provide exact integrated invariants for refinement bookkeeping.

## 9. Euler--Berry and Poincare gates

Closed phase transport satisfies

\[
\gamma_B=\oint\mathcal A=\int\mathcal F_B,
\qquad
e^{i\Gamma}=1.
\]

RFC uses this Euler--Berry condition to relate complex phase accumulation to a real modulo-cycle invariant.

The Poincare metric may carry negative curvature while remaining positive definite. RFC therefore keeps two notions distinct:

\[
\boxed{\text{curvature sign}\ne\text{metric signature sign}.}
\]

Poincare geometry belongs to the curvature/refinement branch; the negative temporal direction is supplied by the temporal orientation gate.

## 10. Phase-clock physicalization of the local 3-space

IDT supplies the calibrated phase rate

\[
\omega_t
=\frac{d\varphi}{dt}
=\frac{d\varphi/d\tau_{\rm int}}{dt/d\tau_{\rm int}}
\]

and the exact local length carrier

\[
\boxed{
\ell_\varphi
=\frac{c}{|\omega_t|}
=\frac{\hbar c}{E}.
}
\]

For a common nonzero rate over one regular hexahedral cell,

\[
\boxed{
h_H^{\rm phys}
=\ell_\varphi^2h_H
=\frac{\ell_\varphi^2}{6}I_3
=\frac{c^2}{6\omega_t^2}I_3.
}
\]

Let `vartheta^i` be a dimensionless local orientation coframe and define

\[
\boxed{
E^i=\frac{\ell_\varphi}{\sqrt6}\,\vartheta^i.
}
\]

Then

\[
\boxed{h_\perp=\sum_{i=1}^3E^i\otimes E^i}
\]

is positive and rank three wherever `0<ell_phi<infinity`.

The global identification `E^i=dX^i` is not inserted. It requires a separate integrability or connection theorem.

## 11. Exact anisotropic phase-rate extension

Allow each antipodal face pair to carry its own finite nonzero phase-clock length

\[
\ell_i=\frac{c}{|\omega_i|},
\qquad i=1,2,3.
\]

Physicalizing each pair before aggregation gives

\[
\boxed{
h_H^{\rm aniso}
=\frac1{12}
\begin{pmatrix}
\ell_2^2+\ell_3^2&0&0\\
0&\ell_1^2+\ell_3^2&0\\
0&0&\ell_1^2+\ell_2^2
\end{pmatrix}.
}
\]

Equivalently,

\[
\boxed{
h_{11}^{\rm aniso}
=\frac{c^2}{12}(\omega_2^{-2}+\omega_3^{-2})}
\]

with cyclic permutations for the remaining diagonal entries.

Every diagonal entry is positive for finite nonzero `omega_i`, so the rank remains three. The isotropic metric is recovered at `omega_1=omega_2=omega_3`.

This is an exact structural map from phase-clock anisotropy to local spatial metric anisotropy. The law governing the phase rates remains downstream.

## 12. Lorentzian assembly

Let the IDT time sector provide the nonvanishing temporal covector

\[
\Theta=c\,dt
\]

within the present clock-normalized gate. Then

\[
\boxed{
g_L=-\Theta\otimes\Theta+h_\perp}
\]

has exact local signature

\[
\boxed{(-,+,+,+).}
\]

At a point the tetrad

\[
\boxed{\{\Theta,E^1,E^2,E^3\}}
\]

gives a local Minkowski-normal form.

RF-02H therefore upgrades RF-G0: the previously conditional positive-rank-three spatial prerequisite now has an explicit local realization. The remaining geometric question is how these local tetrads glue and curve across neighboring cells.

## 13. Maxwell branch from the imaginary QGT sector

The Berry connection transforms under ray rephasing as

\[
|\psi\rangle\to e^{i\chi}|\psi\rangle
\quad\Longrightarrow\quad
\mathcal A\to\mathcal A+d\chi.
\]

Its curvature is

\[
\boxed{\mathcal F=d\mathcal A}
\]

and therefore

\[
\boxed{d\mathcal F=0.}
\]

For states depending on temporal and relational spatial coordinates,

\[
\mathcal F_{\tau i}
=\partial_\tau\mathcal A_i-\partial_i\mathcal A_\tau,
\qquad
\mathcal F_{ij}
=\partial_i\mathcal A_j-\partial_j\mathcal A_i.
\]

This supplies the homogeneous gauge-curvature structure. Physical electromagnetic normalization and sourced Maxwell dynamics remain separate action/source gates.

## 14. Phase-energy and photoelectric bridge

The calibrated phase rate gives

\[
\boxed{E=\hbar|\omega|.}
\]

The same relation controls bound transitions

\[
\hbar\omega_{mn}=E_m-E_n
\]

and the photoelectric threshold

\[
K_{\max}=\hbar\omega-\Phi.
\]

Thus phase rate, spectral transfer and material energy exchange meet in a single typed interface before stress-energy bookkeeping.

## 15. Physicalized Fubini--Study area

The FS area form is

\[
\boxed{
da_{FS}=\frac14\sin\theta\,d\theta\wedge d\varphi
}
\]

and

\[
\boxed{\mathcal F_B=\pm2\,da_{FS}.}
\]

The phase-clock physicalized area element is

\[
\boxed{
d\mathcal A_{\rm rel}
=\ell_\varphi^2da_{FS}
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

For a varying nonzero rate,

\[
\boxed{
\mathcal A_{\rm rel}^{(P)}
=\int_P\frac{c^2}{\omega(x)^2}\,da_{FS}(x).
}
\]

The formerly free length calibration is therefore replaced, under the present binding, by the local phase-clock scale.

## 16. Temporal information curvature

Let

\[
\mathcal I_\pi=D_{\rm KL}^{(2)}(p\|\pi),
\qquad
\mathcal J_\pi=(\ln2)\mathcal I_\pi
=24\pi\kappa\mathcal I_\pi.
\]

Define

\[
\boxed{\Xi_I=\frac{\mathcal J_\pi}{\mathcal A_{\rm rel}}.}
\]

For a constant-rate cell,

\[
\boxed{
\Xi_I^{(P)}
=\frac{\mathcal J_\pi}{a_{FS}^{(P)}}
\left(\frac{\omega_P}{c}\right)^2
}
\]

and therefore

\[
\boxed{[\Xi_I]=L^{-2}.}
\]

Using the TIR normalization,

\[
\boxed{
\Xi_I^{(P)}
=\frac{24\pi\kappa}{a_{FS}^{(P)}}
\mathcal I_\pi
\left(\frac{\omega_P}{c}\right)^2.
}
\]

For full CP1, `a_FS=pi`,

\[
\boxed{
\Xi_I^{(S^2)}
=24\kappa\mathcal I_\pi
\left(\frac{\omega}{c}\right)^2.
}
\]

Its exact temporal evolution on a constant-`a_FS` patch is

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

Information redistribution and phase-rate evolution therefore enter as separately typed channels.

## 17. Dynamic Lambda0 information-phase channel

RFC defines

\[
\boxed{\Lambda_I=\alpha_I\Xi_I}
\]

with dimensionless `alpha_I`. Hence for full CP1

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

The multi-sector candidate remains

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

## 18. Bianchi and action-level closure

For the phenomenological bookkeeping convention

\[
G_{\mu\nu}+\Lambda_0g_{\mu\nu}
=\frac{8\pi G}{c^4}T^{\rm visible}_{\mu\nu},
\]

the contracted Bianchi identity gives

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

For

\[
S_\Lambda
=-\frac{c^3}{8\pi G}
\int\sqrt{-g}\,\Lambda_0\,d^4x,
\]

algebraic metric dependence of `Lambda0` gives the corrected metric variation

\[
\boxed{
G_{\mu\nu}
+\Lambda_0g_{\mu\nu}
-2\frac{\partial\Lambda_0}{\partial g^{\mu\nu}}
=\frac{8\pi G}{c^4}T_{\mu\nu}.
}
\]

Derivative-dependent functionals require the corresponding Euler--Lagrange functional variation.

## 19. What RF-02H changes

Before RF-02H, the Lorentzian theorem required an unspecified positive rank-three spatial metric. RF-02H supplies one explicitly from the six-face hexahedral Bloch configuration:

\[
\boxed{
\mathcal H^\star
\to M_H=I_3/3
\to h_H=I_3/6
\to h_H^{\rm phys}=c^2I_3/(6\omega^2)
\to g_L.
}
\]

The spatial-rank problem is therefore locally closed for this declared configuration class.

The remaining obstacle is no longer the existence of three positive local directions. It is their differential geometry: coframe gluing, connection, curvature, temporal lapse dynamics and the source law.

## 20. Derivation frontier

The next geometry chain is

\[
\boxed{
\mathrm{RF\!-\!02H}
\to
\mathrm{RF\!-\!02I\ coframe\ gluing/integrability}
\to
\mathrm{RF\!-\!N0\ lapse/clock\ dynamics}
\to
\mathrm{tetrad\ connection/curvature}
\to
\mathrm{RF\!-\!N1\ Newton\ weak\ field}.
}
\]

In parallel,

\[
\boxed{
\mathrm{Berry\ connection}
\to
\mathrm{sourced\ Maxwell\ dynamics}
\to
\mathrm{phase-energy/photoelectric\ transfer}.
}
\]

The scalar closure path is

\[
\boxed{
\Xi_I
\to
\alpha_I
\to
\Lambda_0\text{ action variation}
\to
\mathrm{Einstein-Bianchi\ closure}.
}
\]

The programme has therefore moved from searching for a possible `3+1` carrier to deriving the differential dynamics of an explicit local tetrad. Target equations remain outside the premise set and will be admitted only through their corresponding derivation and limit receipts.
