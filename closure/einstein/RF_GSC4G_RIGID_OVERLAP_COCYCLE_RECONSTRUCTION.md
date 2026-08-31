# RF-GSC4G — Rigid SE(3) Overlap-Cocycle Reconstruction

Status: `EXACT_CONNECTED_COCYCLE_RECONSTRUCTION_THEOREM / EXECUTABLE_HOLONOMY_CERTIFIER / NUMERIC_OVERLAP_COCYCLE_SOURCE_INPUT_OPEN`

Date: 2026-08-31

## 1. Scope

RF-GSC4F identifies the common ambient `SE(3)` action on the anchored rigid route as gauge and replaces absolute anchors/frames by the relative rigid configuration modulo one global Euclidean frame.

RF-GSC4G gives a minimal representation of that quotient geometry directly in terms of rigid overlap data.

For every oriented overlap `p -> q`, write

\[
\boxed{x_q=A_{qp}x_p+t_{qp}},
\qquad
A_{qp}\in SO(3),
\qquad
t_{qp}\in\mathbb R^3.
\]

For anchored charts

\[
x_p=Q_p^T(r-r_p),
\]

the exact overlap coefficients are

\[
\boxed{A_{qp}=Q_q^TQ_p},
\qquad
\boxed{t_{qp}=Q_q^T(r_p-r_q)}.
\]

## 2. Inverse and composition laws

The inverse overlap is

\[
\boxed{A_{pq}=A_{qp}^T},
\qquad
\boxed{t_{pq}=-A_{qp}^Tt_{qp}}.
\]

For consecutive overlaps `p -> q -> r`,

\[
x_r=A_{rq}(A_{qp}x_p+t_{qp})+t_{rq},
\]

hence

\[
\boxed{A_{rp}=A_{rq}A_{qp}},
\qquad
\boxed{t_{rp}=A_{rq}t_{qp}+t_{rq}}.
\]

These are the `SE(3)` cocycle laws in the coordinate convention used by RF-GSC4D.

## 3. Reconstruction after global gauge fixing

Let the overlap graph be connected and choose one root patch `0`. RF-GSC4F permits the canonical gauge

\[
\boxed{Q_0=I_3},
\qquad
\boxed{r_0=0}.
\]

Suppose `p` has already been reconstructed and an oriented tree edge `p -> q` is supplied. From

\[
A_{qp}=Q_q^TQ_p
\]

we obtain

\[
\boxed{Q_q=Q_pA_{qp}^T}.
\]

From

\[
t_{qp}=Q_q^T(r_p-r_q)
\]

we obtain

\[
\boxed{r_q=r_p-Q_qt_{qp}}.
\]

Therefore one connected spanning tree reconstructs every anchored chart in the fixed global gauge.

## 4. Minimal continuous coordinate count

For `N` patches, anchored data contain

\[
3N+3N=6N
\]

continuous coordinates: three anchor coordinates and three frame coordinates per patch.

RF-GSC4F removes one global `SE(3)` action with six continuous parameters, leaving

\[
\boxed{6N-6=6(N-1)}.
\]

A spanning tree has exactly `N-1` edges, and each `SE(3)` overlap edge carries six continuous coordinates. Thus the spanning-tree overlap packet has exactly the same continuous dimension:

\[
\boxed{\dim(\text{tree overlap packet})=6(N-1)}.
\]

The tree packet is therefore a minimal continuous representation of the anchored rigid configuration modulo global `SE(3)`.

## 5. Non-tree edges as holonomy checks

Any additional edge closes one or more graph cycles. It introduces no new local chart degree of freedom once the tree reconstruction is fixed; instead it tests path independence.

For a cycle

\[
p_0\to p_1\to\cdots\to p_k=p_0,
\]

composition must return the identity rigid transformation:

\[
\boxed{A_C=I_3},
\qquad
\boxed{t_C=0}.
\]

Equivalently, the chart reconstructed along any two paths to the same patch must agree. Failure of either the rotational or translational closure is a fail-closed holonomy defect.

