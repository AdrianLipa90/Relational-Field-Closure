# RF-S12 — Tetrahedral Role-Permutation Source-Binding Reduction

Status: `EXACT_S4_ROLE_AMBIGUITY / ORIENTED_A4_REDUCTION / EXECUTABLE_SOURCE_SIGNATURE_ASSIGNMENT / PHYSICAL_ROLE_SIGNATURE_DATA_OPEN`

RF-S12 is stacked on exact-green RF-S11. It consumes the TIR tetrahedral congruence-class closure together with the RF-S11 full tetrahedral projective scope.

TIR source pinned for this gate:

`AdrianLipa90/The-Fundamental-Theory-of-Informational-Relations@ccc89fc06bdf42c1937c0a2303d3e477db487e0f`

Source theorem:
`TIR/integration/TIR_TETRAHEDRAL_CONGRUENCE_CLASS_CLOSURE_V0_1.md`.

RF-S12 isolates the residual source-role coordinate after the spatial minimal-isotropy tetrahedron and the SIC minimal-informationally-complete tetrahedron have already been placed in one exact Gram/congruence class.

## 1. Exact common tetrahedral class

Let

\[
N=(\mathbf n_1\;\mathbf n_2\;\mathbf n_3\;\mathbf n_4)
\]

be an ordered spatial tetrahedral frame and

\[
M=(\mathbf m_1\;\mathbf m_2\;\mathbf m_3\;\mathbf m_4)
\]

an ordered SIC tetrahedral frame in the common carrier

\[
\operatorname{Herm}_0(2)\simeq\mathbb R^3.
\]

TIR gives

\[
\boxed{
N^TN=M^TM
=G
=\frac43I_4-\frac13\mathbf1\mathbf1^T,
}
\]

and

\[
\boxed{NN^T=MM^T=\frac43I_3.}
\]

Hence both ordered frames span rank three and belong to one regular-tetrahedral orthogonal congruence class.

## 2. Permutation family of exact congruences

Let `sigma` be any permutation of the four SIC role labels,

\[
\sigma\in S_4.
\]

Write

\[
M_\sigma
=(\mathbf m_{\sigma(1)}\;\mathbf m_{\sigma(2)}\;\mathbf m_{\sigma(3)}\;\mathbf m_{\sigma(4)}).
\]

The tetrahedral Gram matrix is invariant under every permutation because all diagonal entries are `1` and all off-diagonal entries are `-1/3`. Therefore

\[
\boxed{M_\sigma^TM_\sigma=G}
\]

for every `sigma`.

Define

\[
\boxed{
Q_\sigma:=\frac34M_\sigma N^T.
}
\]

Exactly as in the TIR congruence theorem,

\[
\boxed{Q_\sigma N=M_\sigma}
\]

and

\[
\boxed{Q_\sigma Q_\sigma^T=I_3.}
\]

Thus

\[
\boxed{Q_\sigma\in O(3)}
\]

for all `24` permutations.

The common Gram/shape data therefore leave a finite residual role coordinate

\[
\boxed{\sigma\in S_4.}
\]

All orthogonal shape invariants already used by RF-S1/RF-S6/RF-S10 are shared across this family.

## 3. Orientation refinement

Choose compatible orientations of the ordered reference frames so that the identity role ordering has

\[
\det Q_{id}=+1.
\]

An odd permutation reverses the oriented tetrahedral volume and an even permutation preserves it. Therefore

\[
\boxed{
\det Q_\sigma=\operatorname{sgn}(\sigma).
}
\]

Consequently an orientation-preserving source ledger restricts the role candidates to

\[
\boxed{\sigma\in A_4,}
\]

with

\[
\boxed{|A_4|=12.}
\]

The unoriented candidate set has `24` elements; the oriented candidate set has `12`.

## 4. Typed source signatures

Let each spatial role carry an independently sourced typed signature

\[
\mathbf s_a\in\mathbb R^d,
\qquad a=1,\ldots,4,
\]

and each SIC role carry a signature of the same admitted type

\[
\mathbf q_b\in\mathbb R^d,
\qquad b=1,\ldots,4.
\]

