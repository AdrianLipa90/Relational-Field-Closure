# RF-E17 — Clock-Information Scalar Action Potential

Status: `EXACT_RF_L3_ACTION_ROUTING / RF_I1_INFORMATION_SOURCE_BINDING_PASS_CANDIDATE / RF_E18_E19_PHYSICAL_VELOCITY_SOURCE_PASS_CONDITIONAL / RF_S1_SCALE_CLOSURE_PASS_CONDITIONAL`

RF-E17 asks whether the dimensionless directional relative-information carrier derived along the IDT/RFC rate seam has an admitted route into the RFC action. RF-L3 supplies that scalar-information route. RF-I1 now supplies the explicit Shannon information-curvature source lineage; RF-E18/RF-E19 supply the physical velocity firewall/source; RF-S1 owns the scale-closure line.

## 1. Parent information-scalar action route

RF-L3 uses the natural-log information scalar

\[
\boxed{
\Xi_I=\frac{\mathcal J_I}{\mathcal A_{\rm rel}},
\qquad [\Xi_I]=L^{-2},
}
\]

and reconstructs the RF-L2 scalar potential as

\[
\boxed{
U_I=\frac{\alpha_I}{\kappa_E}\Xi_I.
}
\]

The physical normalization coefficient `alpha_I` retains its own promotion gate.

## 2. Directional information source

RF-E16 supplies the positive gauge-covariant normal phase-rate pair

\[
\boxed{
r_s:=r_n^{(s)}>0,
\qquad
r_0>0,
\qquad
R_s=\frac{r_s}{r_0},
\qquad
x_s=R_s^{-1}=\frac{r_0}{r_s}.
}
\]

IDT 05F gives the Shannon maximum-entropy positive-rate embedding and RF-I1 source-pins it into RFC:

\[
\boxed{
\mathcal J_{\rm clk}^{(s)}
= D_{KL}(\mathfrak E(r_s)\|\mathfrak E(r_0))
=\Phi(x_s),
\qquad
\Phi(x)=x-1-\ln x.
}
\]

IDT 05E supplies the finite-01C refinement lineage, and RF-I1 therefore gives

\[
\boxed{
\Xi_{\rm clk}^{(s)}
=\frac{\mathcal J_{\rm clk}^{(s)}}{\mathcal A_{\rm rel}}
=\frac{\Phi(x_s)}{\mathcal A_{\rm rel}}.
}
\]

This is the RF-L3 information-curvature type. The earlier source-attribution target `CLOCK_KL_TO_XI` is owned and resolved by RF-I1 at the information/source-typing level.

## 3. RF-L3 potential reconstruction

Applying the RF-L3 map gives

\[
\boxed{
U_{\rm clk}^{(s)}
=\frac{\alpha_{\rm clk}}{\kappa_E\mathcal A_{\rm rel}}
\Phi(x_s).
}
\]

On the RF-E16 local directional specialization,

\[
R_s=1-sb,
\qquad
x_s=\frac1{1-sb},
\]

so the chart representation is

\[
\boxed{
U_{\rm clk}^{(+)}
=\frac{\alpha_{\rm clk}}{\kappa_E\mathcal A_{\rm rel}}
\left[
\ln(1-b)+\frac{b}{1-b}
\right],
}
\]

\[
\boxed{
U_{\rm clk}^{(-)}
=\frac{\alpha_{\rm clk}}{\kappa_E\mathcal A_{\rm rel}}
\left[
\ln(1+b)-\frac{b}{1+b}
\right].
}
\]

RF-E18 keeps this chart representation separate from the physical velocity observable.

## 4. Homogeneous-cell integrated energy coordinate

On a local homogeneous cell with physical spatial volume `V_cell`,

\[
\boxed{
H_{\rm clk}^{(s)}
=V_{\rm cell}U_{\rm clk}^{(s)}
=E_\star\Phi(x_s),
}
\]

where

\[
\boxed{
E_\star
:=\frac{\alpha_{\rm clk}}{\kappa_E}
\frac{V_{\rm cell}}{\mathcal A_{\rm rel}}.
}
\]

In natural units,

\[
[\kappa_E]=L^2,
\qquad
[V/A]=L,
\]

so

\[
\boxed{[E_\star]=L^{-1}=\text{energy}.}
\]

