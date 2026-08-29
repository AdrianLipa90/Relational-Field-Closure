# RF-E19 — Tetra / Phase-Clock Mass-Scale Closure

Status: `EXACT_SCALE_COMPOSITION / TIR_TETRA_PARENT_PROMOTED / RF_E18_PHYSICAL_BETA_PARENT_PROMOTED / PHYSICAL_MASS_BINDINGS_OPEN`

RF-E19 combines four already gated structures:

1. RF-E17 clock-information scalar action routing;
2. RF-E18 gauge firewall and physical normal-relative velocity carrier;
3. RF-L4A Shannon-Fisher mass normalization;
4. the promoted TIR tetrahedral FS/spatial shape crosswalk.

Its purpose is to replace the remaining free energy prefactor by one explicit dimensionless closure equation among coupling, spatial-scale, phase-scale and mass/energy coordinates.

## 1. Physical directional carrier from RF-E18

RF-E18 defines the normal-observer relative spatial velocity

\[
V^i=\frac{w^i+b^i}{N}
\]

and the physical scalar speed

\[
\boxed{\beta_{phys}^2=h_{ij}V^iV^j.}
\]

In a local orthonormal frame `beta_phys=v_phys/c`. With an independent orientation label `s=+-1`, the gauge-invariant directional carrier is

\[
\boxed{
x_s^{phys}=\frac1{1-s\beta_{phys}}.}
\]

The relative-information generator is

\[
\boxed{\Phi(x)=x-1-\ln x,}
\]

so

\[
\boxed{
\Phi_s^{phys}
=\ln(1-s\beta_{phys})
+\frac{s\beta_{phys}}{1-s\beta_{phys}}.
}
\]

This replaces the earlier shortcut from a coordinate shift to velocity. Source-binding the relevant material congruence remains a separate matter-sector gate.

## 2. RF-E17 action energy scale

RF-E17 gives the homogeneous-cell action contribution

\[
\boxed{
H_{clk}^{(s)}
=E_\star\Phi_s^{phys},
}
\]

with

\[
\boxed{
E_\star
=\frac{\alpha_{clk}}{\kappa_E}
\frac{V_{cell}}{\mathcal A_{rel}}.
}
\]

## 3. Promoted TIR tetrahedral dual-shape crosswalk

TIR PR #104 passed 7/7 hosted workflows and was promoted to `main` as commit

`267a6c2022237fcc49284788d7d25c0c3580ff68`.

On its explicitly typed shared tetrahedral Bloch realization it derives

\[
\hat V_{\Delta^3}=\frac{8}{9\sqrt3},
\qquad
 a_{FS}^{tet}=\pi,
\]

and therefore

\[
\boxed{
C_{\Delta/FS}
:=\frac{\hat V_{\Delta^3}}{a_{FS}^{tet}}
=\frac{8}{9\sqrt3\pi}.
}
\]

Let `ell_s` be the physical conversion scale of the spatial Pauli/Bloch relation carrier and let IDT 01L supply

\[
\ell_\varphi=\frac{\hbar c}{E_\varphi}.
\]

Define

\[
\boxed{q_s:=\frac{\ell_s}{\ell_\varphi}>0.}
\]

The promoted TIR crosswalk gives

\[
\boxed{
\frac{V_{cell}}{\mathcal A_{rel}}
=C_{\Delta/FS}\,q_s^3\ell_\varphi.
}
\]

The TIR informational-SIC to physical-spatial-cell promotion remains separately typed; RF-E19 consumes the crosswalk only on the admitted shared-cell realization.

## 4. Coupling-ratio coordinate

RF-L4A gives

\[
\boxed{\alpha_I=\kappa_E m_I^2.}
\]

Keep the clock-sector source binding explicit:

\[
\boxed{r_\alpha:=\frac{\alpha_{clk}}{\alpha_I}.}
\]

Then

\[
\frac{\alpha_{clk}}{\kappa_E}=r_\alpha m_I^2
\]

and hence

\[
\boxed{
E_\star
=r_\alpha C_{\Delta/FS}q_s^3
m_I^2\ell_\varphi.
}
\]

Using IDT 01L,

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

