# RFG22 — Five-Point BCJ / Soft-Factorization Gate

Status: `FIVE_POINT_MHV_BCJ_REFERENCE_PASS / TWO_AMPLITUDE_BASIS_PASS / CONSERVED_SOFT_FAMILY_FACTORISATION_PASS / PROJECT_COUPLING_SCALING_PASS / FULL_PROJECT_FIVE_POINT_ASSEMBLY_OPEN`

RFG22 advances the RFG14–RFG21 four-point project Yang–Mills / double-copy spine to the first explicit higher-point tree gate. It uses the same normalized Yang–Mills coupling surface `g_YM^2=1/alpha_c` established by RFG4G, but keeps the five-point amplitude construction explicitly typed as an MHV reference until a direct project Berends–Giele / Feynman assembly is admitted.

## 1. Five-point massless kinematics

The executable gate generates complex spinors `(lambda_i, tilde_lambda_i)` with

\[
p_i^{\alpha\dot\alpha}=\lambda_i^\alpha\widetilde\lambda_i^{\dot\alpha},
\qquad p_i^2=0,
\]

and solves the final two anti-holomorphic spinors so that

\[
\boxed{\sum_{i=1}^{5}p_i=0.}
\]

The Mandelstam coordinates are

\[
\boxed{s_{ij}=\langle ij\rangle[ji].}
\]

## 2. MHV color-ordered reference

For the helicity sector `1-,2-,3+,4+,5+`, define the stripped tree amplitude

\[
\boxed{
A_5(\sigma)
=
\frac{\langle12\rangle^4}
{\langle\sigma_1\sigma_2\rangle
 \langle\sigma_2\sigma_3\rangle
 \langle\sigma_3\sigma_4\rangle
 \langle\sigma_4\sigma_5\rangle
 \langle\sigma_5\sigma_1\rangle}.
}
\]

On the project normalization surface the physical five-gluon amplitude scales as

\[
\boxed{\mathcal A_5^{project}=g_{YM}^3 A_5,\qquad g_{YM}=\alpha_c^{-1/2}.}
\]

No new five-point coupling coordinate is introduced.

## 3. Fundamental five-point BCJ relation

The gate verifies

\[
\boxed{
0=
 s_{12}A_5(1,2,3,4,5)
 +(s_{12}+s_{23})A_5(1,3,2,4,5)
 +(s_{12}+s_{23}+s_{24})A_5(1,3,4,2,5).
}
\]

Therefore the third ordering is determined by the first two whenever the final coefficient is nonzero:

\[
\boxed{
A_5(1,3,4,2,5)
=-\frac{s_{12}A_5(1,2,3,4,5)
 +(s_{12}+s_{23})A_5(1,3,2,4,5)}
{s_{12}+s_{23}+s_{24}}.
}
\]

This is the explicit five-point reduction to the expected BCJ basis size

\[
\boxed{(5-3)!=2.}
\]

## 4. Momentum-conserving positive-helicity soft family

A one-parameter family is constructed with

\[
\lambda_5\mapsto\sqrt\varepsilon\,\lambda_5,
\qquad
\widetilde\lambda_5\mapsto\sqrt\varepsilon\,\widetilde\lambda_5,
\]

while two remaining anti-holomorphic spinors are re-solved at each `epsilon` so that five-point momentum conservation remains exact.

For a positive-helicity soft leg between ordered legs `4` and `1`, the gate verifies

\[
\boxed{
A_5(1,2,3,4,5^+)
=
S^+(4,5,1)A_4(1,2,3,4)
}
\]

with

\[
\boxed{
S^+(4,5,1)=
\frac{\langle41\rangle}{\langle45\rangle\langle51\rangle}.
}
\]

Along the conserved soft family,

\[
A_5\sim\varepsilon^{-1}
\]

and the executable witness verifies that

\[
\boxed{\varepsilon A_5\to\text{constant}.}
\]

This is the first higher-point recursive factorization witness attached to the project gauge normalization spine.

## 5. Executable validation

The reference test checks:

1. five complex external momenta are null and exactly conserved;
2. the fundamental five-point BCJ relation on 500 deterministic random points;
3. reconstruction of the third ordering from a two-amplitude BCJ basis;
4. positive-helicity soft factorization on a momentum-conserving `epsilon` family;
5. `A5_project ~ g_YM^3` with `g_YM^2=1/alpha_c`;
6. five-point BCJ basis dimension `(5-3)!=2`.

Local result:

```text
6 passed, 0 failed
```

## 6. Advancement

```text
RFG14 complete project A4                       PASS
RFG15 project four-point BCJ numerators          PASS
RFG20 four-point project KLT                     PASS
RFG21 four-point pole factorization              PASS
five-point MHV fundamental BCJ                   PASS REFERENCE
five-point basis reduction 6 -> 2                PASS
momentum-conserving soft factorization           PASS
project five-point coupling power g_YM^3         PASS
full project five-point vertex assembly          OPEN
five-point project KLT matrix                     NEXT
five-point project cubic numerator set            OPEN
```

RFG22 is intentionally a higher-point reference/admission gate. Promotion to a direct project five-point BCJ statement requires assembling the five-point amplitude from the same RFG8/RFG13 cubic and quartic project vertices rather than importing the MHV closed form alone.