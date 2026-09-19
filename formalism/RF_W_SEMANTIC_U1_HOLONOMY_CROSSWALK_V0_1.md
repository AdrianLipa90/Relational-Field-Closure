# RFC W_sem Semantic U(1) Holonomy Crosswalk v0.1

Status: `TYPE_FIREWALL / CHYBA / CANON_NOT_PROMOTED`

Date: 2026-09-19

## Purpose

This note prevents symbol collision between the newly typed semantic U(1) transporter and existing RFC/Metatime gauge transports.

## Semantic transport

Let `A_sem` be a local semantic U(1) connection/potential on a declared relational path gamma. Define

\[
\boxed{W^{\rm sem}_{ij}[\gamma]=\exp\!\left(i\int_{\gamma_{ij}}A_{\rm sem}\right)\in U(1).}
\]

For a discrete path,

\[W^{\rm sem}_{ij}[\gamma]=\exp\!\left(i\sum_{e\in\gamma}A_e^{\rm sem}\right).\]

`W_sem` is a nonlocal semantic phase transporter / holonomy. It is not identified by notation alone with any physical gauge field.

## Existing RFC objects remain distinct

- RFC Abelian phase/Wilson constructions from `A_minus` or other explicitly typed U(1) connections remain their own objects.
- RFC/Metatime non-Abelian links `W_ij^c` / Wilson loops in the colour sector remain SU(3)-valued.
- Continuum Yang-Mills connections `A_mu^a` and lattice links derived from them remain non-Abelian gauge objects.
- Existing White-Thread/Berry transports remain source-typed according to their own provenance.

Therefore no unsuperscripted equality such as `W_sem = W_ij^c` is permitted.

## Allowed source binding

An identification between `W_sem` and another U(1) transporter is allowed only if all of the following are explicit:

1. same endpoints and oriented path;
2. same connection normalization;
3. same fibre/gauge convention;
4. same source provenance;
5. same epistemic status.

Absent those gates, the relation is only a crosswalk, not equality.

## Semantic coupling observable

For projective relation overlap `z_ij`,

\[\boxed{\mathcal C_{ij}[\gamma]=W^{\rm sem}_{ij}[\gamma]z_{ij}.}\]

A pure scalar U(1) transporter preserves `|z_ij|` and transports its phase.

## Boundary

This crosswalk does not establish physical nonlocal signalling, hypercharge, electroweak identification, or equivalence between semantic and colour holonomies.