RF-S1 supplies the dedicated scale-composition equation for this prefactor using the TIR tetrahedral shape crosswalk, the phase-clock length, the RF-L4A mass coordinate and explicit coupling/scale ratios.

## 5. Physical velocity source and Newtonian calibration target

RF-E18 establishes the ADM velocity firewall. For a material/worldline coordinate rate `w^i`,

\[
\boxed{V^i=\frac{w^i+b^i}{N},}
\qquad
\boxed{\beta_{\rm phys}^2=h_{ij}V^iV^j.}
\]

RF-E19 source-binds this velocity, on the future-timelike RFC Noether-current sector, through

\[
\boxed{V^\mu=\frac{j^\mu}{q},}
\qquad
q=-n_\mu J^\mu>0,
\qquad
\beta_{\rm phys}^2=\frac{j_\mu j^\mu}{q^2}<1.
\]

For an oriented local physical direction `e`, define

\[
\beta_e=V_\mu e^\mu,
\qquad |\beta_e|<1,
\]

and the physical directional carrier

\[
\boxed{x_s^{\rm phys}=\frac1{1-s\beta_e}.}
\]

The corresponding information branch has expansion

\[
\boxed{
\Phi(x_s^{\rm phys})
=\frac12\beta_e^2+s\frac23\beta_e^3+\frac34\beta_e^4+O(\beta_e^5).
}
\]

If the integrated scalar-potential contribution is selected by the downstream observable gate as translational kinetic energy, matching its leading term to

\[
\frac12m v^2
=\frac12mc^2\beta_e^2
\]

gives the scale target

\[
\boxed{E_\star=mc^2.}
\]

RF-S1 rewrites this target as a dimensionless coupling/spatial/phase/mass-scale closure equation.

## 6. Relation to the existing phase-energy carrier

RF-E16 independently gives the same directional phase-rate ratio

\[
R_s=\frac{r_s}{r_0}
\]

inside the canonical phase-energy sector,

\[
\frac{\epsilon_N^{(s)}}{\epsilon_0}=R_s,
\qquad
\frac{\mathcal E_\vartheta^{(s)}}{\mathcal E_{\vartheta,0}}=R_s^2.
\]

RF-I1 supplies the information-scalar action coordinate on the reciprocal rate,

\[
\boxed{
H_{\rm clk}^{(s)}/E_\star
=\Phi(R_s^{-1}).
}
\]

The bridge therefore contains the typed three-channel dictionary

```text
phase Noether energy/carrier     ~ R_s
phase kinetic energy density     ~ R_s^2
information-scalar action energy ~ Phi(1/R_s)
```

The measured observable is selected by the corresponding action/source sector and the downstream experiment.

## 7. Current promotion frontier

The dependency state after RF-I1, RF-E18, RF-E19 and RF-S1 is

```text
RF-E16 positive phase-rate source                         PASS
IDT 05F Shannon rate-information embedding                PASS
IDT 05E finite-01C refinement lineage                     PASS
RF-I1 CLOCK_KL_TO_XI information/source binding           PASS CANDIDATE
RF-E18 coordinate/physical-velocity firewall              PASS
RF-E19 timelike Noether-flow beta_phys source             PASS CONDITIONAL
RF-S1 E_star scale-composition equation                   PASS CONDITIONAL
PHYSICAL_PROJECTIVE_CELL_SELECTION                        OPEN
ALPHA_CLK / ALPHA_I CALIBRATION                           OPEN
RF-S1 SPATIAL / PHASE SCALE CALIBRATION                   OPEN
TIMELIKE DOMAIN ACROSS TARGET MATTER SECTOR                OPEN
TRANSLATIONAL_OBSERVABLE SELECTION                        OPEN
DIRECTIONAL DISPERSION / CUBIC EXPERIMENT                 OPEN
```

## 8. Evidence boundary

RF-E17 carries the exact RF-L3 functional route with its source lineage now supplied by RF-I1. RF-E18/RF-E19 govern physical motion typing; RF-S1 governs scale composition. Physical cell selection, coupling calibration, target-sector domain, observable assignment and experimental comparison remain independently gated.

Reference implementation: `src/rfc/clock_information_scalar_action.py`.
Reference tests: `tests/reference/test_rfe17_clock_information_scalar_action.py`.
Validation receipt: `validation/RF_E17_CLOCK_INFORMATION_SCALAR_ACTION_V0_1.json`.

Current cross-repository information source gate: RF-I1.
Current scale gate: RF-S1.
