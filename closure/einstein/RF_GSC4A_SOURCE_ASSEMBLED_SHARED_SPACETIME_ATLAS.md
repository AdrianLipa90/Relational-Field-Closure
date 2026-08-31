# RF-GSC4A — Source-Assembled Shared Spacetime Atlas

Status: `EXACT_SOURCE_ASSEMBLY_THEOREM / RF_E25_J_AND_LORENTZ_TRANSITIONS_DERIVED / EXECUTABLE_REUSE_OF_RF_E25 / PRODUCTION_SOURCE_PACKET_OPEN`

Date: 2026-08-31

## 1. Purpose

RF-E25 certifies a supplied shared time-oriented Lorentzian atlas from ADM patch data, coordinate Jacobians and Lorentz-frame transitions. The TIR/IDT/GSC3 chain already supplies enough typed structure to construct a sufficient subclass of those RF-E25 inputs.

RF-GSC4A assembles the RF-E25 overlap packet from:

- a shared IDT clock and overlap-consistent positive lapse;
- TIR spatial orthonormal coframes and their oriented spatial overlap cocycle;
- the GSC3A matching-field shift cocycle;
- the shared time-dependent spatial coordinate relabeling.

The existing RF-E25 certifier remains the downstream validation authority.

## 2. Source patch data

On a patch `p`, let

\[
N_p>0
\]

be the shared-clock lapse, let

\[
e_p
\]

be the invertible TIR spatial triad/coframe component matrix, and let

\[
b_p
\]

be the matching-flow shift in one common temporal-coordinate convention.

As in RF-E25, assemble

\[
\boxed{
E_p=
\begin{pmatrix}
N_p&0\\
e_pb_p&e_p
\end{pmatrix}.
}
\]

## 3. Source overlap data

For an overlap `p -> q`, let the shared clock be fixed and the spatial coordinates transform by

\[
\boxed{
dx_q=A_{qp}\,dx_p+v_{qp}\,dt.}
\]

Thus the four-dimensional coordinate Jacobian is constructed as

\[
\boxed{
J_{q\leftarrow p}
=
\begin{pmatrix}
1&0\\
v_{qp}&A_{qp}
\end{pmatrix}.
}
\]

The oriented TIR spatial coframe cocycle is supplied in component form by

\[
\boxed{e_qA_{qp}=R_{qp}e_p,}
\qquad
R_{qp}\in SO(3).
\]

The GSC3A matching law is

\[
\boxed{b_q=A_{qp}b_p-v_{qp}.}
\]

The shared lapse is a scalar on the overlap:

\[
\boxed{N_q=N_p.}
\]

Define the Lorentz-frame transition directly from the TIR spatial rotation,

\[
\boxed{
\Lambda_{q\leftarrow p}
=
\operatorname{diag}(1,R_{qp}).
}
\]

## 4. Exact coframe assembly theorem

Multiplying the assembled target coframe by the constructed coordinate Jacobian gives

\[
E_qJ_{q\leftarrow p}
=
\begin{pmatrix}
N_q&0\\
e_qb_q&e_q
\end{pmatrix}
\begin{pmatrix}
1&0\\
v&A
\end{pmatrix}.
\]

Therefore

\[
E_qJ
=
\begin{pmatrix}
N_q&0\\
e_q(b_q+v)&e_qA
\end{pmatrix}.
\]

Using

\[
N_q=N_p,
\qquad
b_q+v=Ab_p,
\qquad
e_qA=Re_p,
\]

one obtains

\[
\begin{aligned}
E_qJ
&=
\begin{pmatrix}
N_p&0\\
Re_pb_p&Re_p
\end{pmatrix}\\
&=
\begin{pmatrix}
1&0\\0&R
\end{pmatrix}
\begin{pmatrix}
N_p&0\\e_pb_p&e_p
\end{pmatrix}.
\end{aligned}
\]

Hence

\[
\boxed{
E_qJ_{q\leftarrow p}
=\Lambda_{q\leftarrow p}E_p.
}
\]

This is exactly the central RF-E25 overlap equation.

## 5. Lorentz and orientation properties

With

\[
\eta=\operatorname{diag}(-1,1,1,1)
\]

