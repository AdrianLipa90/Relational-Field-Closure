# RFG34 — Projected Loop-Cut Channel Covariance Gate

Status: `S_T_U_CUT_KINEMATICS_PASS / HELICITY_CHANNEL_SELECTION_PASS / PROJECTOR_CHANNEL_COVARIANCE_PASS / MIXED_SECTOR_TU_REMOVAL_EXACT / S_CHANNEL_AUTOMATIC_SPIN2_PASS / VECTOR_WARD_AUDIT_OPEN`

RFG34 consumes the explicit RFG33 internal pure-spin-2 projector and tests whether its state-selection rule behaves coherently across the three two-particle channel pairings of the external `(--++)` four-point sector.

## 1. Channel pairings

With external helicities

\[
(h_1,h_2,h_3,h_4)=(-,-,+,+),
\]

use the pairings

\[
s:(1,2)\mid(3,4),\qquad
t:(1,3)\mid(2,4),\qquad
u:(1,4)\mid(2,3).
\]

For each channel the executable gate constructs exact complex massless cut kinematics and verifies momentum conservation independently on the left and right four-point subamplitudes.

## 2. Helicity-selection asymmetry

Requiring both cut subamplitudes in a Yang-Mills copy to lie on the four-point MHV support gives:

\[
\boxed{s:\;(-,-)}
\]

as the unique internal assignment in the frozen orientation, whereas

\[
\boxed{t,u:\;(+,-),\;(-,+)}.
\]

Thus the `s` channel has only one one-copy internal assignment and its double copy is already matched-spin-two on this external helicity sector.

The crossed `t` and `u` channels admit the two one-copy assignments diagnosed in RFG32, so their raw independent-copy sums contain the crossed helicity-zero sector.

## 3. Projected channel sums

For `t` or `u`, let `x_A,x_B` be the two one-copy cut products. RFG33 gives

\[
\boxed{\mathcal C_{projected}=x_A^2+x_B^2}
\]

and RFG34 verifies on both channels

\[
\boxed{\mathcal C_{raw}-\mathcal C_{projected}=2x_Ax_B}.
\]

For the `s` channel there is one allowed product `x_s`, hence

\[
\boxed{\mathcal C_{raw}^{(s)}=\mathcal C_{projected}^{(s)}=x_s^2}.
\]

Therefore the projector acts only where the tensor-product state sum actually enlarges the internal spectrum.

## 4. State-space covariance

In the one-line tensor-product basis

\[
\{|++\rangle,|+-\rangle,|-+\rangle,|--\rangle\},
\]

RFG33 uses

\[
P_2=\operatorname{diag}(1,0,0,1).
\]

RFG34 verifies that `P2` commutes with:

- exchange of the two Yang-Mills copies,
- simultaneous helicity reversal in both copies,
- admissible state-coordinate relabelings that preserve matched versus crossed tensor-product sectors.

Hence the cut projection is a state-subspace statement rather than an artifact of the labels `A/B` or of one channel name.

## 5. Executable validation

Fresh live-surface local result:

```text
6 passed, 0 failed
```

The tests verify exact three-channel helicity counts, exact cut momentum compatibility, automatic `s`-channel spin-two selection, nonzero `t/u` mixed sectors with exact subtraction, projector covariance under copy exchange and helicity reversal, and commutation with admissible channel state-coordinate relabelings.

## 6. Advancement

```text
RFG32 raw-loop mixed internal-state witness                 PASS FIREWALL
RFG33 explicit pure-spin2 cut projector                     PASS
RFG34 s/t/u channel helicity-selection audit                PASS
RFG34 t/u mixed-sector removal                              PASS
RFG34 s-channel automatic matched-sector selection          PASS
vector-polarization projected-cut Ward audit                NEXT RFG35
projected loop-integrand realization                        OPEN
integrated loop amplitude                                   OPEN
```

RFG34 is a channel-covariance and factorization-state gate. It does not replace the separate vector-polarization Ward audit required before loop-integrand promotion.
