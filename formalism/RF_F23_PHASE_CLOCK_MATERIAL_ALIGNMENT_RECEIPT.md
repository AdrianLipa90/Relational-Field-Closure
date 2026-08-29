# RF-F23 — Phase-Clock / Material-Congruence Independent Alignment Receipt

Status: `RF_F18_RF_E19_ALIGNMENT_EXECUTABLE / FUTURE_TIMELIKE_DOMAIN_ENFORCED / LINEAGE_FIREWALL / PHYSICAL_REALIZATION_OPEN`

RF-F23 turns the RF-F18 alignment coordinate and RF-E19 timelike-current material congruence into one independent-input executable receipt. It tests the phase-clock and material directions rather than constructing their equality.

## 1. Independent inputs

The receipt receives separately:

\[
g_{\mu\nu},
\qquad
g^{\mu\nu},
\qquad
q_\mu=\mathscr D_\mu\vartheta,
\qquad
\mu_\vartheta>0,
\qquad
J^\mu,
\qquad
n^\mu.
\]

It also receives independent phase-clock and current lineage identifiers for the `U(1)` bundle, phase patch, ABE connection, slice, coframe, measure and support.

No phase/current equality is assigned inside the receipt.

## 2. Phase-clock direction

RF-F18 defines

\[
\boxed{
v^{(\vartheta)}_\mu
=\frac{q_\mu}{\mu_\vartheta}.}
\]

The independently supplied phase scale gives the projector coordinate

\[
\boxed{
C_\vartheta
=-\frac{g^{\mu\nu}q_\mu q_\nu}{\mu_\vartheta^2}.}
\]

The receipt records

\[
\boxed{\Delta_C=|C_\vartheta-1|}
\]

instead of normalizing `mu_vartheta` from `q_mu`.

The raised phase-clock direction is

\[
\boxed{
v_{(\vartheta)}^\mu
=g^{\mu\nu}v^{(\vartheta)}_\nu.}
\]

## 3. RF-E19 material direction

For the independently supplied current, RF-E19 requires

\[
J_\mu J^\mu<0.
\]

On this domain define

\[
\boxed{
\nu_J^\mu
=\frac{J^\mu}{\sqrt{-J_\alpha J^\alpha}}.}
\]

The implementation rejects null/spacelike input at this domain gate rather than manufacturing a timelike normalization.

Positive rescaling

\[
J^\mu\mapsto cJ^\mu,
\qquad c>0,
\]

leaves `nu_J^mu` and therefore the alignment coordinate invariant.

## 4. Future orientation

For the supplied slice normal `n^mu`, the receipt audits

\[
\boxed{
g_{\mu\nu}n^\mu n^\nu=-1.}
\]

The material future-orientation coordinate is

\[
\boxed{
Q_J:=-n_\mu J^\mu>0.}
\]

The phase-clock future-orientation coordinate is

\[
\boxed{
Q_\vartheta:=-v^{(\vartheta)}_\mu n^\mu>0.}
\]

Each failed orientation gives an explicit receipt defect.

## 5. Alignment theorem

RF-F18 defines

\[
\boxed{
\gamma_{\vartheta J}
:=-v^{(\vartheta)}_\mu\nu_J^\mu.}
\]

The executable alignment defect is

\[
\boxed{
\Delta_{\vartheta J}
:=|\gamma_{\vartheta J}-1|.}
\]

On the future unit timelike phase-clock/current sector,

\[
\gamma_{\vartheta J}\ge1,
\]

with equality exactly when the two local timelike directions coincide. Therefore

\[
\boxed{
\Delta_{\vartheta J}=0}
\]

is the exact local congruence-alignment surface.

A relative boost produces `gamma_varthetaJ>1` and a strictly positive alignment defect.

## 6. Metric-pair firewall

Because the phase one-form uses `g^{mu nu}` while the material current norm uses `g_{mu nu}`, the receipt independently audits

\[
\boxed{
g_{\mu\alpha}g^{\alpha\nu}=\delta_\mu{}^\nu.}
\]

Define

\[
\Delta_{g^{-1}}
=
\max_{\mu,\nu}
\left|
 g_{\mu\alpha}g^{\alpha\nu}
-\delta_\mu{}^\nu
\right|.
\]

Thus a numerically aligned phase/current pair cannot pass while using inconsistent metric and inverse-metric inputs.

## 7. Lineage firewall

The receipt independently compares:

- `U(1)` bundle ID;
- phase patch ID;
- ABE connection ID;
- ADM/slice ID;
- coframe ID;
- finite-current measure ID;
- support ID.

Every mismatch creates an independent binary defect. In particular, `Delta_varthetaJ=0` does not override a connection, slice, measure or support mismatch.

## 8. Zero-defect surface

The reference zero-defect surface is

\[
\boxed{
\Delta_{g^{-1}}
=\Delta_n
=\Delta_C
=\Delta_{\nu}
=\Delta_{future,\vartheta}
=\Delta_{future,J}
=\Delta_{\vartheta J}
=0
}
\]

plus zero lineage defects.

On that surface the independently supplied RF-F18 phase-clock direction and RF-E19 material-current direction are the same local future unit timelike congruence.

## 9. Einstein-source consequence

RF-F22 already closes the total Einstein residual independently of the numerical alignment value. RF-F23 supplies the remaining local identification receipt needed when the RF-F20/RF-F22 projector source is physically interpreted on the same material flow carrying the RFC current.

On the zero-defect alignment surface,

\[
\boxed{
v_{(\vartheta)}^\mu=\nu_J^\mu.}
\]

Therefore the frozen-response `eta=1`, `f'(1)=1/2` projector term can be written on the same congruence as

\[
\boxed{
D_{\mu\nu}
=\widehat U_L\nu^J_\mu\nu^J_\nu
}
\]

when the independently validated RF-F20 response conditions for that branch also hold.

For nonzero RF-F20 response tensors, their additional source terms remain explicitly present and the alignment receipt continues to test only the congruence identity.

## 10. Evidential boundary

The reference suite validates the independent comparison contract, domain gates, orientation tests, current-scale invariance and lineage firewall. Physical promotion requires phase-clock and current values/IDs sourced independently from the same realized RFC/IDT system.

## 11. Executable reference

`src/rfc/phase_clock_material_alignment_receipt.py` implements:

- independent metric/inverse-metric audit;
- independent `q_mu`, `mu_vartheta`, `J^mu`, `n^mu` inputs;
- RF-F18 projector defect;
- RF-E19 future-timelike current normalization;
- future-orientation defects;
- exact `gamma_varthetaJ` and `Delta_varthetaJ`;
- positive-current-rescaling invariance;
- bundle/patch/connection/slice/coframe/measure/support lineage defects;
- exact-zero and explicit-tolerance admission;
- fail-closed null/spacelike-current and invalid-input handling.
