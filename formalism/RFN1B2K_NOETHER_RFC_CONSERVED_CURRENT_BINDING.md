# RF-N1B2K — Noether ↔ RFC Conserved-Current Binding Gate

Status: `EXACT_DEFECT_THEOREM_PASS / COMMON_SLICE_MEASURE_ORIENTATION_EXPLICIT / LOCAL_CURRENT_BINDING_PASS_CONDITIONAL / RFC_PHYSICAL_PROMOTION_OPEN`

RF-N1B2K follows RF-N1B2J and consumes IDT 01AA. It tests whether the RFC source carrier and the finite Euler–Noether phase charge are the same conserved carrier on one pinned spatial slice.

The target is

\[
\boxed{
Q_\Sigma
\stackrel{?}{\longleftrightarrow}
Q_\vartheta
=\int_\Sigma n_\mu J_\vartheta^\mu\,dV_h.
}
\]

## 1. Common slice, orientation and finite-cell support

Choose one oriented slice with ordered cells \(C_a\). The Noether representation carries

\[
j_{\vartheta,a},\qquad V_a^{(\vartheta)}>0,
\]

and RFC carries

\[
j_{Q,a},\qquad V_a^{(Q)}>0.
\]

The interface requires exact agreement of `slice_id`, normal-orientation identifier, semantic measure identifier and ordered `cell_ids` before current promotion.

The positive finite charges are

\[
\boxed{
Q_\vartheta=\sum_aV_a^{(\vartheta)}j_{\vartheta,a}>0,
\qquad
Q_\Sigma=\sum_aV_a^{(Q)}j_{Q,a}>0.
}
\]

## 2. Independent local-current and measure defects

Define

\[
\boxed{
\Delta_J
=
\frac{\sum_aV_a^{(Q)}|j_{Q,a}-j_{\vartheta,a}|}{Q_\vartheta}
}
\]

and

\[
\boxed{
\Delta_V
=
\frac{\sum_a|V_a^{(Q)}-V_a^{(\vartheta)}|\,|j_{\vartheta,a}|}{Q_\vartheta}.
}
\]

The extensive-charge mismatch is

\[
\boxed{
\Delta_\Sigma
=
\frac{|Q_\Sigma-Q_\vartheta|}{Q_\vartheta}.
}
\]

The current and measure defects remain separate coordinates, so a measure choice cannot hide a current mismatch.

## 3. Exact defect theorem

Cellwise,

\[
V_a^{(Q)}j_{Q,a}-V_a^{(\vartheta)}j_{\vartheta,a}
=
V_a^{(Q)}(j_{Q,a}-j_{\vartheta,a})
+(V_a^{(Q)}-V_a^{(\vartheta)})j_{\vartheta,a}.
\]

Therefore

\[
\boxed{
\Delta_\Sigma\le\Delta_J+\Delta_V.
}
\]

Consequently,

\[
\Delta_J=0,
\qquad
\Delta_V=0
\]

implies

\[
\boxed{Q_\Sigma=Q_\vartheta.}
\]

This is the exact conditional closure needed before RF-N1B2K can pass the finite-carrier identity downstream.

## 4. Integrated equality is insufficient

For

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
\Delta_\Sigma=0,
\qquad
\Delta_J=1/2.
\]

Thus

\[
\boxed{
\Delta_\Sigma=0
\not\Rightarrow
\Delta_J=0.
}
\]

RFC does not promote a local current identity from equality of integrated totals alone.

## 5. Normalized carrier profile

On the positive sector,

\[
p_{\vartheta,a}
=\frac{V_a^{(\vartheta)}j_{\vartheta,a}}{Q_\vartheta},
\qquad
p_{Q,a}
=\frac{V_a^{(Q)}j_{Q,a}}{Q_\Sigma}.
\]

Under exact current and measure binding,

\[
\boxed{p_{Q,a}=p_{\vartheta,a}.}
\]

This supplies the phase-current profile needed by the later `p_IDT ↔ p_Q` state-space gate.

## 6. Side-flux conservation

Carry the side-flux coordinate \(F_{\rm side}\) with

\[
\boxed{\Delta_F=|F_{\rm side}|.}
\]

Exact cross-slice conservation uses zero side flux, periodic boundary conditions, or an admitted sufficient-decay equivalent.

## 7. Downstream epsilon and mass coordinate

RF-N1B2J supplies

\[
\epsilon_N^{EB}=\frac{H_\Phi^{EB}}{Q_\vartheta}.
\]

Once the physical current/measure identity admits

\[
Q_\Sigma=Q_\vartheta,
\]

the RFC carrier coordinate receives

\[
\boxed{
\epsilon_Q\stackrel{?}{=}\epsilon_N^{EB}
=\frac{H_\Phi^{EB}}{Q_\Sigma}.
}
\]

and

\[
\boxed{
M_N
=\frac{\epsilon_QQ_\Sigma}{c^2}
=\frac{H_\Phi^{EB}}{c^2}.
}
\]

## 8. PNCS executable gate

Canonical semantic loop:

```text
SOURCE.PHASE_NOETHER.RFC_CONSERVED_CURRENT.ROUNDTRIP
```

Contract:

```text
PNCS_PNV_NOETHER_RFC_CURRENT_BINDING_V0_1
```

Required audit invariants are

```text
SOURCE.NOETHER_TOTAL_CHARGE
SOURCE.RFC_TOTAL_CHARGE
SOURCE.COMMON_MEASURE_DEFECT
SOURCE.LOCAL_CURRENT_BINDING_DEFECT
SOURCE.TOTAL_CHARGE_BINDING_DEFECT
SOURCE.CURRENT_MEASURE_BOUND_MARGIN
SOURCE.NOETHER_PROFILE_NORM
SOURCE.RFC_PROFILE_NORM
SOURCE.SIDE_FLUX_DEFECT
```

where

\[
\Delta_{\rm bound}
=\max\{0,\Delta_\Sigma-(\Delta_J+\Delta_V)\}
\]

must remain zero within the declared numerical floor.

## 9. Advancement

```text
common slice / normal orientation                 EXPLICIT gate
common semantic measure / ordered cells           EXPLICIT gate
Delta_J                                            PASS exact audit coordinate
Delta_V                                            PASS exact audit coordinate
Delta_Sigma                                        PASS exact audit coordinate
Delta_Sigma <= Delta_J + Delta_V                  PASS EXACT THEOREM
Delta_F                                            PASS audit coordinate
zero local defects -> Q_Sigma=Q_theta             PASS CONDITIONAL
Q_Sigma=Q_theta alone -> local identity            INSUFFICIENT
Q_Sigma <-> Q_theta physical carrier identity     OPEN measured binding
epsilon_Q <-> epsilon_N^EB                        OPEN promotion after carrier identity
p_IDT <-> p_theta physical state-space binding    OPEN
RF-N1C coupling/universality                       OPEN
```
