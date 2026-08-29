# RF-E20 — Tetra / Phase-Clock Mass-Scale Closure

Status: `EXACT_SCALE_COMPOSITION / TIR_PR_104_PARENT_PROMOTED / NOETHER_FLOW_SOURCE_AVAILABLE_CONDITIONAL / PHYSICAL_MASS_BINDINGS_OPEN`

RF-E20 combines the RF-E17 clock-information action scale with the exact tetrahedral FS/spatial shape crosswalk promoted from TIR PR #104. RF-E18 and RF-E19 now separately protect the physical motion interpretation: the ADM shift alone is not a velocity observable, while a future-timelike RFC Noether current can source the local physical speed `beta_phys`.

The purpose is to replace a free energy prefactor by one explicit dimensionless closure equation among already typed coupling, spatial-scale, phase-scale and mass/energy coordinates.

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

RF-E18/RF-E19 replace the old chart-only motion carrier by the physical directional carrier

\[
\boxed{
x_s^{phys}=\frac1{1-s\beta_e},}
\]

where `beta_e=V_mu e^mu` is sourced from a future-timelike RFC Noether flow on the admitted matter sector.

## 2. Tetrahedral dual-shape crosswalk

TIR PR #104 derives on the explicitly typed shared tetrahedral Bloch realization

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

Let `ell_s` be the physical conversion scale of the spatial Pauli/Bloch relation carrier and let

\[
\ell_\varphi=\frac{\hbar c}{E_\varphi}
\]

be the IDT phase-clock length. Define

\[
\boxed{q_s:=\frac{\ell_s}{\ell_\varphi}>0.}
\]

Then

\[
\boxed{
\frac{V_{cell}}{\mathcal A_{rel}}
=C_{\Delta/FS}\,q_s^3\ell_\varphi.
}
\]

The TIR parent is promoted: PR #104 exact head `ea4bfd74e803e00c27d14499d88d7f48b442310a` passed all seven hosted workflows and entered TIR `main` through merge commit `267a6c2022237fcc49284788d7d25c0c3580ff68`.

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

Thus spatial/phase scale calibration and coupling calibration become experimentally distinguishable once either side is fixed independently.

## 6. Directional physical corollary

RF-E19 supplies, on the future-timelike RFC Noether-current sector,

\[
\beta_e=V_\mu e^\mu,
\qquad
|\beta_e|<1.
\]

If the RF-E17 action contribution is independently promoted as the translational kinetic observable and the mass-scale closure gives `E_star=m_target c^2`, then

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

The branch shape is inherited from the exact IDT 05D / RF-E14 relative-information construction. RF-E20 supplies only the conditional scale closure required for the action coefficient to equal the selected mass-energy scale.

## 7. Falsification ledger

```text
TIR_SHARED_TETRA_CARRIER      PASS parent promoted from TIR PR #104
CLOCK_KL_TO_XI                physical/source attribution remains gated
ALPHA_RATIO                   r_alpha=alpha_clk/alpha_I open calibration
SPATIAL_PHASE_SCALE           q_s=ell_s/ell_phi open calibration
PHASE_MASS_RATIO              mu_phi=E_phi/m_I open calibration
TARGET_MASS_BINDING           r_m=m_target/m_I open physical binding
NOETHER_FLOW_DOMAIN           RF-E19 future-timelike sector conditional
OBSERVABLE_SELECTION          H_clk as translational kinetic observable open
DIRECTIONAL_CUBIC_TEST        parity-odd O(beta^3) physical signature open
```

A failed gate localizes the physical interpretation while preserving the exact upstream KL, ADM, current-decomposition and scale-composition identities.

## 8. Validation authority

Reference implementation: `src/rfc/tetra_clock_mass_scale_closure.py`.
Reference tests: `tests/reference/test_rfe20_tetra_clock_mass_scale_closure.py`.
Validation receipt: `validation/RF_E20_TETRA_CLOCK_MASS_SCALE_CLOSURE_V0_1.json`.
