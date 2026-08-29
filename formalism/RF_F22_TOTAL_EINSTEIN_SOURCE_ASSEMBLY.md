# RF-F22 — Total Einstein Source Assembly and Bianchi Repartition Theorem

Status: `EXACT_FIXED_DYNAMIC_LAMBDA_EQUIVALENCE / EXACT_BIANCHI_REPARTITION / RF_F20_RESPONSE_AGNOSTIC / PHYSICAL_SOURCE_PROMOTION_OPEN`

RF-F22 composes the action-level Einstein/ADM spine, RF-E7 matter composition, RF-F16 dynamic-`Lambda0` ledger, RF-F17 state-dependent interaction, RF-F20 ABE/phase-scale metric response, and RF-F21 independent phase-rate receipt into one final source-bookkeeping theorem.

The theorem separates two questions:

1. the exact variational/repartition structure of the Einstein equation;
2. the physical realization of the response tensors and carrier inputs entering that source.

The first is closed below without assigning a value to the still-measured physical response coordinates.

## 1. Common action ledger

Use the renormalized reference cosmological coordinate of RF-F16,

\[
\Lambda_*,
\]

and the dynamic coordinate

\[
\boxed{
\Lambda_0
=\Lambda_*+\kappa_E\widehat U_L.}
\]

Let `T_rest` denote the complete action-derived source tensor after removing only the explicit `Uhat_L` potential/inter\-action bookkeeping treated in this gate. It may contain, as admitted on the selected branch:

- RF-E7 amplitude/phase/potential matter sectors outside the displayed `Uhat_L` term;
- RF-E0 electromagnetic stress;
- generator/base matter stress;
- kinetic `phi_L` stress;
- any RF-F20 ABE metric-response correction belonging to those underlying action sectors;
- additional independently action-derived admitted source sectors.

This typing prevents double counting of the `Uhat_L` repartition below.

Take the RF-F17 state-dependent interaction

\[
\boxed{
\mathcal L_{int}
=\eta\widehat U_L f(C_\vartheta),
\qquad
0\le\eta\le1,
\qquad
f(1)=1.}
\]

On the projector surface `C_vartheta=1`, define the non-metric-proportional interaction response

\[
\boxed{
D_{\mu\nu}
:=-2\eta\widehat U_L f'(1)
\frac{\partial C_\vartheta}{\partial g^{\mu\nu}}.}
\]

RF-F20 gives the complete derivative

\[
\frac{\partial C_\vartheta}{\partial g^{\mu\nu}}
=-\frac{q_\mu q_\nu+2R_{\mu\nu}}{\mu_\vartheta^2}
-2S^{(\vartheta)}_{\mu\nu}
\]

on `C_vartheta=1`, hence

\[
\boxed{
D_{\mu\nu}
=
2\eta\widehat U_L f'(1)
\frac{q_\mu q_\nu}{\mu_\vartheta^2}
+
4\eta\widehat U_L f'(1)
\frac{R_{\mu\nu}}{\mu_\vartheta^2}
+
4\eta\widehat U_L f'(1)
S^{(\vartheta)}_{\mu\nu}.}
\]

No value of `R_mn` or `S_mn^(vartheta)` is required for the repartition theorem.

## 2. Constant-reference Einstein ledger

Keep `Lambda_*` on the geometric side and retain the complete `Uhat_L` action contribution in the matter tensor. Since

\[
-\widehat U_L+\eta\widehat U_L f(1)
=-(1-\eta)\widehat U_L,
\]

the fixed-reference source is

\[
\boxed{
T^{(*)}_{\mu\nu}
=
T^{rest}_{\mu\nu}
-(1-\eta)\widehat U_L g_{\mu\nu}
+D_{\mu\nu}.}
\]

The Einstein equation is

\[
\boxed{
G_{\mu\nu}+\Lambda_*g_{\mu\nu}
=\kappa_E T^{(*)}_{\mu\nu}.}
\]

On the equations of motion of the complete generally covariant matter action, this is the ordinary constant-reference ledger with

\[
\boxed{
\nabla^\mu T^{(*)}_{\mu\nu}=0.}
\]

## 3. Dynamic-`Lambda0` ledger

Move the full metric-proportional `-Uhat_L g_mn` contribution from matter to geometry through

\[
\Lambda_0=\Lambda_*+\kappa_E\widehat U_L.
\]

The remaining dynamic-ledger source is

\[
\boxed{
T^{(0)}_{\mu\nu}
=
T^{rest}_{\mu\nu}
+\eta\widehat U_L g_{\mu\nu}
+D_{\mu\nu}.}
\]

Therefore

\[
\boxed{
T^{(0)}_{\mu\nu}-T^{(*)}_{\mu\nu}
=\widehat U_L g_{\mu\nu}.}
\]

The dynamic equation is

\[
\boxed{
G_{\mu\nu}+\Lambda_0g_{\mu\nu}
=\kappa_E T^{(0)}_{\mu\nu}.}
\]

## 4. Exact residual identity

Define the two Einstein residuals

\[
\mathcal E^{(*)}_{\mu\nu}
:=G_{\mu\nu}+\Lambda_*g_{\mu\nu}
-\kappa_ET^{(*)}_{\mu\nu},
\]

\[
\mathcal E^{(0)}_{\mu\nu}
:=G_{\mu\nu}+\Lambda_0g_{\mu\nu}
-\kappa_ET^{(0)}_{\mu\nu}.
\]

