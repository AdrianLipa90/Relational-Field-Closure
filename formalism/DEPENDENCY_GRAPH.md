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
  P_Phi^EB=J-J_I^EB
  H_Phi^EB=(P_Phi^EB)^2/(2 I_phi)
  |
IDT 01Z / RF-N1B2J finite Noether carrier
  Q_theta=I_A D_tau chi
  epsilon_N^EB=H_Phi^EB/Q_theta
  |
IDT 01AA / RF-N1B2K exact local current/measure theorem
  Delta_Sigma <= Delta_J + Delta_V
  |
IDT 01AB / RF-N1B2L scalar-field -> rotor coefficient reduction
  I_A=2 integral A^2 dV_h
  I_phi=I_A on the common collective reduction
  |
IDT 01AC / RF-N1B2M gauge-covariant common-U(1) pullback
  A'=A-dlambda
  theta'=theta+lambda
  Dtheta=dtheta+A_ABE
  q^*(Dtheta)=D_tau chi dtau
  Q_theta/P_Phi=(I_A/I_phi)(r_n/r_rotor)
  |
PNCS physical-law frame / executable holonomy
  eight source/control loops
  Delta_gamma + invariant defects + inverse lineage
  |
  +---------------- measured physical promotion ------------------+
  |  physical common-U(1) bundle/patch/ABE realization          |
  |  normal-flow/slice realization                               |
  |  J_Q^mu <-> J_theta^mu                                      |
  |  Q_Sigma <-> Q_theta                                        |
  |  p_IDT <-> p_Q physical state-space binding                  |
  +---------------------------------------------------------------+
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
- `IDT 05C`: EXACT CLOCK-RATIO PASS — `N_R>0`, dimensionless, reparameterization invariant and compositional.
- `RF-N0`: exact conditional geodesic kinematics after temporal-coframe binding.
- `RF-N1A`: LOCAL EXACT OPERATOR PASS — IDT graph response plus hexahedral symmetry yields the Laplace principal operator from the admitted graph-response and symmetry premises.
- `RF-N1B2`: conserved continuous carrier factorization PASS at the stated conditional level: `Q_a=Q_Sigma p_a^(Q)`.
- `RF-N1B2H`: normalized-shape/extensive-scale holonomy PASS for the positive finite-cell factorization.
- `RF-N1B2I`: Euler-selected intention charge and canonical rotor energy PASS at the formal reference level.
- `RF-N1B2J`: finite collective Noether carrier and energy-per-carrier coordinates typed.
- `RF-N1B2K`: exact current/measure defect theorem implemented.
- `RF-N1B2L`: scalar-field/rotor coefficient reduction implemented as a conditional exact theorem.
- `RF-N1B2M`: gauge-covariant common-U(1) pullback implemented as a conditional exact theorem.

## RF-N1B2K — local current and measure gate

On one common slice, orientation and ordered cell support,

\[
Q_\vartheta=\sum_aV_{\vartheta,a}j_{\vartheta,a},
\qquad
Q_\Sigma=\sum_aV_{Q,a}j_{Q,a}.
\]

The local coordinates are

\[
\boxed{
\Delta_J
=\frac{\sum_aV_{Q,a}|j_{Q,a}-j_{\vartheta,a}|}{Q_\vartheta},
}
\]

\[
\boxed{
\Delta_V
=\frac{\sum_a|V_{Q,a}-V_{\vartheta,a}|\,|j_{\vartheta,a}|}{Q_\vartheta},
}
\]

\[
\boxed{
\Delta_\Sigma
=\frac{|Q_\Sigma-Q_\vartheta|}{Q_\vartheta}.
}
\]

The exact bound is

\[
\boxed{\Delta_\Sigma\le\Delta_J+\Delta_V.}
\]

The witness

\[
j_\vartheta=(1,3),\qquad j_Q=(2,2),\qquad V=(1,1)
\]

has equal integrated charge together with

\[
\Delta_\Sigma=0,
\qquad
\Delta_J=1/2,
\]

so the local-current coordinate remains part of the promotion gate.

## RF-N1B2L — scalar-field / rotor coefficient reduction

\[
C_A=\int_\Sigma A^2dV_h,
\qquad
I_A=2C_A,
\]

\[
L_{phase}^{field}=\frac{I_A}{2}(D_\tau\chi)^2,
\qquad
L_{phase}^{rotor}=\frac{I_\phi}{2}(D_\tau\chi)^2.
\]

On the admitted common collective reduction,

\[
\boxed{I_\phi=I_A.}
\]

The executable coordinate is

\[
\boxed{
\Delta_I^{red}=\frac{|I_\phi-I_A|}{I_A},
}
\]

kept separately typed from the RF-N1B2J ratio coordinate.

## RF-N1B2M — gauge-covariant phase pullback and generator bridge

The admitted Berry convention gives

