# RF-S4 — Radial Information / Matter Action Reclassification

Status: `LOCAL_FISHER_RADIAL_NORMALIZATION / EXACT_POLAR_RADIAL_CANONICALIZATION / CONDITIONAL_SINGLE_CARRIER_ACTION_EQUIVALENCE / MASS_EQUALITY_FORCED_ON_ZERO_DEFECT_SURFACE / DOUBLE_COUNTING_FIREWALL_ACTIVE / GLOBAL_SOURCE_BINDING_OPEN`

RF-S4 addresses the `MATTER_INFORMATION_MASS_BINDING` left by RF-S3. It tests whether the locally Fisher-normalized information scalar can be represented as the canonical radial degree of freedom of the same RFC complex matter scalar whose phase supplies the RF-E5/RF-E16 clock/Noether carrier.

The gate does not identify the two sectors by name. It derives the exact action-level consequences of one explicit radial source-binding defect and keeps the single-representation bookkeeping condition active.

## 1. RF-L4A information radial coordinate

RF-L4 introduces the baseline-resolved information curvature

\[
\bar\Xi_I:=\Xi_I-\Xi_\star\ge0
\]

and the canonical scalar coordinate

\[
\phi_I=\beta_I\sqrt{\bar\Xi_I}.
\]

RF-L4A fixes, in the local Shannon-Fisher stationary-reference sector,

\[
\boxed{\beta_I=\sqrt2.}
\]

Hence the canonical information scalar is

\[
\boxed{
\phi_I=\sqrt{2\bar\Xi_I}
}
\]

on the admitted local positive chart. Equivalently,

\[
\boxed{
\bar\Xi_I=\frac12\phi_I^2.
}
\]

The RF-L4A quadratic potential is

\[
\boxed{
U_I(\phi_I)=\frac12m_I^2\phi_I^2,
\qquad
\alpha_I=\kappa_E m_I^2.
}
\]

## 2. Canonical radial coordinate of the RFC complex scalar

Take one positive-mass eigenmode of the RF-E6 complex matter scalar on the quadratic branch,

\[
\Psi=Ae^{i\vartheta},
\qquad A\ge0,
\]

with gauge-covariant phase one-form

\[
q_\mu:=\mathscr D_\mu\vartheta.
\]

For the free quadratic eigenmode,

\[
U_\Psi=m_\Psi^2A^2.
\]

The exact polar kinetic decomposition gives

\[
(\mathcal D_\mu\Psi)^*\mathcal D^\mu\Psi
=(\partial A)^2+A^2q^2.
\]

Define the canonically normalized radial coordinate

\[
\boxed{
\phi_A:=\sqrt2\,A.
}
\]

Then the selected matter-mode Lagrangian is exactly

\[
\boxed{
\mathcal L_\Psi
=-\frac12(\nabla\phi_A)^2
-\frac12\phi_A^2q^2
-\frac12m_\Psi^2\phi_A^2.
}
\]

The same factor `sqrt(2)` therefore appears independently in the canonical polar radial normalization and in the RF-L4A Shannon-Fisher normalization.

## 3. Radial information-amplitude defect

Define the nonnegative radial source-binding defect

\[
\boxed{
\Delta_{A\Xi}
:=\frac{|A^2-\bar\Xi_I|}{A^2+\bar\Xi_I}
}
\]

for nondegenerate support `A^2+barXi_I>0`.

Because

\[
\phi_A^2=2A^2,
\qquad
\phi_I^2=2\bar\Xi_I,
\]

one has exactly

\[
\boxed{
\Delta_{A\Xi}=0
\Longleftrightarrow
A^2=\bar\Xi_I
\Longleftrightarrow
\phi_A=\phi_I
}
\]

on the nonnegative radial branch.

Thus the matter/information field-coordinate identification is reduced to one executable amplitude-curvature source test.

## 4. Single-representation action ledger

RF-L2 writes the closure scalar separately from `L_base`, while RF-E6 places the full complex matter scalar in the base matter action. If `phi_I` and `phi_A` are admitted as the same physical radial degree of freedom, both representations must not retain duplicate radial kinetic or radial mass-potential terms.

On the zero-defect surface define the single radial coordinate

\[
\phi_R:=\phi_I=\phi_A.
\]

The selected complex scalar may then be reclassified exactly as

\[
\boxed{
\mathcal L_\Psi
=
\underbrace{
\left[-\frac12(\nabla\phi_R)^2
-\frac12m_\Psi^2\phi_R^2\right]
}_{\text{radial sector}}
+
\underbrace{
\left[-\frac12\phi_R^2q^2\right]
}_{\text{phase/Noether sector}}.
}
\]

RF-L2/RF-L4 supplies the closure radial representation

\[
\boxed{
\mathcal L_I^{rad}
=-\frac12(\nabla\phi_R)^2
-\frac12m_I^2\phi_R^2.
}
\]

The action ledger therefore has two legal descriptions of the same radial carrier:

```text
original matter representation:
    radial kinetic + radial mass potential + phase term

reclassified closure representation:
    RF-L2/RF-L4 radial kinetic + RF-L4 mass potential
    + RF-E6/RF-E16 phase term with the same radial coefficient
```

Only one radial kinetic term and one radial mass-potential term are retained in a physical action instance.

## 5. Mass equality is forced by action equivalence

On `Delta_AXi=0`, require the original and reclassified descriptions to represent the same selected quadratic matter eigenmode for nonzero radial support.

The kinetic coefficients already agree canonically. Equality of the radial quadratic potentials requires

