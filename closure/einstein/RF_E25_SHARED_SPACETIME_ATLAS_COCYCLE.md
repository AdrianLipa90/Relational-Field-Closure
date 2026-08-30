# RF-E25 — Shared Spacetime Atlas and Lorentz-Coframe Cocycle Certificate

Status: `SHARED_SPACETIME_ATLAS_CERTIFIER / EXACT_OVERLAP_GATE / PRODUCTION_SHARED_ATLAS_OPEN_INPUT`

Date: 2026-08-30

## 1. Purpose

RF-E24 closes the local Einstein field-equation form on the admitted local geometric and source-selection premises. TIR A5 supplies a combinatorial 3-manifold/smooth-realization certifier, while IDT 05H and 05G supply the discrete global-clock exactness criterion and the positive-lapse Frobenius foliation gate.

RF-E25 owns the remaining atlas compatibility question: whether admitted spatial and temporal local data glue as one time-oriented Lorentzian four-dimensional carrier.

The input is a finite collection of ADM-adapted local patches and overlap maps. The output is a fail-closed compatibility certificate.

## 2. Local ADM coframe

On patch `p`, RF-E8 supplies

\[
\vartheta_p^0=N_p\,dx_p^0,
\qquad N_p>0,
\]

and

\[
\vartheta_p^a=e^a{}_{i,p}
\left(dx_p^i+b_p^i dx_p^0\right),
\qquad a,i=1,2,3.
\]

Write

\[
\vartheta_p^A=E_p{}^A{}_{\mu}\,dx_p^\mu.
\]

In matrix form,

\[
E_p=
\begin{pmatrix}
N_p&0\\
e_pb_p&e_p
\end{pmatrix}.
\]

Hence

\[
\boxed{\det E_p=N_p\det e_p.}
\]

For positive lapse and invertible spatial triad,

\[
\boxed{\det E_p\neq0,}
\]

so the assembled coframe has rank four.

With

\[
\eta=\operatorname{diag}(-1,1,1,1),
\]

the local metric is

\[
\boxed{g_p=E_p^T\eta E_p.}
\]

## 3. Shared clock-adapted overlap

For an overlap from patch `p` to patch `q`, define the coordinate Jacobian by

\[
\boxed{dx_q=J_{q\leftarrow p}\,dx_p.}
\]

IDT 05H supplies one exact scalar event clock on a certified event complex, and 05G uses its regular smooth extension as the foliation scalar. In a shared time-adapted atlas the same scalar clock differential is used on every overlap:

\[
\boxed{dx_q^0=dx_p^0.}
\]

Therefore the first row of the overlap Jacobian obeys

\[
\boxed{(J_{q\leftarrow p})^0{}_{\mu}=(1,0,0,0).}
\]

Spatial coordinates may retain time-dependent relabeling through the lower-left Jacobian block.

For the oriented TIR spatial sector joined to the IDT time orientation, RF-E25 selects orientation-preserving coordinate overlaps,

\[
\boxed{\det J_{q\leftarrow p}>0.}
\]

## 4. Lorentz coframe transition

Let the local orthonormal coframes be related by

\[
\boxed{\vartheta_q=\Lambda_{q\leftarrow p}\vartheta_p.}
\]

The frame transition must preserve the Lorentz metric,

\[
\boxed{\Lambda^T\eta\Lambda=\eta,}
\]

and the time-oriented, proper sector is selected by

\[
\boxed{\det\Lambda=+1,\qquad \Lambda^0{}_0\ge1.}
\]

Combining coordinate and frame transformations gives the central overlap equation

\[
\boxed{
E_qJ_{q\leftarrow p}
=\Lambda_{q\leftarrow p}E_p.
}
\]

This equation is the executable TIR × IDT × RFC gluing condition in the ADM time gauge.

## 5. Metric gluing theorem

Using

\[
g_p=E_p^T\eta E_p,
\qquad
g_q=E_q^T\eta E_q,
\]

and the overlap equation,

\[
E_qJ=\Lambda E_p,
\]

one obtains

\[
\begin{aligned}
J^Tg_qJ
&=(E_qJ)^T\eta(E_qJ)\\
&=(\Lambda E_p)^T\eta(\Lambda E_p)\\
&=E_p^T\Lambda^T\eta\Lambda E_p\\
&=E_p^T\eta E_p.
\end{aligned}
\]

Therefore

\[
\boxed{J^Tg_qJ=g_p.}
\]

The local Lorentzian metrics consequently define one metric tensor across every certified overlap.

## 6. Triple-overlap cocycle

For three patches `p,q,r` with direct overlaps, coordinate consistency requires

\[
\boxed{
J_{r\leftarrow p}
=J_{r\leftarrow q}J_{q\leftarrow p}.
}
\]

Frame consistency requires

\[
\boxed{
\Lambda_{r\leftarrow p}
=\Lambda_{r\leftarrow q}\Lambda_{q\leftarrow p}.
}
\]

These are the atlas and orthonormal-frame cocycle conditions. Together with connected overlap incidence they certify one joined time-oriented Lorentzian atlas on the supplied patch system.

## 7. Cross-repository dependency line

The typed handoff is

```text
TIR A5 certified spatial 3-manifold realization input
 + IDT 05H exact event clock
 + IDT 05G regular smooth clock / positive lapse
 + RFC RF-E8 local ADM coframes
 -> RF-E25 overlap equation
 -> Lorentz metric invariance
 -> time/orientation preservation
 -> coordinate + frame triple cocycles
 -> shared Lorentzian metric atlas on the supplied realization
 -> RF-E24 local Einstein form on that assembled domain
```

The FPDG cross-repository coordinate corresponding to this gate is `GSC-4`.

## 8. Production promotion contract

Reference validation exercises exact positive and negative controls for the algebraic atlas certificate.

Production promotion requires the actual shared TIR × IDT × RFC patch realization, including:

- patchwise positive lapses;
- patchwise invertible spatial triads and shifts;
- overlap incidence;
- coordinate Jacobians;
- orthonormal-frame transition matrices;
- declared triple overlaps.

The current production status is

`PRODUCTION_SHARED_ATLAS_OPEN_INPUT`.

A production PASS promotes `GSC-4` to a certified shared spacetime realization and supplies the global carrier required by FPDG `GSC-5`.

## 9. Falsification gates

The reference certifier fails closed on any of the following:

1. non-positive/non-finite lapse;
2. singular spatial triad;
3. singular or orientation-reversing overlap Jacobian;
4. overlap mixing of the shared scalar clock differential into spatial differentials;
5. failure of Lorentz metric preservation;
6. improper or time-reversing frame transition;
7. failure of `E_q J = Lambda E_p`;
8. failure of metric pullback `J^T g_q J = g_p`;
9. disconnected declared patch atlas;
10. failure of coordinate or frame cocycle on a declared triple overlap.

## 10. Validation authority

Reference implementation:

`src/rfc/shared_spacetime_atlas.py`

Reference tests:

`tests/reference/test_rfe25_shared_spacetime_atlas.py`

Static receipt:

`validation/RFE25_SHARED_SPACETIME_ATLAS_COCYCLE_V0_1.json`

Target verdict:

`PASS_RFE25_SHARED_SPACETIME_ATLAS_CERTIFIER_WITH_PRODUCTION_INPUT_OPEN`.
