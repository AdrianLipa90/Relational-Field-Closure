# RF-S11 — Qubit Informational-Completeness Tetrahedral Scope Selection

Status: `EXACT_QUBIT_IC_LOWER_BOUND / EXACT_TETRA_SIC_RECONSTRUCTION / FULL_TETRA_SCOPE_SELECTED_ON_IC_BRANCH / PROJECTIVE_SPATIAL_SOURCE_BINDING_OPEN`

RF-S11 is stacked on RF-S10. It consumes the exact TIR qubit tetrahedral informational-completeness theorem together with the discrete projective scope contract introduced by RF-S10.

TIR source pinned for this gate:

`AdrianLipa90/The-Fundamental-Theory-of-Informational-Relations@ccc89fc06bdf42c1937c0a2303d3e477db487e0f`

Source theorem:
`TIR/foundations/TIR_QUBIT_TETRAHEDRAL_INFORMATIONAL_COMPLETENESS_V0_1.md`.

RF-S11 selects a projective scope on the branch whose local information carrier is required to be the minimal symmetric informationally complete probe of a generic qubit state.

## 1. Qubit information dimension

For

\[
\mathcal H_2\cong\mathbb C^2,
\]

a normalized density operator has Bloch form

\[
\rho=\frac12(I+\mathbf r\cdot\boldsymbol\sigma),
\qquad |\mathbf r|\le1.
\]

The trace condition leaves three independent real Bloch coordinates.

A normalized measurement with `m` probabilities has at most

\[
\boxed{m-1}
\]

independent real coordinates. Informational completeness for a generic qubit therefore requires

\[
\boxed{m-1\ge3,}
\]

hence

\[
\boxed{m\ge4.}
\]

Four is the minimal outcome count on this branch.

## 2. Exact tetrahedral SIC realization

Let the four unit Bloch vectors obey

\[
\sum_{a=1}^4\mathbf n_a=0,
\qquad
\mathbf n_a\cdot\mathbf n_b=-\frac13\quad(a\ne b).
\]

Define

\[
E_a=\frac14(I+\mathbf n_a\cdot\boldsymbol\sigma).
\]

TIR gives

\[
\sum_{a=1}^4E_a=I
\]

and, for

\[
p_a=\operatorname{Tr}(\rho E_a),
\]

the exact reconstruction

\[
\boxed{
\mathbf r=3\sum_{a=1}^4p_a\mathbf n_a.
}
\]

Thus the four tetrahedral outcome directions saturate the lower bound `m=4` and carry the complete three-real-coordinate qubit state.

## 3. RF-S10 scope/outcome contract

RF-S10 admits the canonical tetrahedral projective scopes

```text
FACE             -> one geodesic tetrahedral face
FULL_TETRA_CP1   -> all four geodesic tetrahedral faces
```

For the informational-outcome ownership used by RF-S11, the scope carries the tetrahedral vertices incident to that canonical object:

```text
FACE             -> 3 tetrahedral outcome directions
FULL_TETRA_CP1   -> 4 tetrahedral outcome directions
```

Hence their normalized probability-coordinate capacities are

\[
\boxed{d_{prob}^{FACE}=3-1=2,}
\]

and

\[
\boxed{d_{prob}^{FULL}=4-1=3.}
\]

The target generic qubit state dimension is

\[
\boxed{d_{qubit}=3.}
\]

## 4. Exact scope selection on the minimal-IC branch

Define the RF-S11 admission condition:

```text
local carrier = generic qubit C^2 state
measurement = normalized symmetric tetrahedral probe
selection target = minimal informational completeness
scope contract = RF-S10 {FACE, FULL_TETRA_CP1}
```

The capacity comparison is then

\[
d_{prob}^{FACE}=2,
\qquad
d_{prob}^{FULL}=3=d_{qubit}.
\]

Together with the exact TIR four-outcome reconstruction, the RF-S10 selector is fixed to

\[
\boxed{
\mathrm{scope}_{IC}=\mathrm{FULL\_TETRA\_CP1}.
}
\]

The corresponding canonical projective area is therefore

\[
\boxed{a_{FS}^{IC}=\pi.}
\]

