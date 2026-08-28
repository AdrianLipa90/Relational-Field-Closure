# RF-E5 — On-Shell Scalar Carrier-Energy Firewall

Status: `EXACT_HOMOGENEOUS_ONSHELL_SCALAR_REDUCTION / RF_E6_SIGNATURE_ALIGNMENT_PASS / DUST_SURFACE_PASS / ENERGY_PER_CARRIER_FACTOR_TWO_FIREWALL`

RF-E5 consumes RF-E4 and the same complex scalar action used by RF-N1B2L/O. RF-E6 aligns that action with the canonical RFC signature `(-,+,+,+)` while preserving the on-shell energy and carrier relations.

## 1. Homogeneous massive scalar

Take

\[
\psi=Ae^{i\omega t},
\qquad
V(|\psi|^2)=m^2|\psi|^2=m^2A^2,
\]

with constant `A` and canonical signature `(-,+,+,+)`.

Using

\[
\mathcal L=-\partial_\mu\psi^*\partial^\mu\psi-m^2|\psi|^2,
\]

the homogeneous Klein–Gordon equation gives

\[
\boxed{\omega^2=m^2.}
\]

Define

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

Hence

\[
\boxed{p=0,\qquad \varepsilon_{tot}=2K.}
\]

The active weak-field Einstein source is

\[
\boxed{\varepsilon_{tot}+3p=2K.}
\]

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

The total on-shell scalar energy per carrier is

\[
\boxed{
\frac{\varepsilon_{tot}}{j_\vartheta}=\omega=2\epsilon_N.
}
\]

Thus the factor-two firewall is invariant under the RF-E6 signature transfer.

## 4. Consequence for the double-copy mass scale

RF-N1C2/RFG7 use an independently typed dimensionful scale `M_star`. Two candidate meanings remain separated:

```text
KINETIC_CARRIER       M_star = epsilon_N = omega/2
TOTAL_ONSHELL_REST    M_star = 2 epsilon_N = omega
```

Their physical selection remains the RF-N1C4 scale-typing gate.

## 5. Executable reference

The reference suite verifies:

1. `omega^2=m^2` on the homogeneous harmonic on-shell surface;
2. `V=K`;
3. `p=0`;
4. `epsilon_total=2K`;
5. `K/j=omega/2` and `epsilon_total/j=omega`;
6. active dust source `2K`;
7. RF-E6 signature transfer preserves each relation.

## 6. Advancement

```text
homogeneous quadratic scalar on-shell               PASS EXACT
canonical RFC signature transfer                     PASS EXACT
V=K dust surface                                    PASS EXACT
phase kinetic energy per carrier = omega/2          PASS EXACT
total on-shell energy per carrier = omega           PASS EXACT
factor between total and kinetic carrier energies   2 EXACT
M_star physical type                                OPEN / RF-N1C4
```
