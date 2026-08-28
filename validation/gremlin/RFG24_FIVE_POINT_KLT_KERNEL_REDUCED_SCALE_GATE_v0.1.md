# RFG24 — Five-Point KLT Kernel / Reduced-Scale Gate

Status: `FIVE_POINT_KLT_MATRIX_PASS / TWO_TERM_KLT_EQUIVALENCE_PASS / PURE_SPIN2_LITTLE_GROUP_PASS / REDUCED_SCALE_COORDINATE_PASS / PROJECT_PREFactor_ADMISSION_OPEN_RFG27`

RFG24 consumes the RFG23 five-point BCJ/soft reference and the RFG7/RFG17 reduced-gravity-scale spine. It advances the higher-point gravity side from the two-amplitude BCJ basis to an explicit `2 x 2` KLT bilinear. The KLT core and reduced-scale coordinate are admitted here; attachment of an overall physical project-amplitude coefficient is independently gated by RFG27.

## 1. Five-point BCJ basis

RFG23 establishes the basis size

\[
\boxed{(5-3)!=2}.
\]

Use

\[
\mathbf A_L=\begin{pmatrix}A(1,2,3,4,5)\\A(1,3,2,4,5)\end{pmatrix},\qquad
\mathbf A_R=\begin{pmatrix}\widetilde A(1,2,3,5,4)\\\widetilde A(1,3,2,5,4)\end{pmatrix}.
\]

## 2. KLT kernel

\[
\boxed{S_5=\begin{pmatrix}
s_{12}(s_{13}+s_{23}) & s_{12}s_{13}\\
s_{12}s_{13} & s_{13}(s_{12}+s_{23})
\end{pmatrix}}
\]

and

\[
\boxed{\mathcal C_5^{KLT}=\mathbf A_L^T S_5\mathbf A_R}.
\]

The determinant factorizes exactly,

\[
\boxed{\det S_5=s_{12}s_{13}s_{23}(s_{12}+s_{13}+s_{23})}.
\]

The same core is reproduced by the frozen two-term ordering convention

\[
\boxed{\mathcal C_5^{KLT}=-\left[s_{12}s_{34}A(1,2,3,4,5)\widetilde A(2,1,4,3,5)+s_{13}s_{24}A(1,3,2,4,5)\widetilde A(3,1,4,2,5)\right]}.
\]

## 3. Copy exchange and spin-2 little group

Because `S5` is symmetric,

\[
\boxed{\mathbf A_L^T S_5\mathbf A_R=\mathbf A_R^T S_5\mathbf A_L}.
\]

For matching Yang–Mills helicities in the two copies, the KLT core carries the RFG18/RFG19 pure-spin-2 little-group weights `+/-4` at each external leg.

## 4. Reduced-scale coordinate

RFG7 supplies

\[
\bar M_G=\frac{2}{\kappa_g}.
\]

Therefore the standard five-point gravity coupling coordinate obeys the exact algebraic identities

\[
\boxed{\left(\frac{\kappa_g}{2}\right)^3=\frac1{\bar M_G^3}=\frac{\kappa_E}{\bar M_G}}.
\]

Using RF-N1C3 and the local carrier candidate surface,

\[
\boxed{\frac1{\bar M_G^3}=\frac1{(M_HT_H)^{3/2}}=\left(\frac{2\Gamma_{DC}}{\alpha_c\omega_Q}\right)^3}.
\]

These are reduced-scale coordinate identities. RFG27 identifies the dimensionless phase/magnitude coefficient that multiplies this coordinate on the direct project five-point KLT amplitude.

## 5. Executable validation

The byte-preserved reference test verifies:

1. symmetry and determinant factorization of `S5`;
2. matrix KLT equals the two-term representation on 450 deterministic left/right samples;
3. copy-exchange symmetry;
4. pure-spin-2 little-group weights `+/-4`;
5. the algebraic reduced-scale identities above;
6. horizon/local-carrier equivalence on the common admitted surface.

Recorded result:

```text
6 passed, 0 failed
```

## 6. Advancement

```text
RFG23 five-point BCJ / soft reference             PASS
RFG24 five-point KLT kernel                       PASS
RFG24 reduced-scale coordinate                    PASS ALGEBRAIC
RFG25 direct project five-point BG/BCJ            DOWNSTREAM PASS
RFG26 direct project five-point KLT core          DOWNSTREAM PASS
project five-point overall normalization          OPEN RFG27
five-point multi-particle pole audit              AFTER RFG27
```
