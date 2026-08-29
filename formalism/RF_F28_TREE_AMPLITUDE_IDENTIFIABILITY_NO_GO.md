# RF-F28 — Tree-Amplitude Identifiability No-Go

Status: `REFERENCE_IMPLEMENTED_AWAITING_CI / TREE_COUPLING_NULL_DIRECTION_EXACT / GAMMA_ZETA_SEPARATE_IDENTIFICATION_IMPOSSIBLE_FROM_PURE_GRAVITY_TREE_PREFACTORS`

RF-F28 follows RF-F27. RF-F27 shows that the source and horizon routes identify the ratio `Gamma_DC/zeta_M`. RF-F28 determines whether higher-point pure-gravity tree amplitudes can break the remaining degeneracy.

They cannot on the stated double-copy coupling structure.

## 1. Double-copy coupling coordinate

RFG2 uses

\[
\boxed{
\kappa_g
=\frac{2\Gamma_{DC}g_1g_2}{M_\star}
}.
\]

RF-N1C4 writes

\[
M_\star=\zeta_M\epsilon_Q.
\]

Therefore

\[
\boxed{
\kappa_g
=\frac{2(\Gamma_{DC}/\zeta_M)g_1g_2}{\epsilon_Q}
}.
\]

Only the ratio `Gamma_DC/zeta_M` enters the gravitational coupling once the carrier-energy coordinate is used.

## 2. Exact positive scaling symmetry

For any positive `lambda`, define

\[
\boxed{
\Gamma_{DC}\mapsto\lambda\Gamma_{DC},
\qquad
\zeta_M\mapsto\lambda\zeta_M,
\qquad
M_\star\mapsto\lambda M_\star
}.
\]

Hold `g1`, `g2`, and `epsilon_Q` fixed. Then exactly

\[
\boxed{
\kappa_g\mapsto\kappa_g
}.
\]

Likewise

\[
\boxed{
\kappa_E=\frac{\kappa_g^2}{4}
}
\]

is invariant, and

\[
\boxed{
\bar M_G=\frac{M_\star}{\Gamma_{DC}g_1g_2}
}
\]

is invariant.

The carrier relation `M_star=zeta_M epsilon_Q` is preserved by the same transformation.

## 3. All tree multiplicities

The double-copy tree prefactor at multiplicity `n>=3` is

\[
\boxed{
P_n
=\left(\frac{\kappa_g}{2}\right)^{n-2}
}.
\]

Because `kappa_g` is invariant under the common positive scaling,

\[
\boxed{
P_n\mapsto P_n
\qquad\forall n\ge3.
}
\]

Therefore adding higher tree multiplicities cannot identify `Gamma_DC` and `zeta_M` separately if their only appearance is through the same double-copy coupling coordinate.

RFG29/RFG30 provide the explicit five-point project BCJ / double-copy realization; RF-F28 records the coupling-level invariance for arbitrary tree multiplicity.

## 4. Identifiability rank

Using logarithmic coordinates,

\[
\ln\kappa_g
=\ln2+\ln\Gamma_{DC}+\ln g_1+\ln g_2-\ln\zeta_M-\ln\epsilon_Q.
\]

Hence the sensitivity to

\[
(\ln\Gamma_{DC},\ln\zeta_M)
\]

is

\[
\boxed{(1,-1)}.
\]

For `kappa_E` it is

\[
\boxed{(2,-2)}.
\]

Both have rank one. Their common null direction is

\[
\boxed{(1,1)}.
\]

Thus the two-dimensional `(Gamma_DC,zeta_M)` coordinate plane contains one gravitationally identifiable direction and one exact positive-scaling null direction.

The identifiable coordinate is

\[
\boxed{\Gamma_{DC}/\zeta_M}.
\]

## 5. Kinetic/rest degeneracy as a special case

RF-N1C4 gives

```text
KINETIC_CARRIER       zeta_M = 1
TOTAL_ONSHELL_REST    zeta_M = 2
```

If simultaneously

\[
\Gamma_{DC}^{rest}=2\Gamma_{DC}^{kin},
\]

then both surfaces have identical

\[
\Gamma_{DC}/\zeta_M,
\quad
\kappa_g,
\quad
\kappa_E,
\quad
\bar M_G,
\quad
P_n
\]

for every tree multiplicity.

No pure-gravity tree amplitude can choose between these two carrier-energy meanings through its overall coupling normalization.

## 6. Consequence for physical promotion

The degeneracy must be broken by an independently typed non-gravitational input, for example the physical meaning of `M_star` / `zeta_M` in the carrier or matter sector.

The gravity output, the Einstein coupling, horizon normalization, and higher-point tree prefactors cannot be used to make that choice without circularity.

The remaining frontier is therefore evidence, not another pure-gravity tree identity:

```text
RF-F27 source route             -> Gamma_DC/zeta_M
RF-F28 all tree prefactors      -> same ratio only
independent carrier typing      -> zeta_M
ratio + zeta_M                  -> Gamma_DC
RF-F25 cross-system receipt     -> universal reduced gravity scale test
```
