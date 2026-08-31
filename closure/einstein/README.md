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
19. dynamic-`Lambda0` independent scalar action / stability — **PASS at RF-L2**;
20. information-scalar potential reconstruction — **PASS CONDITIONAL at RF-L3**;
21. local Fisher normalization / canonical pullback — **PASS at RF-L4/RF-L4A**;
22. Shannon–Onsager Temporal Wave graph/operator bridge — **PASS at RF-L5**;
23. premetric-to-physical light-cone and mass-frequency calibration firewall — **EXACT GIVEN CALIBRATION at RF-L5A**;
24. tetra/phase-clock mass-scale composition — **EXACT SCALE COMPOSITION at RF-E20; physical bindings OPEN**;
25. multispecies/additional matter composition — **OPEN**;
26. primitive promotion of the RF-E21 action-class assumptions — **OPEN**.

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

## Dynamic Lambda / information-scale chain

The action-level variable vacuum sector is already carried by RF-L2,

\[
\boxed{\Lambda_0=\Lambda_{ref}+\kappa_EU_L(\phi_L),}
\]

with exact on-shell Bianchi transfer. RF-L3 through RF-L5A then connect the IDT information curvature and Temporal Wave coordinates to the physical scalar chart. The current exact calibration identities include

\[
\boxed{m_I^2=\frac{\alpha_I}{\kappa_E}}
\]

and

\[
\boxed{
M_{eff}\frac{\Gamma_x^2}{\Gamma_t^2}=c^2,
\qquad
\mu_\lambda^2=\Gamma_t^2c^2m_I^2.
}
\]

RF-E20 adds the tetra/phase-clock scale-composition equation

\[
\boxed{
r_\alpha q_s^3
=r_m\mu_\varphi\frac{9\sqrt3\pi}{8}.
}
\]

These relations move the active frontier from action existence to physical scale binding and curved variable-lapse propagation.

## Validation

RF-E6 correction authority: PR #16, final run `33207702078`, job `98972879666`, **470/470 PASS**.

RF-E7 stacked gate: PR #17, tested commit `904d641948b48ca564dbbfb38a9442e7ca6ab078`, run `33207870117`, job `98973459240`, **479/479 PASS**.

RF-L2 authority: tested commit `38c9589608abe77bdcf05d46e997731ef5d6e430`, run `33208242527`, job `98974734417`, **489/489 PASS**.

RF-L4 authority: tested head `99621c0848b36ef93cd6c41e9f3d88be3023cb1a`, run `33245133095`, job `99081186401`, **522/522 PASS**.

RF-L4A authority: tested head `7fcedd30a1ba59ae82750eb6b5f89b9e3288d162`, run `33245318290`, job `99081667619`, **543/543 PASS**.

RF-L5 graph/operator authority: tested head `ceac4269a9944e1a17d3a9321ab5d7975a4ce15d`, run `33245513490`, job `99082170070`, **561/561 PASS**.

RF-E21 first exact-head regression: commit `225327b4d9c74161ab0bc5ed3c1a229a0b246b66`, run `33326298999`, job `99296909792`, **SUCCESS**. The final synchronized feature head requires its own exact-head receipt.

## Current frontier

The Einstein–Hilbert bulk form now has an explicit conditional selection theorem from the TIR×IDT four-coframe. The dynamic information-vacuum action and its local information-field reconstruction are already present downstream. The active closure coordinates are now the RF-L5A variable-`N_R` curved covariant extension, independent physical phase-clock spectral matching, spatial cell/length calibration, RF-E20 physical scale bindings, multispecies matter composition, physical `G` universality, global/nonlinear information-field stability, and primitive promotion of the RF-E21 action-class assumptions.

**Current status:** `GEOMETRIC_SPINE_PRESENT / TIR_IDT_4COFRAME_PASS / CARTAN_PALATINI_EH_SELECTION_CONDITIONAL_EXACT / ADM_CONSTRAINT_EVOLUTION_BIANCHI_PRESENT / RF_L2_DYNAMIC_ACTION_PASS / RF_L3_L4_L4A_INFORMATION_PULLBACK_PRESENT / RF_L5_GRAPH_OPERATOR_PASS / RF_L5A_PHYSICAL_CALIBRATION_FIREWALL_PRESENT / RF_E20_SCALE_COMPOSITION_PRESENT / PHYSICAL_SCALE_BINDINGS_VARIABLE_LAPSE_COVARIANT_EXTENSION_MULTISPECIES_G_UNIVERSALITY_GLOBAL_STABILITY_AND_PRIMITIVE_ACTION_PROMOTION_OPEN`.
