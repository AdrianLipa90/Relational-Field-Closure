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
  |
IDT 05C clock ratio N_R=phi_x/phi_ref
  |
RF-N0 relational lapse
  |
RF-N1A source-operator theorem
  |
RF-N1B source-type firewall
  |
RF-N1B2 conserved source-carrier factorization
  Q_a=Q_Sigma p_a^(Q)
  |
RF-N1B2H normalized-shape / extensive-scale holonomy
  |
IDT 01Y / RF-N1B2I Euler-closed intention charge
  Phi_tot=2 pi(D+epsilon_EB)
  J_I^EB=hbar theta_I^EB
  H_Phi^EB=(J-J_I^EB)^2/(2 I_phi)
  |
IDT 01Z / RF-N1B2J Noether collective carrier
  P_Phi^EB=J-J_I^EB
  J_theta^mu=2 A^2 partial^mu theta
  Q_theta=I_A D_tau chi=(I_A/I_phi)P_Phi^EB
  Delta_I=|I_A/I_phi-1|
  epsilon_N^EB=H_Phi^EB/Q_theta
  exact I_A=I_phi => epsilon_N^EB=(1/2)D_tau chi
  |
PNCS physical-law frame / executable holonomy
  five source/control loops
  Delta_gamma + invariant defects + inverse lineage
  |
  +---------------- current/carrier binding OPEN ----------------+
  |  I_A <-> I_phi                                              |
  |  Q_Sigma <-> Q_theta                                       |
  |  epsilon_Q <-> epsilon_N^EB                                 |
  |  p_IDT <-> p_Q and local cell/measure/current transport     |
  +--------------------------------------------------------------+
  |
RF-N1C coupling/universality audit
  Delta_h ln N_R = S_R
  Delta_h Phi_R = c^2 S_R
  target diagnostic: c^2 S_R ?= 4 pi G rho_m
  G OPEN
  |
RF-E1 Einstein-Bianchi closure -> RF-X1 unified limit audit
```

Parallel gauge and information-curvature branches retain their existing RF-M0/RF-M1/RF-M2 and IDT 01K/RF-L0 interfaces.

## Current exact/candidate status

- `RF-02H`: LOCAL STRUCTURAL PASS — regular dual frame gives `h_H=I3/6`, exact rank three and octahedral isotropy.
- `RF-G0`: exact conditional Lorentzian signature theorem.
- `RF-02I`: LOCAL EXACT CONNECTION PASS; phase-clock gradients enter the spatial connection/curvature.
- `IDT 05C`: EXACT CLOCK-RATIO PASS — `N_R>0`, dimensionless, reparameterization invariant, compositional.
- `RF-N0`: exact conditional geodesic kinematics after temporal-coframe binding.
- `RF-N1A`: LOCAL EXACT OPERATOR PASS — IDT graph response plus hexahedral symmetry yields the Laplace principal operator from the admitted graph-response and symmetry premises.
- `RF-N1B2`: conserved continuous carrier factorization PASS at the stated conditional level: `Q_a=Q_Sigma p_a^(Q)`.
- `RF-N1B2H`: normalized-shape/extensive-scale holonomy PASS for the positive finite-cell factorization.
- `RF-N1B2I`: Euler-closed intention charge PASS for `J_I^EB=hbar theta_I^EB`; canonical rotor energy PASS for `H_Phi^EB=(J-J_I^EB)^2/(2I_phi)`.
- `RF-N1B2J`: local U(1) Noether current and polar reduction PASS; collective finite-charge reduction PASS_CONDITIONAL.
- `field inertia`: `I_A=2 integral A^2 dV_h` is the finite collective-field inertia coordinate.
- `rotor kinetic coordinate`: `P_Phi^EB=J-J_I^EB=I_phi D_tau chi`.
- `field/rotor normalization`: OPEN physical gate `I_A <-> I_phi` with exact audit coordinate
  \[
  \Delta_I=\left|I_A/I_\phi-1\right|.
  \]
- `finite Noether carrier`: `Q_theta=I_A D_tau chi=(I_A/I_phi)P_Phi^EB`.
- `Noether/rotor charge equality`: PASS_CONDITIONAL only at `Delta_I=0`, giving `Q_theta=P_Phi^EB`.
- `finite Noether energy coordinate`: PASS as typed positive-sector ratio,
  \[
  \epsilon_N^{EB}=H_\Phi^{EB}/Q_\vartheta.
  \]
- `exact inertia-binding reduction`: PASS_CONDITIONAL at `I_A=I_phi`,
  \[
  \epsilon_N^{EB}=H_\Phi^{EB}/P_\Phi^{EB}=P_\Phi^{EB}/(2I_\phi)=\tfrac12D_\tau\chi.
  \]
- `RFC physical carrier binding`: OPEN chain `Q_Sigma <-> Q_theta`.
- `RFC epsilon binding`: OPEN downstream binding `epsilon_Q <-> epsilon_N^EB` after the conserved carrier identity is admitted.
- `source mass coordinate`: `M_N=epsilon_N^EB Q_theta/c^2=H_Phi^EB/c^2`.

## PNCS execution layer

Pinned PNCS code snapshot:

```text
AdrianLipa90/PhaseNav-Natural-Coding-System
feat/gremlin-pnv-authoring-v0.2
fa517208e40873523d1c2a5b7fdb852092421afa
```

Contracts:

```text
PNCS_GREMLIN_NATIVE_PNV_BRIDGE_V0_2
PNCS_PNV_INFORMATION_HOLONOMY_V0_1
PNCS_PNV_SOURCE_HOLONOMY_LOOPS_V0_1
PNCS_PNV_NOETHER_COLLECTIVE_CARRIER_V0_1
```

Loops:

```text
SOURCE.CARRIER.NORMALIZATION.ROUNDTRIP
SOURCE.CARRIER.Q0_OCCUPATION.ROUNDTRIP
SOURCE.CARRIER.EPSILON_MASS_DENSITY.ROUNDTRIP
SOURCE.PHASE_INTENTION.EULER_CHARGE_ENERGY.ROUNDTRIP
SOURCE.PHASE_NOETHER.COLLECTIVE_CARRIER.ROUNDTRIP
```

The fifth loop audits

```text
SOURCE.ROTOR_KINETIC_CHARGE
SOURCE.NOETHER_FINITE_CHARGE
SOURCE.NOETHER_INERTIA_BINDING_DEFECT
SOURCE.NOETHER_ENERGY_PER_CHARGE
```

and fails closed at RFC candidate binding when the declared inertia tolerance is exceeded. Its general energy coordinate is `H_Phi_EB/Q_theta`; `H_Phi_EB/P_Phi_EB=(1/2)D_tau_chi` is the exact zero-defect reduction.

Latest executed cross-repository reference snapshots:

```text
IDT Reference suite     356 passed, 0 failed
RFC Reference suite      48 passed, 0 failed
```

PNCS native workflow remains `CI_EXECUTION_UNRESOLVED_PRE_TEST`; the observed candidate-authoring job for the test head has `steps=null`.

## Current source frontier

\[
\boxed{
Q_\Sigma\stackrel{?}{\longleftrightarrow}Q_\vartheta,
\qquad
I_A\stackrel{?}{=}I_\phi.
}
\]

The immediate RF-N1B2J closure target is the conserved-current identity under one explicitly pinned spatial slice, measure/cell partition, orientation and side-flux convention. Once that carrier identity is admitted, `epsilon_Q <-> epsilon_N^EB` becomes a direct downstream gate rather than a free normalization search.
