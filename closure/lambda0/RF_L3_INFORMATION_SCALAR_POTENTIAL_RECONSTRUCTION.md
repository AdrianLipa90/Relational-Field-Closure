# RF-L3 — Information-Scalar Potential Reconstruction Gate

Status: `FUNCTIONAL_RECONSTRUCTION_PASS_CONDITIONAL / IDT_XI_I_HOLONOMY_PRESERVED / STABILITY_PULLBACK_EXACT / ALPHA_I_CALIBRATION_OPEN`

RF-L3 consumes RF-L2 together with the IDT 01L export of the inverse-area information scalar

\[
\Xi_I=\frac{\mathcal J_\pi}{\mathcal A_{\rm rel}},
\qquad [\Xi_I]=L^{-2}.
\]

The purpose of this gate is to reconstruct the RF-L2 potential coordinate from an admitted RFC/IDT scalar binding while keeping the scalar coupling coefficient explicit.

## 1. Typed scalar binding

IDT 01L exports the information-sector family

\[
\boxed{\Lambda_I=\alpha_I\Xi_I},
\]

where `alpha_I` is dimensionless. RF-L2 supplies

\[
\boxed{\Lambda_0=\Lambda_{ref}+\kappa_E U_L}.
\]

Define the information-sector displacement

\[
\Delta\Lambda_I:=\Lambda_0-\Lambda_{ref}.
\]

The typed identification admitted by this gate is

\[
\boxed{\Delta\Lambda_I=\alpha_I\Xi_I}.
\]

Therefore the corresponding potential is reconstructed exactly as

\[
\boxed{
U_I=\frac{\alpha_I}{\kappa_E}\Xi_I.
}
\]

Substitution gives the exact roundtrip

\[
\boxed{
\Lambda_{ref}+\kappa_EU_I
=\Lambda_{ref}+\alpha_I\Xi_I
=\Lambda_0.
}
\]

No value of `alpha_I` is selected at RF-L3. Its physical calibration remains a separate promotion coordinate.

## 2. Dimensional closure

Because

\[
[\Xi_I]=L^{-2},\qquad [\alpha_I]=1,
\]

one has

\[
[\alpha_I\Xi_I]=L^{-2}=[\Lambda_0].
\]

Since RF-L2 requires

\[
[\kappa_EU_L]=L^{-2},
\]

the reconstructed `U_I` has exactly the RF-L2 potential dimension.

## 3. Scalar-coordinate pullback

Let the RF-L2 closure coordinate parameterize the admitted information scalar,

\[
\Xi_I=\Xi_I(\phi_L).
\]

Then

\[
\boxed{
U_I(\phi_L)=\frac{\alpha_I}{\kappa_E}\Xi_I(\phi_L).
}
\]

For constant `alpha_I` and `kappa_E`,

\[
\boxed{
U_I'(\phi_L)=\frac{\alpha_I}{\kappa_E}\Xi_I'(\phi_L)
}
\]

and

\[
\boxed{
U_I''(\phi_L)=\frac{\alpha_I}{\kappa_E}\Xi_I''(\phi_L).
}
\]

Thus the RF-L2 stationary condition pulls back to

\[
\boxed{
U_I'(\phi_{L0})=0
\Longleftrightarrow
\alpha_I\Xi_I'(\phi_{L0})=0.
}
\]

For a nonzero admitted coupling `alpha_I`, this becomes

\[
\boxed{
\Xi_I'(\phi_{L0})=0.
}
\]

## 4. Stability pullback

RF-L2 defines

\[
m_L^2:=U_L''(\phi_{L0}).
\]

For the information-sector reconstruction,

\[
\boxed{
m_{L,I}^2=\frac{\alpha_I}{\kappa_E}\Xi_I''(\phi_{L0}).}
\]

Therefore the local RF-L2 stability gate is transferred exactly to

\[
\boxed{
\frac{\alpha_I}{\kappa_E}\Xi_I''(\phi_{L0})\ge0.
}
\]

This keeps the sign of the information-sector coupling visible in the stability ledger.

## 5. Bianchi transfer compatibility

RF-L2 gives

\[
\kappa_E\nabla^\mu T^{\rm displayed}_{\mu\nu}
=\nabla_\nu\Lambda_0.
\]

For constant `Lambda_ref` and constant `alpha_I`, the RF-L3 reconstruction gives

\[
\boxed{
\nabla_\nu\Lambda_0
=\alpha_I\nabla_\nu\Xi_I.
}
\]

Hence

\[
\boxed{
\kappa_E\nabla^\mu T^{\rm displayed}_{\mu\nu}
=\alpha_I\nabla_\nu\Xi_I.
}
\]

The IDT information scalar therefore enters the already-admitted Einstein-Bianchi transfer through the same scalar lineage rather than through an additional source type.

## 6. Holonomy preservation

IDT 01L exports the pair

\[
(\Xi_I,\tau_R),
\qquad
\tau_R=\operatorname{wrap}_\pi\Phi_T(C),
\]

and uses the scalar magnitude channel together with the oriented phase carrier `exp(i tau_R)`.

RF-L3 acts only on the scalar-magnitude coordinate:

\[
\Xi_I\mapsto\Delta\Lambda_I\mapsto U_I.
\]

The phase coordinate `tau_R` is transported unchanged. The cross-repository state therefore remains typed as

\[
\boxed{
(\Xi_I,\tau_R)
\longmapsto
(\Lambda_{ref}+\alpha_I\Xi_I,\tau_R)
\longmapsto
(U_I,\tau_R).
}
\]

This is the RF-L3 information-holonomy preservation contract.

## 7. Identifiability firewall

The functional form is fixed once the admitted field `Xi_I(phi_L)` and the coefficient `alpha_I` are fixed:

\[
U_I(\phi_L)=\frac{\alpha_I}{\kappa_E}\Xi_I(\phi_L).
\]

The remaining physical normalization problem is isolated to `alpha_I`. RF-L3 therefore separates two questions:

```text
functional reconstruction from admitted Xi_I          PASS EXACT CONDITIONAL
cross-repository scalar type preservation              PASS EXACT
Bianchi derivative transfer                            PASS EXACT GIVEN RF-L2
stationary/stability pullback                          PASS EXACT
orientation coordinate tau_R preservation              PASS EXACT
alpha_I physical calibration                           OPEN
parameter-free alpha_I derivation                      OPEN
nonlinear/global stability                              OPEN
```

## 8. Executable reference gates

RF-L3 tests verify:

1. exact `Xi_I -> U_I -> Lambda0` roundtrip;
2. invariance under a constant reference shift `Lambda_ref`;
3. first-derivative pullback;
4. second-derivative/stability pullback;
5. zero-coupling degeneracy remains explicitly classified;
6. sign of `alpha_I` remains visible in `m_L^2`;
7. the oriented holonomy coordinate is unchanged by scalar reconstruction;
8. nonfinite scalar/coupling inputs fail closed.

## 9. Advancement

```text
RF-L2 action realization                              ADMITTED
IDT Xi_I inverse-area scalar lineage                  ADMITTED INPUT
DeltaLambda_I = alpha_I Xi_I                          PASS TYPED BINDING
U_I = alpha_I Xi_I / kappa_E                          PASS EXACT RECONSTRUCTION
Lambda0 roundtrip                                     PASS EXACT
Bianchi transfer pullback                             PASS EXACT GIVEN RF-L2
stationary/stability pullback                         PASS EXACT
IDT tau_R orientation preservation                    PASS EXACT
alpha_I calibration                                   OPEN
parameter-free physical calibration                   OPEN
```
