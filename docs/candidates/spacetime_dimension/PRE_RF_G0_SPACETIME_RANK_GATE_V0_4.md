# PRE-RF-G0 Spacetime Rank Gate v0.4

Status: **CANDIDATE / EXACT PREMETRIC RANK THEOREM**

Purpose: derive the local spacetime-base dimension before any RFC theorem assumes
a four-dimensional base or writes a four-dimensional metric.

## 1. Upstream data

TIR/RFC spatial geometry supplies three local spatial one-forms

\[
E^1,E^2,E^3
\]

whose spatial coframe matrix has rank three.

IDT/RFC supplies one positive elapsed-clock one-form

\[
E^0=N_Rc\,dt,
\qquad N_R>0.
\]

The dimension question must be decided before defining

\[
g=-(E^0)^2+\sum_i(E^i)^2.
\]

## 2. Premetric zero-shift condition

Define the temporal direction \(e_0\) and spatial directions \(e_i\) without
reference to a metric by the incidence conditions

\[
\boxed{
E^0(e_0)\ne0,
\qquad
E^i(e_0)=0
}
\]

and

\[
\boxed{
E^0(e_i)=0.
}
\]

Let

\[
S_{ij}:=E^i(e_j).
\]

The independently derived spatial-rank result is

\[
\boxed{\det S\ne0.}
\]

No Lorentzian metric is used in these premises.

## 3. Four-volume theorem

Evaluate the four one-forms on the four candidate directions. The coframe matrix is

\[
C=
\begin{pmatrix}
E^0(e_0)&0&0&0\\
0&&&\\
0&&S&\\
0&&&
\end{pmatrix}.
\]

Therefore

\[
\boxed{
\det C
=
E^0(e_0)\det S.
}
\]

Since both factors are nonzero,

\[
\boxed{\det C\ne0.}
\]

Equivalently,

\[
\boxed{
E^0\wedge E^1\wedge E^2\wedge E^3\ne0.
}
\]

Hence the cotangent rank is exactly four on the admitted patch:

\[
\boxed{\dim T_p^*M=4.}
\]

This establishes the local base dimension before metric signature is introduced.

## 4. Why this removes the RF-G0 circularity

Current RF-G0 states its signature theorem on an already four-dimensional
relational base. The corrected dependency is:

\[
\text{TIR spatial carrier}
\to
\operatorname{rank}(E^1,E^2,E^3)=3,
\]

\[
\text{IDT elapsed primitive}
\to
E^0\ne0,
\]

\[
\text{PREMETRIC ZERO-SHIFT INCIDENCE}
\to
E^0\wedge E^1\wedge E^2\wedge E^3\ne0,
\]

\[
\boxed{D=4},
\]

and only then

\[
g
=
-E^0\otimes E^0
+\sum_{i=1}^3E^i\otimes E^i
\]

with Lorentzian signature.

Thus dimension and signature become two consecutive theorems rather than one
theorem with dimension in its premise.

## 5. Hermitian soldering cross-check

Using the Pauli basis, define the matrix-valued coframe

\[
\boxed{
\mathbb E
=
\frac12
\left(
E^0 I+\sum_{i=1}^3E^i\sigma_i
\right).
}
\]

For any tangent vector \(v\),

\[
\boxed{
4\det\mathbb E(v)
=
E^0(v)^2
-\sum_{i=1}^3E^i(v)^2.
}
\]

Thus after the premetric rank gate has established four independent legs, the
same primitive `Herm(2)` carrier supplies the Lorentzian quadratic form by its
determinant.

## 6. Exact remaining test in the repositories

The spatial factor is already available:

\[
\det S\ne0
\]

from the rank-three TIR/RFC spatial metric/coframe work.

The unresolved repository-level statement is now only the premetric incidence
binding

\[
\boxed{
E^i(e_0)=0,
\qquad
E^0(e_i)=0,
}
\]

derived from the relational construction rather than from a metric declared
zero-shift after the fact.

A sufficient implementation gate is:

`PREMETRIC_TEMPORAL_SPATIAL_TRANSVERSALITY`

with executable defect matrix

\[
D_{\rm cross}
=
\left(
E^1(e_0),E^2(e_0),E^3(e_0),
E^0(e_1),E^0(e_2),E^0(e_3)
\right).
\]

PASS requires

\[
D_{\rm cross}=0
\]

and independently

\[
E^0(e_0)\ne0,\qquad \det S\ne0.
\]

## 7. Status ledger

| Claim | Status |
|---|---|
| spatial coframe rank 3 | CURRENT TIR/RFC RESULT |
| IDT elapsed one-form nonzero on active clock domain | EXACT / CONDITIONAL ON ACTIVE DOMAIN |
| four-volume determinant factorization | EXACT |
| nonzero four-volume under transversality | EXACT |
| Hermitian matrix-coframe determinant identity | EXACT |
| premetric temporal/spatial transversality in current repo | OPEN |
| local base dimension 4 after transversality PASS | EXACT CONSEQUENCE |
| Lorentzian signature after dimension gate | EXACT CONSEQUENCE / RF-G0 |
