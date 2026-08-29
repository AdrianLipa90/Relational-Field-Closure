# RF-S2 — Light-Cone Spectral Scale Reduction

Status: `EXACT_PHASE_KG_SPECTRAL_RATIO / EXACT_PHASE_LENGTH_REDUCTION / RF_S1_TWO_RATIO_REDUCTION / SPATIAL_MASS_COORDINATE_OPEN_PHYSICAL_BINDING / SPECTRAL_MATCH_OPEN`

RF-S2 reduces the scale coordinates carried by RF-S1 using two already admitted parents:

1. RFC RF-L5A, which calibrates the premetric homogeneous Klein–Gordon mode to physical time;
2. IDT 01L, which defines the phase-clock length from an independently admitted calibrated phase rate.

The gate keeps the phase-clock spectral line and the RFC homogeneous Klein–Gordon line separately measurable through one explicit dimensionless ratio.

## 1. RFC homogeneous mass frequency

RF-L5A supplies, on one local affine calibration patch,

\[
t-t_\star=\Gamma_t(\lambda-\lambda_\star),
\qquad \Gamma_t>0,
\]

and the positive homogeneous premetric gap

\[
\omega_{\lambda,KG}=\mu_\lambda>0.
\]

Its calibrated physical frequency is

\[
\boxed{
\omega_t^{KG}=\frac{\mu_\lambda}{\Gamma_t}=c\,m_I,
}
\]

where

\[
\boxed{m_I^2=\frac{\alpha_I}{\kappa_E}}
\]

is the RFC inverse-length mass coordinate.

## 2. Independent phase-clock line

Let the IDT phase clock on the same calibrated physical-time patch have ordering-coordinate phase rate

\[
\omega_{\lambda,\varphi}:=\frac{d\varphi}{d\lambda},
\qquad |\omega_{\lambda,\varphi}|>0.
\]

The chain rule gives

\[
\boxed{
\omega_t^{\varphi}
=\frac{\omega_{\lambda,\varphi}}{\Gamma_t}.
}
\]

Define the dimensionless spectral ratio

\[
\boxed{
\rho_\omega
:=\frac{|\omega_t^{\varphi}|}{\omega_t^{KG}}
=\frac{|\omega_{\lambda,\varphi}|}{\mu_\lambda}>0.
}
\]

Because both rates use the same calibrated clock, `Gamma_t` cancels exactly.

## 3. Phase-clock length reduction

IDT 01L gives

\[
\ell_\varphi=\frac{c}{|\omega_t^{\varphi}|}.
\]

Using

\[
|\omega_t^{\varphi}|=\rho_\omega c m_I,
\]

one obtains

\[
\boxed{
\ell_\varphi=\frac{1}{\rho_\omega m_I}.
}
\]

Equivalently,

\[
\boxed{
m_I\ell_\varphi=\rho_\omega^{-1}.}
\]

Thus the IDT phase-clock length and the RFC inverse-length mass coordinate are linked by the directly auditable spectral ratio.

## 4. Phase-energy ratio

IDT 01L also gives the admitted phase-energy calibration

\[
E_\varphi=\hbar|\omega_t^{\varphi}|.
\]

Hence

\[
\boxed{
E_\varphi=\rho_\omega\,\hbar c\,m_I.
}
\]

Define the dimensionless physical phase/mass energy ratio

\[
\boxed{
\widehat\mu_\varphi
:=\frac{E_\varphi}{\hbar c\,m_I}.
}
\]

Then exactly

\[
\boxed{\widehat\mu_\varphi=\rho_\omega.}
\]

In the natural-unit convention used by RF-S1, `hbar=c=1`, this is the RF-S1 coordinate

\[
\boxed{\mu_\varphi=E_\varphi/m_I=\rho_\omega.}
\]

## 5. RF-S1 spatial/phase ratio

RF-S1 defines

\[
q_s:=\frac{\ell_s}{\ell_\varphi}.
\]

Introduce the dimensionless spatial mass coordinate

\[
\boxed{
\zeta_s:=m_I\ell_s>0.
}
\]

Using the phase-length identity above,

\[
\boxed{
q_s=\rho_\omega\zeta_s.
}
\]

Therefore the RF-S1 pair `(q_s, mu_phi)` reduces to

```text
spectral ratio             rho_omega
spatial mass coordinate    zeta_s = m_I ell_s
mu_phi                      = rho_omega          [natural units]
q_s                         = rho_omega zeta_s
```

The phase-clock scale is no longer an independent coordinate after the two calibrated frequencies are supplied.

## 6. Premetric light-cone representation of the spatial coordinate

RF-L5A additionally supplies

\[
\frac{\Gamma_x}{\Gamma_t}=\frac{c}{\sqrt{M_{eff}}},
\qquad
\mu_\lambda=\Gamma_t c m_I.
\]

Define the positive spatial-coordinate normalization

\[
\boxed{
\sigma_x:=\frac{\ell_s}{\Gamma_x}.
}
\]

Then

