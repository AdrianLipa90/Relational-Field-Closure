# RF-GSC3B — Quotient-Descended Relational Event Placement Binding

Status: `EXACT_QUOTIENT_FACTORING_THEOREM / EXECUTABLE_RELATIONAL_PLACEMENT_CERTIFIER / SHARED_RELATIONAL_STATE_BINDING_OPEN / PRODUCTION_INPUT_OPEN`

Date: 2026-08-31

## 1. Purpose

RF-GSC3 supplies the sufficient product carrier

\[
M=I\times\Sigma,
\qquad t=\operatorname{pr}_I,
\]

and records an event placement candidate

\[
\iota(v)=(t_v+C,p_v),\qquad p_v\in\Sigma.
\]

IDT 00F already assigns every realized occurrence

\[
\nu_k=(P_k,x_k)
\]

a terminal relational-state label \(x_k=t(P_k)\). IDT 05J separately introduces the quotient from occurrence identifiers to event identifiers. RF-GSC3B tests whether the spatial part of the event placement can be inherited from that existing relational state instead of being chosen independently.

## 2. Quotient-factorization theorem

Let \(O\) be the occurrence set and let

\[
q:O\to E
\]

be the 05J event quotient. Let a source-owned spatial binding give

\[
a:O\to V(\Sigma),
\]

where \(a(o)\) is obtained from the 00F terminal state of occurrence \(o\), either by a shared identifier namespace or by an explicit terminal-state-to-spatial-vertex map.

Then the following are equivalent:

1. \(a\) is constant on every quotient fibre \(q^{-1}(e)\);
2. there exists a unique map

\[
\boxed{\bar a:E\to V(\Sigma)}
\]

such that

\[
\boxed{a=\bar a\circ q.}
\]

This is the standard factorization property of a quotient map at the set level. The executable certifier checks its finite production-data realization directly.

## 3. Event placement on the RF-GSC3 product carrier

Let 05H provide an exact event clock

\[
t_E:E\to I
\]

up to one common additive calibration. When the quotient-factorization condition holds, define

\[
\boxed{
\iota(e)=\bigl(t_E(e)+C,\bar a(e)\bigr)
\in I\times |\Sigma|.
}
\]

Then

\[
\boxed{
\operatorname{pr}_I\circ\iota=t_E+C.
}
\]

The temporal coordinate therefore remains the exact 05H clock, while the discrete spatial anchor is inherited from the terminal relational state carried by the occurrence quotient.

## 4. Shared-state binding gate

The exact factorization theorem does not select the physical map from IDT terminal-state labels to TIR spatial vertices. Production use requires one of two source-owned bindings:

```text
A. shared namespace:
   terminal_state_id == TIR spatial_vertex_id

B. explicit map:
   terminal_state_id -> TIR spatial_vertex_id
```

Every target of the explicit map must be a vertex of the supplied GSC-1 spatial complex. A reference fixture cannot establish the production binding.

The resulting dependency line is

```text
IDT 00F occurrence nu=(P,x)
 + IDT 05J quotient q:O->E
 + TIR GSC-1 spatial vertex set V(Sigma)
 + source-owned state->vertex binding
 -> quotient-fibre constancy gate
 -> unique event spatial anchor a_bar:E->V(Sigma)
 + IDT 05H exact event clock
 -> iota(e)=(t_E(e)+C,a_bar(e))
 -> RF-GSC3 product carrier event placement
 -> RF-E25 production ADM/coframe realization
```

## 5. Injectivity is a separate gate

The quotient-factorization theorem determines one spatial anchor for each event class. It does not require two distinct event classes to have distinct pairs \((t,p)\).

The implementation therefore reports whether the resulting placement is injective and only rejects a collision when `require_injective=true` is explicitly requested by a downstream sector.

## 6. Falsification rules

The certifier fails closed if:

1. spatial vertex identifiers are empty or duplicated;
2. an occurrence lacks its terminal-state identifier;
3. event classes fail to partition the supplied occurrences exactly once;
4. a terminal state has no source-bound TIR spatial vertex;
5. one event quotient fibre maps to more than one spatial vertex;
6. the event clock does not cover exactly the event quotient or contains non-finite values;
7. the common clock offset is non-finite;
8. an injective placement is explicitly required and two event classes collide at the same \((t,p)\).

## 7. Claim ledger

| Claim | Status |
|---|---|
| occurrence terminal state \(x_k=t(P_k)\) | `PARENT IDT 00F` |
| event quotient \(q:O\to E\) | `PARENT IDT 05J` |
| exact event clock \(t_E\) | `PARENT IDT 05H` |
| spatial vertex carrier \(V(\Sigma)\) | `PARENT TIR GSC-1` |
| quotient-fibre constancy iff unique descent \(\bar a:E\to V(\Sigma)\) | `EXACT SET-THEORETIC QUOTIENT FACTORIZATION` |
| \(\iota(e)=(t_E(e)+C,\bar a(e))\) on supplied binding sector | `EXACT CONDITIONAL CONSTRUCTION` |
| source-owned terminal-state ↔ TIR-vertex binding | `OPEN INPUT` |
| production occurrence/state table and event quotient | `OPEN INPUT` |
| executable relational placement certifier | `PASS TARGET` |

## 8. Validation authority

Implementation:

`src/rfc/relational_event_placement_binding.py`

Reference tests:

`tests/reference/test_rfgsc3b_relational_event_placement_binding.py`

Static receipt:

`validation/RFC_GSC3B_RELATIONAL_EVENT_PLACEMENT_V0_1.json`

Dedicated workflow:

`.github/workflows/rfc-gsc3b-relational-event-placement.yml`

Verdict target:

`PASS_RFC_GSC3B_QUOTIENT_DESCENDED_EVENT_PLACEMENT_WITH_PRODUCTION_RELATIONAL_BINDING_OPEN`.
