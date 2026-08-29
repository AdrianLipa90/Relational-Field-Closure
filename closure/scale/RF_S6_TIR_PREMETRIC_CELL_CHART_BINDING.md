# RF-S6 — TIR / Premetric Cell-Chart Binding

Status: `EXACT_CELL_SCALE_CANCELLATION / CONDITIONAL_TIR_RFC_CHART_BINDING / SIGMA_X_UNIT_CROSSWALK / ZETA_PREMETRIC_REDUCTION / COUPLING_SPECTRAL_TARGET`

RF-S6 consumes the TIR normalized tetrahedral spatial carrier together with the RF-L5A premetric cell calibration and the RF-S2/RF-S4 scale reductions.

The gate tests one precise chart statement: whether the dimensionless RF-L5A cell coordinate is source-bound to the same normalized TIR relation-length coordinate used to define the physical spatial conversion scale `ell_s`.

## 1. TIR normalized tetrahedral edge

The promoted TIR tetrahedral spatial/FS crosswalk gives the normalized regular-tetrahedron edge

\[
\boxed{
\hat a=\sqrt{\frac83}.
}
\]

Let `ell_s>0` be the physical length conversion attached to the normalized TIR Pauli/Bloch spatial relation carrier. The physical edge is

\[
\boxed{
L_\Delta=\ell_s\hat a.
}
\]

TIR keeps `ell_s` as the physical unit map from its dimensionless local carrier.

## 2. RF-L5A premetric cell calibration

RF-L5A introduces a dimensionless premetric cell-coordinate increment `h>0` and its physical image `L_h>0`, with

\[
\boxed{
\Gamma_x=\frac{L_h}{h}.
}
\]

The affine spatial calibration is

\[
X-X_\star=\Gamma_x(\xi-\xi_\star).
\]

Thus `Gamma_x` is the physical length conversion per unit premetric cell coordinate.

## 3. TIR/RFC cell-chart source binding

Define the chart-binding surface by assigning the RF-L5A cell increment to the same normalized TIR tetrahedral edge and its physical image:

\[
\boxed{
h=\hat a,
\qquad
L_h=L_\Delta=\ell_s\hat a.
}
\]

Then exactly

\[
\Gamma_x
=\frac{\ell_s\hat a}{\hat a}.
\]

Since `hat(a)>0`,

\[
\boxed{
\Gamma_x=\ell_s.
}
\]

RF-S2 defines

\[
\sigma_x:=\frac{\ell_s}{\Gamma_x}.
\]

Therefore the cell-chart binding gives

\[
\boxed{
\sigma_x=1.
}
\]

The normalized tetrahedral edge cancels. The result depends on common chart attribution rather than on the numerical value of `hat(a)`.

## 4. Executable chart defects

Define

\[
\boxed{
\Delta_h:=\left|\frac{h}{\hat a}-1\right|,
}
\]

and

\[
\boxed{
\Delta_L
:=\left|\frac{L_h}{\ell_s\hat a}-1\right|.
}
\]

The common cell-chart surface is

\[
\boxed{
\Delta_h=\Delta_L=0.
}
\]

On this surface,

\[
\boxed{
\Delta_\sigma:=|\sigma_x-1|=0.
}
\]

These coordinates allow the TIR normalized cell, the premetric cell coordinate and the physical cell width to be supplied independently in an executable audit.

## 5. RF-S2 spatial mass coordinate

RF-S2 gives

\[
\boxed{
\zeta_s:=m_I\ell_s
=\sigma_x\frac{\mu_\lambda}{\sqrt{M_{eff}}}.
}
\]

On the RF-S6 chart-binding surface `sigma_x=1`,

\[
\boxed{
\zeta_s
=\frac{\mu_\lambda}{\sqrt{M_{eff}}}.
}
\]

Define the dimensionless premetric scale coordinate

\[
\boxed{
\eta_{pm}
:=\frac{\mu_\lambda}{\sqrt{M_{eff}}}>0.
}
\]

Then

\[
\boxed{
\zeta_s=\eta_{pm}.
}
\]

## 6. Exact RF-L5A roundtrip

RF-L5A also gives

\[
\mu_\lambda=\Gamma_t c m_I
\]

on the positive mass branch and

\[
\frac{\Gamma_x}{\Gamma_t}
=\frac{c}{\sqrt{M_{eff}}}.
\]

Therefore

\[
\frac{\mu_\lambda}{\sqrt{M_{eff}}}
=\frac{\Gamma_t c m_I}{\sqrt{M_{eff}}}
=m_I\Gamma_x.
\]

Using the RF-S6 cell-chart result `Gamma_x=ell_s`,

\[
\boxed{
\frac{\mu_\lambda}{\sqrt{M_{eff}}}
=m_I\ell_s
=\zeta_s.
}
\]

