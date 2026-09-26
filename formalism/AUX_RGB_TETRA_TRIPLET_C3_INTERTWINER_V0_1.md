# AUX RGB to Tetrahedral Triplet C3 Intertwiner v0.1

Status: `EXACT_C3_EQUIVARIANT_REPRESENTATION_BRIDGE / PHYSICAL_QCD_COLOR_BINDING_OPEN`

Date: 2026-09-26

## Purpose

This note connects the generic AUX RGB three-channel carrier to the existing
Module-39 tetrahedral triplet at the representation level without declaring
that RGB labels are physical QCD colors by definition.

## Tetrahedral parent

Module 39 uses

[
v_0=(1,1,1),quad
v_1=(1,-1,-1),quad
v_2=(-1,1,-1),quad
v_3=(-1,-1,1).
]

Choosing (v_0) as reference leaves the opposite equilateral face
((v_1,v_2,v_3)), whose labels supply the project triplet carrier.

The proper (120^circ) rotation about the (v_0) axis is

[
R_{tet}=
egin{pmatrix}
0&0&1\
1&0&0\
0&1&0
end{pmatrix}.
]

It fixes (v_0) and acts by

[
v_1	o v_2	o v_3	o v_1.
]

Therefore

[
R_{tet}^3=I,qquad det R_{tet}=1,
]

and the opposite face carries the regular oriented (C_3) action.

## Exact match to AUX orbital shift

The existing AUX orbital shift is

[
X_{orb}=P_3=
egin{pmatrix}
0&0&1\
1&0&0\
0&1&0
end{pmatrix}.
]

Hence

[
oxed{R_{tet}=X_{orb}}
]

as matrices in the declared ordered representations.

This is stronger than a shared cardinality-three statement: the same
order-three operator acts on both carriers.

## Character basis

Let

[
omega=e^{2pi i/3},qquad
F_3=rac1{sqrt3}
egin{pmatrix}
1&1&1\
1&omega&omega^2\
1&omega^2&omega
end{pmatrix}.
]

Then

[
F_3^dagger P_3 F_3
=
operatorname{diag}(1,omega^2,omega).
]

With

[
Z_{RGB}=operatorname{diag}(1,omega,omega^2),
]

this becomes

[
oxed{
F_3^dagger R_{tet}F_3=Z_{RGB}^dagger.
}
]

Thus the AUX RGB roots of unity are exactly the character spectrum of the
oriented tetrahedral face cycle, up to reversal of orientation.

## Anchored label intertwiner

Choose the representation anchor

[
|Ranglemapsto |color_0angle,qquad
|Ganglemapsto |color_1angle,qquad
|Banglemapsto |color_2angle.
]

In these ordered bases (M=I_3), and

[
oxed{
M X_{orb}=P_{color}M.
}
]

The bridge is therefore an exact (C_3)-equivariant representation
intertwiner.

Changing the orientation exchanges (omegaleftrightarrowomega^2) and
corresponds to the inverse cycle; this is a representation convention, not
a new physical parameter.

## Consequence

The current chain is now

[
	ext{generic AUX three-channel carrier}
	o
C_3	ext{ orbital action}
leftrightarrow
C_3	ext{ tetrahedral opposite-face action}
	o
mathbb C^3	ext{ project triplet}
	o
CP^2
	o
mathfrak{su}(3)
]

at the representation level.

Together with the Weyl and structure-tensor gates, AUX RGB therefore has an
exact representation path into the existing project triplet/SU(3) carrier.

## Firewall

This theorem does not state

[
RGB equiv 	ext{physical QCD color}.
]

AUX is a reusable three-channel relational carrier and has also been used in
other sectors. The theorem only proves that its oriented (C_3)
representation is exactly equivariant with the tetrahedral triplet already
used by the project color construction.

The remaining physical gate is whether that project triplet is the
physically realized QCD color degree of freedom, including the correct
coupling/running and nonperturbative confinement behavior.

## Validation

Reference:

`tests/reference/test_aux_rgb_tetra_triplet_intertwiner.py`

Local result:

```text
4 passed, 0 failed
```

Status:

`EXACT_TETRA_FACE_C3_EQUALS_AUX_ORBITAL_C3 / EXACT_CHARACTER_CROSSWALK /
EXACT_ANCHORED_INTERTWINER / PHYSICAL_QCD_COLOR_BINDING_OPEN`.
