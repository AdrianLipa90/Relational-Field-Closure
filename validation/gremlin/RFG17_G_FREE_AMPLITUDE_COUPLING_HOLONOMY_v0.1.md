# RFG17 — G-Free Amplitude Coupling Holonomy

Status: `EXACT_ALGEBRAIC_CROSS_ROUTE_REDUCTION / PROJECT_AMPLITUDE_PREFATOR_BOUND / PHYSICAL_INPUTS_REMAIN_GATED`

RFG17 combines RFG16, RFG7, RF-N1C2 and RF-N1C3. It introduces no numerical value of Newton's constant.

RFG16 gives the project four-point double-copy amplitude

\[
\mathcal M_4^{project}
=i\kappa_E\sum_i\frac{n_i\tilde n_i}{D_i}
\]

with

\[
\boxed{\kappa_E=\frac1{\bar M_G^2}=8\pi G}
\]

in natural units.

RF-N1C3 gives the independently typed horizon/thermal reduced-scale relation

\[
\boxed{\bar M_G^2=M_HT_H=\frac{M_H\kappa_H}{2\pi}.}
\]

Therefore, on the common admitted surface,

\[
\boxed{\kappa_E=\frac1{M_HT_H}}
\]

and

\[
\boxed{
\mathcal M_4^{project}
=\frac{i}{M_HT_H}\sum_i\frac{n_i\tilde n_i}{D_i}.
}
\]

No numerical `G` is required to state or test this cross-route prediction.

RFG4G/RFG7 and the local phase-carrier candidate give

\[
\bar M_G=\frac{\alpha_cM_\star}{\Gamma_{DC}},
\qquad
M_\star=\frac{\omega_Q}{2},
\]

hence

\[
\boxed{\bar M_G=\frac{\alpha_c\omega_Q}{2\Gamma_{DC}}}
\]

and therefore

\[
\boxed{\kappa_E=\frac{4\Gamma_{DC}^2}{\alpha_c^2\omega_Q^2}.}
\]

Combining local carrier and horizon routes gives the zero-fit coupling holonomy

\[
\boxed{
\frac{4\Gamma_{DC}^2}{\alpha_c^2\omega_Q^2}
=\frac1{M_HT_H}.
}
\]

Equivalently,

\[
\boxed{
\Gamma_{DC}
=\frac{\alpha_c\omega_Q}{2\sqrt{M_HT_H}}.
}
\]

The executable reference verifies the `kappa_g`, reduced-scale, horizon and local-carrier parameterizations of the same Einstein/amplitude coupling, including 1000 deterministic random cross-route samples.

Local result:

```text
6 passed, 0 failed
```

The result is an exact algebraic cross-route reduction on the stated admitted surfaces. Independent physical promotion of `M_star`, horizon inputs, `Gamma_DC` and cross-system universality remains evidence-gated.
