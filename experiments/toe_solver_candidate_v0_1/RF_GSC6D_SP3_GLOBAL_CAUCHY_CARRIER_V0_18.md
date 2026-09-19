# RF-GSC6D — SP3 Source-Derived Global Cauchy Carrier v0.18

Status: CANDIDATE_ONLY / GLOBAL_TEMPORAL_FUNCTION_EXACT_ON_STATIONARY_EXTENSION / PROPER_CLOCK_DERIVED / GLOBAL_HYPERBOLICITY_ELIGIBLE_BY_EXISTING_RF_GSC6B_THEOREM / RF_E25_PRODUCTION_ATLAS_OPEN / CANON_ALLOWED_FALSE

Date: 2026-09-19

## 1. Purpose

V0.15–v0.17 provide, from one frozen SP3 parent source:

- a smooth compact ellipsoid
  \[
  \mathcal E_Q=\{y:(y-g)^TQ(y-g)=1\},
  \qquad Q>0;
  \]
- a global smooth spatial frame and coframe on \(\mathcal E_Q\);
- a smooth tangent matching vector \(W\);
- a smooth positive lapse \(N(y)\), bounded above and below;
- a global Lorentz coframe
  \[
  \vartheta^0=N\,dx^0,
  \qquad
  \vartheta^a=\theta^a+b^a dx^0;
  \]
- the Lorentz metric
  \[
  g=E^T\eta E,
  \qquad
  \eta=\operatorname{diag}(-1,1,1,1).
  \]

The remaining causal question on this candidate carrier is whether the clock coordinate is a global temporal function whose level sets are Cauchy hypersurfaces.

## 2. Stationary mathematical extension

The source-derived fields \(Q,B,N,\theta^a\) depend only on the spatial carrier coordinate \(y\), not on \(x^0\).

Therefore they define a stationary smooth mathematical extension to

\[
\boxed{
M=\mathbb R\times\mathcal E_Q.
}
\]

This is a mathematical continuation of the frozen source-derived fields. It is not an external observational claim outside the frozen source window.

Let

\[
\boxed{
t:=x^0:M\to\mathbb R.
}
\]

Then

\[
dt\neq0
\]

everywhere.

## 3. Timelike gradient

In the global frame basis
\[
\{\partial_t,e_1,e_2,e_3\},
\]
the coframe matrix is

\[
E=
\begin{pmatrix}
N&0&0&0\\
b^1&1&0&0\\
b^2&0&1&0\\
b^3&0&0&1
\end{pmatrix}.
\]

With
\[
g=E^T\eta E,
\]
one obtains

\[
\boxed{
g^{-1}(dt,dt)=-\frac1{N^2}.
}
\]

Because

\[
N>0,
\]

\[
\boxed{
g^{-1}(dt,dt)<0.
}
\]

Hence \(t\) is a smooth global temporal function on the candidate carrier.

Its level sets

\[
\Sigma_s=t^{-1}(s)
\]

are spacelike and diffeomorphic to \(\mathcal E_Q\).

## 4. Compact spatial fiber

V0.15 gives \(Q>0\). Therefore

\[
\mathcal E_Q
=
g+Q^{-1/2}S^3,
\]

so \(\mathcal E_Q\) is compact and diffeomorphic to \(S^3\).

Thus every time slice

\[
\Sigma_s\cong\mathcal E_Q
\]

is compact.

## 5. Proper temporal clock

For every compact interval \(K=[a,b]\subset\mathbb R\),

\[
t^{-1}(K)
=
[a,b]\times\mathcal E_Q.
\]

Both factors are compact. Therefore

\[
\boxed{
t:M\to\mathbb R
\text{ is proper}.
}
\]

This supplies the exact global input required by RF-GSC6B.

## 6. Lapse regularity

V0.17 proves

\[
0<N_{\min}\le N(y)\le N_{\max}<\infty
\]

on the full compact carrier.

Because the stationary extension introduces no time dependence,

\[
N(t,y)=N(y)
\]

is smooth, finite and strictly positive globally on \(M\).

## 7. RF-GSC6B composition

RF-GSC6B proves the sufficient route

\[
\text{global Lorentzian carrier}
+
\text{global regular proper temporal clock}
+
\text{smooth finite positive lapse}
\Longrightarrow
\text{global hyperbolicity eligibility}.
\]

V0.18 supplies all three premises on the stationary source-derived candidate carrier.

Therefore

\[
\boxed{
(M,g)
\text{ is globally hyperbolic at candidate mathematical level}
}
\]

through the existing RF-GSC6B theorem route.

Consequently the level sets

\[
\boxed{
\Sigma_s=t^{-1}(s)
}
\]

form a global Cauchy foliation on this candidate carrier.

## 8. Relation to IDT 05G

IDT 05G requires a global regular scalar clock to promote local Frobenius integrability to a domain-wide foliation.

Here that scalar is explicitly

\[
t=x^0.
\]

Therefore on this candidate carrier:

\[
\boxed{
\texttt{GLOBAL_CLOCK_SCALAR_INPUT_OPEN}
\to
\texttt{SUPPLIED}.
}
\]

The stronger Cauchy/global-hyperbolicity step is then supplied by RF-GSC6B rather than inferred from Frobenius alone.

## 9. Relation to RF-E25 and RF-E26

This result does not replace RF-E25.

V0.18 proves global hyperbolicity of the already-defined intrinsic candidate Lorentz metric on

\[
\mathbb R\times\mathcal E_Q.
\]

RF-E25 still requires the explicit coordinate-atlas packet

\[
(J_{q\leftarrow p},\Lambda_{q\leftarrow p})
\]

in its executable data structure for atlas certification and production promotion.

RF-E26 still separately requires the global Einstein tensor/source carrier and target-domain coverage.

Therefore:

\[
\boxed{
\text{candidate global Cauchy carrier}
\neq
\text{production RF-E25/RF-E26 promotion}.
}
\]

## 10. Evidence boundary

Exact / candidate mathematical:

- compact \(\mathcal E_Q\);
- stationary extension \(M=\mathbb R\times\mathcal E_Q\);
- global regular clock \(t=x^0\);
- timelike clock gradient;
- properness of \(t\);
- global smooth finite positive lapse;
- RF-GSC6B global-hyperbolicity eligibility;
- global Cauchy foliation on the candidate carrier.

Still open:

- RF-E25 executable coordinate atlas packet;
- physical production admission;
- RF-E26 global Einstein carrier;
- empirical claim that the stationary mathematical extension represents physical evolution outside the frozen source window;
- nonlinear global stability.

No physical production or universal empirical claim is promoted.
