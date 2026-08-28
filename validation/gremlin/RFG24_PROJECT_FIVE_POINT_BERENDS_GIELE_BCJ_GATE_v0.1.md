# RFG24 — Project Five-Point Berends–Giele / BCJ Gate

Status: `DIRECT_PROJECT_FIVE_POINT_YM_ASSEMBLY_PASS / FIVE_LEG_WARD_PASS / FUNDAMENTAL_BCJ_PASS / REFLECTION_AND_DECOUPLING_PASS / QUARTIC_NORMALIZATION_FIREWALL_PASS`

RFG24 closes the main admission gap left open by RFG22/RFG23: the five-point Yang–Mills amplitude is assembled directly from the same project cubic and quartic interaction normalization used at four points, rather than imported from the MHV closed form.

## 1. Ordered project currents

The color-ordered Berends–Giele current uses the cubic bracket

\[
[J_X,J_Y]^\mu
=(k_Y\cdot J_X)J_Y^\mu
+\frac12 k_X^\mu(J_X\cdot J_Y)
-(k_X\cdot J_Y)J_X^\mu
-\frac12 k_Y^\mu(J_X\cdot J_Y),
\]

and the quartic bracket

\[
\{J_X,J_Y,J_Z\}^\mu
=(J_X\cdot J_Z)J_Y^\mu
-\frac12(J_X\cdot J_Y)J_Z^\mu
-\frac12(J_Y\cdot J_Z)J_X^\mu.
\]

With the RFG8/RFG13 color-ordered normalization, the current recursion is

\[
\boxed{
P^2 J_P^\mu
=\sqrt2\sum_{XY=P}[J_X,J_Y]^\mu
+\sum_{XYZ=P}\{J_X,J_Y,J_Z\}^\mu.
}
\]

The relative `sqrt(2) : 1` normalization is fixed by the same stripped color-ordered cubic and quartic vertices; it is not tuned to the five-point output.

The final external propagator is amputated before contraction with the fifth polarization.

## 2. Direct five-point project amplitude

For each ordering `sigma`, define

\[
\boxed{A_5^{BG}(\sigma)}
\]

by the recursive current above. The executable gate uses real `2 -> 3` massless kinematics written in the all-outgoing convention and random physical transverse polarizations.

The physical project coupling is then

\[
\boxed{\mathcal A_5^{project}=g_{YM}^3 A_5^{BG},\qquad g_{YM}^2=1/\alpha_c.}
\]

## 3. Five-leg Ward gate

For every external leg `i`, the reference test replaces

\[
\varepsilon_i\to p_i
\]

and verifies

\[
\boxed{A_5^{BG}|_{\varepsilon_i\to p_i}=0}
\]

on 180 deterministic random `2 -> 3` configurations.

This is a direct project gauge-invariance test of the complete five-point recursion.

## 4. Direct project fundamental BCJ relation

Using the project amplitudes themselves, RFG24 verifies

\[
\boxed{
0=
 s_{12}A_5^{BG}(1,2,3,4,5)
 +(s_{12}+s_{23})A_5^{BG}(1,3,2,4,5)
 +(s_{12}+s_{23}+s_{24})A_5^{BG}(1,3,4,2,5).
}
\]

No gravity amplitude and no Parke–Taylor value are used in this test.

## 5. Ordered-amplitude identities

The same project recursion verifies the five-point reflection identity

\[
\boxed{A(1,2,3,4,5)=-A(5,4,3,2,1)}
\]

and the photon-decoupling / insertion identity

\[
\boxed{
A(1,2,3,4,5)+A(2,1,3,4,5)+A(2,3,1,4,5)+A(2,3,4,1,5)=0.
}
\]

## 6. Quartic-normalization firewall

The quartic bracket is inherited from RFG13. Setting its relative coefficient to zero while leaving the cubic recursion untouched gives large five-leg Ward defects, whereas the admitted coefficient gives numerical zero.

Thus the same quartic contact that was required by RFG14 at four points remains required by direct project gauge invariance at five points.

## 7. Executable validation

The reference test checks:

1. masslessness, total momentum conservation and transversality for project `2 -> 3` states;
2. all five single-leg Ward identities on 180 random configurations;
3. the fundamental five-point BCJ relation on 220 direct project amplitudes;
4. reflection and photon-decoupling identities on 150 configurations;
5. adversarial removal of the quartic contact breaks Ward closure;
6. project coupling power `A5_project ~ g_YM^3` with `g_YM^2=1/alpha_c`.

Local result:

```text
6 passed, 0 failed
```

## 8. Advancement

```text
RFG8 project cubic vertex                          PASS
RFG13 project quartic normalization                 PASS
RFG14 direct project four-point amplitude           PASS
RFG22 five-point BCJ/soft reference                 PASS
RFG23 five-point KLT reference                      PASS
project five-point Berends-Giele assembly           PASS
five-leg project Ward identities                    PASS
project five-point fundamental BCJ                  PASS
five-point project KLT from two BG copies           NEXT
explicit 15-cubic-graph project numerator set       OPEN
```

RFG24 promotes the five-point Yang–Mills side from reference-only to direct project amplitude status.