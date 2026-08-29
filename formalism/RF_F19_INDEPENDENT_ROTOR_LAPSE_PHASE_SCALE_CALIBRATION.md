# RF-F19 — Independent Rotor-Lapse Phase-Scale Calibration

Status: `IDT_INDEPENDENT_RATE_CALIBRATION_EXACT_CONDITIONAL / METRIC_VARIATION_VS_SPACETIME_EVOLUTION_FIREWALL_EXACT / RF_F18_PROJECTOR_ROUNDTRIP_PASS / RF_F3_PHASE_CELL_REWRITE_EXACT_CONDITIONAL / RF_F12_F15_SCALING_ROUNDTRIP_PASS`

RF-F19 is stacked on RF-F18. It closes the phase-clock projector scale from the independently evaluated IDT rotor/lapse rate and separates metric-variation independence from ordinary spacetime evolution.

## 1. Independent field and rotor rates

IDT 01AC provides the gauge-covariant field pullback rate

\[
r_t^{field}:=q^*(\mathscr D\vartheta)(\partial_t).
\]

The rotor route independently evaluates

\[
r_t^{rot}:=D_t\chi.
\]

IDT 01AC/01AD audit their equality rather than constructing it by assignment. Define

\[
\boxed{
\Delta_t
:=
\frac{|r_t^{field}-r_t^{rot}|}{|r_t^{rot}|}
}
\]

on the nonzero rotor-rate sector.

IDT 01AD supplies the relational lapse `N_R>0` and proper rotor rate

\[
\boxed{r_{\tau}^{rot}:=\frac{r_t^{rot}}{N_R}.}
\]

For an independently evaluated field proper rate `r_tau^field`, define

\[
\boxed{
\Delta_\tau
:=
\frac{|r_\tau^{field}-r_\tau^{rot}|}{|r_\tau^{rot}|}.
}
\]

The common rate surface is

\[
\boxed{\Delta_t=\Delta_\tau=0.}
\]

## 2. Independent phase-clock calibration

Define

\[
\boxed{
\mu_\vartheta
:=
\frac{|r_t^{rot}|}{N_Rc}
=
\frac{|r_\tau^{rot}|}{c}.
}
\]

This calibration uses the independently evaluated rotor rate and the activity-derived lapse, rather than the metric norm of the RF-F18 field one-form.

On the pure-normal field branch,

\[
-g^{-1}(q,q)
=
\left(\frac{|r_\tau^{field}|}{c}\right)^2.
\]

Therefore RF-F18 becomes

\[
\boxed{
\mathcal C_\vartheta
=
\left(
\frac{r_\tau^{field}}{r_\tau^{rot}}
\right)^2.
}
\]

Hence

\[
\boxed{
\Delta_\tau=0
\quad\Longrightarrow\quad
\mathcal C_\vartheta=1.
}
\]

The unit projector surface is therefore reached by an independently audited field↔rotor rate equality, not by self-normalizing `q_mu` with its own metric norm.

## 3. Metric variation versus spacetime evolution

The phase scale may evolve over spacetime while remaining an independent input during the local metric variation.

Define

\[
S_{\mu\nu}^{rot}
:=
\frac{\partial\ln|r_t^{rot}|}{\partial g^{\mu\nu}},
\qquad
S_{\mu\nu}^{N}
:=
\frac{\partial\ln N_R}{\partial g^{\mu\nu}}.
\]

Then

\[
\boxed{
S_{\mu\nu}^{\vartheta}
:=
\frac{\partial\ln\mu_\vartheta}{\partial g^{\mu\nu}}
=
S_{\mu\nu}^{rot}-S_{\mu\nu}^{N}.
}
\]

The RF-F18 independent-scale branch is the exact conditional surface

\[
\boxed{S_{\mu\nu}^{\vartheta}=0.}
\]

In particular, independently frozen rotor-rate and lapse inputs give

\[
S_{\mu\nu}^{rot}=S_{\mu\nu}^{N}=0
\quad\Longrightarrow\quad
S_{\mu\nu}^{\vartheta}=0.
\]

By contrast, along physical evolution,

\[
\boxed{
\frac{d\ln\mu_\vartheta}{d\tau}
=
\frac{d\ln|r_t^{rot}|}{d\tau}
-
\frac{d\ln N_R}{d\tau}
}
\]

may be nonzero. Therefore

```text
metric functional response of mu_vartheta = 0
```

and

```text
spacetime evolution of mu_vartheta != 0
```

are compatible statements on the same branch.

## 4. General scale-response correction

RF-F18 used independent `mu_vartheta`. If its metric response is retained, then for

\[
\mathcal C_\vartheta
=-g^{-1}(q,q)/\mu_\vartheta^2
\]

the full derivative is

