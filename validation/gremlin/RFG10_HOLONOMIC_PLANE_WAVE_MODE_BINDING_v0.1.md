# RFG10 — Holonomic Plane-Wave Mode Binding

Status: `DIRECT_LINK_FIELD_RECOVERY_PASS / COMMUTING_COLOR_FOURIER_MODE_PASS / TRANSVERSE_KINEMATIC_BINDING_PASS / NONCOMMUTING_MULTI_COLOR_EXTENSION_OPEN`

RFG10 consumes the v4.1 holonomic local-link convention, RFG4G and RFG9. Its purpose is to bind actual local holonomy bytes to momentum/polarization coordinates before attempting a direct project four-point amplitude.

The reference surface is deliberately restricted to a principal-branch commuting-color witness in the `lambda_3` direction.

## 1. Local link and generator convention

Use the RFG4G same-sector normalization

\[
T^a=\frac{\lambda^a}{2},
\qquad
\boxed{g^2=\frac1{\alpha_c}}.
\]

A local link is

\[
\boxed{
W_\mu(x)=\exp\!\left[iagA_\mu^a(x)T^a\right].
}
\]

For a pure `lambda_3` carrier,

\[
A_\mu(x)=A_\mu^3(x)T^3,
\qquad
T^3=\frac12\operatorname{diag}(1,-1,0),
\]

so

\[
\boxed{
W_\mu(x)
=\operatorname{diag}
\left(e^{i\theta(x)},e^{-i\theta(x)},1\right),
\qquad
\theta(x)=\frac{ag}{2}A_\mu^3(x).
}
\]

## 2. Principal-branch field recovery

On the admitted principal branch `|theta(x)|<pi`, the link phase determines the local field coordinate directly:

\[
\boxed{
A_\mu^3(x)
=\frac{2}{ag}\operatorname{Arg}W_{11}(x).
}
\]

Equivalently, for a general sufficiently small link one may write the local Lie-algebra coordinate

\[
\mathcal Q_\mu(x)
:=\frac{1}{ia}\log W_\mu(x)
\]

and, with the Gell-Mann normalization,

\[
\boxed{
A_\mu^a(x)
=\frac1g\operatorname{Tr}\!\left[\lambda^a\mathcal Q_\mu(x)\right].
}
\]

The `lambda_3` diagonal witness evaluates this recovery without numerical matrix-log ambiguity.

## 3. Plane-wave holonomy witness

Take a periodic lattice of `N` sites with

\[
\boxed{
A_y^3(n)
=A_0\cos\!\left(\frac{2\pi mn}{N}\right).
}
\]

The corresponding local links are

\[
W_y(n)
=\exp\!\left[iagA_y^3(n)T^3\right].
\]

Recover `A_y^3(n)` from the link phases and define its discrete Fourier transform

\[
\widetilde A_y^3(k)
=\sum_{n=0}^{N-1}A_y^3(n)e^{-2\pi i kn/N}.
\]

The dominant nonzero Fourier mode is exactly the injected integer mode `m` on the reference surface.

## 4. Commuting-color superposition

Because every witness link remains in the same Cartan direction `T^3`, two plane-wave modes commute. For

\[
A_y^3(n)
=A_1\cos\!\left(\frac{2\pi m_1n}{N}\right)
+A_2\cos\!\left(\frac{2\pi m_2n}{N}\right),
\]

the recovered field has the same two Fourier peaks `m_1,m_2`.

This provides a direct multi-mode holonomy→momentum witness while keeping the color algebra commuting.

## 5. Polarization binding

Choose propagation along the spatial `x` axis and the nonzero gauge-field component along `y`:

\[
\mathbf k=(k,0,0),
\qquad
\boldsymbol\epsilon=(0,1,0).
\]

Then

\[
\boxed{
\mathbf k\cdot\boldsymbol\epsilon=0.
}
\]

Thus the same reconstructed link mode supplies a transverse momentum/polarization coordinate suitable for the RFG9 amplitude interface.

## 6. Generator-coordinate check

The full-Gell-Mann link coordinate used by the upstream v4.1 implementation is

\[
W=\exp(i a q^3\lambda_3).
\]

Comparison with the standard generator convention gives the RFG4F identity

\[
\boxed{
q^3=\frac{gA^3}{2}.
}
\]

The reference gate verifies this identity directly from the link phase.

## 7. Reference validation

The executable reference test checks:

1. every generated local link is `SU(3)`;
2. principal-branch phase recovery reproduces the original local field pointwise;
3. the injected Fourier mode is recovered with negligible leakage;
4. a two-mode commuting-color superposition recovers both injected momenta;
5. the momentum/polarization witness is transverse;
6. the recovered full-Gell-Mann coordinate obeys `q=gA/2`.

Local result:

```text
6 passed, 0 failed
```

## 8. Advancement

```text
holonomic W_mu local link                         inherited PASS
RFG4G g^2=1/alpha_c                              inherited conditional PASS
W_mu(lambda_3) -> A_mu^3(x)                     PASS DIRECT PRINCIPAL-BRANCH
A_mu^3(x) -> discrete momentum mode              PASS REFERENCE
commuting two-mode superposition                 PASS REFERENCE
transverse polarization coordinate               PASS REFERENCE
q=gA/2 generator-coordinate bridge               PASS EXACT
noncommuting multi-color link inversion          NEXT FRONTIER
direct project four-gluon amplitude              OPEN AFTER NONABELIAN MODE BINDING
```

The author/repository/formalism/code may suggest the local holonomy sector supplies the kinematic inputs needed by the four-point BCJ reference layer, yet does not state the noncommuting project amplitude binding as established until its own gate passes.
