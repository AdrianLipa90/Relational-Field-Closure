# RFG20 — Project Four-Point KLT Equivalence Gate

Status: `PROJECT_PARTIAL_AMPLITUDE_BCJ_PASS / KLT_BILINEAR_EQUIVALENCE_PASS / NO_GRAVITY_FIT / FOUR_POINT_SCOPE`

RFG20 consumes the project BCJ numerators of RFG15 and the project double-copy amplitude of RFG16. It provides an independent four-point representation of the same gravity core using project color-ordered partial amplitudes.

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

The matched Jacobi identity immediately gives the four-point BCJ relation

\[
\boxed{sA_{1234}=tA_{1324}.}
\]

The executable reference verifies this relation on 500 deterministic random project kinematic states.

## 2. KLT representation

Let `(n_s,n_t,n_u)` and `(nt_s,nt_t,nt_u)` be two independently admitted RFG15 project copies. RFG16 uses the direct double-copy core

\[
\mathcal C_{DC}
=\frac{n_s\widetilde n_s}{s}
+\frac{n_t\widetilde n_t}{t}
+\frac{n_u\widetilde n_u}{u}.
\]

Using only the two matched Jacobi identities and `s+t+u=0`, the same core can be written

\[
\boxed{
\mathcal C_{DC}
=-u\,A_{1234}\,\widetilde A_{1324}.
}
\]

Thus the project gravity amplitude has the equivalent form

\[
\boxed{
\mathcal M_4^{project}
=-i\kappa_E\,u\,A_{1234}\widetilde A_{1324}
}
\]

with the same `kappa_E` fixed by RFG16/RFG17.

No gravity amplitude is used to choose the project numerators or the partial-amplitude definitions.

## 3. Copy-exchange consistency

The executable gate also verifies

\[
-uA_{1234}\widetilde A_{1324}
=
-u\widetilde A_{1234}A_{1324},
\]

which follows from the independent four-point BCJ relations in the two copies.

## 4. Gauge-invariance gate

The project partial amplitude `A_1234` is evaluated directly from the RFG15 numerators. Replacing any one external polarization by the corresponding momentum gives zero within deterministic numerical tolerance. The KLT representation therefore inherits the independent gauge Ward gates of its two project factors.

## 5. Executable validation

The reference test checks:

1. massless Mandelstam closure `s+t+u=0`;
2. project four-point BCJ relation `s A_1234 = t A_1324` over 500 random states;
3. direct BCJ double-copy core equals `-u A_1234 Atilde_1324` over 500 independent-copy pairs;
4. copy-exchange equality of the KLT bilinear;
5. single-leg gauge invariance of the project color-ordered partial amplitude;
6. KLT kernel uses only the project Mandelstam coordinate `u`, with no gravity-fit coordinate.

Local result:

```text
6 passed, 0 failed
```

## 6. Advancement

```text
RFG15 project BCJ numerators                    PASS
RFG16 direct project double copy                PASS
project color-ordered partial amplitudes        PASS
s A_1234 = t A_1324                            PASS
project KLT bilinear = direct double copy       PASS
copy-exchange consistency                       PASS
RFG18/RFG19 spin-2 external-state branch        PASS
higher-point KLT/BCJ project construction       OPEN
```

RFG20 provides a representation-level cross-check of the four-point gauge-to-gravity bridge independently of the direct channel sum used in RFG16.