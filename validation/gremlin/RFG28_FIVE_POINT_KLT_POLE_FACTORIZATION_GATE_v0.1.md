# RFG28 — Five-Point KLT Pole-Factorization Gate

Status: `COMPLEX_S12_FACTOR_FAMILY_PASS / SIMPLE_GRAVITY_POLE_PASS / DOUBLE_POLE_CANCELLATION_PASS / RANK_ONE_KLT_RESIDUE_FACTORIZATION_PASS / PROJECT_RESIDUE_NORMALIZATION_PASS_RFG27`

RFG28 consumes the RFG23–RFG27 higher-point spine and audits a genuine non-soft factorization channel. It approaches the two-particle invariant

\[
\boxed{s_{12}\to0}
\]

on exactly momentum-conserving complex massless kinematics while keeping the five-point KLT basis explicit.

## 1. Factorization family

Choose

\[
\lambda_2=\lambda_1+\varepsilon\chi
\]

with generic anti-holomorphic spinors for legs 1,2,3. The final two anti-holomorphic spinors are re-solved at every `epsilon` so

\[
\sum_{i=1}^{5}\lambda_i\widetilde\lambda_i=0.
\]

Then

\[
\boxed{s_{12}=\langle12\rangle[21]=O(\varepsilon)}.
\]

The MHV witness uses negative helicities on legs 1 and 3 so the selected ordering has a nonzero factorization residue.

## 2. KLT basis near the pole

Use

\[
\mathbf A_L=(A_{12345},A_{13245})^T,\qquad
\mathbf A_R=(\widetilde A_{12354},\widetilde A_{13254})^T.
\]

Along the family,

\[
A_{12345}\sim\frac{R_L^{YM}}{s_{12}},\qquad
\widetilde A_{12354}\sim\frac{R_R^{YM}}{s_{12}},
\]

while the second basis entries remain finite.

The KLT kernel has

\[
S_{11}=s_{12}(s_{13}+s_{23}),\qquad S_{12}=s_{12}s_{13}.
\]

Thus the kernel removes one power of the apparent product pole.

## 3. Simple gravity pole

The executable gate verifies

\[
\boxed{\mathcal C_5^{BG}\sim\frac1{s_{12}}},\qquad
\boxed{s_{12}^2\mathcal C_5^{BG}\to0}.
\]

Therefore the admitted five-point KLT core carries a simple massless factorization pole on this channel.

## 4. Rank-one residue factorization

Define the two Yang–Mills residues

\[
R_L^{YM}=\lim_{s_{12}\to0}s_{12}A_{12345},\qquad
R_R^{YM}=\lim_{s_{12}\to0}s_{12}\widetilde A_{12354}.
\]

RFG28 verifies

\[
\boxed{
\operatorname*{Res}_{s_{12}=0}\mathcal C_5^{BG}
=(s_{13}+s_{23})R_L^{YM}R_R^{YM}.
}
\]

The `S12` cross contribution and the finite `S22` contribution vanish after multiplication by `s12`. The residue therefore becomes rank one in the two-dimensional BCJ/KLT basis.

## 5. Project and physical residue

RFG27 gives

\[
\mathcal C_5^{project}=4\mathcal C_5^{BG},
\qquad
\mathcal M_5^{project}=-\frac{i}{4}P_5\mathcal C_5^{project},
\qquad
P_5=\left(\frac{\kappa_g}{2}\right)^3.
\]

Hence

\[
\boxed{\operatorname*{Res}\mathcal M_5^{project}=-iP_5\operatorname*{Res}\mathcal C_5^{BG}}.
\]

This is the normalized five-point pole residue on the same RFG27 project surface.

## 6. Executable validation

Fresh local result:

```text
6 passed, 0 failed
```

The tests verify exact masslessness/conservation, linear `s12`, Yang–Mills pole/finite basis separation, simple rather than double KLT pole, rank-one residue factorization over 30 deterministic random families, decoupling of cross/finite KLT terms from the residue, and the RFG27 project/physical normalization map.

## 7. Advancement

```text
RFG27 five-point project normalization              PASS
RFG28 non-soft s12 factorization family              PASS
RFG28 simple gravity pole                            PASS
RFG28 rank-one KLT residue factorization             PASS
RFG28 physical residue normalization                 PASS
explicit 15-cubic-graph project BCJ numerators       NEXT RFG29
explicit 3pt x 4pt project-current residue expansion OPEN RFG29
internal-state / loop spectrum                       OPEN
```
