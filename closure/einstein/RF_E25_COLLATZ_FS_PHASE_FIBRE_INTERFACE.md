# RF-E25 — Collatz–Fubini–Study Phase-Fibre Interface

**Date:** 2026-09-04  
**Status:** `FIBRE_INTERFACE_ADDED / METRIC_COUPLING_OPEN / EINSTEIN_FIELD_CLOSURE_UNCHANGED`

## 1. Purpose

This note imports the new IDT/TIR projective phase coordinate into the Einstein-facing closure layer without promoting an unproved modification of the spacetime metric.

The upstream exact phase map is

\[
\zeta_C=e^{i\phi},
\qquad
\phi\mapsto2\phi\pmod{2\pi},
\qquad
\zeta_C\mapsto\zeta_C^2.
\]

The spinorial lift, when required by the state carrier, is typed separately as

\[
\widetilde\phi\in\mathbb R/4\pi\mathbb Z.
\]

## 2. Minimal Einstein-compatible placement

Let \((\mathcal M_4,g)\) be the existing spacetime manifold. The least-assumptive extension is a phase fibre over spacetime,

\[
\boxed{
S^1\hookrightarrow\mathcal E\xrightarrow{\pi}\mathcal M_4
}
\]

with local state

\[
\boxed{(x^\mu,\phi)}.
\]

This does not alter \(g_{\mu\nu}\) by itself.

A local phase connection may be represented as

\[
D_\mu=\partial_\mu+iA_\mu,
\]

with holonomy

\[
\boxed{
\gamma[C]=\oint_C A_\mu\,dx^\mu
}
\]

when such a connection is independently admitted.

## 3. Relation to existing RFC geometry

RFC already carries Fubini–Study/Berry data and the relational lapse

\[
N_R=\frac{d\tau_x}{d\tau_{ref}},
\qquad
g_R=-N_R^2c^2dt^2+h_\perp.
\]

RF-E25 does **not** identify the new discrete phase with \(N_R\), with coordinate time \(t\), or with proper time \(\tau\). The current typed relation is only

\[
\boxed{
\text{IDT discrete phase fibre}\quad\parallel\quad\text{RFC spacetime/lapse geometry}
}
\]

until a physical coupling is derived.

## 4. Candidate metric extension — quarantined

A fibre metric of the familiar form

\[
\widetilde g
=
g_{\mu\nu}dx^\mu dx^\nu
+\lambda^2(d\phi+A_\mu dx^\mu)^2
\]

is mathematically available, but RF-E25 records it only as a **QUARANTINED CANDIDATE**. Neither \(\lambda\), nor the physical identity of \(A_\mu\), nor the coupling to RFC source tensors is currently derived.

Therefore the canonical RFC metric remains unchanged.

## 5. Compatibility conditions for later promotion

Any future phase–gravity coupling must satisfy all of the following before promotion:

1. preserve local Lorentz covariance of the physical spacetime sector;
2. identify whether the phase is gauge, internal, observable, or redundant;
3. derive rather than fit the coupling scale;
4. preserve the Bianchi identity and source conservation after variation;
5. reduce to the existing RFC/GR sector when phase coupling is switched off;
6. avoid double-counting Berry/connection structure already present upstream;
7. provide a measurable discriminator or prove representational equivalence.

## 6. Discrete return structure

For every tested/assumed Collatz trajectory reaching the terminal cycle,

\[
q(n)\in\frac{1}{7\,2^{L_n}}\mathbb Z,
\qquad
\zeta_C(n)^{7\,2^{L_n}}=1.
\]

RF-E25 may therefore transport a root-of-unity-labelled internal phase state along spacetime curves. This is a kinematic interface only. It does not imply quantized spacetime, quantized proper time or modified Einstein equations.

## 7. Einstein-sector frontier

The revised dependency order is

\[
\boxed{
\mathrm{TIR}
\to
\mathrm{IDT\ phase/time}
\to
\mathrm{relational\ phase\ fibre}
\to
\mathrm{RFC\ geometry/lapse}
\to
\mathrm{source\ derivation}
\to
\mathrm{Einstein\ closure}
}
\]

The existing Einstein closure gate remains open. RF-E25 narrows the interface by specifying where the new phase structure may enter without contaminating the already-derived metric/source results.

## 8. Claim firewall

**EXACT / imported mathematics:** circle phase, doubling map, CP1/Fubini–Study placement, 2π/4π distinction.

**RFC kinematic extension:** phase fibre over \(\mathcal M_4\).

**QUARANTINED:** extended metric term, physical gauge connection, coupling scale.

**OPEN:** any modification to Einstein equations, stress–energy, lapse dynamics, Newtonian limit or cosmological sector.
