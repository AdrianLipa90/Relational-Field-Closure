# RF-S8 — Joint-KL Clock / Radial Action Composition

Status: `EXACT_KL_PRODUCT_COMPOSITION / EXACT_CORRELATION_DECOMPOSITION / CONDITIONAL_SINGLE_JOINT_ACTION_COEFFICIENT / R_ALPHA_UNITY_ON_JOINT_ACTION_SURFACE / PHYSICAL_JOINT_STATE_BINDING_OPEN`

RF-S8 follows RF-S5 and RF-I1 and addresses `CLOCK_RADIAL_ACTION_COMPOSITION` and the ratio part of `CLOCK_ALPHA_BINDING`. The gate uses the fact that both the radial information coordinate and the positive-rate clock coordinate already carry the natural-log relative-information type. Their state dependence remains distinct as established by RF-S5.

The theorem is formulated on the stationary zero-baseline dynamic chart. Any constant RF-L4 information background is retained in the corresponding constant `Lambda_star` coordinate before the dynamic relative-information components are composed.

## 1. Radial relative-information component

Let the radial relational state be

\[
p_R=(p_a),
\qquad
\pi_R=(\pi_a),
\]

with `pi_a>0` and normalized probabilities. IDT 01C supplies

\[
\boxed{
\mathcal J_R
:=D_{KL}(p_R\|\pi_R)
=\sum_{a:p_a>0}p_a\ln\frac{p_a}{\pi_a}.
}
\]

On a common positive relational area `A_rel`, define

\[
\boxed{
\Xi_R:=\frac{\mathcal J_R}{\mathcal A_{rel}}.
}
\]

On the RF-S4 locally Fisher-normalized radial branch this is the dynamic information-curvature coordinate whose canonical scalar is `phi_I=sqrt(2 Xi_R)` in the stationary zero-baseline chart.

## 2. Clock relative-information component

RF-I1 source-pins the positive phase-rate pair

\[
r_s>0,
\qquad
r_0>0
\]

into the IDT 05F maximum-Shannon-entropy rate family

\[
\boxed{
f_r(t)=r e^{-rt},
\qquad t\ge0.
}
\]

The exact rate relative information is

\[
\boxed{
\mathcal J_C
:=D_{KL}(f_{r_s}\|f_{r_0})
=\ln\frac{r_s}{r_0}+\frac{r_0}{r_s}-1
=\Phi\!\left(\frac{r_0}{r_s}\right),
}
\]

where

\[
\Phi(x)=x-1-\ln x.
\]

On the same admitted relational area,

\[
\boxed{
\Xi_C:=\frac{\mathcal J_C}{\mathcal A_{rel}}.
}
\]

This is the RF-I1/RF-E17 clock information-curvature coordinate.

## 3. Exact product-state KL composition

Define the product information state on the radial label and positive-time clock coordinate,

\[
\boxed{
P_{RC}(a,t)=p_a f_{r_s}(t),
}
\]

with product reference

\[
\boxed{
\Pi_{RC}(a,t)=\pi_a f_{r_0}(t).
}
\]

Then

\[
\ln\frac{P_{RC}(a,t)}{\Pi_{RC}(a,t)}
=
\ln\frac{p_a}{\pi_a}
+
\ln\frac{f_{r_s}(t)}{f_{r_0}(t)}.
\]

Normalization of both factors gives exactly

\[
\boxed{
\mathcal J_{RC}
:=D_{KL}(P_{RC}\|\Pi_{RC})
=\mathcal J_R+\mathcal J_C.
}
\]

On a shared area,

\[
\boxed{
\Xi_{RC}=\Xi_R+\Xi_C.
}
\]

This is the factorized clock/radial composition theorem.

## 4. Correlated-state decomposition

More generally, let `P_RC` be an admitted joint state with marginals `P_R` and `P_C`, while the reference remains the product `pi_R x pi_C`. The KL chain identity gives

\[
\boxed{
D_{KL}(P_{RC}\|\pi_R\pi_C)
=
D_{KL}(P_R\|\pi_R)
+
D_{KL}(P_C\|\pi_C)
+I_{P}(R;C),
}
\]

where

\[
\boxed{
I_P(R;C)
:=D_{KL}(P_{RC}\|P_RP_C)\ge0.
}
\]

Define

\[
\mathcal J_X:=I_P(R;C),
\qquad
\Xi_X:=\frac{\mathcal J_X}{\mathcal A_{rel}}.
\]

Then exactly

\[
\boxed{
\Xi_{RC}=\Xi_R+\Xi_C+\Xi_X.
}
\]

The factorized branch is the zero-correlation surface

\[
\boxed{
\Xi_X=0.
}
\]

Thus clock/radial correlation is carried as an explicit information coordinate rather than absorbed into either marginal state.

## 5. Single joint-information action

RF-L3 supplies the linear information-curvature potential map. Introduce a joint-action coefficient `alpha_J` for the admitted joint information scalar:

\[
\boxed{
U_J
=\frac{\alpha_J}{\kappa_E}\Xi_{RC}.
}
\]

Using the exact decomposition,

\[
U_J
=\frac{\alpha_J}{\kappa_E}
(\Xi_R+\Xi_C+\Xi_X).
\]

The independently typed decomposed representation is

\[
\boxed{
U_D
=\frac1{\kappa_E}
\left(
\alpha_I\Xi_R
+\alpha_{clk}\Xi_C
+\alpha_X\Xi_X
\right).
}
\]

