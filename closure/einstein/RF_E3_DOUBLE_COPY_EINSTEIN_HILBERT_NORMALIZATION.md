# RF-E3 — Double-Copy to Einstein–Hilbert Action Normalization

Status: `EXACT_ACTION_NORMALIZATION_TRANSFER / STANDARD_METRIC_VARIATION_PASS / DOUBLE_COPY_PROJECT_BINDINGS_CONDITIONAL / DYNAMIC_LAMBDA_ACTION_GATE_OPEN`

RF-E3 consumes RF-N1C after the geometric Einstein spine of RF-02I/RF-E0 is already present. Its role is to transfer the independently gated double-copy graviton normalization into the coefficient of the full Einstein–Hilbert action.

## 1. Coupling coordinates

In natural units the double-copy/graviton convention is

\[
\boxed{\kappa_g^2=32\pi G.}
\]

RF-N1C gives the Einstein field-equation coupling

\[
\boxed{\kappa_E=8\pi G=\frac{\kappa_g^2}{4}.}
\]

Therefore

\[
\boxed{
\frac{1}{2\kappa_E}=\frac{2}{\kappa_g^2}.
}
\]

This equality is the action-normalization bridge.

## 2. Einstein–Hilbert action

Define

\[
\boxed{
S_{EH}[g]
=\frac{1}{2\kappa_E}
\int d^4x\sqrt{-g}\,R
=\frac{2}{\kappa_g^2}
\int d^4x\sqrt{-g}\,R.
}
\]

For the standard stress-energy definition

\[
\boxed{
T_{\mu\nu}
=-\frac{2}{\sqrt{-g}}
\frac{\delta S_m}{\delta g^{\mu\nu}},
}
\]

the metric variation of the gravitational action, after the standard boundary term is handled, is

\[
\delta S_{EH}
=\frac{1}{2\kappa_E}
\int d^4x\sqrt{-g}\,G_{\mu\nu}\,\delta g^{\mu\nu}.
\]

The matter variation is

\[
\delta S_m
=-\frac12
\int d^4x\sqrt{-g}\,T_{\mu\nu}\,\delta g^{\mu\nu}.
\]

Stationarity therefore gives

\[
\boxed{
G_{\mu\nu}=\kappa_E T_{\mu\nu}.
}
\]

Thus the same coupling coordinate that closes the RF-N1C Newton normalization fixes the full tensor equation through the Einstein–Hilbert action coefficient.

## 3. Project double-copy coordinates

RFG2 supplies

\[
\kappa_g
=\frac{2\Gamma_{DC}g_{YM}^2}{M_\star}
\]

for the self-copy candidate.

On the separately gated RF-N1B2N carrier-scale surface

\[
M_\star=\epsilon_Q=\frac12\omega_Q,
\qquad
\omega_Q=D_{\hat\tau}\chi,
\]

one obtains

\[
\boxed{
\kappa_g
=\frac{4\Gamma_{DC}g_{YM}^2}{\omega_Q}.
}
\]

Therefore

\[
\boxed{
\kappa_E^{DC}
=\frac{\kappa_g^2}{4}
=\frac{4\Gamma_{DC}^2g_{YM}^4}{\omega_Q^2}.
}
\]

Using the Wilson coordinate

\[
g_{YM}^2=\frac6{\beta_W},
\]

this becomes

\[
\boxed{
\kappa_E^{DC}
=\frac{144\Gamma_{DC}^2}
{\beta_W^2\omega_Q^2}.
}
\]

The corresponding Einstein–Hilbert coefficient is

\[
\boxed{
A_{EH}^{DC}
:=\frac{1}{2\kappa_E^{DC}}
=\frac{\beta_W^2\omega_Q^2}
{288\Gamma_{DC}^2}.
}
\]

Equivalently,

\[
\boxed{
A_{EH}^{DC}=\frac{2}{\kappa_g^2}.
}
\]

## 4. Newton limit as the same normalization

RF-N1C gives, in natural units,

\[
\rho_m=\frac12\omega_Qj_Q
\]

on the promoted source-carrier surface.

The weak-field `00` equation from the same action gives

\[
\Delta\Phi_R=\frac{\kappa_E}{2}\rho_m.
\]

Substituting `kappa_E^DC` yields

\[
\boxed{
\mathcal S_R^{DC}
=\frac{36\Gamma_{DC}^2}
{\beta_W^2\omega_Q}\,j_Q,
}
\]

identical to the RF-N1C source↔double-copy relation.

Thus the tensor action normalization and the Newton-source normalization close on one coupling coordinate.

## 5. Dynamic Lambda0 insertion

For a scalar coordinate `Lambda0(x)`, the metric-side action coordinate is

\[
\boxed{
S_{g,\Lambda}
=\frac{1}{2\kappa_E}
\int d^4x\sqrt{-g}\,[R-2\Lambda_0(x)].
}
\]

Metric variation at fixed scalar field gives

\[
\boxed{
G_{\mu\nu}+\Lambda_0g_{\mu\nu}
=\kappa_ET_{\mu\nu}.
}
\]

The contracted Bianchi identity then reproduces the RF-E0 transfer coordinate

\[
\boxed{
\kappa_E\nabla^\mu T_{\mu\nu}
=\nabla_\nu\Lambda_0.
}
\]

The action-level dynamics assigned to `Lambda0` itself remains the next independently gated sector, including its own variation, source exchange and stability conditions.

## 6. Exact normalization triangle

RF-E3 records one exact normalization triangle:

\[
\boxed{
\kappa_g^2
=4\kappa_E
=32\pi G
}
\]

in natural units, and therefore

\[
\boxed{
\frac{2}{\kappa_g^2}
=\frac{1}{2\kappa_E}
=\frac{1}{16\pi G}.
}
\]

Restoring SI units on the field-equation side gives

\[
\boxed{
\kappa_E=\frac{8\pi G}{c^4}.
}
\]

## 7. Promotion surface

RF-E3 consumes the same independent physical gates as RF-N1C for the project-side value of the coupling:

- project Yang–Mills/Wilson normalization;
- project BCJ-compatible kinematic numerators;
- double-copy normalization `Gamma_DC`;
- carrier-scale binding `M_star=epsilon_Q`;
- physical RFC source-carrier/matter binding;
- cross-system Newton universality.

The metric-variation theorem and the algebraic coefficient transfers are exact on their stated conventions.

The author/repository/formalism/code may suggest a complete action-level Einstein normalization from the gauge/double-copy route, yet does not state that physical promotion as an established result until the project-side coupling gates pass with frozen provenance.

## 8. Advancement

The Einstein bridge now has the chain

```text
project gauge sector
 -> beta_W, BCJ numerators, Gamma_DC
 -> kappa_g
 -> kappa_E = kappa_g^2/4
 -> A_EH = 2/kappa_g^2 = 1/(2 kappa_E)
 -> metric variation
 -> G_mu_nu = kappa_E T_mu_nu
 -> weak-field RF-N1C source law
```

The remaining action frontier is the physical project-side promotion of the coupling coordinates and the independent dynamical action for `Lambda0`.