Thus the TIR cell map and the RF-L5A light-cone/mass calibration independently close the same dimensionless spatial-mass coordinate.

## 7. RF-S4 same-mass target reduction

RF-S4 supplies, on its admitted radial source-binding/action-equivalence surface,

\[
m_\Psi=m_I.
\]

For the same selected matter target,

\[
m_{target}=m_\Psi,
\]

RF-S3/RF-S4 gives

\[
r_m=\rho_\omega=r_{\Psi I}=1.
\]

The RF-S3 target equation is then

\[
\boxed{
r_\alpha\zeta_s^3
=\frac1{C_{\Delta/FS}},
}
\]

with

\[
C_{\Delta/FS}=\frac{8}{9\sqrt3\pi}.
\]

Substituting the RF-S6 premetric coordinate,

\[
\boxed{
 r_\alpha
\left(\frac{\mu_\lambda}{\sqrt{M_{eff}}}\right)^3
=\frac{9\sqrt3\pi}{8}.
}
\]

This is the reduced premetric scale/coupling target.

## 8. Coupling target form

Solving for the remaining coupling ratio gives

\[
\boxed{
 r_\alpha
=\frac1{C_{\Delta/FS}}
\left(\frac{\sqrt{M_{eff}}}{\mu_\lambda}\right)^3.
}
\]

Equivalently, for an independently supplied `r_alpha`,

\[
\boxed{
\eta_{pm}
=\left(
\frac1{C_{\Delta/FS}r_\alpha}
\right)^{1/3}.
}
\]

On the separately gated unit-coupling surface

\[
r_\alpha=1,
\]

the premetric target becomes

\[
\boxed{
\frac{\mu_\lambda}{\sqrt{M_{eff}}}
=C_{\Delta/FS}^{-1/3}
=\left(\frac{9\sqrt3\pi}{8}\right)^{1/3}
\approx1.82931154035502.
}
\]

## 9. Role of the chart binding

RF-S6 promotes a coordinate crosswalk:

```text
TIR normalized cell increment     hat(a)
RF-L5A premetric cell increment   h
TIR physical image                ell_s hat(a)
RF-L5A physical image             L_h
```

The zero-defect source binding assigns the same dimensionless cell and the same physical edge to both descriptions. The resulting `Gamma_x=ell_s` removes the intermediate chart factor `sigma_x` from RF-S2.

The remaining premetric coordinate `eta_pm=mu_lambda/sqrt(M_eff)` is then exactly the physical dimensionless spatial-mass product `m_I ell_s` on the calibrated patch.

## 10. Promotion ledger

Promoted/exact parents:

```text
TIR regular tetrahedral normalized edge hat(a)=sqrt(8/3)   PASS
TIR physical length scale map L_Delta=ell_s hat(a)          TYPED SCALE MAP
RF-L5A Gamma_x=L_h/h                                        PASS EXACT
RF-L5A light-cone ratio                                     PASS EXACT
RF-L5A positive mass-slot relation                          PASS EXACT
RF-S2 zeta_s=sigma_x mu_lambda/sqrt(M_eff)                  PASS
RF-S4 same-mass consequence                                 CONDITIONAL SOURCE-BINDING SURFACE
```

RF-S6 outputs on the common cell-chart surface:

```text
Gamma_x=ell_s                                               PASS EXACT
sigma_x=1                                                   PASS EXACT
zeta_s=mu_lambda/sqrt(M_eff)                                PASS EXACT
RF-L5A roundtrip m_I ell_s=mu_lambda/sqrt(M_eff)            PASS EXACT
premetric scale/coupling target                             PASS EXACT GIVEN RF-S4 TARGET SURFACE
```

Remaining physical gates:

```text
TIR_RFC_CELL_CHART_SOURCE_BINDING
RADIAL_INFORMATION_SOURCE_BINDING
CLOCK_RADIAL_ACTION_COMPOSITION
CLOCK_ALPHA_BINDING
TRANSLATIONAL_OBSERVABLE
DIRECTIONAL_CUBIC_TEST
GENERAL_MATTER_MULTIPLET
VARIABLE_LAPSE_GLOBAL_EXTENSION
```

## 11. Validation authority

Reference implementation: `src/rfc/tir_premetric_cell_chart_binding.py`.
Reference tests: `tests/reference/test_rfs6_tir_premetric_cell_chart_binding.py`.
Validation receipt: `validation/RF_S6_TIR_PREMETRIC_CELL_CHART_BINDING_V0_1.json`.

Parent RFC main at branch creation: `466d364f3d903215b94e2ba66e1fd1fac23e7a30`.
TIR source main inspected at: `ccc89fc06bdf42c1937c0a2303d3e477db487e0f`.
