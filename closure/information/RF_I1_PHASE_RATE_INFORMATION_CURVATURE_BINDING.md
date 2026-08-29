# RF-I1 — Phase-Rate Information-Curvature Source Binding

Status: `EXACT_IDT_05F_TO_01K_NUMERATOR_BINDING / RF_E16_PHASE_RATE_SOURCE_PIN / RF_L3_ACTION_ROUTE_PASS / PHYSICAL_AREA_AND_OBSERVABLE_GATES_OPEN`

## 1. Purpose

RF-E16 source-pins the RF-E14 directional carrier to the gauge-covariant normal phase-rate sector,

\[
R_s=\frac{r_n^{(s)}}{r_0}>0,
\qquad
x_s=R_s^{-1}=\frac{r_0}{r_n^{(s)}}.
\]

RF-E17 then uses the candidate information-curvature scalar

\[
\Xi_{clk}^{(s)}=\frac{\Phi(x_s)}{\mathcal A_{rel}},
\qquad
\Phi(x)=x-1-\ln x,
\]

but its source attribution `CLOCK_KL_TO_XI` was left open.

IDT 05E and 05F now close the missing information lineage. RF-I1 composes those promoted parents into RFC without identifying the ADM shift with a physical velocity and without requiring the phase rate to equal the IDT activity lapse.

Promoted IDT parent:

```text
IDT main commit = feb8c92ffb8605c0057a29356c9e1da9c09b8d47
05E = finite 01C refinement completion
05F = Shannon maximum-entropy positive-rate embedding
```

## 2. RF-E16 phase-rate source

On the admitted local directional phase sector,

\[
\boxed{
r_s:=r_n^{(s)}>0,
\qquad
r_0>0,
\qquad
R_s=\frac{r_s}{r_0},
\qquad
x_s=\frac{r_0}{r_s}.
}
\]

RF-E16 independently derives, in its local orthonormal directional specialization,

\[
R_s=1-sb,
\qquad
x_s=\frac1{1-sb}.
\]

The source used by RF-I1 is the positive phase-rate pair `(r_s,r_0)`, not the coordinate shift by itself.

## 3. IDT 05F Shannon rate embedding

IDT 05F associates any positive rate `r` with the unique maximum-Shannon-entropy positive-time representative with reciprocal mean `1/r`,

\[
\boxed{f_r(t)=r e^{-rt}.}
\]

For two rates `a,b`,

\[
\boxed{
\mathcal J_{rate}(a\|b)
=D_{KL}(f_a\|f_b)
=\ln\frac ab+\frac ba-1
=\Phi\!\left(\frac ba\right).
}
\]

Taking

\[
a=r_s,
\qquad
b=r_0,
\]

gives

\[
\boxed{
\mathcal J_{phase}^{(s)}
:=\mathcal J_{rate}(r_s\|r_0)
=\Phi\!\left(\frac{r_0}{r_s}\right)
=\Phi(x_s).
}
\]

05E supplies the finite-01C refinement completion of this continuous relative-information scalar, so `J_phase^(s)` has the 01K natural-log numerator type.

The maximum-entropy embedding is an information representation of the positive rate. A physical exponential dwell-time law is a separate optional realization and is not required for this source-binding theorem.

## 4. 01K information-curvature binding

01K defines

\[
\Xi_I=\frac{\mathcal J_\pi}{\mathcal A_{rel}},
\qquad
[\mathcal A_{rel}]=L^2.
\]

RF-I1 therefore defines the phase-rate information curvature

\[
\boxed{
\Xi_{phase}^{(s)}
:=\frac{\mathcal J_{phase}^{(s)}}{\mathcal A_{rel}}
=\frac{\Phi(x_s)}{\mathcal A_{rel}}.
}
\]

Hence

\[
\boxed{[\Xi_{phase}^{(s)}]=L^{-2}.}
\]

This is the exact RF-E17 `Xi_clk^(s)` source form.

