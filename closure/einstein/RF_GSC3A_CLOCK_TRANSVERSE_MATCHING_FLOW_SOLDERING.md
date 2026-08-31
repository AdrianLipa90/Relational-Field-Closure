# RF-GSC3A — Clock-Transverse Matching-Flow Soldering

Status: `EXACT_CLOCK_TRANSVERSE_MATCHING_FIELD / EXACT_INTERVAL_COMPLETE_FLOW_PRODUCT_TRIVIALIZATION / EXECUTABLE_OVERLAP_AND_EVENT_ANCHOR_CERTIFIER / GLOBAL_FLOW_COVERAGE_OPEN / PHYSICAL_EVENT_PLACEMENT_OPEN / RF_E25_METRIC_PROMOTION_DOWNSTREAM`

Date: 2026-08-31

## 1. Purpose

RF-GSC3 gives the exact product-clock construction

\[
M=I\times\Sigma,
\qquad t=\operatorname{pr}_I,
\]

as a sufficient continuum realization between TIR A5, IDT 05H/05G and RF-E25.

RF-GSC3A resolves the preceding realization seam. The input is a regular shared clock together with the TIR/RFC inter-leaf matching field. The output theorem shows when that field generates a global product trivialization by flow.

The resulting dependency line is

```text
TIR A5 smooth connected spatial leaf Sigma
+ IDT regular shared clock t
+ TIR/RFC inter-leaf matching field
-> RF-GSC3A global clock-transverse vector field
-> interval-complete matching flow
-> M ≅ I x Sigma_t0
-> RF-GSC3 product-clock representation
-> RF-E25 Lorentz/coframe promotion
```

## 2. Clock-transverse matching vector

On one RF-E25 time-adapted patch, write the spatial coframe as

\[
\boxed{
\vartheta^a=e^a{}_i\left(dx^i+b^i dt\right).
}
\]

Define

\[
\boxed{
X=\partial_t-b^i\partial_i.
}
\]

Then

\[
\boxed{dt(X)=1}
\]

and

\[
\boxed{
\vartheta^a(X)
=e^a{}_i\bigl(dx^i(X)+b^i dt(X)\bigr)
=e^a{}_i(-b^i+b^i)=0.
}
\]

Thus `X` is exactly clock-transverse and annihilates the spatial coframe. With the RF-E25 temporal coframe

\[
\vartheta^0=Ndt,
\qquad N>0,
\]

one also has

\[
\boxed{\vartheta^0(X)=N.}
\]

The unit-normal scaling used downstream is therefore obtained from the same matching direction by the admitted lapse normalization.

## 3. Shared-clock overlap law

Let two time-adapted coordinate systems obey

\[
\boxed{t_q=t_p=t}
\]

and

\[
\boxed{x_q=f_{qp}(t,x_p).}
\]

Define

\[
A_{qp}=D_xf_{qp},
\qquad
v_{qp}=\partial_t f_{qp}.
\]

The coordinate vector transforms as

\[
\partial_t\big|_p
=
\partial_t\big|_q
+v_{qp}^j\partial_{x_q^j},
\]

while

\[
\partial_{x_p^i}
=(A_{qp})^j{}_i\partial_{x_q^j}.
\]

Hence

\[
X_p
=
\partial_t\big|_q
+\left(v_{qp}-A_{qp}b_p\right)^j\partial_{x_q^j}.
\]

Equality with

\[
X_q=\partial_t\big|_q-b_q^j\partial_{x_q^j}
\]

is equivalent to the exact overlap law

\[
\boxed{b_q=A_{qp}b_p-v_{qp}.}
\]

This is the premetric soldering condition for the TIR/RFC matching field.

## 4. Triple-overlap compatibility

For

\[
p\to q\to r,
\]

the shared-clock coordinate cocycle gives

\[
\boxed{A_{rp}=A_{rq}A_{qp}}
\]

and

\[
\boxed{v_{rp}=v_{rq}+A_{rq}v_{qp}.}
\]

Applying the matching-field law twice,

\[
\begin{aligned}
b_r
&=A_{rq}b_q-v_{rq}\\
&=A_{rq}(A_{qp}b_p-v_{qp})-v_{rq}\\
&=A_{rp}b_p-v_{rp}.
\end{aligned}
\]

Therefore the local fields glue to one global smooth vector field `X` whenever the declared first-order coordinate cocycle and the pairwise matching-field law hold.

## 5. Interval-complete flow theorem

Let

\[
t:M\to I\subset\mathbb R
\]

be the admitted smooth regular clock and let `X` be the global smooth matching field satisfying

\[
\boxed{dt(X)=1.}
\]

Fix

\[
t_0\in I,
\qquad
\Sigma_{t_0}=t^{-1}(t_0).
\]

Let `Phi_s` denote the maximal flow of `X`. Assume interval-complete coverage in the following precise sense:

1. for every `p in Sigma_{t0}` and every `tau in I`, `Phi_{tau-t0}(p)` exists;
2. for every `m in M`, `Phi_{t0-t(m)}(m)` exists.

Along every flow line,

\[
\frac{d}{ds}t(\Phi_s(m))
=dt_{\Phi_s(m)}(X)=1.
\]

Hence

\[
\boxed{t(\Phi_s(m))=t(m)+s.}
\]

Define

\[
\boxed{
F:I\times\Sigma_{t_0}\to M,
\qquad
F(\tau,p)=\Phi_{\tau-t_0}(p).
}
\]