RF-S5 remains active: `Xi_R` and `Xi_C` are distinct state coordinates. RF-S8 compares only their action coefficients under a single joint-information action admission.

## 6. Coefficient forcing by independent coordinate variation

Assume the joint-action representation and decomposed representation describe the same dynamic scalar potential on an admitted coordinate domain containing independent radial and clock variations.

Require

\[
\boxed{U_J=U_D}
\]

as a functional identity on that domain.

On a radial-only variation with

\[
\Xi_R>0,
\qquad
\Xi_C=\Xi_X=0,
\]

one obtains

\[
\boxed{\alpha_I=\alpha_J.}
\]

On a clock-only variation with

\[
\Xi_C>0,
\qquad
\Xi_R=\Xi_X=0,
\]

one obtains

\[
\boxed{\alpha_{clk}=\alpha_J.}
\]

Therefore

\[
\boxed{
\alpha_{clk}=\alpha_I=\alpha_J.
}
\]

If an independently variable correlated coordinate is also admitted, a correlation-only variation additionally gives

\[
\boxed{\alpha_X=\alpha_J.}
\]

The clock/radial coefficient equality is therefore forced by functional equivalence of one joint information action and its decomposed representation, rather than by equality of the state coordinates.

## 7. Consequence for the scale coupling ratio

RF-S5 defines

\[
\boxed{
r_\alpha:=\frac{\alpha_{clk}}{\alpha_I}.}
\]

On the RF-S8 single-joint-action surface with nonzero admitted coupling,

\[
\boxed{r_\alpha=1.}
\]

This fixes the clock/radial coupling ratio while leaving the common absolute coefficient `alpha_J=alpha_I=alpha_clk` as the existing physical normalization coordinate.

On the separately admitted RF-S4 same-mass/same-target surface, the RF-S4/RF-S1 scale equation therefore reduces to

\[
\boxed{
\zeta_s^3
=\frac1{C_{\Delta/FS}}
=\frac{9\sqrt3\pi}{8},
}
\]

hence

\[
\boxed{
\zeta_s
=C_{\Delta/FS}^{-1/3}.
}
\]

Physical conversion of `zeta_s=m_I ell_s` remains attached to the TIR/RFC cell-source gate and the relevant scale-calibration branch.

## 8. Common-area and joint-state admission ledger

The coefficient theorem requires the following typed composition surface:

```text
radial J_R has IDT 01C natural-log relative-information lineage
clock J_C has RF-I1 / IDT 05F natural-log relative-information lineage
one common selected relational area A_rel
one joint reference Pi_RC = pi_R x pi_C
one admitted joint information scalar J_RC
RF-L3 map applied once to the joint scalar
same physical action represented either jointly or decomposed
radial and clock coordinates independently variable on the admitted domain
constant Xi_star background already absorbed into Lambda_star
```

These are source/action-composition conditions. A physical joint-state receipt remains required before the coefficient equality is promoted as a physical binding for a target system.

## 9. Factorization and correlation diagnostics

For a measured or constructed joint state define the correlation information

\[
\boxed{
\mathcal J_X
=\mathcal J_{RC}-\mathcal J_R-\mathcal J_C.
}
\]

and, on a common area,

\[
\boxed{
\Xi_X=\Xi_{RC}-\Xi_R-\Xi_C.
}
\]

A normalized additivity defect may be defined by

\[
\boxed{
\Delta_{add}
:=
\frac{
|\mathcal J_{RC}-\mathcal J_R-\mathcal J_C-\mathcal J_X|
}
{
\mathcal J_{RC}+\mathcal J_R+\mathcal J_C+\mathcal J_X
}
}
\]

on nondegenerate support. Exact KL bookkeeping gives `Delta_add=0`.

The factorization defect may be represented by

\[
\boxed{
\Delta_{fact}
:=\frac{\mathcal J_X}{1+\mathcal J_X}
\in[0,1).
}
\]

with `Delta_fact=0` exactly on the product-state surface.

## 10. Promotion ledger

Promoted parents:

```text
IDT 01C radial natural-log KL lineage                    PASS
RF-I1 / IDT 05F clock rate-KL lineage                    PASS
RF-L3 linear information-curvature action map            PASS CONDITIONAL
RF-S5 radial/clock state separation                       PASS
```

RF-S8 outputs:

```text
product-state KL additivity J_RC=J_R+J_C                 PASS EXACT
correlated joint decomposition + mutual information       PASS EXACT
common-area Xi_RC=Xi_R+Xi_C+Xi_X                          PASS EXACT GIVEN AREA BINDING
joint/decomposed action coefficient comparison             PASS EXACT CONDITIONAL
alpha_I=alpha_clk=alpha_J from independent variations      PASS EXACT ON JOINT-ACTION SURFACE
r_alpha=1                                                   PASS CONSEQUENCE ON SAME SURFACE
RF-S5 state-coordinate separation                           PRESERVED
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

## 11. Validation authority

Reference implementation: `src/rfc/joint_kl_clock_radial_action_composition.py`.
Reference tests: `tests/reference/test_rfs8_joint_kl_clock_radial_action_composition.py`.
Validation receipt: `validation/RF_S8_JOINT_KL_CLOCK_RADIAL_ACTION_COMPOSITION_V0_1.json`.

Parent RFC main at branch creation: `466d364f3d903215b94e2ba66e1fd1fac23e7a30`.
