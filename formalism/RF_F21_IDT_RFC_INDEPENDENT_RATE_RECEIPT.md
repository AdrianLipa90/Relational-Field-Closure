# RF-F21 — IDT↔RFC Independent Phase-Rate Receipt

Status: `CROSS_REPO_EXECUTABLE_RATE_AUDIT / ZERO_DEFECT_REFERENCE_SURFACE / PHYSICAL_RATE_REALIZATION_OPEN`

RF-F21 turns the independent-input requirement already stated by IDT 01AC/01AD and RFC RF-N1B2M/N into an executable cross-repository receipt. The receipt compares field, rotor, lapse/coframe, Noether-generator and RFC proper-phase-rate coordinates without constructing equality by assignment.

Pinned IDT source state for this receipt:

`Informational-Dynamics-of-Time main @ ed902458b6e0ad338ca4ba637d8d8228bc7c549b`

Relevant IDT inputs:

- `01AC_gauge_covariant_phase_pullback_noether_generator.md`;
- `01AD_relational_lapse_normal_phase_rate.md`.

Relevant RFC inputs:

- RF-N1B2M gauge-covariant phase pullback;
- RF-N1B2N relational-lapse normal phase rate;
- RF-F3 proper phase rate `omega`;
- RF-F19 independent rotor/lapse scale calibration.

## 1. Independent rate coordinates

The executable receipt receives four rates as separate inputs:

\[
r_t^{field},
\qquad
r_n^{field},
\qquad
r_t^{rotor},
\qquad
r_\tau^{rotor}.
\]

It also receives independently:

\[
N_R,
\qquad
I_A,
\qquad
I_\phi,
\qquad
\omega_{RFC}.
\]

No equality between these coordinates is generated inside the receipt.

## 2. Coordinate-rate defect

IDT 01AC / RFC RF-N1B2M require the common pullback rate on the admitted same-`U(1)` surface. The executable comparison is

\[
\boxed{
\Delta_t
=
\frac{|r_t^{field}-r_t^{rotor}|}{|r_t^{rotor}|}.}
\]

## 3. Field lapse/coframe defect

IDT 01AD / RFC RF-N1B2N give

\[
r_t=N_R r_n^{(\tau)}.
\]

The field-side receipt is

\[
\boxed{
\Delta_{Nf}
=
\frac{|r_t^{field}-N_Rr_n^{field}|}{|r_t^{field}|}.}
\]

## 4. Rotor lapse defect

The rotor proper-rate chain rule gives

\[
r_t^{rotor}=N_Rr_\tau^{rotor}.
\]

The independently evaluated rotor-side receipt is

\[
\boxed{
\Delta_{Nr}
=
\frac{|r_t^{rotor}-N_Rr_\tau^{rotor}|}{|r_t^{rotor}|}.}
\]

## 5. Proper-rate defect

The field normal proper rate and rotor proper rate are compared directly:

\[
\boxed{
\Delta_\tau
=
\frac{|r_n^{field}-r_\tau^{rotor}|}{|r_\tau^{rotor}|}.}
\]

Thus the proper-rate equality is tested independently from both coordinate-rate equality and lapse identities.

## 6. Independent generator receipt

The scalar-field and rotor inertias remain separate inputs:

\[
I_A,
\qquad
I_\phi.
\]

Define

\[
Q_\vartheta=I_A r_n^{field},
\qquad
P_\Phi=I_\phi r_\tau^{rotor}.
\]

The receipt retains separate defects

\[
\boxed{
\Delta_I=\frac{|I_A-I_\phi|}{|I_\phi|}}
\]

and

\[
\boxed{
\Delta_Q=\frac{|Q_\vartheta-P_\Phi|}{|P_\Phi|}.}
\]

On the common zero-defect surface,

\[
\Delta_t
=\Delta_{Nf}
=\Delta_{Nr}
=\Delta_\tau
=\Delta_I
=\Delta_Q
=0,
\]

which reproduces the IDT 01AC/01AD generator consequence through independent comparisons.

## 7. RFC RF-F3 phase-rate receipt

RF-F3 defines the RFC proper phase rate

\[
\omega=u^\mu\mathscr D_\mu\vartheta.
\]

RF-F21 receives `omega_RFC` independently and audits

\[
\boxed{
\Delta_\omega
=
\frac{|\omega_{RFC}-r_n^{field}|}{|r_n^{field}|}.}
\]

Therefore the common proper-rate bridge required by RF-F19 is an explicit receipt coordinate rather than an internal identification.

## 8. RF-F19 scale consequence

The independently evaluated rotor proper rate gives

\[
\boxed{
\mu_\vartheta=\frac{|r_\tau^{rotor}|}{c}.}
\]

On `Delta_omega=Delta_tau=0`,

\[
|\omega_{RFC}|=|r_n^{field}|=|r_\tau^{rotor}|=c\mu_\vartheta,
\]

which closes the executable path used by RF-F19 to rewrite the phase-cell geometry.

## 9. Lineage firewall

The receipt also compares explicit IDs for:

- `U(1)` bundle;
- local phase patch;
- ABE connection;
- calibrated clock;
- zero-shift coframe;
- finite-generator measure;
- ordered support.

Each mismatch produces an independent binary defect. Numerical rate agreement therefore cannot by itself pass a cross-repository lineage mismatch.

## 10. Evidential status

The executable zero-defect reference surface validates the comparison contract and algebraic roundtrip. Physical promotion requires independently sourced field/rotor rate values and lineage IDs from the same realized system.

This gate advances the Einstein-source closure by removing the software-level equality-by-assignment ambiguity between IDT 01AC/01AD and RFC RF-N1B2M/N/F3.

## 11. Executable reference

`src/rfc/idt_rfc_independent_rate_receipt.py` implements:

- separate coordinate/proper rate inputs;
- coordinate-rate, field-lapse, rotor-lapse and proper-rate defects;
- independent inertia and Noether-generator defects;
- independent RFC `omega` defect;
- RF-F19 phase-scale extraction from the rotor proper rate;
- explicit bundle/patch/connection/clock/coframe/measure/support lineage defects;
- exact-zero and explicit-tolerance admission;
- fail-closed finite/nonzero/positive input checks.
