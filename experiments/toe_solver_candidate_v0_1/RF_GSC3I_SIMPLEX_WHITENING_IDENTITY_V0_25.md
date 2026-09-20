# RF-GSC3I — Simplex Whitening Identity v0.25

Status: CANDIDATE_ONLY / GENERAL_N_SIMPLEX_WHITENING_THEOREM / V0_15_REGULARITY_REINTERPRETED_AS_NORMALIZATION_IDENTITY / NOT_EMPIRICAL_SIGNATURE / CANON_ALLOWED_FALSE

Date: 2026-09-20

## 1. Purpose

V0.15 defines, from five affinely independent source points in four real dimensions,

\[
Q=\frac54\left(\sum_{i=1}^{5}z_i z_i^T\right)^{-1},
\qquad
z_i=y_i-\bar y,
\]

and obtains

\[
z_i^TQz_i=1,
\qquad
z_i^TQz_j=-\frac14
\quad(i\ne j).
\]

Those identities are mathematically correct.

This note determines their evidential status.

The result is stronger and more general: for any \(n+1\) affinely independent points in \(\mathbb R^n\), the same whitening construction necessarily produces the Gram matrix of a regular \(n\)-simplex.

Therefore the regular-simplex identities are a theorem of the normalization, not an independent empirical signature of the particular SP3 source.

## 2. General centered simplex

Let

\[
y_1,\ldots,y_{n+1}\in\mathbb R^n
\]

be affinely independent.

Define

\[
\bar y=\frac1{n+1}\sum_{i=1}^{n+1}y_i,
\qquad
z_i=y_i-\bar y.
\]

Form the \(n\times(n+1)\) centered data matrix

\[
\boxed{
Z=
\begin{pmatrix}
|&&|\\
z_1&\cdots&z_{n+1}\\
|&&|
\end{pmatrix}.
}
\]

Centering gives

\[
\boxed{
Z\mathbf 1=0.
}
\]

Affine independence gives

\[
\boxed{
\operatorname{rank}Z=n.
}
\]

Since \(Z\) has \(n+1\) columns and rank \(n\), its nullspace is one-dimensional.

Because \(\mathbf1\) lies in that nullspace,

\[
\boxed{
\ker Z=\operatorname{span}\{\mathbf1\}.
}
\]

Hence the row space of \(Z\) is exactly

\[
\boxed{
\operatorname{row}(Z)=\mathbf1^\perp.
}
\]

## 3. The whitening projector

Define

\[
S=ZZ^T=\sum_{i=1}^{n+1}z_i z_i^T.
\]

Because \(Z\) has full row rank,

\[
S>0
\]

and is invertible.

Consider

\[
\boxed{
P=Z^T(ZZ^T)^{-1}Z.
}
\]

For any full-row-rank matrix, this is the orthogonal projector onto the row space of \(Z\).

But

\[
\operatorname{row}(Z)=\mathbf1^\perp.
\]

The orthogonal projector onto \(\mathbf1^\perp\subset\mathbb R^{n+1}\) is uniquely

\[
\boxed{
P
=
I_{n+1}
-
\frac1{n+1}\mathbf1\mathbf1^T.
}
\]

Therefore

\[
\boxed{
Z^TS^{-1}Z
=
I_{n+1}
-
\frac1{n+1}\mathbf1\mathbf1^T.
}
\]

Entrywise,

\[
\boxed{
z_i^TS^{-1}z_j
=
\delta_{ij}
-
\frac1{n+1}.
}
\]

Thus

\[
z_i^TS^{-1}z_i=\frac{n}{n+1}
\]

and, for \(i\ne j\),

\[
z_i^TS^{-1}z_j=-\frac1{n+1}.
\]

## 4. Regular-simplex normalization

Define

\[
\boxed{
Q
=
\frac{n+1}{n}S^{-1}.
}
\]

Then

\[
\boxed{
z_i^TQz_i=1
}
\]

for every \(i\), and

\[
\boxed{
z_i^TQz_j=-\frac1n
}
\]

for every \(i\ne j\).

Therefore every affinely independent \(n+1\)-point simplex becomes a regular \(n\)-simplex in its own centered whitening metric \(Q\).

This is an identity, not a source-specific coincidence.

## 5. Affine covariance

Let

\[
y_i'=Ay_i+b
\]

with

\[
A\in GL(n,\mathbb R).
\]

Then

\[
z_i'=Az_i
\]

and

\[
S'=AS A^T.
\]

Consequently

