# RF-GSC5G — SP3-Only W6 Source Insufficiency v0.24

Status: CANDIDATE_ONLY / CURRENT_SOURCE_TYPE_INSUFFICIENCY / EXTERNAL_AUGMENTATION_REQUIRED / NO_SOURCE_PROMOTION / CANON_ALLOWED_FALSE

Date: 2026-09-20

## 1. Purpose

V0.21 defines the fail-closed W6 physical source receipt contract required downstream of RF-E24/RF-E26.

The current frozen SP3 source contains two epochs of:

- satellite spatial coordinates;
- satellite clock corrections.

It is already useful for clock, spatial-carrier and matching-field construction.

This note asks a narrower question:

\[
\boxed{
\text{Can the current SP3 archive by itself satisfy W6?}
}
\]

The answer under the current typed contracts is no.

## 2. Current SP3 observable content

The frozen source records contain, for five satellites and two epochs,

\[
(x,y,z,\delta t_{\rm clock}).
\]

They therefore directly provide:

- coordinate observations;
- two-epoch displacements;
- derived tangent/matching data;
- clock-rate information.

They do not directly contain:

- local matter density;
- conserved matter current;
- electromagnetic field tensor;
- scalar-field amplitude/phase source packet;
- rank-two stress-energy observations;
- independently certified vacuum-domain coverage;
- full-patch source tensor coverage on both stereographic atlas patches.

## 3. W6 requirements

V0.21 requires, on each atlas patch:

1. independent source observations;
2. immutable source provenance;
3. a symmetric covariant rank-two source tensor;
4. full-patch coverage;
5. independence from target-metric construction;
6. an RF-E24 local-solution residual certificate;
7. the same source-field lineage across both patches.

The current SP3 archive does not contain those source primitives.

## 4. Four obvious SP3-only routes and why they fail

### 4.1 No source tensor

Using positions and clocks only, with no source tensor packet, fails the W6 schema directly.

### 4.2 Define T from the target geometry

Defining

\[
T_{\mu\nu}
=
\frac{1}{\kappa_E}
\left(
G_{\mu\nu}
+
\Lambda g_{\mu\nu}
\right)
\]

fails the v0.21 independence firewall.

It is an algebraic rearrangement of the equation under test, not independent physical source evidence.

### 4.3 Declare vacuum

Setting

\[
T_{\mu\nu}=0
\]

without independent vacuum-domain provenance fails the W6 vacuum-source rule.

V0.22 additionally tests the vacuum-plus-one-Lambda source class against the candidate metric rather than treating vacuum as a free label.

### 4.4 Promote the finite anchors to patch coverage

The five SP3 anchor observations are finite source points.

W6 requires source-tensor coverage of the full north and south atlas patches.

Declaring finite anchors to be full-patch coverage without an independently validated source model/interpolation law fails the coverage firewall.

## 5. Relation to RF-N1B

RF-N1B already proves an upstream source-identifiability statement:

the current relational geometry/clock state does not identify a unique physical matter density without an additional conserved source carrier, measure and energy assignment.

The present result is the RF-E26/W6 specialization of that firewall.

SP3 supplies geometry/clock observations.

It does not by itself supply the missing independent physical source primitive.

## 6. Exact advancement

The remaining production frontier is therefore not

\[
\text{more manipulation of SP3 positions/clocks}.
\]

It is

\[
\boxed{
\text{additional independent source dataset or source primitive}
}
\]

with:

- matter/field observables;
- source conservation/transport semantics;
- full-patch coverage or a certified model that supplies it;
- immutable provenance;
- common realization/source lineage with the metric carrier.

## 7. What external augmentation could look like

Admissible future source classes include, in principle:

- independently calibrated matter/current density;
- independently measured electromagnetic field data sufficient to reconstruct \(T^{EM}_{\mu\nu}\);
- independently admitted scalar-field source data;
- a physically certified vacuum-domain packet;
- another source model with its own action/provenance and tensor construction.

Each must satisfy v0.21 independently.

## 8. Evidence boundary

This no-go is conditional on the current repository source types and contracts.

It does not prove that SP3 can never participate in a future richer source derivation.

It proves:

\[
\boxed{
\text{current frozen SP3 position/clock archive alone}
\not\Rightarrow
\text{W6 physical source packet}.
}
\]

No physical source is manufactured or promoted.
