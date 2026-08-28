# Relational Field Closure — Canonical Dependency Graph

Status: `CURRENT_FRONTIER / CROSS_REFERENCE_LOCK_V0_33`

```text
TIR/IDT -> Newton/Einstein source closure
 -> project Yang-Mills normalization and BCJ
 -> four-point double copy / spin-2 / Einstein normalization
 -> five-point BG / KLT / project normalization / pole
 -> RFG29 explicit 15-graph BCJ
 -> RFG30 explicit 15-graph double-copy <-> KLT
 -> RFG31 matched-helicity internal tree spin-2 factorization
 -> RFG32 raw-loop mixed internal-state spectrum firewall
 -> RFG33 explicit pure-spin2 internal-state projector              PASS
 -> RFG34 projected-cut Ward / factorization / crossing audit       NEXT
```

RFG31 pins the selected tree factorization residue to the symmetric-traceless spin-two sector.

RFG32 shows that the corresponding loop state isolation is not automatic. On a generic two-particle t-channel cut, each Yang-Mills copy admits internal assignments `(+,-)` and `(-,+)`. Independent copy sums therefore generate both matched spin-two and crossed helicity-zero tensor-product states:

\[
\boxed{\mathcal C_{raw}=(x_A+x_B)^2},
\qquad
\boxed{\mathcal C_{spin2}=x_A^2+x_B^2},
\qquad
\boxed{\mathcal C_{mixed}=2x_Ax_B\neq0}.
\]

RFG33 introduces the explicit one-line tensor-product helicity projector

\[
\boxed{P_2=\operatorname{diag}(1,0,0,1)}
\]

on the ordered basis

\[
\{|++\rangle,|+-\rangle,|-+\rangle,|--\rangle\}.
\]

It satisfies

\[
P_2^\dagger=P_2,\qquad P_2^2=P_2,\qquad \operatorname{rank}P_2=2,
\]

and on the RFG32 two-particle cut gives

\[
\boxed{\mathcal C_{projected}=x_A^2+x_B^2},
\qquad
\boxed{\mathcal C_{removed}=2x_Ax_B=\mathcal C_{mixed}}.
\]

Thus the mixed internal sector is now removed by an explicit state-space operator rather than an inferred cancellation.

## Open firewalls

```text
RFG34 projected-cut Ward / factorization / crossing audit
loop-integrand realization with the RFG33 projector
integrated loop amplitude
permutation-complete tree internal-state extension
direct diagram-local alternative numerator representative
Gamma_DC numerical promotion
M_star physical-scale promotion
cross-system Mbar_G universality
universal G evidence
complete total-matter T_mn binding
dynamic Lambda_0 action closure
```
