# Relational Field Closure
## Relativistic Matter-Source Closure: AB Curvature, Charge Projection, Lorentzian Stress-Energy and Einstein Normalization

**Working monograph v0.12 — 28 August 2026**

**Status:** `GEOMETRIC_SPINE_PASS / AB_MAXWELL_CURVATURE_PASS / LORENTZIAN_MATTER_ACTION_ALIGNED / CHARGE_PROJECTED_CURRENT_PASS / CHARGED_MATTER_STRESS_TENSOR_PASS / TOTAL_MATTER_COMPOSITION_OPEN / DYNAMIC_LAMBDA_ACTION_OPEN`

## Abstract

RFC now joins its relational geometry, Newton source operator and conserved-carrier chain to an action-consistent relativistic matter/Maxwell interface. RF-G0 fixes the spacetime signature `(-,+,+,+)`. RF-M1 fixes the physical electromagnetic connection by the Aharonov–Bohm phase. RF-N1B2K/O supply the independently audited matter carrier and phase-energy source. RF-N1B2P and RF-E6 then apply electric charge as a separate projection and derive the Maxwell source current from the canonical Lorentzian matter action.

The resulting active chain is

\[
\boxed{
\mathfrak a_{AB}
\to A
\to F=dA
\to J_{RFC}
\xrightarrow{\Pi_Q}
\mathcal J_Q
\to J_{EM}
\to (T^{EM},T^{matter})
\to T^{total}
\to G_{\mu\nu}=\kappa_ET_{\mu\nu}.
}
\]

The immediate Einstein-facing frontier is the total matter stress-energy composition across all admitted sectors, followed by the independent dynamic-`Lambda0` action.

## 1. Canonical Lorentzian geometry

RF-G0 fixes

\[
\boxed{\operatorname{signature}(g)=(-,+,+,+)}.
\]

The local static lapse sector remains

\[
\boxed{
g_R=-N_R^2c^2dt^2+h_\perp,}
\qquad
\boxed{\Phi_R=c^2\ln N_R.}
\]

RF-02I supplies the compatible metric connection and curvature, while the contracted Bianchi identity gives

\[
\boxed{\nabla^\mu G_{\mu\nu}=0.}
\]

## 2. AB-normalized Maxwell curvature

RF-M1 identifies

\[
\boxed{
\mathfrak a_{AB}=\frac q\hbar A,
\qquad
A=\frac\hbar q\mathfrak a_{AB}
}
\]

for an admitted nonzero probe charge. Therefore

\[
\boxed{
F=dA=\frac\hbar q d\mathfrak a_{AB}.
}
\]

Nilpotency immediately yields

\[
\boxed{dF=0.}
\]

The synchronized gauge convention is

\[
\boxed{
A'=A-d\Lambda,
\qquad
\Psi'=e^{iQ\Lambda/\hbar}\Psi,
}
\]

with

\[
\boxed{
\mathcal D_\mu\Psi
=\nabla_\mu\Psi+\frac{i}{\hbar}A_\mu Q\Psi.
}
\]

## 3. Conserved matter carrier before electric charge projection

RF-N1B2O carries the gauge-covariant phase source through

\[
\boxed{j_\vartheta=2A^2r_n,}
\qquad
\boxed{\mathcal E_\vartheta=A^2r_n^2,}
\]

where

\[
\boxed{r_n=D_{\hat\tau}\chi.}
\]

Thus

\[
\boxed{
\mathcal E_\vartheta
=\epsilon_Nj_\vartheta,
\qquad
\epsilon_N=\frac12r_n,
}
\]

and

\[
\boxed{
\rho_\vartheta
=\frac{\epsilon_N}{c^2}j_\vartheta.
}
\]

This carrier enters the matter/gravity source before electric charge weighting.

## 4. RF-E6 canonical matter action

For the canonical metric signature, RF-E6 uses

\[
\boxed{
\mathcal L_m
=-(\mathcal D_\mu\Psi)^\dagger\mathcal D^\mu\Psi
-U(\Psi),
}
\]

with

\[
U(\Psi)
=\Psi^\dagger\mathcal M^2\Psi+V_{inv}(\Psi),
\qquad
\boxed{[\mathcal M^2,Q]=0.}
\]

The charge-projected Noether current is

\[
\boxed{
\mathcal J_Q^\mu
=i\left[
(\mathcal D^\mu\Psi)^\dagger Q\Psi
-\Psi^\dagger Q\mathcal D^\mu\Psi
\right].
}
\]

Direct variation gives

\[
\boxed{
\frac{1}{\sqrt{-g}}
\frac{\delta S_m}{\delta A_\mu}
=-\frac1\hbar\mathcal J_Q^\mu.
}
\]

Combining this with the Maxwell kinetic action gives

\[
\boxed{
\nabla_\mu F^{\mu\nu}=\mu_*J_{EM}^\nu,
\qquad
J_{EM}^\nu=\frac1\hbar\mathcal J_Q^\nu.
}
\]

## 5. Charge-projected RFC current intertwiner

For a charge-resolved carrier packet,

\[
\boxed{
\Pi_Q[J]^{\mu}=\sum_aq_aJ_a^{\mu}.
}
\]

The RFC-to-Maxwell map is

\[
\boxed{
J_{EM}^{\mu}
=\frac1\hbar\Pi_Q[J_{RFC}]^{\mu}.
}
\]

For a single charge eigenvalue,

\[
\boxed{
J_{EM}^{\mu}
=\frac q\hbar J_{RFC,\vartheta}^{\mu}
}
\]

on the RF-N1B2K zero-defect carrier-match surface.

For the neutral sector,

\[
\boxed{Q=0\Longrightarrow J_{EM}^{\mu}=0,}
\]

while the unweighted matter carrier and matter stress-energy remain available to the gravitational source.

