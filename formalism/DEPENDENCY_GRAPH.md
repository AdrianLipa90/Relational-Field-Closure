# Relational Field Closure — Canonical Dependency Graph

Status: `CURRENT_FRONTIER / CROSS_REFERENCE_LOCK_V0_28`

## Core dependency spine

```text
TIR/IDT geometry + phase source
 -> RFN1C three-route coupling holonomy
 -> RF-E3/E4/E5 Einstein/source closures
 -> RFG3/RFG4G Yang-Mills normalization
 -> RFG8-RFG15 project interaction + four-point BCJ
 -> RFG16-RFG22 four-point double-copy / spin-2 / normalization / pole / KLT
 -> RFG23 five-point BCJ + conserved gauge soft reference
 -> RFG24 five-point KLT kernel + reduced scale
 -> RFG25 direct Berends-Giele / BCJ
 -> RFG26 direct BG x BG KLT core
 -> RFG27 project normalization + conserved gravity soft transport
 -> RFG28 non-soft s12 KLT pole factorization
 -> RFG29 explicit 15-cubic-graph/project-current residue expansion     NEXT
```

Four-point physical coupling remains

\[
\kappa_E=\frac{\kappa_g^2}{4}=8\pi G=\frac1{\bar M_G^2}=\frac1{M_HT_H}.
\]

RFG27 fixes the five-point color-order map and amplitude coefficient:

\[
A_5^{project}=2A_5^{BG},\qquad
C_5^{project}=4C_5^{BG},
\]

\[
\boxed{M_5^{project}=-\frac{i}{4}\left(\frac{\kappa_g}{2}\right)^3C_5^{project}=-i\left(\frac{\kappa_g}{2}\right)^3C_5^{BG}}.
\]

RFG28 adds the independent non-soft factorization channel

\[
s_{12}\to0,
\]

with

\[
\boxed{C_5^{BG}\sim1/s_{12}},\qquad
\boxed{\operatorname*{Res}_{s_{12}=0}C_5^{BG}=(s_{13}+s_{23})R_L^{YM}R_R^{YM}}.
\]

The KLT residue is rank one: cross and finite basis contributions vanish after multiplication by `s12`. On the project surface,

\[
\boxed{\operatorname*{Res}M_5^{project}=-i\left(\frac{\kappa_g}{2}\right)^3\operatorname*{Res}C_5^{BG}}.
\]

## Open firewalls

```text
RFG29 explicit 15-cubic-graph project BCJ numerator representation
RFG29 explicit 3pt x 4pt project-current residue expansion
higher-point per-vertex normalization beyond the pinned eta_A map
internal-state / loop spectrum and pure-Einstein audit
Gamma_DC numerical promotion
M_star physical-scale promotion
cross-system Mbar_G universality
universal G evidence
complete total-matter T_mn binding
dynamic Lambda_0 action closure
```
