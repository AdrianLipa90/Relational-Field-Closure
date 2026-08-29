# RF-F20 — Aharonov–Bohm–Berry–Euler Off-Shell Metric-Response Firewall

Status: `EXACT_METRIC_RESPONSE_DECOMPOSITION / RF_E4_FROZEN_CONNECTION_RECOVERY / RF_F18_F19_PROJECTOR_COMPOSITION / LOCAL_ABE_METRIC_BINDING_OPEN`

RF-F20 closes the algebraic ambiguity left by RF-F18/RF-F19 around the metric variation of the gauge-covariant phase one-form. It composes the existing RF-N1B2M ABE connection, RF-E4 phase stress tensor, RF-F18 projector response and RF-F19 independent phase-scale response into one off-shell metric-response ledger.

## 1. Upstream phase connection

RF-N1B2M supplies

\[
\mathcal A^{ABE}=\mathcal A_{AB}+\mathcal A_B+\mathcal A_E,
\]

and

\[
\boxed{q_\mu:=\mathscr D_\mu\vartheta=\partial_\mu\vartheta+\mathcal A^{ABE}_\mu.}
\]

For metric variation at fixed scalar phase coordinate,

\[
\frac{\partial(\partial_\beta\vartheta)}{\partial g^{\mu\nu}}=0.
\]

Therefore every additional metric response of the covariant phase one-form is carried by the connection sector.

Define channel responses

\[
\Pi^{AB}_{\beta|\mu\nu}
:=\frac{\partial\mathcal A^{AB}_\beta}{\partial g^{\mu\nu}},
\qquad
\Pi^{B}_{\beta|\mu\nu}
:=\frac{\partial\mathcal A^{B}_\beta}{\partial g^{\mu\nu}},
\qquad
\Pi^{E}_{\beta|\mu\nu}
:=\frac{\partial\mathcal A^{E}_\beta}{\partial g^{\mu\nu}}.
\]

Linearity gives

\[
\boxed{
\Pi^{ABE}_{\beta|\mu\nu}
=\Pi^{AB}_{\beta|\mu\nu}
+\Pi^{B}_{\beta|\mu\nu}
+\Pi^{E}_{\beta|\mu\nu}.}
\]

The contracted response introduced in RF-F18 is therefore

\[
\boxed{
R_{\mu\nu}
:=g^{\alpha\beta}q_\alpha\Pi^{ABE}_{\beta|\mu\nu}
=R^{AB}_{\mu\nu}+R^B_{\mu\nu}+R^E_{\mu\nu}.}
\]

This is the exact ABE metric-response decomposition.

## 2. RF-E4 stress tensor with general ABE response

RF-E4 uses

\[
\mathcal L_{phase}=-A^2g^{\alpha\beta}q_\alpha q_\beta-V.
\]

Keeping the same action while retaining the off-shell metric response of `q_mu`,

\[
\frac{\partial}{\partial g^{\mu\nu}}
\left(g^{\alpha\beta}q_\alpha q_\beta\right)
=q_\mu q_\nu+2R_{\mu\nu}.
\]

Hence

\[
\boxed{
T^{phase}_{\mu\nu}
=2A^2q_\mu q_\nu
+4A^2R_{\mu\nu}
+g_{\mu\nu}\mathcal L_{phase}}
\]

for metric-independent `A` and `V` on this variation ledger.

Relative to the current RF-E4 expression, the exact connection-response correction is

\[
\boxed{\Delta T^{phase}_{\mu\nu}=4A^2R_{\mu\nu}.}
\]

Therefore the current RF-E4 stress tensor is recovered exactly on the frozen-connection variation branch

\[
\boxed{R_{\mu\nu}=0.}
\]

This includes the component-wise sufficient surface

\[
\Pi^{AB}=\Pi^B=\Pi^E=0,
\]

while allowing the logically distinct possibility of channel cancellation in the contracted sum.

## 3. RF-F18 projector derivative

RF-F18 defines

\[
C_\vartheta=-\frac{g^{\alpha\beta}q_\alpha q_\beta}{\mu_\vartheta^2}.
\]

For an independent phase scale under metric variation,

\[
\boxed{
\frac{\partial C_\vartheta}{\partial g^{\mu\nu}}
=-\frac{q_\mu q_\nu+2R_{\mu\nu}}{\mu_\vartheta^2}.}
\]

