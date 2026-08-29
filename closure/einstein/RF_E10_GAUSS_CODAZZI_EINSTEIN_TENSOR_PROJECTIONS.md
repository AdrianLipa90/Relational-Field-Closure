# RF-E10 — Gauss-Codazzi Einstein-Tensor Projection Identities

Status: `EXACT_DIFFERENTIAL_GEOMETRY_CANDIDATE / PRE_SOURCE_CONSTRAINT_GATE`

## 1. Parent geometry and convention

RF-E8 supplies a Lorentzian ADM foliation with future unit normal

\[
n_\mu n^\mu=-1
\]

and induced spatial metric

\[
h_{\mu\nu}=g_{\mu\nu}+n_\mu n_\nu.
\]

RF-E9 fixes

\[
\boxed{K_{ij}:=-\frac12\mathcal L_n h_{ij}}
\]

or equivalently

\[
\boxed{K_{\mu\nu}=-h_\mu{}^\alpha h_\nu{}^\beta\nabla_\alpha n_\beta.}
\]

All signs below are bound to this convention and signature `(-,+,+,+)`.

## 2. Gauss identity

For spatially projected indices, the Gauss equation is

\[
\boxed{
{}^{(3)}R_{ijkl}
=h_i{}^\alpha h_j{}^\beta h_k{}^\gamma h_l{}^\delta
{}^{(4)}R_{\alpha\beta\gamma\delta}
+K_{ik}K_{jl}-K_{il}K_{jk}.
}
\]

Contracting with `h^{ik}h^{jl}` gives

\[
{}^{(3)}R
=h^{\alpha\gamma}h^{\beta\delta}
{}^{(4)}R_{\alpha\beta\gamma\delta}
+K^2-K_{ij}K^{ij}.
\]

Using

\[
h^{\mu\nu}=g^{\mu\nu}+n^\mu n^\nu
\]

and the Riemann symmetries,

\[
h^{\alpha\gamma}h^{\beta\delta}
{}^{(4)}R_{\alpha\beta\gamma\delta}
={} ^{(4)}R+2{}^{(4)}R_{\mu\nu}n^\mu n^\nu.
\]

Therefore

\[
{}^{(3)}R+K^2-K_{ij}K^{ij}
={} ^{(4)}R+2{}^{(4)}R_{\mu\nu}n^\mu n^\nu.
\]

Since

\[
G_{\mu\nu}n^\mu n^\nu
=R_{\mu\nu}n^\mu n^\nu+\frac12R
\]

for `n_mu n^mu=-1`, one obtains the exact normal-normal projection identity

\[
\boxed{
2G_{\mu\nu}n^\mu n^\nu
={} ^{(3)}R+K^2-K_{ij}K^{ij}.
}
\]

Define the geometric Hamiltonian projection scalar

\[
\boxed{
\mathcal G_H
:={} ^{(3)}R+K^2-K_{ij}K^{ij}.
}
\]

Then

\[
\boxed{\mathcal G_H=2G_{nn}.}
\]

This is a differential-geometric identity; no stress-energy tensor or Einstein field equation enters its derivation.

## 3. Codazzi identity

With the RF-E9 sign convention, the contracted Codazzi equation is

\[
\boxed{
h_i{}^\mu n^\nu R_{\mu\nu}
=D_iK-D_jK^j{}_i.
}
\]

The mixed metric projection vanishes,

\[
h_i{}^\mu n^\nu g_{\mu\nu}=0,
\]

so the Ricci and Einstein mixed projections coincide:

\[
h_i{}^\mu n^\nu G_{\mu\nu}
=h_i{}^\mu n^\nu R_{\mu\nu}.
\]

Hence

\[
\boxed{
h_i{}^\mu n^\nu G_{\mu\nu}
=D_iK-D_jK^j{}_i.}
\]

Define the geometric momentum projection covector

\[
\boxed{
\mathcal G_{M i}
:=D_jK^j{}_i-D_iK.
}
\]

Then the sign-fixed projection identity is

\[
\boxed{
\mathcal G_{M i}
=-h_i{}^\mu n^\nu G_{\mu\nu}.
}
\]

Writing the quantity this way fixes the future matter-source convention without ambiguity at the geometry stage.

## 4. Dimensional typing

RF-E9 gives

\[
[K_{ij}]=L^{-1}.
\]

