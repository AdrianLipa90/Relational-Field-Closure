# RF-M1 / RF-E0 — Aharonov–Bohm → Maxwell → Einstein dependency bridge

Status: `HOMOGENEOUS_MAXWELL_EXACT / SOURCED_MAXWELL_CONDITIONAL / RF_E6_LORENTZIAN_ACTION_ALIGNMENT_PASS / RFC_CHARGE_PROJECTED_CURRENT_INTERTWINER_ACTIVE / EINSTEIN_BIANCHI_BRIDGE_HARDENED / TOTAL_SOURCE_AND_PHYSICAL_COUPLING_PROMOTION_OPEN`

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
F = dA = (hbar/q) d a_AB
  |
  +--> dF = 0
  |
  v
RF-E6 canonical Lorentzian matter action
  signature (-,+,+,+)
  L_m = -(D Psi)^dagger D Psi - U(Psi)
  delta S_m/delta A_mu = -J_Q^mu/hbar
  |
  v
RF-M4 / RF-N1B2P charge projection
  J_EM^mu = +J_Q^mu/hbar
  J_EM^mu = +(1/hbar) Pi_Q[J_RFC]^mu
  single charge: J_EM^mu = +(q/hbar) J_RFC,theta^mu
  neutral Q=0: J_EM^mu = 0
  |
  v
Maxwell equation
  nabla_mu F^(mu nu) = mu_* J_EM^nu
  |
  +--> T_EM
  |
  +--> RF-E6 T_matter
  |      nabla T_matter = +F.J_EM
  |      nabla T_EM     = -F.J_EM
  |      nabla(T_EM+T_matter)=0
  |
  v
RF-E4 / RF-E5 matter stress-energy structure
  epsilon = K+V
  p = K-V
  on-shell massive homogeneous scalar: V=K, p=0, epsilon=2K
  |
  v
RFC geometric spine
  RF-02H -> RF-G0 -> RF-02I -> contracted Bianchi
  |
  v
RF-N1C / RF-E3 Einstein normalization
  G_mu_nu + Lambda g_mu_nu = kappa_E T_total_mu_nu
  kappa_E = 8 pi G / c^4
  |
  v
RF-E0 dynamic Lambda0 transfer
  kappa_E nabla^mu T_total_mu_nu = nabla_nu Lambda0
```

## 1. Exact structural layer

For an admitted nonzero probe charge and regular local gauge patch,

\[
\boxed{
\mathfrak a_{AB}=\frac q\hbar A,
\qquad
F=\frac\hbar q d\mathfrak a_{AB}=dA,
\qquad
dF=0.
}
\]

For the admitted RFC Levi-Civita geometry,

\[
\boxed{\nabla^\mu G_{\mu\nu}=0,}
\qquad
\boxed{\nabla^\mu g_{\mu\nu}=0.}
\]

## 2. Action-consistent source layer

RF-G0 fixes

\[
\operatorname{signature}(g)=(-,+,+,+).
\]

RF-E6 aligns the scalar/multiplet action with that signature:

\[
\boxed{
\mathcal L_m
=-(\mathcal D_\mu\Psi)^\dagger\mathcal D^\mu\Psi-U(\Psi).
}
\]

With

\[
\mathcal J_Q^\mu
=i\left[(\mathcal D^\mu\Psi)^\dagger Q\Psi
-\Psi^\dagger Q\mathcal D^\mu\Psi\right],
\]

matter variation gives

\[
\boxed{
\frac{1}{\sqrt{-g}}\frac{\delta S_m}{\delta A_\mu}
=-\frac1\hbar\mathcal J_Q^\mu.
}
\]

Combined with the Maxwell kinetic action,

\[
\boxed{
\nabla_\mu F^{\mu\nu}=\mu_*J_{EM}^\nu,
\qquad
J_{EM}^\nu=\frac1\hbar\mathcal J_Q^\nu.
}
\]

RF-N1B2P therefore carries

\[
\boxed{
J_{EM}^\mu=\frac1\hbar\Pi_Q[J_{RFC}]^\mu,
}
\]

and for one charge eigenvalue,

\[
\boxed{
J_{EM}^\mu=\frac q\hbar J_{RFC,\vartheta}^\mu.
}
\]

## 3. Source bookkeeping firewall

RF-E6 keeps two source representations separately typed:

- microscopic matter action with coupling inside `D_mu Psi`;
- effective external-current action with `-J_EM^mu A_mu`.

Each representation yields the same sourced Maxwell equation. The action ledger uses one representation for a given carrier realization.

## 4. Stress-energy layer

RF-E6 supplies

\[
\boxed{
T_{\mu\nu}^{matter}
=(\mathcal D_\mu\Psi)^\dagger\mathcal D_\nu\Psi
+(\mathcal D_\nu\Psi)^\dagger\mathcal D_\mu\Psi
+g_{\mu\nu}\mathcal L_m.
}
\]

Together with

\[
T_{\mu\nu}^{EM}
=\frac1{\mu_*}
\left(F_{\mu\alpha}F_\nu{}^\alpha-\frac14g_{\mu\nu}F^2\right),
\]

one has on shell

\[
\boxed{
\nabla^\mu T^{EM}_{\mu\nu}=-F_{\nu\lambda}J_{EM}^\lambda,
\qquad
\nabla^\mu T^{matter}_{\mu\nu}=+F_{\nu\lambda}J_{EM}^\lambda.
}
\]

Hence

\[
\boxed{
\nabla^\mu(T^{EM}+T^{matter})_{\mu\nu}=0.
}
\]

RF-E4/RF-E5 preserve their physical pressure and on-shell carrier-energy results after transfer to the canonical `(-,+,+,+)` convention.

## 5. `mu_*` normalization

RF-E6 closes the unit-convention map

\[
\boxed{\mu_*=1}
\]

for canonically normalized rationalized Heaviside–Lorentz natural units, and

\[
\boxed{\mu_*=\mu_0}
\]

for SI electromagnetic fields/currents. In the SI normalization,

\[
\boxed{
\alpha_{EM}=\frac{\mu_*e^2c}{4\pi\hbar},
\qquad
\mu_*=\frac{4\pi\alpha_{EM}\hbar}{e^2c}.
}
\]

A frozen independent `alpha_EM` therefore calibrates `mu_*` exactly in that convention. First-principles `alpha_EM` prediction remains a separate physical gate.

## 6. Einstein layer

RF-N1C/RF-E3 provide

\[
\boxed{\kappa_E=\frac{8\pi G}{c^4}}
\]

as the Newton↔Einstein normalization transfer, with project-side physical promotion tied to the independent gravity-coupling gates.

For dynamic `Lambda0` and spacetime-constant `kappa_E`, RF-E0 gives

\[
\boxed{
\kappa_E\nabla^\mu T^{total}_{\mu\nu}=\nabla_\nu\Lambda_0.
}
\]

## 7. Current frontier

1. RF-N1B2K physical current/measure realization;
2. total-matter composition across phase, amplitude-gradient, potential/rest and additional admitted sectors;
3. cross-system physical `G` universality;
4. first-principles `alpha_EM` only if pursued as a project prediction;
5. independent dynamic-`Lambda0` action and stability gate;
6. full Einstein/unified-limit audit.

RF-E6 validation is carried by its dedicated reference suite and receipt on the correction branch.
