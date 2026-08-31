# RF-GSC3B — Matching-Flow × RF-E9 Extrinsic-Curvature Crosslink

Status: `EXACT_KINEMATIC_CROSSLINK / SHIFT_SOURCE_BINDING_REFINED / TEMPORAL_COORDINATE_SCALE_FIREWALL / RF_E9_OPERATOR_REUSED`

Date: 2026-08-31

## 1. Purpose

RF-GSC3A derives a global clock-transverse matching field from the TIR/RFC inter-leaf identification data. RF-E8 and RF-E9 already define the ADM shift carrier, unit normal and extrinsic curvature.

RF-GSC3B identifies these two kinematic surfaces under one explicit temporal-coordinate convention. The crosslink reuses RF-E9; it introduces no competing extrinsic-curvature operator.

The dependency refinement is

```text
TIR beta_match / GSC3A matching-field cocycle
 -> global clock-transverse matching direction X
 -> temporal-coordinate scale binding
 -> RF-E8 shift b^i
 -> RF-E9 unit normal n
 -> RF-E9 K_ij
```

## 2. RF-E8 temporal coordinate

RF-E8 fixes the length-valued temporal coordinate

\[
\boxed{x^0:=ct.}
\]

Its ADM spatial coframe is

\[
\boxed{
\vartheta^a=e^a{}_i\left(dx^i+b_{(0)}^i dx^0\right),
}
\]

where `b_(0)^i` is dimensionless in the RF-E8 convention.

The corresponding GSC3A clock-transverse field is

\[
\boxed{
X_0:=\partial_0-b_{(0)}^i\partial_i.
}
\]

Then

\[
\boxed{dx^0(X_0)=1}
\]

and

\[
\boxed{\vartheta^a(X_0)=0.}
\]

## 3. Coordinate-time representation

Writing the same spatial coframe with the time coordinate `t`,

\[
\vartheta^a
=e^a{}_i\left(dx^i+\beta_{(t)}^i dt\right),
\]

and using

\[
dx^0=c\,dt,
\]

gives the exact scale binding

\[
\boxed{\beta_{(t)}^i=c\,b_{(0)}^i.}
\]

Therefore

\[
\boxed{
X_t:=\partial_t-\beta_{(t)}^i\partial_i
=c\left(\partial_0-b_{(0)}^i\partial_i\right)
=cX_0.
}
\]

This is the required coordinate-scale firewall between the generic GSC3A `t` representation and the RF-E8/RF-E9 `x^0=ct` convention.

## 4. Lie derivative of the spatial metric

Let `D_i` be the Levi-Civita connection of the spatial metric `h_ij`. For

\[
X_0=\partial_0-b^k\partial_k,
\]

the spatial components of the Lie derivative are

\[
\boxed{
(\mathcal L_{X_0}h)_{ij}
=\partial_0h_{ij}
-\left(\mathcal L_bh\right)_{ij}.
}
\]

Metric compatibility gives

\[
\boxed{
(\mathcal L_bh)_{ij}=D_i b_j+D_j b_i,
}
\]

hence

\[
\boxed{
(\mathcal L_{X_0}h)_{ij}
=\partial_0h_{ij}-D_i b_j-D_j b_i.
}
\]

## 5. RF-E9 reuse

RF-E9 fixes

\[
\boxed{
K_{ij}
=\frac{1}{2N}
\left(-\partial_0h_{ij}+D_i b_j+D_j b_i\right).
}
\]

Combining this established RF-E9 operator with the GSC3A matching field gives the exact crosslink

\[
\boxed{
K_{ij}
=-\frac{1}{2N}(\mathcal L_{X_0}h)_{ij}.
}
\]

RF-E8 also gives

\[
\boxed{
n=\frac1N X_0,
}
\]

which agrees with the RF-E9 convention

\[
K_{ij}=-\frac12\mathcal L_nh_{ij}
\]

on the spatially projected metric.

## 6. Equivalent `t`-coordinate form

Since

\[
X_t=cX_0,
\]

one has

\[
\boxed{
\mathcal L_{X_t}h=c\,\mathcal L_{X_0}h.
}
\]

Therefore

\[
\boxed{
K_{ij}
=-\frac{1}{2Nc}(\mathcal L_{X_t}h)_{ij}.
}
\]

The two representations are identical after the explicit `x^0=ct` scale conversion.

## 7. Shift-source refinement

RF-E8 currently types `b^i` as an independent shift input and records a future source from TIR affine gluing. RF-GSC3A supplies the exact shared-clock transformation law

\[
\boxed{b_q=A_{qp}b_p-v_{qp}.}
\]

RF-GSC3B therefore refines the source line to

```text
TIR inter-leaf matching field beta_match
 + GSC3A shared-clock cocycle
 + x0=ct coordinate-scale binding
 -> RF-E8 shift b^i
 -> RF-E9 extrinsic curvature
```

Production promotion requires the source-owned identification of the TIR matching field with the admitted RFC patch data on the same physical realization.

## 8. Claim ledger

| Claim | Status |
|---|---|
| `beta_(t)^i = c b_(0)^i` | `EXACT COORDINATE SCALE` |
| `X_t=cX_0` | `EXACT` |
| `L_X0 h = partial_0 h - D_i b_j - D_j b_i` | `EXACT DIFFERENTIAL GEOMETRY` |
| `K_ij=-(2N)^-1 L_X0 h_ij` | `EXACT CROSSLINK TO EXISTING RF-E9` |
| `K_ij=-(2Nc)^-1 L_Xt h_ij` | `EXACT EQUIVALENT REPRESENTATION` |
| RF-E9 extrinsic-curvature operator | `REUSED EXISTING GATE` |
| production TIR beta_match ↔ RFC b patch identity | `OPEN SOURCE-OWNED BINDING` |

## 9. Validation authority

Reference crosslink tests:

`tests/reference/test_gsc3b_matching_flow_rfe9_crosslink.py`

The tests verify the sign, lapse factor, temporal-coordinate scale factor, nonzero-shift sector and static controls against the existing RF-E9 convention.

Target verdict:

`PASS_RFC_GSC3B_MATCHING_FLOW_RFE9_KINEMATIC_CROSSLINK_WITH_PRODUCTION_SHIFT_SOURCE_BINDING_OPEN`.
