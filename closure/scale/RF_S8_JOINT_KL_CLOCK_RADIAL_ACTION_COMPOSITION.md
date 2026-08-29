# RF-S8 — Joint-KL Clock / Radial Action Composition

Status: `EXACT_KL_PRODUCT_COMPOSITION / EXACT_CORRELATION_DECOMPOSITION / CONDITIONAL_SINGLE_JOINT_ACTION_COEFFICIENT / R_ALPHA_UNITY_ON_JOINT_ACTION_SURFACE / PHYSICAL_JOINT_STATE_BINDING_OPEN`

RF-S8 follows RF-S5 and RF-I1 and addresses `CLOCK_RADIAL_ACTION_COMPOSITION` and the ratio part of `CLOCK_ALPHA_BINDING`. The radial and clock coordinates remain distinct state coordinates as established by RF-S5. RF-S8 compares their coefficients only after admission into one joint relative-information action.

The theorem uses the stationary zero-baseline dynamic chart. A constant RF-L4 information background is retained in `Lambda_star` before the dynamic relative-information components are composed.

## 1. Radial natural-log relative information

IDT 01C supplies the radial Shannon relative-information state in bits,

\[
\mathcal I_R=D_{KL}^{(2)}(p_R\|\pi_R).
\]

IDT 01K supplies the exact bit-to-natural-log conversion

\[
\boxed{
\mathcal J_R=(\ln2)\mathcal I_R
=\sum_{a:p_a>0}p_a\ln\frac{p_a}{\pi_a}.
}
\]

For one admitted positive relational area,

\[
\boxed{\Xi_R=\frac{\mathcal J_R}{\mathcal A_{rel}}.}
\]

This is the natural-log numerator type used by RF-L3/RF-L4A on the local dynamic radial chart.

## 2. Clock natural-log relative information

RF-I1 source-pins the positive phase-rate pair `r_s,r_0>0` into the IDT 05F maximum-Shannon-entropy rate family

\[
f_r(t)=r e^{-rt},\qquad t\ge0.
\]

The exact rate relative information is

\[
\boxed{
\mathcal J_C
=D_{KL}(f_{r_s}\|f_{r_0})
=\ln\frac{r_s}{r_0}+\frac{r_0}{r_s}-1
=\Phi\!\left(\frac{r_0}{r_s}\right),
}
\]

with

\[
\Phi(x)=x-1-\ln x.
\]

RF-I1/IDT 05E places this quantity in the same 01K natural-log numerator type. On the same admitted area,

\[
\boxed{\Xi_C=\frac{\mathcal J_C}{\mathcal A_{rel}}.}
\]

## 3. Exact product-state KL composition

Define

\[
P_{RC}(a,t)=p_a f_{r_s}(t),
\qquad
\Pi_{RC}(a,t)=\pi_a f_{r_0}(t).
\]

Then

\[
\ln\frac{P_{RC}}{\Pi_{RC}}
=\ln\frac{p_a}{\pi_a}
+\ln\frac{f_{r_s}}{f_{r_0}}.
\]

Normalization of both factors gives

\[
\boxed{
\mathcal J_{RC}
=D_{KL}(P_{RC}\|\Pi_{RC})
=\mathcal J_R+\mathcal J_C.
}
\]

On a shared area,

\[
\boxed{\Xi_{RC}=\Xi_R+\Xi_C.}
\]

## 4. Correlated-state decomposition

For a general admitted joint state `P_RC` with marginals `P_R,P_C` and product reference `pi_R pi_C`, the KL chain identity gives

\[
\boxed{
D_{KL}(P_{RC}\|\pi_R\pi_C)
=D_{KL}(P_R\|\pi_R)
+D_{KL}(P_C\|\pi_C)
+I_P(R;C),
}
\]

where

\[
\boxed{
I_P(R;C)=D_{KL}(P_{RC}\|P_RP_C)\ge0.
}
\]

Define

\[
\mathcal J_X:=I_P(R;C),
\qquad
\Xi_X:=\frac{\mathcal J_X}{\mathcal A_{rel}}.
\]

Then

\[
\boxed{\Xi_{RC}=\Xi_R+\Xi_C+\Xi_X.}
\]

The factorized surface is `Xi_X=0`. Correlation therefore remains an explicit information coordinate.

## 5. Joint versus decomposed information action

RF-L3 supplies the linear information-curvature potential map. For one admitted joint scalar define

\[
\boxed{
U_J=\frac{\alpha_J}{\kappa_E}\Xi_{RC}
=\frac{\alpha_J}{\kappa_E}(\Xi_R+\Xi_C+\Xi_X).
}
\]

The typed decomposed representation is

\[
\boxed{
U_D=\frac1{\kappa_E}
(\alpha_I\Xi_R+\alpha_{clk}\Xi_C+\alpha_X\Xi_X).
}
\]

RF-S8 requires these to be the same dynamic scalar potential on an admitted coordinate domain containing independent radial and clock variations.

A radial-only variation gives

