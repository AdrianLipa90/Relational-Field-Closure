# RFG24 — Project Five-Point Berends–Giele / BCJ Gate

Status: `DIRECT_PROJECT_FIVE_POINT_YM_ASSEMBLY_PASS / FIVE_LEG_WARD_PASS / FUNDAMENTAL_BCJ_PASS / REFLECTION_AND_DECOUPLING_PASS / RFG26_PROJECT_NORMALIZATION_BOUND`

RFG24 assembles the five-point Yang–Mills amplitude directly from the project cubic/quartic interaction layer and now consumes the explicit normalization bridge supplied by RFG26.

## 1. Project-current normalization

The ordered Berends–Giele brackets are

\[
[J_X,J_Y]^\mu
=(k_Y\!\cdot J_X)J_Y^\mu
+\frac12 k_X^\mu(J_X\!\cdot J_Y)
-(k_X\!\cdot J_Y)J_X^\mu
-\frac12 k_Y^\mu(J_X\!\cdot J_Y),
\]

and

\[
\{J_X,J_Y,J_Z\}^\mu
=(J_X\!\cdot J_Z)J_Y^\mu
-\frac12(J_X\!\cdot J_Y)J_Z^\mu
-\frac12(J_Y\!\cdot J_Z)J_X^\mu.
\]

RFG26 compares this recursion directly with the admitted RFG15 four-point project amplitude. The previously used stripped-current coefficients

\[
\sqrt2:1
\]

produce exactly one half of the RFG15 project partial amplitude at four points. The project-consistent coefficients are therefore

\[
\boxed{2:2},
\]

which are obtained by the common interaction normalization rescaling

\[
c=\sqrt2,\qquad
V_3\mapsto cV_3,\qquad
V_4\mapsto c^2V_4.
\]

The gauge-coupling coordinate remains fixed at

\[
\boxed{g_{YM}^2=1/\alpha_c}.
\]

Thus the project current recursion used here is

\[
\boxed{
P^2J_P^\mu
=2\sum_{XY=P}[J_X,J_Y]^\mu
+2\sum_{XYZ=P}\{J_X,J_Y,J_Z\}^\mu.
}
\]

## 2. Direct five-point project amplitude

For each ordering \(\sigma\),

\[
\boxed{A_5^{BG,project}(\sigma)}
\]

is evaluated directly from the corrected recursion. The physical gauge amplitude is

\[
\boxed{\mathcal A_5^{project}=g_{YM}^3 A_5^{BG,project}}.
\]

RFG26 verifies the exact tree-scaling relation

\[
A_4^{BG,project}=2A_4^{BG,base},
\qquad
A_5^{BG,project}=2\sqrt2\,A_5^{BG,base},
\]

and the four-point bridge

\[
\boxed{A_4^{BG,project}=A_4^{RFG15}}.
\]

## 3. Five-leg Ward gate

For each external leg,

\[
\varepsilon_i\to p_i
\]

gives

\[
\boxed{A_5^{BG,project}|_{\varepsilon_i\to p_i}=0}.
\]

The corrected common interaction normalization leaves the Ward closure intact.

## 4. Direct five-point BCJ relation

The direct project amplitudes satisfy

\[
\boxed{
0=s_{12}A(1,2,3,4,5)
+(s_{12}+s_{23})A(1,3,2,4,5)
+(s_{12}+s_{23}+s_{24})A(1,3,4,2,5).
}
\]

RFG23 supplies the independent five-point MHV BCJ/soft reference; RFG24 supplies the direct project-current realization.

## 5. Ordered-amplitude identities

The direct amplitudes satisfy

\[
\boxed{A(1,2,3,4,5)=-A(5,4,3,2,1)}
\]

and the insertion/decoupling identity

\[
\boxed{
A(1,2,3,4,5)+A(2,1,3,4,5)+A(2,3,1,4,5)+A(2,3,4,1,5)=0.
}
\]

## 6. Quartic firewall

With the admitted cubic coefficient fixed at `2`, removing the quartic contribution while leaving the cubic recursion unchanged breaks five-leg Ward closure. Restoring the project-consistent quartic coefficient `2` restores numerical zero.

This preserves the same cubic/quartic action genealogy established by RFG8/RFG13 while making the stripped-current normalization consistent with RFG15/RFG20.

## 7. Executable validation

The reference test checks:

1. masslessness, momentum conservation and transversality;
2. all five single-leg Ward identities;
3. the direct fundamental five-point BCJ relation;
4. reflection and insertion/decoupling identities;
5. the quartic-contact firewall;
6. \(g_{YM}^3\) coupling power.

Corrected local result:

```text
6 passed, 0 failed
```

RFG26 independently checks the normalization bridge in six additional tests.

## 8. Advancement

```text
RFG23 five-point BCJ/soft reference                 PASS REFERENCE
RFG24 direct project five-point BG assembly         PASS
RFG24 five-leg Ward / BCJ                           PASS
RFG26 four-point BG -> RFG15 normalization bridge   PASS
RFG25 project five-point KLT gravity                PASS CORRECTED
explicit 15-cubic-graph project numerator set       OPEN
five-point multi-particle pole residue audit         NEXT
```
