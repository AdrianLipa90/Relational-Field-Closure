# RFG23 — Five-Point BCJ / Soft-Factorization Gate

Status: `FIVE_POINT_MHV_BCJ_REFERENCE_PASS / TWO_AMPLITUDE_BASIS_PASS / CONSERVED_SOFT_FAMILY_FACTORISATION_PASS / BG_STANDARD_COLOR_ORDER_REFERENCE / PROJECT_BASIS_MAP_RFG27_PASS`

RFG23 is the first explicit higher-point tree reference. It establishes the five-point MHV BCJ basis and a momentum-conserving positive-helicity soft family. RFG27 later identifies the exact map from this raw/standard color-ordered basis to the RFG15 project color-order basis.

For `1-,2-,3+,4+,5+`,

\[
A_5(\sigma)=\frac{\langle12\rangle^4}{\langle\sigma_1\sigma_2\rangle\langle\sigma_2\sigma_3\rangle\langle\sigma_3\sigma_4\rangle\langle\sigma_4\sigma_5\rangle\langle\sigma_5\sigma_1\rangle}.
\]

The fundamental relation

\[
\boxed{0=s_{12}A(12345)+(s_{12}+s_{23})A(13245)+(s_{12}+s_{23}+s_{24})A(13425)}
\]

reduces the basis to `(5-3)!=2` amplitudes.

For the conserved positive-helicity soft family,

\[
\boxed{A_5(1,2,3,4,5^+)=\frac{\langle41\rangle}{\langle45\rangle\langle51\rangle}A_4(1,2,3,4)},
\qquad A_5\sim\varepsilon^{-1}.
\]

RFG27 verifies that the direct RFG25 Berends–Giele amplitudes occupy this same raw color-order normalization and maps it to the RFG15 project basis by

\[
\boxed{A_n^{project}=2A_n^{BG/reference}}.
\]

Recorded reference result remains

```text
6 passed, 0 failed
```

with the project normalization handoff now pinned by RFG27.
