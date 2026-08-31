# RF-GSC3C — TIR `beta_match` × RFC Shift Source-Binding Firewall

Status: `EXACT_COVARIANT_FAMILY_THEOREM / EXECUTABLE_SOURCE_BINDING_CERTIFIER / PRODUCTION_SOURCE_BINDING_OPEN`

Date: 2026-08-31

## 1. Purpose

The TIR spatial-temporal closure interface exports an inter-leaf matching field `beta_match` as the coordinate-matching carrier between spatial leaves. RF-E8 independently types the ADM shift `b^i` as its gluing/coordinate carrier and records a TIR affine-gluing source as a separately gated dependency.

RF-GSC3A derives the shared-clock matching-field overlap law. RF-GSC3B PR #100 then reuses the existing RF-E8/RF-E9 shift and curvature operators under the exact temporal-coordinate scale

\[
\boxed{x^0=ct.}
\]

RF-GSC3C isolates the remaining source-owned binding coordinate and gives it an executable admission surface.

## 2. Two coordinate representations

Write the TIR matching field in coordinate time `t` as

\[
\boxed{\beta_{(t)}^i.}
\]

RF-E8 uses the dimensionless shift `b_(0)^i` against `x^0=ct`. A source binding on one realization therefore has the coordinate-scale form

\[
\boxed{\beta_{(t)}^i=c\,b_{(0)}^i.}
\]

The equality is evaluated only after the TIR and RFC records identify the same physical realization, the same scalar clock and the same spatial patch.

## 3. Shared-clock overlap laws

Let a spatial coordinate overlap be

\[
x_q=f_{qp}(t,x_p),
\]

with

\[
A_{qp}=D_xf_{qp},
\qquad
v_{(t),qp}=\partial_t f_{qp}.
\]

The TIR/GSC3A time-coordinate matching field obeys

\[
\boxed{\beta_{(t),q}=A_{qp}\beta_{(t),p}-v_{(t),qp}.}
\]

Since

\[
\partial_0 f_{qp}=c^{-1}\partial_t f_{qp},
\]

RF-E8 shift covariance reads

\[
\boxed{
b_{(0),q}=A_{qp}b_{(0),p}-c^{-1}v_{(t),qp}.}
\]

Multiplication by `c` gives

\[
\boxed{
c b_{(0),q}=A_{qp}(c b_{(0),p})-v_{(t),qp}.}
\]

Thus the two carriers belong to the same affine transformation class once the temporal-coordinate scale is fixed.

## 4. Covariant-family theorem

Define the source-binding difference field

\[
\boxed{W_p:=\beta_{(t),p}-c b_{(0),p}.}
\]

Subtracting the two affine overlap equations yields

\[
\begin{aligned}
W_q
&=\beta_{(t),q}-c b_{(0),q}\\
&=A_{qp}\beta_{(t),p}-v_{(t),qp}
 -A_{qp}(c b_{(0),p})+v_{(t),qp}\\
&=A_{qp}W_p.
\end{aligned}
\]

Therefore

\[
\boxed{W_q=A_{qp}W_p.}
\]

The common affine overlap structure admits a covariant family parameterized by an ordinary spatial vector field `W`. The source-owned identity is the distinguished section

\[
\boxed{W=0.}
\]

Equivalently,

\[
\boxed{\beta_{(t)}=c b_{(0)}}.
\]

This separates the exact geometry of the overlap class from the repository-owned identification of two independently typed carriers.

## 5. Minimal production witness

A production source-binding witness contains:

1. one common `realization_id` for the admitted TIR and RFC geometry;
2. one common scalar `clock_id`;
3. a common set of spatial patch identifiers;
4. TIR patch values `beta_(t)`;
5. RFC patch values `b_(0)`;
6. shared-clock overlap data `(A_qp, v_(t),qp)`;
7. a deterministic certificate for
   \[
   \beta_{(t),q}=A_{qp}\beta_{(t),p}-v_{(t),qp},
   \]
   \[
   b_{(0),q}=A_{qp}b_{(0),p}-c^{-1}v_{(t),qp},
   \]
   and
   \[
   \boxed{\max_p\|\beta_{(t),p}-c b_{(0),p}\|\le\varepsilon}.
   \]

The first two equations certify the shared affine geometry. The last equation certifies the source binding on the supplied realization.

## 6. Falsification control

Choose any nonzero spatial vector field `W` obeying

\[
W_q=A_{qp}W_p.
\]

Starting from an exact bound pair, define

\[
\beta'_{(t),p}=c b_{(0),p}+W_p.
\]

Then

\[
\beta'_{(t),q}=A_{qp}\beta'_{(t),p}-v_{(t),qp}
\]

and the RFC shift overlap law remains unchanged. The supplied geometry therefore remains overlap-consistent while the binding defect becomes

\[
\boxed{\beta'_{(t)}-c b_{(0)}=W.}
\]

This is the decisive negative control for the source-binding certifier.

## 7. Executable certifier

Implementation:

`src/rfc/beta_match_shift_source_binding.py`

Reference tests:

`tests/reference/test_beta_match_shift_source_binding.py`

The certifier distinguishes:

```text
OVERLAP_COVARIANCE_PASS
```

from

```text
SOURCE_BINDING_CERTIFIED_ON_SUPPLIED_REALIZATION
```

and reports the patchwise covariant field `W` together with its maximum binding defect.

A downstream gate requiring the source identity invokes a separate fail-closed `require_exact_source_binding(...)` check.

## 8. Dependency refinement

The seam is now typed as

```text
TIR beta_match interface
 + GSC3A shared-clock matching-field cocycle
 + RF-E8 x0=ct shift convention
 -> common affine transformation class
 -> RF-GSC3C W-field source-binding certifier
 -> [W=0 source receipt on supplied realization]
 -> RF-GSC3B/#100 matching-flow -> RF-E9 crosslink
 -> RF-E25 shared spacetime atlas
```

This keeps the existing RF-E8/RF-E9 operators as the RFC owners of shift and extrinsic curvature.

## 9. Claim ledger

| Statement | Status |
|---|---|
| `beta_t` and `c b_0` obey the same affine overlap law on a shared clock atlas | `EXACT CONDITIONAL ON DECLARED SOURCE OVERLAPS` |
| `W=beta_t-c b_0` transforms as `W_q=A_qp W_p` | `EXACT` |
| common affine covariance admits the `W`-parameterized family | `EXACT` |
| source binding corresponds to the `W=0` section | `EXACT DEFINITIONAL BINDING` |
| executable covariance/binding certifier | `PASS TARGET` |
| production TIR `beta_match` ↔ RFC shift identity | `OPEN SOURCE-OWNED INPUT` |
| RF-E9 kinematic crosslink | `REUSED PR #100 HOSTED-PASS GATE` |

## 10. Live GREMLIN × Terminal36D × PhaseNav boundary

The source-binding question was routed through the active NOEMA surface

```text
/dev/shm/ciel_noema
 -> GREMLIN
 -> Terminal36D
 -> PhaseNav 36D
 -> GREMLIN fused state
```

with `CANDIDATE_ONLY` authority. The runtime audit tests relational underdetermination and naming/covariance seams; deterministic source records and hosted tests remain the executable evidence.

Target verdict:

`PASS_RFC_GSC3C_COVARIANT_FAMILY_AND_SOURCE_BINDING_CERTIFIER_WITH_PRODUCTION_BINDING_OPEN`.
