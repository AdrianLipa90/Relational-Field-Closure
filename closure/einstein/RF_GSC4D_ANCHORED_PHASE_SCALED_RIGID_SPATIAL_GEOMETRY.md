# RF-GSC4D — Anchored Phase-Scaled Rigid Spatial-Geometry Route

Status: `EXACT_ANCHORED_RIGID_TRANSITION / EXACT_PHASE_SCALED_COFRAME_SPECIALIZATION / GSC4_SPATIAL_GEOMETRY_INPUT_REDUCTION / PRODUCTION_ANCHOR_FRAME_PHASE_RATE_PACKET_OPEN`

Date: 2026-08-31

## 1. Purpose

RF-GSC4A accepts a general spatial source packet consisting of local spatial coframes `e_p`, oriented spatial coordinate Jacobians `A_qp`, and internal frame rotations `R_qp`, constrained by

\[
\boxed{e_qA_{qp}=R_{qp}e_p.}
\]

TIR already contains two narrower source structures:

1. anchored Pauli/affine charts with orthonormal frames `Q_p in SO(3)`;
2. the hexahedral phase-clock local coframe physicalization
   \[
   E^i=\frac{c}{\sqrt6|\omega_t|}\,\vartheta^i.
   \]

RF-GSC4D composes these structures into one sufficient rigid-atlas route. It reduces the independent matrix packet `(e,A,R)` to anchored frames plus one source-bound phase-scale scalar on each represented overlap.

The general GSC4A smooth-atlas route remains a separate route.

## 2. Anchored Pauli charts

Let a local TIR chart `p` be specified by an anchor

\[
r_p\in\mathbb R^3
\]

and an orthonormal frame

\[
Q_p\in SO(3).
\]

For one common Pauli affine carrier coordinate `r`, define

\[
\boxed{x_p=Q_p^{\mathsf T}(r-r_p).}
\]

For two charts `p,q`, eliminating `r` gives the exact TIR anchored transition

\[
\boxed{x_q=Q_q^{\mathsf T}Q_p x_p+Q_q^{\mathsf T}(r_p-r_q).}
\]

Hence

\[
\boxed{A_{qp}=Q_q^{\mathsf T}Q_p,}
\]

\[
\boxed{t_{qp}=Q_q^{\mathsf T}(r_p-r_q).}
\]

The internal TIR frame rotation between the same anchored frames is

\[
\boxed{R_{qp}=Q_q^{\mathsf T}Q_p.}
\]

Therefore on this rigid anchored route

\[
\boxed{A_{qp}=R_{qp}\in SO(3).}
\]

This equality is a property of the admitted anchored rigid charts. It is not a restriction on the general smooth GSC4A atlas.

## 3. Dimensionless solder form on the anchored carrier

The TIR endpoint relation uses the Pauli displacement vector

\[
\Delta r=r_y-r_x.
\]

In the local anchored frame,

\[
\Delta x_p=Q_p^{\mathsf T}\Delta r.
\]

The same local frame extracts the internal displacement components as

\[
Q_p^{\mathsf T}\Delta r.
\]

Thus on the pure affine anchored carrier the dimensionless local solder/orientation coframe is represented by

\[
\boxed{\vartheta_p=dx_p,}
\]

so its coframe matrix in the local coordinate/internal-frame pair is

\[
\boxed{I_3.}
\]

This is the rigid anchored specialization of the discrete TIR solder source, not a statement about a general curved coordinate chart.

## 4. Phase-clock spatial physicalization

RF-02H/TIR hexahedral physicalization supplies

\[
\ell_\varphi=\frac{c}{|\omega_t|}
\]

for finite nonzero local phase rate `omega_t`, and

\[
\boxed{s:=\frac{\ell_\varphi}{\sqrt6}
=\frac{c}{\sqrt6|\omega_t|}.}
\]

With `vartheta=dx`, the physical spatial coframe on patch `p` is

\[
\boxed{e_p=s_p I_3.}
\]

The sign of `omega_t` does not change the spatial scale because `s` depends on its magnitude.

## 5. Overlap coframe theorem

At one common physical point represented by patches `p` and `q`, require the phase-clock spatial scale to be one source-bound scalar:

\[
\boxed{s_q=s_p.}
\]

