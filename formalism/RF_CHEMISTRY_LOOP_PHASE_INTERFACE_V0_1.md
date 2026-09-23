# RF Chemistry Loop-Phase Source Interface v0.1

Status: EXACT_GAUGE_KINEMATICS / FIXED_CARRIER_LINEAR_RESPONSE / COMMON_PHYSICAL_CYCLE_BINDING_OPEN

## 1. Purpose

This note narrows the candidate chemistry handoff to a gauge-invariant loop coordinate already present in RFC. It does not identify an RFC path with a chemical/effective-state cycle and does not add a new chemistry interaction.

RF-F1 defines the lifted, gauge-invariant relational phase

\[
\Phi_C(x|x_0)
=
\widetilde\vartheta(x)
-
\widetilde\vartheta(x_0)
+
\int_C \mathcal A_-.
\]

For two paths with the same endpoints,

\[
\boxed{
\Gamma[C_1,C_2]
:=
\Phi_{C_1}-\Phi_{C_2}
=
\oint_{C_1\circ C_2^{-1}}\mathcal A_-.
}
\]

This is a lifted loop-holonomy coordinate. Its projective representative is
\(e^{i\Gamma}\).

## 2. Loop displacement between two admitted realizations

Let the same declared loop/cycle identity be evaluated in a reference realization r=0 and a perturbed realization r=1:

\[
\Gamma_a^{(0)},\qquad \Gamma_a^{(1)}.
\]

Define the lifted displacement

\[
\boxed{
\delta\Phi_a^{RFC}
=
\Gamma_a^{(1)}-\Gamma_a^{(0)}.
}
\]

Both parent loop coordinates are gauge invariant, so their difference is gauge invariant.

The projective displacement is

\[
\boxed{
\delta\phi_a^{proj}
=
\operatorname{Arg}
\exp(i\delta\Phi_a^{RFC})
}
\]

while the lifted displacement retains winding information. A first-order downstream expansion must declare a continuous local lift; it may not replace a large winding jump by a small perturbation after inspecting a target result.

## 3. Exact gauge test

For a common endpoint gauge transformation, each path integral changes by the same endpoint term,

\[
I_C\mapsto I_C-(\lambda_x-\lambda_0).
\]

Therefore

\[
(I_{C_1}-\Delta\lambda)-(I_{C_2}-\Delta\lambda)
=
I_{C_1}-I_{C_2},
\]

and hence

\[
\boxed{\Gamma' = \Gamma},\qquad
\boxed{\delta\Phi' = \delta\Phi}.
\]

No physical interpretation is required for this identity.

## 4. Fixed-carrier RF-F5 energy slope

RF-F5 gives

\[
\epsilon_G
=
B\omega(\Phi_C+\kappa).
\]

At fixed B and omega,

\[
\boxed{
\frac{\partial\epsilon_G}{\partial\Phi_C}
=
B\omega.
}
\]

Hence a lifted phase displacement has the exact fixed-carrier response

\[
\boxed{
\delta\epsilon_G
=
B\omega\,\delta\Phi
}
\]

when B and omega are unchanged between the compared states.

Dimensionally,

\[
[B]=E T,\qquad [\omega]=T^{-1},\qquad [\delta\Phi]=1,
\]

so \([\delta\epsilon_G]=E\).

This does not close the physical normalization because RFC still lists physical B-action realization and common phase-path/reference realization as OPEN inputs.

## 5. Chemistry cross-repository handoff

Resonant Chemistry may consume a dimensionless gauge-invariant cycle displacement only after a separate physical identity contract establishes that

\[
\boxed{
\Gamma_a^{RFC}
\leftrightarrow
\Phi_a^{RC}
}
\]

refers to the same physical carrier/cycle and state comparison.

The mathematical type match alone is insufficient.

The future cross-repository gate is COMMON_PHYSICAL_CYCLE_BINDING with required evidence:

1. common carrier identity;
2. common cycle/path identity;
3. same reference and perturbed physical states;
4. units/normalization and orientation convention;
5. no use of target spectroscopy residuals in the binding;
6. independent validation receipt.

## 6. Relation to the RC first-order operator

If the common-cycle gate later passes, the RC linearized operator

\[
V_I^{(1)}
=
\sum_a\delta\Phi_a^{RC}
\frac{\partial H_{RC}}{\partial\Phi_a}
\]

may consume

\[
\delta\Phi_a^{RC}
=
\delta\Phi_a^{RFC}.
\]

Until then this equality is CANDIDATE_ONLY.

## 7. Epistemic boundary

Exact in this RFC candidate:

- loop phase from two same-endpoint paths;
- gauge invariance of the loop phase;
- gauge invariance of its inter-realization displacement;
- lifted versus projective displacement separation;
- RF-F5 fixed-B,omega energy slope and dimensions.

Open:

- physical shared RFC/RC cycle realization;
- physical B-action realization;
- chemical state-space carrier binding;
- any measured new chemistry effect.

No Standard-Model, gravitational, semantic or consciousness interpretation follows from this interface.