\[
\boxed{\alpha_I=\alpha_J,}
\]

and a clock-only variation gives

\[
\boxed{\alpha_{clk}=\alpha_J.}
\]

Therefore

\[
\boxed{\alpha_{clk}=\alpha_I=\alpha_J.}
\]

If an independently variable correlation coordinate is admitted, a correlation-only variation additionally gives `alpha_X=alpha_J`.

This coefficient equality follows from functional equivalence of the joint and decomposed actions; the RF-S5 state-coordinate separation is preserved.

## 6. Coupling-ratio and scale consequence

RF-S5 defines

\[
r_\alpha=\frac{\alpha_{clk}}{\alpha_I}.
\]

On the RF-S8 single-joint-action surface with nonzero coupling,

\[
\boxed{r_\alpha=1.}
\]

The common absolute coefficient remains the separate normalization coordinate.

On the separately admitted RF-S4 same-mass/same-target surface, the scale relation reduces to

\[
\boxed{
\zeta_s^3
=\frac1{C_{\Delta/FS}}
=\frac{9\sqrt3\pi}{8},
\qquad
\zeta_s=C_{\Delta/FS}^{-1/3}.
}
\]

Physical conversion of `zeta_s=m_I ell_s` remains attached to the TIR/RFC cell-source and scale-calibration gates.

## 7. Admission ledger

The coefficient theorem requires:

```text
radial I_R from IDT 01C
radial J_R=(ln2)I_R from IDT 01K
clock J_C from RF-I1 / IDT 05F with the same natural-log numerator type
one common selected relational area A_rel
one joint reference Pi_RC=pi_R x pi_C
one admitted joint information scalar J_RC
RF-L3 map applied once to the joint scalar
same dynamic action represented jointly and decomposed
radial and clock coordinates independently variable
constant Xi_star background absorbed into Lambda_star
```

A physical joint-state receipt and common-area source receipt remain separate promotion gates.

## 8. Executable diagnostics

The executable reference checks:

1. `J_C=Phi(r_0/r_s)`;
2. product-state KL additivity;
3. the correlated chain rule `J_RC=J_R+J_C+J_X`;
4. mutual-information nonnegativity and zero on factorized states;
5. common-area curvature additivity;
6. equality of joint/decomposed potentials for one common coefficient;
7. radial-only, clock-only and correlation-only basis residuals;
8. `r_alpha=1` when `alpha_clk=alpha_I`;
9. the cubic shape-scale consequence;
10. invalid probability/rate/area domains fail closed.

Define the exact additivity defect on nondegenerate support,

\[
\Delta_{add}
=\frac{|\mathcal J_{RC}-\mathcal J_R-\mathcal J_C-\mathcal J_X|}
{\mathcal J_{RC}+\mathcal J_R+\mathcal J_C+\mathcal J_X},
\]

and the factorization coordinate

\[
\Delta_{fact}=\frac{\mathcal J_X}{1+\mathcal J_X}.
\]

Exact bookkeeping gives `Delta_add=0`; factorization gives `Delta_fact=0`.

## 9. Promotion ledger

```text
IDT 01C radial bit-valued KL state                         PASS
IDT 01K radial natural-log conversion                      PASS EXACT
RF-I1 / IDT 05F clock natural-log rate-KL lineage          PASS
RF-L3 linear information-curvature action map              PASS CONDITIONAL
RF-S5 radial/clock state separation                         PASS
product-state KL additivity                                PASS EXACT
correlated joint decomposition + mutual information         PASS EXACT
common-area Xi_RC=Xi_R+Xi_C+Xi_X                            PASS EXACT GIVEN AREA BINDING
joint/decomposed coefficient comparison                     PASS EXACT CONDITIONAL
alpha_I=alpha_clk=alpha_J                                   PASS EXACT ON JOINT-ACTION SURFACE
r_alpha=1                                                   PASS CONSEQUENCE ON SAME SURFACE
```

Remaining gates:

```text
PHYSICAL_JOINT_INFORMATION_STATE_BINDING
COMMON_RELATIONAL_AREA_SOURCE_BINDING
ABSOLUTE_ALPHA_NORMALIZATION
PHYSICAL_RADIAL_ZERO_DEFECT_DATA
RADIAL_BINDING_DYNAMICAL_TRANSPORT
TIR_RFC_CELL_SOURCE_BINDING
TRANSLATIONAL_OBSERVABLE
DIRECTIONAL_CUBIC_TEST
GENERAL_MATTER_MULTIPLET
GLOBAL_INFORMATION_GEODESIC_EXTENSION
```

## 10. Validation authority

Reference implementation: `src/rfc/joint_kl_clock_radial_action_composition.py`.
Reference tests: `tests/reference/test_rfs8_joint_kl_clock_radial_action_composition.py`.
Validation receipt: `validation/RF_S8_JOINT_KL_CLOCK_RADIAL_ACTION_COMPOSITION_V0_1.json`.

Parent RFC main at branch creation: `466d364f3d903215b94e2ba66e1fd1fac23e7a30`.
