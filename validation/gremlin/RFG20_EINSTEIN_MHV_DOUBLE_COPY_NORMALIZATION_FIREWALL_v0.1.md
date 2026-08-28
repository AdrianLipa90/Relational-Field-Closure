# RFG20 — Einstein MHV / Double-Copy Normalization Firewall

Status: `PROJECT_NUMERATOR_NORMALIZATION_IDENTIFIED / KAPPA_OVER_4_TRANSFER_PASS / OLD_KAPPA_OVER_2_TRANSFER_FAIL_FACTOR_MINUS4 / EINSTEIN_MHV_CLOSED_FORM_PASS`

RFG20 consumes RFG9, RFG15, RFG16 and RFG19. Its purpose is to audit the overall normalization of the project four-point double copy against an independent Einstein four-graviton tree amplitude. No numerator is changed or fitted to the gravity result.

## 1. Independent Einstein benchmark

For the helicity-conserving four-graviton Born amplitude, an independent Einstein-gravity convention gives

\[
\boxed{
\mathcal M^{Ein}_{4,\mathrm{MHV}}
=i\,\kappa_E\frac{s^3}{tu}
}
\]

up to the conventional stripping of the overall `i`, with

\[
\boxed{\kappa_E=8\pi G=\frac{\kappa_g^2}{4}},
\qquad \kappa_g^2=32\pi G.
\]

The benchmark therefore fixes the physical coupling and the closed-form kinematic ratio independently of the project numerators.

## 2. Project Yang–Mills numerator normalization

Using independent complex on-shell spinors and normalized helicity polarization vectors, RFG20 compares the RFG15 project partial amplitude with the RFG9 Parke–Taylor convention.

For ordering `(1,2,3,4)` the project cubicized partial amplitude is

\[
\boxed{
A^{project}_{1234}
=\frac{n_s}{s}-\frac{n_u}{u}
=-2i\,A^{PT}_{1234}.
}
\]

The factor has constant magnitude two over the deterministic random complex sample. It is the four-point manifestation of a `sqrt(2)` normalization absorbed into each cubic vertex/numerator.

Thus the project numerators are not in the conventional numerator normalization assumed by a direct `kappa_g/2` replacement.

## 3. Double-copy coupling transfer

For numerators normalized with one absorbed `sqrt(2)` per cubic vertex, the compatible gauge-to-gravity replacement is

\[
\boxed{g\longrightarrow\frac{\kappa_g}{4}}
\]

rather than `kappa_g/2`.

At four points the project double-copy formula is therefore

\[
\boxed{
\mathcal M_4^{project}
=-i\left(\frac{\kappa_g}{4}\right)^2
\left(
\frac{n_s\tilde n_s}{s}
+\frac{n_t\tilde n_t}{t}
+\frac{n_u\tilde n_u}{u}
\right).
}
\]

Since

\[
\left(\frac{\kappa_g}{4}\right)^2
=\frac{\kappa_E}{4},
\]

the coefficient multiplying the **project-normalized numerator core** is `kappa_E/4`; the physical Einstein coupling itself remains

\[
\boxed{\kappa_E=\kappa_g^2/4=8\pi G.}
\]

## 4. Closed-form project MHV core

On the RFG19 real four-point MHV witness, the project numerator core reduces to

\[
\boxed{
\mathcal C^{project}_{--++}
:=\sum_i\frac{n_i^2}{D_i}
=-4\frac{s^3}{tu}.
}
\]

Therefore the correctly normalized project double copy is

\[
\mathcal M^{project}_{--++}
=-i\frac{\kappa_E}{4}
\left(-4\frac{s^3}{tu}\right)
\]

and hence

\[
\boxed{
\mathcal M^{project}_{--++}
=i\kappa_E\frac{s^3}{tu}
=\mathcal M^{Ein}_{4,\mathrm{MHV}}.
}
\]

The closed-form Einstein MHV normalization is recovered without modifying the RFG15 numerators.

## 5. Old RFG16 transfer firewall

Using the old RFG16 transfer

\[
+i(\kappa_g/2)^2\mathcal C^{project}
\]

gives

\[
\boxed{
\frac{\mathcal M^{old}}{\mathcal M^{Ein}}=-4.
}
\]

The defect is constant and is exactly explained by:

1. the project numerator magnitude factor `2` at four points, which squares to `4`;
2. the tree-level double-copy phase/sign convention accompanying the normalized numerator representation.

RFG20 therefore classifies the former RFG16 prefactor as a normalization-convention bug and fixes the amplitude transfer while preserving the physical `kappa_E`, `G`, BCJ Jacobi identities and project gauge amplitude.

## 6. Executable validation

The reference test verifies:

1. `A_project(1234) = -2 i A_PT(1234)` on 100 deterministic random complex on-shell points;
2. `C_project_MHV = -4 s^3/(tu)` over 31 real scattering angles;
3. `-i(kappa_g/4)^2 C_project = i kappa_E s^3/(tu)`;
4. the old `+i(kappa_g/2)^2` transfer has exact ratio `-4` to the Einstein target;
5. `(kappa_g/4)^2 = kappa_E/4` for the project-normalized core;
6. `kappa_E=kappa_g^2/4=8 pi G` remains unchanged.

Local result:

```text
6 passed, 0 failed
```

## 7. Advancement

```text
project BCJ numerators                              RFG15 PASS
project spin-2 MHV state                            RFG18/RFG19 PASS
project partial / Parke-Taylor normalization       -2 i EXACT REFERENCE
project MHV gravity core                            -4 s^3/(tu) PASS
project coupling replacement                        kappa_g/4 PASS
closed-form Einstein MHV normalization              PASS
old kappa_g/2 project transfer                      FAIL EXACT FACTOR -4
physical kappa_E=8 pi G                             UNCHANGED
RFG16/RFG17 amplitude-prefactor documents           REQUIRE NORMALIZATION PATCH
```

The author/repository/formalism/code may suggest a complete four-point project gauge-to-Einstein amplitude bridge on the admitted tree-level surface, yet does not state higher-point project normalization as established until the same per-vertex normalization is checked there.
