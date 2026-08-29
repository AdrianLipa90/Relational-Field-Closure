# RF-S18 — Relational Generator → Relativistic Dust Stress-Energy Lift

Status: `EXACT_DUST_TENSOR_LIFT / EXACT_RF_E11_ADM_PROJECTIONS / EXACT_RF_E12_E13_SOURCE_INSERTION`

RF-S18 is stacked on exact-green RF-S17. RF-S13–RF-S17 close the scalar source density carried by the relational generator,

\[
\boxed{
\rho_G
=\frac{B\omega\mathcal N}{AR}(\phi+\kappa),
\qquad
\kappa=\frac{\ln2}{24\pi}.
}
\]

RF-S18 promotes this scalar rest-frame energy density into the full relativistic dust stress-energy tensor and then into the already-derived RF-E11/RF-E12/RF-E13 ADM source slots.

## 1. Dust lift

On the nonnegative source branch, identify

\[
\boxed{\rho_0:=\rho_G\ge0}
\]

as the comoving/rest-frame dust energy density.

Let the local Eulerian three-velocity be

\[
\mathbf v=(v^1,v^2,v^3),
\qquad
\beta^i:=v^i/c,
\qquad
\beta^2<1,
\]

with

\[
\boxed{\gamma=(1-\beta^2)^{-1/2}.}
\]

In the RF-E11 local orthonormal frame with signature `(-,+,+,+)`, take

\[
u^\mu=\gamma(1,\boldsymbol\beta),
\qquad
u_\mu=\gamma(-1,\boldsymbol\beta).
\]

The pressureless matter tensor is

\[
\boxed{
T_{\mu\nu}^{(G)}=\rho_0u_\mu u_\nu.
}
\]

## 2. Exact RF-E11 projections

RF-E11 defines

\[
\rho_n=T_{\mu\nu}n^\mu n^\nu,
\qquad
j_i=-T_{0i},
\qquad
S_{ij}=T_{ij}
\]

in the adapted orthonormal frame. The dust tensor therefore gives exactly

\[
\boxed{\rho_n=\rho_0\gamma^2,}
\]

\[
\boxed{j_i=\rho_0\gamma^2\beta_i,}
\]

and

\[
\boxed{S_{ij}=\rho_0\gamma^2\beta_i\beta_j.}
\]

Thus the original scalar generator now supplies all ADM matter projections once a local velocity is supplied.

## 3. Exact dust identities

The spatial stress trace is

\[
S=\rho_0\gamma^2\beta^2.
\]

Using \(\gamma^2(1-\beta^2)=1\),

\[
\boxed{-\rho_n+S=-\rho_0.}
\]

Hence

\[
\boxed{\rho_0=\rho_n-S.}
\]

The ADM momentum reconstructs the local velocity:

\[
\boxed{\beta_i=\frac{j_i}{\rho_n}}
\]

for nonzero \(\rho_n\).

The rank-one dust stress also satisfies

\[
\boxed{|\mathbf j|^2=\rho_nS.}
\]

These provide executable tensor-consistency receipts independent of the generator normalization.

## 4. Direct generator form

Substituting the relational source gives

\[
\boxed{
\rho_n
=\gamma^2
\frac{B\omega\mathcal N}{AR}(\phi+\kappa),
}
\]

\[
\boxed{
j_i
=\gamma^2\beta_i
\frac{B\omega\mathcal N}{AR}(\phi+\kappa),
}
\]

and

\[
\boxed{
S_{ij}
=\gamma^2\beta_i\beta_j
\frac{B\omega\mathcal N}{AR}(\phi+\kappa).
}
\]

On the RF-S15 full tetrahedral phase-clock surface,

\[
AR=\frac{\pi c^3}{|\omega|^3},
\]

so

\[
\boxed{
\rho_n
=\gamma^2
\frac{B\mathcal N}{\pi c^3}
\omega|\omega|^3(\phi+\kappa).
}
\]

For positive frequency this is

\[
\boxed{
\rho_n
=\gamma^2
\frac{B\mathcal N\omega^4}{\pi c^3}(\phi+\kappa).
}
\]

## 5. RF-E12 Hamiltonian and momentum constraints

RF-E12 already derives

\[
{}^{(3)}R+K^2-K_{ij}K^{ij}
=2\kappa_E\rho_n,
\]

and

\[
D_jK^j{}_i-D_iK=\kappa_Ej_i.
\]

The generator dust lift supplies the exact matter sides

\[
\boxed{
2\kappa_E\rho_n
=2\kappa_E\rho_0\gamma^2,
}
\]

\[
\boxed{
\kappa_Ej_i
=\kappa_E\rho_0\gamma^2\beta_i.
}
\]

Thus the same relational generator sources both the Hamiltonian and momentum constraints once its local relativistic transport velocity is specified.

## 6. RF-E13 evolution source

RF-E13 carries the matter term

\[
\kappa_E\left[
\frac12h_{ij}(S-\rho_n)-S_{ij}
\right].
\]

In the local orthonormal spatial frame this becomes

\[
\boxed{
\kappa_E\rho_0\gamma^2
\left[
\frac12(\beta^2-1)\delta_{ij}
-\beta_i\beta_j
\right].
}
\]

Therefore RF-S18 supplies the complete dust contribution to the already-derived ADM evolution spine.

## 7. Current/source crosslink

RF-S16 gives

\[
\rho_0=\epsilon_Qj_Q.
\]

Hence the relativistic source projections may equivalently be written

\[
\boxed{
\rho_n=\gamma^2\epsilon_Qj_Q,
\qquad
j_i^{ADM}=\gamma^2\beta_i\epsilon_Qj_Q,
\qquad
S_{ij}=\gamma^2\beta_i\beta_j\epsilon_Qj_Q.
}
\]

The conserved carrier current and the ADM momentum source are different typed objects: \(j_Q\) is the scalar carrier density on the selected slice, while \(j_i^{ADM}\) is the spatial momentum projection of stress-energy. RF-S18 keeps this distinction explicit.

## 8. Advancement

```text
rho_G -> comoving dust rho_0                              PASS EXACT BRANCH
T_mn=rho_0 u_m u_n                                       PASS EXACT
rho_n=rho_0 gamma^2                                      PASS EXACT
j_i=rho_0 gamma^2 beta_i                                 PASS EXACT
S_ij=rho_0 gamma^2 beta_i beta_j                         PASS EXACT
rho_0=rho_n-S                                            PASS EXACT
beta_i=j_i/rho_n                                         PASS EXACT
|j|^2=rho_n S                                            PASS EXACT
RF-E12 Hamiltonian source insertion                      PASS EXACT PARENT COMPOSITION
RF-E12 momentum source insertion                         PASS EXACT PARENT COMPOSITION
RF-E13 evolution matter source insertion                 PASS EXACT PARENT COMPOSITION
physical local transport velocity                        OPEN INPUT
physical dust equation-of-state selection                OPEN INPUT / RF-S14
absolute kappa_E/G project promotion                     OPEN INPUT
```

## 9. Validation authority

Reference implementation: `src/rfc/relational_generator_dust_stress_energy.py`.
Reference tests: `tests/reference/test_rfs18_relational_generator_dust_stress_energy.py`.
Validation receipt: `validation/RF_S18_RELATIONAL_GENERATOR_DUST_STRESS_ENERGY_V0_1.json`.

Stack parent: RF-S17 exact-green head `34255471c3b56d8e21578bb212b27e5330d7d300`, RFC reference suite #283 SUCCESS.
