# RFG16 — Project Double-Copy → Einstein Coupling Gate

Status: `PROJECT_FOUR_POINT_DOUBLE_COPY_PASS / GRAVITATIONAL_WARD_PASS / PROJECT_NUMERATOR_NORMALIZATION_CORRECTED_RFG20 / EINSTEIN_MHV_NORMALIZATION_PASS / TREE_LEVEL_FOUR_POINT_SCOPE`

RFG16 consumes the project numerators produced by RFG15. No gravity amplitude is used to construct or tune those numerators. RFG20 audits their explicit normalization and fixes the coupling-conversion convention used by this gate.

For two admitted kinematic copies,

\[
(n_s,n_t,n_u),\qquad (\tilde n_s,\tilde n_t,\tilde n_u),
\]

RFG15 gives

\[
\boxed{n_s-n_t+n_u=0},\qquad\boxed{\tilde n_s-\tilde n_t+\tilde n_u=0}.
\]

## Project numerator normalization

RFG20 verifies independently

\[
\boxed{A^{project}_{1234}=-2i\,A^{PT}_{1234}}.
\]

The magnitude factor `2` is the four-point result of one absorbed `sqrt(2)` normalization per cubic vertex. For this numerator convention the compatible double-copy transfer is

\[
\boxed{g\longrightarrow\kappa_g/4}
\]

rather than `kappa_g/2`.

The corrected project double-copy amplitude is

\[
\boxed{\mathcal M_4^{project}=-i\left(\frac{\kappa_g}{4}\right)^2\left(\frac{n_s\tilde n_s}{s}+\frac{n_t\tilde n_t}{t}+\frac{n_u\tilde n_u}{u}\right).}
\]

The physical gravitational coupling remains

\[
\kappa_g^2=32\pi G,\qquad\boxed{\kappa_E=\frac{\kappa_g^2}{4}=8\pi G}.
\]

Therefore the coefficient multiplying the project-normalized numerator core is

\[
\boxed{-i\left(\frac{\kappa_g}{4}\right)^2=-\frac{i\kappa_E}{4}.}
\]

This coefficient is distinct from the physical Einstein coupling because the project numerator core carries the compensating normalization identified by RFG20.

For the spin-2 MHV sector,

\[
\boxed{\mathcal C_{--++}^{project}:=\sum_i\frac{n_i^2}{D_i}=-4\frac{s^3}{tu}.}
\]

Hence

\[
\boxed{\mathcal M_{4,--++}^{project}=i\kappa_E\frac{s^3}{tu},}
\]

matching the independent Einstein four-graviton Born normalization.

Using RFG7,

\[
\bar M_G=\frac{2}{\kappa_g},
\]

so the physical coupling identities remain

\[
\boxed{\kappa_E=\frac1{\bar M_G^2},\qquad G=\frac1{8\pi\bar M_G^2}.}
\]

The project-core coefficient is equivalently

\[
\boxed{-\frac{i}{4\bar M_G^2}}.
\]

## Gravitational Ward gate

Replacing any external polarization vector by its corresponding momentum in either copy gives a vanishing double-copy core to numerical tolerance. Copy-exchange symmetry and nonzero witnesses remain unchanged by the prefactor correction.

Corrected local reference result:

```text
6 passed, 0 failed
```

RFG20 records the normalization firewall:

```text
old +i(kappa_g/2)^2 project transfer   FAIL EXACT FACTOR -4
new -i(kappa_g/4)^2 project transfer   PASS EINSTEIN MHV
```

The admitted four-point bridge is

```text
holonomic SU(3)
 -> normalized project Yang-Mills A4
 -> project BCJ numerators
 -> project-normalized double copy [-i(kappa_g/4)^2]
 -> physical kappa_E = 8 pi G = kappa_g^2/4
 -> Einstein MHV normalization
```

RFG21 preserves pole factorization and RFG22 preserves the four-point KLT core identity; their external amplitude coefficients consume the canonical RFG20 normalization. RFG23 starts the higher-point BCJ/soft reference frontier.
