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
   and closes the functional reconstruction
   \[
   \boxed{\Delta\Lambda_I=\alpha_I\Xi_I,\qquad U_I=\frac{\alpha_I}{\kappa_E}\Xi_I.}
   \]
9. RF-L4 introduces an admitted constant information-curvature baseline `Xi_star` and
   \[
   \bar\Xi_I=\Xi_I-\Xi_\star\ge0,
   \qquad
   \boxed{\Lambda_\star=\Lambda_{ref}+\alpha_I\Xi_\star.}
   \]
10. In four-dimensional natural units, RF-L4 defines
   \[
   \boxed{\phi_I=\beta_I\sqrt{\bar\Xi_I},\qquad \beta_I>0,}
   \]
   giving
   \[
   \boxed{\bar\Xi_I=\phi_I^2/\beta_I^2.}
   \]
11. The RF-L3 potential is therefore quadratic:
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
12. RF-L4 induces the information-curvature chart coefficient
   \[
   \boxed{Z_I^{RFC}(\Xi_I)=\frac{\beta_I^2}{4(\Xi_I-\Xi_\star)}}.
   \]
13. RF-L4A evaluates the local stationary-reference geometry of the natural-log Shannon relative information
   \[
   \mathcal J_\pi=\sum_a p_a\ln\frac{p_a}{\pi_a}.
   \]
   For `p=pi+delta p`, `sum(delta p)=0`,
   \[
   \boxed{
   \mathcal J_\pi
   =\frac12\sum_a\frac{(\delta p_a)^2}{\pi_a}
   +O(\|\delta p\|^3).
   }
   \]
   The Hessian is the local Fisher metric `diag(1/pi_a)` on the simplex tangent space.
14. Let
   \[
   s_F^2=\sum_a\frac{(\delta p_a)^2}{\pi_a},
   \qquad
   \mathcal A_{rel}=\mathcal A_\star+O(\|\delta p\|).
   \]
   Since `J_pi=O(delta p^2)`, smooth first-order area variation enters `Xi_I=J_pi/A_rel` only at cubic order, so
   \[
   \boxed{
   \Xi_I=\frac{s_F^2}{2\mathcal A_\star}+O(\|\delta p\|^3).
   }
   \]
15. Define the local Fisher radial scalar
   \[
   \phi_F=\frac{s_F}{\sqrt{\mathcal A_\star}}.
   \]
   Matching RF-L4 `phi_I=beta_I sqrt(Xi_I)` to the leading Fisher coordinate fixes
   \[
   \boxed{\beta_I=\sqrt2}
   \]
   in the local stationary-reference Fisher sector. Hence
   \[
   \boxed{\phi_I=\sqrt{2\Xi_I}=\phi_F+O(\|\delta p\|^2).}
   \]
16. The locally normalized kinetic coefficient and RFC mass relation become
   \[
   \boxed{Z_I^{RFC}(\Xi_I)=\frac1{2\Xi_I}},
   \qquad
   \boxed{m_I^2=\frac{\alpha_I}{\kappa_E}},
   \qquad
   \boxed{\alpha_I=\kappa_E m_I^2}.
   \]
17. For the IDT full CP1/Bloch-sphere constant-rate sector,
   \[
   \boxed{
   \phi_I^{(S^2)}
   =\sqrt{48\kappa\mathcal I_\pi}\frac{|\omega|}{c}
   =\sqrt{\frac{2\ln2}{\pi}\mathcal I_\pi}\frac{|\omega|}{c},
   \qquad
   \kappa=\frac{\ln2}{24\pi}.
   }
   \]
18. RF-L5 uses the exact IDT 01D uniform-equilibrium identity
   \[
   \boxed{
   G_u^{(2)}(u)=\frac{\ln2}{N_s}K_0,
   \qquad
   K_0=\frac{N_s}{\ln2}G_u^{(2)}(u),
   }
   \]
   where 02B identifies `K0` as the untwisted Temporal Wave relational-mobility stiffness.
19. IDT 02B differentiates with respect to the ordering coordinate `lambda`. RF-L5 therefore types the homogeneous graph gap as a premetric coefficient `mu_lambda^2` and writes
   \[
   \boxed{
   \frac{d^2\phi_I}{d\lambda^2}
   +(K_0+\mu_\lambda^2I)\phi_I=0.
   }
   \]
20. The same premetric equation written directly through the Shannon response is
   \[
   \boxed{
   \frac{d^2\phi_I}{d\lambda^2}
   +\left[
   \frac{N_s}{\ln2}G_u^{(2)}(u)
   +\mu_\lambda^2I
   \right]\phi_I=0.
   }
   \]
