# RF-M1 / RF-E0 — Aharonov–Bohm → Maxwell → Einstein dependency bridge

Status: `HOMOGENEOUS_MAXWELL_EXACT / SOURCED_MAXWELL_CONDITIONAL / EINSTEIN_BIANCHI_BRIDGE_PRESENT / COUPLING_AND_TOTAL_SOURCE_BINDING_OPEN`

```text
physical Aharonov–Bohm phase
  phi_AB[C] = (q/hbar) integral_C A
  |
  v
RF-M1 physical AB connection
  a_AB = (q/hbar) A
  A = (hbar/q) a_AB       [q != 0]
  |
  v
local EM curvature
  F = dA = (hbar/q) d a_AB
  |
  +--> Stokes / Wilson-loop flux
  |      phi_AB[partial Sigma] = (q/hbar) integral_Sigma F
  |
  +--> homogeneous Maxwell
  |      dF = 0
  |      nabla_[a F_bc] = 0
  |
  v
admitted lowest-derivative Abelian action
  S_EM = integral sqrt(-g)[-F^2/(4 mu_*) - J.A]
  |
  +--> sourced Maxwell
  |      nabla_mu F^(mu nu) = mu_* J^nu
  |
  +--> current conservation
  |
  +--> metric variation
         T_EM(mu,nu)
         |
         v
RF-E0 EM/matter exchange
  nabla^mu T_EM(mu,nu)     = -F_(nu lambda) J^lambda
  nabla^mu T_matter(mu,nu) = +F_(nu lambda) J^lambda
  ---------------------------------------------------
  nabla^mu (T_EM + T_matter)_(mu,nu) = 0
         |
         v
RFC geometric spine
  RF-02H rank-3 spatial metric
    -> RF-G0 Lorentzian signature
    -> RF-02I metric connection / curvature
    -> contracted Bianchi identity
         |
         v
Einstein source gate
  G_mu_nu + Lambda g_mu_nu = kappa_E T_total(mu,nu)
  kappa_E = 8 pi G / c^4 only after RF-N1C fixes G
         |
         +--> constant Lambda: nabla^mu T_total(mu,nu)=0
         |
         +--> dynamic Lambda0:
                kappa_E nabla^mu T_total(mu,nu)=nabla_nu Lambda0
                T_Lambda(mu,nu)=-(Lambda0/kappa_E)g_mu_nu
                nabla^mu(T_total+T_Lambda)_(mu,nu)=0
```

## Exact/conditional firewall

### Exact structural layer

For an admitted nonzero probe charge and regular local gauge patch:

\[
\mathfrak a_{AB}=\frac q\hbar A,
\qquad
F=\frac\hbar q d\mathfrak a_{AB}=dA,
\qquad
\boxed{dF=0}.
\]

The AB coupling therefore fixes the potential normalization on this branch and removes the independent `alpha_A` rescaling used by the older generic Berry-to-Maxwell candidate.

For the admitted RFC Levi-Civita geometry:

\[
\boxed{\nabla^\mu G_{\mu\nu}=0},
\qquad
\boxed{\nabla^\mu g_{\mu\nu}=0}.
\]

For a dynamic scalar closure,

\[
G_{\mu\nu}+\Lambda_0 g_{\mu\nu}=\kappa_E T^{total}_{\mu\nu}
\]

implies exactly

\[
\boxed{\kappa_E\nabla^\mu T^{total}_{\mu\nu}=\nabla_\nu\Lambda_0}.
\]

### Conditional action layer

After admitting the local Maxwell action and the charged-matter exchange action:

\[
\nabla_\mu F^{\mu\nu}=\mu_*J^\nu,
\]

\[
T^{EM}_{\mu\nu}
=\frac1{\mu_*}
\left(F_{\mu\alpha}F_\nu{}^\alpha-rac14g_{\mu\nu}F^2\right),
\]

and EM/matter exchange closes to a conserved combined source.

## Current open promotion coordinates

1. bind the RFC/IDT conserved current to physical electromagnetic current:
   \[
   J_Q^\mu\stackrel{?}{\longleftrightarrow}J_{EM}^\mu;
   \]
2. derive or empirically bind the vacuum field normalization `mu_*`;
3. complete the admitted matter stress-energy action;
4. finish RF-N1C and determine `G`, hence `kappa_E`;
5. derive the dynamic `Lambda0` sector at action level;
6. run the full Einstein field-equation and unified-limit audit.

## Validation snapshot

On branch `feat/rfm1-ab-maxwell-holonomy-v0.1`:

- RF-M1 Maxwell-only checkpoint after the floating-point test correction: `94 passed, 0 failed`;
- RF-M1 + RF-E0 checkpoint: `99 passed, 0 failed`.

The initial RF-M1 run produced `93 passed, 1 failed`; the sole failure was an exact Python float-list comparison (`-0.6` versus `-0.6000000000000001`). It was corrected to tolerance-aware comparison before the green checkpoints above.
