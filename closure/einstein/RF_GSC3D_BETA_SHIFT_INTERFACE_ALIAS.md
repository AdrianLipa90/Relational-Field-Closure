# RF-GSC3D — Beta-Match / Shift Interface Alias

Status: `EXACT_MATCHING_ONE_FORM_COEFFICIENT_ALIAS / EXACT_TEMPORAL_SCALE_CONVERSION / EXACT_OVERLAP_EQUIVARIANCE / SAME_PATCH_CLOCK_IDENTITY_REQUIRED`

Date: 2026-08-31

## 1. Purpose

TIR exports `beta_match` as the inter-leaf coordinate-matching field in the spatial-temporal interface. RFC RF-E8 uses the ADM shift `b` in the same time-adapted spatial one-form slot. RF-GSC3B already establishes the `x^0=ct` coordinate-scale relation and the crosslink to RF-E9 extrinsic curvature.

RF-GSC3D isolates the exact interface statement: once both repository surfaces refer to the same physical patch, the same spatial chart and the same calibrated clock coordinate, the two coefficient arrays are coordinate representations of one matching one-form.

## 2. General temporal-coordinate scale

Let the TIR interface use a scalar temporal coordinate `Theta` and let RFC use a length-valued temporal coordinate `x^0` related by

\[
\boxed{x^0=\alpha\Theta+\mathrm{const}},
\qquad \alpha>0.
\]

Then

\[
\boxed{dx^0=\alpha\,d\Theta}.
\]

On the same spatial chart, write the TIR matching form as

\[
\boxed{\xi^i=dx^i+\beta_{(\Theta)}^i d\Theta}
\]

and the RFC form as

\[
\boxed{\xi^i=dx^i+b_{(0)}^i dx^0}.
\]

Equality of the one-form gives

\[
\beta_{(\Theta)}^i d\Theta
=b_{(0)}^i\alpha d\Theta,
\]

hence the unique coefficient alias

\[
\boxed{\beta_{(\Theta)}^i=\alpha b_{(0)}^i.}
\]

For the RF-E8 convention

\[
\Theta=t,
\qquad x^0=ct,
\]

this becomes

\[
\boxed{\beta_{(t)}^i=c\,b_{(0)}^i,}
\]

which is the scale relation already used by RF-GSC3B.

## 3. Uniqueness from the matching one-form

The coordinate differentials `dx^i` and `dTheta` are linearly independent on a regular time-adapted chart. Therefore equality

\[
dx^i+\beta^i d\Theta
=dx^i+\widetilde\beta^i d\Theta
\]

implies

\[
\boxed{\beta^i=\widetilde\beta^i.}
\]

Thus a declared shared matching one-form fixes the shift coefficients uniquely after the temporal-coordinate scale is fixed.

The remaining repository-level coordinate is the identity contract

```text
same physical realization
same patch_id
same spatial_chart_id
same clock_id / calibrated temporal scale
```

rather than an independently selected shift field.

## 4. Equivariance under time-dependent spatial relabeling

Let

\[
x_q=f_{qp}(\Theta,x_p),
\qquad A_{qp}=D_xf_{qp},
\qquad v_{(\Theta),qp}=\partial_\Theta f_{qp}.
\]

The TIR/GSC3A matching coefficient transforms as

\[
\boxed{\beta_q=A_{qp}\beta_p-v_{(\Theta),qp}.}
\]

Using `x^0=alpha Theta`, define

\[
\boxed{v_{(0),qp}=\partial_0f_{qp}=\alpha^{-1}v_{(\Theta),qp}.}
\]

The RFC shift transformation is

\[
\boxed{b_q=A_{qp}b_p-v_{(0),qp}.}
\]

Assume on patch `p`

\[
\beta_p=\alpha b_p.
\]

Then

\[
\begin{aligned}
\beta_q
&=A_{qp}(\alpha b_p)-v_{(\Theta),qp}\\
&=\alpha\left(A_{qp}b_p-v_{(0),qp}\right)\\
&=\alpha b_q.
\end{aligned}
\]

Therefore

\[
\boxed{\beta=\alpha b}
\]

is equivariant under the admitted time-dependent spatial relabelings.

## 5. Relation to GSC3A and RF-E9

The GSC3A matching vector in the `Theta` representation is

\[
X_\Theta=\partial_\Theta-\beta_{(\Theta)}^i\partial_i.
\]

The RFC representation is

\[
X_0=\partial_0-b_{(0)}^i\partial_i.
\]

Since

\[
\partial_\Theta=\alpha\partial_0
\]

and

\[
\beta_{(\Theta)}=\alpha b_{(0)},
\]

one obtains

\[
\boxed{X_\Theta=\alpha X_0.}
\]

For `alpha=c`, this is the RF-GSC3B relation `X_t=cX_0`, and RF-E9 gives

\[
K_{ij}
=-\frac{1}{2N}\mathcal L_{X_0}h_{ij}
=-\frac{1}{2N\alpha}\mathcal L_{X_\Theta}h_{ij}.
\]

RF-GSC3D therefore converts the former field-selection seam into a patch/clock identity seam before the RF-E9 kinematic crosslink.

## 6. Executable certifier

The reference implementation checks:

- positive finite temporal scale `alpha`;
- exact patch and clock identifier agreement;
- finite three-component `beta_Theta` and `b_0` arrays;
- coefficient residual `beta_Theta-alpha*b_0`;
- optional time-dependent overlap data `(A,v_Theta,v_0)`;
- drift-scale relation `v_Theta=alpha*v_0`;
- equivariance of the alias on the target patch.

Implementation:

`src/rfc/beta_shift_interface_alias.py`

Tests:

`tests/reference/test_gsc3d_beta_shift_interface_alias.py`

## 7. Claim ledger

| Claim | Status |
|---|---|
| `dx^0=alpha dTheta` | `EXACT COORDINATE CALIBRATION` |
| shared matching one-form gives `beta_Theta=alpha b_0` | `EXACT COEFFICIENT UNIQUENESS` |
| `Theta=t`, `x^0=ct` gives `beta_t=c b_0` | `EXACT RF-E8 SPECIALIZATION` |
| alias is equivariant under time-dependent spatial relabeling | `EXACT` |
| `X_Theta=alpha X_0` | `EXACT` |
| RF-E9 extrinsic-curvature crosslink | `PARENT RF-GSC3B / RF-E9` |
| source-owned same-patch / same-clock identity | `OPEN PROVENANCE INPUT` |

## 8. Validation boundary

RF-GSC3D certifies the interface alias once the patch and clock identifiers are source-bound. The production RF-E25 atlas remains responsible for the actual shared coframe/metric realization and overlap data on the physical domain.

GREMLIN, PhaseNav and Terminal36D provide candidate dependency audit only; hosted deterministic validation remains the executable evidence surface.
