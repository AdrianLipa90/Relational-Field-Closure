# AUX RGB-Moire QCD Group-Invariant Gate v0.1

Status: `TF_HALF_PASS / CF_FOUR_THIRDS_PASS / CA_THREE_PASS / ONE_LOOP_GROUP_FACTOR_PASS / PHYSICAL_RUNNING_NORMALIZATION_OPEN`

Date: 2026-09-26

## Purpose

This gate asks how much of standard QCD running follows already from the
Weyl-derived SU(3) representation, before any physical coupling normalization
or scale is inserted.

The result is structural: it derives the SU(3) group factors from the AUX
RGB-Moire representation. It does not by itself derive a measured running
coupling.

## Fundamental normalization

Use the Weyl-derived generators (T_A) from the previous gates with

[
operatorname{Tr}(T_A T_B)=rac12delta_{AB}.
]

Therefore the fundamental Dynkin index is

[
oxed{T_F=rac12}.
]

## Fundamental quadratic Casimir

The executable gate verifies

[
sum_{A=1}^{8}T_A T_A
=
rac43 I_3
]

to floating-point residual below (5	imes10^{-16}). Hence

[
oxed{C_F=rac43}.
]

## Adjoint quadratic Casimir

From the Weyl-derived structure constants,

[
f_{ACD}f_{BCD}=3delta_{AB},
]

so

[
oxed{C_A=3}.
]

This agrees with the previous direct adjoint-Casimir gate.

## One-loop QCD group coefficient

For SU(3) with (n_f) fundamental Dirac flavours, the standard one-loop
coefficient is

[
b_0
=
rac{11C_A-4T_F n_f}{12pi}.
]

Substituting only the group factors derived above gives

[
oxed{
b_0
=
rac{33-2n_f}{12pi}.
}
]

Therefore the sign of the one-loop beta function is structurally fixed by the
AUX/Weyl SU(3) representation once the matter multiplicity (n_f) is supplied.

In particular,

[
b_0>0quadLongleftrightarrowquad n_f<rac{33}{2}.
]

This closes the group-theoretic asymptotic-freedom coefficient. It does not
derive the physical flavour count, renormalization scale, Lambda_QCD, or the
boundary value of alpha_s.

## Z3 center firewall

The Weyl construction contains the center elements

[
Z(SU(3))={I,omega I,omega^2 I}.
]

They act trivially in the adjoint representation,

[
zT_Az^dagger=T_A,
]

while acting nontrivially on a fundamental triplet. This is the correct
representation-theoretic distinction.

Accordingly, center symmetry is useful as a pure-gauge structural diagnostic
but is not promoted here as an exact symmetry of full QCD with dynamical
fundamental quarks.

## Relation to existing project gates

- RFG4 explicitly leaves running-coupling validation open after the bare
  coupling coordinate is frozen.
- RFG11 closes the local eight-component SU(3) field and adjoint covariance.
- TIR Stage 27 closes the gauge-invariant quark-triplet/link bilinear.

The present gate removes the SU(3) group factors from the running-coupling
debt. What remains is physical normalization and RG/scale binding, not the
values of (T_F,C_F,C_A).

## Validation

Reference:

`tests/reference/test_aux_rgb_moire_qcd_group_invariants.py`

Local result:

```text
5 passed, 0 failed
```

Numerical residuals:

- (C_F=4/3): (4.44	imes10^{-16})
- (C_A=3): (8.89	imes10^{-16})

## Verdict

[
oxed{
	ext{AUX RGB-Moire Weyl SU(3)}
Rightarrow
T_F=rac12, C_F=rac43, C_A=3
Rightarrow
b_0=rac{33-2n_f}{12pi}
}
]

at the representation/group-theory level.

`PHYSICAL_ALPHA_S_BOUNDARY_VALUE / RG_SCALE_BINDING / LAMBDA_QCD /
NONPERTURBATIVE_CONFINEMENT` remain open.
