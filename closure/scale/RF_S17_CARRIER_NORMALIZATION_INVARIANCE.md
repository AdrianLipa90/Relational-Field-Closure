# RF-S17 — Carrier-Normalization Invariance

Status: `EXACT_Q0_RESCALING_INVARIANCE / SOURCE_DENSITY_Q0_INDEPENDENT / PROFILE_INVARIANT`

RF-S17 is stacked on exact-green RF-S16. RF-S16 gives

\[
 j_Q=q_0\frac{\mathcal N}{V_R},
\qquad
\epsilon_Q=\frac{\epsilon_{occ}}{q_0},
\qquad
\rho_G=\epsilon_Q j_Q,
\]

with

\[
\epsilon_{occ}=B\omega(\phi+\kappa).
\]

RF-S17 isolates the normalization freedom carried by the arbitrary positive carrier unit \(q_0\).

## 1. Positive carrier rescaling

For any \(\lambda>0\), define

\[
\boxed{q_0' = \lambda q_0.}
\]

The corresponding current coordinate becomes

\[
\boxed{j_Q'=\lambda j_Q}
\]

while energy per charge becomes

\[
\boxed{\epsilon_Q'=\epsilon_Q/\lambda.}
\]

Therefore

\[
\boxed{
\epsilon_Q'j_Q'
=\epsilon_Qj_Q
=\rho_G.
}
\]

The physical source energy density is exactly invariant under carrier-unit rescaling.

## 2. Extensive charge and profile

The extensive charge scales as

\[
\boxed{Q_\Sigma'=\lambda Q_\Sigma.}
\]

But the normalized profile

\[
p_{Q,a}=\frac{V_a j_{Q,a}}{Q_\Sigma}
\]

satisfies

\[
\boxed{p'_{Q,a}=p_{Q,a}.}
\]

Together with RF-S16,

\[
\boxed{
p_{Q,a}=p_{\mathcal N,a}}
\]

for every positive carrier normalization.

## 3. Source density without q0

Combining the rescaling pair gives

\[
\boxed{
\rho_G
=\frac{\mathcal N}{V_R}\epsilon_{occ}
}
\]

with no remaining \(q_0\).

Equivalently,

\[
\boxed{
\rho_G
=\frac{B\omega\mathcal N}{V_R}(\phi+\kappa).
}
\]

Thus the carrier quantum is required only to assign an absolute unit to the conserved-current coordinate. It is not required for the generator source density itself.

## 4. Full tetrahedral specialization

RF-S15 gives

\[
V_R=\frac{\pi c^3}{|\omega|^3}.
\]

Therefore

\[
\boxed{
\rho_G
=\frac{B\mathcal N}{\pi c^3}\omega|\omega|^3(\phi+\kappa)
}
\]

independently of the carrier-current normalization.

On the positive-frequency branch,

\[
\boxed{
\rho_G
=\frac{B\mathcal N\omega^4}{\pi c^3}(\phi+\kappa).
}
\]

## 5. Current-binding consequence

A physical RF-N1B2K current receipt may be expressed in any fixed positive charge convention. If two descriptions differ only by a global positive carrier-unit factor, their absolute current numbers differ but their occupation profile and source energy density coincide after the reciprocal energy-per-charge transformation.

The invariant comparison objects are therefore

\[
\boxed{p_Q}
\]

and

\[
\boxed{\rho_G=\epsilon_Qj_Q.}
\]

Absolute \(q_0\) remains relevant only when the project requires an independently normalized physical charge value.

## 6. Advancement

```text
q0 -> lambda q0                                      PASS EXACT
j_Q -> lambda j_Q                                    PASS EXACT
energy/charge -> (energy/charge)/lambda              PASS EXACT
rho_G invariant                                      PASS EXACT
Q_Sigma -> lambda Q_Sigma                            PASS EXACT
normalized current profile invariant                 PASS EXACT
rho_G independent of q0                              PASS EXACT
absolute physical current-charge unit                OPEN INPUT WHEN REQUIRED
physical local current/profile receipt               OPEN RF-N1B2K INPUT
```

## 7. Validation authority

Reference implementation: `src/rfc/carrier_normalization_invariance.py`.
Reference tests: `tests/reference/test_rfs17_carrier_normalization_invariance.py`.
Validation receipt: `validation/RF_S17_CARRIER_NORMALIZATION_INVARIANCE_V0_1.json`.

Stack parent: RF-S16 exact-green head `71d4762a5a1396d75a8db5454db56ec4c0998319`, RFC reference suite #282 SUCCESS.
