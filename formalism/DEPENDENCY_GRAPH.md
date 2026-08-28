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

## Gauge -> amplitude -> gravity branch

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
  |                           |
  |                         RFG11
  |                         full 8-component principal-log recovery
  |                         F_link = i g[A_mu,A_nu] for sigma=+1
  |                           |
  |                         RFG12
  |                         nonabelian color/momentum convolution
  |                         color 1 x 2 -> 3
  |                         k_out = k1-k2, k1+k2
  |                           |
  |                         RFG13
  |                         quartic YM contact normalization
  |                         E4=-g^2 Tr[A_mu,A_nu]^2
  |                           |
  +-------------+-------------+
                |
RFG14 project four-gluon exchange + contact
  full Ward cancellation / A4 ~ g^2
                |
RFG15 project BCJ numerator binding
  n_i = X_i + D_i K_i
  c_s-c_t+c_u = 0
  n_s-n_t+n_u = 0
                |
RFG16 project four-point double copy
  M4 = i kappa_E sum_i n_i n~_i/D_i
  kappa_E=(kappa_g/2)^2=8 pi G
  gravitational Ward PASS in either copy
                |
RFG17 G-free amplitude coupling holonomy
  kappa_E=1/Mbar_G^2
  =1/(M_H T_H)
  =4 Gamma_DC^2/(alpha_c^2 omega_Q^2)
                |
RFG7 / RF-N1C / RF-E3
  reduced gravity scale + Newton/Einstein/action closure
                |
higher-point project BCJ + cross-system Mbar_G evidence [NEXT]
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
\boxed{\omega_Q=D_{\hat\tau}\chi=\frac{D_t\chi}{N_R},\qquad\epsilon_N=\frac12\omega_Q}
\]

and

\[
\boxed{j_\vartheta=2A^2\omega_Q,\qquad\rho_\vartheta=\frac{A^2\omega_Q^2}{c^2}.}
\]

RF-N1C/RF-N1C1 give, in natural units on the admitted local carrier surface,

\[
\boxed{G_{DC}=\frac{18\Gamma_{DC}^2}{\pi\beta_W^2\omega_Q^2},\qquad\mathcal S_R^{DC}=\frac{72\Gamma_{DC}^2}{\beta_W^2}A^2.}
\]

RFG4G reduces the gauge normalization to

\[
\boxed{g_{YM}^2=\frac1{\alpha_c},\qquad\beta_W=6\alpha_c.}
\]

RFG7 removes the factorization coordinate from the invariant gravity scale:

\[
\boxed{\bar M_G=\frac{M_\star}{\Gamma_{DC}g_{YM}^2}=\frac{2}{\kappa_g},\qquad G=\frac{1}{8\pi\bar M_G^2}=\frac{\kappa_g^2}{32\pi}.}
\]

RF-N1C3 independently gives

\[
\boxed{\bar M_G^2=M_HT_H=\frac{M_H\kappa_H}{2\pi}.}
\]

Therefore, on the RFG4G surface,

\[
\boxed{\Gamma_{DC}=\frac{\alpha_cM_\star}{\sqrt{M_HT_H}}}
\]

and on `M_star=omega_Q/2`,

\[
\boxed{\Gamma_{DC}=\frac{\alpha_c\omega_Q}{2\sqrt{M_HT_H}}.}
\]

## Direct project Yang-Mills binding

RFG10 recovers local field modes from link phases; RFG11 generalizes this to all eight SU(3) coordinates on the principal matrix-log branch:

\[
\boxed{A_\mu^a=\frac1g\operatorname{Tr}(\lambda^a\mathcal Q_\mu),\qquad\mathcal Q_\mu=\frac1a\operatorname{HermLog}W_\mu.}
\]

For upstream `sigma_link=+1`,

\[
\boxed{F_{\mu\nu}^{link}=\partial_\mu A_\nu-\partial_\nu A_\mu+i g[A_\mu,A_\nu].}
\]

RFG12 supplies the direct interacting momentum witness

\[
\boxed{A_y^1\sim\cos(k_1x),\ A_z^2\sim\cos(k_2x)\Rightarrow F_{yz}^3=-gA_y^1A_z^2,\quad k_{out}=k_1-k_2,\ k_1+k_2.}
\]

RFG13 fixes the quartic contact density from the same action normalization:

\[
\boxed{\mathcal E_4^{\mu\nu}=\operatorname{Tr}(F_{\mu\nu}^2)=-g^2\operatorname{Tr}[A_\mu,A_\nu]^2}
\]

and

\[
\boxed{\frac{(2\alpha_c)D_p}{a^4}\longrightarrow\operatorname{Tr}(F_{\mu\nu}^2).}
\]

