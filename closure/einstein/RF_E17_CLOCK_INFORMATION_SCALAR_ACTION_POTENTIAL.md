# RF-E17 — Clock-Information Scalar Action Potential

Status: `EXACT_RF_L3_ACTION_ROUTING_CONDITIONAL / CLOCK_KL_TO_XI_SOURCE_BINDING_OPEN / MASS_SCALE_BINDING_OPEN`

RF-E17 asks whether the dimensionless directional clock relative information derived in IDT 05D / RF-E14 has an already admitted route into the RFC action.

RF-L3 supplies exactly such a scalar-information route.

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

## 2. Clock relative-information source candidate

IDT 05D supplies the exact dimensionless clock relative information

\[
\boxed{
\mathcal J_{\rm clk}(x)=\Phi(x)=x-1-\ln x.
}
\]

RF-E14/RF-E16 supplies the directional ADM/phase realization

\[
\boxed{x_s=\frac1{1-sb},\qquad s\in\{+1,-1\}.}
\]

Introduce an explicit typed source-binding candidate

\[
\boxed{
\Xi_{\rm clk}^{(s)}
:=\frac{\mathcal J_{\rm clk}(x_s)}{\mathcal A_{\rm rel}}
=\frac{\Phi(x_s)}{\mathcal A_{\rm rel}}.
}
\]

This gate requires the clock-KL carrier to be admitted into the same RFC information-scalar type used by RF-L3. The exact functional consequences below are conditional on that source binding.

## 3. RF-L3 potential reconstruction

Applying the RF-L3 map gives

\[
\boxed{
U_{\rm clk}^{(s)}
=\frac{\alpha_{\rm clk}}{\kappa_E\mathcal A_{\rm rel}}
\Phi(x_s).
}
\]

For the two directional factors,

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

Thus the RF-E14 branch shape enters the already admitted RF-L2/RF-L3 scalar-potential action route without changing its functional form.

## 4. Homogeneous-cell integrated energy coordinate

On a local homogeneous cell with physical spatial volume `V_cell`, the scalar-potential contribution integrates to

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

The bridge therefore supplies an action-level energy scale from the scalar coupling and the cell volume-to-area ratio.

## 5. Newtonian calibration equation

RF-E14 gives

\[
\Phi(x_s)
=\frac12b^2+s\frac23b^3+\frac34b^4+O(b^5).
\]

If the independently gated physical shift realization gives

\[
b=\frac vc
\]

and the integrated scalar-potential contribution is selected as the translational kinetic-energy observable, then matching the leading Newtonian coefficient

\[
H_{\rm clk}=\frac12mv^2+o(v^2)
\]

forces

\[
\boxed{E_\star=mc^2.}
\]

Equivalently, the geometric/coupling binding target is

\[
\boxed{
\frac{\alpha_{\rm clk}}{\kappa_E}
\frac{V_{\rm cell}}{\mathcal A_{\rm rel}}
=mc^2.
}
\]

In natural units this is `alpha_clk V/(kappa_E A)=m`.

This is now a falsifiable mass-scale equation rather than an arbitrary multiplicative insertion.

## 6. Relation to the existing phase-energy carrier

RF-E16 independently gives the same directional rate ratio

\[
R_s=1-sb
\]

inside the canonical phase-energy sector,

\[
\frac{\epsilon_N^{(s)}}{\epsilon_0}=R_s,
\qquad
\frac{\mathcal E_\vartheta^{(s)}}{\mathcal E_{\vartheta,0}}=R_s^2.
\]

RF-E17 supplies a separate scalar-potential coordinate on the reciprocal rate,

\[
\boxed{
H_{\rm clk}^{(s)}/E_\star=\Phi(R_s^{-1}).
}
\]

The bridge therefore contains a typed three-channel dictionary on one source-bound directional rate:

```text
phase Noether energy/carrier     ~ R_s
phase kinetic energy density     ~ R_s^2
information-scalar action energy ~ Phi(1/R_s)
```

The physical observable assignment is controlled by the action/source sector being measured.

## 7. Promotion gates

The RF-E17 exact functional routing is conditional on four explicit source/scale gates:

1. `CLOCK_KL_TO_XI`: admit the IDT 05D clock KL as an RF-L3 information-scalar numerator;
2. `SHIFT_TO_PHYSICAL_VELOCITY`: source-bind the local ADM shift ratio to the measured relative velocity coordinate;
3. `CELL_SCALE`: derive or measure `V_cell/A_rel` from the TIR/RFC spatial carrier;
4. `ALPHA_CLK`: derive or calibrate the scalar coupling.

If these gates fix

\[
E_\star=mc^2,
\]

the two logarithmic/rational energy branches follow from the RFC action-potential route as a direct corollary.

## 8. Evidence boundary

RF-E17 promotes the exact RF-L3 functional pullback and the homogeneous-cell energy-scale identity on the stated source binding. The mass/velocity/observable assignment remains a separately testable physical promotion surface.

Reference implementation: `src/rfc/clock_information_scalar_action.py`.
Reference tests: `tests/reference/test_rfe17_clock_information_scalar_action.py`.
Validation receipt: `validation/RF_E17_CLOCK_INFORMATION_SCALAR_ACTION_V0_1.json`.

Next gate: RF-E18 — derive the cell scale `V_cell/A_rel` and `alpha_clk` from the upstream TIR tetrahedral/spatial carrier and existing RFC normalization coordinates, then compare the resulting `E_star` with independently bound mass/rest-energy scales.