## 6. One electromagnetic source ledger

RFC keeps two equivalent action representations separately typed.

The microscopic representation is

\[
\boxed{
S_{micro}
=\int d^4x\sqrt{-g}
\left[-\frac{F^2}{4\mu_*}+\mathcal L_m(D\Psi,A,g)\right].
}
\]

For a prescribed external current,

\[
\boxed{
S_{eff}
=\int d^4x\sqrt{-g}
\left[-\frac{F^2}{4\mu_*}-J_{EM}^\mu A_\mu\right].
}
\]

Each produces

\[
\nabla_\mu F^{\mu\nu}=\mu_*J_{EM}^\nu.
\]

The source ledger therefore has one current contribution for a given microscopic carrier realization.

## 7. Charged-matter stress-energy

Metric variation of the canonical matter action gives

\[
\boxed{
T_{\mu\nu}^{matter}
=(\mathcal D_\mu\Psi)^\dagger\mathcal D_\nu\Psi
+(\mathcal D_\nu\Psi)^\dagger\mathcal D_\mu\Psi
+g_{\mu\nu}\mathcal L_m.
}
\]

The Maxwell tensor is

\[
\boxed{
T_{\mu\nu}^{EM}
=\frac1{\mu_*}
\left(
F_{\mu\alpha}F_\nu{}^\alpha
-\frac14g_{\mu\nu}F^2
\right).
}
\]

On the admitted matter equations,

\[
\boxed{
\nabla^\mu T_{\mu\nu}^{matter}
=+F_{\nu\lambda}J_{EM}^\lambda,
}
\]

and

\[
\boxed{
\nabla^\mu T_{\mu\nu}^{EM}
=-F_{\nu\lambda}J_{EM}^\lambda.
}
\]

Hence

\[
\boxed{
\nabla^\mu
(T^{matter}+T^{EM})_{\mu\nu}=0.
}
\]

This is the explicit source pair needed by the Einstein–Bianchi bridge.

## 8. Phase pressure and on-shell massive scalar

For a single phase field with

\[
\mathcal L_{phase}
=-A^2q_\mu q^\mu-V,
\]

and pure normal flow, define

\[
K=A^2r_n^2.
\]

RF-E4 gives

\[
\boxed{
\varepsilon=K+V,
\qquad
p=K-V,
\qquad
\varepsilon+3p=4K-2V.
}
\]

For the homogeneous quadratic on-shell scalar, RF-E5 gives

\[
\boxed{
\omega^2=m^2,
\qquad
V=K,
\qquad
p=0,
\qquad
\varepsilon=2K.
}
\]

The Noether carrier is

\[
\boxed{j_\vartheta=2A^2\omega,}
\]

so

\[
\boxed{
\frac K{j_\vartheta}=\frac\omega2,
\qquad
\frac{\varepsilon}{j_\vartheta}=\omega.
}
\]

The factor-two carrier-energy firewall therefore survives the canonical Lorentzian action closure.

## 9. Maxwell normalization coordinate

In rationalized Heaviside–Lorentz natural units,

\[
\boxed{\mu_*=1.}
\]

In SI,

\[
\boxed{\mu_*=\mu_0.}
\]

The electromagnetic coupling satisfies

\[
\boxed{
\alpha_{EM}
=\frac{\mu_*e^2c}{4\pi\hbar},
}
\]

hence

\[
\boxed{
\mu_*
=\frac{4\pi\alpha_{EM}\hbar}{e^2c}.
}
\]

This closes the unit-convention calibration once the electromagnetic coupling is independently frozen.

## 10. Einstein normalization

RF-N1C and RF-E3 give

\[
\boxed{
\kappa_E=\frac{8\pi G}{c^4}.
}
\]

In natural units,

\[
\boxed{
\kappa_g^2=4\kappa_E=32\pi G.
}
\]

Therefore

\[
\boxed{
S_{EH}
=\frac{1}{2\kappa_E}
\int d^4x\sqrt{-g}\,R
=\frac{2}{\kappa_g^2}
\int d^4x\sqrt{-g}\,R.
}
\]

The metric field equation is

\[
\boxed{
G_{\mu\nu}=\kappa_ET_{\mu\nu}.
}
\]

For dynamic `Lambda0`, RF-E0 gives the exact transfer identity

\[
\boxed{
\kappa_E\nabla^\mu T^{total}_{\mu\nu}
=\nabla_\nu\Lambda_0.
}
\]

## 11. Validation authority

RF-E6 correction branch:

- tested commit `3083337b15742d9aebae802469aa93c17109aeb8`;
- workflow run `33207514670`;
- job `98972226978`;
- full reference suite: **470/470 PASS**;
- dedicated RF-E6 tests: **11/11 PASS**.

Receipt:

`validation/RFE6_LORENTZIAN_MATTER_ACTION_SOURCE_BOOKKEEPING_V0_1.json`

`CROSS_REFERENCE_LOCK.json` v0.36 pins RF-E6 as the active RFC action/current-sign correction authority while retaining earlier receipts as historical provenance.

## 12. Current frontier

The matter side now supplies a complete covariant tensor for the admitted charged scalar/multiplet action. The next closure gate is the explicit decomposition and recomposition of the complete scalar matter tensor into phase, amplitude-gradient and potential/rest contributions on one shared action ledger:

\[
\boxed{
T_{\mu\nu}^{scalar}
=T_{\mu\nu}^{phase}
+T_{\mu\nu}^{amp/grad}
+T_{\mu\nu}^{pot/rest}.
}
\]

That gate must verify exact recomposition, gauge covariance, anisotropic gradient stresses, the homogeneous RF-E4/RF-E5 limits, and conservation on admitted on-shell solutions. It is the immediate prerequisite to total-matter Einstein source promotion.
