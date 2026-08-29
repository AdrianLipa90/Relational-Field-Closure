# RF-S1 — Tetra / Phase-Clock Mass-Scale Closure

Status: `EXACT_SCALE_COMPOSITION / TIR_SHAPE_CLASS_PROMOTED / RF_I1_INFORMATION_SOURCE_PROMOTED / NOETHER_FLOW_SOURCE_AVAILABLE_CONDITIONAL / PHYSICAL_MASS_BINDINGS_OPEN`

RF-S1 is the first dedicated scale-closure gate. It consumes the RF-E17 clock-information action scale, the promoted RF-E18 velocity-gauge firewall, the promoted RF-E19 future-timelike Noether-current material congruence, the RF-L4A Shannon-Fisher mass coordinate, the IDT phase-clock length, the RF-I1 phase-rate information-curvature source binding, and the promoted TIR tetrahedral FS/spatial shape-class crosswalk.

The purpose is to replace a free energy prefactor by one explicit dimensionless relation among already typed coupling, spatial-scale, phase-scale and mass/energy coordinates.

## 1. RF-E17 action energy scale

RF-E17 gives the homogeneous-cell coefficient

\[
\boxed{
E_\star
=\frac{\alpha_{clk}}{\kappa_E}
\frac{V_{cell}}{\mathcal A_{rel}}.
}
\]

The directional action contribution is

\[
\boxed{
H_{clk}^{(s)}=E_\star\Phi(x_s),
\qquad
\Phi(x)=x-1-\ln x.
}
\]

RF-E18/RF-E19 supply the physically typed directional carrier

\[
\boxed{
x_s^{phys}=\frac1{1-s\beta_e},}
\]

where `beta_e=V_mu e^mu` is generated from a future-timelike RFC Noether flow on the admitted matter sector.

RF-I1 supplies the promoted information-source chain

\[
\boxed{
\mathcal J_{phase}^{(s)}=\Phi(x_s),
\qquad
\Xi_{phase}^{(s)}=\frac{\Phi(x_s)}{\mathcal A_{rel}},
}
\]

so the clock/phase relative-information numerator is already admitted into the RF-L3/RF-E17 action route.

## 2. Tetrahedral dual-shape crosswalk

TIR PR #104 derives on the tetrahedral Bloch realization

\[
\hat V_{\Delta^3}=\frac{8}{9\sqrt3},
\qquad
 a_{FS}^{tet}=\pi,
\]

hence

\[
\boxed{
C_{\Delta/FS}
:=\frac{\hat V_{\Delta^3}}{a_{FS}^{tet}}
=\frac{8}{9\sqrt3\pi}.
}
\]

TIR PR #105 subsequently promotes the common tetrahedral congruence class of the independently typed minimal spatial-isotropy frame and minimal symmetric qubit informational-completeness frame. Their common Gram matrix fixes the shape invariants used here up to the admitted orthogonal congruence class.

Let `ell_s` be the physical conversion scale of the spatial Pauli/Bloch relation carrier and let

\[
\ell_\varphi=\frac{\hbar c}{E_\varphi}
\]

be the IDT phase-clock length. Define

\[
\boxed{q_s:=\frac{\ell_s}{\ell_\varphi}>0.}
\]

The shape crosswalk gives

\[
\boxed{
\frac{V_{cell}}{\mathcal A_{rel}}
=C_{\Delta/FS}\,q_s^3\ell_\varphi.
}
\]

The exact TIR shape parent was promoted after 7/7 hosted workflows in PR #104 at merge commit `267a6c2022237fcc49284788d7d25c0c3580ff68`. The exact congruence-class closure was promoted after 7/7 hosted workflows in PR #105 at merge commit `ccc89fc04e1d85e9c6a60b7bb92e62a5d22d5f44`.

## 3. Coupling-ratio coordinate

RF-L4A gives

\[
\boxed{\alpha_I=\kappa_E m_I^2.}
\]

Define

\[
\boxed{r_\alpha:=\frac{\alpha_{clk}}{\alpha_I}.}
\]

Then

\[
\frac{\alpha_{clk}}{\kappa_E}=r_\alpha m_I^2
\]

and therefore

\[
\boxed{
E_\star
=r_\alpha C_{\Delta/FS}q_s^3m_I^2\ell_\varphi.
}
\]

Using `ell_phi=hbar c/E_phi`,

\[
\boxed{
E_\star
=r_\alpha C_{\Delta/FS}q_s^3
\frac{m_I^2\hbar c}{E_\varphi}.
}
\]

In natural units,

\[
\boxed{
E_\star
=r_\alpha C_{\Delta/FS}q_s^3
\frac{m_I^2}{E_\varphi}.
}
\]

## 4. Dimensionless closure equation

Define

\[
\boxed{\mu_\varphi:=\frac{E_\varphi}{m_I},}
\qquad
\boxed{r_m:=\frac{m_{target}}{m_I}}
\]

in natural units.

The matching condition

