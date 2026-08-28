# RF-E4 — Phase-Kinetic Stress-Energy / Pressure Firewall

Status: `EXACT_STRESS_TENSOR_DERIVATION / RFN1B2O_ENERGY_DENSITY_MATCH / EINSTEIN_ACTIVE_SOURCE_PRESSURE_FIREWALL / TOTAL_MATTER_CLOSURE_OPEN`

RF-E4 consumes RF-N1B2L/O and the Einstein coupling/action normalization already fixed by RF-E3. Its purpose is to promote the scalar phase source from an energy-density coordinate to an explicit covariant stress-energy tensor and to expose the pressure term that must be included before Newton and Einstein source maps are identified.

## 1. Upstream phase action

RF-N1B2L starts from

\[
\mathcal L=\partial_\mu\psi^*\partial^\mu\psi-V(|\psi|^2),
\qquad \psi=Ae^{i\vartheta}.
\]

On the admitted pure phase sector with fixed amplitude and gauge-covariant phase one-form `q_mu := D_mu vartheta`,

\[
\boxed{\mathcal L_{phase}=A^2 q_\mu q^\mu.}
\]

Using signature `(+---)`, the metric stress tensor is

\[
\boxed{
T_{\mu\nu}^{phase}
=2A^2q_\mu q_\nu-g_{\mu\nu}A^2q_\alpha q^\alpha.
}
\]

This follows from the same scalar action; no independent matter-source coefficient is introduced.

## 2. RF-N1B2O normal-flow match

For the pure normal phase-rate sector in an orthonormal frame,

\[
q_{\hat a}=(r_n,0,0,0)
\]

in natural units. Define

\[
K:=A^2r_n^2.
\]

Then

\[
\boxed{T_{\hat0\hat0}^{phase}=K=\mathcal E_\vartheta}
\]

which exactly reproduces the RF-N1B2O local phase-energy density.

The spatial diagonal components are

\[
\boxed{T_{\hat i\hat j}^{phase}=K\,\delta_{ij}.}
\]

Thus the pure normal phase-kinetic sector has

\[
\boxed{\varepsilon=K,\qquad p=K.}
\]

It is therefore a stiff phase-kinetic stress sector rather than a pressureless dust source.

## 3. Einstein active-source firewall

For an isotropic static weak-field source, the Einstein source combination entering the Newtonian `00` equation is proportional to

\[
\varepsilon+3p.
\]

For the pure phase-kinetic sector,

\[
\boxed{\varepsilon+3p=4K.}
\]

Therefore the RF-N1B2O mass-density coordinate

\[
\rho_\vartheta=K/c^2
\]

and the corresponding Einstein active-density coordinate obey

\[
\boxed{
\rho_{active}^{phase}=4\rho_\vartheta
}
\]

on this pure normal phase-kinetic surface.

This is a required relativistic source correction. RF-N1B2O remains the exact local phase-energy factorization; RF-E4 shows that total Einstein-source promotion must also account for stress/pressure.

## 4. Homogeneous potential/rest completion

Retain a homogeneous scalar potential/rest contribution `V`. Then

\[
\mathcal L=K-V,
\]

and

\[
\boxed{\varepsilon=K+V,\qquad p=K-V.}
\]

Hence

\[
\boxed{\varepsilon+3p=4K-2V.}
\]

Two distinct closure surfaces follow.

### A. Pressureless/dust surface

Requiring

\[
p=0
\]

gives

\[
\boxed{V=K,\qquad \varepsilon_{tot}=2K.}
\]

### B. Preserve the RF-N1B2O phase-energy value as the active Newton source

If the intended weak-field active source is required to equal the already-defined phase kinetic value `K`, then

\[
4K-2V=K
\]

requires

\[
\boxed{V=\frac32K.}
\]

These are different physical closure conditions and must not be conflated.

## 5. Einstein bridge

RF-E3 supplies

\[
G_{\mu\nu}=\kappa_E T_{\mu\nu},
\qquad \kappa_E=8\pi G/c^4.
\]

RF-E4 therefore upgrades the phase source path to

```text
RF-N1B2L scalar action
 -> RF-N1B2O local phase energy K=A^2 r_n^2
 -> RF-E4 T_mu_nu^phase
 -> pressure/stress contribution
 -> Einstein source
```

The remaining total-matter gate must specify the admitted amplitude-gradient, potential/rest and any additional sectors before a universal Newton-source identification is promoted.

## 6. Executable reference

The reference test verifies:

1. `T_00=K` for the pure normal phase sector;
2. `p_x=p_y=p_z=K`;
3. `epsilon+3p=4K`;
4. with potential, `epsilon=K+V`, `p=K-V` and active source `4K-2V`;
5. the dust surface `V=K`;
6. the RF-N1B2O-active-source preservation surface `V=3K/2`.

Local result:

```text
6 passed, 0 failed
```

## 7. Advancement

```text
RF-N1B2O phase energy density                      PASS EXACT CONDITIONAL
metric stress tensor from same phase action        PASS EXACT
T_00 = E_theta on normal phase flow                PASS EXACT
phase-only equation of state p=epsilon             PASS EXACT
phase-only Einstein active density = 4 rho_theta   PRESSURE FIREWALL
homogeneous potential/rest completion              PARAMETRIC EXACT
V=K dust surface                                   EXACT CONDITION
V=3K/2 preserve-K active-source surface             EXACT CONDITION
total matter stress-energy composition             NEXT EINSTEIN FRONTIER
```
