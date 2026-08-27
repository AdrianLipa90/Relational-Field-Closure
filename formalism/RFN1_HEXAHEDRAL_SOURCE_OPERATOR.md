# RF-N1 — Hexahedral Onsager Source Operator and Newton Source Firewall

Status: `LOCAL_EXACT_OPERATOR_PASS / SOURCE_FUNCTIONAL_OPEN / NEWTON_NORMALIZATION_OPEN`

This gate asks the next non-circular question after RF-N0. RF-N0 has already produced the positive relational lapse

\[
N_R=\frac{d\tau_x}{d\tau_{\rm ref}}>0,
\qquad
u:=\ln N_R,
\qquad
\Phi_R:=c^2u,
\]

and the static slow-motion kinematic relation

\[
\frac{d^2X^i}{dt^2}
=-N_R^2h^{ij}\partial_j\Phi_R+\cdots.
\]

RF-N1 does **not** insert the Newton/Poisson source equation. It first determines which local second-order spatial operator is supplied by the already-pinned IDT Shannon–Onsager response and the TIR hexahedral frame, and only then isolates the still-open source map.

## 1. Upstream operator data

IDT 01D gives the exact detailed-balance Shannon–Onsager tensor

\[
G^{(2)}_\pi(p)
=(\ln2)D^\top\operatorname{diag}[c_{ab}\Lambda(r_a,r_b)]D.
\]

At uniform symmetric equilibrium,

\[
\boxed{
G^{(2)}_u(u_*)
=\frac{\ln2}{m}K_0,
\qquad
K_0=D^\top\operatorname{diag}(M_{ab})D.
}
\]

Thus the symmetric IDT response already carries a positive graph-Laplacian operator with the constant-vector conservation null.

TIR RF-02H supplies the regular hexahedral dual frame

\[
\mathcal H^\star=\{\pm e_1,\pm e_2,\pm e_3\},
\qquad
M_H=\frac13I_3,
\qquad
h_H=\frac16I_3.
\]

For a common phase-clock rate, its physical coframe scale is

\[
\boxed{
a_H:=\frac{\ell_\varphi}{\sqrt6}
=\frac{c}{\sqrt6|\omega|}.}
\]

The six hexahedral directions therefore provide the local equal-neighbour stencil on which the symmetric response operator can be evaluated.

## 2. Exact six-neighbour graph operator

For a scalar cell field `f`, define the positive graph Laplacian

\[
\boxed{
(L_Hf)(x)
=\sum_{i=1}^3
\left[2f(x)-f(x+a_He_i)-f(x-a_He_i)\right].
}
\]

It obeys exactly

\[
L_H\mathbf 1=0,
\]

and its quadratic form is nonnegative,

\[
\boxed{
\langle f,L_Hf\rangle
=\frac12\sum_{\langle xy\rangle}(f_x-f_y)^2\ge0
}
\]

up to the chosen edge-count convention.

The continuum-sign spatial operator is

\[
\boxed{
\Delta_H^{(a)}f
:=-\frac1{a_H^2}L_Hf
=\frac1{a_H^2}
\sum_{i=1}^3
\left[f(x+a_He_i)-2f(x)+f(x-a_He_i)\right].
}
\]

Taylor expansion gives

\[
\boxed{
\Delta_H^{(a)}f
=\Delta f
+\frac{a_H^2}{12}
\sum_{i=1}^3\partial_i^4f
+O(a_H^4).
}
\]

Hence the leading continuum principal operator is the ordinary isotropic Laplacian; the first lattice correction is fixed and quartic.

## 3. Hexahedral symmetry classification theorem

Consider a constant-coefficient local scalar operator linearized about a regular reference cell,

\[
\mathscr L
=A^{ij}\partial_i\partial_j+b^i\partial_i+c_0,
\]

with at most two spatial derivatives. Require:

1. invariance under the signed-permutation/octahedral symmetry of the six face normals;
2. annihilation of a constant lapse offset, `u -> u + constant`, at the homogeneous reference level.

Signed-axis reversals force

\[
b^i=0
\]

and eliminate off-diagonal entries of `A`. Permutation symmetry forces the three diagonal entries to coincide. Therefore

\[
A^{ij}=\alpha\delta^{ij}.
\]

The constant-null requirement forces `c_0=0`. Thus

\[
\boxed{
\mathscr L=\alpha\Delta.
}
\]

