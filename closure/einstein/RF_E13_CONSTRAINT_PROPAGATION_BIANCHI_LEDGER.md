# RF-E13 — Constraint Propagation and Bianchi Source Ledger

Status: `ACTION_EVOLUTION_PROJECTION_AND_HOMOGENEOUS_CONSTRAINT_PROPAGATION_CANDIDATE`

## 1. Parent chain

RF-E13 consumes the already gated sequence

```text
RF-E3   metric variation of the stated Einstein-Hilbert + matter action
RF-E8   ADM kinematic assembly
RF-E9   extrinsic-curvature convention
RF-E10  Gauss-Codazzi geometric projections
RF-E11  matter projection typing
RF-E12  action-projected Hamiltonian/momentum source constraints
```

with signature `(-,+,+,+)`, length-valued temporal coordinate `x^0=ct`, lapse `N>0`, shift `b^i`, and

\[
K_{ij}=-\frac12\mathcal L_n h_{ij}.
\]

## 2. Metric evolution identity

The RF-E9 definition gives directly

\[
\boxed{
(\partial_0-\mathcal L_b)h_{ij}=-2NK_{ij}.
}
\]

For a spatial covariant two-tensor,

\[
(\mathcal L_bK)_{ij}
=b^kD_kK_{ij}
+K_{ik}D_jb^k
+K_{kj}D_ib^k.
\]

This equation is kinematic and precedes the dynamical spatial projection.

## 3. Spatial action projection

Projecting the RF-E3 stationary metric equation tangentially to the slice and using the RF-E9 convention gives

\[
\boxed{
(\partial_0-\mathcal L_b)K_{ij}
=-D_iD_jN
+N\left({}^{(3)}R_{ij}+KK_{ij}-2K_{ik}K^k{}_j\right)
+N\kappa_E\left[\frac12h_{ij}(S-\rho_n)-S_{ij}\right].
}
\]

Here RF-E11 supplies

\[
\rho_n=T_{\mu\nu}n^\mu n^\nu,
\qquad
S_{ij}=h_i{}^\mu h_j{}^\nu T_{\mu\nu},
\qquad
S=h^{ij}S_{ij}.
\]

This is the spatial evolution equation associated with the same action whose normal and mixed projections produced RF-E12.

## 4. Dynamic-Lambda branch

For the RF-E3 metric equation

\[
G_{\mu\nu}+\Lambda_0g_{\mu\nu}=\kappa_ET_{\mu\nu},
\]

the spatial evolution equation gains

\[
\boxed{-N\Lambda_0h_{ij}}
\]

on the right-hand side:

\[
\boxed{
(\partial_0-\mathcal L_b)K_{ij}
=-D_iD_jN
+N\left({}^{(3)}R_{ij}+KK_{ij}-2K_{ik}K^k{}_j\right)
+N\kappa_E\left[\frac12h_{ij}(S-\rho_n)-S_{ij}\right]
-N\Lambda_0h_{ij}.
}
\]

The independent scalar dynamics of `Lambda0` remain governed by the Lambda-sector action gates.

## 5. Constraint residuals

Define the base action residuals

\[
\boxed{
\mathcal H
:={}^{(3)}R+K^2-K_{ij}K^{ij}-2\kappa_E\rho_n,
}
\]

\[
\boxed{
\mathcal M_i
:=D_jK^j{}_i-D_iK-\kappa_Ej_i.
}
\]

RF-E10/RF-E11 imply that these are precisely the normal and mixed projections of the four-dimensional Euler-Lagrange residual tensor

\[
E_{\mu\nu}:=G_{\mu\nu}-\kappa_ET_{\mu\nu}:
\]

\[
\boxed{
\mathcal H=2E_{\mu\nu}n^\mu n^\nu,
\qquad
\mathcal M_i=-h_i{}^\mu n^\nu E_{\mu\nu}.
}
\]

For the dynamic-Lambda branch define instead

\[
E^{\Lambda}_{\mu\nu}
:=G_{\mu\nu}+\Lambda_0g_{\mu\nu}-\kappa_ET_{\mu\nu},
\]

and

\[
\boxed{
\mathcal H_{\Lambda}
:={}^{(3)}R+K^2-K_{ij}K^{ij}-2\Lambda_0-2\kappa_E\rho_n.
}
\]

The momentum residual is unchanged.

## 6. Bianchi source ledger

The contracted Bianchi identity gives

\[
\boxed{\nabla^\mu G_{\mu\nu}=0.}
\]

For constant coupling and the base matter ledger,

\[
\boxed{\nabla^\mu T_{\mu\nu}=0,}
\]

so

\[
\boxed{\nabla^\mu E_{\mu\nu}=0.}
\]

For the dynamic-Lambda branch, RF-E3/RF-L2 record the exchange law

