# RFG26 — Project Five-Point KLT Gravity Gate

Status: `DIRECT_PROJECT_FIVE_POINT_KLT_CORE_PASS / LEFT_RIGHT_GRAVITY_WARD_PASS / COPY_EXCHANGE_PASS / QUARTIC_PROPAGATION_FIREWALL_PASS / OVERALL_NORMALIZATION_OPEN_RFG27`

RFG26 consumes the direct project five-point Yang–Mills amplitudes of RFG25 and the five-point KLT kernel of RFG24. It promotes the five-point gravity **core** from reference input to a bilinear built from two independently evaluated project Berends–Giele copies. The overall project-to-Einstein normalization is intentionally represented by an explicit coordinate and is fixed only by RFG27.

## 1. Project KLT core

For two independently evaluated project copies,

\[
\mathbf A_L^{project}=\begin{pmatrix}A^{BG}(1,2,3,4,5)\\A^{BG}(1,3,2,4,5)\end{pmatrix},\qquad
\mathbf A_R^{project}=\begin{pmatrix}\widetilde A^{BG}(1,2,3,5,4)\\\widetilde A^{BG}(1,3,2,5,4)\end{pmatrix},
\]

define

\[
\boxed{\mathcal C_5^{project}=\mathbf A_L^{project\,T}S_5\mathbf A_R^{project}}.
\]

The same core is independently reconstructed in the two-term KLT ordering convention.

## 2. Overall normalization coordinate

RFG24 supplies the reduced-scale coordinate

\[
P_5:=\left(\frac{\kappa_g}{2}\right)^3=\frac1{\bar M_G^3}=\frac{\kappa_E}{\bar M_G}.
\]

Write the physical project amplitude as

\[
\boxed{\mathcal M_5^{project}=\zeta_5\,P_5\,\mathcal C_5^{project}},
\]

where the dimensionless complex normalization coordinate `zeta_5` carries the remaining convention-dependent phase/magnitude. RFG27 determines `zeta_5` against an independent five-point normalization witness and the already normalized four-point Einstein surface.

## 3. Gravitational Ward gate

Replacing any one external polarization by its momentum in the left project copy kills the KLT core. The same holds independently in the right copy. These tests are independent of `zeta_5`.

## 4. Copy exchange

\[
\boxed{\mathcal C_5^{project}[L,R]=\mathcal C_5^{project}[R,L]}.
\]

## 5. Quartic-contact propagation firewall

RFG25 establishes that the project five-point Yang–Mills Ward gate requires the inherited quartic contribution. RFG26 verifies that removing that contribution in one copy propagates into order-one gravitational Ward defects, whereas the admitted cubic/quartic layer preserves the KLT Ward gate.

## 6. Executable validation

The byte-preserved reference test verifies:

1. matrix KLT equals the independent two-term project KLT core;
2. all five left-copy Ward replacements vanish;
3. all five right-copy Ward replacements vanish;
4. copy exchange symmetry;
5. the quartic-contact propagation firewall;
6. the algebraic reduced-scale identity `P5=1/Mbar_G^3=kappa_E/Mbar_G`.

Recorded result:

```text
6 passed, 0 failed
```

The executable result admits the KLT core and scale coordinate. The overall coefficient `zeta_5` is the next normalization frontier.

## 7. Advancement

```text
RFG24 five-point KLT kernel                          PASS
RFG25 direct project five-point Yang-Mills          PASS
RFG26 project BG x BG KLT core                      PASS
RFG26 left/right gravitational Ward                 PASS
RFG26 quartic propagation firewall                  PASS
RFG26 reduced-scale coordinate P5                   PASS ALGEBRAIC
project-to-Einstein normalization zeta_5            OPEN RFG27
five-point multi-particle pole residue audit         AFTER RFG27
explicit 15-cubic-graph BCJ numerator representation OPEN
```
