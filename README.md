# Relational Field Closure

**Status:** `EARLY_FORMALISM / EXACT_QGT_LORENTZ_PHASE_CLOCK_AND_HEXAHEDRAL_RANK3_RESULTS / PHYSICAL_CLOSURE_OPEN`

Relational Field Closure (RFC) is a derivation-first research repository testing whether Maxwell, Newton and Einstein field structures can be obtained from three pinned upstream theories:

1. **The Fundamental Theory of Informational Relations (TIR)**
2. **Secret of a Half**
3. **Informational Dynamics of Time (IDT)**

The repository carries dynamic `Lambda0` as the candidate scalar closure entering the Einstein sector.

## Current structural core

For a projective state,

\[
Q_{\mu\nu}=\langle D_\mu\psi|D_\nu\psi\rangle,
\qquad
\Re Q=g^{FS},
\qquad
2\Im Q=\Omega.
\]

A single `CP1` pullback has rank at most two, so the rank-three spatial sector is assigned to the multi-state/polyhedral refinement gate.

## RF-02H hexahedral rank-three local metric

Represent a regular hexahedral cell by its six oriented face-normal Bloch rays,

\[
\boxed{
\mathcal H^\star=\{\pm e_1,\pm e_2,\pm e_3\}.
}
\]

With equal weights, their Bloch second moment is

\[
\boxed{M_H=\frac13I_3.}
\]

The aggregate Fubini--Study orbit metric is therefore

\[
\boxed{
h_H=\frac14(I_3-M_H)=\frac16I_3.}
\]

Hence

\[
\boxed{
\operatorname{rank}h_H=3,
\qquad
\det h_H=\frac1{216},
\qquad
\operatorname{cond}(h_H)=1.
}
\]

The six dual Bloch points tessellate the sphere into eight octants. The exact refinement invariants include

\[
\boxed{
\chi=2,
\qquad
\sum_f a_{FS}(f)=\pi,
\qquad
\int_{S^2}F_B=\pm2\pi,
\qquad
c_1=\pm1.
}
\]

Each octant carries

\[
\boxed{
a_{FS}=\frac\pi8,
\qquad
|\gamma_B|=\frac\pi4.
}
\]

## Lorentzian assembly

Given the IDT temporal one-form `Theta` and the RF-02H positive rank-three spatial metric,

\[
\boxed{g_L=-\Theta\otimes\Theta+h_\perp}
\]

has exact signature

\[
\boxed{(-,+,+,+)}.
\]

RF-02H therefore satisfies the local positive-rank-three prerequisite of RF-G0. The next geometric gate is the gluing/integrability of the local spatial coframe across neighboring cells.

## Phase-clock length and physicalized projective geometry

IDT supplies the local phase-clock length carrier

\[
\boxed{
\ell_\varphi
=\frac{c}{|\omega|}
=\frac{\hbar c}{E},
\qquad
\omega=\frac{d\varphi/d\tau_{\rm int}}{dt/d\tau_{\rm int}}.
}
\]

TIR binds this to the dimensionless Fubini--Study geometry through

\[
\boxed{
 ds^2_{\rm rel}=\ell_\varphi^2ds^2_{FS},
\qquad
 d\mathcal A_{\rm rel}=\ell_\varphi^2da_{FS}.
}
\]

For the regular RF-02H cell with a common local phase rate,

\[
\boxed{
h_H^{\rm phys}
=\frac{\ell_\varphi^2}{6}I_3
=\frac{c^2}{6\omega^2}I_3.
}
\]

For three paired local rates, `ell_i=c/|omega_i|`, the exact anisotropic extension is

\[
\boxed{
h_H^{\rm aniso}
=\frac1{12}
\operatorname{diag}
(\ell_2^2+\ell_3^2,\ell_1^2+\ell_3^2,\ell_1^2+\ell_2^2).
}
\]

This gives a typed local map from phase-clock anisotropy to spatial metric anisotropy.

## Temporal information curvature

With

\[
\mathcal J_\pi=(\ln2)\mathcal I_\pi
=24\pi\kappa\mathcal I_\pi,
\]

RFC uses

\[
\boxed{
\Xi_I=\frac{\mathcal J_\pi}{\mathcal A_{\rm rel}},
\qquad [\Xi_I]=L^{-2}.
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
=\frac{24\pi\kappa}{a_{FS}^{(P)}}
\mathcal I_\pi
\left(\frac{\omega_P}{c}\right)^2.
}
\]

For the full CP1/Bloch sphere, `a_FS = pi`, giving

\[
\boxed{
\Xi_I^{(S^2)}
=24\kappa\mathcal I_\pi
\left(\frac{\omega}{c}\right)^2.
}
\]

The temporal derivative on a constant-`a_FS` patch is

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

## Dynamic Lambda0 information-phase channel

RFC defines

\[
\boxed{\Lambda_I=\alpha_I\Xi_I},
\]

with dimensionless `alpha_I`. For the full CP1/Bloch sphere,

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

The general scalar basis remains

\[
\Lambda_0
=\Lambda_{\rm vac}
+\Lambda_I
+\sum_r\alpha_r\mathcal S_r.
\]

## Action-level correction gate

For algebraic metric dependence of `Lambda0`, metric variation gives

\[
\boxed{
G_{\mu\nu}
+\Lambda_0g_{\mu\nu}
-2\frac{\partial\Lambda_0}{\partial g^{\mu\nu}}
=\frac{8\pi G}{c^4}T_{\mu\nu}.
}
\]

The physicalized FS/Berry area therefore has a dedicated metric-dependence gate before Einstein closure.

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

1. `RF-02I`: derive hexahedral coframe gluing/refinement and determine the integrability/connection structure;
2. `RF-N0`: derive local lapse/clock-rate dynamics from IDT rather than fixing the temporal leg;
3. derive the connection and curvature of the physicalized tetrad;
4. construct the weak-field variables from those derived objects and run the Newton/Poisson limit gate;
5. handle phase-rate-zero patches and nonuniform refinement convergence;
6. determine or bound `alpha_I`;
7. close sourced Maxwell dynamics;
8. close dynamic `Lambda0` and Einstein-Bianchi dynamics.

## Claim firewall

Target equations remain validation targets. A closure is promoted only after upstream provenance, covariance, dimensional and physical-limit gates pass. The author/formalism may suggest unified field emergence, yet does not state that implication as an established result before those gates pass.
