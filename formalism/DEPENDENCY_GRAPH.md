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
IDT relational clock ratio N_R
  |
RF-N0 relational lapse Phi_R = c^2 ln N_R
  |
RF-N1A hexahedral source operator
  Delta_h ln N_R = S_R
  |
RF-N1B source-type / identifiability firewall
  |
RF-N1B2 conserved carrier factorization
  |
RF-N1B2H/I/J/K/L/M/N/O
  normalized shape -> action charge -> Noether carrier
  -> local current -> rotor inertia -> gauge pullback
  -> omega_Q = D_hat_tau chi -> phase-energy source
  |
RF-N1C three-route coupling holonomy
  Newton source <-> double copy <-> Einstein / horizon
  |
  +-----------------------------+
  |                             |
RF-N1C1                      RF-N1C2
phase-source                reduced gravity-scale
specialization              Mbar_G=M_star/(Gamma_DC g_YM^2)
  |                             |
  |                          RFG7
  |                          Mbar_G=2/kappa_g
  |                             |
  |                          RF-N1C3
  |                          Mbar_G^2=M_H T_H
  |                             |
  +---------------+-------------+
                  |
RF-E3 Einstein-Hilbert action normalization
  2/kappa_g^2 = 1/(2 kappa_E) = 1/(16 pi G)
  |
metric variation -> G_mu_nu = kappa_E T_mu_nu
  |
total-matter composition + dynamic Lambda0 action
  |
RF-X1 unified-limit audit
```

## Gauge → amplitude → gravity branch

```text
holonomic SU(3) W_ij / W_mu(x)
  |
RFG3 Wilson continuum normalization
  |
RFG4E action-coefficient theorem
  |
RFG4F generator/link-rescale firewall
  |
RFG4G same-sector normalization transfer
  g_YM^2 = 1/alpha_c
  C_p = 2 alpha_c
  beta_W = 6 alpha_c
  |
RFG8 oriented cubic Yang-Mills vertex
  W_mu = exp(i sigma_link g a A_mu)
  upstream sigma_link = +1
  V3 = -sigma_link g f V
  |
  +---------------------------+
  |                           |
RFG9                        RFG10
four-gluon MHV             direct project link
BCJ reference              -> A_mu -> k,epsilon
n_s+n_t+n_u=0                |
  |                         RFG11
  |                         full 8-component principal-log recovery
  |                         F_link = i g[A_mu,A_nu] for sigma=+1
  |                           |
  |                         RFG12
  |                         project nonabelian color/momentum convolution
  |                         color 1 x 2 -> 3
  |                         k_out = k1-k2, k1+k2
  |                           |
  |                         RFG13
  |                         quartic YM contact normalization
  |                         E4=-g^2 Tr[A_mu,A_nu]^2
  |                           |
  +-------------+-------------+
                |
RFG14 direct project four-point exchange + contact assembly [NEXT]
                |
project BCJ numerator comparison against RFG9
                |
RFG2 / RFG7 double-copy factorization
                |
RF-N1C / RF-E3 Einstein normalization
```

## Maxwell branch

```text
RF-M1 Aharonov-Bohm normalized U(1) curvature
  -> RF-M4 charge-projected Noether Maxwell source
