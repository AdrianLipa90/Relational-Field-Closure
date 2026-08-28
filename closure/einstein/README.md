# Einstein closure

Current gates:

1. Lorentzian metric candidate with canonical signature `(-,+,+,+)` — **PASS at RF-G0/RF-02H**;
2. torsion-free metric connection and local curvature — **PASS at RF-02I on the admitted coframe sector**;
3. contracted Bianchi identity — **EXACT GEOMETRIC IDENTITY**;
4. AB-normalized electromagnetic curvature — **PASS at RF-M1**;
5. charge-projected Maxwell current — **PASS algebraically at RF-M4/RF-N1B2P, with RF-E6 sign alignment**;
6. energy-positive charged scalar/multiplet action under `(-,+,+,+)` — **PASS at RF-E6**;
7. explicit charged-matter stress-energy tensor — **PASS at RF-E6 under the admitted action**;
8. EM/matter Lorentz-force exchange cancellation — **PASS at RF-E0/RF-E6**;
9. phase stress-energy / pressure firewall — **PASS at RF-E4 after canonical-signature transfer**;
10. homogeneous on-shell massive scalar dust/factor-two gate — **PASS at RF-E5 after canonical-signature transfer**;
11. `mu_*` unit normalization — **PASS as an exact convention map at RF-E6**;
12. Newton ↔ Einstein normalization `kappa_E=8piG/c^4` — **EXACT TRANSFER at RF-N1C/RF-E3**;
13. double-copy ↔ Einstein normalization `kappa_E=kappa_g^2/4` — **EXACT ALGEBRAIC TRANSFER**;
14. Einstein–Hilbert prefactor `2/kappa_g^2=1/(2kappa_E)` — **PASS at RF-E3**;
15. dynamic `Lambda0` transfer identity — **EXACT BIANCHI/EXCHANGE IDENTITY**;
16. total physical matter stress-energy composition across all admitted sectors — **OPEN**;
17. dynamic-`Lambda0` independent action and stability audit — **OPEN**.

## Canonical matter/source chain

RF-E6 makes the Einstein-facing action convention explicit:

\[
\boxed{\operatorname{signature}(g)=(-,+,+,+)}
\]

and

\[
\boxed{
\mathcal L_m
=-(D_\mu\Psi)^\dagger D^\mu\Psi-U(\Psi).
}
\]

The charge-projected source is

\[
\boxed{
J_{EM}^\mu=\frac1\hbar\mathcal J_Q^\mu
=\frac1\hbar\Pi_Q[J_{RFC}]^\mu.
}
\]

For one charge eigenvalue,

\[
\boxed{J_{EM}^\mu=(q/\hbar)J_{RFC,\vartheta}^\mu.}
\]

The charged-matter stress tensor is

\[
\boxed{
T_{\mu\nu}^{matter}
=(D_\mu\Psi)^\dagger D_\nu\Psi
+(D_\nu\Psi)^\dagger D_\mu\Psi
+g_{\mu\nu}\mathcal L_m.
}
\]

Together with the Maxwell tensor,

\[
\boxed{
\nabla^\mu(T^{EM}+T^{matter})_{\mu\nu}=0
}
\]

on the admitted matter equations.

## Phase-sector stress structure

RF-E4 gives, for `K=A^2 r_n^2`,

\[
\boxed{
\varepsilon=K+V,
\qquad
p=K-V,
\qquad
\varepsilon+3p=4K-2V.
}
\]

RF-E5 gives the homogeneous quadratic on-shell surface

\[
\boxed{V=K,\qquad p=0,\qquad \varepsilon=2K.}
\]

The phase-kinetic energy per Noether carrier remains `omega/2`, while total on-shell energy per carrier is `omega`.

## Maxwell normalization

RF-E6 binds

\[
\boxed{\mu_*=1}
\]

in rationalized Heaviside–Lorentz natural units and

\[
\boxed{\mu_*=\mu_0}
\]

in SI, with

\[
\boxed{
\alpha_{EM}=\frac{\mu_*e^2c}{4\pi\hbar}.
}
\]

Thus an independently frozen electromagnetic coupling fixes the numerical field normalization in the selected unit convention.

## Einstein normalization

RF-N1C/RF-E3 provide

\[
\boxed{
\kappa_E=\frac{8\pi G}{c^4}
}
\]

and in natural units

\[
\boxed{
\kappa_E=8\pi G=\frac{\kappa_g^2}{4}.
}
\]

The Einstein–Hilbert action is

\[
\boxed{
S_{EH}
=\frac{1}{2\kappa_E}\int d^4x\sqrt{-g}\,R
=\frac{2}{\kappa_g^2}\int d^4x\sqrt{-g}\,R.
}
\]

## Current frontier

The immediate Einstein-facing frontier is now the **total-matter composition gate**: combine the already explicit phase/charged sector with amplitude-gradient, potential/rest and any additional admitted matter sectors under one stress-energy ledger, then test cross-system source universality. The independent dynamic-`Lambda0` action remains the following action gate.

**Current status:** `GEOMETRIC_SPINE_PRESENT / AB_MAXWELL_PRESENT / RF_E6_LORENTZIAN_MATTER_ACTION_PRESENT / EXPLICIT_CHARGED_MATTER_T_PRESENT / RFE4_RFE5_SIGNATURE_ALIGNED / MU_STAR_UNIT_BINDING_AVAILABLE / TOTAL_MATTER_AND_DYNAMIC_LAMBDA_PROMOTION_OPEN`.
