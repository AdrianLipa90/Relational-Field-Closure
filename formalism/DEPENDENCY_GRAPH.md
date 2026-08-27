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
  source binding requires conserved carrier + measure + energy assignment
                                 |
                                 v
RF-N1B2 conserved source-carrier factorization
  conserved current + dV_h -> extensive Q_Sigma
  positive-source sector -> normalized p_Q
  Q_a=Q_Sigma p_a^(Q)
                                 |
                                 v
RF-N1B2H normalized-shape / extensive-scale holonomy
  N(Q)=Q/Q_Sigma
  H_s(Q)=L_s(N(Q))=(s/Q_Sigma)Q
  Delta_ext=|1-s/Q_Sigma|
  exact inverse lift at s=Q_Sigma
                                 |
                                 v
IDT 01Y / RF-N1B2I Euler-closed phase-energy normalization
  Phi_tot=2 pi(D+epsilon_EB)
  theta_I^EB = closure residual
  J_I^EB=hbar theta_I^EB
  H_Phi^EB=(J-J_I^EB)^2/(2 I_phi)
  epsilon_I^EB=H_Phi^EB/J_I^EB
  Delta_tau_eff^EB=J_I^EB/H_Phi^EB
                                 |
                                 v
PNCS physical-law frame / executable holonomy
  PNCS_PNV_INFORMATION_HOLONOMY_V0_1
  PNCS_PNV_SOURCE_HOLONOMY_LOOPS_V0_1
  Q_a <-> (Q_Sigma,p_Q) exact control loop
  Q_a <-> n_a through conditional q0
  j_Q <-> rho_Q through downstream conditional epsilon_Q
  Euler/Berry -> J_I^EB -> H_Phi^EB -> epsilon_I^EB round trip
  Delta_gamma=d(I,H_gamma(I)) + invariant defects + inverse lineage
                                 |
                +----------------+----------------+
                |                                 |
                v                                 v
physical source binding OPEN              bounded candidate basis
 Q_Sigma <-> J_I^EB                       S_R=beta_I Xi_I+...
 J_I^EB <-> integral j_I dV_h             CANDIDATE_ONLY
 p_IDT <-> p_Q
 local cell/measure transport
                |                                 |
                +----------------+----------------+
                                 |
                                 v
