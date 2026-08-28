# RFG25 — Project Five-Point Berends–Giele / BCJ Gate

Status: `DIRECT_PROJECT_FIVE_POINT_YM_ASSEMBLY_PASS / FIVE_LEG_WARD_PASS / FUNDAMENTAL_BCJ_PASS / REFLECTION_AND_DECOUPLING_PASS / QUARTIC_NORMALIZATION_FIREWALL_PASS`

RFG25 closes the project Yang–Mills assembly gap left by the RFG23 reference gate. It evaluates five-point color-ordered amplitudes directly from the same RFG8 cubic and RFG13 quartic interaction normalization used at four points.

## 1. Ordered project currents

The color-ordered Berends–Giele recursion is

\[
\boxed{P^2J_P^\mu=\sqrt2\sum_{XY=P}[J_X,J_Y]^\mu+\sum_{XYZ=P}\{J_X,J_Y,J_Z\}^\mu}.
\]

The binary `sqrt(2)` and quartic `1` coefficients are inherited from the admitted project interaction layer. The final external propagator is amputated before contraction with the fifth polarization.

For ordering `sigma` define the stripped amplitude

\[
\boxed{A_5^{BG}(\sigma)}.
\]

The Yang–Mills coupling attachment remains

\[
\boxed{\mathcal A_5^{project}=g_{YM}^3A_5^{BG},\qquad g_{YM}^2=1/\alpha_c}.
\]

## 2. Five-leg Ward gate

For every external leg,

\[
\boxed{A_5^{BG}|_{\varepsilon_i\to p_i}=0}
\]

on deterministic physical `2 -> 3` massless configurations.

## 3. Direct project BCJ

The project amplitudes themselves satisfy

\[
\boxed{0=s_{12}A_5^{BG}(1,2,3,4,5)+(s_{12}+s_{23})A_5^{BG}(1,3,2,4,5)+(s_{12}+s_{23}+s_{24})A_5^{BG}(1,3,4,2,5)}.
\]

No gravity output is used to select this relation.

## 4. Ordered-amplitude identities

The same recursion verifies reflection

\[
\boxed{A(1,2,3,4,5)=-A(5,4,3,2,1)}
\]

and the five-point insertion/photon-decoupling identity.

## 5. Quartic-normalization firewall

Removing the inherited quartic current contribution while leaving the cubic recursion fixed produces order-one Ward defects. The admitted RFG13 coefficient restores five-leg Ward closure.

## 6. Executable validation

The byte-preserved reference test verifies masslessness/conservation/transversality, all five Ward replacements, direct project fundamental BCJ, reflection and decoupling, the quartic adversarial firewall, and `g_YM^3` coupling power.

Recorded result:

```text
6 passed, 0 failed
```

## 7. Advancement

```text
RFG23 five-point BCJ / soft reference               PASS
RFG24 five-point KLT kernel                         PASS
RFG25 direct project five-point Yang-Mills          PASS
RFG25 five-leg Ward                                 PASS
RFG25 project fundamental BCJ                       PASS
RFG26 project BG x BG KLT gravity core              NEXT/PASS DOWNSTREAM
explicit 15-cubic-graph numerator set               OPEN
```
