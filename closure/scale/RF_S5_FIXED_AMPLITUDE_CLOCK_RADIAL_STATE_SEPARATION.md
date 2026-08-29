# RF-S5 — Fixed-Amplitude Clock / Radial State-Separation Firewall

Status: `EXACT_FIXED_AMPLITUDE_STATE_SEPARATION / NOETHER_AMPLITUDE_RECONSTRUCTION_PASS / POINTWISE_CLOCK_RADIAL_CROSSING_TEST / CLOCK_ALPHA_BINDING_REMAINS_SEPARATE`

RF-S5 follows RF-S4 and RF-I1. Its purpose is to distinguish the radial information-curvature coordinate carried by the locally Fisher-normalized matter amplitude from the directional phase-rate information curvature carried by the RF-E16/RF-I1 clock branch.

Both coordinates have dimension `L^-2`, while their state dependence is independently auditable.

## 1. Radial information coordinate

RF-S4 supplies the local radial source-binding surface

\[
\boxed{
\bar\Xi_{rad}=A^2,
}
\]

where `A>=0` is the amplitude of the selected RFC complex scalar and

\[
\bar\Xi_{rad}:=\Xi_I-\Xi_\star.
\]

On the RF-E16 fixed-amplitude directional specialization,

\[
\boxed{D_b A=0,}
\]

so

\[
\boxed{D_b\bar\Xi_{rad}=0.}
\]

For the local branch considered below take nondegenerate radial support

\[
A>0.
\]

## 2. Directional clock information coordinate

RF-E16 supplies positive phase rates

\[
\boxed{
r_s=r_0(1-sb),
\qquad s\in\{+1,-1\},
\qquad |b|<1,
}
\]

and

\[
\boxed{x_s=\frac{r_0}{r_s}=\frac1{1-sb}.}
\]

RF-I1 supplies the Shannon phase-rate information curvature

\[
\boxed{
\Xi_{phase}^{(s)}(b)
=\frac{\Phi(x_s)}{\mathcal A_{rel}},
\qquad
\Phi(x)=x-1-\ln x,
}
\]

for an admitted positive relational area.

On the constant reference phase-clock cell used by RF-I1,

\[
\mathcal A_{rel}
=\frac{c^2}{r_0^2}a_{FS},
\]

so the area is fixed by the reference rate `r_0` while the directional branch is parameterized by `b`.

## 3. Reference-point state separation

At

\[
b=0,
\]

one has

\[
x_s=1,
\qquad
\Phi(1)=0,
\]

and therefore

\[
\boxed{
\Xi_{phase}^{(s)}(0)=0.
}
\]

The nondegenerate RF-S4 radial coordinate is

\[
\boxed{
\bar\Xi_{rad}(0)=A^2>0.
}
\]

Hence the two state coordinates are separated already at the reference point:

\[
\boxed{
\bar\Xi_{rad}(0)-\Xi_{phase}^{(s)}(0)=A^2>0.
}
\]

This is an exact branch statement from the promoted parent definitions.

## 4. Differential state separation

RF-E14/RF-E16 gives the local expansion

\[
\Phi(x_s)
=\frac12b^2
+s\frac23b^3
+\frac34b^4
+O(b^5).
\]

Therefore

\[
\boxed{
\left.\frac{d\Xi_{phase}^{(s)}}{db}\right|_{b=0}=0,
}
\]

and

\[
\boxed{
\left.\frac{d^2\Xi_{phase}^{(s)}}{db^2}\right|_{b=0}
=\frac1{\mathcal A_{rel}}>0.
}
\]

For the fixed-amplitude radial coordinate,

\[
\boxed{
\frac{d\bar\Xi_{rad}}{db}=0,
\qquad
\frac{d^2\bar\Xi_{rad}}{db^2}=0.
}
\]

Thus the clock and radial coordinates have different local response tensors with respect to the directional deformation parameter `b`.

## 5. Noether reconstruction of the radial amplitude

RF-E16/RF-N1B2O supplies the positive-carrier phase current density

\[
\boxed{
j_\vartheta=2A^2r_s.}
\]

For

\[
r_s>0,
\qquad
j_\vartheta>0,
\]

the amplitude is reconstructed exactly as

\[
\boxed{
A^2=\frac{j_\vartheta}{2r_s}.
}
\]

On the RF-S4 radial source-binding surface,

\[
\boxed{
\bar\Xi_{rad}
=\frac{j_\vartheta}{2r_s}.
}
\]

The radial coordinate can therefore be evaluated independently from the phase-current/rate ledger.

## 6. Executable clock/radial ratio

Define the dimensionless pointwise clock-to-radial ratio

\[
\boxed{
\chi_{CR}^{(s)}
:=\frac{\Xi_{phase}^{(s)}}{\bar\Xi_{rad}}.
}
\]

Using the Noether reconstruction,

\[
\boxed{
\chi_{CR}^{(s)}
=\frac{2r_s\Phi(x_s)}
{\mathcal A_{rel}j_\vartheta}.
}
\]

On the reference surface,

