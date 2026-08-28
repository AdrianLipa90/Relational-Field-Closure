# RF-N1C4 — Double-Copy Carrier-Energy Type Firewall

Status: `EXACT_SCALE_TYPE_FACTORIZATION / KINETIC_VS_TOTAL_REST_BRANCHES / KAPPA_E_FACTOR_FOUR_DISCRIMINANT / PHYSICAL_TYPE_OPEN`

RF-N1C4 consumes RF-E5, RF-N1C2, RFG4G and RFG7. It keeps the dimensionful double-copy normalization scale `M_star` physically typed after RF-E5 shows that phase-kinetic energy-per-carrier and total on-shell rest-energy-per-carrier differ by a factor of two on the simplest homogeneous massive scalar surface.

## 1. Scale-type coordinate

RF-N1B2N/O define

\[
\epsilon_N=\frac{\omega_Q}{2}.
\]

Introduce the dimensionless type coordinate

\[
\boxed{\zeta_M:=\frac{M_\star}{\epsilon_N}.}
\]

Two explicitly typed candidate surfaces are:

```text
KINETIC_CARRIER       zeta_M = 1, M_star = epsilon_N = omega_Q/2
TOTAL_ONSHELL_REST    zeta_M = 2, M_star = 2 epsilon_N = omega_Q
```

RF-E5 supplies the second relation for the homogeneous on-shell quadratic scalar; it does not by itself decide which physical role the double-copy normalization scale must carry.

## 2. Reduced gravity scale

RFG4G/RFG7 give

\[
\bar M_G=\frac{\alpha_cM_\star}{\Gamma_{DC}}.
\]

Therefore

\[
\boxed{
\bar M_G
=\frac{\zeta_M\alpha_c\omega_Q}{2\Gamma_{DC}}.
}
\]

The Einstein amplitude/field coupling is

\[
\boxed{
\kappa_E=\frac1{\bar M_G^2}
=\frac{4\Gamma_{DC}^2}{\zeta_M^2\alpha_c^2\omega_Q^2}.
}
\]

## 3. Two scale surfaces

### Kinetic-carrier surface

For `zeta_M=1`,

\[
\boxed{
\kappa_E^{kin}
=\frac{4\Gamma_{DC}^2}{\alpha_c^2\omega_Q^2}.
}
\]

This is the explicit candidate surface used by RFG17.

### Total on-shell rest-energy surface

For `zeta_M=2`,

\[
\boxed{
\kappa_E^{rest}
=\frac{\Gamma_{DC}^2}{\alpha_c^2\omega_Q^2}.
}
\]

Hence

\[
\boxed{\kappa_E^{rest}=\frac14\kappa_E^{kin}}
\]

for the same `alpha_c`, `omega_Q` and `Gamma_DC`.

Equivalently the reduced gravity scale doubles:

\[
\boxed{\bar M_G^{rest}=2\bar M_G^{kin}.}
\]

## 4. Physical promotion rule

The factor-of-four difference is not a numerical nuisance. It reflects two physically distinct meanings for `M_star`.

Promotion therefore requires an independent statement of whether the dimensionful double-copy scale is:

- the phase-kinetic energy per conserved carrier;
- the total on-shell rest energy per conserved carrier;
- or a separately derived scale with another provenance.

The gravity output itself may not be used to choose the branch.

## 5. Horizon relation

RF-N1C3/RFG17 give

\[
\kappa_E=\frac1{M_HT_H}.
\]

Combining with the general scale-type expression gives

\[
\boxed{
\frac{4\Gamma_{DC}^2}{\zeta_M^2\alpha_c^2\omega_Q^2}
=\frac1{M_HT_H}.
}
\]

or

\[
\boxed{
\frac{\Gamma_{DC}}{\zeta_M}
=\frac{\alpha_c\omega_Q}{2\sqrt{M_HT_H}}.
}
\]

Thus the horizon route constrains the ratio `Gamma_DC/zeta_M`. Independent normalization of either factor is required to determine the other.

## 6. Executable reference

The reference test verifies:

1. `zeta_M=1` reproduces the RFG17 kinetic expression;
2. `zeta_M=2` produces exactly one quarter of that `kappa_E`;
3. the total-rest expression is `Gamma_DC^2/(alpha_c^2 omega_Q^2)`;
4. the reduced gravity scale doubles between the two surfaces;
5. a horizon value generated on one fixed type surface distinguishes the other when `Gamma_DC` is held independently fixed;
6. the two type coordinates are exactly `1` and `2` on the defined surfaces.

Local result:

```text
6 passed, 0 failed
```

## 7. Advancement

```text
RF-E5 carrier-energy factor two                     PASS EXACT
M_star/epsilon_N type coordinate zeta_M             DEFINED
kinetic carrier surface zeta_M=1                    PASS CONDITIONAL
on-shell rest surface zeta_M=2                      PASS CONDITIONAL
kappa_E factor-four split                           PASS EXACT
Gamma_DC/zeta_M horizon invariant                   NEXT IDENTIFIABILITY GATE / RFG18
physical M_star type                                OPEN INDEPENDENT EVIDENCE
```