## 5. Constant phase-clock cell

01K supplies, on a constant-rate projective cell,

\[
\mathcal A_{rel}^{(P)}
=\frac{c^2}{\omega_P^2}a_{FS}^{(P)}.
\]

On the RF-E16 zero-direction reference patch choose the same calibrated normal phase-rate magnitude

\[
\boxed{\omega_P=r_0.}
\]

Then

\[
\boxed{
\mathcal A_{rel}^{(P)}
=\frac{c^2}{r_0^2}a_{FS}^{(P)},
}
\]

and

\[
\boxed{
\Xi_{phase}^{(s,P)}
=
\frac{\Phi(x_s)}{a_{FS}^{(P)}}
\left(\frac{r_0}{c}\right)^2.
}
\]

The dimensionless information branch and the inverse-area phase-clock scale are thus explicitly separated.

Selection of the physical projective cell remains the existing 01K/TIR calibration gate.

## 6. RF-L3 / RF-E17 action route

RF-L3 admits the information-curvature potential map

\[
\boxed{
\Delta\Lambda_I=\alpha_I\Xi_I,
\qquad
U_I=\frac{\alpha_I}{\kappa_E}\Xi_I.
}
\]

For the clock/phase-rate branch retain the separately typed coefficient `alpha_clk` used by RF-E17. Substituting the RF-I1 source gives

\[
\boxed{
U_{clk}^{(s)}
=\frac{\alpha_{clk}}{\kappa_E}\Xi_{phase}^{(s)}
=\frac{\alpha_{clk}}
       {\kappa_E\mathcal A_{rel}}
  \Phi(x_s).
}
\]

This is exactly the RF-E17 scalar-action potential.

For a homogeneous admitted cell,

\[
H_{clk}^{(s)}
=U_{clk}^{(s)}V_{cell}
=E_\star\Phi(x_s),
\]

with

\[
\boxed{
E_\star
=\frac{\alpha_{clk}}{\kappa_E}
\frac{V_{cell}}{\mathcal A_{rel}}.
}
\]

RF-S1 separately owns the physical scale closure of this prefactor.

## 7. Source-binding verdict

The former RF-E17 open item

```text
CLOCK_KL_TO_XI_SOURCE_BINDING
```

is resolved at the information/source-typing level by the exact chain

```text
RF-E16 positive phase-rate pair (r_s,r_0)
 -> IDT 05F Shannon maximum-entropy rate embedding
 -> IDT 05E finite-01C refinement lineage
 -> J_phase^(s)=Phi(r_0/r_s)
 -> 01K numerator type
 -> Xi_phase^(s)=J_phase^(s)/A_rel
 -> RF-L3 potential map
 -> RF-E17 U_clk^(s)
```

No equality `x_s=N_R` is used. The activity-clock branch and the phase-rate branch are specializations of the same IDT 05F positive-rate information geometry.

## 8. Remaining physical gates

RF-I1 closes the information-curvature source attribution. The remaining promotion frontier is:

```text
PHYSICAL_PROJECTIVE_CELL_SELECTION
ALPHA_CLK / ALPHA_I CALIBRATION
RF-S1 SPATIAL / PHASE SCALE CALIBRATION
RF-E19 TIMELIKE MATTER-FLOW DOMAIN
TRANSLATIONAL_OBSERVABLE_SELECTION
DIRECTIONAL DISPERSION / CUBIC EXPERIMENT
```

RF-E18/RF-E19 continue to govern the physical velocity interpretation. The RF-I1 theorem concerns the gauge-covariant positive phase-rate carrier and its Shannon information curvature.

Reference implementation: `src/rfc/phase_rate_information_curvature.py`.
Reference tests: `tests/reference/test_rfi1_phase_rate_information_curvature.py`.
Validation receipt: `validation/RF_I1_PHASE_RATE_INFORMATION_CURVATURE_V0_1.json`.
