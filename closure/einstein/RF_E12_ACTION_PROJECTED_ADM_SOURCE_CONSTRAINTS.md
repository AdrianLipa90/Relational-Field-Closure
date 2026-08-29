# RF-E12 — Action-Projected ADM Source Constraints

Status: `EXACT_ACTION_PROJECTION_COMPOSITION / PROJECT_COUPLING_VALUE_CONDITIONAL`

## 1. Parent theorem chain

RF-E12 composes three independently gated RFC surfaces:

```text
RF-E3   Einstein-Hilbert action normalization and metric variation
RF-E10  Gauss-Codazzi geometric Einstein-tensor projections
RF-E11  foliation decomposition of the admitted matter tensor
```

RF-E3 fixes, on its stated action convention,

\[
S_{EH}[g]
=\frac{1}{2\kappa_E}\int d^4x\sqrt{-g}\,R,
\]

with matter definition

\[
T_{\mu\nu}
=-\frac{2}{\sqrt{-g}}
\frac{\delta S_m}{\delta g^{\mu\nu}}.
\]

After the standard gravitational boundary term is handled, stationarity of

\[
S_{EH}+S_m
\]

gives

\[
\boxed{G_{\mu\nu}=\kappa_E T_{\mu\nu}.}
\]

RF-E12 does not introduce this tensor equation independently; it consumes the already-recorded RF-E3 metric-variation result and projects it onto the now independently derived RF-E10/RF-E11 carriers.

## 2. Normal-normal action projection

RF-E10 gives

\[
\boxed{
\mathcal G_H
:={} ^{(3)}R+K^2-K_{ij}K^{ij}
=2G_{\mu\nu}n^\mu n^\nu.
}
\]

RF-E11 gives

\[
\boxed{
\rho_n=T_{\mu\nu}n^\mu n^\nu.
}
\]

Projecting the RF-E3 stationary metric equation twice along the unit normal therefore yields

\[
\boxed{
\mathcal G_H=2\kappa_E\rho_n.
}
\]

Equivalently,

\[
\boxed{
{} ^{(3)}R+K^2-K_{ij}K^{ij}
=2\kappa_E\rho_n.
}
\]

This is the action-projected Hamiltonian source constraint on the admitted foliation.

## 3. Mixed action projection

RF-E10 fixes the sign-typed geometric momentum carrier

\[
\boxed{
\mathcal G_{Mi}
:=D_jK^j{}_i-D_iK
=-h_i{}^\mu n^\nu G_{\mu\nu}.
}
\]

RF-E11 fixes

\[
\boxed{
j_i=-h_i{}^\mu n^\nu T_{\mu\nu}.}
\]

Applying the same mixed projection to the RF-E3 stationary metric equation gives

\[
\boxed{
\mathcal G_{Mi}=\kappa_E j_i.
}
\]

Hence

\[
\boxed{
D_jK^j{}_i-D_iK
=\kappa_Ej_i.
}
\]

The sign follows from the already-gated definitions on both sides rather than from a new convention introduced here.

## 4. Dynamic-Lambda action branch

RF-E3 also records the action coordinate

\[
S_{g,\Lambda}
=\frac{1}{2\kappa_E}
\int d^4x\sqrt{-g}\,[R-2\Lambda_0(x)]
\]

with metric-side equation at fixed scalar coordinate

\[
G_{\mu\nu}+\Lambda_0g_{\mu\nu}
=\kappa_ET_{\mu\nu}.
\]

The normal-normal projection uses

\[
g_{\mu\nu}n^\mu n^\nu=-1,
\]

so

\[
\boxed{
\mathcal G_H-2\Lambda_0
=2\kappa_E\rho_n.
}
\]

Equivalently,

\[
\boxed{
\mathcal G_H
=2\Lambda_0+2\kappa_E\rho_n.
}
\]

The mixed projection of the metric term vanishes,

\[
h_i{}^\mu n^\nu g_{\mu\nu}=0,
\]

therefore

\[
\boxed{
\mathcal G_{Mi}=\kappa_Ej_i
}
\]

is unchanged by the `Lambda0` metric term.

The independent dynamics and physical promotion of `Lambda0` retain the gates already assigned by the RFC Lambda sector.

## 5. Coupling normalization hierarchy