The signature coordinate can contain any downstream quantity that is independently available for both role ledgers, for example a conserved-source tag, orientation-sensitive coupling coordinate, phase/holonomy tag, or another typed observable selected by the physical model.

For a candidate permutation define the exact assignment defect

\[
\boxed{
D_{role}(\sigma)
:=
\left[
\sum_{a=1}^4
\|\mathbf s_a-\mathbf q_{\sigma(a)}\|_2^2
\right]^{1/2}.
}
\]

Then

\[
\boxed{D_{role}(\sigma)=0}
\]

means that the two independently supplied role ledgers match exactly under `sigma`.

## 5. Unique zero-defect promotion rule

Let `C` denote the admitted candidate set:

\[
C=S_4
\]

for an unoriented ledger, or

\[
C=A_4
\]

for an orientation-preserving ledger.

Define

\[
Z:=\{\sigma\in C:D_{role}(\sigma)=0\}.
\]

RF-S12's deterministic source-binding rule is

\[
\boxed{|Z|=1.}
\]

When this condition holds, the unique member

\[
\boxed{\sigma_\star\in Z}
\]

is the selected role map.

The other possible outcomes remain explicitly typed:

```text
|Z| = 0    source signatures disagree on every admitted role map
|Z| = 1    unique exact role assignment
|Z| > 1    residual discrete symmetry remains in the supplied signatures
```

For finite-precision data the executable gate uses a supplied tolerance and retains the same uniqueness requirement among candidates inside that tolerance.

## 6. Residual symmetry diagnostic

If all four role signatures are identical within one ledger and compatible with the other ledger, every candidate permutation carries the same defect. The resulting multiplicity records unresolved source symmetry rather than selecting an arbitrary label map.

More generally define the best-defect multiplicity

\[
\boxed{
\nu_{min}
:=
\#\{\sigma\in C:
D_{role}(\sigma)=\min_{\rho\in C}D_{role}(\rho)\}.
}
\]

A unique role map requires

\[
\boxed{\nu_{min}=1}
\]

together with an admitted zero/tolerance criterion.

This exposes the exact amount of discrete source information still required after the geometric congruence theorem.

## 7. RF-S11 / IDT consequence

RF-S11 selects the full four-outcome tetrahedral projective carrier on the minimal-IC qubit branch. RF-S12 therefore assigns source roles across exactly four SIC outcomes and four spatial adjacency directions.

Once a physical source ledger supplies a unique `sigma_star`, the already-derived projective information-area branch

\[
a_{FS}^{IC}=\pi,
\qquad
\mathcal A_{IC}=\frac{\pi c^2}{\omega^2}
\]

can carry that role correspondence without altering its Gram/area normalization.

The role assignment acts on the four tetrahedral labels; the tetrahedral projective area and orthogonal shape invariants remain permutation-invariant.

## 8. Promotion ledger

```text
TIR common tetrahedral Gram class                       PASS EXACT
TIR explicit orthogonal congruence                     PASS EXACT
all 24 role permutations give O(3) congruences         PASS EXACT
compatible orientation reduces candidates to A4        PASS EXACT
unoriented candidate count = 24                        PASS EXACT
oriented candidate count = 12                          PASS EXACT
source-signature assignment defect                     PASS EXACT DEFINITION
unique zero-defect permutation rule                    PASS DETERMINISTIC
RF-S11 four-outcome full tetra scope                    PASS EXACT PARENT
physical role signatures                               OPEN INPUT
unique physical role map                               OPEN UNTIL SOURCE RECEIPT
```

Remaining gates after RF-S12:

```text
PHYSICAL_TETRA_ROLE_SIGNATURE_RECEIPT
PHYSICAL_MINIMAL_IC_CARRIER_SELECTION
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

Reference implementation: `src/rfc/tetra_role_permutation_source_binding.py`.
Reference tests: `tests/reference/test_rfs12_tetra_role_permutation_source_binding.py`.
Validation receipt: `validation/RF_S12_TETRA_ROLE_PERMUTATION_SOURCE_BINDING_V0_1.json`.

Stack parent: RF-S11 exact-green head `1822db1a805ca9b67fdbd25df192beff1a3983c5`.
