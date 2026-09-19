# RF-GSC3L — SP3 Source-Lapse Lorentz Coframe v0.17

Status: CANDIDATE_ONLY / UNIQUE_AFFINE_LOG_LAPSE / POSITIVE_GLOBAL_LAPSE / GLOBAL_LORENTZ_COFRAME_ON_SOURCE_CARRIER / RF_E25_COORDINATE_ATLAS_AND_PRODUCTION_ADMISSION_OPEN / CANON_ALLOWED_FALSE

Date: 2026-09-19

## 1. Purpose

V0.13–v0.16 already provide, from one frozen SP3 parent source:

- five source midpoint events;
- a source-defined affine 4-simplex;
- one unique affine matching coefficient field \(B\);
- the source-derived smooth ellipsoid \(\mathcal E_Q\);
- one global \(Q\)-orthonormal tangent frame \(e_a\);
- its dual coframe \(\theta^a\);
- the dimensionless matching coefficients
  \[
  b^a=\frac{B^a}{c};
  \]
- the smooth tangent matching vector
  \[
  W=\sum_a b^a e_a.
  \]

The remaining local ADM datum is a positive lapse.

The same external SP3 parent already supplies five relative clock-rate observations used by the existing observational E2E as source-derived log-lapse values.

## 2. Source-derived log lapse

Let the five source anchors be \(y_i\in\mathbb R^4\), and let the existing clock packet provide

\[
L_i
=
\log N_i
\]

relative to the reference source clock.

Because the five \(y_i\) are affinely independent, there is one unique affine scalar function

\[
\boxed{
L(y)
=
q_0+\sum_{\mu=0}^{3}q_{\mu+1}y^\mu
}
\]

such that

\[
\boxed{
L(y_i)=L_i
}
\]

for all five source anchors.

Define

\[
\boxed{
N(y)=e^{L(y)}.
}
\]

Then

\[
\boxed{
N(y)>0
}
\]

everywhere.

Since \(\mathcal E_Q\) is compact and \(L\) is continuous, \(N\) is globally finite and bounded away from zero on the entire source-derived carrier.

No lapse fit parameter is introduced beyond the five source clock values.

## 3. Global ADM coframe in the v0.16 frame

Use the product carrier

\[
M=I\times\mathcal E_Q
\]

with dimensionless/normalized clock coordinate \(x^0\).

Define

\[
\boxed{
\vartheta^0
=
N\,dx^0
}
\]

and

\[
\boxed{
\vartheta^a
=
\theta^a+b^a dx^0.
}
\]

In the global frame basis

\[
\{\partial_{x^0},e_1,e_2,e_3\},
\]

the coframe matrix is

\[
\boxed{
E(y)
=
\begin{pmatrix}
N & 0 & 0 & 0\\
b^1 & 1 & 0 & 0\\
b^2 & 0 & 1 & 0\\
b^3 & 0 & 0 & 1
\end{pmatrix}.
}
\]

Therefore

\[
\boxed{
\det E=N>0.
}
\]

The coframe has rank four everywhere.

## 4. Lorentz metric

With

\[
\eta=\operatorname{diag}(-1,1,1,1),
\]

define

\[
\boxed{
g=E^\top\eta E.
}
\]

Because \(E\) is invertible and \(N>0\), Sylvester inertia under congruence gives

\[
\boxed{
\operatorname{signature}(g)=(-,+,+,+).
}
\]

Also

\[
\boxed{
\det g=-N^2<0.
}
\]

Hence the source-derived carrier admits a globally smooth Lorentz metric candidate.

## 5. Matching-flow compatibility

V0.16 defines

\[
X
=
\partial_{x^0}-W.
\]

Since

\[
\theta^a(W)=b^a,
\]

one has

\[
\boxed{
\vartheta^a(X)=0.
}
\]

The temporal form gives

\[
\boxed{
\vartheta^0(X)=N>0.
}
\]

Thus \(X\) is future-oriented and exactly transverse to the spatial ADM coframe.

This is the intrinsic version of the RF-GSC3A/RF-E25 local ADM relation.

## 6. What is source-derived

The construction consumes no independently selected metric coefficients:

\[
\boxed{
\text{SP3 positions}
\to Q,\theta^a
}
\]

\[
\boxed{
\text{SP3 spatial differences}
\to B
\to b
}
\]

\[
\boxed{
\text{SP3 clock-rate differences}
\to L
\to N.
}
\]

Then

\[
\boxed{
(Q,B,L)
\to
(\vartheta^0,\vartheta^a)
\to
g.
}
\]

The local Lorentz metric coefficients are therefore downstream of one common frozen source parent.

## 7. Relation to RF-E25

RF-E25 requires local ADM coframes

\[
\vartheta^0=Ndx^0,
\qquad
\vartheta^a=e^a{}_i(dx^i+b^i dx^0),
\]

plus coordinate-atlas overlaps and Lorentz-frame transitions.

V0.17 supplies the intrinsic global coframe and Lorentz metric on the source-derived carrier.

It does not yet provide the finite coordinate atlas packet

\[
(J_{q\leftarrow p},\Lambda_{q\leftarrow p})
\]

in the exact data structure consumed by the RF-E25 executable certifier.

That is now the narrow mathematical/software gate.

## 8. Evidence boundary

Current classification:

five source log-lapse anchors: EXTERNAL ARCHIVE DERIVED
unique affine log lapse: EXACT GIVEN SOURCE VALUES
positive lapse N=exp(L): EXACT
global Q-orthonormal spatial coframe: EXACT PARENT V0.16
global shift coefficients: EXACT CANDIDATE PARENT
global ADM coframe rank four: EXACT
global Lorentz signature: EXACT
matching-field coframe annihilation: EXACT
future orientation theta0(X)>0: EXACT
RF-E25 coordinate atlas packet: OPEN
physical production admission: OPEN
physical production claim: FALSE
canon allowed: FALSE
