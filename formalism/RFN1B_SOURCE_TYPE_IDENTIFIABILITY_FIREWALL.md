# RF-N1B — Source-Type and Identifiability Firewall

Status: `EXACT_TYPE_SEPARATION_PASS / MATTER_SOURCE_MAP_OPEN / COUPLING_NORMALIZATION_OPEN`

RF-N1A derives the local principal source operator acting on the relational lapse,

\[
\Delta_h u=\mathcal S_R,
\qquad
u:=\ln N_R,
\qquad
\Phi_R:=c^2u,
\]

with

\[
[\mathcal S_R]=L^{-2}.
\]

This gate determines which upstream quantities can and cannot yet be called a Newtonian matter source. It does not fit a source law.

## 1. Three quantities that must remain distinct

### 1.1 IDT relational density

IDT 00C introduces positive scalar fields

\[
\rho_R(s)>0,
\qquad
\eta_R(s)>0,
\]

through the symmetric mobility

\[
M_{ab}
=\frac{\sqrt{\rho_R(a)\rho_R(b)}}{\tfrac12[\eta_R(a)+\eta_R(b)]}.
\]

At that gate `rho_R` is a relational kinetic/mobility scalar. No physical mass-density type `M L^-3` is assigned to it by 00C. Therefore

\[
\boxed{
\rho_R\not\equiv\rho_m
}
\]

at the present dependency level.

The later IDT lapse relation

\[
N_R
=\frac{M_x\cosh(A_x/2)}{M_{ref}\cosh(A_{ref}/2)}
\]

uses `rho_R` only through the mobility ratio. This does not add mass semantics.

### 1.2 IDT phase energy

IDT 01L admits the phase-energy calibration

\[
\boxed{E=\hbar|\omega|}
\]

and therefore

\[
\ell_\varphi=\frac{\hbar c}{E}.
\]

This gives a local energy scale. It does not by itself define an energy **density**, rest-mass density, number density, occupation number or stress-energy tensor.

Thus

\[
\boxed{
E\ \text{alone}\not\Rightarrow\rho_m.
}
\]

### 1.3 Temporal information curvature

The TIR×IDT interface supplies

\[
\Xi_I
=\frac{\mathcal J_\pi}{\mathcal A_{rel}},
\qquad
[\Xi_I]=L^{-2}.
\]

This is already correctly typed for `S_R`. Type compatibility permits it to enter a source basis, but type compatibility does not establish matter semantics:

\[
\boxed{
[\Xi_I]=[\mathcal S_R]
\quad\not\Rightarrow\quad
\Xi_I=\mathcal S_R.
}
\]

## 2. TIR mass formulas do not close this gate

The active TIR claim hierarchy classifies the exponential mass ansatz

\[
m=E_Pe^{-S/\kappa}
\]

as a class-B/C model construction depending on sector, and explicitly states that it is not a universal established mass law. Therefore historical or sector-specific TIR mass assignments cannot silently be promoted into the independent Newtonian source density required here.

The RF-N1B source bridge must have its own derivation and admission receipt.

## 3. Geometry supplies a local volume form, but occupancy remains independent

The RF-02H physicalized spatial metric supplies a local Riemannian volume element

\[
\boxed{
dV_h=\sqrt{\det h}\,d^3X.
}
\]

For an orthonormal reference-coordinate cell with the regular coframe scale

\[
a_H=\frac{c}{\sqrt6|\omega|},
\]

a coordinate unit cell would carry the candidate physical volume

\[
\boxed{V_H=a_H^3}
\]

**only after** the discrete cell-to-physical-volume binding is admitted. The hexahedral Bloch dual frame by itself fixes directions and metric scale, not the physical occupation content assigned to a cell.

Even after a volume map is admitted, converting a local energy scale into an energy density requires an independent occupation/source weight `n_E`:

\[
\boxed{
\varepsilon_{cell}
=\frac{n_EE}{V_H}.
}
\]

A rest-mass-density candidate would then be

\[
\boxed{
\rho_{cell}
=\frac{\varepsilon_{cell}}{c^2}
=\frac{n_EE}{c^2V_H}.
}
\]

The dimensions are correct, but `n_E` and the physical cell-volume interpretation are not currently derived source variables. Therefore this is a candidate bridge, not a source identification.

