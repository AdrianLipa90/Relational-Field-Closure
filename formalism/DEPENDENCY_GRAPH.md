# Relational Field Closure — Canonical Dependency Graph

Status: `CURRENT_FRONTIER / CROSS_REFERENCE_LOCK_V0_34`

```text
TIR/IDT -> Newton/Einstein source closure
 -> project Yang-Mills normalization and BCJ
 -> four-point double copy / spin-2 / Einstein normalization
 -> five-point BG / KLT / project normalization / pole
 -> RFG29 explicit 15-graph BCJ
 -> RFG30 explicit 15-graph double-copy <-> KLT
 -> RFG31 matched-helicity internal tree spin-2 factorization
 -> RFG32 raw-loop mixed internal-state spectrum firewall
 -> RFG33 explicit pure-spin2 internal-state projector
 -> RFG34 projected s/t/u loop-cut channel covariance              PASS
 -> RFG35 vector-polarization projected-cut Ward audit             NEXT
```

For one internal double-copy line, RFG33 uses

\[
\boxed{P_2=\operatorname{diag}(1,0,0,1)}
\]

on the ordered tensor-product helicity basis

\[
\{|++\rangle,|+-\rangle,|-+\rangle,|--\rangle\}.
\]

RFG34 extends this to the three two-particle pairings of the external `(--++)` sector. MHV support gives

\[
\boxed{s:\;(-,-)},
\qquad
\boxed{t,u:\;(+,-),(-,+)}.
\]

Thus the `s`-channel cut is already matched-spin-two on this helicity surface, while `t/u` contain the RFG32 mixed tensor-product sector. There,

\[
\boxed{\mathcal C_{raw}-\mathcal C_{projected}=2x_Ax_B}.
\]

The projector commutes with copy exchange, simultaneous helicity reversal, and admissible state-coordinate relabelings preserving the matched/crossed decomposition.

## Open firewalls

```text
RFG35 vector-polarization projected-cut Ward audit
projected loop-integrand realization
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
