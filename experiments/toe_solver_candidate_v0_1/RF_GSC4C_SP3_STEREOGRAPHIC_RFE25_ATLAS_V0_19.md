# RF-GSC4C — SP3 Stereographic RF-E25 Atlas Bridge v0.19

Status: CANDIDATE_ONLY / EXACT_TWO_CHART_STEREOGRAPHIC_COVER / ORIENTATION_PRESERVING_OVERLAP / GLOBAL_QUATERNIONIC_COFRAME_PULLBACK / RF_E25_EXECUTABLE_COMPATIBILITY_PASS_TARGET / PRODUCTION_ADMISSION_OPEN / CANON_ALLOWED_FALSE

Date: 2026-09-19

## 1. Purpose

V0.15–v0.18 supply a compact source-derived spatial carrier

\[
\mathcal E_Q
=
\{y:(y-g)^TQ(y-g)=1\},
\qquad
Q>0,
\]

together with the deterministic map

\[
u=R(y-g)\in S^3,
\qquad
Q=R^TR,
\]

a global quaternionic orthonormal frame/coframe on the carrier, a smooth source-derived shift, a smooth positive lapse, a global Lorentz metric, and a candidate global Cauchy foliation.

The remaining RF-E25 software seam is an explicit finite coordinate-atlas packet

\[
(J_{q\leftarrow p},\Lambda_{q\leftarrow p})
\]

compatible with the existing GSC4A / RF-E25 certifier.

This note supplies that packet from a two-chart stereographic cover of the already-derived \(S^3\)-carrier.

## 2. North stereographic chart

Write

\[
u=(u_0,\mathbf u),
\qquad
u_0^2+|\mathbf u|^2=1.
\]

On

\[
U_N=S^3\setminus\{(1,0,0,0)\},
\]

define

\[
\boxed{
x=\frac{\mathbf u}{1-u_0}\in\mathbb R^3.
}
\]

The inverse map is

\[
\boxed{
u_N(x)
=
\left(
\frac{|x|^2-1}{|x|^2+1},
\frac{2x}{|x|^2+1}
\right).
}
\]

## 3. Oriented south stereographic chart

The ordinary south stereographic coordinate

\[
s=\frac{\mathbf u}{1+u_0}
\]

has an orientation-reversing transition relative to the north chart in three dimensions.

Introduce the fixed reflection

\[
\boxed{
S=\operatorname{diag}(-1,1,1)
}
\]

and define the oriented south coordinate

\[
\boxed{
q=S\,s.
}
\]

The chart domain is

\[
U_S=S^3\setminus\{(-1,0,0,0)\}.
\]

Since \(S^2=I\), its inverse is

\[
\boxed{
u_S(q)
=
\left(
\frac{1-|q|^2}{1+|q|^2},
\frac{2Sq}{1+|q|^2}
\right).
}
\]

The two domains cover the full sphere:

\[
\boxed{
U_N\cup U_S=S^3.
}
\]

## 4. Exact overlap transition

On the overlap, \(x\neq0\), and

\[
\boxed{
q
=
S\,\frac{x}{|x|^2}.
}
\]

Let

\[
A(x)
=
\frac{\partial q}{\partial x}.
\]

Then

\[
\boxed{
A(x)
=
S
\left(
\frac{I}{|x|^2}
-
\frac{2xx^T}{|x|^4}
\right).
}
\]

Ordinary inversion in \(\mathbb R^3\) has determinant

\[
-|x|^{-6},
\]

while

\[
\det S=-1.
\]

Therefore

\[
\boxed{
\det A(x)=|x|^{-6}>0.
}
\]

The overlap is orientation preserving exactly as required by RF-E25.

The time coordinate is shared:

\[
\boxed{
t_S=t_N.
}
\]

Therefore the four-dimensional coordinate Jacobian is

\[
\boxed{
J_{S\leftarrow N}
=
\begin{pmatrix}
1&0\\
0&A
\end{pmatrix},
}
\]

whose first row is exactly

\[
(1,0,0,0).
\]

## 5. Pullback of the global quaternionic coframe

Let \(J_a\), \(a=1,2,3\), be the fixed quaternionic generators used by v0.16.

On \(S^3\),

\[
E_a(u)=J_au
\]

