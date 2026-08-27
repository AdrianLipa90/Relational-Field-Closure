# Relational Field Closure

**Status:** `EARLY_FORMALISM / EXACT_QGT_LORENTZ_AND_PHASE_CLOCK_CURVATURE_RESULTS / PHYSICAL_CLOSURE_OPEN`

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

Given a nonvanishing IDT temporal one-form `Theta` and a positive rank-three spatial metric `h_perp` on `ker(Theta)`,

\[
\boxed{g_L=-\Theta\otimes\Theta+h_\perp}
\]

has exact signature

\[
\boxed{(-,+,+,+)}.
\]

## Phase-clock length and physicalized projective area

IDT now supplies the local phase-clock length carrier

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

For a constant-rate cell `P`,

\[
\boxed{
\mathcal A_{\rm rel}^{(P)}
=\frac{c^2}{\omega_P^2}a_{FS}^{(P)}.
}
\]

Thus the former scalar area calibration is replaced, under this binding, by the local dynamical scale

\[
\boxed{
\ell_R(x)\equiv\ell_\varphi(x)=\frac{c}{|\omega(x)|}.
}
\]

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

1. derive a positive rank-three spatial metric from the hexahedral/higher refinement hierarchy;
2. promote or falsify the phase-clock physical metric binding `ds_rel^2 = ell_phi^2 ds_FS^2`;
3. handle phase-rate-zero patches and nonuniform refinement convergence;
4. determine or bound `alpha_I`;
5. classify metric dependence of the physicalized area and complete action variation;
6. derive lapse/shift dynamics and the Newton weak-field limit;
7. close sourced Maxwell dynamics;
8. close dynamic `Lambda0` and Einstein-Bianchi dynamics.

## Claim firewall

Target equations remain validation targets. A closure is promoted only after upstream provenance, covariance, dimensional and physical-limit gates pass. The author/formalism may suggest unified field emergence, yet does not state that implication as an established result before those gates pass.
