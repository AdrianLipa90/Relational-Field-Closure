# RF-GSC4D — Anchored Phase-Scaled Rigid Spatial-Geometry Route

Status: `EXACT_ANCHORED_RIGID_TRANSITION / EXACT_POINTWISE_PHASE_SCALED_COFRAME_SPECIALIZATION / GSC4_SPATIAL_GEOMETRY_INPUT_REDUCTION / PRODUCTION_ANCHOR_FRAME_PHASE_FIELD_PACKET_OPEN`

Date: 2026-08-31

## 1. Purpose

RF-GSC4A accepts a general spatial source packet with local coframes `e_p`, oriented spatial Jacobians `A_qp`, and frame rotations `R_qp`, constrained by

\[
\boxed{e_qA_{qp}=R_{qp}e_p.}
\]

TIR supplies anchored Pauli/affine charts with orthonormal frames, while RF-02H/RF-02I supply the phase-clock spatial physicalization

\[
\boxed{E^i=a\,\vartheta^i,\qquad a(x)=\frac{c}{\sqrt6\,|\omega_t(x)|}.}
\]

RF-GSC4D composes these structures into one sufficient rigid-atlas route. Version 0.2 represents the phase scale as a scalar field and certifies its gluing pointwise on overlap samples. This preserves the RF-02I sector with spatially varying `a(x)` and its induced connection contribution.

The general smooth GSC4A atlas remains a parallel sufficient route.

## 2. Anchored Pauli charts

For patch `p`, let

\[
r_p\in\mathbb R^3,
\qquad Q_p\in SO(3),
\]

and define

\[
\boxed{x_p=Q_p^{\mathsf T}(r-r_p).}
\]

On an overlap `p -> q`,

\[
\boxed{x_q=Q_q^{\mathsf T}Q_p x_p+Q_q^{\mathsf T}(r_p-r_q).}
\]

Therefore

\[
\boxed{A_{qp}=Q_q^{\mathsf T}Q_p,}
\qquad
\boxed{t_{qp}=Q_q^{\mathsf T}(r_p-r_q).}
\]

The corresponding internal-frame rotation is

\[
\boxed{R_{qp}=Q_q^{\mathsf T}Q_p.}
\]

Hence on the anchored rigid route

\[
\boxed{A_{qp}=R_{qp}\in SO(3).}
\]

This equality is the declared rigid specialization; the general GSC4A route retains arbitrary oriented smooth spatial Jacobians together with their own frame rotations.

## 3. Dimensionless solder specialization

The anchored Pauli displacement carrier uses

\[
\Delta x_p=Q_p^{\mathsf T}\Delta r.
\]

In the common affine carrier/frame pair, the dimensionless local orientation coframe is

\[
\boxed{\vartheta_p=dx_p,}
\]

with local matrix `I_3`.

## 4. Phase-scale field

Let the signed local phase rate be a field

\[
\omega_t:U\to\mathbb R\setminus\{0\}.
\]

Define its positive magnitude field and spatial scale field by

\[
\boxed{\nu(x):=|\omega_t(x)|>0,}
\]

\[
\boxed{a(x):=\frac{c}{\sqrt6\,\nu(x)}.}
\]

On patch `p`, the physical coframe at a represented point `x` is

\[
\boxed{e_p(x)=a_p(x)I_3.}
\]

A sign reversal of `omega_t` preserves `nu` and therefore preserves the spatial scale. Signed phase-rate information remains available to other dynamical sectors as a separately typed carrier.

## 5. Pointwise overlap theorem

Consider one physical overlap point `x` represented in patches `p` and `q`. A shared phase-magnitude field supplies

\[
\boxed{\nu_p(x)=\nu_q(x),}
\]

and therefore

\[
\boxed{a_p(x)=a_q(x).}
\]

Using `A_qp=R_qp`,

\[
\begin{aligned}
e_q(x)A_{qp}
&=a_q(x)I_3A_{qp}\\
&=a_p(x)R_{qp}\\
&=R_{qp}a_p(x)I_3\\
&=R_{qp}e_p(x).
\end{aligned}
\]

Thus

\[
\boxed{e_q(x)A_{qp}=R_{qp}e_p(x)}
\]

