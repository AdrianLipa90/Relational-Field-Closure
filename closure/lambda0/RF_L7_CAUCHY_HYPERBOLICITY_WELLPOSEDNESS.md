# RF-L7 — Cauchy Hyperbolicity and Well-Posedness Gate

Status: `EXACT_LOCAL_PRINCIPAL_HYPERBOLICITY / EXACT_CAUCHY_DATA_MAP / POSITIVE_SLICE_ENERGY_FOR_NONNEGATIVE_MASS / GLOBAL_WELLPOSEDNESS_CONDITIONAL_ON_CAUCHY_FOLIATION / GLOBAL_CAUCHY_PROMOTION_OPEN`

## 1. Purpose

RF-L6 evaluates the RF-L2 information-scalar equation on the full variable-lapse RF-E8 ADM carrier,

\[
(\Box_g-m_I^2)\phi_I=0.
\]

RF-L7 asks the next logically separate question: whether this equation defines a predictive initial-value problem.

The gate has two layers:

1. derive the local hyperbolic principal structure directly from the RF-E8 ADM coefficients;
2. isolate the exact additional global condition required to promote local propagation to a global Cauchy evolution.

No global-causality assumption is hidden inside the local algebra.

## 2. Frozen stacked source lock

```text
TIR main       = 3f5a08ef04ec53c1a155263d23e8b10a96404370
IDT main       = 84ce1886175af872ae4a56ba36f7e106d8e23635
RFC main       = 63418a88d686021c2a6fe6ab159d6152db303c19
RF-L6 head     = e19aeaef978f1bf46e37287759a7a6f67df54eb0
RF-L6 PR       = #89
```

Parent surfaces:

```text
closure/einstein/RF_E8_ADM_KINEMATIC_ASSEMBLY_FIREWALL.md
closure/lambda0/RF_L2_DYNAMIC_LAMBDA0_ACTION_REALIZABILITY_STABILITY.md
closure/lambda0/RF_L6_VARIABLE_LAPSE_CURVED_COVARIANT_PROPAGATION.md
src/rfc/variable_lapse_covariant_scalar.py
validation/RF_L6_VARIABLE_LAPSE_CURVED_COVARIANT_PROPAGATION_V0_1.json
```

External theorem dependency for the global layer:

- C. Bär, N. Ginoux, F. Pfäffle, *Wave Equations on Lorentzian Manifolds and Quantization*, arXiv:0806.1036, especially the global Cauchy theory for normally hyperbolic operators on globally hyperbolic spacetimes.

This external theorem is used only after the RFC geometry has independently satisfied the declared Cauchy-foliation conditions below.

## 3. RF-L6 operator and principal symbol

RF-L6 supplies

\[
\boxed{
P_I\phi_I:=(\Box_g-m_I^2)\phi_I=0.
}
\]

The mass term is zeroth order. Therefore the principal symbol is exactly the metric quadratic form

\[
\boxed{
\sigma_2(P_I)(x,\xi)=g^{\mu\nu}(x)\xi_\mu\xi_\nu.
}
\]

Using the RF-E8 inverse ADM metric,

\[
g^{00}=-\frac1{N_R^2},
\qquad
g^{0i}=\frac{b^i}{N_R^2},
\qquad
g^{ij}=h^{ij}-\frac{b^ib^j}{N_R^2},
\]

write

\[
B:=b^ik_i,
\qquad
Q_h(k):=h^{ij}k_i k_j.
\]

For a covector `xi=(xi_0,k_i)`, the principal symbol becomes

\[
\boxed{
\sigma_2(P_I)
=-\frac{(\xi_0-B)^2}{N_R^2}+Q_h(k).
}
\]

## 4. Exact characteristic roots

The characteristic equation `sigma_2(P_I)=0` gives

\[
(\xi_0-B)^2=N_R^2Q_h(k).
\]

Hence

\[
\boxed{
\xi_0^{\pm}
=B\pm N_R\sqrt{Q_h(k)}.
}
\]

