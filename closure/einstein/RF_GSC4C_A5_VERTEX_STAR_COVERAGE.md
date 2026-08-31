# RF-GSC4C — A5 Vertex-Star Coverage for Source-Assembled Spacetime Atlases

Status: `EXACT_SIMPLICIAL_OPEN_STAR_COVERAGE / EXACT_PAIR_TRIPLE_INCIDENCE_DERIVATION / GSC4_COVERAGE_INPUT_REDUCTION / SOURCE_GEOMETRY_VALUES_OPEN`

Date: 2026-08-31

## 1. Purpose

RF-GSC4A requires a production patch cover and explicit pair/triple overlap incidence before source transition values are delegated to RF-E25. TIR Gate A5 already promotes the spatial carrier through a supplied tetrahedral simplicial complex once the global manifold certificate passes.

RF-GSC4C shows that one sufficient patch cover is determined directly by that A5 complex. Production overlap coverage therefore need not remain an independent datum on this route.

## 2. A5 parent

Let

\[
K=(V,E,F,\mathcal T)
\]

be a finite pure tetrahedral simplicial complex carrying an admitted TIR A5 manifold certificate.

For each vertex \(v\in V\), let

\[
\operatorname{st}^\circ_K(v)
\]

be its open simplicial star in the geometric realization \(|K|\).

Every point of \(|K|\) lies in the relative interior of one simplex. That simplex contains at least one vertex, hence the point lies in the open star of each vertex of the simplex. Therefore

\[
\boxed{|K|=\bigcup_{v\in V}\operatorname{st}^\circ_K(v).}
\]

The vertex open stars form a canonical cover indexed by the A5 vertex carrier.

## 3. Pair overlap incidence

For two distinct vertices \(v,w\),

\[
\operatorname{st}^\circ(v)\cap\operatorname{st}^\circ(w)\neq\varnothing
\]

exactly when some simplex contains both vertices. In a simplicial complex this is equivalent to

\[
\boxed{\{v,w\}\in E.}
\]

Thus pair overlap incidence is the edge set of the A5 complex.

## 4. Triple overlap incidence

For three distinct vertices \(u,v,w\),

\[
\operatorname{st}^\circ(u)\cap\operatorname{st}^\circ(v)\cap\operatorname{st}^\circ(w)\neq\varnothing
\]

exactly when the three vertices span a simplex, equivalently a triangular face:

\[
\boxed{\{u,v,w\}\in F.}
\]

Hence the triple-overlap list required for coordinate/Lorentz cocycle checks is determined by the triangular-face carrier already generated as the downward closure of the tetrahedral facet list.

## 5. Facet-list sufficiency for coverage indices

For each tetrahedron \(\tau=\{a,b,c,d\}\), all six two-subsets are edges and all four three-subsets are triangles. Therefore the supplied tetrahedral facets determine

\[
V,
\qquad E,
\qquad F,
\]

by finite downward closure. No independent overlap-incidence table is required for the vertex-star route.

This result concerns cover indices and incidence. The numerical source geometry remains separately typed:

```text
TIR spatial coframes e                         source geometry packet
spatial Jacobians A                            source geometry packet
SO(3) frame rotations R                        source geometry packet
IDT lapse N                                    source temporal packet
matching shift/drift or flow-adapted route     GSC3/GSC4 source route
```

## 6. RF-GSC4A handoff

Given the GSC4C coverage certificate, RF-GSC4A can instantiate source-overlap objects precisely on the derived pair-overlap list and supply its triangle list from the derived triple overlaps.

The resulting dependency reduction is

```text
GSC1 production tetrahedral facet list
 + TIR A5 manifold PASS
 -> GSC4C vertex-star cover
 -> pair overlap indices from edges
 -> triple overlap indices from triangles
 -> RF-GSC4A / GSC4B source packet assembly
```

The transition values on those overlaps remain source-owned inputs.

## 7. Executable surface

Implementation:

`src/rfc/a5_vertex_star_coverage.py`

Reference tests:

`tests/reference/test_gsc4c_a5_vertex_star_coverage.py`

The implementation requires an explicit A5 parent admission, validates the supplied tetrahedral facets, derives the downward edge/triangle closure, and emits deterministic patch/pair/triple identifiers.

## 8. Claim ledger

| Statement | Status |
|---|---|
| vertex open stars cover the admitted simplicial realization | `EXACT` |
| pair vertex-star overlap iff the vertices span an edge | `EXACT` |
| triple vertex-star overlap iff the vertices span a triangle | `EXACT` |
| tetrahedral facets determine pair/triple overlap incidence | `EXACT FINITE CONSTRUCTION` |
| independent production overlap-incidence packet on this route | `DERIVED FROM GSC1 FACET INPUT` |
| numerical `e,A,R,N,b,v` values | `SOURCE PACKETS / DOWNSTREAM ROUTES` |
| actual GSC1 production tetrahedral complex | `OPEN INPUT` |

## 9. Runtime audit boundary

The coverage reduction was audited through the active

```text
GREMLIN -> Terminal36D -> PhaseNav36D -> GREMLIN
```

surface with `CANDIDATE_ONLY` authority. The deterministic simplicial construction and hosted tests remain the executable evidence surface.