holds pointwise on every certified overlap sample.

## 6. Spatial variation is retained

The overlap law compares two chart representations of the same physical point. It does not equate the field at distinct physical points. Therefore two overlap samples `x` and `y` may satisfy

\[
\nu_p(x)=\nu_q(x),
\qquad
\nu_q(y)=\nu_r(y),
\]

while

\[
\boxed{\nu(x)\neq\nu(y).}
\]

Consequently

\[
\boxed{a(x)\neq a(y)}
\]

is admitted on a connected patch cover.

This preserves the RF-02I exact local relation

\[
\boxed{f_i=E_i(\ln a)=-E_i(\ln|\omega|),}
\]

so spatial gradients of the phase-scale field remain available to the connection and curvature layers.

## 7. Source-packet reduction

On this sufficient route, the general spatial matrix packet

```text
local coframe matrices e_p(x)
spatial Jacobians A_qp
SO(3) frame rotations R_qp
```

is generated from

```text
TIR anchor vectors r_p
TIR orthonormal frames Q_p
overlap-local samples of the phase-magnitude field nu=|omega_t|
shared magnitude-field provenance on each represented overlap
```

through

\[
\boxed{A_{qp}=R_{qp}=Q_q^TQ_p,}
\]

\[
\boxed{t_{qp}=Q_q^T(r_p-r_q),}
\]

\[
\boxed{e_p(x)=\frac{c}{\sqrt6\,\nu_p(x)}I_3.}
\]

GSC4C can supply overlap incidence from the production A5 tetrahedral facet witness. The lapse and matching-flow/shift routes retain their existing owners.

## 8. Production witness

The production rigid-route witness contains:

1. source-owned anchor vectors `r_p`;
2. source-owned `SO(3)` frame matrices `Q_p`;
3. one declared phase-magnitude field identity and clock calibration;
4. finite positive overlap-local magnitude samples `nu_p(x_alpha)`;
5. pointwise equality of the two chart representatives on each physical overlap sample;
6. provenance linking every sample to its physical overlap point.

A compact one-rate-per-patch representation remains useful as a reference fixture. Production certification uses overlap-local field samples and therefore admits spatial variation across the represented domain.

## 9. Executable surface

Implementation:

`src/rfc/anchored_phase_scaled_rigid_geometry.py`

Reference tests:

`tests/reference/test_gsc4d_anchored_phase_scaled_rigid_geometry.py`

The executable surface checks:

- finite anchors and rates;
- `Q_p in SO(3)`;
- anchored rigid `A=R` construction;
- anchored translations;
- overlap-local phase-field sample coverage;
- pointwise phase-scale agreement;
- `e_qA=Re_p` at each overlap sample;
- connected-cover examples with distinct phase scales at distinct points;
- separation from the general smooth GSC4A route.

## 10. Claim ledger

| Statement | Status |
|---|---|
| `A_qp=Q_q^TQ_p` | `EXACT TIR AFFINE ALGEBRA` |
| `R_qp=Q_q^TQ_p` | `EXACT` |
| `A_qp=R_qp` on anchored rigid route | `EXACT ROUTE SPECIALIZATION` |
| `vartheta=dx` on common anchored affine carrier | `EXACT ROUTE SPECIALIZATION` |
| `e(x)=c I/(sqrt6 |omega_t(x)|)` | `EXACT CONDITIONAL PHASE-CLOCK PHYSICALIZATION` |
| pointwise shared magnitude gives `e_qA=Re_p` | `EXACT` |
| connected cover admits varying `a(x)` | `EXACT REPRESENTATION PROPERTY` |
| executable overlap-local field certifier | `VALIDATION TARGET` |
| production anchor/frame/magnitude-field packet | `OPEN SOURCE INPUT` |
| production overlap sample provenance | `OPEN SOURCE BINDING` |
| general smooth GSC4A route | `SEPARATE HOSTED-PASS ROUTE` |

## 11. Live 36D boundary

The v0.2 field-semantics correction was audited through the active

```text
GREMLIN -> Terminal36D -> PhaseNav36D -> GREMLIN
```

surface. The audit authority remains `CANDIDATE_ONLY`; deterministic hosted validation remains the executable theorem evidence surface.
