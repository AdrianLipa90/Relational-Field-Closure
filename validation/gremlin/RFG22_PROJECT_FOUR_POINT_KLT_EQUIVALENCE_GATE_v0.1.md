# RFG22 — Project Four-Point KLT Equivalence Gate

Status: `PROJECT_PARTIAL_AMPLITUDE_BCJ_PASS / KLT_BILINEAR_EQUIVALENCE_PASS / RFG20_NORMALIZATION_APPLIED / NO_GRAVITY_FIT / FOUR_POINT_SCOPE`

RFG22 consumes the project BCJ numerators of RFG15, the corrected project double-copy convention of RFG16/RFG20, and provides an independent four-point representation of the same project gravity core using project color-ordered partial amplitudes.

## 1. Channel orientation

RFG15 fixes

\[
\boxed{n_s-n_t+n_u=0}
\]

with massless Mandelstam closure

\[
\boxed{s+t+u=0.}
\]

Define the project partial amplitudes

\[
\boxed{A_{1234}=\frac{n_s}{s}-\frac{n_u}{u}}
\]

and

\[
\boxed{A_{1324}=\frac{n_t}{t}+\frac{n_u}{u}.}
\]

The matched Jacobi identity gives

\[
\boxed{sA_{1234}=tA_{1324}.}
\]

## 2. KLT representation of the project core

For two independently admitted RFG15 project copies, define

\[
\mathcal C_{project}
=\frac{n_s\widetilde n_s}{s}
+\frac{n_t\widetilde n_t}{t}
+\frac{n_u\widetilde n_u}{u}.
\]

Using only the two matched Jacobi identities and `s+t+u=0`,

\[
\boxed{
\mathcal C_{project}
=-u\,A_{1234}\,\widetilde A_{1324}.
}
\]

This identity concerns the project-normalized numerator core and is independent of any gravity coupling convention.

## 3. Correct full-amplitude normalization

RFG20 independently establishes that the RFG15 project partial amplitude obeys

\[
A^{project}_{1234}=-2iA^{PT}_{1234},
\]

so the compatible project double-copy transfer is

\[
g\rightarrow\kappa_g/4.
\]

RFG16 therefore gives

\[
\boxed{
\mathcal M_4^{project}
=-i\left(\frac{\kappa_g}{4}\right)^2\mathcal C_{project}
=-\frac{i\kappa_E}{4}\mathcal C_{project},
}
\]

where the physical Einstein coupling remains

\[
\boxed{\kappa_E=\frac{\kappa_g^2}{4}=8\pi G.}
\]

Combining this corrected prefactor with the project KLT identity gives

\[
\boxed{
\mathcal M_4^{project}
=+\frac{i\kappa_E}{4}\,u\,A_{1234}\widetilde A_{1324}.
}
\]

The factor `1/4` belongs to the project-normalized numerator/partial-amplitude convention; it does not modify the physical Einstein coupling.

## 4. Copy-exchange consistency

The executable gate verifies

\[
-uA_{1234}\widetilde A_{1324}
=
-u\widetilde A_{1234}A_{1324},
\]

which follows from the independent four-point BCJ relations in both copies.

## 5. Gauge-invariance gate

Replacing any one external polarization by the corresponding momentum annihilates the project partial amplitude within deterministic numerical tolerance. The KLT representation therefore inherits the independent Ward gates of both project factors.

## 6. Executable validation

The reference test checks:

1. massless Mandelstam closure `s+t+u=0`;
2. project four-point BCJ relation `s A_1234 = t A_1324` over 500 random states;
3. direct project core equals `-u A_1234 Atilde_1324` over 500 independent-copy pairs;
4. copy-exchange equality of the KLT bilinear;
5. single-leg gauge invariance of the project color-ordered partial amplitude;
6. the KLT kernel uses only project Mandelstam data and no gravity-fit coordinate.

Local result:

```text
6 passed, 0 failed
```

## 7. Advancement

```text
RFG15 project BCJ numerators                    PASS
RFG16 corrected project double copy             PASS
RFG20 Einstein MHV normalization firewall       PASS
project partial amplitudes                      PASS
s A_1234 = t A_1324                            PASS
project KLT core = direct project core          PASS
full KLT prefactor +i kappa_E u / 4             PASS NORMALIZATION TRANSFER
RFG18/RFG19 pure spin-2 branch                  PASS
higher-point KLT/BCJ normalization              OPEN
```

RFG22 provides a representation-level cross-check of the corrected four-point gauge-to-gravity bridge without altering the RFG15 project numerators.