RF-N1C coupling/universality audit
  Delta_h ln N_R = S_R
  Delta_h Phi_R = c^2 S_R
  target diagnostic: c^2 S_R ?= 4 pi G rho_m
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
- `RF-N1B type separation`: EXACT PASS at the cited interfaces. `rho_R` carries relational kinetic/mobility typing; `E=hbar|omega|` carries energy typing; `Xi_I` carries the required `L^-2` source-basis type. Matter-source semantics remain an explicit binding gate.
- `RF-N1B2 conserved continuous carrier`: PASS at the stated conditional level. An admitted conserved current plus the RF physical spatial measure gives an extensive slice carrier `Q_Sigma` under the declared boundary conditions. On a positive-source sector it factorizes as `Q_a=Q_Sigma p_a^(Q)`.
- `RF-N1B2H normalization holonomy`: EXACT PASS for the positive finite-cell factorization. Exact inverse transport uses the preserved scale coordinate.
- `RF-N1B2H IDT interface`: REFERENCE/ANALYTIC PASS with physical cross-binding OPEN. IDT 01X exports normalized simplex shape and the exact scale-fiber theorem.
- `RF-N1B2I Euler-closed action charge`: PASS for `theta_I^EB -> J_I^EB=hbar theta_I^EB` after the declared Euler/Berry closure input.
- `RF-N1B2I rotor energy`: PASS for `H_Phi^EB=(J-J_I^EB)^2/(2 I_phi)` with `I_phi>0`.
- `RF-N1B2I energy/action-charge`: PASS_CONDITIONAL on the positive non-degenerate sector: `epsilon_I^EB=H_Phi^EB/J_I^EB`; `Delta_tau_eff^EB=1/epsilon_I^EB` is then reconstructed.
- `RFC epsilon_Q binding`: OPEN physical carrier gate `Q_Sigma <-> J_I^EB`, followed by `epsilon_Q <-> epsilon_I^EB` in the admitted bound sector.
- `finite/local current lift`: OPEN gate `J_I^EB <-> integral_Sigma j_I dV_h`; this is the immediate source-normalization frontier.
- `PNCS source-law frame`: REFERENCE IMPLEMENTED at code snapshot `e6d5e217aeed2906372fdd0aa41845f0df32bbae`, with contracts `PNCS_PNV_INFORMATION_HOLONOMY_V0_1` and `PNCS_PNV_SOURCE_HOLONOMY_LOOPS_V0_1`.
- `SOURCE.CARRIER.NORMALIZATION.ROUNDTRIP`: reference exact control for `Q_a -> (Q_Sigma,p_Q) -> Q_a'`.
- `SOURCE.CARRIER.Q0_OCCUPATION.ROUNDTRIP`: CONDITIONAL on positive `q0`.
- `SOURCE.CARRIER.EPSILON_MASS_DENSITY.ROUNDTRIP`: downstream CONDITIONAL consumer of an admitted positive `epsilon_Q`.
- `SOURCE.PHASE_INTENTION.EULER_CHARGE_ENERGY.ROUNDTRIP`: Euler-first normalization control with invariants `SOURCE.EULER_CLOSURE_SECTOR`, `SOURCE.INTENTION_ACTION_CHARGE`, `SOURCE.ROTOR_PHASE_ENERGY`, `SOURCE.ENERGY_PER_ACTION_CHARGE`.
- `paired IDT/RFC reference validation`: PASS on pinned test snapshots. IDT: `348 passed`; RFC: `40 passed`. Shared receipt: `validation/IDT_RFC_PNCS_SOURCE_HOLONOMY_PAIR_V0_1.json`.
- `PNCS native source-loop workflow`: `CI_EXECUTION_UNRESOLVED_PRE_TEST`; observed job `steps=null`, so PNCS native execution remains a separate admission gate.
- `RF-N1B2I normalization frontier`: `Q_Sigma <-> J_I^EB`, finite-charge ↔ conserved-local-current lift, `p_IDT <-> p_Q`, and local measure/cell transport are the explicit prerequisites before RF-N1C.
- `TIR mass sector`: active TIR claim hierarchy classifies the exponential mass ansatz as class B/C depending on sector. Newton-source import remains a separate OPEN gate.
- `RF-M2`, physical carrier/current binding, `RF-N1C`, `RF-L1`, `RF-E1`: OPEN.

## Information-holonomy connection audit

The cross-repository architecture is

\[
\boxed{
\mathrm{IDT\ 01X/01Y}
\leftrightarrow
\mathrm{PNV\ physical\! -\! law\ frame}
\leftrightarrow
\mathrm{RFC\ RF\! -\! N1B2H/I}.
}
\]

For each admitted or conditional transport edge \(T_{i\to j}\), PNV carries an explicit operator and records

\[
\mathcal H_\gamma=T_{n-1}\cdots T_1T_0,
\qquad
\Delta_\gamma=d(I,\mathcal H_\gamma I).
\]

The receipt carries declared invariant defects and inverse lineage to KAKU/RADICAL/OPERATOR evidence.

The immediate source-law closure target is now the physical current/carrier bridge:

\[
\boxed{
J_I^{EB}
\stackrel{?}{\longleftrightarrow}
Q_\Sigma
=\int_{\Sigma_t}j_Q\,dV_h,
\qquad
J_I^{EB}
\stackrel{?}{\longleftrightarrow}
\int_{\Sigma_t}j_I\,dV_h.
}
\]

A successful binding feeds the Euler-derived `epsilon_I^EB` into the conditional RFC density transport and then into the RF-N1C coupling/universality audit.
