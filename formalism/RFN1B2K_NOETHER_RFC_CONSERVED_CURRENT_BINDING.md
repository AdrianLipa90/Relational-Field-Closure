# RF-N1B2K — Noether ↔ RFC Conserved-Current Binding Gate

Status: `COMMON_SLICE_MEASURE_EXPLICIT / LOCAL_CURRENT_BINDING_PASS_CONDITIONAL / TOTAL_CHARGE_BINDING_PASS_CONDITIONAL / RFC_PHYSICAL_PROMOTION_OPEN`

RF-N1B2K follows RF-N1B2J and consumes IDT 01AA. It tests the RFC carrier identity against the local Noether normal current before promoting the integrated charge identity.

The target relation is

\[
\boxed{
Q_\Sigma
\stackrel{?}{\longleftrightarrow}
Q_\vartheta
=\int_\Sigma n_\mu J_\vartheta^\mu\,dV_h.
}
\]

## 1. Common slice and finite-cell measure

Choose one oriented spatial slice \(\Sigma\) and ordered cells \(C_a\) with

\[
V_a=\int_{C_a}dV_h>0.
\]

The interface pins

```text
slice_id
measure_id
ordered cell_ids
cell volumes V_a
```

on both sides.

The semantic measure identifier and ordered cell identifiers must agree exactly. The numerical measure defect is

\[
\boxed{
\Delta_V
=\frac{\sum_a|V_a^{(\vartheta)}-V_a^{(Q)}|}
{\sum_aV_a^{(\vartheta)}}.
}
\]

## 2. Local currents and finite charges

The Noether side supplies

\[
j_{\vartheta,a}
\]

from

\[
J_\vartheta^\mu=2A^2\partial^\mu\vartheta,
\]

while RFC supplies independent carrier-current samples

\[
j_{Q,a}.
\]

The finite charges are

\[
\boxed{
Q_\vartheta=\sum_aV_a j_{\vartheta,a},
\qquad
Q_\Sigma=\sum_aV_a j_{Q,a}.
}
\]

## 3. Local-current binding defect

Define

\[
\boxed{
\Delta_{\rm local}
=\frac{\sum_aV_a|j_{Q,a}-j_{\vartheta,a}|}
{Q_\vartheta}.
}
\]

This is the primary physical-current gate.

Equality of totals is weaker. For

\[
j_\vartheta=(1,3),
\qquad
j_Q=(2,2),
\qquad
V=(1,1),
\]

we obtain

\[
Q_\vartheta=Q_\Sigma=4,
\qquad
\Delta_{\rm local}=1/2.
\]

Therefore integrated equality alone is not sufficient for RF-N1B2K promotion.

## 4. Integrated-charge defect

Define

\[
\boxed{
\Delta_Q
=\frac{|Q_\Sigma-Q_\vartheta|}{Q_\vartheta}.
}
\]

On the exact common measure,

\[
\Delta_{\rm local}=0
\Longrightarrow
\Delta_Q=0.
\]

The reverse implication is not used as a physical binding criterion.

## 5. Side-flux conservation gate

RF-N1B2 conservation uses the zero-side-flux sector. Carry

\[
F_{\rm side}
\]

with

\[
\boxed{\Delta_F=|F_{\rm side}|.}
\]

Exact conserved-current binding uses \(\Delta_F=0\).

## 6. Downstream epsilon binding

RF-N1B2J supplies

\[
\epsilon_N^{EB}=\frac{H_\Phi^{EB}}{Q_\vartheta}.
\]

Once RF-N1B2K admits

\[
Q_\Sigma=Q_\vartheta,
\]

the RFC energy conversion gate becomes

\[
\boxed{
\epsilon_Q\stackrel{?}{=}\epsilon_N^{EB}
=\frac{H_\Phi^{EB}}{Q_\Sigma}.
}
\]

The corresponding source-mass coordinate is

\[
\boxed{
M_N
=\frac{\epsilon_N^{EB}Q_\Sigma}{c^2}
=\frac{H_\Phi^{EB}}{c^2}.
}
\]

## 7. PNCS executable gate

Semantic loop:

```text
SOURCE.PHASE_NOETHER.RFC_CONSERVED_CURRENT.ROUNDTRIP
```

Contract:

```text
PNCS_PNV_NOETHER_RFC_CURRENT_BINDING_V0_1
```

Required invariants:

```text
SOURCE.NOETHER_TOTAL_CHARGE
SOURCE.RFC_TOTAL_CHARGE
SOURCE.COMMON_MEASURE_DEFECT
SOURCE.LOCAL_CURRENT_BINDING_DEFECT
SOURCE.TOTAL_CHARGE_BINDING_DEFECT
SOURCE.SIDE_FLUX_DEFECT
```

## 8. Advancement

```text
common slice / semantic measure                    EXPLICIT gate
ordered cell partition                             EXPLICIT gate
Delta_V                                             PASS audit coordinate
Delta_local                                         PASS audit coordinate
Delta_Q                                             PASS audit coordinate
Delta_F                                             PASS audit coordinate
Q_Sigma <-> Q_theta                                PASS_CONDITIONAL at zero defects
epsilon_Q <-> epsilon_N^EB                        OPEN physical promotion
RF-N1C coupling/universality                       OPEN
```