and `R in SO(3)`, the constructed transition obeys

\[
\boxed{
\Lambda^T\eta\Lambda=\eta,
}
\]

\[
\boxed{
\det\Lambda=1,
\qquad
\Lambda^0{}_0=1.
}
\]

Therefore the transition lies in the proper, time-oriented Lorentz sector selected by RF-E25.

For the coordinate transition,

\[
\boxed{
\det J=\det A.
}
\]

An oriented spatial overlap with `det A>0` therefore gives an oriented four-dimensional overlap.

## 6. Metric pullback follows from the assembly

RF-E25 defines

\[
g_p=E_p^T\eta E_p,
\qquad
g_q=E_q^T\eta E_q.
\]

Using the source-assembled overlap equation and Lorentz preservation,

\[
\boxed{
J^Tg_qJ=g_p.
}
\]

Thus the metric pullback condition is inherited from the source cocycles rather than supplied as an additional independent datum.

## 7. Triple-overlap inheritance

Suppose the spatial coordinate data satisfy

\[
A_{rp}=A_{rq}A_{qp},
\]

\[
v_{rp}=v_{rq}+A_{rq}v_{qp},
\]

and the TIR spatial rotations satisfy

\[
R_{rp}=R_{rq}R_{qp}.
\]

Then the constructed four-dimensional objects obey

\[
\boxed{
J_{r\leftarrow p}
=J_{r\leftarrow q}J_{q\leftarrow p},
}
\]

and

\[
\boxed{
\Lambda_{r\leftarrow p}
=\Lambda_{r\leftarrow q}\Lambda_{q\leftarrow p}.
}
\]

The GSC3A shift law is compatible with the same coordinate cocycle, so the patchwise matching field also transports consistently across the triangle.

## 8. Reduction of the RF-E25 production surface

On this source-assembled subclass, the following RF-E25 fields are derived:

```text
full 4x4 coordinate Jacobian J  <-  spatial A + temporal drift v
full Lorentz transition Lambda  <-  TIR spatial R
full ADM coframe E               <-  IDT lapse N + TIR triad e + GSC3 shift b
metric g                         <-  E^T eta E
metric pullback                  <-  E_q J = Lambda E_p
```

The production source packet is therefore reduced to:

```text
TIR spatial patch/coframe data e
TIR spatial overlap A,R and their cocycle
IDT shared clock and lapse N
GSC3 matching shift b and drift v
source-owned patch/clock identifiers
coverage / overlap incidence
```

RF-E25 then certifies the constructed packet using its existing implementation.

## 9. Executable implementation

Reference constructor:

`src/rfc/source_assembled_shared_spacetime_atlas.py`

It validates the source relations, constructs `ADMPatch` and `AtlasOverlap` objects, and delegates the final atlas verdict to

`certify_shared_spacetime_atlas`.

Reference tests:

`tests/reference/test_gsc4a_source_assembled_shared_spacetime_atlas.py`

## 10. Claim ledger

| Claim | Status |
|---|---|
| `J=[[1,0],[v,A]]` from shared-clock spatial relabeling | `EXACT CONSTRUCTION` |
| `Lambda=diag(1,R)` from `R in SO(3)` | `EXACT CONSTRUCTION` |
| `E_q J = Lambda E_p` from lapse/coframe/shift source laws | `EXACT` |
| `Lambda^T eta Lambda=eta`, `det Lambda=1`, `Lambda00=1` | `EXACT` |
| `det J=det A` | `EXACT` |
| RF-E25 metric pullback inherited from source assembly | `EXACT` |
| coordinate and Lorentz triple cocycles inherited from source cocycles | `EXACT` |
| existing RF-E25 executable certifier | `REUSED` |
| production TIR/IDT/matching source packet and overlap coverage | `OPEN PRODUCTION INPUT` |

## 11. Validation boundary

RF-GSC4A is a sufficient source-assembled subclass of RF-E25. Production promotion requires the actual source-owned TIR spatial patch/coframe packet, IDT clock/lapse packet, matching-flow data and overlap coverage on one common realization.

GREMLIN, PhaseNav and Terminal36D provide `CANDIDATE_ONLY` dependency audit. Hosted deterministic validation and RF-E25 remain the executable evidence path.
