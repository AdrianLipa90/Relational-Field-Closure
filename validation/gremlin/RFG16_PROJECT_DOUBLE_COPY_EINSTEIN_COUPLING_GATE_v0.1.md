# RFG16 — Project Double-Copy → Einstein Coupling Gate

Status: `PROJECT_FOUR_POINT_DOUBLE_COPY_PASS / GRAVITATIONAL_WARD_PASS / EINSTEIN_COUPLING_PREFACTOR_EXACT / TREE_LEVEL_FOUR_POINT_SCOPE`

RFG16 consumes the project numerators produced by RFG15. No gravity amplitude is used to construct or tune those numerators.

For two admitted kinematic copies, let

\[
(n_s,n_t,n_u),\qquad
(\tilde n_s,\tilde n_t,\tilde n_u)
\]

be the RFG15 project numerator triplets, each satisfying the same oriented Jacobi identity

\[
\boxed{n_s-n_t+n_u=0},
\qquad
\boxed{\tilde n_s-\tilde n_t+\tilde n_u=0}.
\]

The four-point double-copy amplitude is

\[
\boxed{
\mathcal M_4
=i\left(\frac{\kappa_g}{2}\right)^2
\left(
\frac{n_s\tilde n_s}{s}
+\frac{n_t\tilde n_t}{t}
+\frac{n_u\tilde n_u}{u}
\right).
}
\]

RFG2 uses

\[
\kappa_g^2=32\pi G.
\]

Therefore at four points

\[
\boxed{
\left(\frac{\kappa_g}{2}\right)^2
=\frac{\kappa_g^2}{4}
=8\pi G
=\kappa_E
}
\]

in natural units. The project double-copy amplitude can consequently be written

\[
\boxed{
\mathcal M_4
=i\kappa_E
\left(
\frac{n_s\tilde n_s}{s}
+\frac{n_t\tilde n_t}{t}
+\frac{n_u\tilde n_u}{u}
\right).
}
\]

Using RFG7,

\[
\bar M_G=\frac{2}{\kappa_g},
\]

so the same prefactor is also

\[
\boxed{
\kappa_E=\frac1{\bar M_G^2},
\qquad
G=\frac1{8\pi\bar M_G^2}.
}
\]

## Gravitational Ward gate

The executable reference constructs two independent physical polarization copies. Replacing any external polarization vector by its corresponding momentum in either copy gives a vanishing double-copy amplitude to numerical tolerance. This is tested independently for all four legs in both copies over deterministic random on-shell kinematics.

The gate also verifies copy-exchange symmetry, nonzero physical witnesses, and exact scaling with `kappa_E`.

Local result:

```text
6 passed, 0 failed
```

This establishes the project four-point bridge

```text
holonomic SU(3)
 -> normalized project Yang-Mills A4
 -> project BCJ numerators
 -> project double copy
 -> kappa_E = 8 pi G = kappa_g^2/4
```

within the admitted tree-level four-point sector.

The next scientific front is no longer the existence of a gauge/gravity coupling bridge at four points. It is the extension of the project numerator construction beyond four points / MHV-like reference kinematics and the independent cross-system promotion of the reduced gravity scale `Mbar_G`.
