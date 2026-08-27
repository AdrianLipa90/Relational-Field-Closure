# RF-02 — Polyhedral Geometric Invariants on the Bloch Sphere

**Status:** EXACT_DISCRETE_GEOMETRY / CONTINUUM_PHYSICAL_BINDING_OPEN

RF-02 promotes the polyhedral layer from a visual construction to a coordinate-independent relational geometry on \(\mathbb{CP}^1\).

For rays \([\psi_a]\), define the Fubini--Study edge distance

\[
\boxed{d^{\rm FS}_{ab}=\arccos|\langle\psi_a|\psi_b\rangle|}
\]

and transition matrix

\[
\boxed{P_{ab}=|\langle\psi_a|\psi_b\rangle|^2.}
\]

Both are invariant under global \(SU(2)\) rotations and local phase representatives of the rays.

For oriented triples define the Bargmann invariant

\[
\boxed{\Delta_{abc}=\langle\psi_a|\psi_b\rangle
\langle\psi_b|\psi_c\rangle
\langle\psi_c|\psi_a\rangle.}
\]

Its argument is a gauge-invariant geometric phase. For a geodesically closed face \(f\),

\[
\gamma_f=\arg\prod_{(ab)\in\partial f}\langle\psi_a|\psi_b\rangle
\]

is the discrete Berry holonomy and, modulo orientation/convention, equals one half of the enclosed solid angle:

\[
\boxed{\gamma_f=\frac12\Omega_f\pmod{2\pi}.}
\]

This produces a hierarchy

\[
\text{vertex}\to\text{edge}\to\text{face}\to\text{closed cell}\to\text{refined surface}.
\]

A polyhedral fingerprint is therefore typed as

\[
\mathfrak I(P)=
\left[
\{d^{\rm FS}_{ab}\},
\{P_{ab}\},
\{\arg\Delta_{abc}\},
\{\Omega_f\},
\{\gamma_f\},
\chi(P),
W(P)
\right].
\]

The hexahedral and higher-polyhedral layers are used as refinement cells. RFC will test which entries of \(\mathfrak I(P)\) survive subdivision/refinement and converge to continuum metric, connection and flux data.

For a closed oriented discretization covering the sphere once,

\[
\sum_f\Omega_f=4\pi,
\qquad
\sum_f\gamma_f=2\pi\pmod{2\pi},
\]

which is the discrete geometric realization of the Bloch-sphere/Berry factor \(1/2\).

No particular polyhedron is identified with physical space by shape alone. The physical candidate is the refinement-stable invariant structure.
