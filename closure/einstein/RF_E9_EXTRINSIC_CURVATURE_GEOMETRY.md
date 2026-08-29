# RF-E9 — Extrinsic-Curvature Geometry

Status: `EXACT_DIFFERENTIAL_GEOMETRY_CANDIDATE / PRE_CONSTRAINT_GATE`

## 1. Parent geometry

RF-E8 supplies the ADM metric in the length-valued temporal coordinate

\[
\boxed{x^0=ct}
\]

with

\[
 ds^2=-N^2(dx^0)^2+h_{ij}(dx^i+b^i dx^0)(dx^j+b^j dx^0),
\]

where

```text
N > 0       IDT lapse carrier
h_ij        positive spatial metric
b^i         typed dimensionless shift carrier
```

and future unit normal

\[
\boxed{
n^\mu=\frac1N(1,-b^i).
}
\]

## 2. Sign convention

RF-E9 fixes the extrinsic-curvature convention

\[
\boxed{
K_{ij}:=-\frac12\mathcal L_n h_{ij}.
}
\]

Equivalently,

\[
\boxed{
K_{ij}
=-\gamma_i{}^\mu\gamma_j{}^\nu\nabla_\mu n_\nu.
}
\]

For the RF-E8 ADM coordinates this becomes

\[
\boxed{
K_{ij}
=\frac1{2N}
\left(
-\partial_0 h_{ij}
+D_i b_j
+D_j b_i
\right),
}
\]

with

\[
b_i=h_{ij}b^j.
\]

No Einstein field equation enters this definition.

## 3. Dimensional firewall

Because `x^0=ct` carries length dimension,

\[
[\partial_0]=L^{-1}.
\]

For dimensionless metric components `h_ij` and dimensionless shift `b^i`,

\[
\boxed{[K_{ij}]=L^{-1}.}
\]

Thus the curvature convention is dimensionally aligned with the RF-L5A physical inverse-length sector without identifying the two quantities.

## 4. Trace and shear decomposition

Define

\[
\boxed{K=h^{ij}K_{ij}.}
\]

The trace-free part is

\[
\boxed{
A_{ij}:=K_{ij}-\frac13 h_{ij}K.
}
\]

Then exactly

\[
\boxed{h^{ij}A_{ij}=0.}
\]

The decomposition

\[
\boxed{K_{ij}=A_{ij}+\frac13h_{ij}K}
\]

separates volume expansion/contraction from trace-free shape deformation.

## 5. Static and Killing-shift controls

For

\[
\partial_0h_{ij}=0
\]

and vanishing shift,

\[
\boxed{K_{ij}=0.}
\]

More generally, if `b^i` is a Killing field of the spatial metric,

\[
D_i b_j+D_j b_i=0,
\]

and the spatial metric is time-independent, then again

\[
\boxed{K_{ij}=0.}
\]

This is an exact coordinate/control sector.

## 6. Isotropic expansion certificate

Let

\[
h_{ij}=a(x^0)^2\delta_{ij},
\qquad b^i=0.
\]

Then

\[
\partial_0h_{ij}=2aa'\delta_{ij},
\]

so

\[
\boxed{
K_{ij}=-\frac{aa'}{N}\delta_{ij}
=-\frac{a'}{aN}h_{ij}.
}
\]

The trace is

\[
\boxed{K=-\frac{3a'}{aN}.}
\]

and the shear vanishes,

\[
\boxed{A_{ij}=0.}
\]

This provides a deterministic nonzero certificate for the convention.

## 7. Source typing

RF-E9 uses:

```text
TIR spatial geometry          -> h_ij, D_i
IDT temporal carrier          -> N
RFC-E8 ADM assembly           -> n^mu, b^i
RF-E9 geometry                -> K_ij, K, A_ij
```

The GREMLIN/TIR `SE(3)` gluing branch proposes a future source binding for `b^i`. RF-E9 remains valid for any admitted typed shift while that source map is gated.

## 8. Gauss-Codazzi frontier

Once `K_ij` is available, the next step can be performed as differential geometry before any matter coupling:

```text
(h_ij, K_ij)
 -> Gauss identity
 -> Codazzi identity
 -> normal-normal Einstein-tensor projection
 -> normal-spatial Einstein-tensor projection
```

Only after these geometric projection identities are established should RFC bind the projected matter tensor and promote Hamiltonian/momentum source constraints.

## 9. Claim ledger

| Statement | Status |
|---|---|
| `K_ij = -1/2 L_n h_ij` convention | DEFINITION |
| ADM coordinate expression | EXACT DIFFERENTIAL GEOMETRY |
| `[K_ij]=L^-1` for `x0=ct` | EXACT DIMENSIONAL TYPING |
| trace/shear decomposition | EXACT ALGEBRA |
| static zero-shift control | EXACT |
| Killing-shift control | EXACT |
| isotropic expansion certificate | EXACT |
| Gauss-Codazzi identities | NEXT GEOMETRY GATE |
| ADM matter constraints | DOWNSTREAM SOURCE GATE |
| Einstein field equations | DOWNSTREAM CLOSURE GATE |

Validation target:

`PASS_RF_E9_EXTRINSIC_CURVATURE_GEOMETRY`.
