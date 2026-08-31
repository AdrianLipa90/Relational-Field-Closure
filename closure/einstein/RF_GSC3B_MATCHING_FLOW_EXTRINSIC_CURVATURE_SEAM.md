# RF-GSC3B — Matching-Flow Extrinsic-Curvature Seam

Status: `EXACT_KINEMATIC_MATCHING_FLOW_TO_EXTRINSIC_CURVATURE_THEOREM / EXECUTABLE_CERTIFIER / GSC3A_PRODUCTION_FLOW_INPUT_INHERITED / PHYSICAL_EVENT_PLACEMENT_INHERITED / RF_E25_PRODUCTION_ATLAS_DOWNSTREAM`

Date: 2026-08-31

## 1. Purpose

RF-GSC3A supplies the clock-transverse matching field

\[
\boxed{X=\partial_t-b^i\partial_i}
\]

with

\[
\boxed{dt(X)=1}
\]

and the exact shared-clock overlap law

\[
\boxed{b_q=A_{qp}b_p-v_{qp}}.
\]

TIR Gate A5 supplies a global positive spatial metric `h` and its Levi-Civita derivative `D` on an admitted spatial realization. The TIR spatial-temporal interface already declares the deformation tensor convention

\[
\boxed{
K_{ij}
=\frac{D_i b_j+D_j b_i-\partial_t h_{ij}}{2N},
\qquad N>0.
}
\]

RF-GSC3B closes the kinematic seam between these two existing interfaces.

## 2. Lie derivative along the matching field

For the spatial metric tensor,

\[
X=\partial_t-b,
\]

so on spatial arguments

\[
\mathcal L_Xh
=\partial_t h-\mathcal L_bh.
\]

Because `D` is the Levi-Civita derivative of `h`,

\[
(\mathcal L_bh)_{ij}
=D_i b_j+D_j b_i.
\]

Therefore

\[
\boxed{
(\mathcal L_Xh)_{ij}
=\partial_t h_{ij}-D_i b_j-D_j b_i.
}
\]

Substitution into the declared deformation convention gives

\[
\boxed{
K_{ij}
=-\frac{1}{2N}(\mathcal L_Xh)_{ij}.
}
\]

This identity is exact and kinematic.

## 3. Unit-normal form

RF-E25 uses

\[
\vartheta^0=Ndt,
\qquad
\vartheta^a=e^a{}_i(dx^i+b^idt).
\]

RF-GSC3A gives a vector `X` annihilated by every spatial coframe and satisfying

\[
\vartheta^0(X)=N.
\]

The corresponding normalized normal direction is

\[
\boxed{n=N^{-1}X.}
\]

When `h` is evaluated on spatial arguments, derivative terms of the scalar factor `N^{-1}` multiply contractions of `h` with the normal direction and vanish. Hence

\[
\boxed{
\mathcal L_nh
=N^{-1}\mathcal L_Xh
}
\]

on the spatial sector. Consequently

\[
\boxed{
K_{ij}=-\frac12(\mathcal L_nh)_{ij}.
}
\]

This is the same sign convention already encoded by the TIR spatial-temporal closure interface.

## 4. Matching-flow coordinates

Suppose the GSC3A interval-complete flow gate passes. The resulting flow trivialization gives coordinates transported by `X`. In those coordinates,

\[
\boxed{X=\partial_t}
\]

and therefore the coordinate shift representation is

\[
\boxed{b'^i=0.}
\]

The deformation tensor remains

\[
K_{ij}
=-\frac{1}{2N}\partial_t h_{ij},
\]

or equivalently

\[
\boxed{
\partial_t h_{ij}=-2NK_{ij}.
}
\]

Thus the dragged-coordinate zero-shift form is a coordinate gauge consequence of the matching-flow trivialization. The geometric deformation carried by `K_ij` remains explicit in the metric evolution.

## 5. Relation to TIR beta_match

The TIR spatial-temporal closure interface names the inter-leaf identification field `beta_match`. GSC3A identifies its shared-clock overlap behavior with the RFC shift representation `b`.

GSC3B therefore gives the typed seam

```text
TIR A5:       h_ij, D_i
TIR/IDT:      t, N
GSC3A:        beta_match <-> b and global matching direction X
GSC3B:        K_ij = -(1/2N) L_X h_ij
RFC E25:      shared Lorentz/coframe atlas promotion
```

A source-owned binding receipt remains required when separate project surfaces use different identifiers for the same matching-field representation.

## 6. Dependency order

The corrected seam is

```text
TIR A5 spatial metric + Levi-Civita derivative
 + IDT positive regular clock/lapse
 + GSC3A matching-field overlap theorem
 -> RF-GSC3B exact kinematic deformation theorem
 -> TIR spatial-temporal packet (h, N, K; beta_match)
 -> RF-E25 ADM/coframe overlap certificate
```

The theorem does not require production event placement or global matching-flow coverage in order to establish the local tensor identity. Those inputs remain required for production global realization.

## 7. Executable certifier

Implementation:

`src/rfc/matching_flow_extrinsic_curvature.py`

Reference tests:

`tests/reference/test_matching_flow_extrinsic_curvature.py`

The certifier checks:

- finite symmetric `partial_t h`;
- finite symmetric `D_i b_j + D_j b_i`;
- positive finite lapse;
- the exact identity `K=-(1/2N)L_Xh`;
- the unit-normal identity `L_nh=-2K`;
- the dragged-coordinate evolution `partial_t h=-2NK`;
- an explicit firewall that zero shift in dragged coordinates is a coordinate gauge statement.

## 8. Claim ledger

| Claim | Status |
|---|---|
| `L_X h = partial_t h - L_b h` on spatial arguments | `EXACT` |
| `L_b h_ij = D_i b_j + D_j b_i` for spatial Levi-Civita `D` | `STANDARD EXACT IDENTITY` |
| `K_ij=-(L_X h)_ij/(2N)` in the declared convention | `EXACT` |
| `K_ij=-(L_n h)_ij/2` with `n=X/N` | `EXACT ON SPATIAL SECTOR` |
| matching-flow coordinates admit `b'=0` | `EXACT CONDITIONAL ON GSC3A FLOW TRIVIALIZATION` |
| dragged-coordinate evolution `partial_t h=-2NK` | `EXACT CONDITIONAL` |
| executable kinematic certifier | `PASS TARGET` |
| production global matching-flow coverage | `UPSTREAM GSC3A OPEN INPUT` |
| physical event placement | `UPSTREAM OPEN INPUT` |
| RF-E25 shared Lorentz/coframe realization | `DOWNSTREAM PRODUCTION GATE` |

## 9. GREMLIN × Terminal36D × PhaseNav audit boundary

The candidate was adversarially routed through the live NOEMA generation

```text
/dev/shm/ciel_noema
 -> GREMLIN
 -> Terminal36D
 -> PhaseNav 36D
 -> GREMLIN fused state
```

with `CANDIDATE_ONLY` authority. The runtime trace may be retained as audit evidence; deterministic reference tests and hosted RFC validation remain the executable theorem evidence.

Target verdict:

`PASS_RFC_GSC3B_MATCHING_FLOW_EXTRINSIC_CURVATURE_KINEMATIC_SEAM_WITH_PRODUCTION_INPUTS_OPEN`.
