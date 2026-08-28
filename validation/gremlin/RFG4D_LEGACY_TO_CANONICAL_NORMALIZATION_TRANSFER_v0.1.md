# RFG4D — Legacy-to-Canonical Information Normalization Transfer

Status: `EXACT_ALGEBRAIC_TRANSFER / INPUT_BINDINGS_INHERITED / PHYSICAL_YM_G_PROMOTION_GATED`

## 1. Purpose

RFG4D propagates only the normalization replacement

\[
I_0^{legacy}=0.009
\quad\longrightarrow\quad
\kappa=\frac{\ln2}{24\pi}
\]

through the RFG4 analytic `alpha_c` reconstruction and the downstream RFG3/RFG2 candidate coordinates.

All other coordinates are held fixed during this sensitivity transfer.

## 2. Legacy and canonical alpha coordinates

Define

\[
\alpha_L
:=
\ln\varphi-\kappa\ln2-\frac{\kappa-I_0^{legacy}}{L_3},
\]

and

\[
\alpha_C
:=
\ln\varphi-\kappa\ln2.
\]

Then exactly

\[
\boxed{
\alpha_C-\alpha_L
=
\frac{\kappa-I_0^{legacy}}{L_3}
}
\]

and for `I0_legacy=0.009`, `L3=7`,

\[
\boxed{
\alpha_L
=0.47481202619417856\ldots
}
\]

\[
\boxed{
\alpha_C
=0.47483961905223004\ldots
}
\]

with

\[
\boxed{
\delta_\alpha
=2.75928580515\times10^{-5}.
}
\]

The relative canonical shift is

\[
\boxed{
\frac{\alpha_C}{\alpha_L}-1
=5.81132249\times10^{-5}
}
\]

or approximately `58.113 ppm`.

## 3. Yang–Mills coupling transfer

Under the independently gated candidate binding

\[
\alpha_c\stackrel{?}{=}\frac1{g_0^2},
\]

the two coupling coordinates are

\[
\boxed{
g_L=\alpha_L^{-1/2}}
\]

and

\[
\boxed{
g_C=\alpha_C^{-1/2}}.
\]

Hence

\[
\boxed{
\frac{g_C}{g_L}
=
\sqrt{\frac{\alpha_L}{\alpha_C}}
}
\]

with

\[
g_L=1.451239681314748\ldots,
\]

\[
g_C=1.451197515043579\ldots,
\]

and

\[
\boxed{
\frac{g_C}{g_L}-1
=-2.90553461\times10^{-5}
}
\]

or approximately `-29.055 ppm`.

## 4. Wilson coordinate transfer

For SU(3),

\[
\beta_W=\frac6{g_0^2}=6\alpha_c.
\]

Therefore

\[
\boxed{
\beta_L=6\alpha_L
=2.848872157165071\ldots
}
\]

and

\[
\boxed{
\beta_C=6\alpha_C
=2.849037714313380\ldots
}.
\]

The relative shift is exactly the alpha shift:

\[
\boxed{
\frac{\beta_C}{\beta_L}-1
=
\frac{\alpha_C}{\alpha_L}-1.
}
\]

## 5. Double-copy G-candidate transfer

RFG3 uses

\[
G_{cand}
=
\frac{18\Gamma_{DC}^2}
{\pi\beta_W^2(D_\tau\chi)^2}.
\]

Holding `Gamma_DC` and `D_tau chi` fixed gives the exact ratio

\[
\boxed{
\frac{G_C}{G_L}
=
\left(\frac{\beta_L}{\beta_C}\right)^2
=
\left(\frac{\alpha_L}{\alpha_C}\right)^2.
}
\]

Numerically,

\[
\boxed{
\frac{G_C}{G_L}
=0.999883783680906\ldots
}
\]

so

\[
\boxed{
\frac{G_C}{G_L}-1
=-1.16216319\times10^{-4}
}
\]

or approximately `-116.216 ppm`.

This is the normalization-only transfer. It carries no fitted Newton target.

## 6. First-order relation

For a small positive fractional alpha shift `epsilon`,

\[
\alpha_C=\alpha_L(1+\epsilon),
\]

one has

\[
\frac{\delta g}{g}
=-\frac12\epsilon+O(\epsilon^2),
\]

and

\[
\boxed{
\frac{\delta G_{cand}}{G_{cand}}
=-2\epsilon+O(\epsilon^2).
}
\]

The exact ratio in Section 5 is used for executable validation.

## 7. Promotion typing

The transfer identities in this document are exact algebra once the input coordinates are supplied.

The physical chain

```text
alpha_c
 -> 1/g_0^2
 -> beta_W
 -> double-copy G
```

inherits the independent promotion gates already defined in RFG3/RFG2. The normalization transfer itself introduces no new fitted parameter.