\[
\boxed{
\zeta_s
=m_I\ell_s
=\sigma_x\frac{\mu_\lambda}{\sqrt{M_{eff}}}.
}
\]

and therefore

\[
\boxed{
q_s
=\rho_\omega\sigma_x
\frac{\mu_\lambda}{\sqrt{M_{eff}}}.
}
\]

This is the exact premetric/light-cone representation of the RF-S1 scale ratio. The coordinate normalization `sigma_x` is retained explicitly until the TIR spatial carrier is bound to the RFC/IDT continuum coordinate.

## 7. Reduction of the RF-S1 mass-scale equation

RF-S1 gives in natural units

\[
E_\star
=r_\alpha C_{\Delta/FS}q_s^3
\frac{m_I^2}{E_\varphi},
\]

with

\[
C_{\Delta/FS}=\frac{8}{9\sqrt3\pi},
\qquad
r_\alpha=\frac{\alpha_{clk}}{\alpha_I}.
\]

Substituting

\[
q_s=\rho_\omega\zeta_s,
\qquad
E_\varphi=\rho_\omega m_I,
\]

gives the exact reduced scale law

\[
\boxed{
E_\star
=r_\alpha C_{\Delta/FS}
\rho_\omega^2\zeta_s^3\,m_I.
}
\]

For a selected target

\[
m_{target}=r_m m_I,
\]

the RF-S1 target equation becomes

\[
\boxed{
r_\alpha\rho_\omega^2\zeta_s^3
=\frac{r_m}{C_{\Delta/FS}}
=r_m\frac{9\sqrt3\pi}{8}.
}
\]

This replaces the RF-S1 equation in `(q_s,mu_phi)` by a relation in independently typed coupling, spectral and spatial-mass coordinates.

Solving for the spatial coordinate,

\[
\boxed{
\zeta_s
=\left(
\frac{r_m}{C_{\Delta/FS}r_\alpha\rho_\omega^2}
\right)^{1/3}.
}
\]

## 8. Spectral-match specialization

On the separately testable surface

\[
\boxed{\rho_\omega=1,}
\]

the independent phase-clock line coincides with the calibrated RFC homogeneous KG line. The scale identities reduce to

\[
\boxed{
\ell_\varphi=\frac1{m_I},
\qquad
q_s=\zeta_s=m_I\ell_s,
}
\]

and

\[
\boxed{
r_\alpha\zeta_s^3=\frac{r_m}{C_{\Delta/FS}}.}
\]

If the separately typed unit coupling and unit target-ratio surfaces are also selected,

\[
r_\alpha=r_m=1,
\]

then

\[
\boxed{
\zeta_s=C_{\Delta/FS}^{-1/3}
=\left(\frac{9\sqrt3\pi}{8}\right)^{1/3}
\approx1.82931154035502.
}
\]

This number is a conditional dimensionless spatial-mass target `m_I ell_s`.

## 9. Promotion ledger

Promoted/exact inputs:

```text
RF-L5A affine clock calibration                    PASS
RF-L5A omega_t^KG = c m_I                         PASS
IDT 01L ell_phi = c/|omega_t^phi|                 PASS
IDT 01L E_phi = hbar |omega_t^phi|                PASS GIVEN PHASE-ENERGY CALIBRATION
RF-S1 tetra/FS shape coefficient                   PASS
TIR tetrahedral congruence-class shape closure     PASS
```

RF-S2 exact outputs:

```text
rho_omega = |omega_lambda^phi|/mu_lambda           PASS EXACT
ell_phi = 1/(rho_omega m_I)                        PASS EXACT
mu_phi_hat = rho_omega                             PASS EXACT
zeta_s = m_I ell_s                                 TYPED
q_s = rho_omega zeta_s                             PASS EXACT
zeta_s = sigma_x mu_lambda/sqrt(M_eff)             PASS EXACT
RF-S1 reduced target equation                      PASS EXACT
```

Next physical gates:

```text
PHASE_KG_SPECTRAL_MATCH        measure/derive rho_omega
TIR_CONTINUUM_COORDINATE_BIND  determine sigma_x or ell_s
CLOCK_ALPHA_BINDING            determine r_alpha
TARGET_MASS_BINDING            determine r_m
TRANSLATIONAL_OBSERVABLE       select measured energy observable
DIRECTIONAL_CUBIC_TEST          compare the parity-odd branch prediction
```

## 10. Validation authority

Reference implementation: `src/rfc/lightcone_spectral_scale_reduction.py`.
Reference tests: `tests/reference/test_rfs2_lightcone_spectral_scale_reduction.py`.
Validation receipt: `validation/RF_S2_LIGHTCONE_SPECTRAL_SCALE_REDUCTION_V0_1.json`.

Parent RFC main at branch creation: `1a351a3dec2beb4371190fa040925a985aa6ce3d`.
IDT source main inspected for 01L: `ed902458b6e0ad338ca4ba637d8d8228bc7c549b`.
TIR tetrahedral congruence-class closure: merge commit `ccc89fc04e1d85e9c6a60b7bb92e62a5d22d5f44`.
