# RF-M1 / RF-E0 — Aharonov–Bohm → Maxwell → Einstein dependency bridge

Status: `HOMOGENEOUS_MAXWELL_EXACT / SOURCED_MAXWELL_CONDITIONAL / IDT_01AG_VARIATION_CURRENT_BRIDGE_PASS / EINSTEIN_BIANCHI_BRIDGE_HARDENED / COUPLING_AND_TOTAL_SOURCE_PROMOTION_OPEN`

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
IDT 01AG charged-matter variation
  delta S_m / delta A_mu = J_Q^mu / hbar
  J_EM^mu = -J_Q^mu / hbar
  single charge: J_EM^mu = -(q/hbar) J_theta^mu
  |
  v
admitted lowest-derivative Abelian action
  S_EM = integral sqrt(-g)[-F^2/(4 mu_*) - J_EM.A]
  |
  +--> sourced Maxwell
  |      nabla_mu F^(mu nu) = mu_* J_EM^nu
  |
  +--> current conservation
  |
  +--> metric variation
         T_EM(mu,nu)
         |
         v
RF-E0 EM/matter exchange
  nabla^mu T_EM(mu,nu)     = -F_(nu lambda) J_EM^lambda
  nabla^mu T_matter(mu,nu) = +F_(nu lambda) J_EM^lambda
  ------------------------------------------------------
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
  kappa_E = 8 pi G / c^4 after RF-N1C fixes G
         |
         +--> constant Lambda: nabla^mu T_total(mu,nu)=0
         |
         +--> dynamic Lambda0:
                kappa_E nabla^mu T_total(mu,nu)=nabla_nu Lambda0
                T_Lambda(mu,nu)=-(Lambda0/kappa_E)g_mu_nu
                nabla^mu(T_total+T_Lambda)_(mu,nu)=0
```

## Exact and conditional layers

### Exact structural layer

For an admitted nonzero probe charge and regular local gauge patch,

\[
\mathfrak a_{AB}=\frac q\hbar A,
\qquad
F=\frac\hbar q d\mathfrak a_{AB}=dA,
\qquad
\boxed{dF=0}.
\]

The AB coupling fixes the physical potential normalization on this branch. The hardened RF-M1 gate additionally checks that distinct nonzero probe-charge representations reconstruct the same physical potential.

For the admitted RFC Levi-Civita geometry,

\[
\boxed{\nabla^\mu G_{\mu\nu}=0},
\qquad
\boxed{\nabla^\mu g_{\mu\nu}=0}.
\]

For the dynamic scalar closure with spacetime-constant Einstein coupling coordinate `kappa_E`,

\[
G_{\mu\nu}+\Lambda_0 g_{\mu\nu}=\kappa_E T^{total}_{\mu\nu}
\]

implies

\[
\boxed{\kappa_E\nabla^\mu T^{total}_{\mu\nu}=\nabla_\nu\Lambda_0}.
\]

### Conditional action layer

After admitting the local Maxwell action with spacetime-constant field normalization `mu_*` and the charged-matter exchange action,

\[
\nabla_\mu F^{\mu\nu}=\mu_*J_{EM}^\nu,
\]

\[
T^{EM}_{\mu\nu}
=\frac1{\mu_*}
\left(F_{\mu\alpha}F_\nu{}^\alpha-\frac14g_{\mu\nu}F^2\right),
\]

and the EM/matter exchange closes to a conserved combined source.

IDT 01AG fixes the variation-level conversion from the charged Noether current to the Maxwell source current:

\[
\boxed{J_{EM}^\mu=-\frac1\hbar\mathcal J_Q^\mu},
\]

with single-charge reduction

\[
\boxed{J_{EM}^\mu=-\frac q\hbar J_\vartheta^\mu}.
\]

The next current promotion coordinate is the measured equality between the independently constructed RFC carrier current and this charge-projected electromagnetic current.

## Current promotion coordinates

1. promote the independently constructed RFC conserved carrier current against the IDT 01AG charge-projected electromagnetic current;
2. derive or empirically bind the vacuum field normalization `mu_*` in the selected physical unit convention;
3. complete the admitted charged-matter stress-energy action;
4. finish RF-N1C and determine `G`, hence `kappa_E`;
5. derive the dynamic `Lambda0` sector at action level;
6. run the full Einstein field-equation and unified-limit audit.

## Hardened validation snapshot — 2026-08-28

RFC branch `audit/relativistic-bridge-hardening-v0.1`, PR #14:

- focused RF-M1 gate: `9/9 PASS`;
- focused RF-E0 gate: `7/7 PASS`;
- first full hardening run `33202996446`: `447 passed, 1 failed`; the fail-closed result exposed schema drift in `CROSS_REFERENCE_LOCK.json` where earlier TIR/IDT/PNCS source-holonomy provenance had been displaced;
- additive lock repair `RFC_CROSS_REFERENCE_LOCK_V0_35` restored the upstream provenance and eight PNCS source-holonomy loops while preserving RFG29–RFG34;
- attested RFC commit `6be45ab1abe56da1ad98255bc7f1ccc1a271cd1d`;
- full RFC reference suite run `33203140994`: `448 passed, 0 failed`.

IDT peer branch `audit/relativistic-bridge-01ag-hardening-v0.1`, PR #22:

- focused IDT 01AG gate: `5/5 PASS`;
- attested IDT commit `82faeffd77e9b6bab0fb879cf76af39b4673d7d2`;
- full IDT reference suite run `33203002798`: `437 passed, 0 failed`.

The hardened evidence chain is

\[
\boxed{
\mathrm{IDT\ 01AC}
\rightarrow
\mathrm{IDT\ 01AG}
\rightarrow
\mathrm{RF\!\! -\! M1}
\rightarrow
\mathrm{RF\!\! -\! E0}
\rightarrow
\mathrm{Einstein\ closure\ gate}.
}
\]

Validation receipt: `validation/RFM1_RFE0_RELATIVISTIC_BRIDGE_HARDENING_V0_1.json`.