\[
\boxed{\chi_{CR}^{(s)}(0)=0.}
\]

A pointwise crossing of the two scalar coordinates is the measurable condition

\[
\boxed{
\chi_{CR}^{(s)}=1
}
\]

or equivalently

\[
\boxed{
\mathcal A_{rel}j_\vartheta
=2r_s\Phi(x_s).
}
\]

Such a crossing is a pointwise state condition. The promoted branch dependence remains encoded in `chi_CR(b)`.

## 7. State-separation defect

Define

\[
\boxed{
\Delta_{CR}^{(s)}
:=
\frac{
\left|
\bar\Xi_{rad}-\Xi_{phase}^{(s)}
\right|
}
{
\bar\Xi_{rad}+\Xi_{phase}^{(s)}
}
}
\]

for positive denominator.

With the Noether reconstruction,

\[
\boxed{
\Delta_{CR}^{(s)}
=
\frac{
\left|
\frac{j_\vartheta}{2r_s}
-rac{\Phi(x_s)}{\mathcal A_{rel}}
\right|
}
{
\frac{j_\vartheta}{2r_s}
+rac{\Phi(x_s)}{\mathcal A_{rel}}
}.
}
\]

At `b=0` and `A>0`,

\[
\boxed{\Delta_{CR}^{(s)}=1.}
\]

At a pointwise crossing,

\[
\boxed{\Delta_{CR}^{(s)}=0.}
\]

This gives a direct executable discriminator between the radial and directional clock state coordinates.

## 8. Coupling ledger consequence

RF-L3 assigns the coefficient `alpha_I` to the admitted information scalar lineage. RF-I1 retains `alpha_clk` for the directional clock source while its state-level relation to the radial coordinate is audited separately.

RF-S5 establishes that, on the fixed-amplitude directional branch, the radial and clock coordinates carry distinct reference values and distinct second-order directional response.

Therefore the coupling ledger remains typed as

```text
radial information coordinate      barXi_rad       -> alpha_I
clock directional coordinate       Xi_phase^(s)    -> alpha_clk
clock/radial state composition     separate gate
```

A future action-composition theorem may bind these coefficients after supplying a state-level composition law. RF-S5 supplies the state discriminator required by that theorem.

## 9. Consequence for RF-S1/RF-S4 scale closure

RF-S4 may source-bind the matter radial amplitude to the locally Fisher-normalized information curvature and thereby force

\[
m_\Psi=m_I
\]

on its zero-defect action-reclassification surface.

RF-S5 keeps the directional clock scalar separately measurable. Hence RF-S1/RF-S3 retains

\[
\boxed{
r_\alpha:=\frac{\alpha_{clk}}{\alpha_I}}
\]

as the remaining coupling coordinate after the RF-S4 mass/spectral reduction.

On the RF-S4 mass-bound same-target surface,

\[
\boxed{
r_\alpha\zeta_s^3
=\frac1{C_{\Delta/FS}}
=\frac{9\sqrt3\pi}{8}.
}
\]

The next scale question is therefore cleanly isolated to the clock/radial action-composition coefficient and the spatial coordinate `zeta_s`.

## 10. Promotion ledger

Promoted parents:

```text
RF-E16 fixed-amplitude directional phase carrier      PASS
RF-E16 j_vartheta=2 A^2 r_s                           PASS
RF-I1 Xi_phase=Phi(r_0/r_s)/A_rel                     PASS
RF-S4 radial coordinate barXi_rad=A^2                 CONDITIONAL SOURCE-BINDING SURFACE
```

RF-S5 exact outputs on the declared branch:

```text
Xi_phase(0)=0                                          PASS EXACT
barXi_rad(0)=A^2>0                                    PASS GIVEN NONDEGENERATE RADIAL SUPPORT
clock directional curvature d2Xi_phase/db2=1/A_rel    PASS EXACT
radial directional curvature d2barXi/db2=0            PASS FIXED-AMPLITUDE BRANCH
A^2=j_vartheta/(2r_s)                                 PASS EXACT
chi_CR=2r_s Phi/(A_rel j_vartheta)                    PASS EXACT
Delta_CR reference value = 1                          PASS EXACT
pointwise crossing condition                           PASS EXACT
```

Remaining physical gates:

```text
RADIAL_INFORMATION_SOURCE_BINDING
CLOCK_RADIAL_ACTION_COMPOSITION
CLOCK_ALPHA_BINDING
TIR_CONTINUUM_COORDINATE_BIND
TRANSLATIONAL_OBSERVABLE
DIRECTIONAL_CUBIC_TEST
GENERAL_MATTER_MULTIPLET
```

## 11. Validation authority

Reference implementation: `src/rfc/fixed_amplitude_clock_radial_state_separation.py`.
Reference tests: `tests/reference/test_rfs5_fixed_amplitude_clock_radial_state_separation.py`.
Validation receipt: `validation/RF_S5_FIXED_AMPLITUDE_CLOCK_RADIAL_STATE_SEPARATION_V0_1.json`.

Parent RFC main at branch creation: `d9280129c8fa4300e5360265e06ed5451c2c3055`.
