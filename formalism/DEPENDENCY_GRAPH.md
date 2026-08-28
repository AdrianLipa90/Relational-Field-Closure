# Formal dependency graph

```text
RF-00 pinned upstream contract
  |
RF-01 QGT relational primitive
  |
RF-02H hexahedral rank-3 metric
  |
RF-G0 Lorentzian signature
  |
RF-02I coframe connection / curvature
  |
IDT 05C relational clock ratio N_R
  |
RF-N0 relational lapse Phi_R = c^2 ln N_R
  |
RF-N1A hexahedral source operator
  Delta_h ln N_R = S_R
  |
RF-N1B source-type / identifiability firewall
  |
RF-N1B2 conserved carrier factorization
  Q_a = Q_Sigma p_a^(Q)
  |
RF-N1B2H normalized-shape / extensive-scale holonomy
  |
RF-N1B2I Euler-closed intention action charge
  |
RF-N1B2J finite Noether carrier
  |
RF-N1B2K local current / measure defect theorem
  |
RF-N1B2L scalar-field -> rotor inertia reduction
  I_phi = 2 integral A^2 dV_h
  |
RF-N1B2M gauge-covariant common-U(1) pullback
  |
RF-N1B2N relational-lapse normal phase-rate bridge
  omega_Q = D_hat_tau chi = D_t chi / N_R
  epsilon_N = omega_Q / 2
  |
RF-N1B2O phase-energy / Noether-carrier source binding
  j_theta = 2 A^2 omega_Q
  E_theta = epsilon_N j_theta
  rho_theta = E_theta / c^2
  |
RF-N1C three-route coupling holonomy
  Newton source <-> double copy <-> Einstein / horizon
  kappa_E = 8 pi G / c^4
  kappa_E = kappa_g^2 / 4  [natural units]
  |
  +---------------------------+
  |                           |
RF-N1C1                    RF-N1C2
phase-source              carrier-scale
specialization            universality firewall
S_R^DC =                  Mbar_G = M_star/(Gamma_DC g_YM^2)
72 Gamma_DC^2 A^2/beta_W^2
  |                           |
  +-------------+-------------+
                |
RF-E3 Einstein-Hilbert action normalization
  2/kappa_g^2 = 1/(2 kappa_E) = 1/(16 pi G)
  |
metric variation
  G_mu_nu = kappa_E T_mu_nu
  |
total-matter composition + dynamic Lambda0 action
  |
RF-X1 unified-limit audit
```

## Parallel gauge branch

```text
RF-M1 Aharonov-Bohm normalized U(1) curvature
  -> RF-M4 charge-projected Noether Maxwell source

holonomic SU(3)
  -> RFG3 Wilson continuum/Yang-Mills normalization
  -> RFG6 kinematic Jacobi / BCJ gate
  -> RFG2 double-copy coupling coordinate
  -> RF-N1C / RF-N1C2
```

The Maxwell electric-charge projection and the gravitational phase-energy carrier remain separately typed. RF-N1B2O uses the charge-independent phase Noether carrier; RF-M4 applies the electric-charge projection only on the Maxwell source branch.

## Current exact and conditional gates

- `RF-02H`: local rank-3 hexahedral metric — PASS.
- `RF-G0`: Lorentzian signature theorem — EXACT CONDITIONAL.
- `RF-02I`: compatible local connection/curvature — PASS on admitted coframe sector.
- `RF-N0`: relational lapse and Newtonian force kinematics — PASS CONDITIONAL.
- `RF-N1A`: Laplace principal source operator — PASS.
- `RF-N1B2`: conserved continuous carrier factorization — PASS.
- `RF-N1B2H`: normalized-shape/extensive-scale holonomy — PASS.
- `RF-N1B2I/J`: Euler-selected action charge and finite Noether carrier — PASS at their stated conditional levels.
- `RF-N1B2K`: local current/measure defect theorem `Delta_Sigma <= Delta_J + Delta_V` — EXACT.
- `RF-N1B2L`: scalar-field/rotor inertia reduction — EXACT CONDITIONAL.
- `RF-N1B2M`: gauge-covariant phase pullback — EXACT CONDITIONAL.
- `RF-N1B2N`: `omega_Q=D_hat_tau chi=D_t chi/N_R`, `epsilon_N=omega_Q/2` — EXACT CONDITIONAL; dedicated reference coverage added on this branch.
- `RF-N1B2O`: `E_theta=(omega_Q/2)j_theta`, `rho_theta=E_theta/c^2` — EXACT LOCAL FACTORIZATION on admitted phase-kinetic matter sector.
- `RF-N1C`: Newton↔double-copy↔Einstein normalization and three-route off-shell syzygy — EXACT ALGEBRAIC FRONTIER, physical inputs gated.
- `RF-N1C1`: phase-source reduction and reciprocal `G`/`rho` phase-rate scaling — EXACT.
- `RF-N1C2`: reduced gravity-scale reparameterization and universal-G equivalence — EXACT; cross-system evidence gate open.
- `RF-E3`: Einstein-Hilbert coefficient transfer and metric-variation normalization — EXACT on admitted conventions.

