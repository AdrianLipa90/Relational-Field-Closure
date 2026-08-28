# RFG3 — Wilson-Loop Continuum and Yang–Mills Normalization Gate

Status: `CHYBA / CANDIDATE_ONLY / STANDARD_WILSON_SUBTHEOREM_EXACT / PROJECT_LINK_EMBEDDING_OPEN`

RFG3 advances RFG2 by testing whether the existing holonomic gluon links can enter the standard Wilson-lattice continuum map with an independently typed gauge coupling.

## 1. Existing project input

The holonomic gluon layer supplies `SU(3)` links and loop products

\[
W_{ij}\in SU(3),
\qquad
U_C=\prod_{(ij)\in C}W_{ij},
\]

with the gauge-invariant loop defect

\[
\boxed{
D_C:=3-\operatorname{Re}\operatorname{Tr}U_C.
}
\]

This is exactly three times the normalized `SU(3)` plaquette defect

\[
\boxed{
D_C=3\left(1-\frac13\operatorname{Re}\operatorname{Tr}U_C\right).
}
\]

## 2. Standard local link embedding

For a hypercubic local embedding with spacing `a`, define the nearest-neighbour link

\[
\boxed{
U_\mu(x)
=\exp\!\left[i g_0 a A_\mu^a(x)T^a\right],
}
\]

with fundamental `SU(3)` generators normalized by

\[
\operatorname{Tr}(T^aT^b)=\frac12\delta^{ab}.
\]

The elementary plaquette is

\[
U_{\mu\nu}(x)
=U_\mu(x)U_\nu(x+a\hat\mu)
 U_\mu^\dagger(x+a\hat\nu)U_\nu^\dagger(x).
\]

Its small-`a` expansion is

\[
\boxed{
U_{\mu\nu}(x)
=\exp\!\left[i g_0a^2F_{\mu\nu}(x)+O(a^3)\right].
}
\]

Thus the project link holonomy can reach a continuum Yang–Mills field-strength gate once its graph links are bound to this local plaquette geometry.

## 3. Wilson action normalization

For `SU(3)`, the standard Wilson gauge action is

\[
\boxed{
S_W
=\beta_W\sum_p
\left(1-\frac13\operatorname{Re}\operatorname{Tr}U_p\right),
}
\]

with

\[
\boxed{
\beta_W=\frac{6}{g_0^2}.
}
\]

Equivalently,

\[
\boxed{
g_0^2=\frac{6}{\beta_W}.}
\]

Using the project defect `D_p=3-ReTr(U_p)`,

\[
\boxed{
S_W=\frac{\beta_W}{3}\sum_pD_p.
}
\]

Hence the missing physical gauge-coupling coordinate is exactly the overall Wilson-action coefficient once the project loop is admitted as a standard plaquette.

## 4. Continuum curvature normalization

Expanding the plaquette with the stated generator normalization gives

\[
1-\frac13\operatorname{ReTr}U_{\mu\nu}
=\frac{g_0^2a^4}{12}
F_{\mu\nu}^aF_{\mu\nu}^a+O(a^6).
\]

With `beta_W=6/g_0^2`, the lattice action approaches the standard continuum Yang–Mills quadratic action after the lattice sum is converted to the spacetime integral.

This is the exact standard subtheorem consumed by the project embedding gate.

## 5. Injection into the RFG2 Newton-coupling candidate

RFG2 gives

\[
G_{DC}
=\frac{\Gamma_{DC}^2g_{YM}^4}{8\pi M_\star^2}
\]

for the self-copy candidate.

At the Wilson bare-coupling gate,

\[
g_{YM}^2\leftrightarrow g_0^2=\frac6{\beta_W}.
\]

Therefore

\[
\boxed{
G_{DC}
=\frac{9\Gamma_{DC}^2}
{2\pi\beta_W^2M_\star^2}.
}
\]

If the independent source-carrier scale candidate

\[
M_\star\stackrel{?}{=}\epsilon_N=\frac12D_\tau\chi
\]

also passes, then

\[
\boxed{
G_{cand}
=\frac{18\Gamma_{DC}^2}
{\pi\beta_W^2(D_\tau\chi)^2}.
}
\]

Thus the gluon→gravity candidate has been reduced to three explicit independently auditable coordinates:

\[
\boxed{
\beta_W,
\qquad
\Gamma_{DC},
\qquad
D_\tau\chi.
}
\]

## 6. Project embedding gates

Promotion requires:

1. identify project `W_ij` edges with local `U_mu(x)` links on an admitted four-dimensional plaquette complex;
2. recover the plaquette BCH expansion with the same generator convention;
3. derive or independently measure the coefficient `beta_W` multiplying the project loop defect;
4. verify the continuum Yang–Mills action normalization;
5. construct color–kinematics numerators and pass RFG2 matched-Jacobi tests;
6. bind the double-copy normalization `Gamma_DC`;
7. bind `M_star` to the source-carrier energy;
8. compare the resulting `G_cand` to the Newton source gate with all upstream coordinates frozen.

## 7. Executable defects

Use

\[
\Delta_{defect}
=\left|D_p-3\left(1-\frac13\ReTr U_p\right)\right|,
\]

\[
\Delta_{g}
=\left|g_0^2-\frac6{\beta_W}\right|,
\]

and, after a local link embedding exists,

\[
\Delta_{plaq}
=\left\|
\frac{\log U_{\mu\nu}}{ig_0a^2}-F_{\mu\nu}
\right\|.
\]

The Newton-level final defect remains

\[
\Delta_G
=\frac{|G_{Newton}-G_{cand}|}{G_{Newton}}.
\]

## 8. GREMLIN verdict

`CHYBA / CANDIDATE_ONLY`.

The Wilson subtheorem removes one ambiguity from the gluon↔gravity traversal: once the project loop coefficient `beta_W` is independently fixed, the bare Yang–Mills coupling is fixed by `g_0^2=6/beta_W`. The frontier is therefore the physical derivation of `beta_W` and the color–kinematics numerator gate.
