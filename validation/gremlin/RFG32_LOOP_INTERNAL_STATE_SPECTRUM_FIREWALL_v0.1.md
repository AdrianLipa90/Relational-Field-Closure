# RFG32 — Loop Internal-State Spectrum Firewall

Status: `T_CHANNEL_UNITARITY_CUT_PASS / RAW_DOUBLE_COPY_MIXED_HELICITY_ZERO_SECTOR_NONZERO / PURE_SPIN2_PROJECTOR_REQUIRED / LOOP_EINSTEIN_PROMOTION_OPEN`

RFG32 consumes the tree-level pure-spin-2 factorization result of RFG31 and asks whether the same state isolation persists automatically in a loop unitarity cut.

## 1. Two-particle t-channel cut

Use four external pure-spin-2 states in the `(--++)` sector and cut two massless internal lines in the t channel. In each Yang–Mills copy, both cut subamplitudes must be MHV. The allowed internal helicity assignments for one copy are therefore

\[
\boxed{(+,-),\qquad(-,+)}.
\]

The two Yang–Mills copies choose these assignments independently.

## 2. Tensor-product state classes

For matched assignments, the two copies produce helicity-two states on each internal line:

\[
(+,+)\mapsto +2,\qquad(-,-)\mapsto -2.
\]

For crossed assignments, they produce helicity-zero tensor-product states:

\[
\boxed{(+,-)\mapsto0,\qquad(-,+)\mapsto0.}
\]

These mixed states are absent in the selected tree residue of RFG31 but are kinematically allowed in the loop state sum.

## 3. Cut decomposition

Let `x_A` and `x_B` denote the nonzero one-copy cut products associated with internal assignments `(+,-)` and `(-,+)`. The raw tensor-product double-copy state sum is

\[
\boxed{\mathcal C_{raw}=(x_A+x_B)^2.}
\]

Separating matched spin-two and mixed helicity-zero sectors gives

\[
\boxed{\mathcal C_{spin2}=x_A^2+x_B^2},
\]

\[
\boxed{\mathcal C_{mixed}=2x_Ax_B},
\]

hence

\[
\boxed{\mathcal C_{raw}=\mathcal C_{spin2}+\mathcal C_{mixed}}.
\]

The executable witness finds `x_A != 0`, `x_B != 0`, and therefore

\[
\boxed{\mathcal C_{mixed}\neq0}
\]

on generic exact massless momentum-conserving complex cut kinematics.

## 4. Promotion consequence

RFG31 remains a valid tree-level pure-spin-2 factorization gate. RFG32 establishes that the corresponding loop state isolation is not automatic for the raw `YM x YM` tensor-product state sum. A loop-level Einstein promotion therefore requires an explicit internal-state projection or an equivalent subtraction/cancellation mechanism whose action on all cuts is independently validated.

## 5. Executable validation

Fresh live-surface local result:

```text
6 passed, 0 failed
```

The tests verify exact cut kinematics, nonzero one-copy assignments, tensor-product helicity classification, nonzero mixed cut terms, exact raw=`spin2+mixed` decomposition, and a generic difference between raw and pure-spin-2 projected cuts.

## 6. Advancement

```text
RFG31 tree internal pure-spin2 selection                 PASS
RFG32 generic loop mixed-state witness                   PASS FIREWALL
raw YM x YM loop pure-spin2 closure                      FAIL-CLOSED / OPEN
explicit internal-state projector                        NEXT RFG33
projected-cut Ward/factorization audit                   FOLLOWING
loop integrand / integrated amplitude                    OPEN
```
