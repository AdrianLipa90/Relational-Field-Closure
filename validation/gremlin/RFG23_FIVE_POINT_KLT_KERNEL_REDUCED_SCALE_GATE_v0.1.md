# RFG23 — Five-Point KLT Kernel / Reduced-Scale Gate

Status: `FIVE_POINT_KLT_MATRIX_PASS / TWO_TERM_KLT_EQUIVALENCE_PASS / PURE_SPIN2_LITTLE_GROUP_PASS / REDUCED_SCALE_PREFactor_HOLONOMY_PASS / FULL_PROJECT_FIVE_POINT_NUMERATORS_OPEN`

RFG23 consumes RFG22 and the RFG7/RFG17 reduced gravity-scale spine. It advances the higher-point gravity side from a five-point BCJ basis to an explicit `2 x 2` KLT bilinear while keeping direct project five-point numerator construction separately gated.

## 1. Five-point BCJ basis

RFG22 reduces the color-ordered tree basis to

\[
\boxed{(5-3)!=2.}
\]

Use the left basis

\[
\mathbf A_L=
\begin{pmatrix}
A(1,2,3,4,5)\\
A(1,3,2,4,5)
\end{pmatrix}
\]

and the right basis

\[
\mathbf A_R=
\begin{pmatrix}
\widetilde A(1,2,3,5,4)\\
\widetilde A(1,3,2,5,4)
\end{pmatrix}.
\]

## 2. Five-point KLT kernel

Define

\[
\boxed{
S_5=
\begin{pmatrix}
s_{12}(s_{13}+s_{23}) & s_{12}s_{13}\\
s_{12}s_{13} & s_{13}(s_{12}+s_{23})
\end{pmatrix}.
}
\]

The stripped gravity core is

\[
\boxed{\mathcal C_5^{KLT}=\mathbf A_L^T S_5\mathbf A_R.}
\]

The kernel is symmetric and its determinant factorizes exactly:

\[
\boxed{
\det S_5
=s_{12}s_{13}s_{23}(s_{12}+s_{13}+s_{23}).
}
\]

Thus the KLT kernel itself carries an explicit factorization/singularity signature on the corresponding massless channels.

## 3. Two-term KLT representation

With the amplitude orientation used in the executable gate, the same core is

\[
\boxed{
\mathcal C_5^{KLT}
=-\Big[
 s_{12}s_{34}A(1,2,3,4,5)\widetilde A(2,1,4,3,5)
+s_{13}s_{24}A(1,3,2,4,5)\widetilde A(3,1,4,2,5)
\Big].
}
\]

The sign is fixed by the chosen stripped-amplitude ordering convention. The executable gate checks equality of the matrix and two-term forms for independent left/right helicity choices.

## 4. Left/right copy symmetry

Because

\[
S_5^T=S_5,
\]

the bilinear obeys

\[
\boxed{
\mathbf A_L^T S_5\mathbf A_R
=
\mathbf A_R^T S_5\mathbf A_L.
}
\]

This is checked numerically on independent MHV helicity assignments.

## 5. Pure spin-2 little-group gate at five points

For matching helicities in the two Yang–Mills copies, each external state is in the RFG18/RFG19 pure spin-2 branch. Under

\[
\lambda_i\to z\lambda_i,
\qquad
\widetilde\lambda_i\to z^{-1}\widetilde\lambda_i,
\]

a helicity-`h` gravity amplitude must scale as

\[
\boxed{\mathcal M\to z^{-2h}\mathcal M.}
\]

The executable five-point KLT core verifies weight `+4` for a negative-helicity graviton and weight `-4` for a positive-helicity graviton, i.e. the doubled Yang–Mills little-group weight.

## 6. Five-point gravity coupling prefactor

At five points the double-copy coupling power is

\[
\boxed{
\left(\frac{\kappa_g}{2}\right)^{5-2}
=\left(\frac{\kappa_g}{2}\right)^3.
}
\]

RFG7 gives

\[
\bar M_G=\frac{2}{\kappa_g},
\]

so

\[
\boxed{
\left(\frac{\kappa_g}{2}\right)^3
=\frac1{\bar M_G^3}.
}
\]

Using RF-N1C3,

\[
\boxed{
\frac1{\bar M_G^3}
=\frac1{(M_HT_H)^{3/2}}.
}
\]

On the local carrier candidate surface

\[
\bar M_G=\frac{\alpha_c\omega_Q}{2\Gamma_{DC}},
\]

therefore

\[
\boxed{
\left(\frac{\kappa_g}{2}\right)^3
=
\left(\frac{2\Gamma_{DC}}{\alpha_c\omega_Q}\right)^3.
}
\]

This is the five-point extension of the RFG17 G-free coupling holonomy.

## 7. Executable validation

The reference test checks:

1. `S5` is symmetric and `det S5=s12 s13 s23 (s12+s13+s23)`;
2. matrix KLT equals the two-term five-point KLT representation on 450 random left/right helicity samples;
3. the KLT bilinear is symmetric under exchange of the two copies;
4. pure spin-2 little-group weights are doubled to `+/-4`;
5. `(kappa_g/2)^3=1/Mbar_G^3=kappa_E/Mbar_G`;
6. horizon and local-carrier forms of the five-point prefactor agree algebraically.

Local result:

```text
6 passed, 0 failed
```

## 8. Advancement

```text
RFG22 five-point BCJ basis / soft factorization       PASS REFERENCE
five-point KLT 2x2 kernel                             PASS
kernel determinant factorization                      PASS EXACT
matrix KLT <-> two-term KLT                           PASS REFERENCE
five-point pure spin-2 little-group weight            PASS
five-point reduced-scale coupling holonomy            PASS EXACT
full project five-point cubic/quartic assembly         OPEN
full 15-graph project numerator set                    OPEN
five-point direct BCJ double-copy from project graphs  NEXT HARD FRONTIER
```

RFG23 establishes the higher-point KLT and coupling surface, while keeping the direct project five-point graph/numerator promotion explicitly separate.