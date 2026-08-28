# Relational Field Closure — Canonical Dependency Graph

Status: `CURRENT_FRONTIER / CROSS_REFERENCE_LOCK_V0_29`

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
 -> RFG29 explicit 15-graph project BCJ + 3pt x 4pt current residue
 -> RFG30 explicit 15-graph double-copy <-> KLT equivalence          NEXT
```

The physical coupling spine remains

\[
\kappa_E=\frac{\kappa_g^2}{4}=8\pi G=\frac1{\bar M_G^2}=\frac1{M_HT_H}.
\]

RFG27 fixes

\[
A_5^{project}=2A_5^{BG},\qquad C_5^{project}=4C_5^{BG},
\]

\[
M_5^{project}=-\frac{i}{4}\left(\frac{\kappa_g}{2}\right)^3C_5^{project}.
\]

RFG29 introduces the explicit cubic-graph coordinates

\[
F_{\alpha\beta}=\sum_{g=1}^{15}\frac{B_{g\alpha}B_{g\beta}}{D_g},\qquad \operatorname{rank}F_5=2,
\]

\[
m^\star=F^+A^{project},\qquad n_g=B_{g\alpha}m^\star_\alpha.
\]

The fifteen numerators satisfy the nine independent matched Jacobi relations and reconstruct all six DDM master amplitudes plus the full color-dressed project amplitude.

On the RFG28 `s12` factorization surface,

\[
\boxed{\operatorname*{Res}A_{12345}^{project}=\frac{n_{12|3|45}}{s_{45}}-\frac{n_{12|5|34}}{s_{34}}},
\]

while the same residue is resolved into project currents as

\[
\boxed{\operatorname*{Res}A_{12345}^{BG}=N_{12}\cdot J_{(12)|345}}.
\]

The two-copy residue reproduces the RFG28 rank-one KLT factorization.

## Open firewalls

```text
RFG30 explicit 15-graph double-copy / KLT equivalence
direct diagram-local alternative numerator representative
internal-state / loop spectrum and pure-Einstein audit
Gamma_DC numerical promotion
M_star physical-scale promotion
cross-system Mbar_G universality
universal G evidence
complete total-matter T_mn binding
dynamic Lambda_0 action closure
```
