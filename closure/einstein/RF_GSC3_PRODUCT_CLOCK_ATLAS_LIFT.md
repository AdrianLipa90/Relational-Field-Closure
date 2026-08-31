# RF-GSC3 — Product Clock Atlas Lift

Status: `EXACT_PRODUCT_MANIFOLD_AND_SHARED_CLOCK_THEOREM / EXECUTABLE_COORDINATE_CERTIFIER / PHYSICAL_PRODUCT_REALIZATION_OPEN / RF_E25_ADM_COFRAME_BINDING_OPEN`

Date: 2026-08-31

## 1. Purpose

TIR Gate A5 supplies the typed route to a smooth oriented spatial three-manifold

\[
\Sigma^3.
\]

IDT Gate 05H supplies, on a certified connected production event complex, one exact scalar event clock up to a common additive constant.

RF-GSC3 records a sufficient global continuum construction joining these two carrier types before RF-E25:

\[
\boxed{M=I\times\Sigma}
\]

for an admitted open interval \(I\subset\mathbb R\), with global clock

\[
\boxed{t=\operatorname{pr}_I:M\to I.}
\]

The theorem owns the product-manifold and shared-clock coordinate structure. Physical identification of the admitted TIR × IDT carrier with this product remains an explicit binding gate. RF-E25 continues to own the ADM coframe and Lorentz-frame compatibility data.

## 2. Dimension and smooth product theorem

If \(\Sigma\) is a smooth three-manifold and \(I\) is a smooth one-manifold interval, the standard product-manifold construction gives

\[
\boxed{\dim(I\times\Sigma)=1+3=4.}
\]

For every spatial chart

\[
x_A:U_A\to\mathbb R^3,
\]

define the product chart

\[
\widetilde x_A:I\times U_A\to\mathbb R^4,
\qquad
\widetilde x_A(t,p)=(t,x_A(p)).
\]

Thus A5 spatial smoothness plus one admitted interval carrier gives a smooth four-dimensional product carrier by a standard differential-topology construction.

## 3. Global regular clock

The projection clock satisfies

\[
\boxed{t(s,p)=s.}
\]

Its differential obeys

\[
dt(\partial_t)=1,
\]

hence

\[
\boxed{dt\neq0}
\]

everywhere on \(I\times\Sigma\).

Therefore the product construction supplies the regular scalar-clock input consumed by IDT 05G.

This route is complementary to IDT 05I. Gate 05I certifies a supplied general affine-atlas clock witness. RF-GSC3 gives a narrower sufficient construction whenever the global carrier is admitted in product form.

## 4. Time-dependent spatial relabeling

RF-E25 permits a common scalar clock together with time-dependent spatial coordinates. Let a spatial overlap be

\[
\boxed{x_B=f_{BA}(t,x_A)}
\]

with orientation-preserving spatial derivative

\[
A_{BA}:=D_x f_{BA},
\qquad
\det A_{BA}>0.
\]

Write

\[
v_{BA}:=\partial_t f_{BA}.
\]

Since the shared clock is unchanged,

\[
t_B=t_A,
\]

the spacetime Jacobian is

\[
\boxed{
J_{B\leftarrow A}
=
\begin{pmatrix}
1 & 0\\
v_{BA} & A_{BA}
\end{pmatrix}.
}
\]

Its first row is exactly

\[
\boxed{(1,0,0,0),}
\]

which is the RF-E25 shared-clock condition.

Block triangularity gives

\[
\boxed{
\det J_{B\leftarrow A}=\det A_{BA}>0.
}
\]

Hence orientation of the product atlas is inherited directly from the oriented spatial atlas.

## 5. Triple-overlap cocycle

For spatial transitions

\[
x_Q=f_{QP}(t,x_P),
\qquad
x_R=f_{RQ}(t,x_Q),
\]

the composed first-order data are

\[
\boxed{A_{RP}=A_{RQ}A_{QP}}
\]

and

\[
\boxed{v_{RP}=v_{RQ}+A_{RQ}v_{QP}.}
\]

Therefore

\[
J_{R\leftarrow P}
=J_{R\leftarrow Q}J_{Q\leftarrow P}
\]

exactly when these two spatial first-order cocycle equations hold.

The executable certifier checks these identities on every declared triple overlap.

## 6. Event-clock anchoring

Let 05H reconstruct potentials

\[
t_v
\]

on the production event graph. For a common additive calibration \(C\), an admitted event-placement map may take the form

\[
\boxed{
iota(v)=(t_v+C,p_v),
\qquad p_v\in\Sigma.
}
\]

Then

\[
\boxed{
(\operatorname{pr}_I\circ\iota)(v)-t_v=C
}
\]

for every event automatically.

Thus, on a physically admitted product realization, the temporal interpolation part of the 05H→05G handoff is canonical. The remaining production binding is the source-owned identification of physical events with points/slices of the admitted TIR × IDT carrier.

## 7. Relation to GSC-1 through GSC-4

The candidate route is

```text
GSC-1: TIR A5 production spatial complex PASS
 + GSC-2: IDT 05H production event-clock PASS
 + physical product-realization / event-placement binding
 -> RF-GSC3 exact product-clock lift
 -> global smooth 4D carrier I x Sigma with dt != 0
 -> IDT 05G regular foliation input
 -> RF-E25 production ADM/coframe atlas compatibility
```

RF-GSC3 can therefore serve as a sufficient GSC-3 realization route. It does not replace the broader 05I affine-atlas certifier; it reduces the continuum clock construction when the product binding is independently established.

## 8. Falsification and promotion gates

The executable coordinate certifier rejects:

1. malformed or non-finite spatial Jacobian data;
2. singular spatial overlaps;
3. orientation-reversing spatial overlaps for the oriented product sector;
4. disconnected patch incidence under a connected-domain claim;
5. failure of the spatial Jacobian cocycle on a declared triple overlap;
6. failure of the time-drift cocycle on a declared triple overlap.

Production promotion additionally requires source-owned receipts for:

- GSC-1 actual spatial realization;
- GSC-2 actual event-clock exactness;
- physical product-realization/event-placement binding;
- RF-E25 ADM/coframe and Lorentz transition realization.

Reference or synthetic product charts remain validator controls.

## 9. Claim ledger

| Claim | Status |
|---|---|
| smooth \(I\times\Sigma^3\) has dimension four | `STANDARD PRODUCT-MANIFOLD THEOREM` |
| \(t=\operatorname{pr}_I\) is globally smooth | `EXACT` |
| \(dt(\partial_t)=1\), hence \(dt\neq0\) | `EXACT` |
| shared-clock overlap first row is \((1,0,0,0)\) | `EXACT` |
| \(\det J=\det D_xf\) | `EXACT` |
| triple-overlap block cocycle identities | `EXACT` |
| executable product-clock coordinate certifier | `PASS TARGET` |
| physical TIR × IDT product realization | `OPEN BINDING` |
| production event placement | `OPEN INPUT` |
| RF-E25 ADM/coframe compatibility | `DOWNSTREAM PRODUCTION GATE` |

## 10. Validation authority

Implementation:

`src/rfc/product_clock_atlas_lift.py`

Reference tests:

`tests/reference/test_rfgsc3_product_clock_atlas_lift.py`

Target verdict:

`PASS_RFC_GSC3_PRODUCT_CLOCK_ATLAS_LIFT_WITH_PHYSICAL_BINDING_OPEN`.
