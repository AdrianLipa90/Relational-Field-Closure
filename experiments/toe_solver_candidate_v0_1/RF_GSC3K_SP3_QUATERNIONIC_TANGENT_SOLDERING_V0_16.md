# RF-GSC3K — SP3 Quaternionic Tangent Soldering v0.16

Status: CANDIDATE_ONLY / EXPLICIT_GLOBAL_Q_ORTHONORMAL_FRAME / SMOOTH_MATCHING_VECTOR_FIELD / EXACT_COFAME_ANNIHILATION / COMPACT_CARRIER_COMPLETE_FLOW / PHYSICAL_RF_E25_IDENTIFICATION_OPEN / CANON_ALLOWED_FALSE

Date: 2026-09-19

## 1. Purpose

V0.15 constructs the smooth source-derived ellipsoid

\[
\mathcal E_Q
=
\{y:(y-g)^\top Q(y-g)=1\}
\]

with \(Q>0\), containing all five source midpoint points, together with the smooth affine matching coefficient field

\[
B|_{\mathcal E_Q}:\mathcal E_Q\to\mathbb R^3.
\]

The remaining mathematical seam is the conversion of the three coefficient functions into an actual tangent vector field and spatial coframe on \(\mathcal E_Q\).

## 2. Canonical linear map to the unit 3-sphere

Let the positive-definite Cholesky factorization be

\[
\boxed{
Q=R^\top R
}
\]

with the standard positive-diagonal convention.

For

\[
z=y-g,
\]

define

\[
\boxed{
u=Rz.
}
\]

On \(\mathcal E_Q\),

\[
|u|^2
=
z^\top R^\top Rz
=
z^\top Qz
=
1,
\]

so

\[
u\in S^3\subset\mathbb R^4.
\]

Thus \(R\) gives a deterministic coordinate-basis-dependent diffeomorphism between the source ellipsoid and the unit \(S^3\).

## 3. Standard quaternionic frame on \(S^3\)

Identify

\[
u=(u_0,u_1,u_2,u_3)
\]

with a unit quaternion.

Let \(J_1,J_2,J_3\) be the constant real \(4\times4\) matrices for left multiplication by the quaternion units \(i,j,k\).

They satisfy

\[
J_a^\top=-J_a,
\]

and for every unit \(u\),

\[
u^\top J_a u=0,
\]

\[
(J_a u)^\top(J_b u)=\delta_{ab}.
\]

Hence

\[
E_a(u)=J_a u
\]

is a global orthonormal tangent frame on \(S^3\).

## 4. Pushforward to the source ellipsoid

Define

\[
\boxed{
e_a(y)
=
R^{-1}J_aR(y-g).
}
\]

Then

\[
(y-g)^\top Qe_a
=
u^\top J_a u
=
0,
\]

so every \(e_a\) is tangent to \(\mathcal E_Q\).

Moreover,

\[
e_a^\top Qe_b
=
(J_au)^\top(J_bu)
=
\delta_{ab}.
\]

Therefore

\[
\boxed{
\{e_1,e_2,e_3\}
}
\]

is a globally smooth \(Q\)-orthonormal frame of \(T\mathcal E_Q\).

This closes the purely mathematical tangent-frame existence and gives one deterministic frame relative to the source coordinate ordering and Cholesky convention.

## 5. Dual spatial coframe

Define

\[
\boxed{
\theta^a(v)
=
e_a^\top Qv
}
\]

for tangent vectors \(v\in T_y\mathcal E_Q\).

Then

\[
\boxed{
\theta^a(e_b)=\delta^a{}_b.
}
\]

Thus \(\{\theta^a\}\) is the exact dual coframe.

## 6. Solder the source matching coefficients

Let v0.15 supply the smooth coefficient field

\[
B(y)=(B^1,B^2,B^3),
\]

and define the dimensionless shift coefficients

\[
\boxed{
b^a(y)=\frac{B^a(y)}{c}.
}
\]

Define the spatial matching vector

\[
\boxed{
W(y)
=
\sum_{a=1}^{3}
b^a(y)e_a(y).
}
\]

Then

\[
\boxed{
\theta^a(W)=b^a.
}
\]

Hence on the product carrier

\[
M=I\times\mathcal E_Q
\]

with clock coordinate \(x^0\), define

\[
\boxed{
X
=
\partial_{x^0}-W.
}
\]

The spatial one-forms

\[
\boxed{
\vartheta^a
=
\theta^a+b^a dx^0
}
\]

satisfy

\[
\boxed{
\vartheta^a(X)=0.
}
\]

Also

\[
dx^0(X)=1.
\]

This is exactly the algebraic clock-transverse matching condition used by RF-GSC3A.

## 7. Completeness on the compact carrier

The ellipsoid \(\mathcal E_Q\) is compact.

The field \(W\) is smooth because both \(B\) and \(e_a\) are smooth.

A smooth vector field on a compact manifold is complete. Therefore its flow \(\psi_s\) exists for all finite \(s\).

Consequently the product field

\[
X=\partial_{x^0}-W
\]

has interval-complete spatial flow on every admitted clock interval \(I\).

At candidate mathematical level this supplies the RF-GSC3A flow-coverage premise for the source-derived carrier.

## 8. What is closed

Candidate-level mathematical chain:

\[
\text{source 3+1 records}
\to
\text{data-defined 4-simplex}
\to
\text{unique affine matching coefficients}
\to
\text{smooth source ellipsoid}
\to
\text{global }Q\text{-orthonormal tangent frame}
\to
\text{smooth matching vector}
\to
\text{exact GSC3A coframe annihilation}
\to
\text{complete spatial flow}.
\]

No arbitrary interpolation kernel or smoothing parameter is introduced.

## 9. What remains open

The frame is canonical relative to:

- the source coordinate ordering;
- the exact source quadratic form \(Q\);
- the positive-diagonal Cholesky convention;
- the standard quaternion orientation.

The remaining physics gate is not tangent-field existence. It is the identification of this mathematically explicit source-derived frame/coframe with the physical RF-E25 spatial coframe/metric realization.

Therefore:

\[
\boxed{
\text{candidate smooth matching field}
\;\text{CLOSED},
}
\]

while

\[
\boxed{
\text{physical RF-E25 coframe/metric identity}
\;\text{OPEN}.
}
\]

## 10. Evidence boundary

Current classification:

source quadratic form Q: EXACT PARENT V0.15
smooth carrier: EXACT PARENT V0.15
global quaternionic frame: EXACT
Q-orthonormal tangent frame: EXACT
dual coframe: EXACT
smooth matching vector: EXACT CANDIDATE
coframe annihilation: EXACT
compact-carrier flow completeness: STANDARD
physical RF-E25 coframe identity: OPEN
global physical spatial-carrier interpretation: OPEN
physical production claim: FALSE
canon allowed: FALSE