```

The Maxwell electric-charge projection and the gravitational phase-energy carrier remain separately typed. RF-N1B2O consumes the charge-independent phase Noether carrier, while RF-M4 applies electric-charge projection on the Maxwell source branch.

## Current source / gravity identities

RF-N1B2N/O give

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

RF-N1C/RF-N1C1 give, in natural units on the admitted local carrier surface,

\[
\boxed{
G_{DC}=\frac{18\Gamma_{DC}^2}{\pi\beta_W^2\omega_Q^2},
\qquad
\mathcal S_R^{DC}=\frac{72\Gamma_{DC}^2}{\beta_W^2}A^2.
}
\]

RFG4G reduces the gauge normalization to

\[
\boxed{
g_{YM}^2=\frac1{\alpha_c},
\qquad
\beta_W=6\alpha_c.}
\]

Hence

\[
\boxed{
\bar M_G
=\frac{\alpha_cM_\star}{\Gamma_{DC}}.
}
\]

RFG7 removes the factorization coordinate from the invariant gravity scale:

\[
\boxed{
\bar M_G
=\frac{M_\star}{\Gamma_{DC}g_{YM}^2}
=\frac{2}{\kappa_g},
\qquad
G=\frac{1}{8\pi\bar M_G^2}
=\frac{\kappa_g^2}{32\pi}.}
\]

RF-N1C3 independently gives

\[
\boxed{
\bar M_G^2=M_HT_H
=\frac{M_H\kappa_H}{2\pi}.}
\]

Therefore, on the RFG4G surface,

\[
\boxed{
\Gamma_{DC}
=\frac{\alpha_cM_\star}{\sqrt{M_HT_H}},}
\]

and on `M_star=omega_Q/2`,

\[
\boxed{
\Gamma_{DC}
=\frac{\alpha_c\omega_Q}{2\sqrt{M_HT_H}}.}
\]

## Direct project Yang–Mills binding

RFG10 recovers commuting-color local field modes from actual link phases. RFG11 generalizes this to all eight `SU(3)` coordinates on the principal matrix-log branch:

\[
\boxed{
A_\mu^a
=\frac1g\operatorname{Tr}(\lambda^a\mathcal Q_\mu),
\qquad
\mathcal Q_\mu=\frac1a\operatorname{HermLog}W_\mu.}
\]

For the upstream `sigma_link=+1` plaquette,

\[
\boxed{
F_{\mu\nu}^{link}
=\partial_\mu A_\nu-\partial_\nu A_\mu
+i g[A_\mu,A_\nu],}
\]

so the component commutator coefficient is `-g f^{abc}`.

RFG12 supplies the direct interacting momentum witness

\[
A_y^1\sim\cos(k_1x),
\qquad
A_z^2\sim\cos(k_2x)
\]

\[
\boxed{
F_{yz}^3
=-gA_y^1A_z^2
\Rightarrow
k_{out}=k_1-k_2,\;k_1+k_2.}
\]

RFG13 fixes the quartic contact density from the same action normalization:

\[
\boxed{
\mathcal E_4^{\mu\nu}
=\operatorname{Tr}(F_{\mu\nu}^2)
=-g^2\operatorname{Tr}[A_\mu,A_\nu]^2,}
\]

and

\[
\boxed{
\frac{(2\alpha_c)D_p}{a^4}
\longrightarrow
\operatorname{Tr}(F_{\mu\nu}^2).}
\]

Thus the project now carries direct link-byte witnesses for the field, nonabelian cubic mixing and quartic contact normalization on one consistent coupling/orientation convention.

## BCJ reference surface

RFG9 verifies in the four-gluon MHV tree sector

\[
\boxed{
s_{12}A(1,2,3,4)=s_{13}A(1,3,2,4)}
\]

and the explicit generalized-gauge representative

\[
\boxed{
n_s=s_{12}A(1234),\qquad n_t=0,\qquad n_u=-n_s,}
\]

so

\[
\boxed{n_s+n_t+n_u=0.}
\]

The immediate project gate is to assemble the exchange and quartic contact pieces from the RFG10–RFG13 external-state coordinates and compare the resulting `A_4^{project}` with this frozen RFG9 surface before any double-copy gravity evaluation.

## Einstein action bridge

RF-N1C and RF-E3 give

\[
\boxed{
\kappa_E=\frac{8\pi G}{c^4},}
\]

and in natural units

\[
\boxed{
\kappa_E=8\pi G=\frac{\kappa_g^2}{4},
\qquad
\frac{1}{2\kappa_E}=\frac{2}{\kappa_g^2}.}
\]

Therefore

\[
\boxed{
S_{EH}
=\frac{1}{2\kappa_E}\int d^4x\sqrt{-g}R,}
\]

and metric variation gives

\[
\boxed{G_{\mu\nu}=\kappa_ET_{\mu\nu}.}
\]

## Validation state on current feature branch

```text
historical IDT suite provenance                 382/382 PASS
historical RFC suite provenance                  74/74 PASS
current RFC local additions through RFG13        84/84 PASS
IDT 01AE local handoff                            4/4 PASS
recent replay RFG10-RFG13                       24/24 PASS
GitHub Actions full branch suite                 NOT EXECUTED
```

## Current physical frontier

```text
phase-kinetic local source map                   PASS CONDITIONAL
Yang-Mills beta_W normalization                  PASS CONDITIONAL SAME-SECTOR / RFG4G
cubic YM orientation/normalization               PASS / RFG8+RFG11
project link -> full local SU(3) field            PASS PRINCIPAL-BRANCH / RFG10+RFG11
project nonabelian color/momentum mixing          PASS / RFG12
quartic YM contact normalization                 PASS / RFG13
four-point MHV BCJ reference                     PASS / RFG9
direct project four-point exchange+contact       OPEN NEXT GATE
project BCJ numerator binding                    OPEN AFTER DIRECT A4
Gamma_DC factorization invariant                 PASS EXACT / RFG7
Gamma_DC numerical promotion                     OPEN EVIDENCE GATE
M_star scale promotion                           OPEN RF-N1C2/RFG7
cross-system Mbar_G universality                  OPEN EVIDENCE GATE
total matter stress-energy composition            OPEN
independent dynamic-Lambda0 action                OPEN
```

## Execution and provenance layer

```text
PNCS main: ebdeb9729f21db17bebe4e14302a9687cdc33f4e
GREMLIN live authoring: v0.3 / canonical AutoBoot V3
IDT phase-source branch: feat/idt-rfc-normalized-shape-holonomy-v0.1
IDT pinned head: e6c57b314bcf2e04de679c46c0be309f46cba053
RFC current branch: feat/rfn1c-three-route-coupling-holonomy-v0.1
```

GREMLIN remains a candidate-generation/audit layer; promotion continues through explicit reference, provenance and physical admission gates.
