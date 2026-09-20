# RF-GSC5F — SP3 Physical Embedding Gate v0.23

Status: CANDIDATE_ONLY / DIRECT_R3_PROJECTION_NO_GO / PHYSICAL_EMBEDDING_REQUIRED / SOURCE_PULLBACK_GATE / CANON_ALLOWED_FALSE

Date: 2026-09-20

## 1. Purpose

V0.15 defines the smooth source-derived spatial carrier

\[
\mathcal E_Q
=
\left\{
y\in\mathbb R^4:
(y-g)^TQ(y-g)=1
\right\},
\qquad
Q>0.
\]

The fourth ambient coordinate used in this construction is the dimensionally homogenized SP3 clock-correction feature.

It is not the physical event-trace time coordinate.

This note determines whether the carrier can nevertheless be identified globally with physical three-space by simply discarding that fourth ambient coordinate.

It cannot.

## 2. Naive spatial projection

Define

\[
\pi:\mathcal E_Q\to\mathbb R^3
\]

by

\[
\boxed{
\pi(y^1,y^2,y^3,y^4)
=
(y^1,y^2,y^3).
}
\]

If \(\pi\) were a valid global physical-space identification, it would at least need to be injective on the full carrier.

## 3. Exact non-injectivity witness

Let \(e_4=(0,0,0,1)^T\).

Because \(Q\) is positive definite,

\[
Q_{44}>0.
\]

Define

\[
\boxed{
y_\pm
=
g
\pm
\frac{1}{\sqrt{Q_{44}}}e_4.
}
\]

Then

\[
y_\pm-g
=
\pm
\frac{1}{\sqrt{Q_{44}}}e_4.
\]

Therefore

\[
(y_\pm-g)^TQ(y_\pm-g)
=
\frac{1}{Q_{44}}
e_4^TQe_4
=
1.
\]

Hence

\[
\boxed{
y_+,y_-\in\mathcal E_Q.
}
\]

They are distinct because

\[
y_+^4\neq y_-^4.
\]

But

\[
\boxed{
\pi(y_+)=\pi(y_-)=
(g^1,g^2,g^3).
}
\]

Therefore

\[
\boxed{
\pi
\text{ is not injective}.
}
\]

So the direct first-three-coordinate projection cannot be a global physical-space embedding of the source-derived carrier.

## 4. Consequence for external physical-source binding

A physical source model such as a magnetospheric plasma / electromagnetic field model lives on a physical spacetime domain with its own coordinate frame.

The source-derived carrier \(\mathcal E_Q\) is instead a relational three-manifold represented by an embedding in \(\mathbb R^4\).

Therefore an external source tensor cannot be bound globally by the rule

\[
T_{\mu\nu}(y)
=
T_{\mu\nu}^{\rm ext}(y^1,y^2,y^3)
\]

without an additional physical-identification theorem.

That shortcut is many-to-one on \(\mathcal E_Q\).

## 5. Fourth ambient coordinate is not physical time

The fourth ambient coordinate in v0.15 is constructed by converting the SP3 clock-correction feature into length units.

The earlier Herm(2) bridge already rejects identifying that raw clock-correction coordinate with the physical event-trace scale.

Therefore the alternative shortcut

\[
(y^1,y^2,y^3,y^4)
\mapsto
(t,\mathbf x)
\]

with

\[
t\propto y^4
\]

is also not admitted.

The physical time coordinate belongs to the separately calibrated IDT/RFC clock sector.

## 6. Required physical embedding

To bind an independent external physical source to the carrier, one must provide a map

\[
\boxed{
\Psi:
I\times\mathcal E_Q
\to
\Omega_{\rm phys}
}
\]

into the physical source-model spacetime domain.

At minimum, \(\Psi\) must provide:

- a physical time map;
- a physical spatial map;
- a declared source coordinate frame;
- a declared target coordinate frame;
- a nonsingular local Jacobian on every admitted patch;
- overlap consistency between north and south charts;
- exact or bounded agreement at the frozen source anchors;
- immutable provenance for the frame transformation;
- coverage of the full declared production target domain.

## 7. Anchor consistency

Let the five frozen source anchors be

\[
y_i\in\mathcal E_Q.
\]

A valid physical embedding must reproduce the source-owned physical event data at those anchors within the declared observational tolerance:

\[
\boxed{
\Psi(t_i,y_i)
=
e_i^{\rm source}
}
\]

up to the explicitly declared coordinate-frame transformation and observational uncertainty.

The anchor constraint alone does not determine \(\Psi\) globally.

A separate interpolation / physical-model binding is required.

## 8. Tensor pullback

If an external physical source model supplies

\[
T_{\alpha\beta}^{\rm phys}
\]

on \(\Omega_{\rm phys}\), then the carrier-side source tensor must be obtained through the declared spacetime map and its Jacobian.

Schematically,

\[
\boxed{
T^{\rm carrier}
=
\Psi^*T^{\rm phys}.
}
\]

The pullback receipt must bind:

- source tensor digest;
- embedding digest;
- frame-transform digest;
- chart Jacobian digest;
- target patch/domain;
- source time interval;
- interpolation rule;
- residual / uncertainty budget.

Only then may the result enter the v0.21 W6 contract.

## 9. Relation to SWMF / magnetosphere candidates

A full 3D time-dependent magnetosphere model is a plausible future independent source-lineage candidate.

However, model availability alone does not solve the binding problem.

Before any such field can count as W6 evidence, the route must provide the physical map from the relational carrier to the model's coordinate system and certify full patch/domain coverage.

Thus:

\[
\boxed{
\text{external source field}
+
\text{no physical embedding}
\neq
\text{W6}.
}
\]

## 10. Main theorem

For the source-derived ellipsoid

\[
\mathcal E_Q
\subset\mathbb R^4
\]

with \(Q>0\), the projection to the first three ambient coordinates is not injective.

Therefore there is no canonical global identification

\[
\mathcal E_Q
\equiv
\mathbb R^3_{\rm physical}
\]

obtained merely by dropping the fourth ambient coordinate.

A separately justified physical embedding / pullback map is required before independently sourced physical fields can be used as W6 stress-energy evidence.

## 11. Evidence boundary

Exact:

- \(Q_{44}>0\);
- two distinct carrier points with identical first-three-coordinate projection exist;
- direct \(R^3\) projection is globally non-injective;
- raw clock-correction feature remains distinct from physical event time.

Open:

- physical embedding \(\Psi\);
- frame transformation to an external source model;
- full production-domain pullback coverage;
- independent W6 source tensor.

This result narrows the next step from "find a source model" to:

\[
\boxed{
\text{construct and certify the physical embedding first.}
}
\]