\[
\boxed{
\kappa_E\nabla^\mu T_{\mu\nu}=\nabla_\nu\Lambda_0.
}
\]

Therefore

\[
\begin{aligned}
\nabla^\mu E^{\Lambda}_{\mu\nu}
&=\nabla^\mu G_{\mu\nu}
+\nabla_\nu\Lambda_0
-\kappa_E\nabla^\mu T_{\mu\nu}\\
&=0,
\end{aligned}
\]

hence

\[
\boxed{\nabla^\mu E^{\Lambda}_{\mu\nu}=0.}
\]

The Lambda exchange ledger is therefore exactly the compatibility condition needed by the Bianchi identity.

## 7. Homogeneous constraint propagation

Assume the spatial evolution projection of the same residual tensor is satisfied,

\[
\boxed{h_i{}^\mu h_j{}^\nu E_{\mu\nu}=0}
\]

for the base branch, or its `E^Lambda` analogue for the dynamic-Lambda branch.

The 3+1 decomposition of the divergence identity then gives the standard homogeneous ADM propagation system for the residuals:

\[
\boxed{
(\partial_0-\mathcal L_b)\mathcal H
=2NK\mathcal H
-2N D_i\mathcal M^i
-4\mathcal M^iD_iN,
}
\]

\[
\boxed{
(\partial_0-\mathcal L_b)\mathcal M_i
=-\frac12N D_i\mathcal H
-\mathcal H D_iN
+NK\mathcal M_i.
}
\]

For the covector `M_i`,

\[
(\mathcal L_b\mathcal M)_i
=b^jD_j\mathcal M_i
+\mathcal M_jD_ib^j.
\]

The same homogeneous equations hold with `H -> H_Lambda` when the Lambda exchange law above is satisfied.

## 8. Zero-residual invariance theorem

The propagation system is homogeneous in `H` and `M_i`. Therefore

\[
\boxed{
\mathcal H=0,
\qquad
\mathcal M_i=0
}
\]

is an exact solution of the propagation equations.

Under the ordinary local uniqueness assumptions for the ADM evolution problem, initial data satisfying the constraints and evolved with the same action equations/source ledger remain on the zero-residual constraint surface for as long as that evolution solution exists.

This is the constraint-propagation closure required after RF-E12.

## 9. Principal flat control

For

\[
N=1,
\qquad
b^i=0,
\qquad
K=0,
\]

the principal system becomes

\[
\boxed{
\partial_0\mathcal H=-2D_i\mathcal M^i,
\qquad
\partial_0\mathcal M_i=-\frac12D_i\mathcal H.
}
\]

Taking one more temporal derivative gives

\[
\boxed{
\partial_0^2\mathcal H=D_iD^i\mathcal H
}
\]

and analogously for the longitudinal momentum-constraint mode. Thus the principal constraint residual propagates rather than acquiring an inhomogeneous source term.

## 10. Action-level ADM closure ledger

The current RFC action/ADM branch is now typed as

```text
RF-E3 stated EH + matter action
 -> metric variation
 -> full tensor Euler-Lagrange equation
 -> RF-E8 ADM metric
 -> RF-E9 K_ij
 -> RF-E10 geometric normal/mixed projections
 -> RF-E11 matter normal/mixed projections
 -> RF-E12 source constraints
 -> RF-E13 spatial evolution projection
 -> Bianchi + source conservation/exchange
 -> homogeneous constraint propagation
```

The project-derived physical value of `kappa_E` remains controlled by the RF-E3 double-copy normalization gates.

The TIR/IDT first-principles programme still owns the upstream derivation/source-binding questions for the spacetime carriers and project coupling coordinates.

## 11. Claim ledger

| Statement | Status |
|---|---|
| metric evolution from `K_ij` definition | EXACT KINEMATICS |
| spatial `K_ij` evolution from RF-E3 action equation | EXACT ACTION PROJECTION |
| matter coefficient/sign | EXACT UNDER RF-E11 CONVENTION |
| dynamic-Lambda `-N Lambda0 h_ij` term | EXACT ACTION PROJECTION |
| residual projection identities | EXACT COMPOSITION |
| base Bianchi source ledger | EXACT |
| dynamic-Lambda exchange cancellation | EXACT |
| homogeneous ADM constraint-propagation equations | EXACT UNDER STATED EVOLUTION/SOURCE LEDGER |
| zero-residual invariance | EXACT LOCAL PROPAGATION CONSEQUENCE |
| local uniqueness extension along a regular evolution | STANDARD PDE CONDITIONAL |
| physical project-derived `kappa_E` | CONDITIONAL RF-E3 GATES |
| TIR/IDT upstream carrier derivation | CROSS-REPO FRONTIER |

Validation target:

`PASS_RF_E13_CONSTRAINT_PROPAGATION_BIANCHI_LEDGER`.