Substitute

\[
\Lambda_0-\Lambda_*=\kappa_E\widehat U_L,
\]

and

\[
T^{(0)}-T^{(*)}=\widehat U_L g.
\]

Then identically

\[
\boxed{
\mathcal E^{(0)}_{\mu\nu}
=\mathcal E^{(*)}_{\mu\nu}.}
\]

Thus the constant-reference and dynamic-`Lambda0` formulations are exactly the same Einstein equation written with two source ledgers.

This identity is independent of `eta`, `R_mn`, `S_mn^(vartheta)`, and the numerical value of `f'(1)` because the complete projector-response tensor `D_mn` is retained on both ledgers.

## 5. Exact Bianchi equivalence

Metric compatibility gives

\[
\nabla^\mu(\widehat U_L g_{\mu\nu})
=\nabla_\nu\widehat U_L.
\]

Since

\[
T^{(0)}_{\mu\nu}
=T^{(*)}_{\mu\nu}+\widehat U_Lg_{\mu\nu},
\]

we have

\[
\boxed{
\nabla^\mu T^{(0)}_{\mu\nu}
=\nabla^\mu T^{(*)}_{\mu\nu}
+\nabla_\nu\widehat U_L.}
\]

Also

\[
\boxed{
\nabla_\nu\Lambda_0
=\kappa_E\nabla_\nu\widehat U_L.}
\]

Therefore

\[
\boxed{
\kappa_E\nabla^\mu T^{(0)}_{\mu\nu}
-\nabla_\nu\Lambda_0
=
\kappa_E\nabla^\mu T^{(*)}_{\mu\nu}.}
\]

Consequently the fixed-reference action conservation law

\[
\nabla^\mu T^{(*)}_{\mu\nu}=0
\]

is exactly equivalent to the RF-F7/RF-F16 dynamic exchange law

\[
\boxed{
\kappa_E\nabla^\mu T^{(0)}_{\mu\nu}
=\nabla_\nu\Lambda_0.}
\]

The contracted Bianchi identity therefore closes on either ledger with the same residual.

## 6. Endpoint checks

### `eta=0` — RF-L2 allocation

The fixed-reference `Uhat_L` sector is

\[
-\widehat U_L g_{\mu\nu},
\]

while the dynamic source carries no explicit `Uhat_L` matter term. The complete `Uhat_L` contribution is then represented by `Lambda0` on the geometric side, reproducing the RF-L2 allocation.

### `eta=1` — all-generator/projector allocation

The fixed-reference metric-proportional potential cancels and the `Uhat_L` sector becomes

\[
\boxed{T^{(*)U}_{\mu\nu}=D_{\mu\nu}.}
\]

The dynamic source is

\[
\boxed{T^{(0)U}_{\mu\nu}=\widehat U_Lg_{\mu\nu}+D_{\mu\nu}.}
\]

Their difference remains exactly `Uhat_L g_mn`, so the residual identity survives the nontrivial projector interaction.

On the RF-F20 frozen-response surface

\[
R_{\mu\nu}=0,
\qquad
S^{(\vartheta)}_{\mu\nu}=0,
\qquad
f'(1)=\frac12,
\]

and `eta=1`,

\[
\boxed{
D_{\mu\nu}
=\widehat U_L
v_\mu^{(\vartheta)}v_\nu^{(\vartheta)}.}
\]

For nonzero `R` or `S`, their exact corrections remain in `D_mn` and the fixed/dynamic equivalence is unchanged.

## 7. Composition with the existing Einstein/ADM spine

RFC already contains the action and ADM projection chain through RF-E13. RF-F22 supplies the total-source ledger needed by that geometric spine:

\[
\boxed{
G_{\mu\nu}+\Lambda_0g_{\mu\nu}
=\kappa_E T^{(0)}_{\mu\nu},}
\]

with

\[
\boxed{
\kappa_E\nabla^\mu T^{(0)}_{\mu\nu}
=\nabla_\nu\Lambda_0.}
\]

The RF-E10–RF-E13 Hamiltonian, momentum, evolution and constraint-propagation equations therefore consume the same action-derived source after the displayed ledger transformation.

## 8. Evidential boundary and physical promotion

RF-F22 closes the variational/repartition identity. Physical promotion of the complete source still consumes independently validated coordinates already isolated by the preceding gates:

- local ABE off-shell response `R_mn` from RF-F20;
- rotor/lapse phase-scale response `S_mn^(vartheta)` from RF-F19/F20;
- realized-system field↔rotor rate and lineage receipt from RF-F21;
- RF-N1B2K physical current/measure realization;
- phase-clock/material-current alignment on the selected matter branch;
- physical state-dependent interaction selection `f(C)` and exchange allocation `eta`;
- physical promotion/universality of `kappa_E=8 pi G/c^4` on the project-derived coupling route.

These inputs determine the realized physical source; they do not alter the exact fixed/dynamic Einstein residual identity established here.

## 9. Executable reference

`src/rfc/total_einstein_source_assembly.py` implements:

- RF-F20 projector-interaction stress `D_mn`;
- fixed-reference and dynamic-`Lambda0` `Uhat_L` source sectors;
- total source assembly around a separately typed `T_rest`;
- exact source repartition `T^(0)-T^(*)=Uhat_L g`;
- exact Einstein residual comparison;
- exact Bianchi residual equivalence;
- `eta=0` and `eta=1` endpoints;
- fail-closed input validation.
