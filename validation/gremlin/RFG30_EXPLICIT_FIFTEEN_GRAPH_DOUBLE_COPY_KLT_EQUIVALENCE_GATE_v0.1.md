# RFG30 — Explicit Fifteen-Graph Double-Copy / KLT Equivalence Gate

Status: `FIFTEEN_GRAPH_DOUBLE_COPY_KLT_EQUIVALENCE_PASS / GRAPH_KLT_ORIENTATION_MINUS_PASS / GENERALIZED_GAUGE_INVARIANCE_PASS / LEFT_RIGHT_WARD_PASS / COPY_EXCHANGE_PASS / S12_RESIDUE_AND_PROJECT_NORMALIZATION_PASS`

RFG30 consumes the explicit five-point BCJ graph representation of RFG29 and the KLT/project normalization spine RFG24–RFG28. It compares two independently polarized project numerator copies graph by graph against the admitted five-point KLT bilinear.

## 1. Fifteen-graph double-copy core

For the RFG29 numerators define

\[
\boxed{\mathcal C_{5,15g}^{project}=\sum_{g=1}^{15}\frac{n_g\widetilde n_g}{D_g}}.
\]

With `n=B m`, `F=B^T D^{-1}B`, this is

\[
\boxed{\mathcal C_{5,15g}^{project}=m_L^T F m_R}.
\]

## 2. Orientation-locked KLT equivalence

The DDM graph orientation of RFG29 and the KLT ordering convention of RFG24/RFG26 are related by

\[
\boxed{\mathcal C_{5,15g}^{project}=-\mathcal C_{5,KLT}^{project}}.
\]

Since RFG27 gives `C5_project=4 C5_BG`, equivalently

\[
\boxed{\mathcal C_{5,15g}^{project}=-4\mathcal C_5^{BG}}.
\]

The sign is fixed by the frozen graph/DDM orientation; the executable gate verifies it on independent left/right project polarization copies.

## 3. Generalized-gauge invariance

Let

\[
m_L\to m_L+\delta_L,\qquad m_R\to m_R+\delta_R,
\]

with

\[
F\delta_L=F\delta_R=0.
\]

Then

\[
(m_L+\delta_L)^T F(m_R+\delta_R)=m_L^T Fm_R.
\]

RFG30 samples the four-dimensional null space of the rank-two `F5` matrix and verifies the graph double-copy core is invariant under independent left/right null-space shifts.

## 4. Ward and copy-exchange gates

For each external leg, replacing the polarization in either numerator copy by the corresponding momentum gives

\[
\boxed{\mathcal C_{5,15g}^{project}|_{L:\varepsilon_i\to p_i}=0},
\qquad
\boxed{\mathcal C_{5,15g}^{project}|_{R:\widetilde\varepsilon_i\to p_i}=0}.
\]

The bilinear also obeys

\[
\boxed{\mathcal C_{5,15g}^{project}[L,R]=\mathcal C_{5,15g}^{project}[R,L]}.
\]

## 5. Non-soft residue

On the RFG28 `s12` factorization family,

\[
\boxed{
\operatorname*{Res}_{s_{12}=0}\mathcal C_{5,15g}^{project}
=-4\operatorname*{Res}_{s_{12}=0}\mathcal C_5^{BG}.
}
\]

Using RFG29,

\[
\boxed{
\operatorname*{Res}\mathcal C_{5,15g}^{project}
=-4(s_{13}+s_{23})(N_{12}\cdot J_4)(\widetilde N_{12}\cdot\widetilde J_4).
}
\]

## 6. Physical project amplitude

RFG27 fixed the KLT-oriented form

\[
\mathcal M_5^{project}=-\frac{i}{4}P_5\mathcal C_{5,KLT}^{project},
\qquad P_5=(\kappa_g/2)^3=1/\bar M_G^3.
\]

Therefore the equivalent graph-oriented form is

\[
\boxed{
\mathcal M_5^{project}=+\frac{i}{4}P_5\mathcal C_{5,15g}^{project}.
}
\]

This reproduces the same physical amplitude and the RFG28 normalized pole residue.

## 7. Executable validation

Fresh live-surface result:

```text
6 passed, 0 failed
```

The reference gate verifies graph/KLT equivalence, independent generalized-gauge shifts, all five Ward replacements in either copy, copy exchange, the `s12` residue, and reduced-scale physical normalization.

## 8. Advancement

```text
explicit 15-graph project BCJ numerators                 PASS RFG29
15-graph double-copy core                                PASS
15-graph <-> KLT project equivalence                     PASS WITH FROZEN ORIENTATION SIGN
independent generalized-gauge invariance                 PASS
left/right gravitational Ward                            PASS
non-soft graph residue                                   PASS
project physical normalization                           PASS
internal-state tree factorization / pure-spin2 audit     NEXT RFG31
loop internal-state spectrum audit                       FOLLOWING FRONTIER
```