## 4. Conditional phase-cell density formula

If, only for a source-bridge test, one admits

\[
V_H=a_H^3,
\qquad
a_H=\frac{c}{\sqrt6|\omega|},
\qquad
E=\hbar|\omega|,
\]

then

\[
\boxed{
\rho_{cell}
=6\sqrt6\,n_E\frac{\hbar|\omega|^4}{c^5}.
}
\]

This equation is an exact dimensional/algebraic consequence of those three admitted bindings. It is **not** a derivation of matter density because the occupation map `n_E` is still free.

The result is useful because it exposes a stringent consistency condition rather than hiding the missing source physics.

## 5. Consistency condition with the information-curvature source candidate

For a constant-rate projective cell,

\[
\Xi_I
=\frac{\mathcal J_\pi}{a_{FS}}
\left(\frac{\omega}{c}\right)^2.
\]

Suppose a later source derivation selected

\[
\mathcal S_R=\beta_I\Xi_I.
\]

Suppose independently that the phase-cell matter bridge of Sec. 4 were admitted. Requiring the Newton target

\[
c^2\mathcal S_R=4\pi G\rho_{cell}
\]

would imply the **consistency relation**

\[
\boxed{
G
=\frac{\beta_I\mathcal J_\pi}{24\pi\sqrt6\,n_Ea_{FS}}
\frac{c^5}{\hbar\omega^2}.
}
\]

This is not used to define `G`. It shows exactly what would have to become invariant if both candidate bridges were independently derived.

For a universal Newton coupling, the combination

\[
\boxed{
\frac{\beta_I\mathcal J_\pi}
{n_Ea_{FS}\omega^2}
}
\]

must have the appropriate source-independent behavior across admitted weak-field systems. If it varies generically, the joint candidate is falsified or requires an additional invariant mechanism.

Thus RF-N1B converts a vague freedom into a measurable universality condition.

## 6. Constructive non-identifiability theorem

Let the current admitted data determine

\[
(N_R,h_{ij},\Xi_I,E)
\]

but leave the occupation/source map unspecified. Choose two distinct positive dimensionless maps

\[
n_E^{(1)}(x)\neq n_E^{(2)}(x).
\]

Both yield dimensionally valid candidate densities

\[
\rho_{cell}^{(k)}
=\frac{n_E^{(k)}E}{c^2V_H},
\qquad k=1,2,
\]

while leaving all RF-N0 lapse kinematics and RF-N1A operator identities unchanged.

Therefore the existing premise set does not identify a unique physical matter density:

\[
\boxed{
\text{current upstream state}
\not\Rightarrow
\text{unique }\rho_m.
}
\]

The same argument applies to `beta_I`: different dimensionless coefficients preserve source typing while changing the physical source equation. Hence

\[
\boxed{
\text{current upstream state}
\not\Rightarrow
\text{unique }G.
}
\]

This is an identifiability theorem for the present dependency set, not a statement that such a derivation is impossible after an additional physical source primitive/interface is admitted.

## 7. Minimal source bridge that would close RF-N1B

A promotable Newton source bridge must independently provide all of:

1. a local source-count/occupation or conserved matter-current carrier;
2. a physical volume/measure map compatible with the RF-02H/RF-02I geometry;
3. an energy/rest-mass assignment for that source carrier;
4. a conservation law under the admitted temporal transport;
5. a coefficient map from that source density to `S_R`;
6. source-independence/universality tests of the resulting weak coupling.

Only after these exist may RFC test

\[
\boxed{
c^2\mathcal S_R\stackrel{?}{=}4\pi G\rho_m}
\]

against the Newton target.

## 8. Advancement

RF-N1B closes the type question even though the matter-source derivation remains open:

```text
rho_R       = relational kinetic/mobility scalar
E=hbar|ω|   = local calibrated phase-energy scale
Xi_I        = inverse-area information-curvature scalar
V_h         = geometric volume form after physical metric binding
rho_m       = requires an independent source occupation/current + measure + energy map
```

The next gate is therefore no longer “find a scalar with the right units.” It is:

\[
\boxed{
\text{derive a conserved physical source carrier and its measure}
}
\]

from the admitted TIR/IDT relational dynamics, then test whether its coupling to the already-derived lapse operator is universal.