\[
\frac12m_\Psi^2\phi_R^2
=\frac12m_I^2\phi_R^2.
\]

For `phi_R != 0`,

\[
\boxed{m_\Psi^2=m_I^2.}
\]

On the positive-mass branch,

\[
\boxed{m_\Psi=m_I.}
\]

Therefore RF-S3 immediately gives

\[
\boxed{
r_{\Psi I}=1,
\qquad
\rho_\omega=1,
\qquad
\Delta_\omega=\Delta_m=0.
}
\]

The equality is a consequence of the admitted single-carrier action equivalence, not an independent numerical calibration.

## 6. Information curvature becomes radial amplitude squared

On the same zero-defect local Fisher surface,

\[
\boxed{
\bar\Xi_I=A^2.
}
\]

The RF-L4A potential can therefore be written in three exactly equivalent coordinates:

\[
\boxed{
U_I
=\frac12m_I^2\phi_I^2
=m_I^2\bar\Xi_I
=m_\Psi^2A^2.
}
\]

This is exactly the quadratic matter radial potential of the selected mode after `m_Psi=m_I` is forced by the action match.

## 7. Dynamic Lambda roundtrip

RF-L2 moves the scalar potential stress to the metric-proportional coordinate,

\[
\Lambda_0=\Lambda_\star+\kappa_EU_I.
\]

Using the RF-S4 zero-defect identities,

\[
\boxed{
\Delta\Lambda_I
=\kappa_E m_I^2A^2.
}
\]

RF-L4A independently gives

\[
\alpha_I=\kappa_E m_I^2
\]

and the information-curvature route gives

\[
\Delta\Lambda_I=\alpha_I\bar\Xi_I.
\]

Since `barXi_I=A^2`,

\[
\boxed{
\kappa_EU_I
=\kappa_E m_I^2A^2
=\alpha_IA^2
=\alpha_I\bar\Xi_I.
}
\]

Thus the matter radial-potential representation and the RF-L3/RF-L4 dynamic-Lambda representation are coefficient-identical on the admitted source-binding surface.

## 8. Phase sector remains explicit

The reclassification does not remove the complex-scalar phase dynamics. The term

\[
\boxed{
\mathcal L_{phase}
=-\frac12\phi_R^2q_\mu q^\mu
=-A^2q_\mu q^\mu
}
\]

remains in the matter/Noether ledger and continues to source RF-E5/RF-E16.

Therefore the same radial coordinate controls the phase-current normalization while the phase rate remains the clock/Noether carrier.

The RF-E5 factor-two observable firewall remains active.

## 9. RF-S3/RF-S2 consequence

For the same selected matter target,

\[
m_{target}=m_\Psi,
\]

RF-S4 gives

\[
r_m=r_{\Psi I}=\rho_\omega=1.
\]

The RF-S3 same-target scale relation becomes

\[
\boxed{
r_\alpha\zeta_s^3
=\frac1{C_{\Delta/FS}}
=\frac{9\sqrt3\pi}{8}.
}
\]

If the separately gated clock coupling also satisfies `r_alpha=1`, then

\[
\boxed{
\zeta_s=m_I\ell_s
=C_{\Delta/FS}^{-1/3}
\approx1.82931154035502.
}
\]

## 10. Promotion ledger

Exact/conditional inputs:

```text
RF-E6 polar complex-scalar action decomposition       PASS EXACT
canonical radial coordinate phi_A=sqrt(2) A           PASS EXACT
RF-L4A beta_I=sqrt(2)                                 PASS LOCAL FISHER
RF-L4A U_I=(1/2)m_I^2 phi_I^2                         PASS LOCAL FISHER
RF-L2 single closure-scalar action ledger              PASS
RF-S3 rho_omega=m_Psi/m_I                             PASS ON COMMON-PHASE ONSHELL SURFACE
```

RF-S4 outputs on the admitted local zero-defect surface:

```text
Delta_AXi=0 <-> A^2=barXi_I <-> phi_A=phi_I           PASS EXACT
single-carrier action reclassification                PASS EXACT GIVEN SOURCE BINDING
m_Psi=m_I from radial potential coefficient match     PASS EXACT GIVEN NONZERO SUPPORT
rho_omega=1                                            PASS CONSEQUENCE
U_I=m_I^2 barXi_I=m_Psi^2 A^2                         PASS EXACT
Lambda roundtrip coefficient identity                 PASS EXACT
```

Remaining physical gates:

```text
RADIAL_INFORMATION_SOURCE_BINDING  demonstrate/derive Delta_AXi=0 physically
GLOBAL_FISHER_EXTENSION            extend beta_I normalization beyond local sector
CLOCK_ALPHA_BINDING                determine r_alpha
TIR_CONTINUUM_COORDINATE_BIND      determine ell_s / zeta_s physically
TRANSLATIONAL_OBSERVABLE           select measured energy coordinate
DIRECTIONAL_CUBIC_TEST             test parity-odd O(beta^3) branch
GENERAL_MATTER_MULTIPLET           extend radial binding across intended matter modes
```

## 11. Validation authority

Reference implementation: `src/rfc/radial_information_matter_action_reclassification.py`.
Reference tests: `tests/reference/test_rfs4_radial_information_matter_action_reclassification.py`.
Validation receipt: `validation/RF_S4_RADIAL_INFORMATION_MATTER_ACTION_RECLASSIFICATION_V0_1.json`.

Parent RFC main at branch creation: `acb5b7fb55f269ef0c29b79429558be7531ab3fa`.
