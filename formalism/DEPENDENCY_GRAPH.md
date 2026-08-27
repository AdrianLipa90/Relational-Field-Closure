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
  J_I^EB=hbar theta_I^EB
  H_Phi^EB=(J-J_I^EB)^2/(2 I_phi)
  |
IDT 01Z / RF-N1B2J finite Noether carrier
  P_Phi^EB=J-J_I^EB
  Q_theta=I_A D_tau chi=(I_A/I_phi)P_Phi^EB
  Delta_I=|I_A/I_phi-1|
  epsilon_N^EB=H_Phi^EB/Q_theta
  |
IDT 01AA / RF-N1B2K local conserved-current binding
  common slice + measure + ordered cells
  Delta_measure
  Delta_local
  Delta_Q
  Delta_F
  zero defects => Q_Sigma=Q_theta candidate identity
  |
PNCS physical-law frame / executable holonomy
  six source/control loops
  Delta_gamma + invariant defects + inverse lineage
  |
  +---------------- physical promotion OPEN ---------------------+
  |  I_A <-> I_phi                                              |
  |  Q_Sigma <-> Q_theta                                       |
  |  epsilon_Q <-> epsilon_N^EB                                 |
  |  p_IDT <-> p_Q physical state-space binding                 |
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
- `field inertia`: `I_A=2 integral A^2 dV_h`.
- `rotor kinetic coordinate`: `P_Phi^EB=J-J_I^EB=I_phi D_tau chi`.
- `field/rotor normalization`: OPEN physical gate with
  \[
  \Delta_I=\left|I_A/I_\phi-1\right|.
  \]
- `finite Noether carrier`: `Q_theta=I_A D_tau chi=(I_A/I_phi)P_Phi^EB`.
- `finite Noether energy coordinate`:
  \[
  \epsilon_N^{EB}=H_\Phi^{EB}/Q_\vartheta.
  \]
- `RF-N1B2K common-measure gate`: semantic slice/measure/ordered-cell support is explicit; numerical cell-volume mismatch is measured by
  \[
  \Delta_V=\frac{\sum_a|V_a^{(\vartheta)}-V_a^{(Q)}|}{\sum_aV_a^{(\vartheta)}}.
  \]
- `RF-N1B2K local-current gate`:
  \[
  \Delta_{\rm local}=\frac{\sum_aV_a|j_{Q,a}-j_{\vartheta,a}|}{Q_\vartheta}.
  \]
- `RF-N1B2K total-charge gate`:
  \[
  \Delta_Q=\frac{|Q_\Sigma-Q_\vartheta|}{Q_\vartheta}.
  \]
- `RF-N1B2K side-flux gate`:
  \[
  \Delta_F=|F_{\rm side}|.
  \]
- `anti-false-positive witness`: `j_theta=(1,3)`, `j_Q=(2,2)`, `V=(1,1)` gives `Q_theta=Q_Sigma=4`, `Delta_Q=0`, but `Delta_local=1/2`; integrated equality alone therefore does not promote local current identity.
- `Q_Sigma <-> Q_theta`: PASS_CONDITIONAL at zero common-measure/local-current/total-charge/side-flux defects; physical promotion remains OPEN.
- `RFC epsilon binding`: OPEN downstream physical promotion `epsilon_Q <-> epsilon_N^EB` after carrier identity evidence is admitted.
- `source mass coordinate`: `M_N=epsilon_N^EB Q_theta/c^2=H_Phi^EB/c^2`.

## PNCS execution layer

Pinned PNCS code snapshot:

```text
AdrianLipa90/PhaseNav-Natural-Coding-System
feat/gremlin-pnv-authoring-v0.2
f7b428f4dc30ddeb1280c9213c5788f576a54db4
```

Contracts:

```text
PNCS_GREMLIN_NATIVE_PNV_BRIDGE_V0_2
PNCS_PNV_INFORMATION_HOLONOMY_V0_1
PNCS_PNV_SOURCE_HOLONOMY_LOOPS_V0_1
PNCS_PNV_NOETHER_COLLECTIVE_CARRIER_V0_1
PNCS_PNV_NOETHER_RFC_CURRENT_BINDING_V0_1
```

Loops:

```text
SOURCE.CARRIER.NORMALIZATION.ROUNDTRIP
SOURCE.CARRIER.Q0_OCCUPATION.ROUNDTRIP
SOURCE.CARRIER.EPSILON_MASS_DENSITY.ROUNDTRIP
SOURCE.PHASE_INTENTION.EULER_CHARGE_ENERGY.ROUNDTRIP
SOURCE.PHASE_NOETHER.COLLECTIVE_CARRIER.ROUNDTRIP
SOURCE.PHASE_NOETHER.RFC_CONSERVED_CURRENT.ROUNDTRIP
```

The sixth loop audits

```text
SOURCE.NOETHER_TOTAL_CHARGE
SOURCE.RFC_TOTAL_CHARGE
SOURCE.COMMON_MEASURE_DEFECT
SOURCE.LOCAL_CURRENT_BINDING_DEFECT
SOURCE.TOTAL_CHARGE_BINDING_DEFECT
SOURCE.SIDE_FLUX_DEFECT
```

and fails closed on semantic measure/cell mismatch or any declared defect above tolerance.

Latest executed cross-repository reference snapshots:

```text
IDT Reference suite     370 passed, 0 failed
RFC Reference suite      62 passed, 0 failed
```

PNCS native workflow remains `CI_EXECUTION_UNRESOLVED_PRE_TEST`; run `33123979049`, job `98697546433` has `steps=null`.

## Current source frontier

The executable candidate-current gate is now present. The remaining source frontier is physical promotion and downstream transport:

\[
\boxed{
Q_\Sigma\stackrel{?}{\longleftrightarrow}Q_\vartheta,
\qquad
\epsilon_Q\stackrel{?}{=}\epsilon_N^{EB}
}
\]

under evidence for the common local current and measure.

The next executable integration target is the full source path

\[
J_\vartheta^\mu
\to Q_\vartheta
\leftrightarrow Q_\Sigma
\to \epsilon_N^{EB}
\to \rho_N
\to RF\text{-}N1C,
\]

with current-binding and physical-promotion defects retained explicitly.
