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
  |   exact theorem: constant lapse -> Gamma^i_tt=0
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
  rho_m binding requires conserved source/occupation + measure + energy assignment
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
                                 v
PNCS physical-law frame / executable holonomy
  PNCS_PNV_INFORMATION_HOLONOMY_V0_1
  PNCS_PNV_SOURCE_HOLONOMY_LOOPS_V0_1
  Q_a <-> (Q_Sigma,p_Q) exact control loop
  Q_a <-> n_a through conditional q0
  j_Q <-> rho_Q through conditional epsilon_Q
  Delta_gamma=d(I,H_gamma(I)) + invariant defects + inverse lineage
                                 |
                +----------------+----------------+
                |                                 |
                v                                 v
source normalization OPEN                 bounded candidate basis
 Q_Sigma / epsilon_Q / M_Q                S_R=beta_I Xi_I+...
 IDT 01X-RFC p <-> p_Q cross-binding      CANDIDATE_ONLY
 q0 / E-per-carrier binding
 temporal/phase carrier <-> rho_m
                |                                 |
                +----------------+----------------+
                                 |
                                 v
RF-N1C coupling/universality audit
  Delta_h ln N_R = S_R
  Delta_h Phi_R = c^2 S_R
  target: c^2 S_R ?= 4 pi G rho_m
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

Every downstream promotion is limited by its weakest unresolved prerequisite.

## Current exact/candidate status

