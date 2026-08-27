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
RF-02I coframe connection/curvature
  |   exact negative theorem: constant lapse -> Gamma^i_tt=0
  v
IDT 05C clock ratio N_R=phi_x/phi_ref
  |
RF-N0 relational lapse
  |   Theta_R=N_R c dt
  |   Phi_R=c^2 ln N_R
  |   weak kinematics -> a^i=-partial^i Phi_R+...
  |
  +------------------- IDT 01D Shannon-Onsager D^T W D
  |                              +
  +------------------- TIR six-ray hexahedral symmetry
                                 |
                                 v
RF-N1A source-operator theorem
  -L_H/a_H^2 -> Delta_h
  octahedral symmetry -> Laplace principal operator
                                 |
                                 v
RF-N1B source-type firewall
  rho_R = relational kinetic/mobility scalar
  E=hbar|omega| = local phase-energy scale
  Xi_I [L^-2] = source-basis-compatible geometry scalar
  dV_h = geometric measure after physical binding
  rho_m requires conserved source/occupation + measure + energy assignment
                                 |
                                 v
RF-N1B2 conserved source-carrier factorization
  fluid_time: J_tau^mu=rho_tau u^mu, nabla_mu J_tau^mu=0
  conserved current + dV_h -> extensive Q_Sigma (boundary-conditioned)
  positive-source sector -> normalized carrier profile p_Q
  Q_a=Q_Sigma p_a^(Q)
                                 |
                                 v
RF-N1B2H normalized-shape / extensive-scale holonomy
  N(Q)=Q/Q_Sigma
  H_s(Q)=L_s(N(Q))=(s/Q_Sigma)Q
  Delta_ext=|1-s/Q_Sigma|
  exact inverse lift at s=Q_Sigma
  m_Q,a=M_Q p_a^(Q), M_Q=epsilon_Q Q_Sigma/c^2
                                 |
                +----------------+----------------+
                |                                 |
                v                                 v
source normalization OPEN                 bounded candidate basis
 Q_Sigma / epsilon_Q / M_Q                S_R=beta_I Xi_I+...
 IDT 01X-RFC p <-> p_Q cross-binding      NO PROMOTION
 E-per-carrier binding
 temporal/phase carrier <-> rho_m
                |                                 |
                +----------------+----------------+
                                 |
                                 v
RF-N1C coupling/universality audit
  Delta_h ln N_R = S_R
  Delta_h Phi_R = c^2 S_R
  target only: c^2 S_R ?= 4 pi G rho_m
  G OPEN
                                 |
                                 v
RF-E1 Einstein-Bianchi closure -> RF-X1 unified limit audit

Parallel gauge branch:
RF-M0 Berry connection -> RF-M1 dF=0 -> RF-M2 sourced Maxwell OPEN

Information-curvature branch:
IDT 01L + TIR FS/Berry area -> IDT 01K Xi_I -> RF-L0 Lambda_I=alpha_I Xi_I
                                                |              |
                                                +--> RF-N1B    +--> RF-L1/RF-E1
```

No downstream node may be promoted above its weakest unresolved prerequisite.

## Current exact/candidate status

- `RF-02H`: LOCAL STRUCTURAL PASS — regular dual frame gives `h_H=I3/6`, exact rank three and octahedral isotropy.
- `RF-G0`: exact conditional Lorentzian signature theorem; RF-02H supplies the local positive rank-three prerequisite.
- `RF-02I`: LOCAL EXACT CONNECTION PASS; phase-clock gradients enter the spatial connection/curvature. Constant lapse gives exact `Gamma^i_tt=0` negative theorem.
- `IDT 05C`: EXACT CLOCK-RATIO PASS — `N_R>0`, dimensionless, reparameterization invariant, compositional.
- `RF-N0`: exact conditional geodesic kinematics after temporal-coframe binding; `Phi_R=c^2 ln N_R`, weak local force form `a=-grad Phi_R+...`.
- `RF-N1A`: LOCAL EXACT OPERATOR PASS — IDT graph response plus hexahedral symmetry yields the Laplace principal operator without using Poisson as a premise.
- `RF-N1B type separation`: EXACT PASS at the cited interfaces. IDT `rho_R` is introduced as a relational kinetic/mobility scalar and is not supplied there as `rho_m`; `E=hbar|omega|` is energy rather than density; `Xi_I` has the correct `L^-2` source type but no automatic matter semantics.
- `RF-N1B conditional phase-cell bridge`: exact algebra once `V_H=a_H^3`, `E=hbar|omega|` and a source occupation `n_E` are separately admitted: `rho_cell=6 sqrt(6) n_E hbar |omega|^4/c^5`. Physical source occupation and cell-volume semantics remain OPEN.
- `RF-N1B identifiability theorem`: EXACT for the current premise set — different free occupation maps or source coefficients give different matter/source laws while preserving the already-derived geometry, lapse kinematics and source operator. Therefore neither unique `rho_m` nor unique `G` is determined yet.
- `RF-N1B universality diagnostic`: CANDIDATE TEST. If independent derivations later give both `S_R=beta_I Xi_I` and the phase-cell matter bridge, Newton matching requires `G=[beta_I J_pi/(24 pi sqrt(6) n_E a_FS)] c^5/(hbar omega^2)`. This is a consistency condition, not a derivation or definition of `G`.
- `RF-N1B2 conserved continuous carrier`: PASS at the stated conditional level. `fluid_time.pdf` supplies `J_tau^mu=rho_tau u^mu` with `nabla_mu J_tau^mu=0`; any admitted conserved current plus the RF physical spatial measure gives an extensive slice carrier `Q_Sigma` under vanishing side flux / periodic / sufficient-decay conditions. On a positive-source sector it factorizes as `Q_a=Q_Sigma p_a^(Q)` with normalized `p_a^(Q)`.
- `RF-N1B2H normalization holonomy`: EXACT PASS for the positive finite-cell factorization. The normalization map is constant on positive rays; the lift holonomy is `H_s(Q)=(s/Q_Sigma)Q`; the relative extensive defect is `Delta_ext=|1-s/Q_Sigma|`; exact inverse transport uses the preserved scale coordinate. The continuous source conversion combines into the extensive coordinate `M_Q=epsilon_Q Q_Sigma/c^2`, with `m_Q,a=M_Q p_a^(Q)` and `rho_Q,a=M_Q p_a^(Q)/V_a`.
- `RF-N1B2H IDT interface`: OPEN. IDT `01X-RFC` exports normalized simplex shape and the exact scale-fiber theorem; physical admission awaits a pinned common state space, cell partition/measure, and transport compatibility.
- `RF-N1B2 normalization frontier`: OPEN. Carrier quantum `q0`, energy-per-carrier conversion `epsilon_Q`, combined physical source-mass scale `M_Q`, the physical `p_IDT <-> p^(Q)` cross-binding, and temporal/phase carrier to ordinary matter binding remain the explicit prerequisites before RF-N1C.
- `TIR mass sector`: active TIR claim hierarchy classifies the exponential mass ansatz as class B/C depending on sector and not as a universal established mass law; it is not imported as the Newton source.
- `RF-M2`, carrier normalization/matter binding, `RF-N1C`, `RF-L1`, `RF-E1`: OPEN.