\[
(S')^{-1}
=
A^{-T}S^{-1}A^{-1}.
\]

The whitened Gram products satisfy

\[
(z_i')^T(S')^{-1}z_j'
=
z_i^TS^{-1}z_j.
\]

Therefore

\[
\boxed{
\text{the normalized simplex Gram matrix is invariant under every invertible affine change of coordinates.}
}
\]

The regular-simplex result is intrinsic to the affine simplex together with the whitening prescription.

## 6. Specialization to v0.15

For v0.15,

\[
n=4,
\qquad
n+1=5.
\]

Hence

\[
\boxed{
Q=\frac54S^{-1}
}
\]

and automatically

\[
\boxed{
z_i^TQz_i=1,
\qquad
z_i^TQz_j=-\frac14.
}
\]

Thus the exact v0.15 identities are a direct specialization of the general theorem.

They do not independently indicate that the five SP3-derived points possess an unexpected physical regular-simplex symmetry.

## 7. What remains source-specific in v0.15

The following remain genuinely source-dependent:

1. that the selected five four-component source vectors are affinely independent;
2. the numerical matrix \(S\);
3. the numerical whitening metric \(Q\);
4. the orientation and scale of the corresponding ellipsoid in the original source coordinates;
5. the source-dependent affine matching field \(B\);
6. the embedding of the five source anchors into the resulting normalized carrier.

The following are not independent source-specific discoveries once \(Q\) is defined by whitening:

\[
z_i^TQz_i=1,
\]

\[
z_i^TQz_j=-\frac14,
\]

and the statement that the five vertices form a regular 4-simplex in the \(Q\)-metric.

## 8. Circumellipsoid interpretation

The level set

\[
\mathcal E_Q
=
\{y:(y-\bar y)^TQ(y-\bar y)=1\}
\]

still passes through all five source vertices exactly.

That statement remains mathematically correct.

However, because \(Q\) is constructed from the same five vertices, the existence of such a normalized circumellipsoid is also construction-driven.

Therefore

\[
\boxed{
\mathcal E_Q
\text{ is a canonical data-normalized carrier, not by itself evidence that physical space is an }S^3\text{-like ellipsoid}.
}
\]

Its later mathematical uses remain valid as candidate constructions.

Its physical identity remains an independent binding gate.

## 9. Consequence for v0.16--v0.22

V0.16--v0.19 use \(\mathcal E_Q\) as a mathematically explicit carrier.

Those downstream constructions are not invalidated by the present theorem.

The evidential interpretation changes:

\[
\boxed{
\text{source data}
\to
\text{canonical whitening carrier}
\to
\text{candidate differential geometry}
}
\]

must remain distinct from

\[
\boxed{
\text{physical spatial manifold identification}.
}
\]

V0.22 is therefore necessary: physical product-domain promotion requires an independent source-owned full-domain binding rather than the fact that the whitening carrier is internally regular.

## 10. Main theorem

### Theorem — simplex whitening identity

For any \(n+1\) affinely independent points in \(\mathbb R^n\), define centered columns \(z_i\), let

\[
S=\sum_i z_i z_i^T,
\]

and define

\[
Q=\frac{n+1}{n}S^{-1}.
\]

Then

\[
\boxed{
z_i^TQz_j
=
\begin{cases}
1,&i=j,\\
-1/n,&i\ne j.
\end{cases}
}
\]

Equivalently, the centered vertices form a regular \(n\)-simplex in the whitening metric \(Q\).

The theorem follows solely from centering and affine independence.

## 11. Evidence reclassification

For v0.15:

- affine independence of the selected source points: SOURCE-SPECIFIC EXACT;
- construction of \(S\) and \(Q\): SOURCE-SPECIFIC DETERMINISTIC;
- positive definiteness of \(Q\): EXACT CONSEQUENCE OF AFFINE INDEPENDENCE;
- unit diagonal / minus-one-quarter off-diagonal Gram identities: GENERAL WHITENING IDENTITY;
- regular 4-simplex in \(Q\): GENERAL WHITENING IDENTITY;
- \(S^3\)-like ellipsoid as normalized candidate carrier: CONSTRUCTION-LEVEL;
- physical spatial identity: OPEN EXTERNAL BINDING.

## 12. Integrity firewall

The following inference is prohibited:

\[
\text{regular in source-derived }Q
\Longrightarrow
\text{independent empirical evidence for physical regular-simplex geometry}.
\]

The left side is guaranteed by the whitening definition.

The correct inference is:

\[
\boxed{
\text{affinely independent source simplex}
\Longrightarrow
\text{canonical regular representation after whitening}.
}
\]

No physical-production or empirical-theory-confirmation claim is promoted.