Thus the ABE response is the unique correction to the numerator-side RF-F18 projector variation on this ledger.

## 4. RF-F19 scale-response composition

RF-F19 permits the independently calibrated phase scale to carry its own off-shell response

\[
S^{(\vartheta)}_{\mu\nu}
:=\frac{\partial\ln\mu_\vartheta}{\partial g^{\mu\nu}}.
\]

The complete derivative becomes

\[
\boxed{
\frac{\partial C_\vartheta}{\partial g^{\mu\nu}}
=-\frac{q_\mu q_\nu+2R_{\mu\nu}}{\mu_\vartheta^2}
-2C_\vartheta S^{(\vartheta)}_{\mu\nu}.}
\]

The two response channels are separately typed:

- `R_mn`: response of the ABE-dressed phase covector;
- `S_mn^(vartheta)`: response of the independently calibrated rotor/lapse phase scale.

## 5. Eta=1 projector stress

For the RF-F17 interaction

\[
\mathcal L_{int}=\eta\widehat U_L f(C_\vartheta)
\]

and projector surface `C_vartheta=1`, the `eta=1` stress is

\[
\boxed{
T^U_{\mu\nu}
=2\widehat U_L f'(1)\frac{q_\mu q_\nu}{\mu_\vartheta^2}
+\frac{4\widehat U_L f'(1)}{\mu_\vartheta^2}R_{\mu\nu}
+4\widehat U_L f'(1)S^{(\vartheta)}_{\mu\nu}.}
\]

Writing

\[
v_\mu^{(\vartheta)}=q_\mu/\mu_\vartheta,
\]

this becomes

\[
\boxed{
T^U_{\mu\nu}
=2\widehat U_L f'(1)v_\mu^{(\vartheta)}v_\nu^{(\vartheta)}
+\frac{4\widehat U_L f'(1)}{\mu_\vartheta^2}R_{\mu\nu}
+4\widehat U_L f'(1)S^{(\vartheta)}_{\mu\nu}.}
\]

On the independent-variation branch `S=0` and frozen-connection branch `R=0`, choosing `f'(1)=1/2` recovers

\[
\boxed{T^U_{\mu\nu}=\widehat U_L v_\mu^{(\vartheta)}v_\nu^{(\vartheta)}.}
\]

## 6. Repository metric-response audit

The current RFC source spine supplies the local ABE decomposition and gauge-covariant phase one-form. The current RF-E4 action variation supplies the frozen-covector stress tensor. RF-F18/F19 supply the general response slots `R_mn` and `S_mn^(vartheta)`.

The current explicit ABE bridge defines `A^ABE=A_AB+A_B+A_E` and its pullback/Noether role, while the local off-shell functional

\[
\mathcal A^X_\beta[g]
\quad (X=AB,B,E)
\]

is retained as a physical promotion input. Consequently RF-F20 does not assign `R_mn=0` or `R_mn!=0` by convention. It gives the exact result for either receipt.

Closed-loop Euler/Berry holonomy fixes integrated phase information. The local off-shell metric derivative is a separate coordinate and therefore requires its own receipt before physical promotion of the projector stress.

## 7. Promotion gates

RF-F20 advances the Einstein-source frontier to the following measurable/formal receipts:

1. an explicit local off-shell metric-response law for each active ABE channel;
2. an `R_mn` receipt on the same phase-clock branch used by RF-F18/F19;
3. the RF-F19 `S_mn^(vartheta)` rotor/lapse response receipt;
4. the independent IDT field↔rotor zero-defect rate receipt;
5. the phase-clock ↔ RF-E19 material-current alignment receipt.

Once `R_mn` and `S_mn^(vartheta)` are fixed, the phase/projector contribution to the Einstein source is algebraically determined by the displayed equations.

## 8. Executable reference

`src/rfc/abe_euler_metric_response.py` implements:

- channel-wise ABE metric-response summation;
- exact contraction to `R_mn`;
- RF-E4 stress correction `4 A^2 R_mn`;
- RF-F18 projector derivative;
- RF-F19 scale-response composition;
- full `eta=1` projector stress;
- frozen-connection branch detection;
- fail-closed symmetry and finiteness checks.
