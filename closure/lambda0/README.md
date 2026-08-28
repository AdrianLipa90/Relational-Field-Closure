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

Validation authority: RF-L2 tested commit `38c9589608abe77bdcf05d46e997731ef5d6e430`, workflow run `33208242527`, job `98974734417`, **489/489 PASS**.

**Current status:** `RF_L1_TARGET_ADMITTED / RF_L2_ACTION_REALIZATION_PASS / STATIONARY_VACUUM_LIMIT_PASS / LOCAL_STABILITY_GATE_PASS / RFC_INVARIANT_POTENTIAL_RECONSTRUCTION_OPEN`.
