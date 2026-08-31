# RF-GSC4F — Global SE(3) Gauge Quotient for the Anchored Rigid Spatial Route

Status: `EXACT_GLOBAL_SE3_QUOTIENT_THEOREM / EXECUTABLE_REFERENCE_PATCH_GAUGE_CERTIFIER / RELATIVE_RIGID_GEOMETRY_SOURCE_INPUT_OPEN`

Date: 2026-08-31

## 1. Scope

RF-GSC4D represents one sufficient rigid spatial route by anchored Pauli charts

\[
\boxed{x_p=Q_p^T(r-r_p)},
\qquad Q_p\in SO(3),
\]

with overlap data

\[
\boxed{A_{qp}=Q_q^TQ_p},
\qquad
\boxed{t_{qp}=Q_q^T(r_p-r_q)}.
\]

RF-GSC4E separately supplies the overlap-local positive phase-magnitude field used by the physical coframe scale. RF-GSC4F isolates the global Euclidean gauge carried by the absolute anchor origin and absolute frame orientation.

## 2. Global Euclidean gauge action

Let

\[
S\in SO(3),
\qquad a\in\mathbb R^3.
\]

Apply one common transformation to every rigid chart:

\[
\boxed{r'_p=S^T(r_p-a)},
\qquad
\boxed{Q'_p=S^TQ_p}.
\]

Then

\[
A'_{qp}
=(Q'_q)^TQ'_p
=Q_q^TSS^TQ_p
=\boxed{A_{qp}}.
\]

For the translational overlap coordinate,

\[
\begin{aligned}
t'_{qp}
&=(Q'_q)^T(r'_p-r'_q)\\
&=Q_q^TS\,S^T[(r_p-a)-(r_q-a)]\\
&=\boxed{Q_q^T(r_p-r_q)}\\
&=\boxed{t_{qp}}.
\end{aligned}
\]

Thus the complete rigid overlap packet is invariant under one common global `SE(3)` gauge.

## 3. Canonical reference-patch gauge

Choose one admitted patch `p0`. Set

\[
S=Q_{p0},
\qquad
a=r_{p0}.
\]

Then

\[
\boxed{r'_{p0}=0},
\qquad
\boxed{Q'_{p0}=I_3}.
\]

All pairwise overlap rotations and translations remain unchanged. Therefore six global coordinates — three translational and three rotational — may be gauge-fixed without changing the GSC4D/GSC4A overlap geometry.

The production rigid-spatial witness is consequently typed by the equivalence class

\[
\boxed{\{(r_p,Q_p)\}_p/SE(3)}
\]

rather than by an absolute ambient origin and orientation.

## 4. Retained source geometry

The quotient retains the relative rigid configuration. In particular, a common spatial scaling

\[
r_p\mapsto\lambda r_p,
\qquad \lambda>0,
\]

changes

\[
t_{qp}\mapsto\lambda t_{qp}
\]

and therefore represents a distinct relative geometry unless separately compensated by an admitted physical scale transformation.

Likewise, patch-dependent frame changes modify `A_qp` unless their induced overlap transformation is explicitly carried by the source atlas. RF-GSC4F therefore removes only the common ambient `SE(3)` gauge.

## 5. Relation to GSC1 and GSC4E

The GSC1/A5 tetrahedral facet witness supplies global topological incidence and the smooth-manifold certification route. The numerical relative rigid configuration remains a source geometry coordinate.

RF-GSC4E supplies the overlap-local field

\[
\nu(x)=|\omega_t(x)|>0
\]

and the coframe scale

\[
s(x)=\frac{c}{\sqrt6\,\nu(x)}.
\]

The global `SE(3)` quotient acts on anchors and frames and leaves this scalar phase-magnitude field separately typed.

## 6. Executable certifier

Implementation:

`src/rfc/global_se3_gauge_quotient.py`

Reference tests:

`tests/reference/test_gsc4f_global_se3_gauge_quotient.py`

The certifier:

1. validates finite `SO(3)` frames;
2. computes every pairwise `(A_qp,t_qp)` overlap;
3. fixes one reference patch to `(0,I_3)`;
4. recomputes all overlaps;
5. requires the before/after defects to vanish to tolerance;
6. reports `global_gauge_dof_removed=6`;
7. preserves `relative_rigid_configuration_retained=true` and `production_geometry_promoted=false`.

## 7. Falsification controls

The reference suite includes:

- arbitrary common translation;
- arbitrary common rotation;
- canonical reference-patch gauge;
- explicit spatial rescaling, which changes relative translation data;
- independent single-patch frame rotation, which changes relative overlap data;
- non-orthogonal and orientation-reversing frame rejection.

These controls separate global coordinate gauge from the retained relative source geometry.

## 8. Live GREMLIN × Terminal36D × PhaseNav audit

The candidate was routed through the active NOEMA surface

```text
/dev/shm/ciel_noema
 -> GREMLIN
 -> Terminal36D
 -> PhaseNav 36D
 -> GREMLIN_PHASE36D_FUSED
```

with `CANDIDATE_ONLY` authority.

Fresh audit:

- source event: `gremlin:whisper:sha256:8609d93ffe0ef3804778db90384c299a7df7ef6fd3b8beb7f38511d17b5ef73e`;
- fused event: `gremlin:whisper:sha256:0970d60244e47887f1f3c127c5747810fb111dd1a6983cc9ec4ca1d6f0eafacf`;
- Terminal36D receipt: `db1df21b30f75fda97671ce4e235a67d2b27dcfad5e4dce3a82178215f0cf963`;
- PhaseNav trace: `1031a3423894408b1f288097873789f411355c6f3e84c8d3568b3500d5b6682e`;
- shape: `[12,36]`.

Runtime audit evidence remains separate from hosted theorem validation.

## 9. Claim ledger

| Statement | Status |
|---|---|
| common global `SE(3)` action leaves `A_qp` invariant | `EXACT` |
| common global `SE(3)` action leaves `t_qp` invariant | `EXACT` |
| one reference patch may be fixed to `r=0,Q=I` | `EXACT` |
| six absolute ambient coordinates are gauge | `EXACT` |
| relative rigid configuration survives the quotient | `EXACT` |
| A5 production incidence supplies topology/coverage | `SOURCE-BOUND PARENT` |
| production relative rigid configuration | `OPEN SOURCE INPUT` |
| production overlap-local phase magnitude field | `OPEN SOURCE INPUT VIA GSC4E` |
| RF-E25 production shared atlas | `DOWNSTREAM GSC4A/GSC4B GATE` |

Target verdict:

`PASS_RFC_GSC4F_GLOBAL_SE3_GAUGE_QUOTIENT_WITH_RELATIVE_GEOMETRY_SOURCE_INPUT_OPEN`.
