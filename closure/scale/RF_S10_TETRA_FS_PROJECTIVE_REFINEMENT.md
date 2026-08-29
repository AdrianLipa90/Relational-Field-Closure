# RF-S10 — Tetrahedral Fubini–Study Projective Refinement

Status: `EXACT_TETRA_FS_REFINEMENT / DISCRETE_PROJECTIVE_SCOPE_REDUCTION / IDT_01K_AREA_SPECIALIZATION / PHYSICAL_SCOPE_SELECTION_OPEN`

RF-S10 is stacked on RF-S9. It consumes the exact projective geometry exported by TIR's tetrahedral Fubini–Study crosswalk and the IDT 01K phase-clock area map.

TIR source pinned for this gate:

`AdrianLipa90/The-Fundamental-Theory-of-Informational-Relations@ccc89fc06bdf42c1937c0a2303d3e477db487e0f`

Source theorem:
`TIR/integration/TIR_TETRA_FS_SPATIAL_SHAPE_CROSSWALK_V0_1.md`.

The TIR spatial-adjacency promotion remains separately typed. RF-S10 uses the projective `CP1` area identities.

## 1. Exact tetrahedral FS areas

For the four regular tetrahedral Bloch directions,

\[
\mathbf n_a\cdot\mathbf n_b=-\frac13\qquad(a\ne b).
\]

TIR derives the geodesic spherical-face angle and the qubit Fubini–Study scale

\[
ds_{FS}^2=\frac14 ds_{S^2}^2.
\]

One tetrahedral geodesic face therefore carries

\[
\boxed{a_{FS}^{face}=\frac\pi4.}
\]

The four congruent faces cover the full projective qubit sphere and give

\[
\boxed{a_{FS}^{tet}=4a_{FS}^{face}=\pi.}
\]

Thus the tetrahedral branch admits two canonical scope coordinates:

```text
FACE             a_FS = pi/4
FULL_TETRA_CP1   a_FS = pi
```

The continuous projective shape-area coordinate is therefore reduced to a discrete scope selector once the tetrahedral projective carrier is admitted.

## 2. IDT 01K constant-rate specialization

IDT 01K gives, for a projective cell with constant nonzero calibrated phase-rate magnitude `omega`,

\[
\mathcal A_{rel}=\frac{c^2}{\omega^2}a_{FS}.
\]

Hence the tetrahedral scopes give

\[
\boxed{
\mathcal A_{face}
=\frac{\pi c^2}{4\omega^2},
}
\]

and

\[
\boxed{
\mathcal A_{tet}
=\frac{\pi c^2}{\omega^2}.
}
\]

Therefore, for one common phase-rate carrier,

\[
\boxed{
\mathcal A_{tet}=4\mathcal A_{face}.
}
\]

Define the refinement ratio

\[
\boxed{R_{4}:=\frac{\mathcal A_{tet}}{\mathcal A_{face}}=4.}
\]

## 3. Information-curvature specialization

For a supplied natural-log information numerator `J>=0`, 01K gives

\[
\Xi=\frac{\mathcal J}{\mathcal A_{rel}}.
\]

Thus at fixed `J` and common `omega`,

\[
\boxed{
\Xi_{face}
=\frac{4\mathcal J}{\pi}
\left(\frac{\omega}{c}\right)^2,
}
\]

and

\[
\boxed{
\Xi_{tet}
=\frac{\mathcal J}{\pi}
\left(\frac{\omega}{c}\right)^2.
}
\]

Consequently

\[
\boxed{
\Xi_{face}=4\Xi_{tet}
}
\]

when the same information numerator is compared across the two scopes. RF-S10 treats the numerator as an independent supplied coordinate; physical scope-dependent information assignment remains a separate data choice.

## 4. Four-face refinement identity

Let the four tetrahedral projective faces be indexed by

\[
f\in\{1,2,3,4\}.
\]

Their dimensionless FS areas satisfy

\[
\boxed{
a_{FS}^{(f)}=\frac\pi4,}
\]

so

\[
\boxed{
\sum_{f=1}^4a_{FS}^{(f)}=\pi=a_{FS}^{tet}.
}
\]

For one common constant phase-rate magnitude,

