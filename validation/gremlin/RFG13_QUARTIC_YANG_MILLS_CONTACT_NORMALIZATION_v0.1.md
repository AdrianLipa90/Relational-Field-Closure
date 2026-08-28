# RFG13 — Quartic Yang–Mills Contact Normalization

Status: `QUARTIC_ACTION_IDENTITY_PASS / ORIENTATION_INDEPENDENCE_PASS / WILSON_RECONSTRUCTION_PASS / NO_EXTRA_QUARTIC_COUPLING / FOUR_POINT_ASSEMBLY_NEXT`

RFG13 consumes RFG4G, RFG8, RFG11 and RFG12. It fixes the quartic Yang–Mills contact normalization on the same holonomic `SU(3)` surface used by the cubic interaction.

## 1. Constant noncommuting pair

For one ordered pair of local directions and explicit link orientation `sigma_link`, RFG8/RFG11 give

\[
\boxed{
F_{\mu\nu}^{(\sigma)}
=i\sigma_{link}g[A_\mu,A_\nu]
}
\]

for the constant-field commutator sector.

Define the positive pair density

\[
\boxed{
\mathcal E_4^{\mu\nu}
:=\operatorname{Tr}\left[(F_{\mu\nu}^{(\sigma)})^2\right].
}
\]

Then

\[
\boxed{
\mathcal E_4^{\mu\nu}
=-g^2\operatorname{Tr}[A_\mu,A_\nu]^2.
}
\]

Because the commutator is anti-Hermitian, this density is nonnegative.

## 2. Component form

With

\[
[T^b,T^c]=if^{bc}{}_aT^a,
\qquad
\operatorname{Tr}(T^aT^b)=\frac12\delta^{ab},
\]

the oriented commutator field has components

\[
(F_{\mu\nu}^{(\sigma)})^a
=-\sigma_{link}g f^{abc}A_\mu^bA_\nu^c.
\]

Therefore

\[
\boxed{
\mathcal E_4^{\mu\nu}
=\frac{g^2}{2}
 f^{abc}f^{ade}
 A_\mu^bA_\nu^cA_\mu^dA_\nu^e.
}
\]

This is quartic in the local gauge field and quadratic in the Yang–Mills coupling.

## 3. Orientation independence

The explicit orientation sign enters `F` linearly but squares out of the quartic density:

\[
\boxed{
\mathcal E_4^{\mu\nu}(\sigma=+1)
=
\mathcal E_4^{\mu\nu}(\sigma=-1).
}
\]

Thus the RFG11 sign firewall changes the oriented cubic vertex sign while preserving the quartic coupling magnitude.

## 4. RFG4G coupling normalization

On RFG4G,

\[
\boxed{g^2=\frac1{\alpha_c}.}
\]

Hence

\[
\boxed{
\mathcal E_4^{\mu\nu}
=-\frac1{\alpha_c}\operatorname{Tr}[A_\mu,A_\nu]^2.
}
\]

No independent quartic coupling coordinate is introduced.

## 5. Wilson reconstruction

For the same constant noncommuting pair, define the project plaquette defect

\[
D_p=3-\operatorname{ReTr}U_p.
\]

RFG4G fixes

\[
\boxed{C_p=2\alpha_c=\frac2{g^2}.}
\]

The small-loop expansion then gives

\[
\boxed{
\frac{C_pD_p}{a^4}
\longrightarrow
\operatorname{Tr}(F_{\mu\nu}^2)
=
\mathcal E_4^{\mu\nu}.
}
\]

Thus the same coefficient that normalized the Wilson continuum action reconstructs the quartic contact density from project holonomy bytes.

## 6. Scaling laws

For a common field rescaling

\[
A_\mu,A_\nu\mapsto\lambda A_\mu,\lambda A_\nu,
\]

one has

\[
\boxed{
\mathcal E_4\mapsto\lambda^4\mathcal E_4.
}
\]

For coupling rescaling at fixed fields,

\[
\boxed{
\mathcal E_4\propto g^2.
}
\]

These provide direct executable diagnostics of quartic order and coupling order.

## 7. Reference validation

The NumPy-only gate checks:

1. matrix and `f^{abc}` component expressions for the quartic density agree on 200 deterministic random field pairs;
2. the density is independent of `sigma_link`;
3. common field rescaling is exactly quartic;
4. the interaction density is proportional to `g^2`;
5. `C_p=2 alpha_c` reconstructs the quartic density from the Wilson plaquette as `a` decreases;
6. the adversarial coefficient `C_p=alpha_c` fails by the expected factor-of-two normalization.

Local result:

```text
6 passed, 0 failed
```

## 8. Advancement

```text
RFG12 project cubic color/momentum mixing             inherited PASS
quartic matrix/component action identity              PASS EXACT
quartic orientation independence                      PASS EXACT
quartic g^2 normalization                             PASS EXACT
RFG4G Wilson reconstruction                            PASS SMALL-LOOP
additional quartic coupling coordinate                 ZERO
exchange + contact four-point assembly                NEXT FRONTIER
RFG9 BCJ amplitude comparison                          OPEN DIRECT PROJECT BINDING
```

The author/repository/formalism/code may suggest that the holonomic Yang–Mills action now carries both cubic and quartic interaction normalizations required for a tree-level four-gluon assembly, yet does not state the direct project four-point amplitude as established until the exchange and contact terms are evaluated together on frozen external states.
