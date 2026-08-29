# RF-E18 — Tetra / Phase-Clock Mass-Scale Closure

Status: `EXACT_SCALE_COMPOSITION / TIR_PR_104_PARENT_PENDING_PROMOTION / PHYSICAL_MASS_BINDINGS_OPEN`

RF-E18 combines the RF-E17 clock-information action scale with the exact tetrahedral FS/spatial shape crosswalk developed in TIR PR #104. The cross-repository parent remains promotion-gated until that exact TIR head passes its complete hosted CI and is promoted.

The purpose is to replace a free kinetic-energy prefactor by one explicit dimensionless closure equation among already typed coupling, spatial-scale, phase-scale and mass/energy coordinates.

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
\Phi(x)=x-1-\ln x,
}
\]

with

\[
x_s=\frac1{1-sb}.
\]

## 2. Tetrahedral dual-shape crosswalk

On the explicitly typed shared tetrahedral Bloch realization, TIR PR #104 derives

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

be the IDT 01L phase-clock length. Define

\[
\boxed{q_s:=\frac{\ell_s}{\ell_\varphi}>0.}
\]

The TIR crosswalk then gives

\[
\boxed{
\frac{V_{cell}}{\mathcal A_{rel}}
=C_{\Delta/FS}\,q_s^3\ell_\varphi.
}
\]

## 3. Coupling-ratio coordinate

RF-L4A gives the canonical local Shannon-Fisher mass relation

\[
\boxed{
\alpha_I=\kappa_E m_I^2.
}
\]

Keep the clock-sector coupling source binding explicit by defining

\[
\boxed{
r_\alpha:=\frac{\alpha_{clk}}{\alpha_I}.}
\]

Then

\[
\frac{\alpha_{clk}}{\kappa_E}
=r_\alpha m_I^2.
\]

Substitution into RF-E17 gives

\[
\boxed{
E_\star
=r_\alpha C_{\Delta/FS}q_s^3
m_I^2\ell_\varphi.
}
\]

Using the IDT phase-clock representation,

\[
\boxed{
E_\star
=r_\alpha C_{\Delta/FS}q_s^3
\frac{m_I^2\hbar c}{E_\varphi}.
}
\]

In natural units `hbar=c=1`,

\[
\boxed{
E_\star
=r_\alpha C_{\Delta/FS}q_s^3
\frac{m_I^2}{E_\varphi}.
}
\]

## 4. Dimensionless closure equation

Define the phase-energy ratio

\[
\boxed{
\mu_\varphi:=\frac{E_\varphi}{m_I}
}
\]

and the target mass ratio

\[
\boxed{
r_m:=\frac{m_{target}}{m_I}
}
\]

in natural units.

The requirement that the RF-E17 action coefficient equal the target kinetic-energy scale,

\[
E_\star=m_{target},
\]

is equivalent to the single dimensionless equation

\[
\boxed{
 r_\alpha\,q_s^3
=\frac{r_m\mu_\varphi}{C_{\Delta/FS}}.
}
\]

Since

\[
\boxed{
\frac1{C_{\Delta/FS}}
=\frac{9\sqrt3\pi}{8},
}
\]

this is

\[
\boxed{
 r_\alpha q_s^3
=r_m\mu_\varphi\frac{9\sqrt3\pi}{8}.
}
\]

Using the canonical TIR constant

\[
\kappa=\frac{\ln2}{24\pi},
\]

one may equivalently write

\[
\boxed{
C_{\Delta/FS}
=\frac{64\kappa}{3\sqrt3\ln2}
}
\]

and therefore

\[
\boxed{
 r_\alpha q_s^3
=r_m\mu_\varphi
\frac{3\sqrt3\ln2}{64\kappa}.
}
\]

The kappa form is an exact algebraic rewrite, not an additional physical premise.

## 5. Unit-binding specialization

If three separately gated identifications pass,

\[
\alpha_{clk}=\alpha_I,
\qquad
E_\varphi=m_I,
\qquad
m_{target}=m_I,
\]

then

\[
r_\alpha=\mu_\varphi=r_m=1
\]

and the closure equation forces

\[
\boxed{
q_s^3=\frac{9\sqrt3\pi}{8}.
}
\]

Hence

\[
\boxed{
q_s
=\left(\frac{9\sqrt3\pi}{8}\right)^{1/3}
\approx1.82931154035502.
}
\]

Thus `ell_s=ell_phi` is not selected by this combined specialization. Under these three bindings, the required spatial conversion scale is approximately `1.82931` times the phase-clock length.

Conversely, if an independent physical calibration gives `q_s=1`, then the closure equation requires

\[
\boxed{
r_\alpha
=\frac{r_m\mu_\varphi}{C_{\Delta/FS}}
}
\]

and in the unit mass/phase specialization

\[
\boxed{
r_\alpha=\frac{9\sqrt3\pi}{8}\approx6.12157285429049.}
\]

The scale and coupling calibrations are therefore experimentally distinguishable rather than freely interchangeable once either one is fixed independently.

## 6. Directional energy corollary

If, in addition to the mass-scale closure above, the physical motion gate establishes

\[
b=\frac vc,
\]

then RF-E17 gives

\[
\boxed{
H_{clk}^{(+)}
=m_{target}c^2
\left[
\ln(1-v/c)+\frac{v/c}{1-v/c}
\right]
}
\]

and

\[
\boxed{
H_{clk}^{(-)}
=m_{target}c^2
\left[
\ln(1+v/c)-\frac{v/c}{1+v/c}
\right]
}
\]

after SI restoration.

The branch shape is already an exact RF-E14 result. RF-E18 only states the conditional scale closure required for the action coefficient to equal the selected mass energy.

## 7. Falsification ledger

The combined route now has separately testable gates:

```text
TIR_SHARED_TETRA_CARRIER     PR #104 exact crosswalk promotion
CLOCK_KL_TO_XI               IDT 05D relative information -> RF-L3 Xi numerator
ALPHA_RATIO                  r_alpha = alpha_clk/alpha_I
SPATIAL_PHASE_SCALE          q_s = ell_s/ell_phi
PHASE_MASS_RATIO             mu_phi = E_phi/m_I
TARGET_MASS_BINDING          r_m = m_target/m_I
SHIFT_VELOCITY               b = v/c
OBSERVABLE_SELECTION         H_clk as translational kinetic observable
DIRECTIONAL_CUBIC_TEST       parity-odd O((v/c)^3) physical signature
```

A failed gate localizes the physical interpretation while preserving the exact upstream KL, ADM and convex-duality identities.

## 8. Validation authority

Reference implementation: `src/rfc/tetra_clock_mass_scale_closure.py`.
Reference tests: `tests/reference/test_rfe18_tetra_clock_mass_scale_closure.py`.
Validation receipt: `validation/RF_E18_TETRA_CLOCK_MASS_SCALE_CLOSURE_V0_1.json`.

The exact TIR parent pinned during construction is PR #104 head `ea4bfd74e803e00c27d14499d88d7f48b442310a`; RFC promotion requires that TIR parent to be fully green and promoted first.