21. For `K0 v_r=lambda_r v_r`, the ordering-coordinate modal spectrum is
   \[
   \boxed{
   \omega_{\lambda,r}^2=\lambda_r+\mu_\lambda^2.
   }
   \]
   The connected-graph constant mode obeys
   \[
   \boxed{\omega_{\lambda,0}^2=\mu_\lambda^2.}
   \]
22. IDT 02C supplies the premetric long-wave coefficient `M_eff`, giving
   \[
   \boxed{
   \partial_\lambda^2\phi_I
   -M_{eff}\partial_\xi^2\phi_I
   +\mu_\lambda^2\phi_I=0.
   }
   \]
23. RF-L5A introduces the local affine calibration
   \[
   t-t_\star=\Gamma_t(\lambda-\lambda_\star),
   \qquad
   X-X_\star=\Gamma_x(\xi-\xi_\star),
   \]
   and derives
   \[
   \boxed{
   c_{cal}^2=M_{eff}\frac{\Gamma_x^2}{\Gamma_t^2},
   \qquad
   \Omega_m^2=\frac{\mu_\lambda^2}{\Gamma_t^2}.
   }
   \]
24. Matching the locally flat RF-L2 Lorentzian scalar equation gives the exact calibration firewall
   \[
   \boxed{
   M_{eff}\frac{\Gamma_x^2}{\Gamma_t^2}=c^2,
   \qquad
   \mu_\lambda^2
   =\Gamma_t^2c^2m_I^2
   =\Gamma_t^2c^2\frac{\alpha_I}{\kappa_E}.
   }
   \]
25. IDT 05C fixes the local reference-clock factor as
   \[
   \boxed{
   \Gamma_t=\frac{dt}{d\lambda}=T_{ref}\phi_{ref}>0.
   }
   \]
   If a premetric cell width `h` receives physical width `L_h`, then
   \[
   \Gamma_x=L_h/h
   \]
   and the light-cone calibration becomes
   \[
   \boxed{
   \frac{L_h}{hT_{ref}\phi_{ref}}
   =\frac{c}{\sqrt{M_{eff}}}.
   }
   \]
26. The physical homogeneous Klein–Gordon frequency is therefore
   \[
   \boxed{
   (\omega_t^{KG})^2
   =c^2m_I^2
   =c^2\frac{\alpha_I}{\kappa_E},
   \qquad
   \omega_t^{KG}=\omega_{\lambda,0}/\Gamma_t.
   }
   \]
   A downstream scale gate may compare this quantity with an independently admitted IDT phase-clock spectral line after common physical-time calibration.

Validation authority:

- RF-L2 tested commit `38c9589608abe77bdcf05d46e997731ef5d6e430`, workflow run `33208242527`, job `98974734417`, **489/489 PASS**.
- RF-L3 PR #19 tested head `2666ced59b4210e1afb2eb2c98ba61f09e674d98`, workflow run `33243796567`, **SUCCESS**.
- RF-L4 PR #20 tested head `99621c0848b36ef93cd6c41e9f3d88be3023cb1a`, workflow run `33245133095`, job `99081186401`, **522/522 PASS**.
- RF-L4A PR #21 tested head `7fcedd30a1ba59ae82750eb6b5f89b9e3288d162`, workflow run `33245318290`, job `99081667619`, **543/543 PASS**.
- RF-L5 PR #22 tested head `ceac4269a9944e1a17d3a9321ab5d7975a4ce15d`, workflow run `33245513490`, job `99082170070`, **561/561 PASS** for the graph/operator algebraic suite.
- RF-L5A carries the physical-dimensional correction and requires its independent workflow receipt before promotion.

**Current branch status:** `RF_L1_TARGET_ADMITTED / RF_L2_ACTION_REALIZATION_PASS / RF_L3_FUNCTIONAL_RECONSTRUCTION_PASS / RF_L4_CANONICAL_PULLBACK_522_OF_522_PASS / RF_L4A_LOCAL_FISHER_NORMALIZATION_543_OF_543_PASS / RF_L5_GRAPH_OPERATOR_ALGEBRA_561_OF_561_PASS / RF_L5A_PREMETRIC_DIMENSIONAL_FIREWALL_CANDIDATE / IDT_XI_I_HOLONOMY_PRESERVED / AFFINE_LIGHTCONE_RATIO_DERIVED / PHASE_CLOCK_MASS_SCALE_OPEN / VARIABLE_LAPSE_CURVED_COVARIANT_GATE_OPEN / GLOBAL_INFORMATION_GEODESIC_EXTENSION_OPEN`.
