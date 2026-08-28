# Relational Field Closure — Canonical Dependency Graph

Status: `CURRENT_FRONTIER / CROSS_REFERENCE_LOCK_V0_30`

```text
TIR/IDT source + geometry
 -> RFN1C / RF-E3-E5 coupling and source closure
 -> RFG4G-RFG15 project Yang-Mills / four-point BCJ
 -> RFG16-RFG22 four-point double-copy / spin-2 / normalization / KLT
 -> RFG23-RFG28 five-point reference, direct BG, normalization and pole factorization
 -> RFG29 explicit 15-graph project BCJ + current residue
 -> RFG30 explicit 15-graph double-copy <-> KLT equivalence
 -> RFG31 internal-state tree-factorization / pure-spin2 firewall        NEXT
```

RFG29 provides

\[
F=B^TD^{-1}B,\qquad \operatorname{rank}F_5=2,\qquad m^\star=F^+A^{project},\qquad n=Bm^\star.
\]

RFG30 closes the explicit graph gravity core:

\[
\boxed{\mathcal C_{5,15g}^{project}=\sum_g\frac{n_g\widetilde n_g}{D_g}=-\mathcal C_{5,KLT}^{project}}.
\]

The graph orientation therefore carries

\[
\boxed{\mathcal M_5^{project}=+\frac{i}{4}\left(\frac{\kappa_g}{2}\right)^3\mathcal C_{5,15g}^{project}},
\]

which is identical to the RFG27 KLT-oriented amplitude. Independent null-space shifts of either numerator copy leave the graph core invariant.

On `s12 -> 0`,

\[
\boxed{\operatorname*{Res}\mathcal C_{5,15g}^{project}=-4(s_{13}+s_{23})(N_{12}\cdot J_4)(\widetilde N_{12}\cdot\widetilde J_4)}.
\]

## Open firewalls

```text
RFG31 internal-state tree-factorization / pure-spin2 audit
loop internal-state spectrum audit
direct diagram-local alternative numerator representative
Gamma_DC numerical promotion
M_star physical-scale promotion
cross-system Mbar_G universality
universal G evidence
complete total-matter T_mn binding
dynamic Lambda_0 action closure
```