This is an informational-completeness scope theorem inside the RF-S10 tetrahedral projective contract.

## 5. IDT 01K consequence

Using the RF-S10 / IDT 01K constant-rate map,

\[
\mathcal A_{rel}=\frac{c^2}{\omega^2}a_{FS},
\]

RF-S11 gives on the minimal-IC constant-rate branch

\[
\boxed{
\mathcal A_{IC}
=\frac{\pi c^2}{\omega^2}.
}
\]

For a supplied natural-log information numerator `J`,

\[
\boxed{
\Xi_{IC}
=\frac{\mathcal J}{\pi}
\left(\frac{\omega}{c}\right)^2.
}
\]

Thus the RF-S9 common-area owner and RF-S10 discrete scope reduce to the full tetrahedral `CP1` area whenever the admitted local information probe carries the minimal complete qubit SIC data.

## 6. Reconstruction receipt

An executable IC receipt records

```text
carrier_dimension = 2
bloch_real_dimension = 3
scope
outcome_count
probability_coordinate_capacity = outcome_count - 1
tetrahedral probability vector p_1..p_4
reconstructed Bloch vector
input/reference Bloch vector when available
reconstruction defect
```

For exact tetrahedral probabilities,

\[
\Delta_r
:=\|\mathbf r_{recon}-\mathbf r_{input}\|_2
\]

vanishes up to numerical precision.

The dimension selector and reconstruction test are independent checks:

```text
m >= 4                         dimension lower-bound gate
r = 3 sum_a p_a n_a           tetrahedral reconstruction gate
```

## 7. Projective/spatial type ledger

RF-S11 promotes the full tetrahedral projective scope on the minimal-IC qubit branch. The TIR spatial tetrahedral carrier retains its dedicated source-binding gate.

The current typed chain is

```text
C^2 generic qubit
-> 3 real Bloch coordinates
-> minimal normalized IC outcome count 4
-> tetrahedral SIC directions
-> RF-S10 FULL_TETRA_CP1 projective scope
-> a_FS = pi
-> IDT 01K A_rel = pi c^2/omega^2
```

The projective-to-spatial source promotion remains downstream as its own gate.

## 8. Promotion ledger

```text
qubit Bloch real dimension = 3                       PASS EXACT
normalized m-outcome capacity = m-1                 PASS EXACT
minimal qubit IC outcome count m=4                  PASS EXACT
four tetrahedral POVM elements sum to identity      PASS EXACT
tetrahedral reconstruction r=3 sum p_a n_a          PASS EXACT
RF-S10 FACE outcome capacity = 2                    PASS EXACT
RF-S10 FULL outcome capacity = 3                    PASS EXACT
minimal-IC scope = FULL_TETRA_CP1                    PASS EXACT ON IC BRANCH
a_FS^IC = pi                                        PASS EXACT
IDT 01K A_IC = pi c^2/omega^2                       PASS EXACT
```

Remaining gates:

```text
PHYSICAL_MINIMAL_IC_CARRIER_SELECTION
TIR_PROJECTIVE_TO_SPATIAL_CELL_SOURCE_BINDING
PHYSICAL_JOINT_INFORMATION_STATE_BINDING
ABSOLUTE_ALPHA_NORMALIZATION
PHYSICAL_RADIAL_ZERO_DEFECT_DATA
RADIAL_BINDING_DYNAMICAL_TRANSPORT
TRANSLATIONAL_OBSERVABLE
DIRECTIONAL_CUBIC_TEST
GENERAL_MATTER_MULTIPLET
GLOBAL_INFORMATION_GEODESIC_EXTENSION
```

## 9. Validation authority

Reference implementation: `src/rfc/qubit_ic_full_tetra_scope_selection.py`.
Reference tests: `tests/reference/test_rfs11_qubit_ic_full_tetra_scope_selection.py`.
Validation receipt: `validation/RF_S11_QUBIT_IC_FULL_TETRA_SCOPE_SELECTION_V0_1.json`.

Stack parent: RF-S10 head `85384de31a8300e688e55735e67a077d6b11e3e0`.