The spatial Ricci scalar satisfies

\[
[{}^{(3)}R]=L^{-2}.
\]

Therefore

\[
\boxed{[\mathcal G_H]=L^{-2}.}
\]

Similarly,

\[
[D_jK^j{}_i]=L^{-2},
\]

so

\[
\boxed{[\mathcal G_{M i}]=L^{-2}.}
\]

Both geometric projection carriers are dimensionally aligned with Einstein-tensor components.

## 5. Static flat control

For

\[
h_{ij}=\delta_{ij},
\qquad
K_{ij}=0,
\]

one has

\[
{}^{(3)}R=0,
\qquad
\boxed{\mathcal G_H=0,\quad \mathcal G_{Mi}=0.}
\]

The corresponding Minkowski slicing has vanishing Einstein tensor, giving the exact null control.

## 6. Isotropic flat-slice certificate

Take

\[
h_{ij}=a(x^0)^2\delta_{ij},
\qquad
N=1,
\qquad
b^i=0.
\]

RF-E9 gives

\[
K^i{}_j=-H\delta^i{}_j,
\qquad
H:=\frac{a'}a.
\]

Then

\[
K=-3H,
\qquad
K_{ij}K^{ij}=3H^2,
\qquad
{}^{(3)}R=0.
\]

Therefore

\[
\boxed{
\mathcal G_H=6H^2,
\qquad
G_{nn}=3H^2.
}
\]

Spatial homogeneity also gives

\[
\boxed{\mathcal G_{Mi}=0.}
\]

This is a nonzero geometry-only certificate for the normal-normal projection.

## 7. Matter source firewall

The future RFC matter projections are to be introduced separately as

\[
\boxed{
\rho_n:=T_{\mu\nu}n^\mu n^\nu,
}
\]

and, with a sign convention chosen to match the geometric momentum carrier,

\[
\boxed{
j_i:=-h_i{}^\mu n^\nu T_{\mu\nu}.}
\]

RF-E10 does not equate these matter carriers to `G_H` or `G_Mi`. It only fixes the geometric projection identities and their signs.

The subsequent source-binding gate may test a candidate dynamical law of the form

\[
G_{\mu\nu}=\kappa_E T_{\mu\nu}
\]

by projecting it onto the already-derived geometric carriers. That later step is where Hamiltonian and momentum **source constraints** enter.

## 8. Dependency graph

```text
TIR h_ij, D_i
 + IDT N
 + RFC-E8 ADM metric
 -> RFC-E9 K_ij
 -> Gauss identity
 -> G_H = R3 + K^2 - K_ij K^ij = 2 G_nn
 -> Codazzi identity
 -> G_Mi = D_j K^j_i - D_i K = -G_ni
 -> matter projection definitions                         [NEXT SOURCE GATE]
 -> dynamical source binding                              [OPEN]
 -> constraint propagation                                [OPEN]
 -> full Einstein closure                                 [OPEN]
```

## 9. Claim ledger

| Statement | Status |
|---|---|
| Gauss hypersurface identity | STANDARD EXACT DIFFERENTIAL GEOMETRY |
| contracted normal-normal identity | EXACT |
| Codazzi hypersurface identity | STANDARD EXACT DIFFERENTIAL GEOMETRY |
| mixed Einstein-tensor projection sign | EXACT UNDER RF-E9 CONVENTION |
| dimensions `L^-2` | EXACT |
| flat static control | EXACT |
| flat isotropic certificate `G_H=6H^2` | EXACT GEOMETRIC CERTIFICATE |
| matter projection definitions | NEXT TYPING GATE |
| Einstein source binding | DOWNSTREAM DYNAMICAL GATE |
| Hamiltonian/momentum source constraints | DOWNSTREAM DYNAMICAL GATE |
| constraint propagation | DOWNSTREAM GATE |

## 10. Validation target

The deterministic gate must include:

1. flat static null control;
2. flat isotropic nonzero normal-normal certificate;
3. a direct four-dimensional curvature computation for a nontrivial time-dependent metric and comparison with `G_H/2`;
4. a nonhomogeneous component audit fixing the mixed-projection sign;
5. dimensional/status firewall markers.

Verdict target:

`PASS_RF_E10_GAUSS_CODAZZI_PROJECTION_IDENTITIES`.
