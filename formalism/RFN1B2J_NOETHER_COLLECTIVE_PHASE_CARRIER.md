# RF-N1B2J — Noether Collective-Phase Carrier Gate

Status: `NOETHER_CURRENT_SOURCE_PASS / COLLECTIVE_REDUCTION_PASS_CONDITIONAL / ROTOR_CARRIER_BINDING_PASS_CONDITIONAL / RFC_CARRIER_BINDING_OPEN`

RF-N1B2J follows RF-N1B2I and consumes IDT 01Z. It tests the local conserved U(1) carrier against the dynamical rotor charge

\[
\boxed{P_\Phi:=J-J_I=I_\phi D_\tau\chi.}
\]

## 1. Noether current and finite charge

The upstream Euler–Noether scalar phase field supplies

\[
J_\vartheta^\mu=2A^2\partial^\mu\vartheta,
\qquad
\partial_\mu J_\vartheta^\mu=0.
\]

On a spatial slice,

\[
\boxed{
Q_\vartheta
=\int_\Sigma n_\mu J_\vartheta^\mu\,dV_h
=2\int_\Sigma A^2\nu_\vartheta\,dV_h,
\qquad
\nu_\vartheta=n_\mu\partial^\mu\vartheta.
}
\]

## 2. Collective phase and field inertia

In the collective sector

\[
\nu_\vartheta(x)=D_\tau\chi,
\]

define

\[
\boxed{I_A:=2\int_\Sigma A^2\,dV_h.}
\]

Then

\[
\boxed{Q_\vartheta=I_A D_\tau\chi.}
\]

The rotor gives

\[
\boxed{P_\Phi=J-J_I=I_\phi D_\tau\chi.}
\]

Hence

\[
\boxed{I_A\stackrel{?}{=}I_\phi}
\]

is the cross-representation normalization gate. When admitted,

\[
\boxed{Q_\vartheta=P_\Phi.}
\]

For nonzero phase rate the exact relative binding defect is

\[
\boxed{\Delta_I=\left|\frac{I_A}{I_\phi}-1\right|.}
\]

## 3. Euler-closed finite carrier and energy conversion

RF-N1B2I supplies

\[
J_I^{EB}=\hbar\theta_I^{EB}.
\]

Therefore

\[
\boxed{P_\Phi^{EB}=J-\hbar\theta_I^{EB}}
\]

and

\[
\boxed{H_\Phi^{EB}=\frac{(P_\Phi^{EB})^2}{2I_\phi}.}
\]

The finite Noether charge is

\[
\boxed{
Q_\vartheta^{EB}
=I_A D_\tau\chi
=\frac{I_A}{I_\phi}P_\Phi^{EB}.
}
\]

The energy-per-conserved-carrier coordinate is therefore

\[
\boxed{
\epsilon_N^{EB}
:=\frac{H_\Phi^{EB}}{Q_\vartheta^{EB}}.
}
\]

On the exact inertia-binding sector \(I_A=I_\phi\),

\[
Q_\vartheta^{EB}=P_\Phi^{EB}
\]

and

\[
\boxed{
\epsilon_N^{EB}
=\frac{H_\Phi^{EB}}{P_\Phi^{EB}}
=\frac{P_\Phi^{EB}}{2I_\phi}
=\frac12D_\tau\chi.
}
\]

The intention-charge ratio \(H_\Phi/J_I\) and the Noether-carrier ratio \(H_\Phi/Q_\vartheta\) remain separately typed. The latter is the RFC conserved-current candidate.

## 4. RFC carrier binding

RF-N1B2 defines

\[
Q_\Sigma=\int_{\Sigma_t}j_Q\,dV_h.
\]

The physical chain is

\[
\boxed{
Q_\Sigma
\stackrel{?}{\longleftrightarrow}
Q_\vartheta^{EB}
\stackrel{I_A=I_\phi}{\longleftrightarrow}
P_\Phi^{EB}.
}
\]

The corresponding candidate conversion is

\[
\boxed{
\epsilon_Q\stackrel{?}{=}\epsilon_N^{EB}
=\frac{H_\Phi^{EB}}{Q_\vartheta^{EB}}.
}
\]

Once the carrier binding is admitted,

\[
\boxed{
M_N
=\frac{\epsilon_N^{EB}Q_\vartheta^{EB}}{c^2}
=\frac{H_\Phi^{EB}}{c^2}.
}
\]

For normalized profile \(p_a^{(Q)}\),

\[
m_{N,a}=M_Np_a^{(Q)}.
\]

## 5. Local source density

Under the admitted local current binding,

\[
\boxed{\rho_N(x)=\frac{\epsilon_N^{EB}}{c^2}j_\vartheta(x).}
\]

This is the local density target for RF-N1C after common state-space/cell transport is fixed.

## 6. PNV gate

The executable loop is

```text
SOURCE.PHASE_NOETHER.COLLECTIVE_CARRIER.ROUNDTRIP

Euler-closed J_I^EB
 -> P_Phi^EB=J-J_I^EB
 -> Q_theta=I_A D_tau chi
 -> audit Delta_I=|I_A/I_phi-1|
 -> H_Phi^EB=P_Phi^2/(2 I_phi)
 -> epsilon_N^EB=H_Phi/Q_theta
 -> exact-binding reduction epsilon_N^EB=(1/2)D_tau chi
 -> Q_RFC=Q_theta
 -> reconstruct rotor carrier
```

Required invariants:

```text
SOURCE.EULER_CLOSURE_SECTOR
SOURCE.ROTOR_KINETIC_CHARGE
SOURCE.NOETHER_FINITE_CHARGE
SOURCE.ROTOR_PHASE_ENERGY
SOURCE.NOETHER_ENERGY_PER_CHARGE
SOURCE.NOETHER_INERTIA_BINDING_DEFECT
```

## 7. Advancement

```text
Noether current and polar reduction             PASS
collective-phase finite charge                  PASS_CONDITIONAL
field inertia I_A                               PASS as defined integral
I_A <-> I_phi                                   OPEN physical normalization gate
Q_theta <-> P_Phi                               PASS_CONDITIONAL on inertia binding
Euler-closed epsilon_N=H/Q_theta                PASS typed finite-carrier ratio
exact epsilon_N=H/P_Phi=(1/2)D_tau chi          PASS_CONDITIONAL on I_A=I_phi
Q_Sigma <-> Q_theta                             OPEN RFC carrier binding
p_IDT <-> p_Q                                   OPEN physical state-space binding
RF-N1C coupling/universality                    OPEN
```