\[
\boxed{\mathcal A'^{ABE}=\mathcal A^{ABE}-d\lambda}
\]

for the section transformation `u -> exp(i lambda)u`. With

\[
\vartheta' = \vartheta+\lambda,
\]

the invariant one-form is

\[
\boxed{\mathscr D\vartheta=d\vartheta+\mathcal A^{ABE}.}
\]

On the common local fiber coordinate,

\[
\chi(\tau)=\vartheta(q(\tau))+\chi_0,
\]

and the trajectory pullback satisfies

\[
\boxed{q^*(\mathscr D\vartheta)=D_\tau\chi\,d\tau.}
\]

The three independently typed rates are

\[
r_{field}=\sum_a(\partial_a\vartheta+\mathcal A_a^{ABE})\dot q^a,
\qquad
r_n=n_\mu\mathscr D^\mu\vartheta,
\qquad
r_{rotor}=D_\tau\chi.
\]

The finite generators obey

\[
Q_\vartheta=I_A r_n,
\qquad
P_\Phi=I_\phi r_{rotor},
\]

and therefore

\[
\boxed{
\frac{Q_\vartheta}{P_\Phi}
=\frac{I_A}{I_\phi}\frac{r_n}{r_{rotor}}.
}
\]

The executable gate audits

\[
\Delta_{gauge},\;
\Delta_I^{red},\;
\Delta_{rate},\;
\Delta_{normal},\;
\Delta_Q,\;
\Delta_\epsilon,\;
\Delta_{factorization},\;
\Delta_{action}.
\]

At the common zero-defect surface,

\[
\boxed{
I_A=I_\phi,
\quad
r_n=r_{field}=r_{rotor},
\quad
Q_\vartheta=P_\Phi^{EB},
\quad
\epsilon_N^{EB}=\frac12D_\tau\chi.
}
\]

After the separately measured RF-N1B2K current promotion, the RFC carrier chain becomes

\[
Q_\Sigma=Q_\vartheta=P_\Phi^{EB},
\qquad
\boxed{\epsilon_Q=\epsilon_N^{EB}=\frac12D_\tau\chi}
\]

at that admitted promotion surface.

## PNCS execution layer

Pinned executable snapshot:

```text
AdrianLipa90/PhaseNav-Natural-Coding-System
feat/gremlin-pnv-authoring-v0.2
b741460dba15d979a6387305daf93f476becb54e
```

Contracts:

```text
PNCS_GREMLIN_NATIVE_PNV_BRIDGE_V0_2
PNCS_PNV_INFORMATION_HOLONOMY_V0_1
PNCS_PNV_SOURCE_HOLONOMY_LOOPS_V0_1
PNCS_PNV_NOETHER_COLLECTIVE_CARRIER_V0_1
PNCS_PNV_NOETHER_RFC_CURRENT_BINDING_V0_1
PNCS_PNV_SCALAR_FIELD_ROTOR_INERTIA_REDUCTION_V0_1
PNCS_PNV_GAUGE_COVARIANT_PHASE_PULLBACK_V0_1
```

Loops:

```text
SOURCE.CARRIER.NORMALIZATION.ROUNDTRIP
SOURCE.CARRIER.Q0_OCCUPATION.ROUNDTRIP
SOURCE.CARRIER.EPSILON_MASS_DENSITY.ROUNDTRIP
SOURCE.PHASE_INTENTION.EULER_CHARGE_ENERGY.ROUNDTRIP
SOURCE.PHASE_NOETHER.COLLECTIVE_CARRIER.ROUNDTRIP
SOURCE.PHASE_NOETHER.RFC_CONSERVED_CURRENT.ROUNDTRIP
SOURCE.PHASE_NOETHER.ROTOR_INERTIA.REDUCTION.ROUNDTRIP
SOURCE.PHASE.NOETHER.GAUGE_COVARIANT_PULLBACK.ROUNDTRIP
```

Focused source-law checks authored: `68`.

Latest executed cross-repository gates:

```text
IDT Reference suite     382 passed, 0 failed
RFC Reference suite      74 passed, 0 failed
```

PNCS native workflow remains `CI_EXECUTION_UNRESOLVED_PRE_TEST`; run `33129045847`, job `98713992469` has `steps=null`, so it supplies no PNCS code-test verdict.

## Current source frontier

The formal field↔rotor gauge pullback now supplies the generator bridge. The measured physical frontier is

\[
\boxed{
\text{physical common-}U(1)\text{ realization}
\to
\text{normal-flow/slice realization}
\to
J_Q^\mu\leftrightarrow J_\vartheta^\mu
\to
Q_\Sigma\leftrightarrow Q_\vartheta
\to
p_{IDT}\leftrightarrow p_Q
\to
RF\text{-}N1C\;\text{coupling/universality}.
}
\]

The epsilon/mass-density transport remains downstream of the carrier promotion gate, with

\[
\epsilon_N^{EB}=\frac12D_\tau\chi,
\qquad
M_N=H_\Phi^{EB}/c^2
\]

available on the admitted common-generator sector.
