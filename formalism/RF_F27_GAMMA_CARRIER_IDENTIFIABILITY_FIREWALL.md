# RF-F27 — Gamma_DC / Carrier-Type Identifiability Firewall

Status: `REFERENCE_IMPLEMENTED_AWAITING_CI / GAMMA_OVER_ZETA_SOURCE_IDENTIFIABLE / GAMMA_AND_CARRIER_TYPE_SEPARATELY_DEGENERATE / HORIZON_CROSS_ROUTE_DEFINED`

RF-F27 follows RF-F26. RF-F26 freezes the project BCJ/Wilson/double-copy/carrier inputs before computing the gravitational coupling. RF-F27 asks a narrower question: which part of `Gamma_DC` can actually be identified from the independently constructed RFC source route without using a numerical gravitational target?

## 1. Reduced-scale relation

RFG4G and RF-N1C4 give

\[
\boxed{
\bar M_G
=\frac{\zeta_M\alpha_c\omega_Q}{2\Gamma_{DC}}
}
\]

with

\[
\zeta_M:=\frac{M_\star}{\epsilon_Q}.
\]

Therefore

\[
\boxed{
\frac{\Gamma_{DC}}{\zeta_M}
=\frac{\alpha_c\omega_Q}{2\bar M_G}.
}
\]

Gravity-sensitive observables identify this ratio unless `zeta_M` is independently typed.

## 2. RFC source estimator without numerical G insertion

RF-N1C supplies, in natural units,

\[
G_N
=\frac{\mathcal S_R}{2\pi\omega_Qj_Q}.
\]

Using

\[
G=\frac{1}{8\pi\bar M_G^2},
\]

one obtains directly from the source/current coordinates

\[
\boxed{
\bar M_G^{source}
=\sqrt{\frac{\omega_Qj_Q}{4\mathcal S_R}}
}.
\]

Substitution into the reduced-scale relation gives the G-free identifiability equation

\[
\boxed{
\frac{\Gamma_{DC}}{\zeta_M}
=\alpha_c\sqrt{\frac{\omega_Q\mathcal S_R}{j_Q}}
}.
\]

No numerical value of `G` is inserted or used for selection.

## 3. Exact carrier-type degeneracy

For a fixed independently determined ratio

\[
r_\Gamma:=\frac{\Gamma_{DC}}{\zeta_M},
\]

the two RF-N1C4 surfaces give

```text
KINETIC_CARRIER       zeta_M = 1 -> Gamma_DC = r_Gamma
TOTAL_ONSHELL_REST    zeta_M = 2 -> Gamma_DC = 2 r_Gamma
```

Hence

\[
\boxed{
\Gamma_{DC}^{rest}=2\Gamma_{DC}^{kin}
}
\]

while both branches produce the same `Gamma_DC/zeta_M`, the same reduced gravity scale, and the same gravitational coupling.

Therefore the gravitational/source output cannot select between the two carrier-energy meanings.

## 4. Horizon estimator

RF-N1C3 supplies

\[
\bar M_G^2=M_HT_H.
\]

For logically independent horizon inputs,

\[
\boxed{
\left(\frac{\Gamma_{DC}}{\zeta_M}\right)_H
=\frac{\alpha_c\omega_Q}{2\sqrt{M_HT_H}}
}.
\]

Equating the source and horizon ratio estimators gives

\[
\alpha_c\sqrt{\frac{\omega_Q\mathcal S_R}{j_Q}}
=
\frac{\alpha_c\omega_Q}{2\sqrt{M_HT_H}}.
\]

On the positive sector this is equivalent to

\[
\boxed{
4M_HT_H\mathcal S_R=\omega_Qj_Q
}.
\]

This is exactly the source↔horizon coupling holonomy already present in RF-N1C after using `kappa_H=2 pi T_H`.

## 5. Promotion firewall

RF-F27 keeps the following inputs independent:

- `alpha_c` provenance,
- RFC source-operator receipt,
- RF-F24 current receipt,
- RF-F21 phase-rate receipt,
- `Gamma_DC` provenance,
- carrier-type / `zeta_M` provenance,
- optional horizon provenance.

The gravity output may not select either `Gamma_DC` or `zeta_M`. Source IDs may not collide with the gravity-output receipt ID. Horizon provenance may not reuse the gravity output or the `Gamma_DC` normalization receipt.

## 6. Consequence

The project normalization frontier is reduced to an identifiability statement:

```text
independent source/current/rate + alpha_c
    -> Gamma_DC / zeta_M                         IDENTIFIABLE CONDITIONAL
independent horizon route
    -> same ratio                                INDEPENDENT CROSS-CHECK
kinetic vs total-rest carrier meaning
    -> factor-two Gamma_DC ambiguity             EXACT
independent zeta_M physical typing
    -> absolute Gamma_DC                         NEXT PHYSICAL INPUT
```

RF-F27 therefore prevents an apparent derivation of `Gamma_DC` from silently choosing the physical meaning of `M_star` using the gravity output itself.