RF-E8 requires

\[
N_R>0
\]

and positive-definite spatial metric `h_ij`, hence positive-definite inverse `h^{ij}`. Therefore for every nonzero spatial covector `k`,

\[
\boxed{Q_h(k)>0.}
\]

The two roots are real and their separation is

\[
\boxed{
\Delta\xi_0
=\xi_0^+-\xi_0^-
=2N_R\sqrt{Q_h(k)}>0.
}
\]

Thus the RF-L6 scalar equation is strictly hyperbolic with respect to the RF-E8 time coordinate at every admitted point for every nonzero spatial covector.

The mass coordinate `m_I^2=alpha_I/kappa_E` does not occur in the principal symbol, so physical mass calibration cannot alter this local hyperbolicity result.

## 5. Characteristic cone and shift transport

The center of the two characteristic roots is

\[
\boxed{
\frac{\xi_0^++\xi_0^-}{2}=b^ik_i,
}
\]

while the half-separation is

\[
\boxed{
\frac{\xi_0^+-\xi_0^-}{2}
=N_R\sqrt{h^{ij}k_i k_j}.
}
\]

The shift therefore advects the characteristic cone without changing its real-root separation. The lapse rescales the normal characteristic opening and the spatial inverse metric supplies its directional norm.

In the local flat calibrated limit,

\[
N_R=1,
\qquad b^i=0,
\qquad h^{ij}=\delta^{ij},
\]

the roots reduce to

\[
\boxed{\xi_0^\pm=\pm|k|,}
\]

which is the standard Klein–Gordon null principal cone in `x^0=ct` coordinates.

## 6. Exact Cauchy data map

The future unit normal used by RF-E8 is

\[
\boxed{
n^\mu=\frac1{N_R}(1,-b^i).
}
\]

Define the normal derivative datum

\[
\boxed{
\pi_I:=n^\mu\nabla_\mu\phi_I
=\frac1{N_R}\left(\partial_0\phi_I-b^i\partial_i\phi_I\right)
=\frac1{N_R}\mathcal D_0\phi_I.
}
\]

Therefore Cauchy data on a spacelike slice `Sigma_s` are

\[
\boxed{
\left(\phi_I|_{\Sigma_s},\pi_I|_{\Sigma_s}\right).
}
\]

The map to the coordinate-time derivative is exactly invertible because `N_R>0`:

\[
\boxed{
\partial_0\phi_I
=N_R\pi_I+b^i\partial_i\phi_I.
}
\]

Thus the relational lapse does not create a local loss of evolution data as long as the RF-E8 positivity gate is maintained.

## 7. Positive instantaneous slice energy

For the Fisher-normalized quadratic sector with

\[
m_I^2\ge0,
\]

define the canonical slice energy density

\[
\boxed{
\mathcal E_{\Sigma}
=\frac12\left[
\pi_I^2
+h^{ij}(D_i\phi_I)(D_j\phi_I)
+m_I^2\phi_I^2
\right].
}
\]

Because `h^{ij}` is positive definite,

\[
\boxed{\mathcal E_{\Sigma}\ge0.}
\]

For `m_I^2>0`, the only pointwise zero of all three terms is the zero Cauchy datum. For `m_I^2=0`, a spatially constant zero-normal-derivative mode has zero local gradient energy, as expected for the massless constant mode.

This positivity supplies the natural instantaneous energy norm for the local Cauchy problem. A uniform global energy estimate additionally requires bounded/regular ADM coefficients on the evolution domain.

## 8. Normally hyperbolic operator classification

`P_I=Box_g-m_I^2` has principal symbol `g^{-1}` and is therefore a normally hyperbolic scalar operator on every smooth Lorentzian RF-E8 spacetime patch.

Consequently the standard global theorem for normally hyperbolic operators applies if the RF-E8 spacetime is promoted to a globally hyperbolic spacetime and the chosen slice is a Cauchy hypersurface.

