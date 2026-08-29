# RF-E11 — Matter Projection and Source Typing

Status: `EXACT_TENSOR_DECOMPOSITION_CANDIDATE / PRE_EINSTEIN_SOURCE_BINDING_GATE`

## 1. Parent surfaces

RF-E7 supplies an admitted symmetric Lorentzian matter tensor `T_{mu nu}` for the current RFC matter composition.

RF-E8--RF-E10 supply a spacelike foliation with

\[
n_\mu n^\mu=-1,
\qquad
h_{\mu\nu}=g_{\mu\nu}+n_\mu n_\nu,
\]

and spatial projector

\[
\boxed{h_\mu{}^\nu=\delta_\mu{}^\nu+n_\mu n^\nu.}
\]

RF-E11 asks only how an already-admitted `T_{mu nu}` decomposes relative to this foliation.

## 2. Energy-density projection

Define

\[
\boxed{
\rho_n:=T_{\mu\nu}n^\mu n^\nu.
}
\]

This is a scalar under spatial frame changes on the slice.

## 3. Momentum-density projection

Define the spatial momentum covector

\[
\boxed{
j_\mu:=-h_\mu{}^\alpha T_{\alpha\beta}n^\beta.}
\]

It is spatial because

\[
\boxed{n^\mu j_\mu=0.}
\]

Its slice components are

\[
\boxed{j_i=-h_i{}^\mu n^\nu T_{\mu\nu}.}
\]

This sign is chosen to match the geometric momentum carrier fixed in RF-E10:

\[
\mathcal G_{Mi}
=-h_i{}^\mu n^\nu G_{\mu\nu}.
\]

The two sides now have identical projection orientation without yet imposing a dynamical relation between them.

## 4. Spatial stress projection

Define

\[
\boxed{
S_{\mu\nu}
:=h_\mu{}^\alpha h_\nu{}^\beta T_{\alpha\beta}.
}
\]

Then

\[
\boxed{n^\mu S_{\mu\nu}=0,}
\]

and the spatial stress trace is

\[
\boxed{S:=h^{\mu\nu}S_{\mu\nu}=h^{ij}S_{ij}.}
\]

## 5. Exact reconstruction theorem

Using the completeness relation

\[
\delta_\mu{}^\alpha
=h_\mu{}^\alpha-n_\mu n^\alpha,
\]

insert one copy on each index of `T_{alpha beta}`. The four terms give exactly

\[
\boxed{
T_{\mu\nu}
=\rho_n n_\mu n_\nu
+n_\mu j_\nu
+j_\mu n_\nu
+S_{\mu\nu}.
}
\]

Thus the foliation projections contain the complete symmetric matter tensor.

## 6. Trace identity

Contracting with

\[
g^{\mu\nu}=h^{\mu\nu}-n^\mu n^\nu
\]

gives

\[
\boxed{
T:=g^{\mu\nu}T_{\mu\nu}
=-\rho_n+S.
}
\]

The momentum terms vanish under the trace because `j_mu` is spatial.

## 7. Orthogonal-frame certificate

In a local orthonormal frame adapted to the foliation,

\[
n^\mu=(1,0,0,0),
\qquad
n_\mu=(-1,0,0,0),
\]

so

\[
\boxed{
T_{00}=\rho_n,
\qquad
T_{0i}=-j_i,
\qquad
T_{ij}=S_{ij}.
}
\]

This fixes the coordinate sign convention used by the tests and the future source-constraint crosswalk.

## 8. RFC matter-spine crosswalk

For each already-admitted RFC matter contribution,

```text
T_mn^EM
T_mn^scalar
T_mn^kin
...
```

projection is linear:

\[
\boxed{
\rho_n[T^{(1)}+T^{(2)}]
=\rho_n[T^{(1)}]+\rho_n[T^{(2)}],
}
\]

with identical linearity for `j_i` and `S_ij`.

Therefore the existing RFC stress-energy composition may be projected sector by sector and recomposed without changing the source bookkeeping hierarchy.

## 9. Einstein-source firewall

RF-E10 supplies geometric carriers

\[
\mathcal G_H
={} ^{(3)}R+K^2-K_{ij}K^{ij}
=2G_{nn},
\]

\[
\mathcal G_{Mi}
=D_jK^j{}_i-D_iK
=-G_{ni}.
\]

RF-E11 supplies matter carriers

\[
\rho_n,
\qquad
j_i.
\]

The present gate records the typed parallel structure

```text
GEOMETRY                       MATTER
G_H = 2 G_nn                  rho_n = T_nn
G_Mi = -G_ni                  j_i   = -T_ni
```

and stops there.

A later dynamical gate must derive or otherwise source-bind the proportionality operator that relates the two columns. Only after that gate may the projected equations be promoted as Hamiltonian/momentum source constraints.

## 10. Claim ledger

| Statement | Status |
|---|---|
| `rho_n=T_nn` projection | DEFINITION |
| `j_mu=-h_mu^a T_ab n^b` | DEFINITION |
| `S_mn=h_m^a h_n^b T_ab` | DEFINITION |
| spatiality of `j` and `S` | EXACT PROJECTOR ALGEBRA |
| reconstruction of `T_mn` | EXACT |
| trace `T=-rho_n+S` | EXACT |
| linearity across RFC matter sectors | EXACT |
| alignment with RF-E10 projection signs | EXACT TYPING CROSSWALK |
| geometry-to-matter proportionality | NEXT DYNAMICAL GATE |
| Hamiltonian/momentum source equations | DOWNSTREAM GATE |

Validation target:

`PASS_RF_E11_MATTER_PROJECTION_SOURCE_TYPING`.
