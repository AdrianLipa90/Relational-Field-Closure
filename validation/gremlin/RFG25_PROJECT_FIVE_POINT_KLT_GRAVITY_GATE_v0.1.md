# RFG25 — Project Five-Point KLT Gravity Gate

Status: `DIRECT_PROJECT_FIVE_POINT_KLT_PASS / LEFT_RIGHT_GRAVITY_WARD_PASS / COPY_EXCHANGE_PASS / QUARTIC_PROPAGATION_FIREWALL_PASS / RFG26_NORMALIZATION_CORRECTED`

RFG25 consumes the direct project five-point Yang–Mills amplitudes of RFG24. RFG23 supplies the admitted two-amplitude BCJ basis and soft-factorization reference; RFG25 constructs and cross-checks the five-point momentum kernel directly.

## 1. Project BCJ bases

Define

\[
\mathbf A_L^{project}
=
\begin{pmatrix}
A^{BG}(1,2,3,4,5)\\
A^{BG}(1,3,2,4,5)
\end{pmatrix},
\qquad
\mathbf A_R^{project}
=
\begin{pmatrix}
\widetilde A^{BG}(1,2,3,5,4)\\
\widetilde A^{BG}(1,3,2,5,4)
\end{pmatrix}.
\]

Each entry uses the RFG24/RFG26 project-consistent current normalization

\[
\boxed{V_3^{BG}:V_4^{BG}=2:2}.
\]

## 2. Five-point project KLT core

On the two-amplitude BCJ basis define

\[
S_5=
\begin{pmatrix}
s_{12}(s_{13}+s_{23}) & s_{12}s_{13}\\
s_{12}s_{13} & s_{13}(s_{12}+s_{23})
\end{pmatrix}.
\]

Then

\[
\boxed{
\mathcal C_5^{project}
=\mathbf A_L^{project\,T}S_5\mathbf A_R^{project}.
}
\]

The executable gate independently checks the equivalent two-term KLT form,

\[
\boxed{
\mathcal C_5^{project}
=-\Big[
s_{12}s_{34}A(1,2,3,4,5)\widetilde A(2,1,4,3,5)
+s_{13}s_{24}A(1,3,2,4,5)\widetilde A(3,1,4,2,5)
\Big].
}
\]

## 3. RFG26 normalization transfer

RFG26 proves

\[
A_5^{BG,project}=2\sqrt2\,A_5^{BG,base},
\]

so for two independent copies

\[
\boxed{\mathcal C_5^{project}=8\,\mathcal C_5^{base}}.
\]

The compatible gravity transfer remains the same project-normalized rule identified at four points:

\[
\boxed{g\longrightarrow\kappa_g/4}.
\]

Therefore

\[
\boxed{
\mathcal M_5^{project}
=i\left(\frac{\kappa_g}{4}\right)^3\mathcal C_5^{project}.
}
\]

The earlier combination of the base-normalized `sqrt(2):1` BG core with \((\kappa_g/2)^3\) produced the same physical product, but it did not live on the RFG15/RFG20 project-current normalization surface. RFG26 moves both factors onto one common project convention:

\[
\mathcal C_5^{project}=8\mathcal C_5^{base},
\qquad
\left(\frac{\kappa_g}{4}\right)^3
=\frac18\left(\frac{\kappa_g}{2}\right)^3.
\]

Hence the physical amplitude is preserved exactly.

## 4. Gravitational Ward gate

For each leg, replacing the polarization in either copy by the corresponding momentum gives

\[
\boxed{\mathcal C_5^{project}|_{L:\varepsilon_i\to p_i}=0},
\qquad
\boxed{\mathcal C_5^{project}|_{R:\widetilde\varepsilon_i\to p_i}=0}.
\]

## 5. Copy-exchange symmetry

\[
\boxed{\mathcal C_5^{project}[L,R]=\mathcal C_5^{project}[R,L]}.
\]

## 6. Quartic-contact propagation firewall

RFG24/RFG26 require the project-consistent quartic coefficient `2`. Removing the quartic contribution in one copy while retaining the admitted cubic coefficient produces gravitational Ward defects. With the admitted coefficient the defects vanish.

## 7. Reduced-scale form

Using

\[
\bar M_G=\frac2{\kappa_g},
\qquad
\kappa_E=\frac1{\bar M_G^2},
\]

the corrected project-core coefficient is

\[
\boxed{
\left(\frac{\kappa_g}{4}\right)^3
=\frac1{8\bar M_G^3}
=\frac{\kappa_E}{8\bar M_G}.
}
\]

With RF-N1C3,

\[
\boxed{
\left(\frac{\kappa_g}{4}\right)^3
=\frac1{8(M_HT_H)^{3/2}}.
}
\]

## 8. Executable validation

The corrected reference test checks:

1. KLT matrix = independent two-term KLT;
2. all five left-copy Ward replacements;
3. all five right-copy Ward replacements;
4. copy-exchange symmetry;
5. quartic-contact propagation;
6. \((\kappa_g/4)^3=1/(8\bar M_G^3)=\kappa_E/(8\bar M_G)\).

Corrected local result:

```text
6 passed, 0 failed
```

## 9. Advancement

```text
RFG24 direct project five-point Yang-Mills           PASS
RFG26 project-current normalization bridge           PASS
project BG x BG five-point KLT                       PASS
left/right gravitational Ward                        PASS
quartic-contact propagation                          PASS
project five-point prefactor (kappa_g/4)^3           PASS
physical five-point amplitude vs pre-RFG26 product   UNCHANGED
explicit 15-cubic-graph BCJ numerator representation OPEN
five-point multi-particle pole residue audit          NEXT
internal-state / loop spectrum                        OPEN
```
