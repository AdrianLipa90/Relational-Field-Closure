# RF-E4 — Phase-Kinetic Stress-Energy / Pressure Firewall

Status: `EXACT_STRESS_TENSOR_DERIVATION / RFN1B2O_ENERGY_DENSITY_MATCH / RF_E6_SIGNATURE_ALIGNMENT_PASS / EINSTEIN_ACTIVE_SOURCE_PRESSURE_FIREWALL / TOTAL_MATTER_CLOSURE_OPEN`

RF-E4 consumes RF-N1B2L/O and the Einstein coupling/action normalization of RF-E3. RF-E6 aligns its covariant action to the canonical RFC metric signature `(-,+,+,+)` while preserving the physical energy-density and pressure relations.

## 1. Upstream phase action

For

\[
\psi=Ae^{i\vartheta},
\qquad
q_\mu:=D_\mu\vartheta,
\]

the canonical Lorentzian phase action is

\[
\boxed{
\mathcal L_{phase}=-A^2 q_\mu q^\mu-V.
}
\]

Metric variation gives

\[
\boxed{
T_{\mu\nu}^{phase}
=2A^2q_\mu q_\nu+g_{\mu\nu}\mathcal L_{phase}.
}
\]

This uses the same matter action as RF-N1B2L/RF-E6 and introduces one common stress-energy normalization.

## 2. RF-N1B2O normal-flow match

For pure normal phase flow in an orthonormal `(-,+,+,+)` frame,

\[
q_{\hat a}=(r_n,0,0,0).
\]

Define

\[
K:=A^2r_n^2.
\]

Since `q_mu q^mu=-r_n^2`, the phase Lagrangian is `K-V`. Therefore

\[
\boxed{T_{\hat0\hat0}^{phase}=K+V,}
\]

and

\[
\boxed{T_{\hat i\hat j}^{phase}=(K-V)\delta_{ij}.}
\]

For the pure kinetic sector `V=0`,

\[
\boxed{T_{\hat0\hat0}^{phase}=K=\mathcal E_\vartheta,}
\qquad
\boxed{p=K.}
\]

Thus the RF-N1B2O local phase-energy density is recovered exactly.

## 3. Einstein active-source firewall

For an isotropic static weak-field source, the active source combination is

\[
\varepsilon+3p.
\]

For the pure phase-kinetic sector,

\[
\boxed{\varepsilon=K,\qquad p=K,\qquad \varepsilon+3p=4K.}
\]

Hence

\[
\boxed{\rho_{active}^{phase}=4\rho_\vartheta}
\]

on this pure normal phase surface, where `rho_theta=K/c^2`.

## 4. Homogeneous potential/rest completion

With homogeneous `V`,

\[
\boxed{\varepsilon=K+V,\qquad p=K-V,}
\]

so

\[
\boxed{\varepsilon+3p=4K-2V.}
\]

### Pressureless/dust surface

Requiring `p=0` gives

\[
\boxed{V=K,\qquad \varepsilon_{tot}=2K.}
\]

### RF-N1B2O-active-source preservation surface

Requiring the active source to equal `K` gives

\[
4K-2V=K
\]

and therefore

\[
\boxed{V=\frac32K.}
\]

These surfaces remain separately typed downstream.

## 5. Einstein bridge

RF-E3 supplies

\[
G_{\mu\nu}=\kappa_ET_{\mu\nu},
\qquad
\kappa_E=8\pi G/c^4.
\]

The phase source chain is

```text
RF-N1B2L canonical Lorentzian scalar action
 -> RF-N1B2O local phase energy K=A^2 r_n^2
 -> RF-E4 T_mu_nu^phase
 -> pressure/stress contribution
 -> RF-E6 charged-matter/source bookkeeping
 -> total Einstein source
```

## 6. Executable reference

The reference suite verifies:

1. canonical metric signature `(-,+,+,+)`;
2. `T_00=K` for pure normal phase flow;
3. `p_x=p_y=p_z=K`;
4. `epsilon+3p=4K`;
5. with potential, `epsilon=K+V`, `p=K-V`, active source `4K-2V`;
6. dust surface `V=K`;
7. active-source preservation surface `V=3K/2`.

## 7. Advancement

```text
canonical RFC signature (-,+,+,+)                   PASS EXACT
RF-N1B2O phase energy density                       PASS EXACT CONDITIONAL
metric stress tensor from same phase action         PASS EXACT
T_00 = E_theta on normal phase flow                 PASS EXACT
phase-only equation of state p=epsilon              PASS EXACT
phase-only Einstein active density = 4 rho_theta    PRESSURE FIREWALL
homogeneous potential/rest completion               PARAMETRIC EXACT
V=K dust surface                                    EXACT CONDITION
V=3K/2 preserve-K active-source surface             EXACT CONDITION
charged-matter tensor/action bookkeeping            PASS via RF-E6
total matter stress-energy composition              NEXT EINSTEIN FRONTIER
```
