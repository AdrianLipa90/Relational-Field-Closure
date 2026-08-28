# RFG22 — Einstein MHV / Double-Copy Normalization Firewall

Status: `PROJECT_NUMERATOR_NORMALIZATION_IDENTIFIED / KAPPA_OVER_4_TRANSFER_PASS / OLD_KAPPA_OVER_2_TRANSFER_FAIL_FACTOR_MINUS4 / EINSTEIN_MHV_CLOSED_FORM_PASS`

RFG22 consumes RFG9, RFG15, RFG16, RFG19, RFG20 and RFG21. It audits the overall normalization of the project four-point double copy against an independent Einstein four-graviton tree amplitude. No numerator is changed or fitted to the gravity result.

## 1. Independent Einstein benchmark

The helicity-conserving four-graviton Born amplitude has the kinematic form

\[
\boxed{\mathcal M^{Ein}_{4,\mathrm{MHV}}=i\kappa_E\frac{s^3}{tu}}
\]

up to the convention of stripping the overall `i`, with

\[
\boxed{\kappa_E=8\pi G=\frac{\kappa_g^2}{4}},
\qquad \kappa_g^2=32\pi G.
\]

## 2. Project Yang–Mills numerator normalization

Using independent complex on-shell spinors and normalized helicity vectors, the RFG15 project partial amplitude obeys

\[
\boxed{
A^{project}_{1234}
=\frac{n_s}{s}-\frac{n_u}{u}
=-2i A^{PT}_{1234}.
}
\]

The constant magnitude factor `2` is the four-point result of one absorbed `sqrt(2)` normalization per cubic vertex/numerator.

## 3. Compatible double-copy transfer

For this numerator normalization the compatible gauge-to-gravity replacement is

\[
\boxed{g\longrightarrow\frac{\kappa_g}{4}}
\]

rather than `kappa_g/2`. Thus

\[
\boxed{
\mathcal M_4^{project}
=-i\left(\frac{\kappa_g}{4}\right)^2
\sum_i\frac{n_i\tilde n_i}{D_i}
=-\frac{i\kappa_E}{4}\mathcal C_{DC}^{project}.
}
\]

The physical Einstein coupling remains

\[
\boxed{\kappa_E=\kappa_g^2/4=8\pi G.}
\]

## 4. Closed-form MHV check

On the RFG19 MHV witness,

\[
\boxed{
\mathcal C_{--++}^{project}=-4\frac{s^3}{tu}.
}
\]

Therefore

\[
\boxed{
\mathcal M_{--++}^{project}
=-\frac{i\kappa_E}{4}\left(-4\frac{s^3}{tu}\right)
=i\kappa_E\frac{s^3}{tu}
=\mathcal M_{4,\mathrm{MHV}}^{Ein}.
}
\]

## 5. Old-prefactor firewall

The former project transfer

\[
+i(\kappa_g/2)^2\mathcal C_{DC}^{project}
\]

gives the exact normalized defect

\[
\boxed{
\mathcal M^{old}/\mathcal M^{Ein}=-4.
}
\]

The defect is explained entirely by project numerator normalization and tree-level phase convention. RFG15 numerators, their Jacobi identity, Ward identities, `G`, and the RF-E3 physical `kappa_E` are unchanged.

## 6. KLT and pole downstreams

RFG20 gives the core identity

\[
\mathcal C_{DC}^{project}=-uA_{1234}\widetilde A_{1324}.
\]

Hence its correctly normalized amplitude form is

\[
\boxed{
\mathcal M_4^{project}
=+\frac{i\kappa_E}{4}
 uA_{1234}\widetilde A_{1324}.
}
\]

RFG21 gives

\[
\lim_{t\to0}t\mathcal C_{DC}=X_t\widetilde X_t,
\]

so its project-amplitude residue is

\[
\boxed{
\operatorname*{Res}_{t=0}\mathcal M_4^{project}
=-\frac{i\kappa_E}{4}X_t\widetilde X_t.
}
\]

The core factorization results of RFG20/RFG21 are preserved; only the external coupling coefficient is corrected.

## 7. Executable validation

The reference test verifies:

1. `A_project(1234)=-2 i A_PT(1234)` on 100 random complex on-shell points;
2. `C_project_MHV=-4 s^3/(tu)` over 31 real angles;
3. `-i(kappa_g/4)^2 C_project=i kappa_E s^3/(tu)`;
4. the old `+i(kappa_g/2)^2` transfer has exact ratio `-4`;
5. `(kappa_g/4)^2=kappa_E/4`;
6. `kappa_E=kappa_g^2/4=8 pi G` is unchanged.

Local result:

```text
6 passed, 0 failed
```

## 8. Advancement

```text
RFG15 project BCJ numerators                    PASS UNCHANGED
RFG20 project KLT core                          PASS UNCHANGED
RFG21 project pole core factorization           PASS UNCHANGED
project numerator normalization                 -2 i vs PT IDENTIFIED
project coupling transfer                       kappa_g/4 PASS
Einstein MHV closed-form normalization          PASS
old kappa_g/2 project transfer                  FAIL EXACT FACTOR -4
physical kappa_E                                UNCHANGED
higher-point per-vertex normalization           NEXT NORMALIZATION FRONTIER
```
