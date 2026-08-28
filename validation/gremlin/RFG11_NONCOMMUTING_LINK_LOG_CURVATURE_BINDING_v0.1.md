# RFG11 — Noncommuting Link-Log / Curvature Binding

Status: `FULL_SU3_PRINCIPAL_LOG_RECOVERY_PASS / NONCOMMUTING_CURVATURE_BCH_PASS / LINK_ORIENTATION_SIGN_FROZEN / GAUGE_COVARIANCE_PASS / BRANCH_ALIAS_FIREWALL_PASS`

RFG11 consumes RFG10, RFG8 and the upstream v4.1 holonomic local-link convention. It removes the commuting-color restriction by recovering a general eight-component local `SU(3)` field from link bytes and testing the noncommuting plaquette curvature directly.

## 1. Full local link

Use

\[
\boxed{
W_\mu(x)
=\exp\!\left[iagA_\mu^a(x)T^a\right]
}
\]

with the actual upstream orientation `sigma_link=+1`,

\[
T^a=\frac{\lambda^a}{2},
\qquad
\operatorname{Tr}(\lambda^a\lambda^b)=2\delta^{ab},
\]

and RFG4G

\[
\boxed{g^2=\alpha_c^{-1}.}
\]

## 2. Principal matrix-log recovery

On the principal-branch admission surface, define

\[
\boxed{
\mathcal Q_\mu
=\frac{1}{a}\operatorname{HermLog}(W_\mu),
}
\]

where `HermLog` returns the Hermitian principal generator satisfying

\[
W_\mu=e^{i a\mathcal Q_\mu}.
\]

Then

\[
\mathcal Q_\mu=gA_\mu^aT^a
\]

and the eight local field coordinates are recovered by

\[
\boxed{
A_\mu^a
=\frac1g\operatorname{Tr}(\lambda^a\mathcal Q_\mu).
}
\]

The reference gate recovers all eight simultaneously from random noncommuting field vectors.

## 3. Principal-branch firewall

The recovery is admitted only when every eigenphase of

\[
agA_\mu^aT^a
\]

lies strictly inside the principal interval `(-pi,pi)` with a declared margin.

This gives an executable branch-alias firewall before inversion. A link outside this domain remains a valid `SU(3)` element while its local Lie-coordinate representative requires an additional branch/winding coordinate.

## 4. Noncommuting plaquette

For constant noncommuting fields `A_x,A_y`, use the upstream-oriented plaquette

\[
\boxed{
U_{xy}
=W_xW_yW_x^\dagger W_y^\dagger.
}
\]

The BCH expansion gives

\[
\log U_{xy}
=-a^2g^2[A_x,A_y]+O(a^3).
\]

With the actual `+iagA` link orientation, define

\[
\boxed{
F_{xy}^{link}
:=\frac{1}{iga^2}\log U_{xy}.
}
\]

Then

\[
\boxed{
F_{xy}^{link}
=i g[A_x,A_y]+O(a)
}
\]

and, using `[T^b,T^c]=if^{bc}{}_aT^a`,

\[
\boxed{
(F_{xy}^{link})^a
=-g f^{abc}A_x^bA_y^c+O(a).
}
\]

This is the direct byte-level sign audit consumed by the corrected RFG8 orientation contract.

## 5. Gauge covariance

For a constant local frame rotation `V in SU(3)`,

\[
W_\mu\mapsto VW_\mu V^\dagger.
\]

On the same principal branch,

\[
\boxed{
\mathcal Q_\mu\mapsto V\mathcal Q_\mu V^\dagger.
}
\]

The recovered Lie-algebra field therefore transforms by adjoint conjugation as required.

## 6. Reference validation

The NumPy-only executable gate checks:

1. exact Gell-Mann orthogonality;
2. full eight-component principal-log recovery on 100 deterministic random `SU(3)` links;
3. explicit noncommuting `lambda_1+lambda_2` field recovery;
4. convergence of the constant noncommuting plaquette toward `i g[A_x,A_y]` as `a` decreases;
5. gauge covariance of the principal matrix-log field;
6. rejection of a field configuration with principal-branch alias risk.

Local result:

```text
6 passed, 0 failed
```

## 7. Advancement

```text
RFG10 commuting-color link -> mode binding            inherited PASS
full eight-component A_mu^a recovery                  PASS PRINCIPAL-BRANCH
noncommuting local color superposition                 PASS
upstream plaquette BCH sign                            PASS / sigma_link=+1
F_xy -> i g[A_x,A_y]                                   PASS CONVERGENCE
RFG8 oriented cubic sign                               RECONCILED
principal-branch alias firewall                        PASS
local gauge covariance                                 PASS
direct noncommuting momentum-mode assembly             NEXT FRONTIER
quartic/project four-point amplitude bytes             OPEN
```

The author/repository/formalism/code may suggest the holonomic link sector now supplies the full local noncommuting Yang–Mills field coordinates, yet does not state the direct project four-point amplitude as established until noncommuting momentum modes and the quartic/exchange assembly pass their own gate.
