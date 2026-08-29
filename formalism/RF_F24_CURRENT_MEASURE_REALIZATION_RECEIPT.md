# RF-F24 — RF-N1B2K Current/Measure Realization Receipt

Status: `RF_N1B2K_EXECUTABLE_RECEIPT / LOCAL_CURRENT_AND_MEASURE_DEFECTS_SEPARATE / RF_S16_OPTIONAL_THIRD_ROUTE / PHYSICAL_REALIZATION_INPUT_OPEN`

RF-F24 turns the existing RF-N1B2K exact defect theorem into a repository-local independent-input executable receipt and connects it to the RF-S16 occupation-current map without identifying any of the input representations by assignment.

## 1. Independent finite-cell representations

On one ordered finite slice, the Noether representation supplies independently

\[
\{j_{\vartheta,a}\},
\qquad
\{V_a^{(\vartheta)}\},
\]

while the RFC representation supplies independently

\[
\{j_{Q,a}\},
\qquad
\{V_a^{(Q)}\}.
\]

The receipt also receives independent lineage identifiers for

- slice;
- future-normal orientation;
- semantic measure;
- ordered cell identifiers.

No local current or measure equality is constructed inside the receipt.

## 2. Extensive charges

On the positive-current sector,

\[
\boxed{
Q_\vartheta
=\sum_aV_a^{(\vartheta)}j_{\vartheta,a}>0,
\qquad
Q_\Sigma
=\sum_aV_a^{(Q)}j_{Q,a}>0.}
\]

Positive cell volumes and positive extensive charges are fail-closed domain conditions.

## 3. Independent local defects

RF-N1B2K defines

\[
\boxed{
\Delta_J
=\frac{\sum_aV_a^{(Q)}|j_{Q,a}-j_{\vartheta,a}|}{Q_\vartheta}}
\]

and

\[
\boxed{
\Delta_V
=\frac{\sum_a|V_a^{(Q)}-V_a^{(\vartheta)}|\,|j_{\vartheta,a}|}{Q_\vartheta}.}
\]

The extensive mismatch is

\[
\boxed{
\Delta_\Sigma
=\frac{|Q_\Sigma-Q_\vartheta|}{Q_\vartheta}.}
\]

The executable theorem coordinate is

\[
\boxed{
\Delta_{bound}
=\max\left\{0,\Delta_\Sigma-(\Delta_J+\Delta_V)\right\}.}
\]

The RF-N1B2K theorem requires

\[
\boxed{\Delta_{bound}=0}
\]

within the explicitly selected numerical floor.

## 4. Integrated-equality firewall

The receipt includes the RF-N1B2K counterexample

\[
j_\vartheta=(1,3),
\qquad
j_Q=(2,2),
\qquad
V=(1,1),
\]

for which

\[
Q_\vartheta=Q_\Sigma=4,
\qquad
\Delta_\Sigma=0,
\qquad
\Delta_J=\frac12.
\]

Thus an exact extensive equality does not pass the local current gate.

## 5. Normalized carrier profile

Define

\[
p_{\vartheta,a}
=\frac{V_a^{(\vartheta)}j_{\vartheta,a}}{Q_\vartheta},
\qquad
p_{Q,a}
=\frac{V_a^{(Q)}j_{Q,a}}{Q_\Sigma}.
\]

RF-F24 audits the independent profile distance

\[
\boxed{
\Delta_p
=\sum_a|p_{Q,a}-p_{\vartheta,a}|.}
\]

On the exact current/measure surface,

\[
\Delta_J=\Delta_V=0
\quad\Longrightarrow\quad
\boxed{\Delta_p=0}.
\]

## 6. Side-flux coordinate

Cross-slice conservation carries the independent coordinate

\[
\boxed{\Delta_F=|F_{side}|.}
\]

The exact closed/periodic/sufficient-decay reference surface has

\[
\Delta_F=0.
\]

## 7. Lineage firewall

Numerical current agreement is admitted only when the two representations also agree on

\[
\boxed{
\text{slice ID},
\text{ normal-orientation ID},
\text{ semantic-measure ID},
\text{ ordered cell IDs}.}
\]

Each mismatch is an independent binary defect. Reordering cells therefore cannot be hidden by coincident integrated totals.

## 8. Optional RF-S16 third route

RF-S16 independently supplies occupation data

\[
\mathcal N_a\ge0
\]

and carrier quantum

\[
q_0>0.
\]

With the independently supplied RFC volumes, its predicted current is

\[
\boxed{
j_{pred,a}=q_0\frac{\mathcal N_a}{V_a^{(Q)}}.}
\]

RF-F24 does not replace the independently supplied RFC current with this expression. It instead audits a third-route defect

\[
\boxed{
\Delta_{J,\mathcal N}
=\frac{\sum_aV_a^{(Q)}|j_{Q,a}-j_{pred,a}|}{Q_{pred}}}
\]

plus extensive-charge and normalized-profile defects.

This gives the three-way finite-cell audit

\[
\boxed{
\text{Noether current}
\leftrightarrow
\text{RFC current}
\leftrightarrow
\text{orbital occupation}}
\]

without generating equality by assignment.

## 9. Exact zero-defect reference surface

The executable reference surface is

\[
\boxed{
\Delta_J
=\Delta_V
=\Delta_\Sigma
=\Delta_{bound}
=\Delta_p
=\Delta_F
=0}
\]

plus zero lineage defects.

When the optional RF-S16 route is present, it additionally requires zero occupation-current, occupation-charge and occupation-profile defects.

## 10. Einstein-source connection

RF-F21 independently audits the field↔rotor phase rate. RF-F23 independently audits the phase-clock↔material congruence. RF-F24 supplies the finite-current/measure receipt that those gates had retained as a physical promotion input.

On a realized zero-defect RF-F24 surface,

\[
\boxed{Q_\Sigma=Q_\vartheta}
\]

and the local normalized carrier profiles coincide. This closes the finite-carrier identity input consumed downstream by the source-factorization and Einstein-source stack.

RF-F22 already establishes the exact Einstein/Bianchi source-repartition algebra. RF-F24 therefore determines admission of the realized carrier into that algebra rather than modifying the Einstein residual identity.

## 11. Evidential status

The reference implementation validates the RF-N1B2K theorem, fail-closed domain, lineage firewall, profile identity and optional RF-S16 third-route comparison.

Physical promotion requires independently sourced realized-system arrays and lineage identifiers on one common slice. A reference zero-defect fixture demonstrates the executable contract and is kept distinct from a realized-system receipt.

## 12. Executable reference

`src/rfc/current_measure_realization_receipt.py` implements:

- independent Noether and RFC local-current arrays;
- independent Noether and RFC cell-volume arrays;
- exact `Delta_J`, `Delta_V`, `Delta_Sigma` and theorem-bound margin;
- normalized carrier-profile defect;
- side-flux defect;
- slice/orientation/measure/ordered-cell lineage defects;
- optional RF-S16 occupation-current third route;
- exact-zero and explicit-tolerance admission;
- fail-closed finite, positivity, shape and lineage checks.
