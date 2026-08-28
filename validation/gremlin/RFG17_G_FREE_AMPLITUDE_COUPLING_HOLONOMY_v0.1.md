# RFG17 — G-Free Amplitude Coupling Holonomy

Status: `EXACT_ALGEBRAIC_CROSS_ROUTE_REDUCTION / PROJECT_CORE_PREFACTOR_CORRECTED_RFG20 / PHYSICAL_KAPPA_E_HOLONOMY_PRESERVED / PHYSICAL_INPUTS_REMAIN_GATED`

RFG17 combines RFG16, RFG7, RF-N1C2 and RF-N1C3. It introduces no numerical value of Newton's constant. RFG20 fixes the explicit normalization of the RFG15 project numerator core; the physical Einstein coupling holonomy remains unchanged.

## 1. Physical coupling holonomy

The physical Einstein coupling is

\[
\boxed{
\kappa_E
=\frac{\kappa_g^2}{4}
=\frac1{\bar M_G^2}
=8\pi G
}
\]

in natural units.

RF-N1C3 gives the independently typed horizon/thermal reduced-scale relation

\[
\boxed{\bar M_G^2=M_HT_H=\frac{M_H\kappa_H}{2\pi}.}
\]

Therefore, on the common admitted surface,

\[
\boxed{\kappa_E=\frac1{M_HT_H}.}
\]

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

and

\[
\boxed{\kappa_E=\frac{4\Gamma_{DC}^2}{\alpha_c^2\omega_Q^2}.}
\]

Combining local carrier and horizon routes gives the zero-fit physical coupling holonomy

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
=\frac{\alpha_c\omega_Q}{2\sqrt{M_HT_H}}
}
\]

on the explicit kinetic-carrier type surface. RF-N1C4 separately keeps the carrier-scale type open.

## 2. Project-normalized amplitude core

RFG20 verifies that the RFG15 project numerators carry an absorbed `sqrt(2)` per cubic vertex. Therefore RFG16 uses

\[
\boxed{
\mathcal M_4^{project}
=-i\frac{\kappa_E}{4}
\sum_i\frac{n_i\tilde n_i}{D_i}.
}
\]

The G-free horizon representation of the **project-core coefficient** is therefore

\[
\boxed{
\mathcal M_4^{project}
=-\frac{i}{4M_HT_H}
\sum_i\frac{n_i\tilde n_i}{D_i}.
}
\]

On the local kinetic-carrier surface it is

\[
\boxed{
\mathcal M_4^{project}
=-i\frac{\Gamma_{DC}^2}{\alpha_c^2\omega_Q^2}
\sum_i\frac{n_i\tilde n_i}{D_i}.
}
\]

These factors are one quarter of the physical `kappa_E` because the project-normalized core itself is four times the conventional gravity MHV core. RFG20 verifies the compensating product explicitly:

\[
\boxed{
\mathcal C^{project}_{--++}=-4\frac{s^3}{tu}
}
\]

so that

\[
\boxed{
\mathcal M^{project}_{--++}
=i\kappa_E\frac{s^3}{tu}.
}
\]

## 3. Executable reference

The corrected reference separately verifies:

1. the physical `kappa_g -> Mbar_G -> kappa_E` triangle;
2. the horizon relation `kappa_E=1/(M_H T_H)`;
3. the local carrier relation for physical `kappa_E`;
4. the project-core coefficient `kappa_E/4` on the horizon surface;
5. the project-core coefficient on the local carrier surface;
6. absence of any numerical insertion of Newton's constant.

Corrected local result:

```text
6 passed, 0 failed
```

The result is an exact algebraic cross-route reduction on the stated admitted surfaces. Independent physical promotion of `M_star` type, horizon inputs, `Gamma_DC` and cross-system universality remains evidence-gated.