- `RF-02H`: LOCAL STRUCTURAL PASS — regular dual frame gives `h_H=I3/6`, exact rank three and octahedral isotropy.
- `RF-G0`: exact conditional Lorentzian signature theorem; RF-02H supplies the local positive rank-three prerequisite.
- `RF-02I`: LOCAL EXACT CONNECTION PASS; phase-clock gradients enter the spatial connection/curvature. Constant lapse gives exact `Gamma^i_tt=0` theorem.
- `IDT 05C`: EXACT CLOCK-RATIO PASS — `N_R>0`, dimensionless, reparameterization invariant, compositional.
- `RF-N0`: exact conditional geodesic kinematics after temporal-coframe binding; `Phi_R=c^2 ln N_R`, weak local force form `a=-grad Phi_R+...`.
- `RF-N1A`: LOCAL EXACT OPERATOR PASS — IDT graph response plus hexahedral symmetry yields the Laplace principal operator from the admitted graph-response and symmetry premises.
- `RF-N1B type separation`: EXACT PASS at the cited interfaces. `rho_R` carries relational kinetic/mobility typing; `rho_R <-> rho_m` remains an explicit OPEN physical binding. `E=hbar|omega|` carries energy typing. `Xi_I` carries the required `L^-2` source-basis type; matter-source semantics remain an explicit binding gate.
- `RF-N1B conditional phase-cell bridge`: exact algebra once `V_H=a_H^3`, `E=hbar|omega|` and a source occupation `n_E` are separately admitted: `rho_cell=6 sqrt(6) n_E hbar |omega|^4/c^5`. Physical source occupation and cell-volume semantics remain OPEN.
- `RF-N1B identifiability theorem`: EXACT for the current premise set — different free occupation maps or source coefficients give different matter/source laws while preserving the already-derived geometry, lapse kinematics and source operator. Unique `rho_m` and unique `G` therefore remain OPEN at this premise level.
- `RF-N1B universality diagnostic`: CANDIDATE TEST. If independent derivations later give both `S_R=beta_I Xi_I` and the phase-cell matter bridge, Newton matching requires `G=[beta_I J_pi/(24 pi sqrt(6) n_E a_FS)] c^5/(hbar omega^2)`. Status: consistency condition; independent `G` derivation remains OPEN.
- `RF-N1B2 conserved continuous carrier`: PASS at the stated conditional level. `fluid_time.pdf` supplies `J_tau^mu=rho_tau u^mu` with `nabla_mu J_tau^mu=0`; any admitted conserved current plus the RF physical spatial measure gives an extensive slice carrier `Q_Sigma` under vanishing side flux / periodic / sufficient-decay conditions. On a positive-source sector it factorizes as `Q_a=Q_Sigma p_a^(Q)` with normalized `p_a^(Q)`.
- `RF-N1B2H normalization holonomy`: EXACT PASS for the positive finite-cell factorization. The normalization map is constant on positive rays; the lift holonomy is `H_s(Q)=(s/Q_Sigma)Q`; the relative extensive defect is `Delta_ext=|1-s/Q_Sigma|`; exact inverse transport uses the preserved scale coordinate. The continuous source conversion combines into the extensive coordinate `M_Q=epsilon_Q Q_Sigma/c^2`, with `m_Q,a=M_Q p_a^(Q)` and `rho_Q,a=M_Q p_a^(Q)/V_a`.
- `RF-N1B2H IDT interface`: REFERENCE/ANALYTIC PASS with physical cross-binding OPEN. IDT `01X-RFC` exports normalized simplex shape and the exact scale-fiber theorem; physical admission awaits a pinned common state space, cell partition/measure, and transport compatibility.
- `PNCS source-law frame`: REFERENCE IMPLEMENTED. Both IDT and RFC pin PNCS code snapshot `5f3bf90998b8c3547d51e7c47bddaf0d6be25d60` and contracts `PNCS_PNV_INFORMATION_HOLONOMY_V0_1` / `PNCS_PNV_SOURCE_HOLONOMY_LOOPS_V0_1`.
- `SOURCE.CARRIER.NORMALIZATION.ROUNDTRIP`: reference exact control loop for `Q_a -> (Q_Sigma,p_Q) -> Q_a'`, with `SOURCE.TOTAL_Q` and `SOURCE.PROFILE_NORM` as explicit invariants.
- `SOURCE.CARRIER.Q0_OCCUPATION.ROUNDTRIP`: CONDITIONAL on an independently admitted positive `q0`; transports `Q_a -> n_a=Q_a/q0 -> Q_a'`.
- `SOURCE.CARRIER.EPSILON_MASS_DENSITY.ROUNDTRIP`: CONDITIONAL on an independently admitted positive `epsilon_Q`; transports `j_Q -> rho_Q=(epsilon_Q/c^2)j_Q -> j_Q'`.
- `paired IDT/RFC reference validation`: PASS. IDT full reference suite: `337 passed`; RFC full reference suite: `29 passed`. Shared receipt: `validation/IDT_RFC_PNCS_SOURCE_HOLONOMY_PAIR_V0_1.json`.
- `PNCS native source-loop workflow`: `CI_EXECUTION_UNRESOLVED_PRE_TEST`; this remains a separate execution admission gate for the PNCS code snapshot.
- `RF-N1B2 normalization frontier`: OPEN. Carrier quantum `q0`, energy-per-carrier conversion `epsilon_Q`, combined physical source-mass scale `M_Q`, the physical `p_IDT <-> p^(Q)` cross-binding, and temporal/phase carrier to ordinary matter binding remain the explicit prerequisites before RF-N1C.
- `TIR mass sector`: active TIR claim hierarchy classifies the exponential mass ansatz as class B/C depending on sector. Newton-source import remains a separate OPEN gate.
- `RF-M2`, carrier normalization/matter binding, `RF-N1C`, `RF-L1`, `RF-E1`: OPEN.

## Information-holonomy connection audit

The cross-repository architecture is now

\[
\boxed{
\mathrm{IDT}
\leftrightarrow
\mathrm{PNV\ physical\! -\! law\ frame}
\leftrightarrow
\mathrm{RFC}.
}
\]

For each admitted or conditional transport edge \(T_{i\to j}\), PNV carries an explicit operator and the loop audit records

\[
\mathcal H_\gamma=T_{n-1}\cdots T_1T_0,
\qquad
\Delta_\gamma=d(I,\mathcal H_\gamma I).
\]

The receipt also carries declared invariant defects and inverse lineage to KAKU/RADICAL/OPERATOR evidence. This turns `RF-N1B2H` into the first executable connection-control layer in the source branch rather than a document-only cross-reference.

The next source-law closure target is an independent derivation of `epsilon_Q`, or equivalently an independently derived `q0` plus per-carrier energy assignment, from the admitted phase/time Hamiltonian. The resulting normalization enters PNCS as an explicit transport edge and must close a declared information-holonomy loop before advancing the RF-N1C source-coupling audit.
