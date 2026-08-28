# RFG31 — Internal-State Tree-Factorization / Pure-Spin-2 Firewall

Status: `MATCHED_HELICITY_INTERNAL_SEED_TRANSVERSE_NULL_PASS / INTERNAL_THREE_POINT_TENSOR_SYMMETRIC_TRACELESS_PASS / TRACE_AND_ANTISYMMETRIC_RESIDUES_ZERO_PASS / CHANNEL_GAUGE_INVARIANCE_PASS / MIXED_COPY_CONTROL_ACTIVATES_ADDITIONAL_TENSOR_COORDINATES / GRAPH_RESIDUE_PURE_SPIN2_PASS`

Scope: `FIVE_POINT_MHV_S12_TREE_FACTORIZATION / MATCHED_COPY_HELICITY_BRANCH`.

RFG31 consumes the current-level factorization of RFG29 and the explicit graph double copy of RFG30. It audits the internal tensor-product state selected on the non-soft `s12` factorization channel when the two Yang–Mills copies carry matching helicities corresponding to the RFG18/RFG19 pure-spin-2 external branch.

## 1. Three-point channel seed

Let `P=P12` and let `N_L`, `N_R` be the two Yang–Mills cubic residue currents on the left side of the factorization channel. On the matching-helicity branch the executable gate finds the same physical seed in both copies,

\[
N_L=N_R=N,
\]

with

\[
\boxed{P\cdot N=0},\qquad
\boxed{N^2=0}.
\]

Thus the tensor-product three-point channel state

\[
\boxed{T_3^{\mu\nu}=N^\mu N^\nu}
\]

is transverse, symmetric and traceless modulo the standard null-momentum gauge equivalence.

## 2. Downstream currents and full residue

The KLT ordering uses distinct downstream currents on the two copies,

\[
J_L=J_{(12)|345},\qquad
J_R=\widetilde J_{(12)|354}.
\]

RFG29 gives

\[
R_L=N\cdot J_L,\qquad R_R=N\cdot J_R,
\]

so the tensor-product residue core is

\[
\boxed{T_3:T_4=(N\cdot J_L)(N\cdot J_R)=R_LR_R},
\]

where

\[
T_4^{\alpha\beta}=J_L^\alpha J_R^\beta.
\]

## 3. Spin-2 projector decomposition

In the two-dimensional physical transverse space, decompose the internal rank-two state into symmetric-traceless, antisymmetric and trace coordinates. The trace contribution to the contraction is

\[
\mathcal R_{tr}=\frac12\,\operatorname{tr}(T_3)\operatorname{tr}(T_4)
=\frac12(N^2)(J_L\cdot J_R)=0.
\]

The antisymmetric contribution vanishes because

\[
T_3^{[\mu\nu]}=0.
\]

Therefore

\[
\boxed{
T_3:T_4=(T_3)_{ST}:(T_4)_{ST}
}
\]

and the selected internal residue is carried by the symmetric-traceless spin-2 coordinate.

## 4. Channel gauge invariance

For gauge shifts along the null channel momentum,

\[
N\to N+aP,\qquad J\to J+bP,
\]

with `P^2=P dot N=P dot J=0`, the null norm and residue contraction are invariant. The executable gate checks complex random `a,b` shifts directly.

## 5. Mixed-copy control

As an adversarial control, RFG31 assigns different helicity patterns to the two Yang–Mills copies. On those tensor-product states the executable witness activates trace and/or antisymmetric coordinates. This confirms that the matching-helicity condition is an active state selector on the full tensor-product space.

## 6. Helicity-branch support

On the holomorphic `s12` factorization family used by RFG28/RFG29, supported MHV assignments give a finite nonzero residue. The two-negative `(1-,2-)` pair belongs to the complementary three-point branch on this family and its tested residue collapses to numerical zero.

## 7. Graph double-copy residue

For matching pure-spin-2 copy helicities, RFG30 and RFG29 combine to

\[
\boxed{
\operatorname*{Res}\mathcal C_{5,15g}^{project}
=-4(s_{13}+s_{23})R_LR_R
}
\]

with `R_L R_R` equal to the symmetric-traceless internal contraction above.

The physical graph-oriented residue is

\[
\boxed{
\operatorname*{Res}\mathcal M_5^{project}
=-iP_5(s_{13}+s_{23})R_LR_R,
\qquad P_5=(\kappa_g/2)^3.
}
\]

## 8. Executable validation

Fresh live-surface result:

```text
6 passed, 0 failed
```

The test covers multiple MHV helicity assignments, channel transversality/nullness, explicit trace/antisymmetric decomposition, channel gauge shifts, a mixed-copy control, holomorphic three-point branch support and the RFG30 graph residue.

## 9. Advancement

```text
five-point matched-helicity s12 internal seed                 PASS TRANSVERSE NULL
internal three-point tensor symmetric-traceless              PASS
trace contribution to selected residue                       ZERO
antisymmetric contribution to selected residue               ZERO
selected tree residue through spin-2 coordinate              PASS
mixed-copy tensor coordinates                                WITNESSED CONTROL
explicit graph residue <-> spin-2 current product            PASS
permutation-complete tree internal-state audit               NEXT OPTIONAL TREE EXTENSION
loop internal-state spectrum / pure-spin2 closure            NEXT RFG32
```
