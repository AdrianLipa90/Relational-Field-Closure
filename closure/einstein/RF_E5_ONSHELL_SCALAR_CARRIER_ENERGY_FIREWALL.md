# RF-E5 — On-Shell Scalar Carrier-Energy Firewall

Status: `EXACT_HOMOGENEOUS_ONSHELL_SCALAR_REDUCTION / DUST_SURFACE_PASS / ENERGY_PER_CARRIER_FACTOR_TWO_FIREWALL`

RF-E5 consumes RF-E4 and the same complex scalar action already used by RF-N1B2L/O. It asks what the phase-kinetic energy-per-Noether-carrier becomes when the simplest homogeneous massive scalar sector is placed on shell.

## 1. Homogeneous massive scalar

Take

\[
\psi=Ae^{i\omega t},
\qquad
V(|\psi|^2)=m^2|\psi|^2=m^2A^2,
\]

with constant `A` and signature `(+---)`.

The Klein-Gordon equation on this homogeneous harmonic sector gives

\[
\boxed{\omega^2=m^2.}
\]

Define the phase kinetic density

\[
\boxed{K:=A^2\omega^2.}
\]

Then on shell

\[
\boxed{V=K.}
\]

## 2. Dust-like stress tensor on this surface

RF-E4 gives

\[
\varepsilon=K+V,
\qquad
p=K-V.
\]

Hence the on-shell quadratic-potential surface gives

\[
\boxed{p=0,\qquad \varepsilon_{tot}=2K.}
\]

The active weak-field Einstein source is therefore

\[
\boxed{\varepsilon_{tot}+3p=2K.}
\]

Thus the simplest on-shell massive homogeneous scalar lands on the RF-E4 dust surface automatically.

## 3. Noether-carrier normalization

The phase Noether density remains

\[
\boxed{j_\vartheta=2A^2\omega.}
\]

The phase-kinetic energy per carrier is

\[
\boxed{
\frac{K}{j_\vartheta}=\frac\omega2=\epsilon_N.
}
\]

But the total on-shell scalar energy per carrier is

\[
\boxed{
\frac{\varepsilon_{tot}}{j_\vartheta}=\omega=2\epsilon_N.
}
\]

Therefore `epsilon_N` is exactly the phase-kinetic energy-per-Noether-charge coordinate on this sector, while the total on-shell rest-energy-per-carrier differs by a factor of two.

## 4. Consequence for the double-copy mass scale

RF-N1C2/RFG7 use an independently typed dimensionful scale `M_star`. Two distinct candidate meanings must therefore remain separated:

```text
KINETIC_CARRIER       M_star = epsilon_N = omega/2
TOTAL_ONSHELL_REST    M_star = 2 epsilon_N = omega
```

The algebra alone does not select which physical meaning the double-copy normalization scale is intended to carry.

## 5. Executable reference

The reference test verifies:

1. `omega^2=m^2` on the homogeneous harmonic on-shell surface;
2. `V=K`;
3. `p=0`;
4. `epsilon_total=2K`;
5. `K/j=omega/2` while `epsilon_total/j=omega`;
6. the active dust source equals `2K`.

Local result:

```text
6 passed, 0 failed
```

## 6. Advancement

```text
homogeneous quadratic scalar on-shell              PASS EXACT
V=K dust surface                                   PASS EXACT
phase kinetic energy per carrier = omega/2         PASS EXACT
total on-shell energy per carrier = omega           PASS EXACT
factor between total and kinetic carrier energies   2 EXACT
M_star physical type                               OPEN / RF-N1C4
```
