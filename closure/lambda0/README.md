# Dynamic Lambda0 closure

Current sequence:

1. RF-L1 admits the dynamic Einstein-side coordinate and dimensional target `[Lambda0]=L^-2`.
2. RF-L2 supplies an independent generally covariant scalar action and defines
   \[
   \boxed{\Lambda_0(x)=\Lambda_{ref}+\kappa_EU_L(\phi_L(x)).}
   \]
3. The dynamical carrier keeps its canonical kinetic stress explicitly on the source side.
4. On the scalar equation of motion, the RF-E0 transfer is recovered exactly:
   \[
   \boxed{\kappa_E\nabla^\mu T^{displayed}_{\mu\nu}=\nabla_\nu\Lambda_0.}
   \]
5. The stationary surface `grad(phi_L)=0`, `U_L'(phi_L0)=0` recovers a constant cosmological term.
6. Homogeneous dynamics obey
   \[
   \varepsilon_L=K_L+U_L,
   \qquad
   p_L=K_L-U_L,
   \]
   while spatial gradients carry explicit anisotropic kinetic stress.
7. Local linear stability is classified by
   \[
   m_L^2=U_L''(\phi_{L0}),
   \]
   with the non-tachyonic condition `m_L^2>=0`.
8. RF-L3 consumes the IDT inverse-area information scalar
   \[
   \Xi_I=\frac{\mathcal J_\pi}{\mathcal A_{rel}},
   \qquad [\Xi_I]=L^{-2},
   \]
   and closes the conditional functional reconstruction
   \[
   \boxed{\Delta\Lambda_I=\alpha_I\Xi_I,\qquad U_I=\frac{\alpha_I}{\kappa_E}\Xi_I.}
   \]
9. The exact action roundtrip is
   \[
   \boxed{\Lambda_{ref}+\kappa_EU_I=\Lambda_{ref}+\alpha_I\Xi_I.}
   \]
   The IDT oriented holonomy coordinate `tau_R` is transported unchanged through this scalar-magnitude reconstruction.
10. RF-L3 transfers the RF-L2 stationary/stability gates to `Xi_I(phi_L)` through
   \[
   U_I'=\frac{\alpha_I}{\kappa_E}\Xi_I',
   \qquad
   U_I''=\frac{\alpha_I}{\kappa_E}\Xi_I''.
   \]
   Physical calibration or derivation of `alpha_I`, the physical `phi_L <-> Xi_I` pullback and global/nonlinear stability remain downstream gates.

Validation authority inherited at the RF-L2 base: tested commit `38c9589608abe77bdcf05d46e997731ef5d6e430`, workflow run `33208242527`, job `98974734417`, **489/489 PASS**. RF-L3 carries its own reference gate and must receive an independent validation receipt before promotion.

**Current branch status:** `RF_L1_TARGET_ADMITTED / RF_L2_ACTION_REALIZATION_PASS / RF_L3_FUNCTIONAL_RECONSTRUCTION_PASS_CONDITIONAL / IDT_XI_I_HOLONOMY_PRESERVED / ALPHA_I_CALIBRATION_OPEN`.
