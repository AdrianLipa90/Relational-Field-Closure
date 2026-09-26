# AUX RGB-Moire SU(3) Structure-Tensor Gate v0.1

Status: `EXACT_LIE_TENSOR_INTERTWINER_PASS / EXACT_ADJOINT8_PASS / STANDARD_C_A_3_PASS / PHYSICAL_QCD_COLOR_BINDING_OPEN`

Date: 2026-09-26

## Scope

This gate strengthens `AUX_RGB_MOIRE_WEYL_SU3_BRIDGE_V0_1`.
It tests whether the Weyl-derived eight-dimensional sector is merely an
8D vector space or is the full standard `su(3)` Lie algebra up to an
orthogonal basis transformation.

It does not identify the representation with physical QCD color.

## Inputs

Use the finite Weyl pair

[
Z X = omega X Z,qquad omega=e^{2pi i/3},
]

with

[
X=P_3,qquad Z=operatorname{diag}(1,omega,omega^2).
]

From the fixed nonidentity Weyl words

[
Z, X, XZ, XZ^2
]

take Hermitian and anti-Hermitian parts, remove trace, and perform a
deterministic Hilbert-Schmidt Gram-Schmidt construction. Normalize the
resulting basis (T_A^{W}) so that

[
operatorname{Tr}(T_A^{W}T_B^{W})=rac12delta_{AB}.
]

Let (T_a^{GM}=lambda_a/2) be the standard Gell-Mann basis with the same
normalization.

## Orthogonal intertwiner

Define

[
O_A{}^a=2,operatorname{Tr}(T_A^{W}T_a^{GM}).
]

The reference gate obtains

[
|OO^T-I_8|_infty < 5	imes10^{-16},
]

so

[
oxed{T_A^{W}=O_A{}^a T_a^{GM}}
]

is an orthogonal basis change.

## Full structure tensor

Define both tensors by

[
[T_A,T_B]=i f_{ABC}T_C.
]

The transported Gell-Mann tensor is

[
widetilde f_{ABC}
=
O_A{}^a O_B{}^b O_C{}^c f^{GM}_{abc}.
]

The numerical gate gives

[
oxed{
max_{ABC}|f^W_{ABC}-widetilde f_{ABC}|
=2.22	imes10^{-16}.
}
]

Therefore the Weyl-derived algebra agrees with the complete Gell-Mann
commutator tensor, not only with its dimension.

## Adjoint-eight representation

Represent the adjoint generators by

[
(mathrm{ad}_A)_B{}^C=f_{ABC}.
]

The transformed Gell-Mann adjoint representation agrees with the
Weyl-derived adjoint representation with maximum residual

[
oxed{2.22	imes10^{-16}}.
]

Thus the same RGB/orbital construction carries the full eight-dimensional
adjoint representation at the algebraic level.

## Quadratic adjoint Casimir

With standard QCD normalization
(operatorname{Tr}(T_aT_b)=rac12delta_{ab}),

[
sum_A mathrm{ad}_Amathrm{ad}_A^T
=
3I_8
]

within a maximum residual (8.89	imes10^{-16}). Hence

[
oxed{C_A=3},
]

the standard SU(3) adjoint Casimir value.

## Cross-repository binding state

Existing project evidence already supplies:

- TIR Stage 27: exact gauge-invariant quark-triplet/link bilinear;
- RFC RFG11: full eight-component local SU(3) link-log recovery and adjoint covariance;
- RFC RFG12-RFG15: non-Abelian color mixing, quartic Yang-Mills, four-gluon Ward and BCJ continuation.

The remaining physical seam is therefore not the Lie algebra.

## GREMLIN live audit

Live GREMLIN event:

`gremlin:whisper:sha256:1c843fa3ea0e914fd9136b0059f9b187c1f0e6c46b45ad6f246d12fa9b75e4d6`

was accepted under `CANDIDATE_ONLY` authority. Terminal36D fused the query and
GREMLIN routed it through OWL/SPIDER/HOUND roles. The graph/repository audit
identifies the remaining physical gates as:

1. source-owned identification of the AUX RGB fundamental carrier with the
   physical QCD color triplet;
2. physical coupling genealogy and running-coupling validation;
3. nonperturbative confinement/hadronization validation.

Center symmetry is not promoted as a universal full-QCD binding criterion;
with dynamical fundamental quarks ordinary center symmetry is explicitly
broken, so a pure-Yang-Mills center argument cannot by itself close QCD.

## Validation

Reference:

`tests/reference/test_aux_rgb_moire_su3_structure_tensor.py`

Local result:

```text
5 passed, 0 failed
```

Measured maximum residuals:

- Weyl relation: (6.74	imes10^{-16})
- orthogonal intertwiner: (4.44	imes10^{-16})
- full structure tensor: (2.22	imes10^{-16})
- adjoint intertwiner: (2.22	imes10^{-16})
- (C_A=3) Casimir: (8.89	imes10^{-16})

## Verdict

[
oxed{
	ext{AUX RGB + orbital }C_3
Longrightarrow
	ext{full }mathfrak{su}(3)	ext{ Lie tensor}
Longrightarrow
mathbf 8_{mathrm{adj}}
}
]

is closed at the representation/algebra level.

`PHYSICAL_SU3_COLOR_IDENTIFICATION / RUNNING / CONFINEMENT` remain separate
physical gates.
