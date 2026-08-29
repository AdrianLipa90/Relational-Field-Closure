# RF-E14 — ADM Directional Relative-Entropy Potential

Status: `EXACT_ADM_KINEMATIC_COMPOSITION / IDT_05D_CONDITIONAL_PARENT / ENERGY_BINDING_OPEN`

This gate combines the promoted RF-E8 ADM kinematics with the IDT 05D relative-information clock potential. The external two-branch kinetic-energy formulas are not used as premises.

## 1. Local orthonormal 1+1 ADM chart

RF-E8 supplies

\[
 ds^2=-N^2(dx^0)^2+h_{11}(dx+b\,dx^0)^2.
\]

At a selected local orthonormal event choose

\[
N=1,\qquad h_{11}=1.
\]

Then

\[
\boxed{ds^2=-(dx^0)^2+(dx+b\,dx^0)^2.}
\]

For a null characteristic `ds^2=0`, write

\[
u:=\frac{dx}{dx^0}.
\]

The two exact roots are

\[
\boxed{u_\to=1-b,\qquad u_\leftarrow=-(1+b).}
\]

For the subluminal shift domain

\[
|b|<1,
\]

the positive directional rate magnitudes relative to the unshifted local null rate are

\[
\boxed{r_\to=1-b,\qquad r_\leftarrow=1+b.}
\]

Define reciprocal traversal factors

\[
\boxed{x_\to=\frac1{1-b},\qquad x_\leftarrow=\frac1{1+b}.}
\]

## 2. Composition with the IDT/RFC information potential

IDT 05D supplies, on its explicitly admitted local memoryless clock realization,

\[
\boxed{\Phi(x)=x-1-\ln x.}
\]

Evaluate the same scalar generator on the two positive ADM reciprocal directional factors:

\[
\mathcal I_\to(b):=\Phi(x_\to),
\qquad
\mathcal I_\leftarrow(b):=\Phi(x_\leftarrow).
\]

This gives exactly

\[
\boxed{
\mathcal I_\to(b)
=\ln(1-b)+\frac{b}{1-b},
}
\]

and

\[
\boxed{
\mathcal I_\leftarrow(b)
=\ln(1+b)-\frac{b}{1+b}.
}
\]

Thus the two logarithmic/rational branches arise from one relative-information generator evaluated on the two null-direction traversal factors of an ADM chart with shift.

## 3. Parity conjugacy

The branch pair obeys

\[
\boxed{\mathcal I_\to(b)=\mathcal I_\leftarrow(-b).}
\]

Define

\[
\mathcal A(b)
=\frac{\mathcal I_\to+\mathcal I_\leftarrow}{2},
\qquad
\mathcal B(b)
=\frac{\mathcal I_\to-\mathcal I_\leftarrow}{2}.
\]

Then

\[
\boxed{\mathcal A(-b)=\mathcal A(b),}
\qquad
\boxed{\mathcal B(-b)=-\mathcal B(b).}
\]

With

\[
\gamma=(1-b^2)^{-1/2},
\qquad
\eta=\operatorname{artanh}b,
\]

one obtains

\[
\boxed{x_\to=\gamma e^{\eta},\qquad x_\leftarrow=\gamma e^{-\eta},}
\]

and

\[
\boxed{\mathcal A=\gamma^2-1-\ln\gamma,}
\]

\[
\boxed{\mathcal B=b\gamma^2-\eta.}
\]

The pair therefore separates into an even magnitude-like coordinate and an odd orientation-like coordinate, matching the GREMLIN XFI.08 structural grammar without promoting that analogy as a theorem dependency.

## 4. Low-shift expansion

For `|b|<1`,

\[
\boxed{
\mathcal I_\to
=\frac12b^2+\frac23b^3+\frac34b^4+\frac45b^5+O(b^6),
}
\]

\[
\boxed{
\mathcal I_\leftarrow
=\frac12b^2-\frac23b^3+\frac34b^4-\frac45b^5+O(b^6).
}
\]

The common leading term is quadratic. The first directional discriminator is cubic.

## 5. Energy-scale calibration candidate

At RF-E14 the quantities `I_to` and `I_leftarrow` remain dimensionless relative-information potentials.

Introduce only a generic positive energy scale `E_*`:

\[
\mathcal E_\pm=E_*\mathcal I_\pm.
\]

If a downstream Hamiltonian/Noether gate identifies this relative-information carrier with translational kinetic energy and independently requires the Newtonian small-speed calibration

\[
\mathcal E=\frac12mv^2+o(v^2),
\qquad b=\frac vc,
\]

then the quadratic coefficient forces

\[
\boxed{E_*=mc^2.}
\]

Under those downstream bindings only,

\[
\mathcal E_\to
=mc^2\left[\ln(1-v/c)+\frac{v/c}{1-v/c}\right],
\]

\[
\mathcal E_\leftarrow
=mc^2\left[\ln(1+v/c)-\frac{v/c}{1+v/c}\right].
\]

The formulas above are therefore an exact corollary of `ADM directional rates + Phi` plus the explicitly listed physical scale and shift/velocity bindings. RF-E14 itself promotes only the dimensionless kinematic-information result.

## 6. Source-binding firewalls

The following remain distinct gates:

1. `b -> v/c`: physical relative-motion realization of the ADM shift coordinate;
2. `IDT activity carrier -> physical memoryless hazard`: IDT 05D realization gate;
3. `Phi -> Hamiltonian/Noether energy`: action-level physical binding;
4. `E_* -> mc^2`: independently derived or experimentally calibrated energy scale;
5. laboratory comparison of the parity-odd cubic term against relativistic observables.

TIR SE(3) affine source binding already supplies a candidate local-frame displacement-rate contribution to `b^i`; RF-E14 does not promote the complete physical shift map.

## 7. Discriminating comparison

For standard special-relativistic kinetic energy,

\[
\frac{E_{SR}}{mc^2}=\gamma-1
=\frac12b^2+\frac38b^4+O(b^6),
\]

which is even in `b`.

The RF-E14 directional information pair has an odd cubic splitting. If RF-E15 promotes the energy binding, this difference becomes a direct falsification target rather than a convention choice.

## 8. Validation authority

Reference implementation: `src/rfc/adm_directional_relative_entropy.py`.
Reference tests: `tests/reference/test_rfe14_adm_directional_relative_entropy.py`.
Validation receipt: `validation/RF_E14_ADM_DIRECTIONAL_RELATIVE_ENTROPY_V0_1.json`.

Next gate: RF-E15 — derive or reject the action/Hamiltonian/Noether binding of the dimensionless relative-information potential without assuming the desired kinetic-energy formula.