\[
E_\star=m_{target}
\]

is equivalent to

\[
\boxed{
r_\alpha q_s^3
=\frac{r_m\mu_\varphi}{C_{\Delta/FS}}
=r_m\mu_\varphi\frac{9\sqrt3\pi}{8}.
}
\]

Using the canonical TIR constant

\[
\kappa=\frac{\ln2}{24\pi},
\]

one has the exact rewrite

\[
\boxed{
C_{\Delta/FS}
=\frac{64\kappa}{3\sqrt3\ln2},
}
\]

so equivalently

\[
\boxed{
r_\alpha q_s^3
=r_m\mu_\varphi
\frac{3\sqrt3\ln2}{64\kappa}.
}
\]

RF-S2 refines the coordinate chart of this same equation by introducing

\[
\rho_\omega
=\frac{|\omega_t^\varphi|}{\omega_t^{KG}},
\qquad
\zeta_s=m_I\ell_s,
\]

and proving

\[
\boxed{\mu_\varphi=\rho_\omega,}
\qquad
\boxed{q_s=\rho_\omega\zeta_s}
\]

in the RF-S1 natural-unit convention. Therefore the same target equation becomes

\[
\boxed{
r_\alpha\rho_\omega^2\zeta_s^3
=\frac{r_m}{C_{\Delta/FS}}.}
\]

## 5. Two falsifiable specializations

If the separately gated identifications

\[
\alpha_{clk}=\alpha_I,
\qquad
E_\varphi=m_I,
\qquad
m_{target}=m_I
\]

all pass, then

\[
r_\alpha=\mu_\varphi=r_m=1
\]

and

\[
\boxed{
q_s
=\left(\frac{9\sqrt3\pi}{8}\right)^{1/3}
\approx1.82931154035502.
}
\]

Conversely, if an independent calibration fixes `q_s=1`, then in the unit mass/phase specialization

\[
\boxed{
r_\alpha=\frac{9\sqrt3\pi}{8}\approx6.12157285429049.}
\]

Thus spatial/phase scale calibration and coupling calibration are experimentally distinguishable once either side is fixed independently.

RF-S2 gives a more resolved spectral-match specialization. On

\[
\rho_\omega=1,
\]

one has

\[
\ell_\varphi=1/m_I,
\qquad
q_s=\zeta_s=m_I\ell_s,
\]

so the unit coupling/unit target surface predicts the same numerical value as a dimensionless spatial-mass target,

\[
\boxed{
m_I\ell_s\approx1.82931154035502.}
\]

## 6. Directional physical corollary

RF-E19 supplies, on the future-timelike RFC Noether-current sector,

\[
\beta_e=V_\mu e^\mu,
\qquad
|\beta_e|<1.
\]

If the RF-E17 action contribution is independently promoted as the translational kinetic observable and RF-S1 gives `E_star=m_target c^2`, then

\[
\boxed{
H_{clk}^{(+)}
=m_{target}c^2
\left[
\ln(1-\beta_e)+\frac{\beta_e}{1-\beta_e}
\right]
}
\]

and

\[
\boxed{
H_{clk}^{(-)}
=m_{target}c^2
\left[
\ln(1+\beta_e)-\frac{\beta_e}{1+\beta_e}
\right].
}
\]

The branch shape is inherited from the exact IDT 05D / RF-E14 relative-information construction. RF-S1 supplies the conditional scale closure.

## 7. Falsification ledger

```text
TIR_TETRA_SHAPE_CLASS         PASS TIR PR #104 + PR #105
CLOCK_KL_TO_XI                PASS RF-I1 promoted on RFC main
RF_S2_RATIO_REDUCTION         q_s=rho_omega zeta_s; mu_phi=rho_omega
ALPHA_RATIO                   r_alpha=alpha_clk/alpha_I open calibration
SPATIAL_MASS_COORDINATE       zeta_s=m_I ell_s open physical/continuum binding
PHASE_KG_SPECTRAL_MATCH       rho_omega open independent spectral comparison
TARGET_MASS_BINDING           r_m=m_target/m_I open physical binding
NOETHER_FLOW_DOMAIN           RF-E19 future-timelike sector conditional
OBSERVABLE_SELECTION          H_clk as translational kinetic observable open
DIRECTIONAL_CUBIC_TEST        parity-odd O(beta^3) physical signature open
```

A failed gate localizes the physical interpretation while preserving the exact upstream KL, ADM, current-decomposition and scale-composition identities.

## 8. Validation authority

Reference implementation: `src/rfc/tetra_clock_mass_scale_closure.py`.
Reference tests: `tests/reference/test_rfs1_tetra_clock_mass_scale_closure.py`.
Validation receipt: `validation/RF_S1_TETRA_CLOCK_MASS_SCALE_CLOSURE_V0_1.json`.

RF-S2 reduction authority: `closure/scale/RF_S2_LIGHTCONE_SPECTRAL_SCALE_REDUCTION.md`.
