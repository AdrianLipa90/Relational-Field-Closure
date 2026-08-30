# RF-E22 — TIR Cartan / Levi-Civita Cross-Repository Binding

Status: `TIR_CARTAN_REFINEMENT_BOUND / LOCAL_LEVI_CIVITA_SPATIAL_GR_PASS / GLOBAL_REFINEMENT_EXISTENCE_OPEN / RF_E21_SECOND_ORDER_SELECTION_FRONTIER`

Date: 2026-08-30

## 1. Purpose

RF-E22 consumes the source-owned TIR spatial-GR gates produced after RF-E21 was first written. It updates only the project-premise ledger of the Einstein-form selection programme. It does not replace the RF-E21 Lovelock theorem statement and it does not import an Einstein-Hilbert action as a premise.

Pinned TIR validation surface:

```text
repository: AdrianLipa90/The-Fundamental-Theory-of-Informational-Relations
branch:     feat/tir-cartan-refinement-v0.1
PR:         #110 (draft)
exact head: 59b820e74c3b7be0e4cd81aa95ec0a23184e4f24
```

Hosted gates on that exact head:

```text
TIR Cartan refinement curvature-torsion gate   SUCCESS
TIR spatial GR Levi-Civita gate                SUCCESS
```

## 2. Gate A2 consumed by RFC

TIR Gate A2 establishes, for a regular shrinking relational triangle family, the separation

\[
\boxed{
\frac{\operatorname{vec}(\mathcal T_\triangle)}{A_\triangle}
\longrightarrow T^a(u,v)
}
\]

and

\[
\boxed{
\frac{R_C-I}{A_\triangle}
\longrightarrow \Omega(u,v).
}
\]

The exact finite-loop relation is

\[
\boxed{
\mathbf t_C
=\operatorname{vec}(\mathcal T_\triangle)
+(I-R_C)\mathbf e_{xz}.
}
\]

For edge scale `epsilon`, the regular refinement has

\[
\mathbf e_{xz}=O(\epsilon),
\qquad
R_C-I=O(\epsilon^2),
\qquad
A_\triangle=\Theta(\epsilon^2),
\]

so curvature contamination of the translational loop is only `O(epsilon^3)`. Therefore the torsion and curvature continuum coefficients are independently identifiable at leading area order.

RFC consumes this as:

`TIR_DISCRETE_TO_CARTAN_REFINEMENT = PASS_CONDITIONAL_ON_REGULAR_REFINING_FAMILY`.

## 3. Gate A3 consumed by RFC

The TIR affine-torsor parent gives a unique intrinsic primitive endpoint displacement. On the same-primitive-endpoint sector, direct and connection-composed endpoint descriptions are required to represent the same intrinsic displacement. Hence

\[
\mathcal C_{xyz}=0,
\qquad
\mathcal T_{xyz}=-\mathcal C_{xyz}=0.
\]

Gate A2 transfers this into the continuum limit:

\[
\boxed{T^a=0.}
\]

The spatial relation transport is induced through

\[
SU(2)\xrightarrow{\mathrm{Ad}}SO(3),
\]

and therefore preserves the Hilbert--Schmidt / Euclidean spatial metric:

\[
\boxed{Dh=0.}
\]

The fundamental theorem of Riemannian geometry then selects the unique spatial connection

\[
\boxed{D=D^{LC}.}
\]

TIR independently verifies the firewall

\[
\boxed{T^a=0\quad\text{with}\quad\Omega^a{}_b\ne0}
\]

as an admitted refinement regime. Thus the zero-torsion GR sector does not collapse curvature.

RFC consumes this as:

`TIR_LOCAL_LEVI_CIVITA_SPATIAL_GR_SECTOR = PASS`.

## 4. Global refinement firewall

TIR Gate A3 keeps one source-owned geometry question open:

\[
\boxed{
\text{global existence and stability of a smooth compatible refinement over the full relational complex}
}
\]

Therefore RF-E22 splits the earlier RF-E21 geometry premise:

```text
local regular Cartan refinement                  PASS
local zero-torsion metric-compatible sector      PASS
local Levi-Civita uniqueness                     PASS
global smooth refinement existence/stability     OPEN
```

