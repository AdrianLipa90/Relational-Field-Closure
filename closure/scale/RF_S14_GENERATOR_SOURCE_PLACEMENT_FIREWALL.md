# RF-S14 — Relational Generator Matter/Vacuum Source-Placement Firewall

Status: `EXACT_EOS_SOURCE_TYPING / EXACT_LAMBDA_MOVE_CRITERION / GENERATOR_PLACEMENT_AUDIT`

RF-S14 is stacked on RF-S13. RF-S13 establishes the typed source-density realization

\[
\rho_G
=
\frac{B\omega\mathcal N}{AR}(\phi+\kappa),
\qquad
\kappa=\frac{\ln2}{24\pi},
\]

with energy-density units on the admitted action/occupation/volume branch.

RF-S14 determines when this scalar energy density belongs to the displayed matter tensor and when it is algebraically equivalent to a dynamic cosmological-potential contribution.

## 1. Perfect-fluid source typing

In a local orthonormal rest frame with signature `(-,+,+,+)`, an isotropic source has

\[
\boxed{
T_{\mu\nu}
=\operatorname{diag}(\rho_G,p_G,p_G,p_G).
}
\]

A pure vacuum-like scalar source has

\[
\boxed{
T^{vac}_{\mu\nu}=-\rho_G g_{\mu\nu}
=\operatorname{diag}(\rho_G,-\rho_G,-\rho_G,-\rho_G).
}
\]

Therefore the exact source-placement criterion is

\[
\boxed{p_G=-\rho_G.}
\]

Equivalently, for nonzero density,

\[
\boxed{w_G:=p_G/\rho_G=-1.}
\]

## 2. Lambda-side equivalence

Start from the RFC Einstein equation

\[
G_{\mu\nu}+\Lambda_{ref}g_{\mu\nu}
=\kappa_E(T^{base}_{\mu\nu}+T^G_{\mu\nu}).
\]

If

\[
T^G_{\mu\nu}=-\rho_Gg_{\mu\nu},
\]

then moving that contribution to the geometric side gives

\[
\boxed{
G_{\mu\nu}
+(\Lambda_{ref}+\kappa_E\rho_G)g_{\mu\nu}
=\kappa_ET^{base}_{\mu\nu}.
}
\]

Hence

\[
\boxed{
\Delta\Lambda_G=\kappa_E\rho_G.
}
\]

With the RF-S13 generator,

\[
\boxed{
\Delta\Lambda_G
=\kappa_E
\frac{B\omega\mathcal N}{AR}(\phi+\kappa).
}
\]

This is exactly the RF-L1 dimensional form

\[
\Lambda_0=\Lambda_{ref}+\kappa_EU_L,
\]

on the branch where

\[
\boxed{U_L=\rho_G.}
\]

## 3. Matter-side branch

If the source has an independently measured stress state with

\[
p_G\ne-\rho_G,
\]

then its stress tensor contains a component that cannot be represented by a scalar multiple of the metric.

The source remains on the displayed matter side and RF-S13 supplies its normal-frame energy-density entry

\[
\boxed{\rho_n=\rho_G.}
\]

For the homogeneous dust surface of RF-E5,

\[
\boxed{p_G=0,}
\]

so the source is matter-typed rather than vacuum-typed.

## 4. Exact algebraic residual

Define

\[
\mathcal R_{\mu\nu}
:=
\kappa_ET^G_{\mu\nu}
+\Delta\Lambda_G g_{\mu\nu},
\qquad
\Delta\Lambda_G=\kappa_E\rho_G.
\]

For the isotropic rest tensor,

\[
\boxed{
\mathcal R_{\mu\nu}
=\operatorname{diag}
(0,\kappa_E(\rho_G+p_G),\kappa_E(\rho_G+p_G),\kappa_E(\rho_G+p_G)).
}
\]

Thus

\[
\boxed{
\mathcal R_{\mu\nu}=0
\iff
p_G=-\rho_G.
}
\]

This criterion is independent of the numerical magnitude of \(\kappa_E\).

## 5. Executable defect

RF-S14 records

\[
\boxed{
D_{vac}
=\rho_G+p_G
}
\]

and the symmetric normalized defect

\[
\boxed{
\delta_{vac}
=
\frac{2|\rho_G+p_G|}{|\rho_G|+|p_G|}
}
\]

for nonzero denominator, with the zero-source point assigned zero defect.

The source is vacuum-absorbable only when the residual lies inside the explicitly supplied numerical tolerance.

## 6. Dynamic Lambda/Bianchi consequence

On the vacuum-typed branch,

\[
\Lambda_0(x)=\Lambda_{ref}+\kappa_E\rho_G(x).
\]

Therefore

\[
\boxed{
\nabla_\nu\Lambda_0
=\kappa_E\nabla_\nu\rho_G.
}
\]

The already-derived RFC exchange law

\[
\kappa_E\nabla^\mu T^{displayed}_{\mu\nu}
=\nabla_\nu\Lambda_0
\]

then becomes

\[
\boxed{
\nabla^\mu T^{displayed}_{\mu\nu}
=\nabla_\nu\rho_G.
}
\]

for this source placement.

## 7. Advancement

```text
RF-S13 generator -> energy density                         PASS EXACT PARENT
perfect-fluid rest typing                                 PASS EXACT
vacuum source iff p=-rho                                  PASS EXACT
Lambda move DeltaLambda=kappa_E rho                       PASS EXACT
Einstein tensor residual criterion                        PASS EXACT
RF-E5 dust branch remains matter-side                     PASS EXACT CROSSLINK
RF-L1 U_L=rho_G branch                                    ADMITTED CONDITIONAL
physical pressure/equation-of-state receipt               OPEN INPUT
physical matter-vs-vacuum placement                       OPEN UNTIL RECEIPT
parameter-free kappa_E/G promotion                        OPEN INPUT
```

## 8. Validation authority

Reference implementation: `src/rfc/generator_source_placement.py`.
Reference tests: `tests/reference/test_rfs14_generator_source_placement_firewall.py`.
Validation receipt: `validation/RF_S14_GENERATOR_SOURCE_PLACEMENT_FIREWALL_V0_1.json`.

Stack parent: RF-S13 exact-green head `9e91a507a9cb55223d1dd5a3700e67939505ac19`, RFC reference suite #279 SUCCESS.
