# RF-GSC3C — State-to-Vertex Binding Non-Identifiability

Status: `EXACT_RELABELING_NONIDENTIFIABILITY_THEOREM / EXECUTABLE_SYMMETRY_WITNESS / SHARED_NAMESPACE_OR_EXPLICIT_SOURCE_BINDING_REQUIRED`

Date: 2026-08-31

## 1. Purpose

RF-GSC3B supplies a quotient-descended event-placement construction once an IDT occurrence terminal state is source-bound to a TIR spatial vertex. The remaining source coordinate is therefore the binding

\[
a:S\to V(\Sigma),
\]

between the IDT 00F state-label carrier `S` and the TIR GSC-1 vertex-label carrier `V(Sigma)`.

RF-GSC3C records the exact identifiability statement for this seam. The parent contracts admit independent relabelings of their identifiers. This symmetry determines when a source-free canonical state-to-vertex selection can be invariantly defined.

## 2. Parent identifier carriers

IDT 00F uses an abstract relational state set

\[
S
\]

and terminal labels

\[
x_k=t(P_k)\in S.
\]

TIR GSC-1 accepts a finite set of unique string vertex identifiers

\[
V=V(\Sigma)
\]

together with tetrahedral incidence. The manifold certificate depends on the incidence structure and is covariant under a consistent permutation of vertex labels.

Thus, before a cross-repository binding is supplied, the identifier seam carries independent relabeling symmetry

\[
\boxed{\operatorname{Sym}(S)\times\operatorname{Sym}(V).}
\]

## 3. Non-identifiability theorem

Assume `S` is non-empty and `V` contains at least two vertices. Suppose a source-free canonical assignment

\[
f:S\to V
\]

is required to be natural under independent relabelings.

Hold the IDT labels fixed and apply an arbitrary vertex permutation

\[
\tau\in\operatorname{Sym}(V).
\]

Naturality would require

\[
\boxed{f(s)=\tau(f(s))}
\]

for every `s in S` and every `tau`.

Choose any `s_0 in S` and write

\[
v_0=f(s_0).
\]

Since `|V|>=2`, choose `v_1!=v_0` and let `tau` be the transposition exchanging `v_0` and `v_1`. Then

\[
\tau(f(s_0))=v_1\ne v_0=f(s_0),
\]

contradicting relabeling naturality.

Therefore the independent parent symmetries yield the exact obstruction

\[
\boxed{
|S|>0,\ |V|>1
\Longrightarrow
\text{state-to-vertex binding requires symmetry-breaking source information}.
}
\]

The source information can be carried by either of the two RF-GSC3B admission routes:

1. a declared shared identifier namespace;
2. an explicit source-owned map `state_id -> TIR spatial_vertex_id`.

## 4. Exceptional one-vertex sector

For `|V|=1`, the target permutation group fixes the unique vertex, so one constant assignment exists. The GSC-1 closed three-manifold production sector uses a nontrivial tetrahedral carrier and therefore lies in the `|V|>1` theorem sector.

This exceptional case is retained in the executable certifier so that the theorem is typed precisely rather than overgeneralized.

## 5. Relation to RF-GSC3B

RF-GSC3B proves the quotient descent

\[
a=\bar a\circ q
\]

exactly when the occurrence-level spatial anchor is constant on each event-quotient fibre.

RF-GSC3C sits one step upstream:

```text
IDT 00F state labels S
+ TIR GSC-1 vertex labels V(Sigma)
+ independent relabeling symmetry
-> RF-GSC3C non-identifiability theorem
-> shared namespace OR explicit source-owned state->vertex map
-> RF-GSC3B quotient-fibre constancy
-> unique event spatial anchor
```

The theorem therefore converts an informal mapping choice into a typed source-information coordinate.

## 6. Executable witness

The reference implementation accepts finite state and vertex identifier sets together with a proposed state-to-vertex map. In the nontrivial target sector it constructs a vertex transposition that:

- preserves the cardinality and abstract identifier structure of the TIR carrier;
- leaves the IDT state carrier untouched;
- changes at least one image of the proposed map.

The returned witness demonstrates the independent relabeling orbit explicitly. It validates the symmetry obstruction; it does not select a physical binding.

Implementation:

`src/rfc/state_vertex_binding_nonidentifiability.py`

Tests:

`tests/reference/test_gsc3c_state_vertex_binding_nonidentifiability.py`

## 7. Claim ledger

| Claim | Status |
|---|---|
| IDT 00F terminal labels live in an abstract state set `S` | `PARENT IDT 00F` |
| TIR GSC-1 vertices are explicit unique identifiers with incidence data | `PARENT TIR GSC-1 INPUT CONTRACT` |
| independent identifier relabelings act before a cross-repo binding | `EXACT TYPING SYMMETRY` |
| no invariant source-free map exists for non-empty `S` and `|V|>1` | `EXACT RELABELING NONIDENTIFIABILITY THEOREM` |
| transposition witness changes any proposed map in the nontrivial target sector | `EXACT / EXECUTABLE` |
| shared namespace or explicit source-owned map breaks the relabeling ambiguity | `SOURCE-BINDING ADMISSION CONTRACT` |
| production state-to-TIR-vertex binding | `OPEN SOURCE INPUT` |

## 8. Promotion firewall

RF-GSC3C certifies the identifiability boundary. Production event placement is promoted only after a source-owned namespace/binding receipt is supplied and RF-GSC3B quotient-fibre constancy passes on production occurrence/event data.

GREMLIN, PhaseNav and Terminal36D may audit candidate dependency structure with `CANDIDATE_ONLY` authority; deterministic source contracts and hosted validation remain the executable evidence surface.