For smooth compactly supported initial data

\[
\boxed{
\phi_I|_\Sigma=f,
\qquad
n^\mu\nabla_\mu\phi_I|_\Sigma=p,
}
\]

on a smooth spacelike Cauchy hypersurface, the theorem gives a unique smooth global solution with causal/finite propagation and continuous dependence in the standard Cauchy topology.

This is a conditional theorem transfer. RF-L7 does not promote global hyperbolicity merely from local Lorentz signature.

## 9. RFC global Cauchy promotion gate

For the global theorem to become an internal RFC closure result, the following geometric conditions must be certified on the selected RF-E8 development domain:

1. `N_R` remains positive and finite;
2. `h_ij` remains positive definite and nondegenerate;
3. `g_{mu nu}` has sufficient regularity for the selected PDE theorem;
4. the foliation parameter is a global time function on the development domain;
5. each selected `Sigma_s` intersects every inextendible causal curve exactly once, i.e. is a Cauchy hypersurface;
6. if the spatial slices are noncompact or have boundary, asymptotic/boundary conditions are separately specified;
7. coefficient bounds needed for the intended global energy estimate are explicit.

The key unresolved statement is therefore geometric rather than local-PDE:

\[
\boxed{
\text{RF-E8 foliation}\quad\Longrightarrow?\quad
\text{global Cauchy foliation}.
}
\]

RF-L7 converts the previous broad `GLOBAL_WELLPOSEDNESS_OPEN` label into this explicit falsifiable promotion contract.

## 10. Relation to Einstein closure

RF-E12/RF-E13 already supply ADM source constraints, evolution equations and Bianchi constraint propagation for the gravitational sector. RF-L6/RF-L7 supply the corresponding scalar evolution and Cauchy structure on a given admitted RF-E8 geometry.

The coupled Einstein–information-field initial-value problem requires the two systems to share one common Cauchy development and to preserve both:

- the Einstein Hamiltonian/momentum constraints;
- the RF-L7 scalar hyperbolicity and Cauchy regularity conditions.

The coupled nonlinear global stability problem remains downstream.

## 11. Claim ledger

| Statement | Status |
|---|---|
| RF-L6 curved scalar equation | PARENT PASS |
| principal symbol `g^{mu nu} xi_mu xi_nu` | EXACT |
| characteristic roots `B +/- N_R sqrt(Q_h)` | EXACT |
| strict local hyperbolicity for `k!=0` | EXACT GIVEN RF-E8 `N_R>0`, `h>0` |
| mass independence of principal hyperbolicity | EXACT |
| invertible Cauchy normal/coordinate derivative map | EXACT |
| nonnegative instantaneous slice energy for `m_I^2>=0` | EXACT |
| normally hyperbolic operator classification | EXACT |
| global KG Cauchy well-posedness | EXTERNAL THEOREM TRANSFER CONDITIONAL ON GLOBAL HYPERBOLICITY |
| RF-E8 slices are global Cauchy hypersurfaces | OPEN GEOMETRIC PROMOTION GATE |
| coupled nonlinear Einstein-information global stability | OPEN |

## 12. Falsification gates

RF-L7 fails locally if any admitted RF-E8 state yields:

1. `N_R<=0` or nonfinite lapse;
2. a non-positive spatial inverse metric;
3. a nonzero spatial covector with `Q_h(k)<=0`;
4. complex or coincident characteristic roots for `k!=0`;
5. a characteristic root that does not null the principal symbol;
6. a noninvertible Cauchy data map despite positive finite lapse;
7. negative canonical slice energy for `m_I^2>=0`.

The global promotion fails if a selected development contains an inextendible causal curve that misses or intersects a declared Cauchy slice more than once, or if the coefficient/regularity assumptions of the invoked global theorem fail.

Validation target:

`PASS_RF_L7_LOCAL_CAUCHY_HYPERBOLICITY_CONTRACT`.