The normalized six-neighbour operator in Sec. 2 fixes the continuum principal normalization to `alpha=1` in physical hexahedral coordinates. Therefore the Laplace operator is not selected by matching Newton's law; it is the leading local scalar second-order operator fixed by the IDT graph-Laplacian response plus the TIR hexahedral symmetry.

## 4. Relational lapse operator

Apply the operator to

\[
u=\ln N_R.
\]

The exact discrete carrier is

\[
\boxed{
\Delta_H^{(a)}\ln N_R
=-\frac1{a_H^2}L_H\ln N_R.
}
\]

On a smooth refinement,

\[
\boxed{
\Delta_H^{(a)}\ln N_R
\longrightarrow
\Delta_h\ln N_R
}
\]

with the Laplace–Beltrami operator of the physicalized spatial metric after the coframe/gluing limit is admitted.

Because `u` is dimensionless,

\[
\boxed{[\Delta_hu]=L^{-2}.}
\]

For the RF-N0 relational potential,

\[
\boxed{
\Delta_h\Phi_R
=c^2\Delta_hu,
\qquad
[\Delta_h\Phi_R]=T^{-2}.
}
\]

## 5. Source functional is a separate gate

Introduce only the typed placeholder

\[
\boxed{
\Delta_hu=\mathcal S_R,
\qquad
[\mathcal S_R]=L^{-2}.
}
\]

This equation becomes a physical source law only after `S_R` is derived independently from admitted upstream matter/information/field variables. RF-N1 therefore separates:

```text
operator derivation   : PASS locally
source identification : OPEN
coupling normalization: OPEN
```

The already-derived temporal information curvature

\[
\Xi_I=\frac{\mathcal J_\pi}{\mathcal A_{\rm rel}},
\qquad [\Xi_I]=L^{-2},
\]

is dimensionally admissible as one independent source-basis candidate. The lowest-order analytic candidate expansion can therefore be written

\[
\boxed{
\mathcal S_R
=\beta_I\Xi_I
+\sum_r\beta_r\mathcal S_r
+O(\text{higher invariants}),
}
\]

with dimensionless coefficients when every `S_r` is separately typed as `L^-2`.

This expansion is a candidate basis, not a promoted source law. In particular `beta_I` is not fixed by RF-N0, RF-02H or IDT 01D.

## 6. Variational representation of a chosen source

For any independently admitted `S_R`, the elliptic balance has the local variational representation

\[
\boxed{
\mathcal E_N[u]
=\int_\Sigma\sqrt h\left[
\frac12h^{ij}\partial_i u\partial_j u
+\mathcal S_Ru
\right]d^3x.
}
\]

With fixed boundary/reference-clock normalization, variation with respect to `u` gives

\[
\boxed{
\Delta_hu=\mathcal S_R.
}
\]

The existence of this representation proves consistency of the operator with a local Dirichlet response. It does not derive `S_R`; the source term remains an independent admission gate.

## 7. Constructive source non-identifiability theorem

The present upstream package fixes `u`, its kinematic role, the hexahedral metric and the symmetric response operator, but does not yet fix a unique independent right-hand side. For example, each of

\[
\mathcal S_R=0,
\qquad
\mathcal S_R=\beta_I\Xi_I,
\qquad
\mathcal S_R=\beta_I\Xi_I+\beta_F\mathcal S_F
\]

is compatible with the current operator typing whenever the added scalar is independently `L^-2`. They produce different sourced lapse fields while preserving all already-proved RF-N0 kinematics.

Therefore the current premises do not identify a unique source functional or its normalization. In particular, the Newton constant is not determined by this gate.

## 8. Newton target audit

Using

\[
\Phi_R=c^2u,
\]

the derived operator form becomes

\[
\boxed{
\Delta_h\Phi_R=c^2\mathcal S_R.
}
\]

The Newton/Poisson target is reached only if an independent upstream derivation later yields

\[
\boxed{
c^2\mathcal S_R
\stackrel{\rm derived}{=}
4\pi G\rho_m
}
\]

in the weak, static, locally Euclidean limit. This equality is a validation target and is not used anywhere in the derivation above.

Thus RF-N1 has now split the Newton problem into two sharply different statements:

\[
\boxed{
\text{hexahedral/Onsager geometry}
\Rightarrow
\text{Laplacian operator}
}
\]

and

\[
\boxed{
\text{upstream source physics}
\stackrel{?}{\Rightarrow}
\mathcal S_R
\stackrel{?}{\longrightarrow}
4\pi G\rho_m/c^2.
}
\]

The first is locally derived here. The second remains the next source-identification gate.
