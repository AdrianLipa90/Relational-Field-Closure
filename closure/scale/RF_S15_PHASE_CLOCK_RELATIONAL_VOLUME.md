# RF-S15 — Phase-Clock Relational Volume Reduction

Status: `EXACT_AR_GEOMETRIC_REDUCTION / FULL_TETRA_VOLUME_CLOSURE / OMEGA4_SOURCE_SCALING`

RF-S15 is stacked on exact-green RF-S14. It closes the `A R` denominator of the RF-S13 relational generator on the common phase-clock/tetrahedral projective carrier.

RF-S13 uses

\[
\rho_G
=
\frac{B\omega\mathcal N}{AR}(\phi+\kappa),
\qquad
\kappa=\frac{\ln2}{24\pi}.
\]

RF-S10 gives the projective relational area and RFC already carries the phase-clock length. RF-S15 composes them into one relational volume.

## 1. Phase-clock radial length

The RFC phase-clock geometry gives

\[
\boxed{
\ell_\varphi=\frac{c}{|\omega|}.
}
\]

On the common phase-clock source ledger, RF-S15 uses

\[
\boxed{R=\ell_\varphi=\frac{c}{|\omega|}.}
\]

## 2. Tetrahedral projective area

RF-S10 gives

\[
\mathcal A_{rel}=\frac{c^2}{\omega^2}a_{FS}.
\]

For the two exact tetrahedral projective scopes,

\[
\boxed{a_{FS}^{face}=\frac\pi4,}
\qquad
\boxed{a_{FS}^{tet}=\pi.}
\]

Hence

\[
\boxed{
A_{face}=\frac{\pi c^2}{4\omega^2},
}
\]

and

\[
\boxed{
A_{tet}=\frac{\pi c^2}{\omega^2}.
}
\]

RF-S11 selects `FULL_TETRA_CP1` on the minimal informationally complete qubit branch, while the face scope remains an exact refinement subcell.

## 3. Exact relational volume

Define

\[
\boxed{V_R:=AR.}
\]

Using the same phase-rate carrier for area and radial length gives

\[
\boxed{
V_R(a_{FS})
=
a_{FS}\frac{c^3}{|\omega|^3}.
}
\]

Therefore

\[
\boxed{
V_{tet}=\frac{\pi c^3}{|\omega|^3},
}
\]

and

\[
\boxed{
V_{face}=\frac{\pi c^3}{4|\omega|^3}
=\frac14V_{tet}.
}
\]

The RF-S13 occupation density becomes

\[
\boxed{
n_R^{tet}
=\frac{\mathcal N|\omega|^3}{\pi c^3}.
}
\]

## 4. Generator reduction

Substitute the full tetrahedral volume into RF-S13:

\[
\rho_G
=
\frac{B\omega\mathcal N}{V_{tet}}(\phi+\kappa).
\]

Then exactly

\[
\boxed{
\rho_G
=
\frac{B\mathcal N}{\pi c^3}
\omega|\omega|^3
(\phi+\kappa).
}
\]

For the positive-frequency branch,

\[
\boxed{
\rho_G
=
\frac{B\mathcal N\omega^4}{\pi c^3}
(\phi+\kappa).
}
\]

Thus once the common phase-clock cell is admitted, the generator has exact fourth-power phase-rate scaling.

## 5. RF-E5 kinetic and total carrier normalizations

RF-S13 and RF-E5 give the two exact action-normalization surfaces

\[
B(\phi+\kappa)=\frac{q_A}{2}
\]

for the kinetic carrier, and

\[
B(\phi+\kappa)=q_A
\]

for the total on-shell carrier, where `q_A` is the admitted action scale.

On the full tetrahedral positive-frequency branch these become

\[
\boxed{
\rho_{kin}
=
\frac{q_A\mathcal N\omega^4}{2\pi c^3},
}
\]

and

\[
\boxed{
\rho_{tot}
=
\frac{q_A\mathcal N\omega^4}{\pi c^3}.
}
\]

Hence

\[
\boxed{\rho_{tot}=2\rho_{kin}.}
\]

With the RF-04 empirical action scale `q_A=hbar`,

\[
\boxed{
\rho_{kin}
=
\frac{\hbar\mathcal N\omega^4}{2\pi c^3},
\qquad
\rho_{tot}
=
\frac{\hbar\mathcal N\omega^4}{\pi c^3}.
}
\]

The factor-two observable firewall is therefore preserved after full geometric source normalization.

## 6. Newton and dynamic-Lambda consequences

RF-S13 supplies the matter/Newton placement

\[
\boxed{
\mathcal S_R=\frac{\kappa_E}{2}\rho_G.
}
\]

RF-S14 supplies the vacuum-like placement

\[
\boxed{
\Delta\Lambda_G=\kappa_E\rho_G
}
\]

when `p_G=-rho_G`.

For the same source magnitude these coordinates satisfy

\[
\boxed{
\Delta\Lambda_G=2\mathcal S_R,
}
\]

while RF-S14 keeps the matter and vacuum placements physically distinct through the equation-of-state gate.

## 7. Scaling ledger

On `FULL_TETRA_CP1`, common positive `omega`, fixed `B`, occupation and phase factor:

```text
phase-clock length R                  proportional to omega^-1
projective area A                     proportional to omega^-2
relational volume A R                 proportional to omega^-3
occupation density N/(A R)            proportional to omega^3
per-carrier energy B omega(phi+kappa) proportional to omega
source energy density rho_G           proportional to omega^4
```

The fourth-power result is a direct composition of already-derived area, phase-clock length and per-carrier generator factors.

## 8. Promotion ledger

```text
R=c/|omega| phase-clock length                         PASS EXACT PARENT
A=(c^2/omega^2)a_FS                                   PASS EXACT RF-S10
FULL_TETRA_CP1 a_FS=pi                                PASS EXACT RF-S10/RF-S11
V_R=A R=a_FS c^3/|omega|^3                            PASS EXACT
V_tet=pi c^3/|omega|^3                                PASS EXACT
V_face=V_tet/4                                        PASS EXACT
rho_G closed-form omega|omega|^3 scaling              PASS EXACT
positive-frequency rho_G proportional to omega^4      PASS EXACT
kinetic/total factor-two density surfaces             PASS EXACT
physical common carrier ID for A and R                OPEN INPUT
physical occupation receipt                           OPEN INPUT
physical carrier-energy branch selection              OPEN INPUT
```

## 9. Validation authority

Reference implementation: `src/rfc/phase_clock_relational_volume.py`.
Reference tests: `tests/reference/test_rfs15_phase_clock_relational_volume.py`.
Validation receipt: `validation/RF_S15_PHASE_CLOCK_RELATIONAL_VOLUME_V0_1.json`.

Stack parent: RF-S14 exact-green head `78faa79da182e5d70a851d746dcf9f75d0d325bb`, RFC reference suite #280 SUCCESS.
