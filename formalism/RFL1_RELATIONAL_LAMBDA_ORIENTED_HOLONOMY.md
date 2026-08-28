# RF-L1 — Relational Lambda Oriented Holonomy Closure

Status: `IDT_01L_INTERFACE_BOUND / ORIENTED_HOLONOMY_CANDIDATE / HERMITIAN_EMBEDDING_OPEN`

Pinned upstreams and implementation witness:

- IDT branch `feat/relational-lambda-oriented-holonomy-v0.1`: `305e8602620b552052471fadfe798cad44a2d182`
- GREMLIN branch `feat/gremlin-oriented-relational-coupling-v1.3`: `d7a93d55bd7f55e6b23a418f6906f2e5f72943e4`
- GREMLIN CI run `33125002181`: `201 passed`
- RF-L0 temporal information curvature closure: current RFC upstream

## 1. Purpose

RF-L1 binds the RFC relational-Lambda scalar sector to the oriented temporal holonomy exported by IDT 01L. The closure preserves scalar source scale, connection lineage, cycle orientation, and energy partition in one typed chain:

\[
\boxed{
\Xi_I
\rightarrow
\Lambda_R
\rightarrow
E_R
\rightarrow
\tau_R
\rightarrow
(J_C,J_D)
\rightarrow
\mathcal J_R
}
\]

RF-L0 supplies the information-curvature scalar basis and Einstein-Bianchi bookkeeping. IDT 01L supplies the temporal U(1) connection and oriented cycle holonomy.

## 2. Scalar-field binding

RF-L0 defines the information-sector candidate

\[
\Lambda_I=\alpha_I\Xi_I,
\qquad
\Xi_I=\frac{\mathcal J_\pi}{\mathcal A_{\rm rel}},
\qquad [\Xi_I]=L^{-2}.
\]

RF-L1 uses the generic admitted relational scalar field

\[
\boxed{\Lambda_R(x)},
\qquad [\Lambda_R]=L^{-2},
\]

with explicit provenance to whichever RFC scalar-basis closure supplies it. In the minimal information-sector candidate, `Lambda_R` may be instantiated by `Lambda_I` once the RF-L0 coupling gate is admitted.

## 3. Effective source-energy map

Using the Einstein-Lambda effective-source convention,

\[
\boxed{u_R
=\frac{c^4}{8\pi G}\Lambda_R
}
\]

and, for an admitted positive support volume `V_R`,

\[
\boxed{E_R=u_RV_R.}
\]

The dimensions close as

\[
[u_R]=E L^{-3},
\qquad
[E_R]=E.
\]

The source-energy receipt must retain the `Lambda_R` commitment, support volume, and convention identifier.

## 4. IDT oriented holonomy import

IDT 01L exports the closed-cycle temporal phase

\[
\Phi_T(C)
=\gamma_B(C)+\kappa\sum_{e\in C}\sigma_e
\pmod{2\pi}
\]

and principal oriented coordinate

\[
\boxed{
\tau_R(C)=\operatorname{wrap}_{\pi}\Phi_T(C).
}
\]

The corresponding U(1) carrier is

\[
\boxed{
h_R=e^{i\tau_R}=\cos\tau_R+i\sin\tau_R.}
\]

Its imaginary quadrature retains the sign of cycle orientation.

## 5. Holonomy-resolved source energy

Define the complementary half-angle weights

\[
\boxed{
C_h=\cos^2\frac{\tau_R}{2},
\qquad
D_h=\sin^2\frac{\tau_R}{2}.
}
\]

They obey

\[
\boxed{C_h+D_h=1}
\]

and

\[
\boxed{C_h-D_h=\cos\tau_R}.
\]

The source-energy channels are

\[
\boxed{
J_C=E_RC_h,
\qquad
J_D=E_RD_h.
}
\]

Therefore

\[
\boxed{J_C+J_D=E_R}
\]

and

\[
\boxed{J_C-J_D=E_R\cos\tau_R.}
\]

These identities are exact once `E_R` and `tau_R` are admitted.

## 6. Oriented relational coupling amplitude

Define

\[
\boxed{
\mathcal J_R
:=E_Re^{i\tau_R}.
}
\]

Then

\[
\boxed{
\operatorname{Re}\mathcal J_R
=E_R\cos\tau_R
=J_C-J_D
}
\]

and

\[
\boxed{
\operatorname{Im}\mathcal J_R
=E_R\sin\tau_R.
}
\]

Magnitude closure is

\[
\boxed{|\mathcal J_R|=|E_R|.}
\]

Thus RFC source magnitude and IDT cycle orientation remain jointly represented after the scalar-to-energy transition.

## 7. Geometry and connection closure

The RF-L1 receipt binds

```text
RELATIONAL_LAMBDA_ORIENTED_HOLONOMY_CLOSURE
  Lambda_R_commitment          = RFC scalar-source lineage
  source_energy                = E_R
  IDT_connection_commitment    = temporal U(1) connection lineage
  cycle_id                     = C
  holonomy                     = tau_R
  holonomy_unit                = exp(i tau_R)
  channel_energy_sum           = J_C + J_D = E_R
  oriented_coupling            = J_R = E_R exp(i tau_R)
```

For a spacetime/spinorial target, the connection adapter must bind the RFC geometric connection or spin connection to the imported U(1) projection used to obtain `tau_R`.

## 8. Einstein-Bianchi bookkeeping

RF-L0 carries the dynamic scalar equation convention

\[
G_{\mu\nu}+\Lambda_0g_{\mu\nu}
=\frac{8\pi G}{c^4}T^{\rm visible}_{\mu\nu}
\]

with the corresponding Bianchi bookkeeping for gradients of `Lambda0`.

RF-L1 adds the oriented phase/holonomy data after scalar-field binding. The scalar source entering the metric closure remains the RFC scalar commitment; the oriented coupling `mathcal J_R` is exported to the interaction/operator layer with the same source lineage.

This keeps the source-curvature and transport-orientation receipts connected by a shared `Lambda_R` commitment.

## 9. Quantum interaction frontier

A physical interaction operator requires an explicit Hermitian embedding of the oriented coupling. The reference GREMLIN stack currently provides:

- exact channel partition identities given the admitted inputs;
- orientation retention through `E_R sin(tau_R)`;
- a two-qubit joint-state concurrence witness;
- a declared `ZZ` interaction diagnostic for reference conformance;
- a synchronization control separated from the joint-state witness.

RF-L1 records:

```text
oriented_coupling             = CANDIDATE_WITH_REFERENCE_CONFORMANCE
hermitian_operator_embedding  = OPEN
neutrino_phase_binding         = TEST_TARGET
joint_state_witness            = REQUIRED_FOR_ENTANGLEMENT_ATTRIBUTION
physical_channel_attribution  = OPEN
```

## 10. Falsification gates

RF-L1 advances through independent receipts for:

1. determination or falsifiable bound of the RFC scalar coupling supplying `Lambda_R`;
2. metric-variation and Bianchi-compatible source closure;
3. explicit geometric/spin-connection projection for the target system;
4. Hermitian embedding of `mathcal J_R`;
5. target-system oscillation-phase prediction;
6. comparison against standard vacuum and matter oscillation phases;
7. joint-state entanglement witness when that claim is tested;
8. a synchronization-only control;
9. orientation reversal test `tau_R -> -tau_R`, preserving the real projection and reversing the rotational quadrature.

The author/formalism may suggest that relational Lambda, internal geometric rotation and phase coupling form one closure chain, yet does not state that physical realization as an established result before these gates are receipted.
