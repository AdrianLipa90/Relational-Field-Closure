# RF-N1B2I — Euler-Closed Phase-Intention Energy-per-Action-Charge Gate

Status: `EULER_CLOSED_ACTION_CHARGE_PASS / ROTOR_ENERGY_PER_CHARGE_PASS_CONDITIONAL / RFC_CARRIER_BINDING_OPEN / LOCAL_CURRENT_LIFT_OPEN`

RF-N1B2I consumes IDT 01Y after Euler/Berry closure selects the admissible phase/action-charge sector. The gate remains downstream of RF-N1B2H and upstream of RF-N1C.

## 1. Euler/Berry closure first

The shared closure law is

\[
\Phi_{\rm tot}=\Phi_{AB}+\int_\Sigma(\mathcal F_B+s_E\mathcal R_E)+\Theta_I=2\pi(D+\epsilon_{EB}).
\]

For the next intention step,

\[
\boxed{\theta_{I,k}^{EB}=2\pi(D+\epsilon_{EB})-\Phi_{AB}-\int_\Sigma(\mathcal F_B+s_E\mathcal R_E)-\Theta_I^{<k}.}
\]

The phase fixes the action charge:

\[
\boxed{J_{I,k}^{EB}=\hbar\theta_{I,k}^{EB}.}
\]

At exact closure, \(\epsilon_{EB}=0\).

## 2. Independent rotor energy

The canonical phase rotor supplies

\[
\boxed{H_{\Phi,k}^{EB}=\frac{(J_k-J_{I,k}^{EB})^2}{2I_\phi}.}
\]

Therefore, on the positive non-degenerate sector,

\[
\boxed{\epsilon_{I,k}^{EB}:=\frac{H_{\Phi,k}^{EB}}{J_{I,k}^{EB}}=\frac{(J_k-\hbar\theta_{I,k}^{EB})^2}{2I_\phi\hbar\theta_{I,k}^{EB}}.}
\]

Since \(J_I\) has action type, \([\epsilon_I]=T^{-1}\).

## 3. Floquet time step becomes derived

The Floquet identity remains

\[
\Delta\tau_kH_{\Phi,k}=J_{I,k}.
\]

After Euler closure and rotor energy are fixed,

\[
\boxed{\Delta\tau_{k,\rm eff}^{EB}=\frac{J_{I,k}^{EB}}{H_{\Phi,k}^{EB}}=\frac1{\epsilon_{I,k}^{EB}}.}
\]

Thus the order is

```text
Euler/Berry closure
 -> theta_I^EB
 -> J_I^EB
 -> rotor H_Phi^EB
 -> epsilon_I^EB
 -> Delta_tau_eff^EB
 -> RFC carrier binding
```

## 4. RFC binding

RF-N1B2 defines

\[
Q_\Sigma=\int_{\Sigma_t}j_Q\,dV_h.
\]

The physical binding remains

\[
\boxed{Q_\Sigma\stackrel{?}{\longleftrightarrow}J_I^{EB}.}
\]

Only in an admitted bound sector does RFC assign

\[
\boxed{\epsilon_Q\stackrel{?}{=}\epsilon_I^{EB}.}
\]

Then

\[
\boxed{M_I=\frac{\epsilon_I^{EB}J_I^{EB}}{c^2}=\frac{H_\Phi^{EB}}{c^2}.}
\]

For normalized profile \(p_a^{(Q)}\), \(m_{I,a}=M_Ip_a^{(Q)}\).

## 5. Local current lift

A local source requires

\[
\boxed{J_I^{EB}\stackrel{?}{=}\int_{\Sigma_t}j_I\,dV_h}
\]

with a conserved local current. Once admitted,

\[
\boxed{\rho_I(x)=\frac{\epsilon_I^{EB}}{c^2}j_I(x).}
\]

The Euler/Noether phase current and temporal-fluid current remain candidate local lifts.

## 6. Fail-closed sector

Ratio evaluation requires

```text
I_phi > 0
J_I^EB > 0
H_Phi^EB > 0
finite Euler/Berry phase data
```

Zero or degenerate sectors retain the closure/action-charge equations without forcing a finite energy-per-charge ratio.

## 7. PNCS loop

Required executable loop:

```text
SOURCE.PHASE_INTENTION.EULER_CHARGE_ENERGY.ROUNDTRIP

Euler/Berry data
 -> theta_I^EB
 -> J_I^EB = hbar theta_I^EB
 -> H_Phi^EB = (J-J_I^EB)^2/(2 I_phi)
 -> epsilon_I^EB = H_Phi^EB/J_I^EB
 -> Delta_tau_eff^EB = 1/epsilon_I^EB
 -> reconstruct J_I^EB
```

Required invariants:

```text
SOURCE.EULER_CLOSURE_SECTOR
SOURCE.INTENTION_ACTION_CHARGE
SOURCE.ROTOR_PHASE_ENERGY
SOURCE.ENERGY_PER_ACTION_CHARGE
```

## 8. Advancement

```text
Euler/Berry closure                            PASS
Euler residual -> action charge J_I^EB         PASS
canonical rotor energy                         PASS
energy/action-charge epsilon_I^EB              PASS_CONDITIONAL
Delta_tau_eff=1/epsilon_I^EB                   PASS_CONDITIONAL
Q_Sigma <-> J_I^EB carrier binding             OPEN
J_I^EB <-> local conserved-current lift        OPEN
p_IDT <-> p_Q physical binding                 OPEN
RF-N1C coupling/universality                   OPEN
```
