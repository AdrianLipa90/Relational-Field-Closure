# RF-GSC5H — Static S3 ADM Dust + Lambda Cross-Check v0.25

Status: CANDIDATE_ONLY / EXACT_INDEPENDENT_ADM_CROSSCHECK / RF_E12_RF_E13_COMPOSITION / NO_PHYSICAL_SOURCE_PROMOTION / CANON_ALLOWED_FALSE

Date: 2026-09-20

## 1. Purpose

V0.24 derives the static round-S3 dust-plus-Lambda balance directly from the four-dimensional Einstein tensor.

This note derives the same result independently from the existing RF-E12 Hamiltonian constraint and RF-E13 spatial evolution equation.

The target is an internal consistency cross-check, not a new source claim.

## 2. Static round-S3 data

Let

\[
M=\mathbb R\times S^3_a
\]

with

\[
k=\frac1{a^2},
\qquad
{}^{(3)}R_{ij}=2k h_{ij},
\qquad
{}^{(3)}R=6k.
\]

Choose the static slicing

\[
N=1,
\qquad
b^i=0,
\qquad
K_{ij}=0.
\]

For pressureless dust at rest,

\[
\rho_n=\rho,
\qquad
j_i=0,
\qquad
S_{ij}=0,
\qquad
S=0.
\]

Define

\[
A:=\kappa_E\rho.
\]

## 3. RF-E12 Hamiltonian constraint

The constant-Lambda RF-E12 constraint is

\[
{}^{(3)}R
+
K^2
-
K_{ij}K^{ij}
-
2\Lambda
=
2\kappa_E\rho_n.
\]

Under the static data,

\[
6k-2\Lambda=2A.
\]

Therefore

\[
\boxed{
3k-\Lambda=A.
}
\]

## 4. RF-E13 spatial evolution

The dynamic-Lambda form of the RF-E13 spatial equation is

\[
(\partial_0-\mathcal L_b)K_{ij}
=
-D_iD_jN
+
N\left(
{}^{(3)}R_{ij}
+
KK_{ij}
-
2K_{ik}K^k{}_j
\right)
+
N\kappa_E
\left[
\frac12h_{ij}(S-\rho_n)-S_{ij}
\right]
-
N\Lambda h_{ij}.
\]

For the static round dust data, the left side is zero, \(D_iD_jN=0\), and all K terms vanish. Thus

\[
0
=
2k h_{ij}
-
\frac12 A h_{ij}
-
\Lambda h_{ij}.
\]

Since \(h_{ij}\) is nondegenerate,

\[
\boxed{
2k-\frac A2-\Lambda=0.
}
\]

## 5. Solve the two independent ADM conditions

The system is

\[
3k-\Lambda=A,
\]

\[
2k-\frac A2-\Lambda=0.
\]

Substituting the first equation into the second gives

\[
2k
-
\frac12(3k-\Lambda)
-
\Lambda
=
0.
\]

Hence

\[
k-\Lambda=0,
\]

so

\[
\boxed{
\Lambda=k.
}
\]

Then

\[
A=3k-k=2k,
\]

therefore

\[
\boxed{
\kappa_E\rho=2k.
}
\]

With

\[
k=\frac1{a^2},
\]

\[
\boxed{
\Lambda=\frac1{a^2},
\qquad
\kappa_E\rho=\frac2{a^2}.
}
\]

## 6. Unit-radius reference

For \(a=1\),

\[
\boxed{
\Lambda=1,
\qquad
\kappa_E\rho=2.
}
\]

This is exactly the v0.24 direct-Einstein reference.

## 7. Vacuum cross-check

For vacuum \(A=0\), RF-E12 requires

\[
\Lambda=3k.
\]

RF-E13 static evolution requires

\[
\Lambda=2k.
\]

For finite radius \(k>0\), these cannot both hold.

Therefore the ADM route independently gives

\[
\boxed{
\text{finite-radius static } \mathbb R\times S^3
\text{ is not vacuum+Lambda}.
}
\]

The direct Einstein-tensor route v0.24 gave the equivalent contradiction through temporal versus spatial tensor components.

## 8. Independence of the cross-check

V0.24 computes the four-dimensional Einstein tensor and solves the tensor equation directly.

V0.25 instead consumes:

- the RF-E12 normal-normal action projection;
- the RF-E13 spatial evolution projection;
- the intrinsic round-S3 curvature identities.

Agreement therefore checks the ADM projection/evolution roundtrip against the direct covariant tensor calculation.

## 9. Relation to the SP3 candidate

If v0.23 classifies the source-derived geometry as close to the normalized static-S3 dust-plus-Lambda class, then v0.24 and v0.25 provide two exact theoretical references for the same parameter pair.

Neither route supplies independent W6 physical source evidence.

The actual physical source packet remains governed by v0.21.

## 10. Evidence boundary

Exact:

- RF-E12 Hamiltonian reduction;
- RF-E13 static spatial evolution reduction;
- unique solution \(\Lambda=k,\ \kappa_E\rho=2k\);
- finite-radius vacuum no-go;
- agreement with v0.24.

Not established:

- physical dust provenance;
- physical value of the radius;
- physical SI Lambda or density;
- W6 completion;
- RF-E26 production promotion.
