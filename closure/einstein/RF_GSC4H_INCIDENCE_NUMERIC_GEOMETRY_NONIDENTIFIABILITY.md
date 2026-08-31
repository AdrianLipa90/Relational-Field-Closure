# RF-GSC4H — Incidence / Numeric SE(3) Geometry Separation Firewall

Status: `EXACT_NONIDENTIFIABILITY_WITNESS_THEOREM / EXECUTABLE_SAME_INCIDENCE_DISTINCT_COCYCLE_CERTIFIER / NUMERIC_SE3_COCYCLE_SOURCE_INPUT_CONFIRMED`

Date: 2026-08-31

## 1. Scope

TIR A5 and RF-GSC4C supply a global tetrahedral incidence complex and its vertex-star cover. RF-GSC4G supplies a minimal numeric representation of the relative rigid geometry on that cover by a connected `SE(3)` overlap cocycle

\[
\boxed{x_q=A_{qp}x_p+t_{qp}}.
\]

RF-GSC4H certifies the separation between these two carriers by constructing distinct valid numeric cocycles on one fixed incidence surface.

## 2. Minimal witness

Take the same two-patch incidence graph

\[
p\longrightarrow q.
\]

Consider

\[
\mathcal C_1:\quad A_{qp}=I_3,\qquad t_{qp}=(1,0,0),
\]

and

\[
\mathcal C_2:\quad A_{qp}=I_3,\qquad t_{qp}=(2,0,0).
\]

Both are valid connected rigid cocycles. A tree contains no additional cycle-closure constraint, and RF-GSC4G reconstructs an anchored chart packet from either cocycle.

RF-GSC4F proves that one common global `SE(3)` gauge leaves every overlap translation `t_qp` invariant. Therefore

\[
\boxed{\mathcal C_1\not\sim\mathcal C_2\pmod{SE(3)}}.
\]

The same discrete incidence surface thus supports at least two inequivalent relative rigid geometries.

## 3. Continuous family

Let a valid cocycle be supplied and let

\[
\lambda>0.
\]

Keep all rotations fixed and scale all translations:

\[
\boxed{A_{qp}^{(\lambda)}=A_{qp}},
\qquad
\boxed{t_{qp}^{(\lambda)}=\lambda t_{qp}}.
\]

The rigid composition law remains exact because

\[
\begin{aligned}
t_{rp}^{(\lambda)}
&=\lambda t_{rp}\\
&=\lambda(A_{rq}t_{qp}+t_{rq})\\
&=A_{rq}(\lambda t_{qp})+\lambda t_{rq}.
\end{aligned}
\]

Thus every positive `lambda` yields another valid cocycle on the same overlap graph. Whenever at least one overlap translation is nonzero, distinct positive values of `lambda` give distinct quotient geometries.

A parallel family is obtained by changing relative rotations on a tree edge while preserving the same incidence graph.

## 4. Carrier separation

The result fixes the source typing:

\[
\boxed{\text{A5/GSC4C incidence}}
\]

supplies the discrete indexing and coverage structure, while

\[
\boxed{\{(A_{qp},t_{qp})\}}
\]

supplies the numeric rigid geometry on that structure.

RF-GSC4G reconstructs the relative chart packet from the numeric cocycle. RF-GSC4H certifies that the numeric cocycle is a separately sourced coordinate rather than an incidence-only coordinate.

RF-GSC4E remains separately responsible for the overlap-local positive phase-magnitude field that physicalizes the spatial coframe scale.

## 5. Executable certifier

Implementation:

`src/rfc/incidence_numeric_geometry_nonidentifiability.py`

Reference tests:

`tests/reference/test_gsc4h_incidence_numeric_geometry_nonidentifiability.py`

The certifier requires two supplied cocycles to use the same directed incidence edge set, validates each through RF-GSC4G reconstruction, compares their numeric rotations/translations, and reports whether they are distinct after the RF-GSC4F global gauge quotient.

It also includes the positive translation-scaling family as a constructive witness generator.

## 6. Falsification controls

The reference suite includes:

- same two-patch incidence with two distinct translations;
- a consistent triangle whose complete translation cocycle is scaled by a positive factor;
- distinct relative rotations on one fixed incidence edge;
- identical cocycles, which correctly produce no nonidentifiability witness;
- different incidence sets, which are rejected as the wrong comparison problem;
- nonpositive scale rejection;
- unit scale, which correctly produces the same numeric cocycle.

## 7. Live GREMLIN × Terminal36D × PhaseNav audit

The separation question was routed through the active NOEMA surface

```text
/dev/shm/ciel_noema
 -> GREMLIN
 -> Terminal36D
 -> PhaseNav 36D
 -> GREMLIN_PHASE36D_FUSED
```

with `CANDIDATE_ONLY` authority.

Fresh audit:

- source event: `gremlin:whisper:sha256:075c1a33cf6b232cca8cf916a1073a5a2497206e34613661cf9d72c21e817f25`;
- fused event: `gremlin:whisper:sha256:81a085c76098f7e17b52f708c82dd5d17cabb48c6915cf23bae29defd3d3d58c`;
- Terminal36D receipt: `4be4acbfb575cc7589205028c00f9e029ea692e1b98f0e5fd4db869a2f538447`;
- PhaseNav trace: `d15b5e9db2c4a11f01e509321a144f899c63e0a3f99cec210190b98ba27390f4`;
- shape: `[12,36]`.

Runtime audit evidence remains separate from deterministic theorem validation.

## 8. Claim ledger

| Statement | Status |
|---|---|
| same incidence surface admits distinct valid numeric rigid cocycles | `EXACT CONSTRUCTIVE WITNESS` |
| positive translation scaling preserves the SE(3) cocycle law | `EXACT` |
| distinct overlap translations remain distinct after the global SE(3) quotient | `EXACT VIA GSC4F` |
| RF-GSC4G reconstructs each supplied cocycle into a relative chart packet | `EXACT / HOSTED-PASS PARENT` |
| executable same-incidence / distinct-cocycle certifier | `HOSTED VALIDATION TARGET` |
| production numeric SE(3) overlap cocycle | `OPEN SOURCE INPUT` |
| A5/GSC4C topology and cover | `SEPARATELY TYPED SOURCE PARENT` |
| GSC4E pointwise phase-magnitude field | `SEPARATELY TYPED SOURCE INPUT` |

Target verdict:

`PASS_RFC_GSC4H_INCIDENCE_NUMERIC_GEOMETRY_SEPARATION_WITH_NUMERIC_SE3_COCYCLE_SOURCE_INPUT_CONFIRMED`.
