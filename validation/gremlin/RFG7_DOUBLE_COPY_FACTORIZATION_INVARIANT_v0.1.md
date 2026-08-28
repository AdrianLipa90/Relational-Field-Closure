# RFG7 — Double-Copy Factorization Invariant

Status: `EXACT_FACTORIZATION_IDENTITY / REDUCED_GRAVITY_SCALE_INVARIANT / HORIZON_BINDING_CONDITIONAL / GAMMA_DC_PROMOTION_GATED`

RFG7 consumes RFG2, RFG4G, RF-N1C2 and RF-N1C3. Its purpose is to isolate the invariant physical content of the double-copy coupling factorization before any numerical promotion of `Gamma_DC`.

## 1. RFG2 factorization coordinate

RFG2 defines

\[
\boxed{
\Gamma_{DC}:=\frac{\kappa_g M_\star}{2g_1g_2}
}
\]

and hence

\[
\boxed{
\kappa_g=\frac{2\Gamma_{DC}g_1g_2}{M_\star}.
}
\]

For the self-copy surface `g_1=g_2=g_YM`,

\[
\boxed{
\Gamma_{DC}=\frac{\kappa_g M_\star}{2g_{YM}^2}.
}
\]

## 2. Reduced gravity-scale invariant

RF-N1C2 defines

\[
\bar M_G:=\frac{M_\star}{\Gamma_{DC}g_{YM}^2}.
\]

Substituting the RFG2 definition gives exactly

\[
\boxed{
\bar M_G=\frac{2}{\kappa_g}.
}
\]

Therefore

\[
\boxed{
G=\frac{\kappa_g^2}{32\pi}
=\frac{1}{8\pi\bar M_G^2}
}
\]

in natural units.

The reduced gravity scale is thus the invariant coordinate carried by the RFG2 factorization.

## 3. Factorization-rescaling theorem

For fixed `kappa_g` and `g_YM`, rescale the auxiliary carrier scale by any positive `lambda`:

\[
M_\star' = \lambda M_\star.
\]

The RFG2 definition then gives

\[
\Gamma_{DC}'=\lambda\Gamma_{DC}.
\]

Hence

\[
\boxed{
\frac{M_\star'}{\Gamma_{DC}'g_{YM}^2}
=
\frac{M_\star}{\Gamma_{DC}g_{YM}^2}
=
\bar M_G.
}
\]

This is the RFG7 factorization invariance theorem. Numerical promotion of `Gamma_DC` therefore requires the `M_star` normalization surface to be frozen independently.

## 4. RFG4G Yang–Mills transfer

RFG4G gives, on the admitted same-sector normalization surface,

\[
\boxed{
g_{YM}^2=\frac1{\alpha_c}.}
\]

Then

\[
\boxed{
\Gamma_{DC}=\frac{\kappa_g\alpha_c M_\star}{2}
}
\]

and

\[
\boxed{
\bar M_G=\frac{\alpha_c M_\star}{\Gamma_{DC}}
=\frac{2}{\kappa_g}.
}
\]

Thus the Wilson/Yang–Mills normalization coordinate is eliminated from the invariant gravity scale.

## 5. Horizon/thermal binding

RF-N1C3 supplies the independent reduced-scale relation

\[
\boxed{
\bar M_G^2=M_HT_H
}
\]

and equivalently

\[
\boxed{
\bar M_G=\sqrt{M_HT_H}
}
\]

on the positive branch.

Combining this with the RFG4G surface gives the G-free double-copy factorization coordinate

\[
\boxed{
\Gamma_{DC}
=
\frac{\alpha_c M_\star}{\sqrt{M_HT_H}}.
}
\]

If the RF-N1C2 carrier-scale candidate is admitted,

\[
M_\star=\epsilon_N=\frac{\omega_Q}{2},
\]

then

\[
\boxed{
\Gamma_{DC}^{local/H}
=
\frac{\alpha_c\omega_Q}
{2\sqrt{M_HT_H}}.
}
\]

This equation contains no inserted numerical value of `G`.

## 6. `Gamma_DC=1` surface

The coordinate value

\[
\Gamma_{DC}=1
\]

selects the specific carrier normalization

\[
\boxed{
M_\star=\frac{2g_{YM}^2}{\kappa_g}
}
\]

or, on RFG4G,

\[
\boxed{
M_\star=\frac{2}{\alpha_c\kappa_g}.
}
\]

It is therefore a definite normalization surface that can be tested against the independently promoted carrier scale.

## 7. Executable defects

Define

\[
\Delta_{fact}
=
\left|
\bar M_G-\frac{2}{\kappa_g}
\right|,
\]

\[
\Delta_G
=
\left|
\frac{1}{8\pi\bar M_G^2}
-
\frac{\kappa_g^2}{32\pi}
\right|,
\]

and on the horizon surface

\[
\Delta_{\Gamma H}
=
\left|
\Gamma_{DC}
-
\frac{\alpha_cM_\star}{\sqrt{M_HT_H}}
\right|.
\]

All vanish on their respective admitted factorization surfaces.

## 8. Reference validation

The executable reference test checks:

1. exact `Mbar_G=2/kappa_g` factorization;
2. exact equivalence of the two `G` expressions;
3. invariance under `M_star -> lambda M_star`, `Gamma_DC -> lambda Gamma_DC`;
4. RFG4G `alpha_c` specialization;
5. horizon determination of `Gamma_DC` once `M_star` is supplied;
6. local carrier specialization `M_star=omega_Q/2`;
7. the specific carrier normalization selected by `Gamma_DC=1`.

Local result:

```text
7 passed, 0 failed
```

## 9. Advancement

```text
RFG2 Gamma_DC factorization definition                 inherited
RF-N1C2 Mbar_G coordinate                              inherited
Mbar_G=2/kappa_g                                       PASS EXACT
G=kappa_g^2/(32 pi)=1/(8 pi Mbar_G^2)                 PASS EXACT
M_star/Gamma_DC rescaling invariance                   PASS EXACT
RFG4G g_YM^2=1/alpha_c transfer                        PASS CONDITIONAL SAME-SECTOR
Gamma_DC=alpha_c M_star/sqrt(M_H T_H)                  PASS CONDITIONAL HORIZON
Gamma_DC=alpha_c omega_Q/(2 sqrt(M_H T_H))             PASS CONDITIONAL LOCAL CARRIER
Gamma_DC numerical promotion                           OPEN M_star + horizon/source evidence
project BCJ numerator/amplitude binding                OPEN RFG6 FRONTIER
```

The author/repository/formalism/code may suggest a preferred double-copy factorization surface, yet does not state a numerical `Gamma_DC` as an established result until the carrier-scale and independent reduced-gravity-scale evidence gates are jointly admitted.
