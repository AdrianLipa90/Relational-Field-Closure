# RFG25 — Project Five-Point KLT Gravity Gate

Status: `DIRECT_PROJECT_FIVE_POINT_KLT_PASS / LEFT_RIGHT_GRAVITY_WARD_PASS / COPY_EXCHANGE_PASS / QUARTIC_PROPAGATION_FIREWALL_PASS / REDUCED_SCALE_PREFactor_PASS`

RFG25 consumes the direct project five-point Yang–Mills amplitudes of RFG24 and the five-point KLT kernel of RFG23. It promotes the five-point gravity side from MHV reference input to a bilinear built from two independently evaluated project Berends–Giele copies.

## 1. Project BCJ bases

For each independently chosen project polarization copy define

\[
\mathbf A_L^{project}=
\begin{pmatrix}
A^{BG}(1,2,3,4,5)\\
A^{BG}(1,3,2,4,5)
\end{pmatrix},
\]

\[
\mathbf A_R^{project}=
\begin{pmatrix}
\widetilde A^{BG}(1,2,3,5,4)\\
\widetilde A^{BG}(1,3,2,5,4)
\end{pmatrix}.
\]

Each entry is computed directly from the RFG24 recursion using the RFG8 cubic and RFG13 quartic relative normalization.

## 2. Five-point project KLT core

Using the RFG23 kernel

\[
S_5=
\begin{pmatrix}
s_{12}(s_{13}+s_{23}) & s_{12}s_{13}\\
s_{12}s_{13} & s_{13}(s_{12}+s_{23})
\end{pmatrix},
\]

define

\[
\boxed{
\mathcal C_5^{project}
=\mathbf A_L^{project\,T}S_5\mathbf A_R^{project}.
}
\]

The corresponding gravity amplitude is

\[
\boxed{
\mathcal M_5^{project}
=i\left(\frac{\kappa_g}{2}\right)^3\mathcal C_5^{project}.
}
\]

## 3. Independent two-term KLT reconstruction

The same direct project amplitude is evaluated independently as

\[
\boxed{
\mathcal C_5^{project}
=-\Big[
 s_{12}s_{34}A^{BG}(1,2,3,4,5)\widetilde A^{BG}(2,1,4,3,5)
+s_{13}s_{24}A^{BG}(1,3,2,4,5)\widetilde A^{BG}(3,1,4,2,5)
\Big].
}
\]

The executable gate verifies equality of the matrix and two-term constructions on independently randomized project polarization copies.

## 4. Five-leg gravitational Ward gate

For every external leg `i`, the left-copy deformation

\[
\varepsilon_i\to p_i
\]

kills every relevant left project partial amplitude, hence

\[
\boxed{\mathcal C_5^{project}|_{L:\varepsilon_i\to p_i}=0.}
\]

The same is checked independently in the right copy:

\[
\boxed{\mathcal C_5^{project}|_{R:\widetilde\varepsilon_i\to p_i}=0.}
\]

The executable reference evaluates both statements over deterministic random `2 -> 3` kinematics for all five external legs.

## 5. Copy-exchange symmetry

With the admitted project amplitudes satisfying their BCJ/ordered-amplitude identities, exchanging the two independent copies leaves the KLT result invariant:

\[
\boxed{\mathcal C_5^{project}[L,R]=\mathcal C_5^{project}[R,L].}
\]

## 6. Quartic-contact propagation firewall

RFG24 showed that the direct five-point Yang–Mills Ward identity requires the RFG13 quartic contact normalization. RFG25 verifies that this requirement propagates through the KLT construction.

If the quartic contribution is removed in one copy while the other copy remains admitted, replacing an external polarization by its momentum produces order-one gravitational Ward defects. With the admitted quartic coefficient, the same defects collapse to numerical zero.

Thus five-point gravity gauge consistency is sensitive to the same project cubic/quartic relative normalization that closed RFG14 and RFG24.

## 7. Reduced-scale coupling

RFG7 gives

\[
\bar M_G=\frac{2}{\kappa_g},
\]

so the project five-point gravity prefactor is

\[
\boxed{
\left(\frac{\kappa_g}{2}\right)^3
=\frac1{\bar M_G^3}
=\frac{\kappa_E}{\bar M_G}.
}
\]

With RF-N1C3,

\[
\boxed{
\left(\frac{\kappa_g}{2}\right)^3
=\frac1{(M_HT_H)^{3/2}}.
}
\]

## 8. Executable validation

The reference test checks:

1. direct project KLT matrix equals the independent two-term five-point KLT form;
2. all five left-copy gravitational Ward replacements vanish;
3. all five right-copy gravitational Ward replacements vanish;
4. exchange of the two project copies leaves the KLT core invariant;
5. removing the quartic contact in one copy destroys gravitational Ward closure;
6. the five-point gravity coupling is `1/Mbar_G^3=kappa_E/Mbar_G`.

Local result:

```text
6 passed, 0 failed
```

## 9. Advancement

```text
RFG24 direct project five-point Yang-Mills           PASS
RFG24 project five-point fundamental BCJ             PASS
RFG23 five-point KLT kernel                          PASS
project BG x BG five-point KLT                       PASS
five-leg gravitational Ward in left copy             PASS
five-leg gravitational Ward in right copy            PASS
quartic-contact propagation into gravity             PASS
five-point reduced-scale prefactor                    PASS
explicit 15-cubic-graph BCJ numerator representation OPEN
five-point multi-particle pole residue audit          NEXT
internal-state / loop spectrum                        OPEN
```

RFG25 establishes a direct project five-point KLT gravity amplitude without using a gravity target to construct the Yang–Mills inputs.