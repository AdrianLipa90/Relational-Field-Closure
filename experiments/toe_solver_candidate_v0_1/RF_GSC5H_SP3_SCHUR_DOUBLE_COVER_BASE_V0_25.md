# RF-GSC5H — SP3 Schur Double-Cover Base v0.25

Status: CANDIDATE_ONLY / EXACT_SCHUR_BASE / TWO_SHEET_RELATIONAL_COVER / FIBERED_BINDING_CANDIDATE / PHYSICAL_SOURCE_BINDING_OPEN / CANON_ALLOWED_FALSE

Date: 2026-09-20

## 1. Purpose

V0.23 and v0.24 reject two shortcuts:

- the direct first-three-coordinate projection is not globally injective;
- the four-dimensional feature carrier is not affinely identical to the same-epoch physical spacetime event set.

This note extracts the exact structure that remains.

The source-derived ellipsoid

\[
\mathcal E_Q
=
\{y:(y-g)^TQ(y-g)=1\},
\qquad Q>0,
\]

is naturally a two-sheeted relational cover of a three-dimensional ellipsoidal base.

## 2. Block decomposition

Write

\[
y-g=
\begin{pmatrix}
\xi\\
\zeta
\end{pmatrix},
\qquad
\xi\in\mathbb R^3,
\quad
\zeta\in\mathbb R,
\]

and partition

\[
Q=
\begin{pmatrix}
A&q\\
q^T&d
\end{pmatrix},
\qquad
d>0.
\]

Then

\[
(y-g)^TQ(y-g)
=
\xi^TA\xi
+
2\zeta q^T\xi
+
d\zeta^2.
\]

## 3. Schur completion

Complete the square:

\[
d
\left(
\zeta+\frac{q^T\xi}{d}
\right)^2
+
\xi^T
\left(
A-\frac{qq^T}{d}
\right)
\xi
=
1.
\]

Define the Schur complement

\[
\boxed{
S
=
A-\frac{qq^T}{d}.
}
\]

Because \(Q>0\) and \(d>0\),

\[
\boxed{
S>0.
}
\]

Therefore the projected three-dimensional base is the closed ellipsoid

\[
\boxed{
\mathcal B_S
=
\{\xi\in\mathbb R^3:
\xi^TS\xi\le1\}.
}
\]

## 4. Two exact sheets

For an interior base point

\[
\xi^TS\xi<1,
\]

the carrier equation has exactly two solutions:

\[
\boxed{
\zeta_\pm(\xi)
=
-\frac{q^T\xi}{d}
\pm
\frac{1}{\sqrt d}
\sqrt{
1-\xi^TS\xi
}.
}
\]

Thus

\[
\boxed{
y_\pm(\xi)
=
g+
\begin{pmatrix}
\xi\\
\zeta_\pm(\xi)
\end{pmatrix}
}
\]

are two distinct points of \(\mathcal E_Q\) with the same three-dimensional base coordinate.

On the boundary

\[
\xi^TS\xi=1,
\]

the two branches coincide.

## 5. Topological interpretation

The carrier is therefore two copies of the three-ball-like base

\[
\mathcal B_S
\]

glued along their common boundary

\[
\partial\mathcal B_S
\cong S^2.
\]

Hence

\[
\boxed{
\mathcal E_Q
\cong
\operatorname{Double}(\mathcal B_S)
\cong
S^3.
}
\]

This recovers the v0.15 topology while exposing the two-sheet structure hidden by the ambient \(R^4\) representation.

## 6. Meaning of the fourth feature

The fourth feature does not become physical coordinate time.

Instead it resolves the two relational sheets over the same three-dimensional base point through

\[
\zeta-\zeta_0(\xi)
=
\pm
\frac{1}{\sqrt d}
\sqrt{1-\xi^TS\xi},
\]

where

\[
\zeta_0(\xi)
=
-\frac{q^T\xi}{d}.
\]

Thus the fourth feature distinguishes relational branches over a common spatial-feature base.

The present theorem does not assign an ontological meaning to the sheet sign.

## 7. Source-anchor reconstruction

Each frozen source midpoint anchor \(y_i\) projects to

\[
\xi_i
=
(y_i^1-g^1,y_i^2-g^2,y_i^3-g^3)
\]

inside or on \(\mathcal B_S\).

Its fourth feature is recovered by exactly one of the two branch values:

\[
\boxed{
\zeta_i
=
\zeta_+(\xi_i)
\quad\text{or}\quad
\zeta_-(\xi_i).
}
\]

Therefore the double-cover description is not an approximation to the v0.15 carrier.

It is an exact rewriting of it.

## 8. Fibered external-source pullback candidate

Let an independent external physical source field be defined on a physical three-dimensional base domain.

A mathematically well-defined candidate pullback may factor through the base projection:

\[
\pi:
\mathcal E_Q
\to
\mathcal B_S.
\]

Then a base field

\[
F_{\rm base}(\xi)
\]

lifts to

\[
\boxed{
F_{\rm carrier}(y)
=
F_{\rm base}(\pi(y)).
}
\]

The two relational sheets receive the same base-field value unless an independently justified sheet-dependent coupling is supplied.

This is structurally different from claiming that \(\mathcal E_Q\) itself is ordinary physical three-space.

## 9. Physical-time separation

The physical time coordinate remains supplied by the independent IDT/RFC clock sector.

Therefore a candidate spacetime source-binding architecture has the form

\[
\boxed{
I_{\rm clock}
\times
\mathcal E_Q
\longrightarrow
I_{\rm phys}
\times
\mathcal B_S
}
\]

with

\[
(t,y)
\mapsto
(\tau(t,y),\pi(y)).
\]

The simplest sheet-independent source pullback uses only the base coordinate for spatial source lookup, while the clock sector supplies physical time.

This remains a candidate architecture, not yet a physical production binding.

## 10. Branch locus

The projection ceases to be locally two-to-one on

\[
\partial\mathcal B_S,
\]

where the two sheets meet.

Therefore any physical-source adapter using the base projection must explicitly handle the branch locus.

It may:

- exclude it from a production subdomain;
- cover it with a separate patch;
- prove that the pulled-back source tensor extends smoothly across it.

The branch locus cannot be silently ignored.

## 11. Relation to W6

V0.21 requires full patch source coverage and independent physical provenance.

The Schur base theorem does not satisfy W6 by itself.

It supplies a mathematically explicit candidate architecture for the missing physical binding:

\[
\boxed{
\text{external physical spatial field}
\to
\mathcal B_S
\to
\mathcal E_Q
}
\]

together with a separate physical-time binding.

A future W6 adapter must still certify:

- physical coordinate-frame mapping onto \(\mathcal B_S\);
- physical time mapping;
- source-domain coverage;
- branch-locus handling;
- tensor transformation;
- independent source provenance.

## 12. Evidence boundary

Exact:

- Schur complement \(S>0\);
- projected base is a three-dimensional ellipsoid;
- interior fibers contain exactly two carrier points;
- boundary fibers contain one;
- the source carrier is the double of the base ellipsoid;
- all source anchors reconstruct exactly.

Open:

- interpretation of sheet sign;
- identification of \(\mathcal B_S\) with a physical source domain;
- physical time map;
- external tensor pullback;
- W6 source evidence.

The theorem gives a fibered carrier structure, not a production spacetime identification.
