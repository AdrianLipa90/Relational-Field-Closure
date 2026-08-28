# RF-N1B2P — Charge-Projected RFC ↔ Maxwell Current Intertwiner

Status: `EXACT_INTERTWINER_ALGEBRA / SINGLE_CHARGE_COMPOSITION_EXACT / NEUTRAL_SECTOR_NULL_EXACT / MULTIPLET_CHARGE_PROJECTION_EXACT / PHYSICAL_CURRENT_MATCH_CONDITIONAL`

RF-N1B2P composes the independently audited RFC carrier line with the RF-M4 / IDT 01AG electromagnetic charge projection. The bridge preserves the distinction between the pre-charge phase carrier used by the matter/gravity source sector and the charge-projected current that sources Maxwell.

## 1. Typed inputs

RF-N1B2K supplies a falsifiable current/measure comparison between an independently constructed RFC carrier current and the phase Noether carrier,

\[
J_{RFC,\vartheta}^{\mu}\stackrel{\Delta_K\to0}{\longleftrightarrow}J_\vartheta^{\mu}.
\]

RF-N1B2O uses the phase carrier before electric-charge projection to build the phase-kinetic matter source,

\[
\rho_\vartheta=\frac{\epsilon_N}{c^2}j_\vartheta.
\]

RF-M4 / IDT 01AG supplies the independently typed electromagnetic variation current,

\[
\boxed{J_{EM}^{\mu}=-\frac1\hbar\mathcal J_Q^{\mu}}.
\]

The bridge therefore acts through a charge projector rather than a raw current equality.

## 2. Single-charge sector

For one electric-charge eigenvalue `q`,

\[
\mathcal J_Q^{\mu}=qJ_\vartheta^{\mu},
\]

hence

\[
\boxed{J_{EM}^{\mu}=-\frac q\hbar J_\vartheta^{\mu}}.
\]

On the RF-N1B2K zero-defect surface,

\[
J_{RFC,\vartheta}^{\mu}=J_\vartheta^{\mu},
\]

so the composed RFC→Maxwell intertwiner is

\[
\boxed{J_{EM}^{\mu}=-\frac q\hbar J_{RFC,\vartheta}^{\mu}}.
\]

The coefficient `-q/hbar` is fixed by the same physical charge normalization that appears in the Aharonov–Bohm phase.

## 3. Multiplet sector

Let the admitted carrier resolve into charge sectors `a`, with separately constructed component currents `J_a^mu` and charge eigenvalues `q_a`. Define

\[
\Pi_Q[J]^{\mu}:=\sum_a q_aJ_a^{\mu}.
\]

Then

\[
\boxed{\mathcal J_Q^{\mu}=\Pi_Q[J]^{\mu}},
\qquad
\boxed{J_{EM}^{\mu}=-\frac1\hbar\Pi_Q[J]^{\mu}}.
\]

The unweighted RFC matter carrier is

\[
J_{RFC}^{\mu}=\sum_aJ_a^{\mu}.
\]

If all admitted components share one charge eigenvalue `q`, the projector reduces to

\[
\Pi_Q[J]^{\mu}=qJ_{RFC}^{\mu}.
\]

For unequal charges, the full charge-resolved packet must be retained. This prevents a scalar rescaling of the total RFC carrier from erasing charge composition.

## 4. Neutral control

For an electrically neutral sector,

\[
Q=0,
\]

therefore

\[
\boxed{J_{EM}^{\mu}=0}
\]

while the phase carrier and its phase-kinetic energy density may remain finite. This is an exact source-typing control between the matter/gravity and Maxwell branches.

## 5. Gauge-covariant consistency

With the synchronized RF-M1 convention

\[
\vartheta\to\vartheta+\lambda,
\qquad
A_\mu\to A_\mu-\partial_\mu\Lambda,
\qquad
\lambda=\frac q\hbar\Lambda,
\]

the covariant phase one-form

\[
D_\mu\vartheta=\partial_\mu\vartheta+\frac q\hbar A_\mu
\]

is invariant. Any admitted phase-current construction from this invariant carrier is therefore unchanged by the synchronized gauge shift, and the charge projector commutes with that transformation.

## 6. Charge-compatibility firewall

For a multiplet with mass generator `M^2` and charge operator `Q`, the already admitted charge-preserving sector requires

\[
\boxed{[M^2,Q]=0}.
\]

This condition keeps the charge decomposition stable under the internal dynamics used to construct the component currents. A nonzero commutator is routed to the open charge-mixing sector and is not promoted through the fixed-eigenvalue intertwiner.

## 7. Executable residuals

For a single-charge current packet define

\[
R_{EM}^{\mu}:=J_{EM}^{\mu}+\frac q\hbar J_{RFC,\vartheta}^{\mu}.
\]

A symmetric dimensionless defect is

\[
\boxed{
\Delta_{EM}
=\frac{2\lVert R_{EM}\rVert_2}
{\lVert J_{EM}\rVert_2+\lVert(q/\hbar)J_{RFC,\vartheta}\rVert_2}
}
\]

when the denominator is positive. The neutral sector is tested separately by the exact `Q=0 -> J_EM=0` control.

For a multiplet,

\[
R_{EM,Q}^{\mu}:=J_{EM}^{\mu}+\frac1\hbar\sum_aq_aJ_a^{\mu}.
\]

Promotion requires both the RF-N1B2K carrier-match gate and the RF-N1B2P charge-projection residual to close on independently supplied current packets.

## 8. Adversarial controls

The reference gate must distinguish:

1. correct single-charge sign and normalization;
2. sign-flipped Maxwell coupling;
3. perturbed charge magnitude;
4. opposite electric charges;
5. neutral `Q=0` with finite phase carrier;
6. equal-charge multiplet reduction;
7. unequal-charge multiplet where total RFC current alone is insufficient;
8. charge-mixing `[M^2,Q] != 0` rejection;
9. synchronized gauge-shift invariance of the phase carrier.

## 9. Einstein-source consequence

RF-N1B2P keeps the two source roles typed:

```text
phase/noether carrier
  -> RF-N1B2O phase energy density
  -> matter/gravity source

same charge-resolved carrier packet
  -> Pi_Q
  -> -(1/hbar) Pi_Q
  -> Maxwell source current
```

The same matter degrees of freedom can therefore feed both branches through different, explicitly typed maps. RF-E0 may then use the charge-projected `J_EM` in the electromagnetic stress-energy exchange while RF-N1B2O supplies the phase contribution to the matter stress-energy budget.

## 10. Advancement

```text
RF-N1B2K independent RFC↔Noether current/measure audit        prerequisite
RF-N1B2O phase-energy matter-source factorization             available
RF-M4 / IDT 01AG charge-projected variation current           available
RF-N1B2P single-charge current intertwiner                    EXACT algebra
RF-N1B2P neutral control                                      EXACT
RF-N1B2P charge-resolved multiplet projector                  EXACT algebra
physical RFC current packet ↔ Noether packet                  CONDITIONAL on measured K-gate
complete charged-matter stress-energy composition             NEXT
mu_* physical normalization                                   OPEN
Einstein total-source promotion                               OPEN
```
