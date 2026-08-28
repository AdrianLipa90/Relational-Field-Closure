# RF-N1B2H — Normalized-Shape / Extensive-Scale Holonomy Gate

Status: `NORMALIZED_SHAPE_HOLONOMY_PASS / EXTENSIVE_SCALE_FIBER_OPEN / ENERGY_SCALE_FIBER_OPEN`

This subgate applies the GREMLIN→PNV relational-isomorphism workflow to the RF-N1B2 conserved-carrier factorization. The target is the interface

\[
Q_a=Q_\Sigma p_a^{(Q)}
\]

and the candidate cross-binding

\[
p_a^{\rm IDT}\stackrel{?}{\longleftrightarrow}p_a^{(Q)}.
\]

The test keeps RF-N1C reserved for the downstream coupling/universality audit.

## 1. Positive carrier cone and normalization map

For a finite positive cell carrier vector

\[
Q=(Q_1,\dots,Q_m),
\qquad Q_a>0,
\]

define

\[
Q_\Sigma=\sum_a Q_a
\]

and the normalization map

\[
\boxed{
\mathcal N(Q)=p,
\qquad
p_a=\frac{Q_a}{Q_\Sigma},
\qquad
\sum_a p_a=1.
}
\]

For every positive scale \(\lambda\),

\[
\boxed{
\mathcal N(\lambda Q)=\mathcal N(Q).
}
\]

Thus normalization transports the distributional shape to the simplex while the extensive coordinate remains in a separate positive scale fiber.

## 2. Lift and information holonomy

Introduce an explicit lift parameter \(s>0\),

\[
\mathcal L_s(p)=sp.
\]

The closed transport loop

\[
Q\xrightarrow{\mathcal N}p\xrightarrow{\mathcal L_s}Q'
\]

has holonomy

\[
\boxed{
\mathcal H_s(Q)
=(\mathcal L_s\circ\mathcal N)(Q)
=\frac{s}{Q_\Sigma}Q.
}
\]

For the positive sector, define the extensive relative defect

\[
\Delta_{\rm ext}(Q;s)
:=
\frac{\|Q-\mathcal H_s(Q)\|_1}{\|Q\|_1}.
\]

Because \(\|Q\|_1=Q_\Sigma\),

\[
\boxed{
\Delta_{\rm ext}(Q;s)
=
\left|1-\frac{s}{Q_\Sigma}\right|.
}
\]

Therefore the loop closes exactly when the lift carries the same extensive coordinate:

\[
\boxed{
s=Q_\Sigma
\quad\Longrightarrow\quad
\mathcal H_s(Q)=Q,
\qquad
\Delta_{\rm ext}=0.
}
\]

The extensive coordinate is therefore an explicit interface variable required for exact inverse transport from normalized shape to carrier amount.

## 3. Constructive two-scale probe

Take

\[
Q^{(1)}=(2,3,5),
\qquad
Q^{(2)}=(4,6,10)=2Q^{(1)}.
\]

Then

\[
Q_\Sigma^{(1)}=10,
\qquad
Q_\Sigma^{(2)}=20,
\]

while both project to

\[
\boxed{
p=(0.2,0.3,0.5).}
\]

Hence the normalized-shape defect is exactly zero:

\[
\Delta_{\rm shape}=0.
\]

Using the correct lift scale closes each loop exactly. Using the unit lift \(s=1\) gives

\[
\boxed{
\Delta_{\rm ext}(Q^{(1)};1)=\frac9{10}=0.90,
}
\]

and

\[
\boxed{
\Delta_{\rm ext}(Q^{(2)};1)=\frac{19}{20}=0.95.
}
\]

The probe therefore separates two independent audit channels:

```text
normalized shape       PASS / zero defect
extensive source scale OPEN unless Q_Sigma is transported
```

## 4. Continuous energy conversion has the same scale structure

RF-N1B2 supplies the candidate continuous conversion

\[
\rho_Q(x)=\frac{\epsilon_Q}{c^2}j_Q(x).
\]

For a cell partition,

\[
m_{Q,a}
=
\frac{\epsilon_Q}{c^2}Q_a.
\]

