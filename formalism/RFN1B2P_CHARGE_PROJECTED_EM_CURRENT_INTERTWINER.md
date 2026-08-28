# RF-N1B2P — Charge-Projected RFC ↔ Maxwell Current Intertwiner

Status: `EXACT_INTERTWINER_ALGEBRA / SINGLE_CHARGE_COMPOSITION_EXACT / NEUTRAL_SECTOR_NULL_EXACT / MULTIPLET_CHARGE_PROJECTION_EXACT / RF_E6_SIGN_CORRECTION_PASS / PHYSICAL_CURRENT_MATCH_CONDITIONAL`

RF-N1B2P composes the independently audited RFC carrier line with the RF-M4 electromagnetic charge projection. RF-E6 aligns the matter action with the canonical RFC metric signature `(-,+,+,+)` and fixes the Maxwell-current sign used by the intertwiner.

## 1. Typed inputs

RF-N1B2K supplies a falsifiable current/measure comparison

\[
J_{RFC,\vartheta}^{\mu}\stackrel{\Delta_K\to0}{\longleftrightarrow}J_\vartheta^{\mu}.
\]

RF-N1B2O uses the phase carrier before electric-charge projection to build the phase-kinetic matter source,

\[
\rho_\vartheta=\frac{\epsilon_N}{c^2}j_\vartheta.
\]

RF-M4/RF-E6 supplies the microscopic electromagnetic variation current

\[
\boxed{J_{EM}^{\mu}=\frac1\hbar\mathcal J_Q^{\mu}}.
\]

The bridge therefore acts through a charge projector.

## 2. Single-charge sector

For one electric-charge eigenvalue `q`,

\[
\mathcal J_Q^{\mu}=qJ_\vartheta^{\mu},
\]

hence

\[
\boxed{J_{EM}^{\mu}=\frac q\hbar J_\vartheta^{\mu}}.
\]

On the RF-N1B2K zero-defect surface,

\[
J_{RFC,\vartheta}^{\mu}=J_\vartheta^{\mu},
\]

so

\[
\boxed{J_{EM}^{\mu}=\frac q\hbar J_{RFC,\vartheta}^{\mu}}.
\]

The coefficient `q/hbar` is fixed by the same physical charge normalization that appears in the Aharonov–Bohm phase.

## 3. Multiplet sector

Let the admitted carrier resolve into charge sectors `a`, with component currents `J_a^mu` and charge eigenvalues `q_a`. Define

\[
\boxed{
\Pi_Q[J]^{\mu}:=\sum_a q_aJ_a^{\mu}.
}
\]

Then

\[
\boxed{
\mathcal J_Q^{\mu}=\Pi_Q[J]^{\mu},
\qquad
J_{EM}^{\mu}=\frac1\hbar\Pi_Q[J]^{\mu}.
}
\]

The unweighted RFC matter carrier is

\[
J_{RFC}^{\mu}=\sum_aJ_a^{\mu}.
\]

For equal charge `q_a=q`,

\[
\Pi_Q[J]^{\mu}=qJ_{RFC}^{\mu},
\qquad
J_{EM}^{\mu}=\frac q\hbar J_{RFC}^{\mu}.
\]

For unequal charges, the charge-resolved packet is the sufficient input to the Maxwell projection.

## 4. Neutral control

For every component with `q_a=0`,

\[
\boxed{\Pi_Q[J]^{\mu}=0,\qquad J_{EM}^{\mu}=0.}
\]

The unweighted matter carrier and phase-energy source can remain finite, preserving the matter/Maxwell type split.

## 5. Charge-compatibility gate

The RF-M4 matter action requires

\[
\boxed{[\mathcal M^2,Q]=0.}
\]

This keeps the charge decomposition dynamically compatible with the local gauge symmetry. A nonzero commutator is an explicit fail-closed condition for the current intertwiner.

## 6. Gauge covariance

Under

\[
\vartheta' = \vartheta + \frac q\hbar\Lambda,
\qquad
A'=A-d\Lambda,
\]

the gauge-covariant phase one-form

\[
d\vartheta+\frac q\hbar A
\]

is invariant. The corresponding phase carrier and its charge projection therefore share the synchronized RFC/AB gauge convention.

## 7. Executable defects

For a single charge define

\[
\Delta_P
=\frac{2\|J_{EM}-(q/\hbar)J_{RFC,\vartheta}\|}
{\|J_{EM}\|+\|(q/\hbar)J_{RFC,\vartheta}\|}
\]

on the nonzero sector. Reference controls cover:

- exact single-charge composition;
- sign perturbation;
- charge-scale perturbation;
- opposite charge;
- neutral `Q=0`;
- equal-charge multiplet reduction;
- unequal-charge resolved projection;
- `[M^2,Q]` compatibility;
- synchronized gauge shifts;
- vector-dimension and `hbar` fail-closed handling.

RF-E6 adds the independent finite-difference matter-action variation check that fixes the positive `q/hbar` source sign under the canonical RFC Lorentzian convention.

## 8. Advancement

```text
RFC carrier decomposition J_a                         TYPED
charge projector Pi_Q                                 EXACT
J_EM = Pi_Q[J]/hbar                                   PASS EXACT ACTION CONVENTION
single charge J_EM=(q/hbar)J_RFC,theta                PASS EXACT after RF-N1B2K match
neutral Q=0 Maxwell-null control                      PASS EXACT
unequal-charge packet requirement                     PASS EXACT TYPE FIREWALL
[M^2,Q]=0 compatibility                               PASS EXACT CONDITION
physical RF-N1B2K carrier/measure realization         OPEN PHYSICAL GATE
charged-matter stress-energy                          AVAILABLE via RF-E6
total-matter composition                              NEXT EINSTEIN GATE
```