## 5. Dimensionless mass-scale closure equation

Define in natural units

\[
\boxed{\mu_\varphi:=\frac{E_\varphi}{m_I}},
\qquad
\boxed{r_m:=\frac{m_{target}}{m_I}}.
\]

Requiring the RF-E17 action coefficient to equal the selected target mass scale,

\[
E_\star=m_{target},
\]

is equivalent to

\[
\boxed{
 r_\alpha q_s^3
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

we obtain

\[
\boxed{
 r_\alpha q_s^3
=r_m\mu_\varphi\frac{9\sqrt3\pi}{8}.
}
\]

With canonical

\[
\kappa=\frac{\ln2}{24\pi},
\]

the same exact relation is

\[
\boxed{
C_{\Delta/FS}
=\frac{64\kappa}{3\sqrt3\ln2},
}
\]

\[
\boxed{
 r_\alpha q_s^3
=r_m\mu_\varphi
\frac{3\sqrt3\ln2}{64\kappa}.
}
\]

The kappa form is an algebraic crosswalk to the canonical TIR normalization.

## 6. Unit-binding specialization

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
q_s
=\left(\frac{9\sqrt3\pi}{8}\right)^{1/3}
\approx1.82931154035502.
}
\]

Thus this specialization predicts a nontrivial spatial/phase-clock conversion ratio.

Conversely, if an independent physical calibration gives `q_s=1`, the same specialization requires

\[
\boxed{
r_\alpha
=\frac{9\sqrt3\pi}{8}
\approx6.12157285429049.}
\]

Once either the coupling ratio or scale ratio is independently fixed, the other becomes a falsifiable target.

## 7. Directional action-energy corollary

When the mass-scale closure has been satisfied, RF-E18 supplies the physical directional carrier directly through `beta_phys=v_phys/c` in the local orthonormal frame. The action contribution becomes

\[
\boxed{
H_{clk}^{(+)}
=m_{target}c^2
\left[
\ln(1-v_{phys}/c)
+\frac{v_{phys}/c}{1-v_{phys}/c}
\right]
}
\]

and

\[
\boxed{
H_{clk}^{(-)}
=m_{target}c^2
\left[
\ln(1+v_{phys}/c)
-\frac{v_{phys}/c}{1+v_{phys}/c}
\right]
}
\]

after SI restoration.

The logarithmic/rational branch shape is inherited from the already promoted information/ADM chain. RF-E19 supplies only the scale-closure condition required for the action coefficient to equal the selected mass energy.

## 8. Remaining promotion ledger

```text
TIR_TETRA_SHAPE_CROSSWALK    PASS / TIR main 267a6c20...
RF_E18_PHYSICAL_BETA         PASS kinematic firewall / material source conditional
CLOCK_KL_TO_XI               IDT 05D relative information -> RF-L3 Xi numerator
TETRA_SIC_TO_SPATIAL_CELL    shared informational/spatial physical realization
MATERIAL_CONGRUENCE          physical moving carrier -> RFC matter sector
ALPHA_RATIO                  r_alpha = alpha_clk/alpha_I
SPATIAL_PHASE_SCALE          q_s = ell_s/ell_phi
PHASE_MASS_RATIO             mu_phi = E_phi/m_I
TARGET_MASS_BINDING          r_m = m_target/m_I
OBSERVABLE_SELECTION         H_clk as translational kinetic observable
DIRECTIONAL_CUBIC_TEST       parity-odd O(beta_phys^3) experimental signature
```

A failed gate localizes the physical interpretation while preserving the exact upstream KL, ADM, gauge and convex-duality identities.

## 9. Validation authority

Reference implementation: `src/rfc/tetra_clock_mass_scale_closure.py`.
Reference tests: `tests/reference/test_rfe19_tetra_clock_mass_scale_closure.py`.
Validation receipt: `validation/RF_E19_TETRA_CLOCK_MASS_SCALE_CLOSURE_V0_1.json`.

Next frontier: source-bind the material congruence and independently determine `r_alpha`, `q_s`, `mu_phi`, and `r_m` from upstream TIR/IDT/RFC observables rather than from the target energy law.
