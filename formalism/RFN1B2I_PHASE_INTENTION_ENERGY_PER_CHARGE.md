# RF-N1B2I — Phase-Intention Energy-per-Action-Charge Gate

Status: `FLOQUET_ENERGY_ACTION_RATIO_PASS / RFC_CARRIER_BINDING_OPEN / LOCAL_CURRENT_LIFT_OPEN`

RF-N1B2I consumes the IDT 01Y phase-intention export and advances the continuous source-normalization branch without using a Newton matching condition.

The gate is downstream of RF-N1B2H and upstream of RF-N1C.

## 1. IDT 01Y source contract

The pinned phase-intention scaffold defines

\[
\boxed{
J_{I,s}(\tau,k)=\hbar\rho_s(k)\mathcal I_s(\tau,k)
}
\]

and

\[
\boxed{
H_{\Phi,s}(\tau,k)
=\frac{\hbar}{\Delta\tau_k}\rho_s(k)\mathcal I_s(\tau,k).
}
\]

Therefore IDT 01Y exports

\[
\boxed{
\Delta\tau_k H_{\Phi,s}=J_{I,s}
}
\]

and the action-charge energy conversion

\[
\boxed{
H_{\Phi,s}=\epsilon_{I,k}J_{I,s},
\qquad
\epsilon_{I,k}=\frac1{\Delta\tau_k}.
}
\]

This is an operator-level identity in the pinned Floquet phase sector.

## 2. RFC carrier-type binding

RF-N1B2 defines a generic extensive conserved carrier

\[
Q_\Sigma=\int_{\Sigma_t}j_Q\,dV_h.
\]

The phase-intention sector now supplies a concrete action-charge candidate. The interface binding is

\[
\boxed{
Q_\Sigma\stackrel{?}{\longleftrightarrow}J_{I,s}.
}
\]

Its gate state is

```text
Q_Sigma <-> J_I    OPEN PHYSICAL/CURRENT BINDING
```

Under admission of this binding, the RFC continuous conversion coordinate becomes

\[
\boxed{
\epsilon_Q
=\epsilon_{I,k}
=\frac1{\Delta\tau_k}.
}
\]

Since \(J_I\) carries action type,

\[
[\epsilon_Q]=T^{-1},
\]

which is the correct energy-per-charge type for an action-valued carrier.

## 3. Extensive source-mass coordinate

RF-N1B2H introduced

\[
M_Q=\frac{\epsilon_QQ_\Sigma}{c^2}.
\]

With the phase-intention binding admitted,

\[
\boxed{
M_I
=\frac{J_{I,s}}{c^2\Delta\tau_k}
=\frac{H_{\Phi,s}}{c^2}.
}
\]

Thus the extensive mass coordinate is exactly the Floquet phase energy divided by \(c^2\) in the bound sector.

For a normalized carrier profile \(p_a^{(Q)}\), the cell mass factorization is

\[
\boxed{
m_{I,a}
=M_Ip_a^{(Q)}
=\frac{H_{\Phi,s}}{c^2}p_a^{(Q)}.
}
\]

A physical cell density additionally uses the admitted RF measure/cell volume:

\[
\rho_{I,a}=\frac{M_I}{V_a}p_a^{(Q)}.
\]

## 4. Local current-lift gate

The finite phase-intention charge becomes a local RFC source only after a current lift satisfies

\[
\boxed{
J_{I,s}
\stackrel{?}{=}
\int_{\Sigma_t}j_I\,dV_h
}
\]

with an admitted conservation law for the corresponding current.

Once that gate passes,

\[
\boxed{
\rho_I(x)
=\frac{1}{c^2\Delta\tau_k}j_I(x).
}
\]

The upstream stack contains two current structures relevant to the search:

```text
Euler/Noether phase current      J_phi^mu
fluid-time conserved current     J_tau^mu
```

Their relation to the finite phase-intention action charge is tracked as a cross-binding problem.

## 5. Exact cancellation structure

The central GREMLIN invariant is the shared factor

\[
\hbar\rho_s(k)\mathcal I_s(\tau,k).
\]

It appears as

\[
J_I
=\hbar\rho_s\mathcal I_s,
\qquad
H_\Phi
=\frac1{\Delta\tau_k}\hbar\rho_s\mathcal I_s.
\]

Hence the normalization coordinate is independent of the particular nonzero scalar realization of the shared factor:

\[
\boxed{
\epsilon_I=\frac1{\Delta\tau_k}.
}
\]

The zero-charge sector is carried by the linear identity

\[
\Delta\tau_kH_\Phi=J_I
\]

without ratio evaluation.

## 6. PNCS source-law control loop

RF-N1B2I requires the executable loop

```text
SOURCE.PHASE_INTENTION.CHARGE_ENERGY.ROUNDTRIP

J_I
  -> H_Phi = J_I / Delta_tau
  -> J_I' = Delta_tau H_Phi
```

with

```text
Delta_tau > 0
invariant: SOURCE.INTENTION_ACTION_CHARGE
normalization: epsilon_I = 1/Delta_tau
```

The PNCS receipt must retain the exact `Delta_tau` parameter, state defect, invariant defect and inverse lineage.

The larger source path is then staged as

```text
phase-intention J_I
  -> phase energy H_Phi
  -> [Q_Sigma <-> J_I binding]
  -> epsilon_Q=1/Delta_tau
  -> RFC source-mass coordinate M_Q
  -> local current/source density after current lift
  -> RF-N1C coupling/universality audit
```

## 7. Advancement state

```text
IDT 01Y Floquet charge-energy identity         PASS
energy/action-charge epsilon_I=1/Delta_tau     PASS
RF-N1B2H extensive mass algebra                PASS
Q_Sigma <-> J_I carrier binding                OPEN
J_I <-> local conserved-current lift           OPEN
p_IDT <-> p_Q physical state-space binding     OPEN
RF-N1C source coupling/universality             OPEN
```

The preferred next derivation target is the finite-charge ↔ local-current lift, because it would turn the exact Floquet energy/action-charge coordinate into a local source-density transport that can be audited in the full IDT ↔ PNCS ↔ RFC physical-law loop.