\[
\boxed{
\frac{\partial\mathcal C_\vartheta}{\partial g^{\mu\nu}}
=
-\frac{q_\mu q_\nu+2R_{\mu\nu}}{\mu_\vartheta^2}
-2\mathcal C_\vartheta S_{\mu\nu}^{\vartheta}.
}
\]

Thus the RF-F17 `eta=1` stress receives the additional exact correction

\[
\boxed{
\Delta T^{(S)}_{\mu\nu}
=
4\widehat U_L f'(1)
\mathcal C_\vartheta S_{\mu\nu}^{\vartheta}.
}
\]

On the RF-F19 independent-variation surface `S_vartheta=0`, the RF-F18 tensor is recovered exactly.

## 5. Common proper phase rate and RF-F3

On the admitted IDT 01AD proper-rate binding and the RFC RF-F3 common phase-rate identification,

\[
|\omega|
=
|D_{\hat\tau}\chi|
=
|r_\tau^{rot}|.
\]

Therefore

\[
\boxed{|\omega|=c\mu_\vartheta.}
\]

This is a conditional cross-representation equality: it uses the same proper phase-clock rate on the IDT and RFC surfaces.

## 6. Phase-cell geometry in the calibrated scale

RF-F3 gives

\[
V_R=a_{FS}\frac{c^3}{|\omega|^3}.
\]

Using `|omega|=c mu_vartheta`,

\[
\boxed{
V_R
=
\frac{a_{FS}}{\mu_\vartheta^3}.
}
\]

For occupation `N`,

\[
\boxed{
n
=
\frac{\mathcal N}{V_R}
=
\frac{\mathcal N\mu_\vartheta^3}{a_{FS}}.
}
\]

Thus the independent phase-clock calibration is simultaneously the inverse relational-cell length scale.

## 7. RF-F15 microscopic scaling rewrite

RF-F15 gives

\[
A^2
=
\frac{q_0\mathcal N}{2a_{FS}c^3}|\omega|^2.
\]

Hence

\[
\boxed{
A^2
=
\frac{q_0\mathcal N}{2a_{FS}c}
\mu_\vartheta^2.
}
\]

The normal kinetic density becomes

\[
K=A^2|\omega|^2
\propto\mu_\vartheta^4.
\]

The RF-F15 solution families therefore read

\[
\boxed{
\rho_{rad}\propto\mu_\vartheta^4,
\qquad
\rho_{dust}\propto\mu_\vartheta^3,
\qquad
\rho_{vac}=\mathrm{constant}.
}
\]

## 8. FLRW roundtrip

RF-F12 supplies

\[
a|\omega|=\mathrm{constant}.
\]

Using `|omega|=c mu_vartheta`,

\[
\boxed{a\mu_\vartheta=\mathrm{constant}.}
\]

Consequently,

\[
\boxed{
\rho_{rad}\propto a^{-4},
\qquad
\rho_{dust}\propto a^{-3},
\qquad
\rho_{vac}\propto a^0,
}
\]

recovering the RF-F12/RF-F15 cosmological scaling through the independent projector calibration.

## 9. Promotion ledger

```text
independent field/rotor coordinate-rate defect Delta_t       PASS EXACT COORDINATE
independent proper-rate defect Delta_tau                      PASS EXACT COORDINATE
mu_vartheta=|r_t^rot|/(N_R c)                                PASS EXACT DEFINITION
Delta_tau=0 -> C_vartheta=1 on pure-normal branch             PASS EXACT CONDITIONAL
self-norm tautology avoided by independent rotor/lapse route  PASS EXACT
S_vartheta=S_rot-S_N metric-response ledger                   PASS EXACT
S_vartheta=0 independent-variation branch                     PASS EXACT CONDITIONAL
nonzero spacetime d ln mu/dtau compatible with S_vartheta=0   PASS EXACT TYPING
scale-response correction to projector derivative             PASS EXACT
scale-response correction to eta=1 stress                     PASS EXACT
common IDT/RFC proper rate -> |omega|=c mu_vartheta           PASS EXACT CONDITIONAL
V_R=a_FS/mu_vartheta^3                                        PASS EXACT
n=N mu_vartheta^3/a_FS                                        PASS EXACT
RF-F15 radiation/dust/vacuum mu-scaling                       PASS EXACT CONDITIONAL
RF-F12 a mu_vartheta=constant                                 PASS EXACT CONDITIONAL
hosted independent field/rotor rate receipt                   OPEN PHYSICAL INPUT
off-shell S_rotor and S_N metric-response receipts            OPEN PHYSICAL INPUT
common IDT 01AD <-> RFC RF-F3 proper-rate lineage             OPEN PHYSICAL INPUT
```

## 10. Validation authority

Reference implementation: `src/rfc/independent_rotor_lapse_calibration.py`.

Reference tests: `tests/reference/test_rff19_independent_rotor_lapse_calibration.py`.

Validation receipt: `validation/RF_F19_INDEPENDENT_ROTOR_LAPSE_CALIBRATION_V0_1.json`.