## Project four-point color-kinematics closure

RFG14 assembles the three exchange graphs and the quartic contact from the same normalized Yang-Mills sector. The full amplitude satisfies all four single-leg Ward identities; reversing the relative contact sign produces an order-one defect.

RFG15 distributes the contact term into the cubic channels:

\[
\boxed{n_i=X_i+D_iK_i.}
\]

With the project channel orientation,

\[
\boxed{c_s-c_t+c_u=0,\qquad n_s-n_t+n_u=0.}
\]

The cubicized representation reconstructs the full RFG14 amplitude:

\[
\boxed{\mathcal A_4^{project}=g^2\left(\frac{c_sn_s}{s}+\frac{c_tn_t}{t}+\frac{c_un_u}{u}\right).}
\]

No gravity target is used to construct the numerators.

## Project double-copy / Einstein coupling bridge

RFG16 uses two independently admitted RFG15 kinematic copies:

\[
\boxed{\mathcal M_4^{project}=i\left(\frac{\kappa_g}{2}\right)^2\left(\frac{n_s\tilde n_s}{s}+\frac{n_t\tilde n_t}{t}+\frac{n_u\tilde n_u}{u}\right).}
\]

Since

\[
\boxed{\left(\frac{\kappa_g}{2}\right)^2=\frac{\kappa_g^2}{4}=8\pi G=\kappa_E=\frac1{\bar M_G^2}}
\]

in natural units,

\[
\boxed{\mathcal M_4^{project}=i\kappa_E\sum_i\frac{n_i\tilde n_i}{D_i}.}
\]

Replacing any external polarization by its momentum in either kinematic copy gives a vanishing double-copy amplitude on the executable reference surface.

## G-free amplitude coupling holonomy

RFG17 combines the RFG16 amplitude coupling with the reduced-scale and horizon routes:

\[
\boxed{\kappa_E=\frac1{\bar M_G^2}=\frac1{M_HT_H}.}
\]

On the local carrier candidate,

\[
\boxed{\bar M_G=\frac{\alpha_c\omega_Q}{2\Gamma_{DC}}}
\]

so

\[
\boxed{\kappa_E=\frac{4\Gamma_{DC}^2}{\alpha_c^2\omega_Q^2}.}
\]

Thus the same project amplitude prefactor obeys the zero-fit cross-route identity

\[
\boxed{\frac{4\Gamma_{DC}^2}{\alpha_c^2\omega_Q^2}=\frac1{M_HT_H}.}
\]

This is algebraically exact on the common admitted surfaces; physical promotion of the carrier, horizon and cross-system inputs remains separately gated.

## Einstein action bridge

RF-N1C and RF-E3 give

\[
\boxed{\kappa_E=\frac{8\pi G}{c^4}}
\]

and in natural units

\[
\boxed{\kappa_E=8\pi G=\frac{\kappa_g^2}{4},\qquad\frac{1}{2\kappa_E}=\frac{2}{\kappa_g^2}.}
\]

Therefore

\[
\boxed{S_{EH}=\frac{1}{2\kappa_E}\int d^4x\sqrt{-g}R}
\]

and metric variation gives

\[
\boxed{G_{\mu\nu}=\kappa_ET_{\mu\nu}.}
\]

## Validation state on current feature branch

```text
historical IDT suite provenance                  382/382 PASS
historical RFC suite provenance                   74/74 PASS
current RFC local additions through RFG17        108/108 PASS
IDT 01AE local handoff                             4/4 PASS
recent RFG14-RFG17 local gates                    24/24 PASS
GitHub Actions full branch suite                  NOT EXECUTED
```

## Current physical frontier

```text
phase-kinetic local source map                    PASS CONDITIONAL
Yang-Mills beta_W normalization                   PASS CONDITIONAL SAME-SECTOR / RFG4G
project link -> full local SU(3) field             PASS PRINCIPAL-BRANCH / RFG10+RFG11
project nonabelian color/momentum mixing           PASS / RFG12
quartic YM contact normalization                  PASS / RFG13
project four-gluon exchange+contact               PASS / RFG14
project four-point BCJ numerator binding          PASS / RFG15
project four-point double-copy gravity            PASS / RFG16
Einstein coupling match kappa_E                   PASS EXACT / RFG16+RF-E3
G-free phase/horizon/amplitude coupling           PASS EXACT ALGEBRAIC / RFG17
higher-point project BCJ                          OPEN
Gamma_DC numerical promotion                      OPEN EVIDENCE GATE
M_star scale promotion                            OPEN RF-N1C2/RFG7
cross-system Mbar_G universality                  OPEN EVIDENCE GATE
total matter stress-energy composition             OPEN
independent dynamic-Lambda0 action                 OPEN
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