RF-E3 carries the exact algebraic normalization triangle

\[
\boxed{
\kappa_g^2=4\kappa_E=32\pi G
}
\]

in natural units and

\[
\boxed{
\frac{2}{\kappa_g^2}
=\frac{1}{2\kappa_E}
=\frac{1}{16\pi G}.
}
\]

Thus, once a value of `kappa_E` is admitted, the action projection into the ADM source constraints uses exactly that same coupling coordinate.

The project-side candidate

\[
\kappa_E^{DC}
=\frac{4\Gamma_{DC}^2g_{YM}^4}{\omega_Q^2}
=\frac{144\Gamma_{DC}^2}{\beta_W^2\omega_Q^2}
\]

retains the physical gates listed in RF-E3: double-copy normalization, carrier-scale binding, source/matter binding and cross-system Newton universality.

Therefore RF-E12 separates two statuses:

```text
EH action metric variation -> tensor equation -> ADM projections    EXACT ON STATED ACTION
project-derived numerical/physical kappa_E                          CONDITIONAL GATE
```

The author/repository/formalism/code may suggest a complete project-derived normalization of the ADM source constraints from the gauge/double-copy line, yet does not state that physical promotion as an established result until the RF-E3 coupling gates pass with frozen provenance.

## 6. Constraint-source linearity

RF-E11 proves linearity of matter projections. Therefore for

\[
T_{\mu\nu}=\sum_A T^{(A)}_{\mu\nu},
\]

one has

\[
\rho_n=\sum_A\rho_n^{(A)},
\qquad
j_i=\sum_Aj_i^{(A)}.
\]

The projected action equations become

\[
\boxed{
\mathcal G_H
=2\kappa_E\sum_A\rho_n^{(A)}
}
\]

and

\[
\boxed{
\mathcal G_{Mi}
=\kappa_E\sum_Aj_i^{(A)}.
}
\]

This preserves the source bookkeeping already established by RF-E6/RF-E7.

## 7. Dimensional firewall

RF-E10 gives

\[
[\mathcal G_H]=[\mathcal G_{Mi}]=L^{-2}.
\]

In SI units RF-E3 gives

\[
\boxed{\kappa_E=\frac{8\pi G}{c^4}.}
\]

Hence the stress-energy projections carry the corresponding SI energy-density/momentum-density dimensions required for `kappa_E T` to have curvature dimension.

The dimensional gate concerns the common tensor coupling and does not identify RFC information-curvature coefficients with stress-energy dimensions without their own source maps.

## 8. Constraint propagation frontier

RF-E12 closes the instantaneous source-constraint composition on a slice. The next closure question is propagation:

```text
initial G_H - 2 kappa_E rho_n = 0
initial G_Mi - kappa_E j_i = 0
 + geometric evolution equations
 + matter/source evolution
 + Bianchi identity / source conservation ledger
 -> constraints remain zero on subsequent slices ?
```

This is assigned to RF-E13.

For the dynamic-Lambda branch, the propagation ledger must use the already recorded exchange law

\[
\kappa_E\nabla^\mu T_{\mu\nu}
=\nabla_\nu\Lambda_0.
\]

## 9. Claim ledger

| Statement | Status |
|---|---|
| RF-E3 metric variation of stated EH+matter action | PARENT EXACT |
| RF-E10 geometric projections | PARENT EXACT |
| RF-E11 matter projections | PARENT EXACT |
| `G_H=2 kappa_E rho_n` | EXACT COMPOSITION OF PARENT THEOREMS |
| `G_Mi=kappa_E j_i` | EXACT COMPOSITION OF PARENT THEOREMS |
| dynamic-Lambda `G_H-2Lambda0=2kappa_E rho_n` | EXACT ACTION PROJECTION |
| dynamic-Lambda mixed projection unchanged | EXACT |
| sectorwise source linearity | EXACT |
| `kappa_g^2=4kappa_E` coefficient transfer | PARENT EXACT ALGEBRA |
| physical project-side value of `kappa_E` | CONDITIONAL RF-E3 GATES |
| constraint propagation | NEXT GATE |
| full physical Einstein closure | DOWNSTREAM FINAL GATE |

Validation target:

`PASS_RF_E12_ACTION_PROJECTED_ADM_SOURCE_CONSTRAINTS`.