\[
\boxed{
\sum_{f=1}^4\mathcal A_f
=\mathcal A_{tet}.
}
\]

Define a normalized refinement defect

\[
\boxed{
\Delta_{4}
:=
\frac{|\mathcal A_{tet}-\sum_f\mathcal A_f|}
{\mathcal A_{tet}+\sum_f\mathcal A_f}.
}
\]

On the exact tetrahedral refinement,

\[
\boxed{\Delta_4=0.}
\]

## 5. Nonuniform phase-rate refinement

IDT 01K gives the nonuniform cell area

\[
\mathcal A_{rel}^{(P)}
=\int_P\frac{c^2}{\omega_t(x)^2}\,da_{FS}(x).
\]

Partition the full tetrahedral `CP1` projective carrier into its four geodesic faces `P_f`. Additivity of the integral gives exactly

\[
\boxed{
\mathcal A_{tet}
=\sum_{f=1}^4
\int_{P_f}\frac{c^2}{\omega_t(x)^2}\,da_{FS}(x)
=\sum_{f=1}^4\mathcal A_f.
}
\]

The stronger relation

\[
\mathcal A_{tet}=4\mathcal A_{face}
\]

requires equal face-area contributions, for example one phase-rate magnitude shared uniformly across the congruent faces. RF-S10 carries exact additivity and the uniform-face specialization as separately typed relations.

## 6. RF-S9 ownership consequence

RF-S9 requires a source-owned `a_FS` carrier for its same-cell relational-area identity. On the admitted tetrahedral projective branch, RF-S10 supplies the canonical values

\[
\boxed{
a_{FS}\in\left\{\frac\pi4,\pi\right\}}
\]

with the scope label carried explicitly.

The RF-S9 tetrahedral source ledger is therefore parameterized by:

```text
projective carrier ID
scope = FACE or FULL_TETRA_CP1
face ID 1..4 when scope=FACE
phase-clock carrier ID
calibrated phase rate
```

The physical selection of which scope is realized in a target measurement remains a separate promotion gate.

## 7. Type firewall

RF-S10 consumes the TIR projective geometry theorem. The spatial tetrahedral carrier and projective tetrahedral carrier remain separately typed until their dedicated source-binding gate is admitted.

The exact RF-S10 advancement is therefore:

```text
TIR projective tetrahedron -> canonical FS face/full areas
canonical FS scope -> IDT 01K relational area
four-face refinement -> exact area additivity
```

The later TIR/RFC spatial-cell source binding remains downstream.

## 8. Promotion ledger

```text
TIR a_FS^face = pi/4                              PASS EXACT
TIR a_FS^tet = pi                                 PASS EXACT
four-face a_FS refinement pi = 4(pi/4)            PASS EXACT
IDT 01K constant-rate area specialization          PASS EXACT
A_tet = 4 A_face on common uniform rate            PASS EXACT
nonuniform full area = sum of four face integrals  PASS EXACT
RF-S9 tetrahedral a_FS continuous freedom           REDUCED TO DISCRETE SCOPE
```

Remaining gates:

```text
PHYSICAL_PROJECTIVE_SCOPE_SELECTION
PHYSICAL_PROJECTIVE_CELL_SELECTION
TIR_PROJECTIVE_TO_SPATIAL_CELL_SOURCE_BINDING
PHYSICAL_JOINT_INFORMATION_STATE_BINDING
ABSOLUTE_ALPHA_NORMALIZATION
PHYSICAL_RADIAL_ZERO_DEFECT_DATA
RADIAL_BINDING_DYNAMICAL_TRANSPORT
TRANSLATIONAL_OBSERVABLE
DIRECTIONAL_CUBIC_TEST
GENERAL_MATTER_MULTIPLET
GLOBAL_INFORMATION_GEODESIC_EXTENSION
```

## 9. Validation authority

Reference implementation: `src/rfc/tetra_fs_projective_refinement.py`.
Reference tests: `tests/reference/test_rfs10_tetra_fs_projective_refinement.py`.
Validation receipt: `validation/RF_S10_TETRA_FS_PROJECTIVE_REFINEMENT_V0_1.json`.

Stack parent: RF-S9 head `b0b0b51336aadc8a0664b907170e0eb050964808`.