## 6. Source boundary

The theorem reconstructs the relative rigid realization from a supplied numeric `SE(3)` overlap cocycle. The production source coordinate is therefore typed as

\[
\boxed{\text{connected numeric rigid-overlap cocycle}}
\]

with one spanning-tree packet providing the independent continuous coordinates and any additional overlap edges providing cycle-closure evidence.

The TIR A5 tetrahedral facet witness supplies the topological complex and, through GSC4C, the cover/incidence structure on which the overlap cocycle is indexed. The numeric overlap values are carried by the source geometry witness.

RF-GSC4E separately supplies the overlap-local positive phase-magnitude field used to physicalize the spatial coframe scale.

## 7. Executable certifier

Implementation:

`src/rfc/rigid_overlap_cocycle_reconstruction.py`

Reference tests:

`tests/reference/test_gsc4g_rigid_overlap_cocycle_reconstruction.py`

The certifier:

1. validates finite `SO(3)` rotations and finite translations;
2. constructs inverse overlap edges;
3. reconstructs all patches from one canonical root;
4. requires graph connectivity;
5. compares every alternate reconstruction path;
6. compares every supplied edge against the reconstructed chart packet;
7. fails closed on rotational or translational holonomy defects;
8. reports `minimal_tree_edge_count=N-1`;
9. reports `minimal_continuous_relative_dof=6(N-1)`;
10. retains `production_geometry_promoted=false`.

## 8. Falsification controls

The reference suite includes:

- exact inverse-edge closure;
- exact two-edge composition;
- two-patch reconstruction;
- three-patch `6N-6` count;
- a consistent triangle with redundant direct edge;
- a translational cycle defect;
- a rotational cycle defect;
- disconnected-graph rejection;
- duplicate directed-edge rejection;
- orientation-reversing frame rejection.

## 9. Live GREMLIN × Terminal36D × PhaseNav audit

The candidate seam was routed through the active NOEMA surface

```text
/dev/shm/ciel_noema
 -> GREMLIN
 -> Terminal36D
 -> PhaseNav 36D
 -> GREMLIN_PHASE36D_FUSED
```

with `CANDIDATE_ONLY` authority.

Fresh audit:

- source event: `gremlin:whisper:sha256:17298a9f3fbef8e1885f5aafe61f527bcff2c56c9a7f3bd0bbbc3491c34f18c4`;
- fused event: `gremlin:whisper:sha256:b53e11c0bd44409c67bf69a9fcfa473677e6ed0f09d67cdb1c7edc7d8935ca52`;
- Terminal36D receipt: `6a20188be0100f732dca2d5f5ffd34d2fd6d99fa5cc292cbec0e8e918e7f0043`;
- PhaseNav trace: `8d2e7c4957ff5ee2ba844e7c0e1ef42a96c97c49450d0f599fd59c5e4bfaedc5`;
- shape: `[12,36]`.

Runtime audit evidence remains separate from hosted theorem validation.

## 10. Claim ledger

| Statement | Status |
|---|---|
| rigid inverse law | `EXACT` |
| rigid composition law | `EXACT` |
| connected spanning-tree packet reconstructs all charts in fixed global gauge | `EXACT` |
| continuous quotient dimension is `6N-6` | `EXACT` |
| spanning tree carries exactly `6(N-1)` continuous overlap coordinates | `EXACT` |
| non-tree edges test path independence / holonomy closure | `EXACT` |
| executable reconstruction and holonomy certifier | `HOSTED VALIDATION TARGET` |
| production numeric rigid-overlap cocycle | `OPEN SOURCE INPUT` |
| GSC4E overlap-local phase-magnitude field | `SEPARATELY TYPED OPEN SOURCE INPUT` |
| RF-E25 production shared atlas | `DOWNSTREAM GSC4A/GSC4B GATE` |

Target verdict:

`PASS_RFC_GSC4G_RIGID_OVERLAP_COCYCLE_RECONSTRUCTION_WITH_NUMERIC_COCYCLE_INPUT_OPEN`.
