# RFG24 — Five-Point KLT Kernel / Reduced-Scale Gate

Status: `FIVE_POINT_KLT_MATRIX_PASS / TWO_TERM_KLT_EQUIVALENCE_PASS / PURE_SPIN2_LITTLE_GROUP_PASS / REDUCED_SCALE_COORDINATE_PASS / PROJECT_NORMALIZATION_PASS_RFG27`

RFG24 consumes RFG23 and supplies the five-point `2 x 2` KLT kernel

\[
\boxed{S_5=\begin{pmatrix}s_{12}(s_{13}+s_{23})&s_{12}s_{13}\\s_{12}s_{13}&s_{13}(s_{12}+s_{23})\end{pmatrix}},
\]

with

\[
\boxed{\det S_5=s_{12}s_{13}s_{23}(s_{12}+s_{13}+s_{23})}.
\]

The raw/BG-basis core is

\[
\boxed{\mathcal C_5^{BG}=\mathbf A_L^{BG\,T}S_5\mathbf A_R^{BG}}.
\]

The frozen two-term KLT representation, copy-exchange symmetry and pure-spin-2 little-group weights are executable PASS results.

The reduced-scale coordinate is

\[
\boxed{P_5=\left(\frac{\kappa_g}{2}\right)^3=\frac1{\bar M_G^3}=\frac{\kappa_E}{\bar M_G}=\frac1{(M_HT_H)^{3/2}}}.
\]

RFG27 supplies the project-basis map `A_project=2 A_BG`, hence

\[
\boxed{\mathcal C_5^{project}=4\mathcal C_5^{BG}}
\]

and fixes the physical project coefficient to `-i P5/4`.

Recorded reference result:

```text
6 passed, 0 failed
```