## Phase-source bridge

RF-N1B2N and RF-N1B2O give

\[
\boxed{
\omega_Q=D_{\hat\tau}\chi=\frac{D_t\chi}{N_R},
\qquad
\epsilon_N=\frac12\omega_Q,
}
\]

\[
\boxed{
j_\vartheta=2A^2\omega_Q,
\qquad
\rho_\vartheta=\frac{A^2\omega_Q^2}{c^2}.
}
\]

On the RF-N1C local double-copy scale candidate,

\[
\boxed{
G_{DC}=\frac{18\Gamma_{DC}^2}{\pi\beta_W^2\omega_Q^2}
}
\]

in natural units, while RF-N1C1 gives

\[
\boxed{
\mathcal S_R^{DC}
=4\pi G_{DC}\rho_\vartheta
=\frac{72\Gamma_{DC}^2}{\beta_W^2}A^2.
}
\]

Thus a phase-rate rescaling obeys

\[
\rho_\vartheta\mapsto\lambda^2\rho_\vartheta,
\qquad
G_{DC}\mapsto\lambda^{-2}G_{DC},
\qquad
\mathcal S_R^{DC}\mapsto\mathcal S_R^{DC}.
\]

## Universal gravity-scale firewall

RF-N1C2 defines

\[
\boxed{
\bar M_G
:=\frac{M_\star}{\Gamma_{DC}g_{YM}^2},
\qquad
G_{DC}=\frac{1}{8\pi\bar M_G^2}.
}
\]

With `g_YM^2=6/beta_W`,

\[
\boxed{
\bar M_G=\frac{\beta_WM_\star}{6\Gamma_{DC}}.
}
\]

On `M_star=omega_Q/2`,

\[
\boxed{
\bar M_G^{local}
=\frac{\beta_W\omega_Q}{12\Gamma_{DC}}.
}
\]

For independently admitted systems `a,b`,

\[
\boxed{
G_a=G_b
\Longleftrightarrow
\bar M_{G,a}=\bar M_{G,b}
}
\]

on the positive scale sector. This is the current zero-fit universality frontier.

## Einstein action bridge

RF-N1C and RF-E3 give

\[
\boxed{
\kappa_E=\frac{8\pi G}{c^4}
}
\]

and in natural units

\[
\boxed{
\kappa_E=8\pi G=\frac{\kappa_g^2}{4},
\qquad
\frac{1}{2\kappa_E}=\frac{2}{\kappa_g^2}.
}
\]

Therefore

\[
\boxed{
S_{EH}
=\frac{1}{2\kappa_E}\int d^4x\sqrt{-g}R
}
\]

and standard metric variation yields

\[
\boxed{G_{\mu\nu}=\kappa_ET_{\mu\nu}.}
\]

## Execution and provenance layer

Current PNCS execution-layer provenance:

```text
AdrianLipa90/PhaseNav-Natural-Coding-System
main
ebdeb9729f21db17bebe4e14302a9687cdc33f4e
```

The PNCS main state contains GREMLIN live authoring v0.3 provenance and canonical NOEMA AutoBoot V3 integration. GREMLIN remains candidate-only and has no independent canon or runtime execution authority.

## Current physical frontier

```text
phase-kinetic local source map                PASS CONDITIONAL
Newton <-> Einstein normalization             PASS EXACT TRANSFER
Einstein-Hilbert prefactor                    PASS EXACT TRANSFER
local phase-source/double-copy closure        PASS ALGEBRAIC
reduced gravity-scale coordinate              PASS EXACT
project beta_W physical normalization         OPEN
project BCJ-compatible numerator binding      OPEN
Gamma_DC physical normalization               OPEN
M_star scale promotion                        OPEN / RF-N1C2 firewall
cross-system Mbar_G universality               OPEN EVIDENCE GATE
total matter stress-energy composition         OPEN
independent dynamic-Lambda0 action             OPEN
```

The next coupling promotion therefore targets independently frozen Yang-Mills/BCJ/double-copy coordinates and cross-system constancy of `Mbar_G`, while the Einstein geometry/action spine remains fixed.
