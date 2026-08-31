# RF-GSC4B — Flow-Adapted Zero-Shift Shared-Atlas Route

Status: `EXACT_FLOW_ADAPTED_COORDINATE_THEOREM / GSC4A_ZERO_SHIFT_SPECIALIZATION / RF_E25_REUSED / PRODUCT_TRIVIALIZATION_PARENT_OPEN`

Date: 2026-08-31

## 1. Purpose

RF-GSC4A constructs a sufficient RF-E25 atlas from shared-clock patch data, TIR spatial coframes, oriented spatial overlap data and a matching shift/drift packet. RF-GSC4B records a narrower sufficient route available after the GSC3A product-trivialization parent.

Let

\[
F:I\times\Sigma\to M
\]

be the admitted GSC3A product trivialization with

\[
F_*\partial_t=X,
\qquad
t(F(\tau,p))=\tau.
\]

Choose spatial coordinates on each reference patch of \(\Sigma\), and extend them to \(I\times\Sigma\) by keeping them constant along the flow of \(X\). In these coordinates the matching shift and temporal spatial drift vanish identically.

This is a coordinate-gauge theorem. It does not assert vanishing extrinsic curvature and it does not replace the general GSC4A route.

## 2. Flow-adapted spatial coordinates

Let \(x^i_\Sigma\) be a spatial chart on \(\Sigma\). Define

\[
x^i(F(\tau,p)):=x^i_\Sigma(p).
\]

Because the coordinate is constant along each flow line,

\[
X(x^i)=0.
\]

Since the product clock satisfies

\[
X(t)=1,
\]

we obtain in the induced coordinates

\[
\boxed{X=\partial_t.}
\]

For the RF-E25/GSC4A convention

\[
X=\partial_t-b^i\partial_i,
\]

this gives

\[
\boxed{b^i=0.}
\]

## 3. Time-independent reference-spatial overlaps

If two spatial charts on the reference leaf obey

\[
x_q=f_{qp}(x_p),
\]

their flow extensions retain the same transition for every \(t\). Therefore

\[
\partial_t f_{qp}=0,
\]

so the temporal drift is

\[
\boxed{v_{qp}=0.}
\]

The four-dimensional Jacobian reduces to

\[
\boxed{
J_{q\leftarrow p}
=\begin{pmatrix}
1&0\\
0&A_{qp}
\end{pmatrix}.
}
\]

The general matching law

\[
b_q=A_{qp}b_p-v_{qp}
\]

is then satisfied identically.

## 4. RF-GSC4A specialization

The flow-adapted source packet is reduced to

```text
GSC3A admitted product-trivialization parent
TIR spatial patch/coframe data e
TIR oriented spatial overlap A,R and their cocycle
IDT shared clock/lapse N
source patch/clock identifiers
production overlap coverage
```

The independent production fields

```text
matching shift b
spatial temporal drift v
```

are absent on this sufficient coordinate route because

\[
\boxed{b=0,\qquad v=0}
\]

follow from the flow-adapted chart construction.

RF-GSC4A then gives

\[
E_p=\begin{pmatrix}N_p&0\\0&e_p\end{pmatrix},
\qquad
J=\operatorname{diag}(1,A),
\qquad
\Lambda=\operatorname{diag}(1,R),
\]

and its exact source-assembly theorem still yields

\[
\boxed{E_qJ=\Lambda E_p.}
\]

RF-E25 remains the final atlas certifier.

## 5. Coordinate-gauge firewall

The relation \(b=0\) is a statement about the coordinates transported by the admitted matching flow. A time-dependent spatial relabeling can reintroduce a nonzero shift according to

\[
\boxed{b_q=A_{qp}b_p-v_{qp}.}
\]

Hence the theorem preserves the general GSC4A/RF-E25 geometry while identifying one sufficient gauge with a smaller production packet.

The extrinsic curvature remains

\[
K_{ij}=-\frac{1}{2N}(\mathcal L_Xh)_{ij}
\]

and can be nonzero in the flow-adapted gauge through time evolution of \(h\).

## 6. Executable surface

Implementation:

`src/rfc/flow_adapted_zero_shift_atlas.py`

Reference tests:

`tests/reference/test_gsc4b_flow_adapted_zero_shift_atlas.py`

The executable gate requires an explicit admitted product-trivialization parent and then constructs the zero-shift/zero-drift specialization before delegating to RF-GSC4A and RF-E25.

## 7. Claim ledger

| Statement | Status |
|---|---|
| product-flow coordinates give `X=partial_t` | `EXACT` |
| RF-E25/GSC4A matching coefficient is `b=0` in that chart | `EXACT` |
| reference-spatial overlap extension gives `v=0` | `EXACT` |
| GSC4A source assembly remains valid with `b=v=0` | `EXACT` |
| RF-E25 final compatibility certification | `REUSED` |
| production GSC3A product-trivialization witness | `OPEN PARENT INPUT` |
| production TIR spatial coframe/overlap packet | `OPEN INPUT` |
| production IDT lapse/shared-clock packet | `OPEN INPUT` |
| production overlap coverage | `OPEN INPUT` |

## 8. Runtime audit boundary

The sufficient route was audited through the active

```text
GREMLIN -> Terminal36D -> PhaseNav36D -> GREMLIN
```

surface with `CANDIDATE_ONLY` authority. Runtime output is dependency/falsification evidence only; hosted deterministic validation remains the executable theorem surface.