No global theorem is promoted from local certificates.

## 5. Four-dimensional naturality update

RFC already possesses a coordinate-free Lorentzian carrier through RF-G0:

\[
\boxed{g=-\Theta\otimes\Theta+h_\perp}
\]

with the exact signature theorem

\[
\operatorname{signature}(g)=(-,+,+,+).
\]

On the TIR Gate-A3 spatial sector, the spatial connection is Levi-Civita. RF-E8 then gives the equivalent ADM decomposition of the same Lorentzian metric using the IDT lapse and typed shift.

Once a smooth four-dimensional metric carrier is admitted, the Levi-Civita connection, Riemann tensor, Ricci tensor, scalar curvature and Einstein tensor are standard natural tensor constructions. This supports the local covariance/naturality side of RF-E21 without taking the Einstein field equation as input.

The remaining cross-repository global issue is the same global smooth-refinement / gluing existence gate above.

## 6. Divergence-free update

For the Levi-Civita connection, the contracted Bianchi identity is exact:

\[
\boxed{\nabla^\mu G_{\mu\nu}=0.}
\]

RF-E13 already uses this identity together with the source-conservation ledger to prove homogeneous propagation of the ADM constraint residuals. Thus divergence-freedom of the Einstein candidate tensor is established after the geometric selection.

RF-E22 keeps distinct the stronger selection question:

```text
Einstein tensor is divergence-free                     EXACT
why the admissible unknown gravitational operator must be divergence-free
                                                       SELECTION PREMISE / TO BE BOUND
```

This prevents Bianchi from being used circularly as an assumption that already names the Einstein tensor.

## 7. Remaining Einstein-form frontier

After TIR A2/A3, RF-E21 no longer has a local Cartan/Levi-Civita blocker. The shortest current dependency line is

```text
TIR primitive relation
 -> Cartan refinement                                  PASS
 -> zero torsion + metric compatibility                PASS
 -> local spatial Levi-Civita geometry                 PASS
 + IDT temporal orientation / lapse                    PASS LOCAL CARRIER
 -> RFC Lorentzian / ADM metric carrier                PASS
 -> natural metric curvature tensors                   STANDARD EXACT
 -> RF-E21 4D uniqueness theorem                       PASS ON THEOREM PREMISES
```

The active promotion gates are now:

1. `GLOBAL_SMOOTH_REFINEMENT_EXISTENCE_STABILITY`;
2. `SECOND_ORDER_LOCAL_METRIC_DYNAMICS_SELECTION` — exclude independent higher-derivative curvature operators such as `nabla R`, `R^2` dynamics as fundamental carriers rather than merely low-energy corrections;
3. `DIVERGENCE_FREE_OPERATOR_SELECTION_BINDING` — derive why the gravitational side belongs to the covariantly conserved natural-tensor class before naming `G_mn`;
4. absolute/project physical promotion of `kappa_E=8 pi G/c^4`, already tracked separately by RF-E3.

The Hojman--Kuchar--Teitelboim route remains an independent future cross-check: deriving the hypersurface-deformation algebra from project-owned canonical variables would select the ADM/GR dynamics without using the Lovelock premise set.

## 8. Advancement

```text
TIR Cartan refinement exact-head hosted receipt         PASS
TIR zero-torsion local GR sector                        PASS
TIR local Levi-Civita selection                         PASS
zero-torsion/nonzero-curvature firewall                 PASS
RFC local Lorentzian metric carrier                     PASS
RFC ADM kinematics                                      PASS
RFC contracted Bianchi / constraint propagation         PASS
RF-E21 Lovelock theorem selection                       PASS ON DECLARED PREMISES
global smooth TIR refinement                            OPEN
second-order/local metric dynamics selection            OPEN
pre-Einstein divergence-free operator binding           OPEN
absolute physical G/kappa_E promotion                   OPEN SEPARATE COUPLING LINE
```

RF-E22 therefore advances the project from `LOCAL_GEOMETRY_PREMISE_OPEN` to `LOCAL_GEOMETRY_PREMISE_BOUND`; it does not promote the remaining global/dynamical selection premises by implication.