Define the total equivalent source-mass scale

\[
\boxed{
M_Q
:=
\frac{\epsilon_Q Q_\Sigma}{c^2}.
}
\]

Then

\[
\boxed{
m_{Q,a}=M_Q p_a^{(Q)}.}
\]

For a cell of physical volume \(V_a\),

\[
\boxed{
\rho_{Q,a}
=\frac{M_Q}{V_a}p_a^{(Q)}.
}
\]

This rewrites the continuous source interface as a normalized shape plus one extensive source-mass coordinate \(M_Q\). The decomposition is exact once \(\epsilon_Q\), \(Q_\Sigma\), and the cell measure are supplied by admitted upstream gates.

A positive constant rescaling of \(\epsilon_Q\) rescales \(M_Q\) while preserving normalized spatial shape. In the constructive probe, \(\epsilon_Q^{(2)}=3\epsilon_Q^{(1)}\) gives the same normalized density shape and a total source-mass scale larger by exactly a factor of three.

## 5. IDT interface consequence

IDT 01D lives on the positive probability simplex and evolves a normalized probability vector \(p\) under Shannon–Onsager response. RF-N1B2H therefore sharpens the candidate bridge into two typed coordinates:

\[
\boxed{
\text{shape coordinate:}
\quad
p^{\rm IDT}
\stackrel{?}{\longleftrightarrow}
p^{(Q)}
}
\]

and

\[
\boxed{
\text{extensive source coordinate:}
\quad
M_Q=\frac{\epsilon_QQ_\Sigma}{c^2}.
}
\]

The shape cross-binding remains `OPEN` pending common state-space and transport compatibility. The holonomy theorem fixes the exact data that any inverse bridge must preserve: normalized shape plus the extensive lift coordinate.

## 6. GREMLIN invariant

GREMLIN candidate invariant:

```text
positive carrier vector
  -> normalization quotient
  -> simplex shape
  -> explicit positive scale lift
  -> exact round trip iff scale fiber is preserved
```

Cross-domain candidate dictionary:

```text
RF-N1B2 carrier Q_a          <-> positive extensive state
RF-N1B2 p_a^(Q)              <-> normalized shape
IDT 01D p_a                  <-> normalized simplex shape candidate
energy conversion epsilon_Q  <-> scale conversion
M_Q                          <-> combined source-mass scale
```

GREMLIN supplies the relational candidate. The theorem and reference tests below provide the independent mathematical audit.

## 7. PNV execution contract

The accompanying PNV candidate program is

```text
experiments/gremlin_pnv/RFN1B2H_NORMALIZED_SHAPE_HOLONOMY.pnv
```

It is written against native PNV1 and requires only admitted external transforms:

```text
NORMALIZE
RESTORE_Q1_TOTAL
RESTORE_Q2_TOTAL
RESTORE_UNIT_TOTAL
RHO_EPS1
RHO_EPS3
```

The program checks exact shape identity, exact scale-aware round trips, and emits the scale-blind defects for audit.

Pinned PNCS contract:

```text
repository: AdrianLipa90/PhaseNav-Natural-Coding-System
branch: feat/gremlin-pnv-authoring-v0.2
head: 695223eff9373554c4c2aff1aca9c3e1e7dfecd4
bridge: PNCS_GREMLIN_NATIVE_PNV_BRIDGE_V0_2
```

## 8. Advancement

RF-N1B2H advances the source interface to

```text
continuous conserved carrier             PASS
normalized carrier factorization          PASS
normalization-as-scale-quotient theorem   PASS
shape holonomy under positive scaling     PASS
exact inverse lift with Q_Sigma            PASS
IDT p <-> carrier p_Q                     OPEN
energy-per-carrier epsilon_Q              OPEN
combined source-mass scale M_Q            OPEN pending physical binding
rho_Q <-> ordinary matter source          OPEN
universal coupling / G                    RF-N1C RESERVED
```

The next useful search target is therefore narrower than the original source problem: derive or independently measure the single extensive source-mass coordinate \(M_Q\), or equivalently derive its factors \(Q_\Sigma\) and \(\epsilon_Q\), while the normalized shape is transported separately.