Then, using `A_qp=R_qp`,

\[
\begin{aligned}
e_qA_{qp}
&=s_q I_3 A_{qp}\\
&=s_p R_{qp}\\
&=R_{qp}s_pI_3\\
&=R_{qp}e_p.
\end{aligned}
\]

Therefore

\[
\boxed{e_qA_{qp}=R_{qp}e_p.}
\]

The GSC4A spatial coframe compatibility equation is exact on the rigid anchored/phase-scaled route.

## 6. Source packet reduction

The general GSC4A spatial packet

```text
patch coframe matrices e_p
spatial Jacobians A_qp
SO(3) rotations R_qp
```

can be replaced on this sufficient route by

```text
TIR anchor vectors r_p
TIR orthonormal frame matrices Q_p
finite nonzero phase rates omega_t,p
shared phase-scale identity on each represented overlap
```

with deterministic outputs

\[
A_{qp}=R_{qp}=Q_q^TQ_p,
\]

\[
t_{qp}=Q_q^T(r_p-r_q),
\]

\[
e_p=\frac{c}{\sqrt6|\omega_{t,p}|}I_3.
\]

The remaining GSC4 inputs — temporal lapse, matching shift/drift route, and production coverage/source identities — retain their existing owners. GSC4C may supply the coverage indices from a production A5 tetrahedral complex.

## 7. Scale-binding firewall

The anchored frame algebra alone fixes `A`, `R` and `t`; it does not fix the physical scalar `s`. Two overlap representations with different `|omega_t|` produce

\[
e_qA_{qp}\ne R_{qp}e_p.
\]

Therefore phase-scale equality on one physical overlap is an explicit source-binding condition.

The event-clock exactness theorem 05H and the relational lapse 05C remain separately typed temporal structures. RF-GSC4D does not identify the phase rate with the lapse.

## 8. Rigid-route firewall

A general smooth spatial overlap may have

\[
A_{qp}=D_xf_{qp}\in GL^+(3)
\]

with shear or non-rigid stretch while the internal frame rotation remains

\[
R_{qp}\in SO(3).
\]

RF-GSC4D therefore exports

\[
\boxed{A=R}
\]

only on its declared anchored rigid-chart route. The general RF-GSC4A relation remains

\[
\boxed{e_qA=Re_p.}
\]

## 9. Executable surface

Implementation:

`src/rfc/anchored_phase_scaled_rigid_geometry.py`

Reference tests:

`tests/reference/test_gsc4d_anchored_phase_scaled_rigid_geometry.py`

The certifier checks:

- finite anchors and phase rates;
- `Q_p in SO(3)`;
- nonzero `omega_t`;
- exact anchored `A=R` construction;
- anchored translation construction;
- shared phase-scale agreement on each declared overlap;
- `e_qA=Re_p`;
- explicit separation from the general smooth GSC4A route.

## 10. Claim ledger

| Statement | Status |
|---|---|
| anchored transition `A_qp=Q_q^T Q_p` | `EXACT TIR AFFINE ALGEBRA` |
| internal frame rotation `R_qp=Q_q^T Q_p` | `EXACT` |
| `A_qp=R_qp` on the anchored rigid route | `EXACT ROUTE SPECIALIZATION` |
| dimensionless anchored solder `vartheta=dx` | `EXACT ON COMMON PAULI AFFINE CARRIER` |
| `e=sI`, `s=c/(sqrt6 |omega_t|)` | `EXACT CONDITIONAL PHASE-CLOCK PHYSICALIZATION` |
| shared scale gives `e_q A=R e_p` | `EXACT` |
| executable route certifier | `PASS TARGET` |
| production anchor/frame/phase-rate packet | `OPEN SOURCE INPUT` |
| phase-scale identity across production overlap | `OPEN SOURCE BINDING` |
| general smooth GSC4A atlas | `SEPARATE HOSTED-PASS ROUTE` |

## 11. Live 36D boundary

The dependency reduction was audited through

```text
GREMLIN -> Terminal36D -> PhaseNav36D -> GREMLIN
```

on the active `/dev/shm/ciel_noema` surface with `CANDIDATE_ONLY` authority. The runtime audit cannot promote source inputs or replace hosted deterministic validation.
