# RF-S16 — Orbital Occupation ↔ Conserved Noether Current Binding

Status: `EXACT_FINITE_CELL_OCCUPATION_CURRENT_MAP / EXACT_PROFILE_IDENTITY / CURRENT_FORM_SOURCE_REDUCTION`

RF-S16 is stacked on exact-green RF-S15. RF-S13/RF-S15 use the occupation variable \(\mathcal N\) in the relational generator

\[
\rho_G
=
\frac{B\omega\mathcal N}{AR}(\phi+\kappa),
\qquad
\kappa=\frac{\ln2}{24\pi}.
\]

RF-N1B2 and RF-N1B2K independently supply the conserved-current source ledger. RF-S16 identifies the exact finite-cell interface between these representations after a carrier quantum \(q_0>0\) and a common cell measure are supplied.

## 1. Cellwise occupation-current map

For each cell \(C_a\) with physical volume \(V_a>0\), occupation \(\mathcal N_a\ge0\), and carrier quantum \(q_0>0\), define

\[
\boxed{
 j_{Q,a}=q_0\frac{\mathcal N_a}{V_a}.
}
\]

Equivalently,

\[
\boxed{
\mathcal N_a=\frac{V_a j_{Q,a}}{q_0}.
}
\]

Thus occupation and local conserved-current density are exact inverse coordinates once \(q_0\) and the cell volume are fixed.

## 2. Extensive carrier identity

The finite-slice charge is

\[
Q_\Sigma
=\sum_a V_a j_{Q,a}.
\]

Substituting the occupation-current map gives

\[
\boxed{
Q_\Sigma=q_0\sum_a\mathcal N_a.
}
\]

Define

\[
\mathcal N_\Sigma:=\sum_a\mathcal N_a.
\]

Then

\[
\boxed{Q_\Sigma=q_0\mathcal N_\Sigma.}
\]

For the unit-charge bookkeeping branch \(q_0=1\), the extensive conserved charge equals total orbital occupation.

## 3. Exact normalized-profile identity

RF-N1B2K uses

\[
p_{Q,a}=\frac{V_a j_{Q,a}}{Q_\Sigma}.
\]

The occupation representation gives

\[
p_{\mathcal N,a}
=\frac{\mathcal N_a}{\mathcal N_\Sigma}.
\]

Using the exact cellwise map,

\[
\boxed{
p_{Q,a}=p_{\mathcal N,a}.}
\]

The cell volumes and carrier quantum cancel. Therefore the normalized conserved-current profile is exactly the normalized orbital-occupation profile.

## 4. Local-current binding audit

Let \(j_{obs,a}\) be an independently supplied Noether/RFC current density on the same ordered cells and measure. Define the occupation-predicted current

\[
 j_{pred,a}=q_0\frac{\mathcal N_a}{V_a}.
\]

With positive predicted total charge, define

\[
\boxed{
\Delta_J
=
\frac{\sum_aV_a|j_{obs,a}-j_{pred,a}|}{Q_{pred}}
}
\]

and

\[
\boxed{
\Delta_\Sigma
=
\frac{|Q_{obs}-Q_{pred}|}{Q_{pred}}.
}
\]

The triangle inequality gives exactly

\[
\boxed{
\Delta_\Sigma\le\Delta_J.
}
\]

Hence exact local binding implies exact extensive-charge binding. Equality of integrated totals alone remains insufficient, consistently with RF-N1B2K.

## 5. Generator rewritten directly in current form

Since

\[
\frac{\mathcal N}{AR}=\frac{j_Q}{q_0},
\]

RF-S13 becomes

\[
\boxed{
\rho_G
=
\frac{B\omega}{q_0}(\phi+\kappa)j_Q.
}
\]

Define the energy per conserved carrier charge

\[
\boxed{
\epsilon_Q
:=
\frac{B\omega}{q_0}(\phi+\kappa).
}
\]

Then

\[
\boxed{
\rho_G=\epsilon_Qj_Q.
}
\]

This is exactly the RF-N1B2 continuous source factorization, now expressed through the orbital occupation variable of the relational generator.

## 6. Phase-clock full-tetra specialization

RF-S15 gives on `FULL_TETRA_CP1`

\[
V_R=AR=\frac{\pi c^3}{|\omega|^3}.
\]

Therefore

\[
\boxed{
 j_Q
=
\frac{q_0\mathcal N|\omega|^3}{\pi c^3}.
}
\]

For positive frequency,

\[
\boxed{
 j_Q
=
\frac{q_0\mathcal N\omega^3}{\pi c^3}.
}
\]

Multiplying this by

\[
\epsilon_Q
=\frac{B\omega}{q_0}(\phi+\kappa)
\]

reproduces the RF-S15 fourth-power source law exactly:

\[
\boxed{
\rho_G
=
\frac{B\mathcal N\omega^4}{\pi c^3}(\phi+\kappa).
}
\]

Thus the \(\omega^4\) source scaling decomposes into

\[
\boxed{
\omega^3\ \text{current-density scaling}
\times
\omega\ \text{energy-per-charge scaling}.
}
\]

## 7. Noether-current consequence

RF-N1B2K compares the RFC current to the Euler-Noether current on a common slice. Once its local current and measure defects vanish,

\[
\boxed{j_Q=j_\vartheta.}
\]

RF-S16 then gives

\[
\boxed{
\mathcal N_a
=\frac{V_a j_{\vartheta,a}}{q_0}.
}
\]

Hence an admitted Noether-current field reconstructs the orbital occupation directly cell by cell.

The relational source can then be written as

\[
\boxed{
\rho_G
=\epsilon_Qj_\vartheta
}
\]

on the same bound current surface.

## 8. Advancement

```text
N_a <-> V_a j_Q,a/q0                              PASS EXACT
Q_Sigma=q0 sum_a N_a                              PASS EXACT
normalized occupation profile = current profile   PASS EXACT
Delta_Sigma <= Delta_J                            PASS EXACT
rho_G=(B omega/q0)(phi+kappa) j_Q                 PASS EXACT
rho_G=epsilon_Q j_Q                               PASS EXACT
full-tetra j_Q proportional to |omega|^3          PASS EXACT
positive-rate rho_G proportional to omega^4       PASS EXACT PARENT ROUNDTRIP
j_Q <-> j_theta physical local binding             OPEN RF-N1B2K RECEIPT
physical q0 carrier quantum                        OPEN INPUT
physical occupation receipt                        OPEN INPUT
```

## 9. Validation authority

Reference implementation: `src/rfc/occupation_noether_current_binding.py`.
Reference tests: `tests/reference/test_rfs16_occupation_noether_current_binding.py`.
Validation receipt: `validation/RF_S16_OCCUPATION_NOETHER_CURRENT_BINDING_V0_1.json`.

Stack parent: RF-S15 exact-green head `504ae049778e9395821ed39395c1c7a55d17a44d`, RFC reference suite #281 SUCCESS.