is the global orthonormal tangent frame.

The dual one-forms are

\[
\boxed{
\theta^a(v)
=
(J_au)^Tv.
}
\]

Pull them back into each stereographic chart.

Define the north triad matrix

\[
\boxed{
(T_N)^a{}_i
=
(J_au_N)^T
\frac{\partial u_N}{\partial x^i}
}
\]

and the south triad matrix

\[
\boxed{
(T_S)^a{}_i
=
(J_au_S)^T
\frac{\partial u_S}{\partial q^i}.
}
\]

Because both are pullbacks of the same global coframe and

\[
u_S(q(x))=u_N(x),
\]

the chain rule gives

\[
\boxed{
T_S(q(x))\,A(x)=T_N(x).
}
\]

Thus no nontrivial Lorentz-frame rotation is required.

Take

\[
\boxed{
\Lambda_{S\leftarrow N}=I_4.
}
\]

Then

\[
\Lambda^T\eta\Lambda=\eta,
\qquad
\det\Lambda=1,
\qquad
\Lambda^0{}_0=1.
\]

## 6. Source-derived shift in chart coordinates

V0.16 provides the global frame coefficients

\[
b^a(y)=\frac{B^a(y)}{c}
\]

for the smooth matching vector

\[
W=\sum_a b^ae_a.
\]

In north coordinates, define

\[
\boxed{
w_N=T_N^{-1}b.
}
\]

In south coordinates, define

\[
\boxed{
w_S=T_S^{-1}b.
}
\]

Using

\[
T_SA=T_N,
\]

one obtains

\[
\boxed{
w_S=Aw_N.
}
\]

Thus the coordinate shift obeys the GSC4A overlap rule with zero temporal drift:

\[
\boxed{
v=0.
}
\]

## 7. ADM coframes in the two charts

Let \(N(y)>0\) be the source-derived lapse from v0.17.

Define

\[
E_N
=
\begin{pmatrix}
N&0\\
b&T_N
\end{pmatrix},
\]

\[
E_S
=
\begin{pmatrix}
N&0\\
b&T_S
\end{pmatrix}.
\]

Then

\[
\boxed{
E_SJ_{S\leftarrow N}
=
E_N
=
\Lambda_{S\leftarrow N}E_N.
}
\]

Hence the exact RF-E25 overlap equation holds:

\[
\boxed{
E_SJ_{S\leftarrow N}
=
\Lambda_{S\leftarrow N}E_N.
}
\]

Consequently

\[
\boxed{
J^Tg_SJ=g_N.
}
\]

## 8. Executable RF-E25 compatibility packet

The analytic theorem is independent of sampling.

For software compatibility, v0.19 additionally selects one frozen source anchor lying in the chart overlap and evaluates:

- common source lapse \(N\);
- north triad \(T_N\);
- south triad \(T_S\);
- north coordinate shift \(w_N\);
- south coordinate shift \(w_S\);
- spatial Jacobian \(A\);
- temporal drift \(v=0\);
- spatial rotation \(R_{\rm overlap}=I_3\).

These are supplied directly to

\[
\texttt{assemble\_source\_shared\_spacetime\_atlas}
\]

which internally calls the existing RF-E25 certifier.

This software witness verifies data-structure compatibility with the current GSC4A / RF-E25 implementation.

## 9. Evidence boundary

Exact mathematical:

- two stereographic charts cover \(S^3\);
- overlap transition is explicit;
- overlap Jacobian is orientation preserving;
- both chart triads are pullbacks of one global quaternionic coframe;
- \(T_SA=T_N\);
- shift transforms as \(w_S=Aw_N\);
- shared time coordinate has exact RF-E25 first Jacobian row;
- \(\Lambda=I_4\) is proper orthochronous Lorentz;
- RF-E25 overlap equation holds analytically.

Executable candidate evidence:

- one frozen-source overlap instantiation is passed through the real GSC4A / RF-E25 implementation.

Still open:

- production admission of the source-derived atlas;
- production provenance classification for the chart packet;
- RF-E26 global Einstein carrier;
- empirical claim that the stationary extension represents physical evolution outside the frozen source window.

The mathematical atlas seam is the target of this candidate.
Production promotion remains separate.