Then

\[
\boxed{t(F(\tau,p))=\tau.}
\]

Define the inverse candidate

\[
\boxed{
G(m)=\left(t(m),\Phi_{t_0-t(m)}(m)\right).
}
\]

The second component lies in `Sigma_{t0}` because

\[
t\!\left(\Phi_{t_0-t(m)}(m)\right)=t_0.
\]

The flow composition law gives

\[
G\circ F=\operatorname{id}_{I\times\Sigma_{t_0}}
\]

and

\[
F\circ G=\operatorname{id}_M.
\]

Smooth dependence of the flow on initial data and flow parameter gives smoothness of both maps. Therefore

\[
\boxed{M\cong I\times\Sigma_{t_0}.}
\]

This theorem converts the RF-GSC3 product representation from a supplied realization into a derived consequence of the regular clock plus interval-complete matching flow.

## 6. Event-clock anchoring

Let IDT 05H reconstruct the exact event-clock potentials

\[
t_v.
\]

For a production event realization

\[
\eta:V(K_1)\to M,
\]

the temporal binding condition is one additive calibration constant

\[
\boxed{t(\eta(v))-t_v=C}
\]

for every admitted event.

After the flow trivialization,

\[
F^{-1}(\eta(v))
=
\boxed{(t_v+C,p_v)}
\]

for a spatial placement

\[
p_v\in\Sigma_{t_0}.
\]

Thus 05H owns temporal event separation, while the production realization supplies the spatial placement coordinate.

## 7. Edge realization lemma

Let `u -> v` be an admitted 05H edge with

\[
\theta_{uv}=t_v-t_u>0.
\]

For connected smooth `Sigma`, select a piecewise-smooth spatial path

\[
\sigma_{uv}:[0,1]\to\Sigma
\]

joining the corresponding spatial placements. In product coordinates define

\[
\Gamma_{uv}(s)
=
\left((1-s)(t_u+C)+s(t_v+C),\sigma_{uv}(s)\right).
\]

Then

\[
\boxed{
\frac{d}{ds}(t\circ\Gamma_{uv})
=t_v-t_u
=\theta_{uv}>0.
}
\]

The temporal orientation of the realized edge is therefore inherited directly from the exact 05H clock.

## 8. Relation to TIR beta_match and RF-E25 shift

The TIR spatial-temporal closure interface already exports an inter-leaf matching vector `beta_match`. RF-E25 uses the ADM shift `b` in its spatial coframe. RF-GSC3A supplies their precise shared-clock transformation rule:

\[
\boxed{\beta_{\rm match}\equiv b}
\]

at the interface convention together with

\[
\boxed{b_q=A_{qp}b_p-v_{qp}.}
\]

A source-owned binding receipt is required when project surfaces use distinct identifiers for these two representations.

## 9. Executable certifier

The reference implementation checks the finite algebraic layer:

- finite 3-vector matching fields on every declared patch;
- shared-clock first-order overlap data `(A,v)`;
- exact matching-field law `b_q=A b_p-v` within tolerance;
- connected patch incidence for a connected-domain claim;
- declared triple-overlap Jacobian and time-drift cocycles;
- exact pairings `dt(X)=1` and `(dx^i+b^i dt)(X)=0`;
- one additive calibration across supplied 05H event-clock anchors.

Reference implementation:

`src/rfc/clock_transverse_matching_flow.py`

Reference tests:

`tests/reference/test_clock_transverse_matching_flow.py`

The analytic production coordinate remains

`GLOBAL_INTERVAL_COMPLETE_FLOW_COVERAGE_OPEN_INPUT`.

The event-realization coordinate remains

`PHYSICAL_EVENT_PLACEMENT_OPEN_INPUT`.

## 10. Claim ledger

| Claim | Status |
|---|---|
| `X=partial_t-b^i partial_i` has `dt(X)=1` | `EXACT` |
| spatial ADM coframe annihilates `X` | `EXACT` |
| matching-field overlap law `b_q=A b_p-v` | `EXACT` |
| triple-overlap compatibility of the matching field | `EXACT` |
| interval-complete matching flow yields `M ≅ I x Sigma_t0` | `EXACT CONDITIONAL THEOREM` |
| 05H event anchors require one additive clock calibration | `EXACT` |
| connected spatial leaf supplies piecewise-smooth edge paths | `STANDARD MANIFOLD RESULT` |
| executable algebraic/event-anchor certifier | `PASS TARGET` |
| global matching-flow coverage on the production domain | `OPEN ANALYTIC INPUT` |
| production event placement | `OPEN PRODUCTION INPUT` |
| RF-E25 Lorentz metric/coframe promotion | `DOWNSTREAM PRODUCTION GATE` |

## 11. GREMLIN × Terminal36D × PhaseNav audit boundary

The live NOEMA runtime audit for this candidate traversed

```text
/dev/shm/ciel_noema
 -> GREMLIN whisper bus
 -> Terminal36D
 -> PhaseNav 36D trace
 -> GREMLIN fused receipt
```

with candidate authority only. The runtime evidence is stored separately under

`validation/gremlin/GSC3A_GREMLIN_PHASENAV_TERMINAL36D_AUDIT_V0_1.json`.

Deterministic theorem tests and hosted RFC reference-suite validation remain the promotion evidence for the executable layer.
