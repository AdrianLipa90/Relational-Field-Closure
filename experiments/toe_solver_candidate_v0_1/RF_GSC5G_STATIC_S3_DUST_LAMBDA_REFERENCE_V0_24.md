# RF-GSC5G — Static S3 Dust + Lambda Reference Theorem v0.24

Status: CANDIDATE_ONLY / EXACT_REFERENCE_GEOMETRY_THEOREM / GENERAL_RADIUS_SCALE / NO_PHYSICAL_SOURCE_PROMOTION / CANON_ALLOWED_FALSE

Date: 2026-09-20

## 1. Purpose

V0.23 tests whether the source-derived candidate Einstein tensor is numerically close to a dust-plus-Lambda class.

This note derives the exact reference geometry independently of the SP3 fit.

Let

\[
M=\mathbb R\times S^3_a
\]

with static product metric

\[
\boxed{
g=-dt^2+h_a,
}
\]

where \(S^3_a\) is the round three-sphere of radius \(a>0\).

Define

\[
\boxed{
k=\frac{1}{a^2}.
}
\]

The result below is exact differential geometry and does not use observational data.

## 2. Spatial curvature

For the round three-sphere of sectional curvature \(k\),

\[
{}^{(3)}R_{ijkl}
=
k(h_{ik}h_{jl}-h_{il}h_{jk}),
\]

hence

\[
\boxed{
{}^{(3)}R_{ij}=2k\,h_{ij}
}
\]

and

\[
\boxed{
{}^{(3)}R=6k.
}
\]

## 3. Product spacetime curvature

Because the product is static with unit lapse and zero shift,

\[
R_{00}=0,
\qquad
R_{0i}=0,
\qquad
R_{ij}=2k\,h_{ij}.
\]

The four-dimensional scalar curvature is

\[
\boxed{
R=6k.
}
\]

Therefore

\[
G_{\mu\nu}
=
R_{\mu\nu}
-\frac12Rg_{\mu\nu}.
\]

For the temporal component,

\[
G_{00}
=
0-\frac12(6k)(-1)
=
3k.
\]

For the spatial components,

\[
G_{ij}
=
2k h_{ij}
-
3k h_{ij}
=
-kh_{ij}.
\]

Thus in any orthonormal frame,

\[
\boxed{
G_{\hat a\hat b}
=
\operatorname{diag}
(3k,-k,-k,-k).
}
\]

For the unit-radius normalized carrier \(a=1\),

\[
\boxed{
G_{\hat a\hat b}
=
\operatorname{diag}
(3,-1,-1,-1).
}
\]

## 4. Dust plus Lambda field equation

Take pressureless dust at rest in the product frame:

\[
T_{\hat a\hat b}
=
\operatorname{diag}(\rho,0,0,0).
\]

Use the Einstein-form equation

\[
G_{\hat a\hat b}
+
\Lambda\eta_{\hat a\hat b}
=
\kappa_E T_{\hat a\hat b},
\]

with

\[
\eta=\operatorname{diag}(-1,1,1,1).
\]

The spatial equation is

\[
-k+\Lambda=0.
\]

Therefore

\[
\boxed{
\Lambda=k=\frac1{a^2}.
}
\]

The temporal equation is

\[
3k-\Lambda
=
\kappa_E\rho.
\]

Substituting \(\Lambda=k\) gives

\[
\boxed{
\kappa_E\rho=2k=\frac{2}{a^2}.
}
\]

Hence the static round product has the unique dust-plus-Lambda balance

\[
\boxed{
\Lambda=\frac1{a^2},
\qquad
\kappa_E\rho=\frac{2}{a^2}.
}
\]

At unit normalized radius,

\[
\boxed{
\Lambda=1,
\qquad
\kappa_E\rho=2.
}
\]

## 5. Uniqueness inside the declared source class

Within the source class

\[
T_{\hat a\hat b}
=
\operatorname{diag}(\rho,0,0,0)
\]

and one scalar \(\Lambda\), the spatial equations force \(\Lambda=k\) uniquely.

The temporal equation then forces \(\kappa_E\rho=2k\) uniquely.

Thus the pair is not a chosen fit for the exact static-round reference.

## 6. Vacuum no-go for finite radius

For vacuum,

\[
T_{\hat a\hat b}=0.
\]

The spatial equations would require

\[
\Lambda=k.
\]

The temporal equation would require

\[
3k-\Lambda=0,
\]

hence

\[
\Lambda=3k.
\]

For finite radius,

\[
k>0,
\]

so both conditions cannot hold.

Therefore

\[
\boxed{
\mathbb R\times S^3_a
\text{ is not a vacuum-plus-Lambda solution for finite }a.
}
\]

This exact reference explains why v0.22 should reject the vacuum class if the source-derived candidate is close to the static-round carrier.

## 7. Relation to the SP3 candidate chain

V0.15 normalizes the source-derived ellipsoid to a unit \(S^3\) through the \(Q\)-metric.

V0.16 supplies the global quaternionic orthonormal frame.

V0.17 adds small source-derived lapse and shift departures from the exact static reference.

Therefore v0.23 compares the actual candidate curvature against the exact normalized reference

\[
(\Lambda,\kappa_E\rho)=(1,2).
\]

Agreement would classify the required effective source geometry.

It would not provide independent physical dust evidence.

## 8. Physical scale firewall

The radius \(a\) above is the radius in the metric whose curvature is being evaluated.

The normalized \(Q\)-carrier has unit radius by construction.

No identification is made here between that normalized radius and a cosmological SI length scale.

Therefore

\[
\Lambda=1
\]

in normalized carrier coordinates must not be identified with the observed cosmological constant.

Physical units require an independent length-scale binding.

## 9. Evidence boundary

Exact:

- round-S3 Ricci tensor;
- scalar curvature;
- product Einstein tensor;
- finite-radius vacuum-plus-Lambda no-go;
- unique dust-plus-Lambda balance.

Not established:

- that the physical source is dust;
- that the source-derived carrier has exact round-static dynamics;
- any physical SI value of Lambda or rho;
- W6 source provenance;
- RF-E26 production promotion.
