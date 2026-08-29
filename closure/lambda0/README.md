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
9. RF-L4 introduces an admitted constant information-curvature baseline `Xi_star` and the dynamic coordinate
   \[
   \bar\Xi_I=\Xi_I-\Xi_\star\ge0.
   \]
   The corresponding constant Einstein-side coordinate is
   \[
   \boxed{\Lambda_\star=\Lambda_{ref}+\alpha_I\Xi_\star.}
   \]
10. In four-dimensional natural units, RF-L4 defines the canonical-dimension scalar coordinate
   \[
   \boxed{\phi_I=\beta_I\sqrt{\bar\Xi_I},\qquad \beta_I>0,}
   \]
   so `[phi_I]=L^-1` and
   \[
   \boxed{\bar\Xi_I=\phi_I^2/\beta_I^2.}
   \]
11. The RF-L3 potential becomes exactly quadratic:
   \[
   \boxed{
   U_I(\phi_I)
   =\frac{\alpha_I}{\kappa_E\beta_I^2}\phi_I^2
   =\frac12m_I^2\phi_I^2,
   }
   \]
   with
   \[
   \boxed{m_I^2=\frac{2\alpha_I}{\kappa_E\beta_I^2}.}
   \]
12. The canonical kinetic term induces the information-curvature chart coefficient
   \[
   \boxed{Z_I^{RFC}(\Xi_I)=\frac{\beta_I^2}{4(\Xi_I-\Xi_\star)}}
   \]
   for `Xi_I>Xi_star`.
13. IDT 01K gives the full-Bloch-sphere specialization
   \[
   \boxed{
   \phi_I^{(S^2)}
   =\beta_I\sqrt{24\kappa\mathcal I_\pi}\frac{|\omega|}{c},
   \qquad
   \kappa=\frac{\ln2}{24\pi}.
   }
   \]
14. The next cross-repository promotion coordinate is the reduction of the IDT 01D Shannon–Onsager tangent metric along the admitted 01K trajectory and the equality test
   \[
   \boxed{Z_I^{IDT}(\Xi_I)=Z_I^{RFC}(\Xi_I).}
   \]
   This is the current kinetic-closure frontier for fixing `beta_I` from upstream information dynamics.

Validation authority:

- RF-L2 tested commit `38c9589608abe77bdcf05d46e997731ef5d6e430`, workflow run `33208242527`, job `98974734417`, **489/489 PASS**.
- RF-L3 PR #19 tested head `2666ced59b4210e1afb2eb2c98ba61f09e674d98`, workflow run `33243796567`, **SUCCESS**.
- RF-L4 carries its own reference gate and requires its independent workflow receipt before promotion.

**Current branch status:** `RF_L1_TARGET_ADMITTED / RF_L2_ACTION_REALIZATION_PASS / RF_L3_FUNCTIONAL_RECONSTRUCTION_PASS / RF_L4_SQRT_CANONICAL_PULLBACK_EXACT_ON_ADMITTED_BRANCH / IDT_XI_I_HOLONOMY_PRESERVED / IDT_01D_KINETIC_METRIC_MATCH_OPEN / BETA_I_AND_ALPHA_I_CALIBRATION_OPEN`.
