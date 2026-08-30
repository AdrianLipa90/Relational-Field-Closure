# Einstein closure

Current gates:

1. canonical Lorentzian signature `(-,+,+,+)` — **PASS at RF-G0/RF-02H**;
2. torsion-free metric connection and curvature — **PASS at RF-02I**;
3. contracted Bianchi identity — **EXACT**;
4. AB-normalized electromagnetic curvature — **PASS at RF-M1**;
5. charge-projected Maxwell current — **PASS at RF-M4/RF-N1B2P with RF-E6 sign alignment**;
6. canonical energy-positive charged scalar/multiplet action — **PASS at RF-E6**;
7. charged-matter stress tensor and EM/matter exchange — **PASS at RF-E0/RF-E6**;
8. phase stress-energy / pressure firewall — **PASS at RF-E4**;
9. homogeneous on-shell massive scalar dust/factor-two gate — **PASS at RF-E5**;
10. exact amplitude/phase/potential scalar decomposition — **PASS at RF-E7**;
11. single-complex-scalar total matter tensor — **CLOSED at RF-E7**;
12. `mu_*` unit normalization — **PASS as convention map at RF-E6**;
13. Newton ↔ Einstein normalization `kappa_E=8piG/c^4` — **EXACT TRANSFER at RF-N1C/RF-E3**;
14. double-copy ↔ Einstein normalization `kappa_E=kappa_g^2/4` — **EXACT**;
15. Einstein–Hilbert prefactor `2/kappa_g^2=1/(2kappa_E)` — **PASS at RF-E3**;
16. dynamic `Lambda0` Bianchi transfer identity — **EXACT**;
17. TIR×IDT ADM four-coframe assembly — **PASS at RF-E8**;
18. minimal Cartan–Palatini bulk action selection — **CONDITIONAL EXACT at RF-E21**;
19. multispecies/additional matter composition — **OPEN**;
20. dynamic-`Lambda0` independent action and stability gate — **NEXT ACTION FRONTIER**.

## Canonical matter/source chain

RF-E6 fixes

\[
\boxed{\operatorname{signature}(g)=(-,+,+,+)}
\]

and

\[
\boxed{
\mathcal L_m=-(D_\mu\Psi)^\dagger D^\mu\Psi-U(\Psi).
}
\]

The Maxwell source is

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

## RF-E7 exact scalar composition

For

\[
\psi=Ae^{i\vartheta},
\qquad
q_\mu=\partial_\mu\vartheta+\frac q\hbar A_\mu^{EM},
\]

one has

\[
\boxed{
D_\mu\psi=e^{i\vartheta}(\partial_\mu A+iAq_\mu)
}
\]

and therefore

\[
\boxed{
(D_\mu\psi)^*D^\mu\psi=(\partial A)^2+A^2q^2.
}
\]

The mixed amplitude/phase terms cancel identically. The complete scalar stress tensor decomposes exactly as

\[
\boxed{
T_{\mu\nu}^{scalar}
=T_{\mu\nu}^{amp}
+T_{\mu\nu}^{phase}
+T_{\mu\nu}^{pot},
}
\]

where

\[
T_{\mu\nu}^{amp}
=2\partial_\mu A\partial_\nu A-g_{\mu\nu}(\partial A)^2,
\]

\[
T_{\mu\nu}^{phase}
=2A^2q_\mu q_\nu-g_{\mu\nu}A^2q^2,
\]

and

\[
T_{\mu\nu}^{pot}=-g_{\mu\nu}V.
\]

For the admitted single-scalar electromagnetic system the Einstein source ledger is

\[
\boxed{
T_{\mu\nu}^{source}
=T_{\mu\nu}^{EM}+T_{\mu\nu}^{scalar}.
}
\]

RF-E6 supplies the coupled on-shell conservation law

\[
\boxed{
\nabla^\mu T_{\mu\nu}^{source}=0.
}
\]

## Phase and amplitude limits

For homogeneous phase flow, RF-E4 is recovered:

\[
\boxed{
\varepsilon=K+V,
\qquad
p=K-V,
\qquad
\varepsilon+3p=4K-2V.
}
\]

For the homogeneous quadratic on-shell scalar, RF-E5 gives

\[
\boxed{V=K,\qquad p=0,\qquad \varepsilon=2K.}
\]

For a pure spatial amplitude gradient `partial_hat A=(0,g,0,0)`, RF-E7 gives

\[
\boxed{
T_{\hat a\hat b}^{amp}
=\operatorname{diag}(g^2,g^2,-g^2,-g^2).
}
\]

Thus the scalar ledger now contains phase energy, potential/rest energy and anisotropic amplitude-gradient stress in one exact tensor.

## Maxwell normalization

RF-E6 uses

\[
\boxed{\mu_*=1}
\]

in rationalized Heaviside–Lorentz natural units and

\[
\boxed{\mu_*=\mu_0}
\]

in SI, with

\[
\boxed{\alpha_{EM}=\frac{\mu_*e^2c}{4\pi\hbar}.}
\]

## Einstein normalization

RF-N1C/RF-E3 provide

\[
\boxed{\kappa_E=\frac{8\pi G}{c^4}}
\]

and in natural units

\[
\boxed{\kappa_E=8\pi G=\frac{\kappa_g^2}{4}.}
\]

## RF-E21 action-form selection

RF-E8 assembles the Lorentzian four-coframe from the TIR spatial coframe and IDT positive lapse. RF-E21 then restricts the local gravitational bulk action to the declared minimal Cartan class. Four-form degree counting and Lorentz/orientation covariance select

\[
\boxed{
\epsilon_{ABCD}E^A\wedge E^B\wedge R^{CD}
}
\]

for the curvature term and

\[
\boxed{
\epsilon_{ABCD}E^A\wedge E^B\wedge E^C\wedge E^D
}
\]

for the volume term. On the torsion-free branch the resulting Cartan–Palatini action is exactly the metric Einstein–Hilbert action used by RF-E3,

\[
\boxed{
S_g=\frac1{2\kappa_E}\int d^4x\sqrt{-g}(R-2\Lambda).
}
\]

RF-E3 remains the normalization owner; RF-E21 owns the conditional action-form selection.

## Validation

RF-E6 correction authority: PR #16, final run `33207702078`, job `98972879666`, **470/470 PASS**.

RF-E7 stacked gate: PR #17, tested commit `904d641948b48ca564dbbfb38a9442e7ca6ab078`, run `33207870117`, job `98973459240`, **479/479 PASS**.

RF-E21 reference target: `PASS_RF_E21_CARTAN_PALATINI_EINSTEIN_HILBERT_SELECTION`; exact-head CI receipt is owned by its feature PR.

## Current frontier

The Einstein–Hilbert bulk form now has an explicit conditional selection theorem from the TIR×IDT four-coframe rather than a free action-form insertion. The remaining matter-composition gate concerns additional independently admitted species/sectors. The next action-level Einstein gate is the independent dynamic-`Lambda0` action and stability closure, while the parallel coupling line continues through physical `G` universality and primitive promotion of the RF-E21 action-class assumptions.

**Current status:** `GEOMETRIC_SPINE_PRESENT / TIR_IDT_4COFRAME_PASS / CARTAN_PALATINI_EH_SELECTION_CONDITIONAL_EXACT / AB_MAXWELL_PRESENT / RF_E6_LORENTZIAN_ACTION_PASS / RF_E7_SINGLE_SCALAR_TOTAL_MATTER_PASS / MULTISPECIES_G_UNIVERSALITY_DYNAMIC_LAMBDA_AND_PRIMITIVE_ACTION_ASSUMPTION_PROMOTION_OPEN`.
