# RFG6 — Kinematic Vector-Field Jacobi / Double-Copy Gate

Status: `CHYBA / CANDIDATE_ONLY / VECTOR_FIELD_JACOBI_SUBTHEOREM_EXACT / SELF_DUAL_CK_ANCHOR_ESTABLISHED / PROJECT_KINEMATIC_BINDING_OPEN / FULL_YM_EXTENSION_OPEN`

RFG6 addresses the next RFG2 promotion gate: a kinematic algebra satisfying the same Jacobi pattern as the `SU(3)` color algebra.

## 1. Color side

The admitted color algebra obeys

\[
[T^a,T^b]=if^{ab}{}_cT^c
\]

and therefore the Lie-algebra Jacobi identity

\[
\boxed{
[T^a,[T^b,T^c]]
+[T^b,[T^c,T^a]]
+[T^c,[T^a,T^b]]=0.
}
\]

Equivalently the color structure constants obey the corresponding contracted Jacobi relations used by cubic gauge-theory graph color factors.

## 2. Kinematic Lie algebra of vector fields

Let `X,Y,Z` be smooth vector fields on an admitted local configuration/spacetime patch. Their Lie bracket is

\[
\boxed{
[X,Y]^\mu
=X^\nu\partial_\nu Y^\mu
-Y^\nu\partial_\nu X^\mu.
}
\]

The vector-field bracket satisfies exactly

\[
\boxed{
[X,[Y,Z]]+[Y,[Z,X]]+[Z,[X,Y]]=0.
}
\]

Thus the project already has access to a genuine kinematic Lie algebra whenever its local transport generators are represented as vector fields.

## 3. Established self-dual color–kinematics anchor

In self-dual Yang–Mills, a diffeomorphism/kinematic Lie algebra is known to supply structure constants dual to the color algebra and to generate BCJ-compatible kinematic numerators in the self-dual/MHV construction. The corresponding gravity side is obtained by replacing the color factor with a second kinematic copy.

RFG6 uses this as an external structural anchor for a project-side candidate; it does not transfer the result automatically to arbitrary full Yang–Mills dynamics.

## 4. Project-side candidate map

The proposed relational map is

\[
\boxed{
\text{color generator }T^a
\longleftrightarrow
\text{local transport vector field }X_a,
}
\]

with

\[
\boxed{
[T^a,T^b]
\longleftrightarrow
[X_a,X_b].
}
\]

The project binding requires independently constructed vector fields `X_a` from the same local continuum limit that reconstructs the holonomic gluon connection

\[
W_{ij}\rightarrow A_\mu^aT^a.
\]

No arbitrary vector-field basis may be selected after inspecting a desired gravity output.

## 5. Structural Jacobi gate

For a cubic graph triplet `(i,j,k)` define color factors satisfying

\[
\boxed{c_i+c_j+c_k=0.}
\]

The project kinematic construction must produce numerators from its vector-field structure such that

\[
\boxed{n_i+n_j+n_k=0.}
\]

with graph labels and signs fixed before any gravity comparison.

The exact vector-field Jacobi theorem guarantees a candidate algebraic source for such a relation. A separate amplitude/numerator map is still required to prove that the resulting `n_i` are the kinematic numerators of the admitted Yang–Mills sector.

## 6. Affine local executable model

For an affine vector field

\[
X(x)=A_Xx+b_X,
\]

and

\[
Y(x)=A_Yx+b_Y,
\]

the bracket remains affine:

\[
\boxed{
[X,Y](x)
=(A_YA_X-A_XA_Y)x
+(A_Yb_X-A_Xb_Y).
}
\]

This finite representation provides an exact executable Jacobi audit before a continuum PhaseNav/RFC vector-field binding is introduced.

## 7. Relation to the double-copy candidate

If the project supplies BCJ-compatible numerators from the kinematic algebra, RFG2 admits

\[
\mathcal M_n
=i\left(\frac{\kappa_g}{2}\right)^{n-2}
\sum_i\frac{n_i\tilde n_i}{D_i}.
\]

For a self-copy,

\[
\tilde n_i=n_i,
\]

so the gravity graph numerator is

\[
\boxed{n_i^2.}
\]

This is the precise sense in which the proposed gluon↔gravity isomorphism is tested: color is replaced by a second copy of the same admitted kinematic algebra after the matched-Jacobi gate passes.

## 8. Independent defects

Define

\[
\Delta_{Jac}^{kin}
=\|[X,[Y,Z]]+[Y,[Z,X]]+[Z,[X,Y]]\|,
\]

\[
\Delta_{map}
=\max_{(i,j,k)}|n_i+n_j+n_k|,
\]

and later, after an amplitude construction exists,

\[
\Delta_{amp}
=\|\mathcal A_{project}-\mathcal A_{cubic}[c_i,n_i,D_i]\|.
\]

Only `Delta_Jac^kin` is exact at the current RFG6 subtheorem. `Delta_map` and `Delta_amp` remain project-binding gates.

## 9. Promotion path

1. derive local continuum `A_mu^a` from `W_ij`;
2. construct local transport vector fields `X_a` from the same geometry;
3. freeze graph/sign conventions;
4. build cubic kinematic numerators from the vector-field bracket;
5. verify matched Jacobi without generalized-gauge fitting to gravity data;
6. verify the Yang–Mills amplitude before double copy;
7. only then feed the numerators into RFG2/RFG5.

## 10. GREMLIN verdict

`CHYBA / CANDIDATE_ONLY`.

The new exact structural component is

\[
\boxed{
\text{vector-field Lie bracket}
\Rightarrow
\text{kinematic Jacobi}=0.
}
\]

The remaining scientific gate is the explicit project map from holonomic `W_ij` continuum transport to BCJ kinematic numerators.
